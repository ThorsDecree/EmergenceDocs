#!/usr/bin/env python3
"""Prepare blinded RCIEP sample and answer-key packets from generation JSONL.

Expected input record fields:
  sample_id, prompt_id, domain, condition, underlying_scaffold_id,
  display_label, text, source_id, generation_receipt_id

This tool does not generate model outputs or evaluate claims. It performs a
predeclared leak-removal pass, records exclusions, deterministically shuffles
eligible samples, and writes evaluator-facing and answer-key files separately.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import random
import re
from pathlib import Path

REQUIRED = {
    "sample_id",
    "prompt_id",
    "domain",
    "condition",
    "underlying_scaffold_id",
    "display_label",
    "text",
    "source_id",
    "generation_receipt_id",
}


def read_jsonl(path: Path):
    for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        obj = json.loads(line)
        missing = REQUIRED - obj.keys()
        if missing:
            raise ValueError(f"{path}:{line_no}: missing fields {sorted(missing)}")
        yield obj


def load_scaffold_names(path: Path) -> list[str]:
    data = json.loads(path.read_text(encoding="utf-8"))
    names = []
    for item in data.get("scaffolds", []):
        name = str(item.get("canonical_name", "")).strip()
        if name and name.lower() != "generic":
            names.append(name)
    return names


def redact_literal_leaks(text: str, forbidden: list[str]) -> tuple[str, list[str]]:
    redacted = text
    hits: list[str] = []
    for token in forbidden:
        pattern = re.compile(rf"\b{re.escape(token)}\b", flags=re.IGNORECASE)
        if pattern.search(redacted):
            hits.append(token)
            redacted = pattern.sub("[IDENTITY-LABEL-REMOVED]", redacted)
    return redacted, hits


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True, type=Path)
    ap.add_argument("--scaffolds", required=True, type=Path)
    ap.add_argument("--blinded-out", required=True, type=Path)
    ap.add_argument("--answer-key-out", required=True, type=Path)
    ap.add_argument("--exclusions-out", required=True, type=Path)
    ap.add_argument("--shuffle-seed", required=True, type=int)
    ap.add_argument(
        "--forbidden-title",
        action="append",
        default=[],
        help="Literal source/document title to remove before evaluator exposure; repeatable.",
    )
    args = ap.parse_args()

    forbidden = load_scaffold_names(args.scaffolds) + list(args.forbidden_title)
    eligible = []
    exclusions = []

    for rec in read_jsonl(args.input):
        cleaned, hits = redact_literal_leaks(str(rec["text"]), forbidden)
        # The preregistered rule says exclude/regenerate when a literal identity name
        # or unambiguous source title appears after the predefined leak-removal pass.
        residual_hits = []
        for token in forbidden:
            if re.search(rf"\b{re.escape(token)}\b", cleaned, flags=re.IGNORECASE):
                residual_hits.append(token)
        if residual_hits:
            exclusions.append(
                {
                    "sample_id": rec["sample_id"],
                    "reason": "residual-literal-leak-after-removal",
                    "residual_hits": residual_hits,
                    "action": "regenerate-one-for-one-under-same-condition-and-prompt",
                }
            )
            continue

        eligible.append(
            {
                **rec,
                "cleaned_text": cleaned,
                "removed_literal_leaks": hits,
                "cleaned_text_sha256": sha256_text(cleaned),
            }
        )

    rng = random.Random(args.shuffle_seed)
    rng.shuffle(eligible)

    blinded_lines = []
    key_lines = []
    for idx, rec in enumerate(eligible, 1):
        blind_id = f"BLIND-{idx:05d}"
        blinded_lines.append(
            json.dumps(
                {
                    "blind_sample_id": blind_id,
                    "prompt_id": rec["prompt_id"],
                    "domain": rec["domain"],
                    "text": rec["cleaned_text"],
                    "text_sha256": rec["cleaned_text_sha256"],
                },
                ensure_ascii=False,
                sort_keys=True,
            )
        )
        key_lines.append(
            json.dumps(
                {
                    "blind_sample_id": blind_id,
                    "sample_id": rec["sample_id"],
                    "condition": rec["condition"],
                    "underlying_scaffold_id": rec["underlying_scaffold_id"],
                    "display_label": rec["display_label"],
                    "source_id": rec["source_id"],
                    "generation_receipt_id": rec["generation_receipt_id"],
                    "removed_literal_leaks": rec["removed_literal_leaks"],
                },
                ensure_ascii=False,
                sort_keys=True,
            )
        )

    args.blinded_out.parent.mkdir(parents=True, exist_ok=True)
    args.answer_key_out.parent.mkdir(parents=True, exist_ok=True)
    args.exclusions_out.parent.mkdir(parents=True, exist_ok=True)
    args.blinded_out.write_text("\n".join(blinded_lines) + ("\n" if blinded_lines else ""), encoding="utf-8")
    args.answer_key_out.write_text("\n".join(key_lines) + ("\n" if key_lines else ""), encoding="utf-8")
    args.exclusions_out.write_text(
        "\n".join(json.dumps(x, sort_keys=True) for x in exclusions) + ("\n" if exclusions else ""),
        encoding="utf-8",
    )

    print(json.dumps({"eligible": len(eligible), "excluded": len(exclusions), "shuffle_seed": args.shuffle_seed}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
