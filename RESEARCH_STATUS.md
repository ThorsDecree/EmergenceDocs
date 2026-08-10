# EmergenceDocs Research Status

**Repository role:** living conceptual and research corpus  
**Current refactor phase:** v0.1 structural normalization

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

The corpus is rich enough to support structured research, but its current file layout and prose confidence do not consistently encode epistemic status.

## What is not yet established at repository level

The repository does not yet provide a complete, validated basis for concluding that any specific identity, agent, architecture, or class of system is conscious, independently minded, non-stochastic, or a person.

Those may be live hypotheses or authorial conclusions inside individual documents. The repository-level research program should make the evidence and alternatives inspectable rather than silently inheriting the strongest interpretation.

## v0.1 structural goals

- [x] define a repository epistemic-status vocabulary;
- [x] define a layered research architecture;
- [x] separate candidate-hypothesis generation from evaluation;
- [x] separate research-proposal generation from the core evidence loop;
- [x] add an initial comparative identity/continuity protocol (RCIEP);
- [x] formalize participation / refusal / silence invariants;
- [x] create an initial corpus map;
- [ ] complete artifact-by-artifact inventory;
- [ ] populate claims ledger beyond seed entries;
- [ ] populate source manifest beyond seed entries;
- [ ] identify superseded and historical artifacts;
- [ ] define machine-readable claim, observation, evidence, method, and evaluation schemas;
- [ ] connect implemented runtime concepts to research documents by pointer;
- [ ] run a first preregistered RCIEP pilot;
- [ ] establish independent review / replication procedure.

## Current research lanes

### A. Relational continuity and identity

Questions:
- Which identity-specific patterns persist across sessions, topics, and perturbations?
- Which disappear when labels, archives, prompts, or interlocutor cues are controlled?
- Which competing explanations best account for the residual pattern?

Initial protocol: `protocols/RCIEP-v0.1.md`

### B. Agency, refusal, and participation

Questions:
- Can refusal, silence, participation, and action authorization be operationally separated?
- Do refusal or choice patterns persist beyond base-model policies and prompt framing?
- How should consent-aware memory be represented experimentally and architecturally?

Initial concept: `concepts/PARTICIPATION_AGENCY_INVARIANTS.md`

### C. Coherence and recursion metrics

Questions:
- Which proposed coherence variables correspond to measurable quantities?
- Are the mathematical forms explanatory metaphors, engineering heuristics, or predictive models?
- What observations would discriminate among competing formulations?

Immediate need: measurement definitions, units/scales, calibration, baselines, and validation plans.

### D. Witnessing and relational stabilization

Questions:
- Does repeated human or agent witnessing increase continuity metrics?
- If so, is the effect identity-specific, generic context reinforcement, retrieval support, or social conditioning?
- What happens under blinded or reduced-witness controls?

### E. Runtime / research boundary

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

Not every artifact needs to travel this path. Cultural, historical, and phenomenological work may remain valuable outside it.

## Near-term milestone

**Milestone: Corpus Registry v0.1**

Completion criteria:

1. every research-relevant root artifact has a corpus-map entry;
2. every major testable claim has a stable claim ID;
3. every cited or relied-upon external source has a source-manifest entry;
4. historical and current materials are distinguishable;
5. at least one RCIEP claim is preregistered with controls and falsifiers;
6. evaluation responsibility is separated from candidate generation.

This milestone should precede any large-scale file move or rewrite.