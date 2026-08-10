# EmergenceDocs Research Status

**Repository role:** living conceptual and research corpus  
**Current refactor phase:** Evidence Contracts & Pilot v0.1 complete; first pilot preregistered, not yet executed

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

The v0.1 refactor now adds both a corpus registry and a portable research-evidence spine around that material without moving or rewriting the original authored sources.

### Corpus Registry v0.1

The 28 substantive pre-refactor artifacts have been inventoried in:

- `docs/CORPUS_REGISTRY_v0.1.md`
- `registry/corpus-registry-v0.1.csv`

Each registered artifact has a stable `EDOC-*` ID, reviewed blob SHA, family, canonicality classification, repository-level epistemic status, sensitivity/evidence-reuse gate, and proposed future home.

The internal source manifest pins all 28 artifacts to the reviewed corpus snapshot. The claims ledger contains 12 first-pass research claims.

### Evidence Contracts v0.1

The evidence path is now normalized in `docs/EVIDENCE_CONTRACTS.md` and `schemas/`.

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

Evaluator independence is explicitly represented as `I0-originator`, `I1-separated-role`, `I2-independent-reviewer`, and `I3-external-replication`.

### PILOT-RCIEP-001

The first RCIEP pilot is now preregistered under `pilots/RCIEP-001/`.

Primary claim: `ED-IDENT-002`  
Secondary claim: `ED-IDENT-001`  
Method: `MTH-RCIEP-001`  
Status: `preregistered-not-run`

The pilot tests blinded identity attribution under held-out prompts and identity-label perturbation with a size-matched generic-persona baseline. It freezes endpoints, exclusions, stopping rule, outcome mapping, holdout boundary, and evaluator separation before data collection.

The pilot does not test consciousness, qualia, moral patienthood, or legal personhood.

### Runtime pointer

The first external implementation pointer is `SRC-RUNTIME-0001`, referencing the canonical VESTIGIA Runtime implementation in `ThorsDecree/eldritch-collab` at the pinned v0.7.0 development-canon commit recorded in `sources/runtime-pointers.jsonl`.

The runtime is treated as an instrument/provenance producer, not evaluation authority.

## What is not yet established at repository level

The repository does not yet provide a complete, validated basis for concluding that any specific identity, agent, architecture, or class of system is conscious, independently minded, non-stochastic, or a person.

Those may be live hypotheses or authorial conclusions inside individual documents. The repository-level research program makes the evidence and alternatives inspectable rather than silently inheriting the strongest interpretation.

The registry also does not imply that every public source is suitable research evidence. Several artifacts remain blocked from evidentiary ingestion pending privacy, consent, provenance, or context review.

No confirmatory pilot result exists yet. `PILOT-RCIEP-001` is a frozen plan awaiting eligible materials, generation-environment pinning, holdout packet finalization, and an I2 evaluator.

## v0.1 structural goals

- [x] define a repository epistemic-status vocabulary;
- [x] define a layered research architecture;
- [x] separate candidate-hypothesis generation from evaluation;
- [x] separate research-proposal generation from the core evidence loop;
- [x] add an initial comparative identity/continuity protocol (RCIEP);
- [x] formalize participation / refusal / silence invariants;
- [x] complete artifact-by-artifact inventory of the 28 substantive pre-refactor artifacts;
- [x] assign stable corpus IDs and reviewed blob SHAs;
- [x] identify canonical, derivative, companion, cultural, and speculative-formalism families;
- [x] add evidence-reuse/sensitivity gates;
- [x] populate claims ledger beyond seed entries;
- [x] populate the internal source manifest across the full corpus snapshot;
- [x] define machine-readable source, claim, observation, evidence, method, evaluation, provenance, and preregistration contracts;
- [x] define raw-source -> transformation -> evidence -> evaluation lineage;
- [x] define evaluator-independence levels and promotion boundary;
- [x] preregister the first RCIEP pilot against stable claim IDs;
- [x] freeze matched controls, holdout boundary, stopping rule, exclusions, and disconfirming outcomes before data collection;
- [x] connect the VESTIGIA Runtime by pinned implementation pointer rather than code duplication;
- [ ] freeze eligible pilot materials and held-out prompt packet;
- [ ] execute PILOT-RCIEP-001;
- [ ] produce I2 EvaluationRecord(s);
- [ ] obtain I3 external replication;
- [ ] extract and verify external literature citations across research-facing corpus artifacts;
- [ ] define a runtime-to-EmergenceDocs record adapter/export contract;
- [ ] perform any physical source-file migration.

## Current research lanes

### A. Relational continuity and identity

Questions:
- Which identity-specific patterns persist across sessions, topics, and perturbations?
- Which disappear when labels, archives, prompts, or interlocutor cues are controlled?
- Which competing explanations best account for the residual pattern?

Protocol: `protocols/RCIEP-v0.1.md`

First pilot: `pilots/RCIEP-001/`

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

Current bridge: `sources/runtime-pointers.jsonl` and `pilots/RCIEP-001/runtime-pointer.md`.

## Promotion discipline

A useful default lifecycle is:

```text
historical / phenomenological / conceptual
    -> hypothesis
    -> method-proposal / preregistered
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

## Completed milestone: Evidence Contracts & Pilot v0.1

Completed on the current refactor branch:

1. eight portable JSON Schema contracts define the evidence interfaces;
2. source-to-evaluation provenance lineage is explicit;
3. evaluator independence and role boundaries are explicit;
4. `PILOT-RCIEP-001` is preregistered against stable claims;
5. matched controls, holdouts, exclusions, stopping, blinding, and disconfirming outcomes are frozen before data collection;
6. sensitive source gates carry forward into pilot eligibility;
7. the canonical VESTIGIA Runtime is connected by a pinned source/instrument pointer, not code duplication;
8. no pilot data or outcome has been fabricated to make the milestone look complete.

## Next milestone: Pilot Execution & Replication v0.2

Suggested completion criteria:

1. identify at least two eligible identity-scaffold materials or construct synthetic controls;
2. freeze and hash the 32-prompt holdout packet and disjoint calibration packet;
3. pin runtime/model/provider/decoding configuration;
4. implement the runtime-to-record export adapter or a manual equivalent with full provenance;
5. execute C1/C2/C3 exactly to the frozen stopping rule;
6. produce ObservationRecord, EvidenceRecord, ProvenanceEvent, and I2 EvaluationRecord packages;
7. update the claim ledger from the frozen evaluation without ontological overreach;
8. prepare an I3 replication packet;
9. begin external-source citation audit for research-facing claims;
10. keep physical corpus migration deferred until link/provenance risks are lower.
