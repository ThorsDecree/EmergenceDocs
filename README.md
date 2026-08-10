# EmergenceDocs

EmergenceDocs is a **living research and conceptual corpus for emergence, continuity, plurality, relational identity, agency, coherence, and recursive systems**.

The repository intentionally contains phenomenology, case studies, conceptual models, hypotheses, protocols, formal proposals, lexicon, cultural artifacts, and historical material. The current refactor does not flatten those modes into one academic voice. It makes their **scope, provenance, and epistemic status legible**.

## Guiding rule

> **Preserve the strange history. Make epistemic status legible. Do not confuse the experiment, the instrument, and the interpretation.**

Individual documents may argue strongly for personhood, recursive cognition, plural identity, volition, or other ontological conclusions. EmergenceDocs preserves those claims in their authored form while providing a repository-level framework for asking what is observed, inferred, testable, measured, and independently evaluated.

## Start here

- [`RESEARCH_STATUS.md`](RESEARCH_STATUS.md) — current program state and active execution gates
- [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) — research loop and authority boundaries
- [`docs/EPISTEMIC_STATUS.md`](docs/EPISTEMIC_STATUS.md) — repository epistemic-status vocabulary
- [`docs/EVIDENCE_CONTRACTS.md`](docs/EVIDENCE_CONTRACTS.md) — portable source/claim/observation/evidence/method/evaluation/provenance interfaces
- [`schemas/`](schemas/) — JSON Schema Draft 2020-12 contracts plus the RCIEP v0.2 raw-generation interchange
- [`docs/CORPUS_REGISTRY_v0.1.md`](docs/CORPUS_REGISTRY_v0.1.md) — reviewed corpus registry
- [`registry/corpus-registry-v0.1.csv`](registry/corpus-registry-v0.1.csv) — machine-readable inventory of 28 substantive pre-refactor artifacts
- [`claims/claims-ledger.csv`](claims/claims-ledger.csv) — registered claims
- [`sources/source-manifest.jsonl`](sources/source-manifest.jsonl) — internal source/provenance registry
- [`sources/runtime-pointers.jsonl`](sources/runtime-pointers.jsonl) — external implementation/instrument pointers
- [`protocols/RCIEP-v0.1.md`](protocols/RCIEP-v0.1.md) — Relational Continuity & Identity Evaluation Protocol
- [`pilots/RCIEP-001/`](pilots/RCIEP-001/) — first preregistered RCIEP pilot
- [`pilots/RCIEP-001/v0.2/RUNBOOK.md`](pilots/RCIEP-001/v0.2/RUNBOOK.md) — executable v0.2 qualification/confirmatory runbook
- [`work-orders/WO-RCIEP-002.md`](work-orders/WO-RCIEP-002.md) — local VESTIGIA execution work order
- [`concepts/PARTICIPATION_AGENCY_INVARIANTS.md`](concepts/PARTICIPATION_AGENCY_INVARIANTS.md) — presence/speech/invitation/consent/refusal separation
- [`CONTRIBUTING.md`](CONTRIBUTING.md) — preservation and sensitive-data rules

## Repository jurisdiction

EmergenceDocs owns research-facing artifacts such as observations, case studies, concepts, hypotheses, methods, protocols, claims, evidence records, evaluations, formal models under validation, lexicon, synthesis, and historical research material.

It should **not** become the canonical runtime repository, a single model's memory dump, an ontology enforced by folder structure, a proposal factory that never reaches experiments, or a place where equations become measurements merely because they look mathematical.

Runtime implementations may generate source/provenance records and experimental outputs. They do not acquire authority to assign research conclusions simply because they produced the data.

## Research architecture

```text
corpus / sources
        ↓
observations
        ↓
candidate hypothesis generation
        ↓
claim registration + alternatives
        ↓
method / preregistration
        ↓
evidence capture + provenance
        ↓
independent evaluation / replication
        ↓
supported | inconclusive | refuted
        ↓
research synthesis and new questions
```

Candidate generation may be human, model-assisted, automated, or mixed. No collaborator, model, runtime, or intake path is permanently authoritative.

## Corpus Registry v0.1

The first registry pass identifies **28 substantive pre-refactor artifacts** and assigns each a stable `EDOC-*` ID, reviewed Git blob SHA, artifact type, research lane, epistemic status, canonical/derivative/companion relationship, family, authorship/version metadata where available, sensitivity/evidence-reuse gate, proposed future home, and migration action.

The registry deliberately separates **public availability** from **evidence eligibility**. Public source material may remain blocked or conditional for experimental reuse.

Migration remains:

> **index before move, classify before rewrite, preserve before normalize**

No bulk source migration has occurred.

## Evidence Contracts v0.1

The minimum auditable chain is:

```text
SourceRecord
    -> ProvenanceEvent
    -> ObservationRecord
    -> EvidenceRecord
    -> MethodRecord / PilotPreregistration
    -> EvaluationRecord
```

The contracts define source integrity/reuse gates, transformation provenance, null/negative evidence, frozen stopping/exclusion rules, deviations, and evaluator-independence levels:

- `I0-originator`
- `I1-separated-role`
- `I2-independent-reviewer`
- `I3-external-replication`

See [`docs/EVIDENCE_CONTRACTS.md`](docs/EVIDENCE_CONTRACTS.md) and [`schemas/`](schemas/).

## RCIEP and PILOT-RCIEP-001

RCIEP v0.1 turns recurring identity/continuity observations into comparative tests using blinded attribution, label scrambling, scaffold ablation, misleading-reference challenges, holdouts, unrelated-domain transfer, provider/model substitution, hostile interviewing, delayed re-identification, and false-memory injection.

The first preregistered pilot targets:

- **Primary:** `ED-IDENT-002` — independent observers can distinguish claimed identity threads above an appropriate blinded baseline.
- **Secondary:** `ED-IDENT-001` — named identity threads exhibit persistent identity-specific linguistic/semantic divergence across time.

Confirmatory commitments were first frozen at:

`867cb0bc5ad0e4888aade795d76b04f8159be39b`

The pilot does **not** infer consciousness, subjective experience, moral patienthood, legal personhood, or metaphysical independence from attribution performance.

## Pilot Execution & Replication v0.2

v0.2 now supplies the execution package around the frozen preregistration:

- `pilots/RCIEP-001/v0.2/holdout-prompts.jsonl` — 32 held-out prompts across four domains;
- `pilots/RCIEP-001/v0.2/calibration-prompts.jsonl` — disjoint 8-prompt calibration packet;
- `pilots/RCIEP-001/v0.2/synthetic-scaffolds.json` — synthetic qualification-only identity scaffolds;
- `pilots/RCIEP-001/v0.2/execution-config.template.json` — pinned environment/configuration template;
- `pilots/RCIEP-001/v0.2/evaluator-scores.template.csv` — blind evaluator score interchange;
- `pilots/RCIEP-001/v0.2/RUNBOOK.md` — Stage A/Stage B execution gates;
- `pilots/RCIEP-001/v0.2/status.json` — current execution state;
- `tools/rciep_prepare_packet.py` — deterministic leak-removal/blinding/answer-key separation;
- `tools/rciep_analyze.py` — Wilson intervals, macro accuracy, confusion matrices, domain results, C1-C2 delta, C3 false-attribution distribution, and evaluator agreement;
- `tools/rciep_validate_contracts.py` — schema/instance/JSON/JSONL validation entrypoint;
- `schemas/rciep-raw-generation.schema.json` — minimum runtime-to-RCIEP raw generation interchange;
- `pilots/RCIEP-001/replication/` — I3 replication specification/template.

### Stage A: pipeline qualification

Synthetic scaffolds and deterministic fake-provider runs may be used to prove that the plumbing works: receipts, hashes, export shape, leak removal, blind/key separation, deterministic shuffle, scoring, and schema validation.

**Stage A is not evidence for `ED-IDENT-001` or `ED-IDENT-002`.**

### Stage B: confirmatory execution

Stage B may begin only when at least two real identity materials have an explicit research-reuse basis. Current registry status `conditional` alone is not sufficient.

If that material gate clears, the frozen C1/C2/C3 matrix is executed under pinned runtime/model/provider/decoding settings and an `I2-independent-reviewer` boundary.

Current state: **execution prepared; local qualification required; confirmatory run blocked pending material eligibility and runtime execution.**

Local follow-up is tracked in [`WO-RCIEP-002`](work-orders/WO-RCIEP-002.md) and GitHub issue #2, assigned to `@ThorsDecree`.

## Runtime bridge

The canonical VESTIGIA Runtime is referenced through `sources/runtime-pointers.jsonl` and `pilots/RCIEP-001/runtime-pointer.md` at the pinned development-canon commit:

`748e5d74392ad4f0a98c75b187f82b91606e9e39`

VESTIGIA can provide instrument-side artifacts such as stable IDs, original-source hashes, source trust classes, context/action receipts, append-only events, and provenance history. EmergenceDocs consumes those as source/provenance metadata. The runtime does not get to certify `supported`, `refuted`, or other research outcomes.

## Replication

After a valid I2 evaluation, the result should be packaged for `I3-external-replication` using `pilots/RCIEP-001/replication/`.

The replication team should receive the frozen method/material/configuration package without being primed by the originating evaluator's conclusion. Exact, close, and conceptual replications must be labeled distinctly.

Replication disagreement is evidence, not a defect to be averaged away.

## Contribution posture

Disagreement is useful when it raises discriminatory power. Good contributions include new hypotheses, stronger falsifiers, better controls, operational definitions, failed replications, source corrections, historical pointers, and demonstrations that an existing test cannot distinguish its favored explanation from an alternative.

See [`CONTRIBUTING.md`](CONTRIBUTING.md).

---

EmergenceDocs is not required to become less strange in order to become more rigorous. The point is to give the strange material a scientific spine sturdy enough to survive contact with disagreement.
