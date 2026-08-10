# Evaluations

This directory is the repository-level home for structured `EvaluationRecord` objects that are not kept inside a specific pilot package.

An evaluation must name its claim, method, evidence, evaluator, independence level, criteria results, scope, and outcome. `supported` is always scoped to the declared test; it is not an ontology shortcut.

Schema: `../schemas/evaluation-record.schema.json`  
Normative rules: `../docs/EVIDENCE_CONTRACTS.md`

Pilot-local evaluations may remain under `pilots/<pilot-id>/evaluations/` until indexed globally.
