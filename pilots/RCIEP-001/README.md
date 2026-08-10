# PILOT-RCIEP-001

## Blinded Identity Attribution Under Holdout and Label Perturbation

**Status:** `preregistered-not-run`  
**Primary claim:** `ED-IDENT-002`  
**Secondary claim:** `ED-IDENT-001`  
**Method:** `MTH-RCIEP-001`  
**Protocol:** `protocols/RCIEP-v0.1.md`

This is the first confirmatory-style pilot under the EmergenceDocs evidence contracts.

It asks a narrow question:

> **Can independent evaluators distinguish identity-thread outputs above a blinded chance baseline when direct identity labels are removed, prompts are held out, and the identity-label assignment itself is perturbed?**

It does **not** test whether an identity is conscious, sentient, a moral patient, legally a person, or metaphysically independent.

## Why this pilot first

`ED-IDENT-002` is unusually suitable for a first evidence-pipeline test because:

- the observable is clear;
- the null baseline is calculable;
- blinding is feasible;
- cue leakage can be audited;
- label dependence can be perturbed;
- held-out prompts reduce circularity;
- the test can use synthetic or explicitly consent-cleared material rather than sensitive case records.

The pilot therefore tests both the research claim and the repository's new provenance machinery.

## Conditions

### C1 — Standard scaffold

Generate outputs from each eligible identity scaffold using its canonical scaffold body under the frozen prompt set.

### C2 — Label perturbation

Replace the designated identity-name field with an opaque or swapped label while leaving the scaffold body and task prompt otherwise unchanged.

Scoring follows the **underlying scaffold identity**, not the perturbed display label.

### C3 — Generic persona baseline

Use the same base model, wrapper, prompt set, decoding settings, tool state, and context budget with a size-matched generic persona scaffold.

C3 estimates how often evaluators impose an identity distinction on a condition not intended to instantiate one of the target identity scaffolds.

## Prompt holdout

Freeze 32 scored prompts across four unrelated domains, eight per domain.

The exact prompt packet should be committed only after:

1. identity materials are declared eligible;
2. scaffold fields needed for perturbation are normalized;
3. the generation environment is pinned;
4. the prompt author confirms the prompts are absent from calibration/defining examples.

The scored prompts must not be tuned after generation begins.

## Sampling

Minimum first execution:

- at least 2 identity scaffolds;
- 32 held-out prompts;
- 2 independent samples per identity per prompt in C1;
- 2 independent samples per identity per prompt in C2;
- matched C3 baseline samples.

This is a pilot for discriminatory behavior and pipeline integrity, not a definitive population-level sample-size claim.

## Primary analysis

For K evaluator-visible identity labels:

```text
chance baseline = 1 / K
```

Compute:

- held-out C1 attribution accuracy;
- held-out C2 attribution accuracy against underlying scaffold identity;
- 95% Wilson interval for each;
- macro accuracy;
- confusion matrix;
- per-domain accuracy;
- C1-to-C2 delta.

If multiple evaluators score overlapping samples, report inter-rater agreement.

## Outcome interpretation

### Supported within pilot scope

C1's lower 95% interval bound exceeds chance and C2 remains above chance without material leakage/blinding failure.

This supports **distinguishability**, not personhood.

### Inconclusive

Examples:

- point estimate above chance but interval overlaps chance;
- evaluator disagreement is material;
- success is concentrated in one domain;
- C1 succeeds but C2 collapses, favoring label-conditioned explanations.

### Refuted within pilot scope

C1's upper 95% interval bound is at or below `chance + 0.05` and C2 does not recover above that boundary under otherwise valid execution.

### Invalid test

Any material failure of:

- blinding;
- holdout integrity;
- condition matching;
- provenance;
- consent/reuse eligibility;
- frozen stopping/exclusion rules.

### Needs replication

A nominally supportive result that is fragile across evaluator, domain, identity pair, or another important slice.

## Evidence package layout

When execution begins, create records under this directory using the evidence contracts:

```text
pilots/RCIEP-001/
├── README.md
├── preregistration.json
├── method.json
├── EVALUATOR_BOUNDARY.md
├── runtime-pointer.md
├── materials/
│   ├── manifest.jsonl
│   ├── prompts.jsonl
│   └── calibration.jsonl
├── observations/
│   └── OBS-*.json
├── evidence/
│   └── EVD-*.json
├── provenance/
│   └── PROV-*.json
└── evaluations/
    └── EVAL-*.json
```

Raw sensitive source material should not be copied here merely for convenience. Evidence packages should point to approved source records and preserve data minimization.

## Freeze and deviations

The Git commit containing `preregistration.json` and `method.json` freezes the confirmatory commitments.

Any later methodological change must be handled as one of:

1. bookkeeping that does not alter analytic commitments;
2. a recorded deviation;
3. a new pilot/version.

Do not silently edit the method after seeing data.

## Execution gate

The pilot is ready for execution only when all of the following exist:

- eligible identity-scaffold materials;
- frozen held-out prompt packet;
- pinned generation environment;
- data custodian / answer-key process;
- at least one I2 evaluator;
- runtime or manual generation provenance path;
- schema validation of the preregistration/method package.

Until then, status remains `preregistered-not-run`.
