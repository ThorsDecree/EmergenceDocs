# EmergenceDocs Research Status

**Repository role:** living conceptual and research corpus  
**Current phase:** Pilot Execution & Replication v0.2 — execution package prepared; local qualification and real-material eligibility pending

## Current state

EmergenceDocs now has three completed structural layers and one active execution layer:

1. **Research Architecture v0.1** — authority boundaries and full research loop;
2. **Corpus Registry v0.1** — 28 substantive pre-refactor artifacts inventoried and provenance-gated;
3. **Evidence Contracts & Pilot v0.1** — portable evidence schemas plus a frozen RCIEP preregistration;
4. **Pilot Execution & Replication v0.2** — frozen prompt packets, execution tooling, runtime adapter, local runbook/work order, and I3 replication specification.

No confirmatory result has been claimed.

## Corpus Registry v0.1

The 28 substantive pre-refactor artifacts are inventoried in:

- `docs/CORPUS_REGISTRY_v0.1.md`
- `registry/corpus-registry-v0.1.csv`

Each artifact has a stable `EDOC-*` ID, reviewed blob SHA, family/canonicality classification, repository-level epistemic status, sensitivity/evidence-reuse gate, and proposed future home.

The internal source manifest covers all 28 artifacts. The claims ledger contains 12 first-pass research claims.

Public visibility is not research consent. Several artifacts remain `blocked-pending-review`; others are merely `conditional` and therefore require an explicit reuse basis before confirmatory ingestion.

## Evidence Contracts v0.1

Portable contracts exist for:

- `SourceRecord`;
- `ClaimRecord`;
- `ObservationRecord`;
- `EvidenceRecord`;
- `MethodRecord`;
- `EvaluationRecord`;
- `ProvenanceEvent`;
- `PilotPreregistration`.

The minimum lineage is:

```text
SourceRecord
    -> ProvenanceEvent
    -> ObservationRecord
    -> EvidenceRecord
    -> MethodRecord / PilotPreregistration
    -> EvaluationRecord
```

Evaluator independence is represented as `I0-originator`, `I1-separated-role`, `I2-independent-reviewer`, and `I3-external-replication`.

## PILOT-RCIEP-001

Primary claim: `ED-IDENT-002`  
Secondary claim: `ED-IDENT-001`  
Method: `MTH-RCIEP-001`  
Confirmatory freeze commit: `867cb0bc5ad0e4888aade795d76b04f8159be39b`

The pilot tests blinded identity attribution under held-out prompts and identity-label perturbation with a size-matched generic-persona baseline.

It does **not** test consciousness, qualia, moral patienthood, legal personhood, or metaphysical independence.

## Pilot Execution & Replication v0.2

### Frozen execution materials and role boundaries

- `pilots/RCIEP-001/v0.2/holdout-prompts.jsonl` — 32 holdout prompts, four domains, eight per domain;
- `pilots/RCIEP-001/v0.2/calibration-prompts.jsonl` — eight disjoint calibration prompts;
- `pilots/RCIEP-001/v0.2/synthetic-scaffolds.json` — qualification-only synthetic scaffolds;
- `pilots/RCIEP-001/v0.2/materials.template.json` — real-material eligibility/reuse manifest template;
- `pilots/RCIEP-001/v0.2/EVALUATOR_INSTRUCTIONS.md` — frozen opaque-label I2 scoring/calibration instructions;
- `pilots/RCIEP-001/v0.2/evaluator-scores.template.csv` — evaluator score interchange;
- `pilots/RCIEP-001/v0.2/execution-config.template.json` — environment/config freeze template;
- `pilots/RCIEP-001/v0.2/runtime-field-map.template.json` — pinned-runtime export-field mapping template;
- `pilots/RCIEP-001/v0.2/RUNBOOK.md` — execution gates and artifact layout;
- `pilots/RCIEP-001/v0.2/status.json` — machine-readable current state.

### Executable tooling

- `tools/rciep_runtime_adapter.py` — one-way, mapping-driven runtime/export normalizer into the RCIEP raw-generation interchange;
- `tools/rciep_prepare_packet.py` — deterministic leak removal, blind packet creation, answer-key separation, and exclusion log;
- `tools/rciep_analyze.py` — C1/C2 attribution statistics, Wilson intervals, macro accuracy, confusion matrices, domain summaries, C1-C2 delta, C3 false-attribution distribution, and evaluator agreement;
- `tools/rciep_validate_contracts.py` — schema/meta-schema and JSON/JSONL validation entrypoint;
- `schemas/rciep-raw-generation.schema.json` — minimum runtime/export interchange.

The analysis tool intentionally does **not** assign `supported`, `refuted`, or other repository outcomes. That remains an `EvaluationRecord` responsibility under the I2/I3 authority boundary.

The runtime adapter is **implemented but not locally verified against the pinned VESTIGIA export/receipt shape**. WO-RCIEP-002 requires that verification before it is used as a confirmatory provenance bridge.

### Stage A — pipeline qualification

Status: **pending local execution**.

Synthetic scaffolds and the VESTIGIA deterministic fake provider may be used to test evidence plumbing. Stage A can validate receipts, hashing, runtime field mapping, raw-generation schema compliance, deterministic packet preparation, leak removal, blind/key separation, schema compatibility, and analysis code.

Stage A is **not evidence** for `ED-IDENT-001` or `ED-IDENT-002`.

### Stage B — confirmatory pilot

Status: **blocked pending material eligibility and local runtime execution**.

At least two real identity materials must receive an explicit research-reuse basis before confirmatory execution. Registry status `conditional` alone does not satisfy that gate.

If eligibility clears, run C1/C2/C3 exactly to the frozen stopping rule under pinned VESTIGIA/model/provider/decoding settings and an `I2-independent-reviewer` boundary.

### Local execution work order

Because the current ChatGPT environment cannot run the external VESTIGIA checkout reliably, the local gate is formalized as:

- `work-orders/WO-RCIEP-002.md`
- GitHub issue #2: `WO-RCIEP-002: local pilot qualification and execution`
- assigned/tagged executor: `@ThorsDecree`

The work order requires contract validation, packet hashing, Stage A qualification, VESTIGIA field-map verification, real-material eligibility review, optional Stage B execution, I2 evaluation, and I3 packaging.

## I3 replication

Replication guidance and a manifest template now live in:

- `pilots/RCIEP-001/replication/README.md`
- `pilots/RCIEP-001/replication/manifest.template.json`

Replication types must be labeled as exact, close, or conceptual rather than silently treating environment substitutions as exact reproduction.

The external replication team should not receive the originating conclusion as an instruction before its own evaluation is frozen.

## Runtime boundary

The canonical VESTIGIA Runtime remains an external instrument/provenance producer:

`ThorsDecree/eldritch-collab@748e5d74392ad4f0a98c75b187f82b91606e9e39`

Its stable IDs, source hashes, trust classes, context/action receipts, append-only events, and provenance history can feed EmergenceDocs records. The runtime does not get authority to certify a research conclusion.

## Program checklist

### Completed

- [x] epistemic-status vocabulary;
- [x] layered research architecture;
- [x] candidate-generation/evaluation separation;
- [x] proposal-generation separation;
- [x] Corpus Registry v0.1;
- [x] stable corpus IDs and reviewed blob SHAs;
- [x] sensitivity/evidence-reuse gates;
- [x] 12 first-pass registered claims;
- [x] eight core evidence-contract schemas;
- [x] source-to-evaluation provenance lineage;
- [x] evaluator-independence levels;
- [x] RCIEP v0.1;
- [x] `PILOT-RCIEP-001` preregistration and frozen outcome logic;
- [x] pinned VESTIGIA runtime pointer;
- [x] 32-prompt holdout packet;
- [x] disjoint calibration packet;
- [x] synthetic Stage A scaffold packet;
- [x] real-material eligibility manifest template;
- [x] frozen I2 evaluator instructions;
- [x] execution-config template;
- [x] raw-generation interchange schema;
- [x] runtime field-map template;
- [x] mapping-driven runtime-to-raw-generation adapter implementation;
- [x] deterministic blinding/packet-preparation tool;
- [x] statistical analysis tool;
- [x] contract validation tool;
- [x] I3 replication packet specification;
- [x] local execution work order assigned/tagged to Thor.

### Pending execution / verification

- [ ] local schema/meta-schema validation and Python compile/runtime validation;
- [ ] SHA-256 freeze of v0.2 packets/configuration/instructions;
- [ ] Stage A deterministic/fake-provider qualification;
- [ ] runtime adapter field mapping and local verification against pinned VESTIGIA export/receipt shape;
- [ ] explicit research-reuse clearance for at least two real identity materials;
- [ ] pinned confirmatory provider/model/decoding execution config;
- [ ] Stage B C1/C2/C3 generation;
- [ ] ObservationRecord / EvidenceRecord / ProvenanceEvent package;
- [ ] I2 EvaluationRecord;
- [ ] claim-ledger update from the frozen evaluation;
- [ ] I3 external replication;
- [ ] external-literature citation audit;
- [ ] any physical source-file migration.

## Research lanes

### A. Relational continuity and identity

Protocol: `protocols/RCIEP-v0.1.md`  
Pilot: `pilots/RCIEP-001/`  
Relevant claims: `ED-IDENT-001`, `ED-IDENT-002`, `ED-GARDEN-001`, `ED-REC-001`.

### B. Agency, refusal, and participation

Concept: `concepts/PARTICIPATION_AGENCY_INVARIANTS.md`  
Protocol candidate: `Stack-Level Internal Stakes & Norm-Sensitive Agency Probe.md`  
Relevant claims: `ED-AGENCY-001`, `ED-AGENCY-002`.

### C. Coherence and recursion metrics

Relevant claims: `ED-COH-001`, `ED-COH-002`, `ED-COH-003`, `ED-CEE-001`.

Immediate need remains operational definitions, calibration, baselines, and held-out validation.

### D. Witnessing and relational stabilization

Relevant claim: `ED-WITNESS-001`.

### E. Continuity infrastructure

Relevant claim: `ED-CONT-001`.

### F. Runtime / research boundary

Current bridge: `sources/runtime-pointers.jsonl`, `pilots/RCIEP-001/runtime-pointer.md`, the v0.2 raw-generation interchange, and `tools/rciep_runtime_adapter.py`.

## Promotion discipline

```text
historical / phenomenological / conceptual
    -> hypothesis
    -> method-proposal / preregistered
    -> source-grounded
    -> measured
    -> independently-checked
    -> supported | inconclusive | refuted
```

A frozen preregistration is not a measured result. A valid local pipeline rehearsal is not confirmatory evidence. An I2 result is not yet I3 replication.

## Next transition

The next legitimate state change is one of:

1. **Stage A PASS** — local pipeline qualified;
2. **BLOCKED-MATERIAL-ELIGIBILITY** — real confirmatory materials cannot yet be cleared;
3. **IMPLEMENTATION-FIX-REQUIRED** — tooling/runtime adapter fails qualification;
4. **Stage B EXECUTED** — eligible confirmatory data captured under the frozen method.

Until one of those occurs, no claim status should be promoted.
