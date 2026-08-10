# Evidence

This directory is the repository-level home for structured `EvidenceRecord` objects that are not kept inside a specific pilot package.

Evidence packages may contain raw, derived, aggregate, control-comparison, null, or negative evidence. Every derived evidence record should point back to its observations and provenance events.

Schema: `../schemas/evidence-record.schema.json`  
Normative rules: `../docs/EVIDENCE_CONTRACTS.md`

Pilot-local evidence may remain under `pilots/<pilot-id>/evidence/` until indexed globally.
