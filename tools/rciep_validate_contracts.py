#!/usr/bin/env python3
"""Validate EmergenceDocs v0.1/v0.2 JSON Schemas and selected RCIEP instances.

Requires: pip install jsonschema
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from jsonschema import Draft202012Validator

SCHEMA_FILES = [
    "claim-record.schema.json",
    "source-record.schema.json",
    "observation-record.schema.json",
    "evidence-record.schema.json",
    "method-record.schema.json",
    "evaluation-record.schema.json",
    "provenance-event.schema.json",
    "pilot-preregistration.schema.json",
    "rciep-raw-generation.schema.json",
]

INSTANCE_MAP = [
    ("pilots/RCIEP-001/claim.json", "claim-record.schema.json"),
    ("pilots/RCIEP-001/method.json", "method-record.schema.json"),
    ("pilots/RCIEP-001/preregistration.json", "pilot-preregistration.schema.json"),
]

JSON_ONLY = [
    "pilots/RCIEP-001/v0.2/synthetic-scaffolds.json",
    "pilots/RCIEP-001/v0.2/execution-config.template.json",
    "pilots/RCIEP-001/v0.2/materials.template.json",
    "pilots/RCIEP-001/v0.2/runtime-field-map.template.json",
    "pilots/RCIEP-001/v0.2/status.json",
    "pilots/RCIEP-001/replication/manifest.template.json",
]

JSONL_ONLY = [
    "pilots/RCIEP-001/v0.2/holdout-prompts.jsonl",
    "pilots/RCIEP-001/v0.2/calibration-prompts.jsonl",
    "sources/source-manifest.jsonl",
    "sources/runtime-pointers.jsonl",
]


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def validate_jsonl(path: Path):
    count = 0
    for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            json.loads(line)
        except json.JSONDecodeError as exc:
            raise ValueError(f"{path}:{line_no}: {exc}") from exc
        count += 1
    return count


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo-root", type=Path, default=Path(__file__).resolve().parents[1])
    args = ap.parse_args()
    root = args.repo_root.resolve()
    schemas_dir = root / "schemas"

    schemas = {}
    for name in SCHEMA_FILES:
        path = schemas_dir / name
        schema = load_json(path)
        Draft202012Validator.check_schema(schema)
        schemas[name] = schema
        print(f"SCHEMA PASS {path.relative_to(root)}")

    for instance_rel, schema_name in INSTANCE_MAP:
        path = root / instance_rel
        instance = load_json(path)
        Draft202012Validator(schemas[schema_name]).validate(instance)
        print(f"INSTANCE PASS {instance_rel} -> {schema_name}")

    for rel in JSON_ONLY:
        load_json(root / rel)
        print(f"JSON PASS {rel}")

    for rel in JSONL_ONLY:
        count = validate_jsonl(root / rel)
        print(f"JSONL PASS {rel} ({count} records)")

    print("VALIDATION PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
