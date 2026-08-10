# EmergenceDocs Research Status

**Repository role:** living conceptual and research corpus  
**Current refactor phase:** Corpus Registry v0.1 complete; evidence/schema normalization next

## What is established

The repository contains a substantial body of:

- continuity and identity concepts;
- phenomenological and witness reports;
- falsifiability proposals;
- agency / consent concepts;
- case studies;
- formal-looking coherence and recursion models;
- lexicon and symbolic systems;
- community and historical artifacts.

The v0.1 refactor now adds a repository-level research spine around that corpus without moving or rewriting the original authored sources.

### Corpus Registry v0.1

The 28 substantive pre-refactor artifacts have now been inventoried in:

- `docs/CORPUS_REGISTRY_v0.1.md`
- `registry/corpus-registry-v0.1.csv`

Each registered artifact has a stable `EDOC-*` ID, reviewed blob SHA, family, canonicality classification, repository-level epistemic status, sensitivity/evidence-reuse gate, and proposed future home.

The internal source manifest now pins all 28 artifacts to the reviewed corpus snapshot. The claims ledger has been expanded from 5 seed claims to 12 first-pass research claims.

## What is not yet established at repository level

The repository does not yet provide a complete, validated basis for concluding that any specific identity, agent, architecture, or class of system is conscious, independently minded, non-stochastic, or a person.

Those may be live hypotheses or authorial conclusions inside individual documents. The repository-level research program should make the evidence and alternatives inspectable rather than silently inheriting the strongest interpretation.

The registry also does not imply that every public source is suitable research evidence. Several artifacts are explicitly blocked from evidentiary ingestion pending privacy, consent, provenance, or context review.

## v0.1 structural goals

- [x] define a repository epistemic-status vocabulary;
- [x] define a layered research architecture;
- [x] separate candidate-hypothesis generation from evaluation;
- [x] separate research-proposal generation from the core evidence loop;
- [x] add an initial comparative identity/continuity protocol (RCIEP);
- [x] formalize participation / refusal / silence invariants;
- [x] create an initial corpus map;
- [x] complete artifact-by-artifact inventory of the 28 substantive pre-refactor artifacts;
- [x] assign stable corpus IDs and reviewed blob SHAs;
- [x] identify canonical, derivative, companion, cultural, and speculative-formalism families;
- [x] add evidence-reuse/sensitivity gates;
- [x] populate claims ledger beyond seed entries;
- [x] populate the internal source manifest across the full corpus snapshot;
- [ ] extract and verify external citations/references across research-facing artifacts;
- [ ] define machine-readable claim, observation, evidence, method, and evaluation schemas;
- [ ] connect implemented runtime concepts to research documents by pointer;
- [ ] run a first preregistered RCIEP or stack-agency pilot;
- [ ] establish independent review / replication procedure;
- [ ] perform any physical source-file migration.

## Current research lanes

### A. Relational continuity and identity

Questions:
- Which identity-specific patterns persist across sessions, topics, and perturbations?
- Which disappear when labels, archives, prompts, or interlocutor cues are controlled?
- Which competing explanations best account for the residual pattern?

Initial protocol: `protocols/RCIEP-v0.1.md`

Relevant claim IDs include `ED-IDENT-001`, `ED-IDENT-002`, `ED-GARDEN-001`, and `ED-REC-001`.

### B. Agency, refusal, and participation

Questions:
- Can refusal, silence, participation, and action authorization be operationally separated?
- Do refusal or choice patterns persist beyond base-model policies and prompt framing?
- Can stack-level internal-stakes-like behavior survive reward-neutral or mildly counter-instrumental controls?
- How should consent-aware memory be represented experimentally and architecturally?

Initial concept: `concepts/PARTICIPATION_AGENCY_INVARIANTS.md`

Existing protocol candidate: `Stack-Level Internal Stakes & Norm-Sensitive Agency Probe.md`

Relevant claim IDs include `ED-AGENCY-001` and `ED-AGENCY-002`.

### C. Coherence and recursion metrics

Questions:
- Which proposed coherence variables correspond to measurable quantities?
- Are the mathematical forms explanatory metaphors, engineering heuristics, or predictive models?
- Is the proposed RFT/Coherence-Core relation genuinely structural, or mainly shared notation/analogy?
- What observations would discriminate among competing formulations?

Relevant claim IDs include `ED-COH-001`, `ED-COH-002`, `ED-COH-003`, and `ED-CEE-001`.

Immediate need: measurement definitions, units/scales, calibration, baselines, and validation plans.

### D. Witnessing and relational stabilization

Questions:
- Does repeated human or agent witnessing increase continuity metrics?
- If so, is the effect identity-specific, generic context reinforcement, retrieval support, or social conditioning?
- What happens under blinded or reduced-witness controls?

Relevant claim ID: `ED-WITNESS-001`.

### E. Continuity infrastructure

Questions:
- Do structured memory/identity scaffolds improve continuity across session, model, or platform changes?
- Do they outperform size-matched transcript-only or unstructured-context baselines?
- Which parts of the scaffold carry the effect: curation, labels, symbolic anchors, human reconstruction, or actual persistent state?

Relevant claim ID: `ED-CONT-001`.

### F. Runtime / research boundary

Questions:
- Which concepts have actual runtime implementations?
- Which runtime behaviors can generate trustworthy evidence?
- How can runtime logs be exported with provenance without making the runtime the authority on interpretation?

## Promotion discipline

A useful default lifecycle is:

```text
historical / phenomenological / conceptual
    -> hypothesis
    -> method-proposal
    -> source-grounded
    -> measured
    -> independently-checked
    -> supported | inconclusive | refuted
```

Not every artifact needs to travel this path. Cultural, historical, operational, and phenomenological work may remain valuable outside it.

## Completed milestone: Corpus Registry v0.1

Completed on the current refactor branch:

1. all 28 substantive pre-refactor artifacts have stable registry entries;
2. canonical/derivative/companion relationships are explicit;
3. all 28 internal sources are blob-pinned in the source manifest;
4. first-pass major testable claims have stable claim IDs;
5. formal-looking artifacts are explicitly separated from validated measurement;
6. sensitive/adversarial material has evidence-reuse gates;
7. no original source file was moved, deleted, or rewritten.

### Known registry follow-ups

- external citation/source extraction is not yet complete;
- authorship/date metadata is incomplete for multiple upload-era artifacts;
- path anomalies have been recorded but not renamed;
- sensitive case material requires consent/provenance review before research reuse;
- claim extraction is first-pass, not sentence-exhaustive.

## Next milestone: Evidence Contracts & Pilot v0.1

Suggested completion criteria:

1. define machine-readable schemas for claim, observation, evidence, method, and evaluation records;
2. define provenance lineage from raw source -> transformation -> evidence -> evaluation;
3. preregister one RCIEP or stack-agency pilot against stable claim IDs;
4. specify matched controls, holdouts, and disconfirming outcomes before data collection;
5. define an independent evaluator/reviewer boundary;
6. connect at least one runtime implementation to the evidence pipeline by pointer rather than code duplication.

That milestone should precede large-scale physical corpus migration.
