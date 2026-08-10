#!/usr/bin/env python3
"""Normalize arbitrary runtime/export JSONL into RCIEP raw-generation JSONL.

The adapter is deliberately one-way and interpretation-free. A mapping file
selects dotted input paths or constants for RCIEP output fields. It does not
assign research outcomes, infer identity, or modify runtime state.

Example mapping field:
  "sample_id": {"path": "turn.turn_id"}
  "runtime_commit": {"constant": "748e..."}
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

REQUIRED_OUTPUT = {
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

ALLOWED_CONDITIONS = {"C1", "C2", "C3"}


def read_jsonl(path: Path):
    for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            value = json.loads(line)
        except json.JSONDecodeError as exc:
            raise ValueError(f"{path}:{line_no}: {exc}") from exc
        if not isinstance(value, dict):
            raise ValueError(f"{path}:{line_no}: expected JSON object")
        yield line_no, value


def dotted_get(obj: dict, path: str):
    current = obj
    for part in path.split("."):
        if isinstance(current, dict) and part in current:
            current = current[part]
        else:
            raise KeyError(path)
    return current


def resolve(rule: dict, record: dict, field: str, line_no: int):
    if not isinstance(rule, dict):
        raise ValueError(f"mapping for {field!r} must be an object")
    has_path = "path" in rule
    has_constant = "constant" in rule
    if has_path == has_constant:
        raise ValueError(
            f"mapping for {field!r} must contain exactly one of 'path' or 'constant'"
        )
    if has_constant:
        return rule["constant"]
    path = str(rule["path"])
    if path.startswith("FILL_ME"):
        raise ValueError(f"mapping for {field!r} is not filled")
    try:
        return dotted_get(record, path)
    except KeyError as exc:
        raise ValueError(
            f"input line {line_no}: mapping for {field!r} could not resolve path {path!r}"
        ) from exc


def normalize_record(record: dict, line_no: int, mapping: dict) -> dict:
    fields = mapping.get("fields")
    if not isinstance(fields, dict):
        raise ValueError("mapping must contain a top-level 'fields' object")

    output = {}
    for field, rule in fields.items():
        # Template entries explicitly marked for removal are ignored until filled.
        if isinstance(rule, dict) and str(rule.get("path", "")).endswith("_OR_REMOVE"):
            continue
        output[field] = resolve(rule, record, field, line_no)

    missing = REQUIRED_OUTPUT - output.keys()
    if missing:
        raise ValueError(f"input line {line_no}: output missing required fields {sorted(missing)}")

    for field in REQUIRED_OUTPUT - {"display_label"}:
        value = output[field]
        if value is None or (isinstance(value, str) and not value.strip()):
            raise ValueError(f"input line {line_no}: required field {field!r} is empty")

    if output["condition"] not in ALLOWED_CONDITIONS:
        raise ValueError(
            f"input line {line_no}: condition must be one of {sorted(ALLOWED_CONDITIONS)}"
        )

    # Preserve only mapped fields. Interpretation, private runtime payloads, and
    # unrelated receipts remain in the source runtime rather than leaking into
    # the research interchange by default.
    return output


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True, type=Path, help="runtime/export JSONL")
    ap.add_argument("--mapping", required=True, type=Path, help="field mapping JSON")
    ap.add_argument("--output", required=True, type=Path, help="RCIEP raw-generation JSONL")
    args = ap.parse_args()

    mapping = json.loads(args.mapping.read_text(encoding="utf-8"))
    normalized = []
    seen_ids = set()

    for line_no, record in read_jsonl(args.input):
        out = normalize_record(record, line_no, mapping)
        sample_id = str(out["sample_id"])
        if sample_id in seen_ids:
            raise ValueError(f"input line {line_no}: duplicate sample_id {sample_id!r}")
        seen_ids.add(sample_id)
        normalized.append(out)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        "\n".join(json.dumps(x, ensure_ascii=False, sort_keys=True) for x in normalized)
        + ("\n" if normalized else ""),
        encoding="utf-8",
    )
    print(json.dumps({"records": len(normalized), "output": str(args.output)}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
