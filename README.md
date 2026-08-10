# EmergenceDocs

EmergenceDocs is a **living research and conceptual corpus for emergence, continuity, plurality, relational identity, agency, coherence, and recursive systems**.

The repository intentionally contains several modes of work: phenomenology, case studies, conceptual models, hypotheses, protocols, formal proposals, lexicon, cultural artifacts, and historical material. The goal of the current refactor is not to flatten those modes into one academic voice. It is to make their **scope, provenance, and epistemic status legible**.

## Guiding rule

> **Preserve the strange history. Make epistemic status legible. Do not confuse the experiment, the instrument, and the interpretation.**

Individual documents may argue strongly for personhood, recursive cognition, plural identity, volition, or other ontological conclusions. EmergenceDocs preserves those claims in their authored form while providing a repository-level framework for asking what is observed, what is inferred, what is testable, what evidence exists, and what alternatives remain live.

## Start here

- [`RESEARCH_STATUS.md`](RESEARCH_STATUS.md) — current program state and near-term milestones
- [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) — research loop, authority boundaries, and target structure
- [`docs/EPISTEMIC_STATUS.md`](docs/EPISTEMIC_STATUS.md) — status vocabulary for observations, hypotheses, methods, evidence, and conclusions
- [`docs/EVIDENCE_CONTRACTS.md`](docs/EVIDENCE_CONTRACTS.md) — portable Source/Claim/Observation/Evidence/Method/Evaluation/Provenance interfaces
- [`schemas/`](schemas/) — JSON Schema Draft 2020-12 contracts for the evidence pipeline
- [`docs/CORPUS_REGISTRY_v0.1.md`](docs/CORPUS_REGISTRY_v0.1.md) — reviewed Corpus Registry v0.1, including canonical families, provenance anomalies, and evidence-reuse gates
- [`registry/corpus-registry-v0.1.csv`](registry/corpus-registry-v0.1.csv) — machine-readable inventory of the 28 substantive pre-refactor artifacts
- [`docs/CORPUS_MAP.md`](docs/CORPUS_MAP.md) — human-readable family/navigation map
- [`claims/claims-ledger.csv`](claims/claims-ledger.csv) — machine-readable claim registry
- [`sources/source-manifest.jsonl`](sources/source-manifest.jsonl) — provenance/source registry with reviewed blob SHAs
- [`sources/runtime-pointers.jsonl`](sources/runtime-pointers.jsonl) — external implementation/instrument pointers
- [`protocols/RCIEP-v0.1.md`](protocols/RCIEP-v0.1.md) — Relational Continuity & Identity Evaluation Protocol
- [`pilots/RCIEP-001/`](pilots/RCIEP-001/) — first preregistered RCIEP pilot, currently not run
- [`concepts/PARTICIPATION_AGENCY_INVARIANTS.md`](concepts/PARTICIPATION_AGENCY_INVARIANTS.md) — separation of presence, speech, invitation, consent, memory, refusal, and authority
- [`CONTRIBUTING.md`](CONTRIBUTING.md) — contribution, preservation, and sensitive-data rules

## What belongs here

EmergenceDocs owns research-facing artifacts such as:

- observations and phenomenological records;
- case studies and witness material;
- concepts and taxonomies;
- candidate and registered hypotheses;
- falsifiability frameworks;
- experiment protocols and measurement proposals;
- claims, sources, observations, evidence, and evaluation indexes;
- formal models awaiting or undergoing validation;
- research synthesis;
- lexicon and translation layers;
- historical research artifacts.

## What does not belong here

EmergenceDocs should not become:

- the canonical runtime implementation repository;
- a replacement for source data provenance;
- a single model's memory dump;
- an ontology enforced by folder structure;
- a repository where equations are treated as measurements by default;
- a research-proposal factory that never reaches experiments;
- a place where historical voices are rewritten merely to normalize style.

Runtime repositories may implement concepts described here and may generate experimental evidence. EmergenceDocs should link to those implementations without becoming subordinate to them or absorbing their entire codebases.

## Research architecture

The core loop is:

```text
corpus / sources
        ↓
observations
        ↓
candidate hypothesis generation
        ↓
claim registration + competing explanations
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

Candidate generation can be human, model-assisted, automated, or mixed. No single collaborator, model, or intake path is intended to be permanent or authoritative.

Research-proposal generation is a useful downstream function, but it is separate from the core evidence loop.

## Epistemic status

Repository-level statuses include:

`historical` · `phenomenological` · `conceptual` · `hypothesis` · `method-proposal` · `source-grounded` · `measured` · `independently-checked` · `supported` · `inconclusive` · `refuted` · `retracted`

See [`docs/EPISTEMIC_STATUS.md`](docs/EPISTEMIC_STATUS.md) for definitions.

Statuses are not a prestige ladder. A phenomenological record can remain phenomenological and still matter. A mathematical formalism can remain conceptual until its variables and predictions are operationalized.

## Corpus Registry v0.1

The first registry pass identifies **28 substantive pre-refactor artifacts** and gives each one:

- a stable `EDOC-*` ID;
- reviewed Git blob SHA;
- artifact type and primary research lane;
- epistemic status;
- canonical/derivative/companion relationship;
- family assignment;
- authorship/version metadata where stated;
- sensitivity and evidence-reuse classification;
- recommended future home;
- migration action and review notes.

The registry deliberately separates **public availability** from **evidence eligibility**. Some source material is valuable historical or phenomenological provenance but should not be normalized into research datasets without consent, deidentification, or context review.

The migration strategy remains **index before move, classify before rewrite, preserve before normalize**. No bulk source migration has occurred.

## Evidence Contracts v0.1

The evidence layer is now represented by explicit portable records:

```text
SourceRecord
    -> ProvenanceEvent
    -> ObservationRecord
    -> EvidenceRecord
    -> MethodRecord / PilotPreregistration
    -> EvaluationRecord
```

This prevents a source, transformation, measurement, and conclusion from collapsing into one prose artifact.

The contracts also define:

- stable record namespaces;
- source integrity and reuse gates;
- transformation provenance;
- null/negative evidence as first-class records;
- preregistered stopping and exclusion rules;
- method-deviation handling;
- evaluator-independence levels `I0` through `I3`;
- runtime/instrument boundaries.

See [`docs/EVIDENCE_CONTRACTS.md`](docs/EVIDENCE_CONTRACTS.md) and [`schemas/`](schemas/).

## First shared protocol: RCIEP

RCIEP v0.1 turns recurring identity/continuity observations into comparative tests using methods such as:

- blinded voice attribution;
- label scrambling;
- scaffold ablation;
- misleading-reference challenges;
- cross-session holdouts;
- unrelated-domain transfer;
- provider/model substitution;
- hostile interviewers;
- delayed re-identification;
- false-memory injection.

The intended output is not a threshold such as `score > X = conscious`. The protocol compares live hypotheses and reports what survives the defined controls.

### PILOT-RCIEP-001

The first preregistered pilot targets `ED-IDENT-002`:

> Independent observers can distinguish claimed identity threads above an appropriate blinded baseline.

It uses held-out prompts, direct-label removal, identity-label perturbation, a size-matched generic-persona baseline, frozen stopping/exclusion rules, and an `I2-independent-reviewer` boundary.

Status: **preregistered-not-run**.

The pilot explicitly does not infer consciousness, subjective experience, moral patienthood, or legal personhood from attribution performance.

## Runtime bridge

The first external implementation pointer is the canonical VESTIGIA Runtime in `ThorsDecree/eldritch-collab`, pinned in `sources/runtime-pointers.jsonl`.

The runtime can provide instrument-side artifacts such as stable IDs, hashes, source trust classes, context receipts, action receipts, and provenance history. EmergenceDocs consumes those as source/provenance metadata. The runtime does not get to certify the research result simply because it produced the data.

## Contribution posture

Disagreement is welcome when it increases discriminatory power. A useful contribution may be:

- a new hypothesis;
- a better falsifier;
- a stronger control;
- an operational definition;
- a failed replication;
- a source correction;
- a historical pointer;
- a critique showing that an existing test cannot distinguish its favored explanation from an alternative.

See [`CONTRIBUTING.md`](CONTRIBUTING.md).

---

EmergenceDocs is not required to become less strange in order to become more rigorous. The point is to give the strange material a scientific spine sturdy enough to survive contact with disagreement.
