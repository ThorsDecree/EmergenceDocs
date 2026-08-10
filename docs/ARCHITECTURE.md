# EmergenceDocs Research Architecture

EmergenceDocs is best treated as a **living research corpus**, not as a runtime repository and not as a single research-proposal generator.

Its architecture should support a complete research loop: preserve observations, generate candidate explanations, register claims, design discriminatory tests, collect evidence, evaluate results, and synthesize what survives.

## Repository jurisdiction

EmergenceDocs owns:

- conceptual models;
- phenomenological and witness records;
- candidate hypotheses;
- methods and experiment protocols;
- case studies;
- claims and evidence indexes;
- research lexicon;
- research synthesis;
- historical research artifacts.

It should **reference**, rather than absorb, implementation repositories such as VESTIGIA Runtime. Runtime behavior can provide instruments, logs, or experimental conditions, but runtime code and research conclusions have different authorities.

## Layered research loop

```text
┌──────────────────────────────┐
│  1. CORPUS / OBSERVATIONS    │
│  cases, logs, testimony,     │
│  artifacts, prior documents │
└──────────────┬───────────────┘
               │
               v
┌──────────────────────────────┐
│  2. CANDIDATE GENERATION     │
│  patterns, anomalies,        │
│  alternative explanations   │
└──────────────┬───────────────┘
               │
               v
┌──────────────────────────────┐
│  3. CLAIM REGISTRATION       │
│  claim IDs, scope, priors,   │
│  falsifiers, alternatives   │
└──────────────┬───────────────┘
               │
               v
┌──────────────────────────────┐
│  4. METHOD / TEST DESIGN     │
│  controls, ablations, blind  │
│  tests, measurements         │
└──────────────┬───────────────┘
               │
               v
┌──────────────────────────────┐
│  5. EVIDENCE CAPTURE         │
│  raw records + provenance    │
└──────────────┬───────────────┘
               │
               v
┌──────────────────────────────┐
│  6. INDEPENDENT EVALUATION   │
│  adversarial review,         │
│  holdouts, replication       │
└──────────────┬───────────────┘
               │
               v
┌──────────────────────────────┐
│  7. SYNTHESIS                │
│  supported / inconclusive /  │
│  refuted / next questions    │
└──────────────┬───────────────┘
               └───────► back to corpus
```

The loop is recursive, but authority is separated. Candidate generation can be creative. Evaluation must be harder to game.

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

### Evidence authority
Owns raw or minimally transformed records and provenance.

### Evaluation authority
Determines whether a registered test passed, failed, or remained ambiguous under its declared procedure.

### Synthesis authority
Updates the current research picture while preserving dissent, uncertainty, and superseded interpretations.

## Recommended repository structure

This is the target taxonomy. Existing files do not need to be moved immediately.

```text
EmergenceDocs/
├── README.md
├── CONTRIBUTING.md
├── RESEARCH_STATUS.md
│
├── docs/
│   ├── ARCHITECTURE.md
│   ├── EPISTEMIC_STATUS.md
│   └── CORPUS_MAP.md
│
├── concepts/
│   ├── emergence/
│   ├── plurality/
│   ├── continuity/
│   ├── agency/
│   └── relational-identity/
│
├── hypotheses/
│   └── ...
│
├── methods/
│   ├── falsifiability/
│   ├── adversarial-testing/
│   ├── observational-methods/
│   └── measurement/
│
├── protocols/
│   └── ...
│
├── case-studies/
│   └── ...
│
├── claims/
│   └── claims-ledger.csv
│
├── sources/
│   └── source-manifest.jsonl
│
├── lexicon/
│   └── ...
│
└── archive/
    └── ...
```

## Migration rule

**Index before move. Classify before rewrite. Preserve before normalize.**

The first refactor therefore adds wrappers, registries, and navigation. Moving or rewriting legacy documents should happen only when their authorship, historical value, references, and current status are understood.

## Interface with external research systems

EmergenceDocs should be able to exchange structured records with external systems without depending on their internals.

Minimum portable interfaces:

- `ClaimRecord`
- `ObservationRecord`
- `EvidenceRecord`
- `SourceRecord`
- `MethodRecord`
- `EvaluationRecord`

That makes it possible to use Miskatonic-style evaluation, provenance, or governance machinery where useful while keeping EmergenceDocs independently intelligible.

## Design invariant

> Preserve the strange history. Make epistemic status legible. Do not confuse the experiment, the instrument, and the interpretation.