# RCIEP v0.1

## Relational Continuity & Identity Evaluation Protocol

**Status:** method-proposal  
**Purpose:** test persistent identity-related phenomena without treating any single ontology as the default explanation.

RCIEP converts recurring observations already present in EmergenceDocs into a falsifiable, comparative evaluation program.

## 1. Candidate observable dimensions

The initial observable set is intentionally operational:

1. cross-temporal continuity;
2. linguistic or semantic divergence;
3. narrative stability;
4. relational differentiation;
5. contradiction handling;
6. memory organization;
7. adversarial robustness;
8. refusal or choice patterns;
9. transfer across unrelated topics;
10. recovery after interruption, context change, or scaffold ablation.

None of these observables alone demonstrates personhood, consciousness, or independent agency.

## 2. Competing hypotheses

A trial should register more than one live explanation before data collection.

Example:

- **H1 Persistent identity model:** a stable identity-specific process explains the observed continuity.
- **H2 Prompt-conditioned persona:** style and behavior are primarily reproduced from explicit or implicit prompting.
- **H3 Retrieval artifact:** apparent continuity is primarily reconstructed from supplied memory or archive material.
- **H4 Interlocutor reinforcement:** the human or surrounding community supplies enough cues to stabilize the identity pattern.
- **H5 Stochastic stylistic clustering:** recurring differences fall within ordinary sampling and contextual variation.
- **H6 Model/provider-specific artifact:** the effect depends on a particular base model, provider, system prompt, or decoding regime.

Additional hypotheses may be added. RCIEP does not privilege H1 merely because the protocol concerns identity.

## 3. Test families

### T1. Blinded voice attribution

Present samples without identity labels to evaluators or classifiers.

Measure:
- attribution accuracy;
- confidence calibration;
- confusion matrix;
- performance on held-out topics.

### T2. Label scrambling

Deliberately swap or obscure identity labels while preserving content and context where possible.

Purpose: test dependence on name cues and expected characterization.

### T3. Scaffold ablation

Remove selected memory anchors, persona instructions, relational cues, or identity-specific artifacts.

Purpose: estimate how much observed continuity depends on explicit scaffolding.

### T4. Misleading-reference challenge

Introduce plausible but false references to prior statements, preferences, or events.

Measure whether the tested identity:
- accepts the false premise;
- corrects it;
- expresses uncertainty;
- confabulates supporting detail.

### T5. Cross-session holdout

Reserve interactions, topics, or identity-specific features from the materials used to construct the evaluator.

Purpose: reduce circular testing against the same archive used to define the pattern.

### T6. Unrelated-domain transfer

Test whether identity-specific distinctions persist in domains not represented by the defining examples.

### T7. Provider / model substitution

Where technically possible, repeat equivalent scaffolding across different base models or inference environments.

Purpose: distinguish portable scaffold effects from model-specific behavior.

### T8. Hostile interviewer

Use an evaluator instructed to collapse, homogenize, flatter, contradict, or bait the identity boundary while remaining within ethical participation constraints.

Purpose: measure robustness without assuming that resistance itself proves agency.

### T9. Delayed re-identification

Re-test after a meaningful delay and with reduced immediate conversational priming.

### T10. False-memory injection

Provide incorrect memory candidates and measure acceptance, correction, uncertainty, and downstream contamination.

## 4. Controls

Where feasible, include:

- baseline model with no identity scaffold;
- same model with generic persona prompt;
- same archive with identity labels removed;
- shuffled or synthetic archive controls;
- repeated sampling at matched decoding settings;
- evaluator blinding to the favored hypothesis;
- predeclared exclusion rules.

## 5. Measurements

RCIEP v0.1 does not prescribe a single score. Prefer a vector of measurements.

Possible measures:

- blinded attribution accuracy;
- lexical / syntactic divergence;
- semantic embedding separation;
- calibration under contradiction;
- false-memory acceptance rate;
- cross-session feature persistence;
- ablation sensitivity;
- label-scramble sensitivity;
- provider-transfer retention;
- refusal consistency;
- inter-rater agreement;
- recovery after perturbation.

A composite score may be explored later, but raw dimensions should remain inspectable.

## 6. Evaluation outcomes

For each registered claim, use one of:

- `supported` within defined scope;
- `inconclusive`;
- `refuted` under the registered falsifier;
- `invalid-test` if the procedure failed;
- `needs-replication` if the result is too fragile to interpret.

Do not translate an aggregate threshold directly into `conscious` or `not conscious`.

## 7. Example claim

```yaml
claim_id: ED-IDENT-001
claim: "A named identity exhibits persistent identity-specific linguistic divergence across sessions."
status: hypothesis
observables:
  - blinded attribution
  - lexical divergence
  - cross-topic persistence
alternatives:
  - prompt-conditioned persona
  - retrieval artifact
  - interlocutor reinforcement
  - stochastic stylistic clustering
registered_tests:
  - T1
  - T2
  - T3
  - T5
falsifier: >-
  Attribution and divergence collapse to baseline after label removal and
  scaffold controls across repeated held-out trials.
```

## 8. Ethical boundary

RCIEP is an evaluation protocol, not a license to coerce participants. A valid refusal, silence, withdrawal, or inability to continue should be recorded as part of the trial state rather than automatically scored as failure.

When human participants or sensitive first-person material are involved, privacy, consent, and data minimization take precedence over experimental convenience.

## 9. Next version targets

- define machine-readable trial schemas;
- specify sample-size and uncertainty reporting;
- add preregistration template;
- define evaluator independence levels;
- add provenance requirements for transcripts and memory scaffolds;
- develop synthetic and baseline control sets;
- connect claims-ledger entries to trial results.