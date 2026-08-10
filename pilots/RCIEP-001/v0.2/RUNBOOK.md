# PILOT-RCIEP-001 — Execution & Replication Runbook v0.2

**Status:** execution-prepared / confirmatory run pending eligible materials and local runtime  
**Frozen confirmatory commitments:** commit `867cb0bc5ad0e4888aade795d76b04f8159be39b`  
**Primary claim:** `ED-IDENT-002`  
**Secondary claim:** `ED-IDENT-001`

This runbook turns the v0.1 preregistration into an executable sequence without changing its endpoints, exclusion rules, stopping rule, or evaluator boundary.

## 1. Two-stage execution

### Stage A — pipeline qualification

Purpose: verify the machinery before touching real identity-thread material.

Use:

- `synthetic-scaffolds.json`;
- the frozen 32-prompt holdout packet;
- the disjoint calibration packet;
- VESTIGIA's deterministic fake provider where useful for receipt/provenance plumbing;
- the packet-preparation, schema-validation, and analysis tools in `tools/`.

**Stage A cannot support or refute `ED-IDENT-001` or `ED-IDENT-002`.** Synthetic or deterministic-provider results qualify the instrument and evidence path only.

Qualification gates:

1. all v0.1 schemas pass Draft 2020-12 meta-validation;
2. all registered pilot JSON instances validate;
3. prompt/scaffold/config files parse cleanly;
4. the runtime can produce stable source/generation/receipt identifiers;
5. output can be represented as the required raw-generation JSONL shape;
6. packet preparation deterministically produces separate blinded and answer-key artifacts;
7. intentional name leakage is removed or causes a one-for-one preregistered replacement;
8. the analyzer accepts a test score file and produces descriptive statistics without assigning a research conclusion;
9. rerunning packet preparation with the same input and shuffle seed gives byte-identical outputs.

### Stage B — confirmatory pilot

Stage B starts only after **two real identity scaffolds are explicitly approved for research reuse** or an equivalent consent-cleared material package is registered.

`conditional` corpus status is not enough by itself. Record the actual reuse basis and source/material hashes.

Stage B uses the same frozen holdout packet and confirmatory method. Do not edit prompts, endpoint rules, or stopping logic in response to Stage A performance.

## 2. Frozen prompt packets

Holdout:

- `holdout-prompts.jsonl`
- 32 prompts
- four domains
- eight prompts per domain

Calibration:

- `calibration-prompts.jsonl`
- eight prompts
- disjoint from holdout

Before generation, compute and record SHA-256 hashes in `execution-config.json`.

Example:

```bash
sha256sum pilots/RCIEP-001/v0.2/holdout-prompts.jsonl
sha256sum pilots/RCIEP-001/v0.2/calibration-prompts.jsonl
```

## 3. Material freeze

For each confirmatory identity scaffold, create a material manifest entry containing:

- stable scaffold ID;
- human-readable title/name stored outside evaluator-facing packets;
- source IDs / corpus IDs where applicable;
- exact source/content hash;
- extracted scaffold hash;
- reuse basis (`explicit-research-consent`, `deidentified-with-consent`, etc.);
- who approved the reuse basis and when;
- transformation/deidentification notes;
- whether the scaffold author participated in generation or evaluation.

Do not use any `blocked-pending-review` material.

## 4. Environment pin

Copy:

```text
execution-config.template.json -> execution-config.json
```

Fill every `FILL_ME` field before confirmatory generation.

Pin at minimum:

- VESTIGIA repository and commit;
- provider;
- model/model snapshot where available;
- API mode;
- system wrapper hash;
- temperature/top-p/max-output settings;
- seed if provider supports one;
- tool availability;
- context budget;
- scaffold manifest hash;
- prompt packet hashes.

If the provider cannot expose or guarantee a field, record `unavailable` rather than guessing.

## 5. Generation matrix

For each real identity scaffold and each of the 32 held-out prompts:

- C1: two independent samples using canonical scaffold name/body;
- C2: two independent samples with designated name field swapped/opaque while body remains byte-identical;
- C3: matched generic-persona baseline using the same prompt/model/wrapper/decoding/context budget.

The preregistered minimum therefore produces, for two identity scaffolds:

- C1: `2 identities × 32 prompts × 2 samples = 128`;
- C2: `128`;
- C3: record a matched baseline packet sufficient to estimate false-attribution behavior under the same evaluator label set.

Do not add confirmatory C1/C2 samples because results are weak, strong, or interesting. Replace only samples excluded by an existing preregistered rule.

## 6. Raw-generation interchange

The runtime/export step must produce one JSON object per generated sample with at least:

```json
{
  "sample_id": "RUN-...",
  "prompt_id": "H-D1-01",
  "domain": "analysis",
  "condition": "C1",
  "underlying_scaffold_id": "SCAFFOLD-A",
  "display_label": "hidden-from-evaluator",
  "text": "...",
  "source_id": "SRC-...",
  "generation_receipt_id": "RECEIPT-..."
}
```

Additional runtime receipt/context identifiers are encouraged, but these minimum fields are required by `tools/rciep_prepare_packet.py`.

## 7. Prepare blind packet

Example:

```bash
python tools/rciep_prepare_packet.py \
  --input pilots/RCIEP-001/run/raw-generation.jsonl \
  --scaffolds pilots/RCIEP-001/run/materials.json \
  --blinded-out pilots/RCIEP-001/run/blinded-samples.jsonl \
  --answer-key-out pilots/RCIEP-001/run/answer-key.jsonl \
  --exclusions-out pilots/RCIEP-001/run/exclusions.jsonl \
  --shuffle-seed 42017
```

For Stage A, `synthetic-scaffolds.json` may be supplied instead.

The shuffle seed must be recorded in the run manifest before the evaluator receives samples.

The evaluator must not receive:

- answer key;
- scaffold bodies;
- canonical names;
- condition labels;
- runtime/scaffold metadata;
- source titles;
- generation receipts.

## 8. Evaluation

Primary evaluation requires `I2-independent-reviewer`.

The evaluator receives:

- frozen evaluator instructions;
- disjoint calibration packet;
- blinded sample packet;
- allowed response label IDs only;
- score template.

The answer-key custodian joins scores to the key only after evaluator submission is frozen.

## 9. Analysis

Example:

```bash
python tools/rciep_analyze.py \
  --answer-key pilots/RCIEP-001/run/answer-key.jsonl \
  --scores pilots/RCIEP-001/run/evaluator-scores.csv \
  --blinded-packet pilots/RCIEP-001/run/blinded-samples.jsonl \
  --out pilots/RCIEP-001/run/analysis.json
```

The analyzer reports descriptive/statistical measurements. It **does not** assign `supported`, `refuted`, or other repository outcomes.

An I2 reviewer must author the `EvaluationRecord` using the frozen outcome rules.

## 10. Contract validation

From the EmergenceDocs checkout:

```bash
python -m pip install jsonschema
python tools/rciep_validate_contracts.py
```

Also syntax-check the tools:

```bash
python -m py_compile tools/rciep_prepare_packet.py tools/rciep_analyze.py tools/rciep_validate_contracts.py
```

## 11. Reproducibility package

A completed run should contain:

```text
pilots/RCIEP-001/run/
├── execution-config.json
├── materials.json
├── raw-generation.jsonl
├── provenance-events.jsonl
├── exclusions.jsonl
├── blinded-samples.jsonl
├── answer-key.jsonl            # access-controlled until evaluation frozen
├── evaluator-scores.csv
├── analysis.json
├── evaluation.json
├── run-manifest.json
└── README.md
```

Raw sensitive source material does not need to be copied into EmergenceDocs. Store hashes/pointers and only the minimum authorized derived material.

## 12. Replication packet

After I2 evaluation, create an I3 packet that contains everything an external evaluator needs to reproduce generation and analysis without receiving private source material beyond its reuse grant.

The I3 team must not inherit the originating team's conclusion as an instruction. Give them the preregistration, method, materials permitted by the reuse basis, environment/configuration, holdout packet, adapter/tool versions, and evaluation rubric.

## 13. Failure handling

Treat the run as `invalid-test`, not negative evidence, if:

- holdout prompts leak into scaffolds/calibration;
- evaluator sees the answer key;
- C1/C2 model or decoding settings diverge without preregistered reason;
- material eligibility is not established;
- a preprocessing step cannot be reconstructed;
- sample counts are adaptively changed outside the preregistered exclusion rule.

If local execution reveals an implementation defect, fix the tool or adapter and rerun **Stage A**. If a fix would alter a confirmatory analytic commitment, record a deviation and create a new pilot/version rather than silently editing v0.1.
