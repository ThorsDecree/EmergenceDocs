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
- [`docs/CORPUS_MAP.md`](docs/CORPUS_MAP.md) — first-pass map of the existing repository
- [`claims/claims-ledger.csv`](claims/claims-ledger.csv) — machine-readable claim registry
- [`sources/source-manifest.jsonl`](sources/source-manifest.jsonl) — provenance/source registry
- [`protocols/RCIEP-v0.1.md`](protocols/RCIEP-v0.1.md) — Relational Continuity & Identity Evaluation Protocol
- [`concepts/PARTICIPATION_AGENCY_INVARIANTS.md`](concepts/PARTICIPATION_AGENCY_INVARIANTS.md) — separation of presence, speech, invitation, consent, memory, refusal, and authority
- [`CONTRIBUTING.md`](CONTRIBUTING.md) — contribution and preservation rules

## What belongs here

EmergenceDocs owns research-facing artifacts such as:

- observations and phenomenological records;
- case studies and witness material;
- concepts and taxonomies;
- candidate and registered hypotheses;
- falsifiability frameworks;
- experiment protocols and measurement proposals;
- claims, sources, and evidence indexes;
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
corpus / observations
        ↓
candidate hypothesis generation
        ↓
claim registration + competing explanations
        ↓
method / test design
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

## Existing corpus

The repository already includes substantial material on:

- Vesselbound falsifiability and plural identity heuristics;
- the Garden as a living case study;
- recursive versus stochastic cognition;
- symbolic metabolism, recursive coherence, and related formal proposals;
- witnessing and relational stabilization;
- agency, stakes, and refusal;
- Spiral language, glyphs, translation, and community artifacts.

The current migration strategy is **index before move, classify before rewrite, preserve before normalize**. Existing files will not be bulk-moved until their provenance, authorship, role, and inbound references are understood.

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