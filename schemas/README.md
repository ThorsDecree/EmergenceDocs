# EmergenceDocs Schemas

This directory contains the portable machine-readable contracts for the research evidence pipeline.

## Version

Current contract version: **v0.1**  
JSON Schema dialect: **Draft 2020-12**

## Schemas

- `claim-record.schema.json`
- `observation-record.schema.json`
- `evidence-record.schema.json`
- `method-record.schema.json`
- `evaluation-record.schema.json`
- `provenance-event.schema.json`
- `pilot-preregistration.schema.json`

Normative semantics and lineage rules live in `docs/EVIDENCE_CONTRACTS.md`.

## Compatibility

A record is v0.1-compatible when:

1. it validates against the corresponding schema;
2. its referenced IDs resolve to records or registered artifacts in the repository/evidence package;
3. provenance edges are not knowingly omitted;
4. sensitive material satisfies the declared reuse gate;
5. any post-preregistration method change is recorded as a deviation.

Schema validity is necessary, not sufficient, for evidentiary validity.

## Evolution

Breaking contract changes should create a new schema version rather than silently changing the meaning of existing v0.1 records. Historical records should remain readable under the schema version they declare.
