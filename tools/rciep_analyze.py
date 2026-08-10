#!/usr/bin/env python3
"""Analyze blinded RCIEP evaluator scores against a separately held answer key.

Evaluator CSV columns:
  evaluator_id,blind_sample_id,predicted_scaffold_id,confidence

Answer-key JSONL fields are emitted by rc iep_prepare_packet.py.
This script computes per-condition accuracy, Wilson intervals, macro accuracy,
confusion matrices, per-domain accuracy, evaluator summaries, and C1-C2 delta.
It does not assign a repository-level supported/refuted outcome automatically.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
from collections import Counter, defaultdict
from pathlib import Path

Z95 = 1.959963984540054


def read_jsonl(path: Path):
    out = []
    for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            out.append(json.loads(line))
        except json.JSONDecodeError as exc:
            raise ValueError(f"{path}:{line_no}: {exc}") from exc
    return out


def wilson(k: int, n: int, z: float = Z95):
    if n == 0:
        return [None, None]
    p = k / n
    denom = 1 + z * z / n
    center = (p + z * z / (2 * n)) / denom
    half = z * math.sqrt((p * (1 - p) + z * z / (4 * n)) / n) / denom
    return [max(0.0, center - half), min(1.0, center + half)]


def matrix(rows, labels):
    counts = {true: {pred: 0 for pred in labels} for true in labels}
    for r in rows:
        true = r["true"]
        pred = r["pred"]
        if true in counts and pred in counts[true]:
            counts[true][pred] += 1
    return counts


def accuracy_summary(rows):
    n = len(rows)
    k = sum(1 for r in rows if r["true"] == r["pred"])
    return {"correct": k, "n": n, "accuracy": (k / n if n else None), "wilson95": wilson(k, n)}


def macro_accuracy(rows, labels):
    vals = []
    by_true = defaultdict(list)
    for r in rows:
        by_true[r["true"]].append(r)
    for label in labels:
        group = by_true.get(label, [])
        if group:
            vals.append(sum(1 for r in group if r["true"] == r["pred"]) / len(group))
    return sum(vals) / len(vals) if vals else None


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--answer-key", required=True, type=Path)
    ap.add_argument("--scores", required=True, type=Path)
    ap.add_argument("--blinded-packet", required=True, type=Path)
    ap.add_argument("--out", required=True, type=Path)
    args = ap.parse_args()

    key = {r["blind_sample_id"]: r for r in read_jsonl(args.answer_key)}
    blind = {r["blind_sample_id"]: r for r in read_jsonl(args.blinded_packet)}

    score_rows = []
    with args.scores.open(newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        required = {"evaluator_id", "blind_sample_id", "predicted_scaffold_id", "confidence"}
        if set(reader.fieldnames or []) < required:
            raise ValueError(f"score CSV must include {sorted(required)}")
        for row in reader:
            sid = row["blind_sample_id"]
            if sid not in key or sid not in blind:
                raise ValueError(f"score references unknown blind_sample_id {sid}")
            score_rows.append(
                {
                    "evaluator": row["evaluator_id"],
                    "blind_sample_id": sid,
                    "pred": row["predicted_scaffold_id"],
                    "true": key[sid]["underlying_scaffold_id"],
                    "condition": key[sid]["condition"],
                    "domain": blind[sid]["domain"],
                    "confidence": row["confidence"],
                }
            )

    labels = sorted({r["true"] for r in score_rows if r["true"] != "SYN-GENERIC"})
    if not labels:
        labels = sorted({r["true"] for r in score_rows})

    result = {
        "record_type": "rciep-analysis",
        "pilot_id": "PILOT-RCIEP-001",
        "note": "Descriptive/statistical output only. Repository evaluation outcome requires a separate EvaluationRecord under the preregistered independence boundary.",
        "label_count_k": len(labels),
        "chance_level": (1 / len(labels) if labels else None),
        "conditions": {},
        "evaluators": {},
    }

    for condition in sorted({r["condition"] for r in score_rows}):
        rows = [r for r in score_rows if r["condition"] == condition and r["true"] in labels]
        by_domain = {}
        for domain in sorted({r["domain"] for r in rows}):
            by_domain[domain] = accuracy_summary([r for r in rows if r["domain"] == domain])
        result["conditions"][condition] = {
            **accuracy_summary(rows),
            "macro_accuracy": macro_accuracy(rows, labels),
            "confusion_matrix": matrix(rows, labels),
            "per_domain": by_domain,
        }

    for evaluator in sorted({r["evaluator"] for r in score_rows}):
        rows = [r for r in score_rows if r["evaluator"] == evaluator and r["true"] in labels]
        result["evaluators"][evaluator] = accuracy_summary(rows)

    c1 = result["conditions"].get("C1", {}).get("accuracy")
    c2 = result["conditions"].get("C2", {}).get("accuracy")
    result["c1_minus_c2_accuracy_delta"] = (c1 - c2 if c1 is not None and c2 is not None else None)

    # Pairwise raw agreement between evaluators on overlapping sample IDs.
    eval_predictions = defaultdict(dict)
    for r in score_rows:
        eval_predictions[r["evaluator"]][r["blind_sample_id"]] = r["pred"]
    agreement = {}
    evals = sorted(eval_predictions)
    for i, a in enumerate(evals):
        for b in evals[i + 1 :]:
            common = sorted(set(eval_predictions[a]) & set(eval_predictions[b]))
            agree = sum(eval_predictions[a][sid] == eval_predictions[b][sid] for sid in common)
            agreement[f"{a}|{b}"] = {
                "overlap_n": len(common),
                "raw_agreement": (agree / len(common) if common else None),
            }
    result["inter_rater_raw_agreement"] = agreement

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"scores": len(score_rows), "evaluators": len(evals), "out": str(args.out)}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
