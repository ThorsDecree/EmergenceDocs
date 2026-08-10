# EmergenceDocs Schemas

This directory contains the portable machine-readable contracts for the research evidence pipeline.

## Version

Core evidence-contract version: **v0.1**  
RCIEP execution interchange extension: **v0.2**  
JSON Schema dialect: **Draft 2020-12**

## Core evidence schemas

- `source-record.schema.json`
- `claim-record.schema.json`
- `observation-record.schema.json`
- `evidence-record.schema.json`
- `method-record.schema.json`
- `evaluation-record.schema.json`
- `provenance-event.schema.json`
- `pilot-preregistration.schema.json`

Normative semantics and lineage rules live in `docs/EVIDENCE_CONTRACTS.md`.

## RCIEP v0.2 execution schema

- `rciep-raw-generation.schema.json`

This execution-specific schema defines the minimum interchange record emitted by a runtime/export step before blinding. It intentionally does not define a research outcome. Extra runtime receipt/context metadata may be included.

## Compatibility

A record is v0.1-compatible when:

1. it validates against the corresponding schema;
2. its referenced IDs resolve to records or registered artifacts in the repository/evidence package;
3. provenance edges are not knowingly omitted;
4. sensitive material satisfies the declared reuse gate;
5. any post-preregistration method change is recorded as a deviation.

Schema validity is necessary, not sufficient, for evidentiary validity.

A v0.2 RCIEP raw-generation record must additionally contain the minimum fields required by `tools/rciep_prepare_packet.py` and validate against `rciep-raw-generation.schema.json`.

## Source compatibility

The original `sources/source-manifest.jsonl` predates the v0.1 `SourceRecord` contract and remains canonical for the Corpus Registry snapshot. New source records should use `source-record.schema.json`; migration of the historical manifest can occur later without renumbering its `SRC-ED-*` identifiers.

`SRC-RUNTIME-0001` in `sources/runtime-pointers.jsonl` is the first native v0.1 `SourceRecord` used as an external implementation/instrument pointer.

## First live contract package

`pilots/RCIEP-001/` contains the first repository package using the evidence contracts:

- `claim.json` -> `ClaimRecord`
- `method.json` -> `MethodRecord`
- `preregistration.json` -> `PilotPreregistration`
- `v0.2/` -> frozen execution materials, configuration template, runbook, and execution state
- `replication/` -> I3 replication packet specification/template

Observation/Evidence/Evaluation records are intentionally absent until a valid local run occurs. Synthetic Stage A outputs qualify pipeline mechanics only and must not be promoted into confirmatory evidence for `ED-IDENT-001` or `ED-IDENT-002`.

## Validation

Local validation entrypoint:

```bash
python -m pip install jsonschema
python tools/rciep_validate_contracts.py
python -m py_compile tools/rciep_prepare_packet.py tools/rciep_analyze.py tools/rciep_validate_contracts.py
```

The local execution work order is `work-orders/WO-RCIEP-002.md`.

## Evolution

Breaking contract changes should create a new schema version rather than silently changing the meaning of existing v0.1 records. Historical records should remain readable under the schema version they declare.
