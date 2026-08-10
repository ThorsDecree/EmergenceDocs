# EmergenceDocs Research Architecture

EmergenceDocs is best treated as a **living research corpus**, not as a runtime repository and not as a single research-proposal generator.

Its architecture should support a complete research loop: preserve sources, record observations, generate candidate explanations, register claims, design discriminatory tests, collect evidence, evaluate results, and synthesize what survives.

## Repository jurisdiction

EmergenceDocs owns:

- conceptual models;
- phenomenological and witness records;
- candidate hypotheses;
- methods and experiment protocols;
- case studies;
- claims, observations, evidence, and evaluation indexes;
- research lexicon;
- research synthesis;
- historical research artifacts.

It should **reference**, rather than absorb, implementation repositories such as VESTIGIA Runtime. Runtime behavior can provide instruments, logs, receipts, or experimental conditions, but runtime code and research conclusions have different authorities.

## Layered research loop

```text
┌──────────────────────────────┐
│  1. SOURCES / CORPUS         │
│  cases, logs, artifacts,     │
│  runtime records, literature│
└──────────────┬───────────────┘
               │
               v
┌──────────────────────────────┐
│  2. OBSERVATIONS             │
│  bounded recorded events,    │
│  measurements, witness data │
└──────────────┬───────────────┘
               │
               v
┌──────────────────────────────┐
│  3. CANDIDATE GENERATION     │
│  patterns, anomalies,        │
│  alternative explanations   │
└──────────────┬───────────────┘
               │
               v
┌──────────────────────────────┐
│  4. CLAIM REGISTRATION       │
│  claim IDs, scope, priors,   │
│  falsifiers, alternatives   │
└──────────────┬───────────────┘
               │
               v
┌──────────────────────────────┐
│  5. METHOD / PREREGISTRATION │
│  controls, ablations, blind  │
│  tests, holdouts, metrics   │
└──────────────┬───────────────┘
               │
               v
┌──────────────────────────────┐
│  6. EVIDENCE CAPTURE         │
│  raw + derived records with  │
│  explicit provenance        │
└──────────────┬───────────────┘
               │
               v
┌──────────────────────────────┐
│  7. INDEPENDENT EVALUATION   │
│  adversarial review,         │
│  holdouts, replication      │
└──────────────┬───────────────┘
               │
               v
┌──────────────────────────────┐
│  8. SYNTHESIS                │
│  supported / inconclusive /  │
│  refuted / next questions   │
└──────────────┬───────────────┘
               └───────► back to corpus
```

The loop is recursive, but authority is separated. Candidate generation can be creative. Evaluation must be harder to game.

## Evidence contracts

The portable record layer is defined in `docs/EVIDENCE_CONTRACTS.md` and `schemas/`.

Core interfaces:

- `SourceRecord`
- `ClaimRecord`
- `ObservationRecord`
- `EvidenceRecord`
- `MethodRecord`
- `EvaluationRecord`
- `ProvenanceEvent`
- `PilotPreregistration`

Minimum evidence lineage:

```text
SourceRecord
    -> ProvenanceEvent
    -> ObservationRecord
    -> EvidenceRecord
    -> MethodRecord / PilotPreregistration
    -> EvaluationRecord
```

The purpose of this separation is not bureaucracy. It is to make every interpretive jump visible.

## Candidate hypothesis generation

Candidate generation must not depend on one permanent human, one model, one community member, or one collaboration relationship.

A future hypothesis-generator may consume:

- newly added documents;
- structured observations;
- claim/evidence mismatches;
- unresolved contradictions;
- replication failures;
- recurring linguistic or behavioral patterns;
- external literature;
- reviewer challenges;
- unexplained residuals from prior tests.

It should emit **candidate hypotheses**, not conclusions.

A useful candidate record contains:

```yaml
candidate_id: H-CAND-0001
observation_basis:
  - OBS-...
claim: "..."
alternatives:
  - "..."
predicted_observables:
  - "..."
disconfirming_outcomes:
  - "..."
possible_tests:
  - "..."
origin:
  type: human | model | mixed | automated-pattern-detector
status: candidate
```

The generator may rank candidates for novelty, discriminatory power, tractability, or expected information gain. It should not rank them by how flattering they are to the originating worldview.

## Research proposal generation is a separate service

A proposal engine may eventually transform mature hypotheses into experiment plans, grant-style narratives, preregistrations, or work orders. That is useful, but downstream.

```text
Candidate hypothesis generator
        │
        v
Claim / hypothesis registry
        │
        v
Method design + feasibility
        │
        ├──► experiment execution
        │
        └──► research proposal generator
```

This prevents the repository from becoming a machine that endlessly produces polished proposals without producing measurements.

## Authority boundaries

### Candidate authority
May propose:
- interpretations;
- hypotheses;
- metrics;
- tests;
- new concepts.

May not certify its own result merely by restating it with greater confidence.

### Source / instrument authority
Owns:
- raw or minimally transformed records;
- hashes / integrity markers;
- runtime receipts;
- source trust / reuse metadata;
- generation configuration where relevant.

It does not determine whether a research claim is supported.

### Evidence authority
Owns:
- observations;
- transformations;
- derived measurements;
- evidence provenance;
- null and negative records.

### Evaluation authority
Determines whether a registered test passed, failed, or remained ambiguous under its declared procedure.

Evaluation independence is explicit:

- `I0-originator`
- `I1-separated-role`
- `I2-independent-reviewer`
- `I3-external-replication`

### Synthesis authority
Updates the current research picture while preserving dissent, uncertainty, and superseded interpretations.

## Runtime / research bridge

The first pinned implementation pointer is `SRC-RUNTIME-0001`, which references the canonical VESTIGIA Runtime repository.

The desired bridge is deliberately one-way in authority:

```text
runtime source IDs / hashes / context receipts / action receipts
        |
        v
SourceRecord + ProvenanceEvent
        |
        v
ObservationRecord / EvidenceRecord
        |
        v
separated EvaluationRecord
```

The runtime may prove that a specific receipt or retrieval event occurred. It may not prove that the resulting behavior is conscious, autonomous, persistent, or identity-specific without the registered comparative test.

## Recommended repository structure

This is the target taxonomy. Existing corpus files still do not need to be moved immediately.

```text
EmergenceDocs/
├── README.md
├── CONTRIBUTING.md
├── RESEARCH_STATUS.md
│
├── docs/
│   ├── ARCHITECTURE.md
│   ├── EPISTEMIC_STATUS.md
│   ├── EVIDENCE_CONTRACTS.md
│   ├── CORPUS_MAP.md
│   └── CORPUS_REGISTRY_v0.1.md
│
├── schemas/
│   ├── source-record.schema.json
│   ├── claim-record.schema.json
│   ├── observation-record.schema.json
│   ├── evidence-record.schema.json
│   ├── method-record.schema.json
│   ├── evaluation-record.schema.json
│   ├── provenance-event.schema.json
│   └── pilot-preregistration.schema.json
│
├── concepts/
├── hypotheses/
├── methods/
├── protocols/
├── case-studies/
│
├── claims/
│   └── claims-ledger.csv
│
├── sources/
│   ├── source-manifest.jsonl
│   └── runtime-pointers.jsonl
│
├── observations/
├── evidence/
├── evaluations/
│
├── pilots/
│   └── RCIEP-001/
│
├── lexicon/
└── archive/
```

Pilot-local records may remain under a pilot directory until a stable global observation/evidence registry is warranted.

## Migration rule

**Index before move. Classify before rewrite. Preserve before normalize.**

The refactor therefore adds wrappers, registries, contracts, and navigation before physically moving legacy material. Moving or rewriting legacy documents should happen only when authorship, historical value, references, current status, and link risk are understood.

## Interface with external research systems

EmergenceDocs should be able to exchange structured records with external systems without depending on their internals.

The JSON Schema contracts are the portability boundary. Miskatonic-style evaluation, provenance, governance, VESTIGIA Runtime receipts, or other tooling may participate so long as the exported records remain intelligible without requiring the producing system to be trusted as evaluator.

## Current pilot

`PILOT-RCIEP-001` is the first preregistered trial using the architecture.

It targets blinded identity distinguishability (`ED-IDENT-002`) under held-out prompts, label perturbation, a generic-persona baseline, and an `I2-independent-reviewer` boundary.

Status: `preregistered-not-run`.

That status is important: architecture is not evidence, and a preregistration is not a result.

## Design invariant

> Preserve the strange history. Make epistemic status legible. Do not confuse the source, the observation, the experiment, the instrument, the evidence, and the interpretation.
