# RCIEP v0.1

## Relational Continuity & Identity Evaluation Protocol

**Status:** method-proposal with first preregistered pilot  
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

Corpus material marked `blocked-pending-review` is not eligible for pilot evidence merely because it is public.

## 9. Evidence-contract integration

RCIEP trials should use the portable records defined in `docs/EVIDENCE_CONTRACTS.md`:

```text
SourceRecord
    -> ProvenanceEvent
    -> ObservationRecord
    -> EvidenceRecord
    -> MethodRecord / PilotPreregistration
    -> EvaluationRecord
```

A scored result should therefore be reproducible as a chain of records rather than only a paragraph in a case study.

Required confirmatory trial properties include:

- stable claim IDs;
- source/material identifiers and reuse gates;
- frozen method and holdout plan;
- provenance for label removal, redaction, feature extraction, and exclusions;
- explicit evaluator-independence level;
- recorded method deviations;
- evidence records for null/negative results as well as positive results.

## 10. First preregistered pilot

`PILOT-RCIEP-001` is the first frozen RCIEP pilot:

**Title:** Blinded Identity Attribution Under Holdout and Label Perturbation  
**Primary claim:** `ED-IDENT-002`  
**Secondary claim:** `ED-IDENT-001`  
**Method:** `MTH-RCIEP-001`  
**Frozen confirmatory commitments:** `867cb0bc5ad0e4888aade795d76b04f8159be39b`

Files:

- `pilots/RCIEP-001/README.md`
- `pilots/RCIEP-001/claim.json`
- `pilots/RCIEP-001/preregistration.json`
- `pilots/RCIEP-001/method.json`
- `pilots/RCIEP-001/EVALUATOR_BOUNDARY.md`
- `pilots/RCIEP-001/runtime-pointer.md`

The pilot uses T1, T2, and T5 with a matched generic-persona baseline and requires an `I2-independent-reviewer` for primary evaluation.

Status: **preregistered-not-run**.

## 11. Next version targets

Completed in Evidence Contracts & Pilot v0.1:

- machine-readable research-record schemas;
- preregistration schema and first frozen pilot;
- evaluator-independence levels;
- provenance requirements for sources, transformations, and evidence;
- claim-to-method linkage for the first pilot;
- runtime implementation pointer without code duplication.

Still open for later RCIEP versions:

- execute PILOT-RCIEP-001;
- define power/sample-size procedures for confirmatory multi-identity studies;
- formalize calibration-packet construction;
- add provider/model-substitution pilot;
- add scaffold-ablation pilot;
- add false-memory/adversarial pilot;
- obtain I3 external replication;
- connect completed trial results back to the claims ledger automatically.
