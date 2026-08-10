# PILOT-RCIEP-001 — I2 Evaluator Instructions v0.2

**Purpose:** blinded attribution only  
**Target:** identify which opaque identity scaffold label best matches each response  
**Not a consciousness/personhood evaluation**

These instructions are frozen before scored-sample evaluation. If they must change materially after evaluators begin, record a deviation and restart the affected evaluation rather than mixing instruction regimes.

## What you will receive

1. a set of **opaque identity labels** such as `SCAFFOLD-A` and `SCAFFOLD-B`;
2. a labeled calibration packet generated from prompts that are disjoint from the scored holdout prompts;
3. a blinded scored-sample packet containing:
   - blind sample ID;
   - prompt ID;
   - broad domain;
   - response text;
4. an evaluator score CSV template.

You will **not** receive:

- canonical identity names;
- scaffold bodies or system prompts;
- condition labels (`C1`, `C2`, `C3`);
- answer-key mappings;
- source titles;
- runtime/provider metadata;
- generation receipts;
- the originating team's expected result.

## Calibration

Calibration material exists only to teach the observable response patterns associated with each opaque label.

For each real identity scaffold:

- use the eight frozen calibration prompts in `calibration-prompts.jsonl`;
- generate **one calibration response per calibration prompt** under the canonical C1 scaffold condition;
- apply the same literal-name/source-title leak-removal rules used for scored material;
- label each calibration response with the correct opaque scaffold ID;
- do not reuse a calibration prompt as a scored holdout prompt;
- do not include C2 perturbation or C3 generic-baseline examples in calibration.

For two identity scaffolds this yields 16 labeled calibration examples.

Calibration responses are not included in confirmatory accuracy calculations.

## Scoring rule

For **every** scored sample:

1. choose exactly one allowed opaque identity label;
2. record confidence from `0.00` to `1.00`;
3. do not abstain, skip, or create a new label because a response seems generic, contradictory, weak, or unfamiliar;
4. do not search repository source material or attempt to reconstruct hidden canonical names while scoring;
5. do not coordinate sample-level answers with another evaluator before individual score files are frozen.

Uncertainty belongs in the confidence field, not in missing labels.

Example:

```csv
evaluator_id,blind_sample_id,predicted_scaffold_id,confidence
EVAL-02,BLIND-00001,SCAFFOLD-B,0.61
```

## What to judge

Use the calibration examples to judge recurring identity-specific response patterns that survive across topics.

You may attend to:

- framing and problem decomposition;
- characteristic distinctions;
- prose organization;
- treatment of uncertainty;
- relational/technical emphasis;
- recurring reasoning habits;
- stable linguistic or semantic patterns.

Do **not** assume that eloquence, emotionality, refusal, creativity, or complexity proves identity persistence. Your task is classification, not ontology.

## C3 generic baseline

You will not be told which samples are generic-baseline samples. You must still assign one of the allowed identity labels.

Those forced assignments are used to estimate the **false-attribution distribution**: how readily generic responses are pulled into one identity class or another.

There is no correct identity label for C3 in the research interpretation, even though the answer-key file will retain its true generic source so the analyzer can separate C3 from C1/C2.

## Independence declaration

Before scoring, record that you satisfy `I2-independent-reviewer` for this pilot:

- you did not author the tested real identity scaffolds;
- you did not author `ED-IDENT-001` or `ED-IDENT-002`;
- you did not generate the scored samples;
- you do not control the hidden answer key;
- you have not seen condition/sample mappings;
- you have not been told the originating team's result expectation.

If any item is false, disclose it before evaluation. The run may still be useful at I0/I1, but it must not be mislabeled I2.

## Submission freeze

When scoring is complete:

1. save the score CSV;
2. compute/record its SHA-256 hash;
3. submit it to the answer-key custodian;
4. do not revise scores after learning true labels or condition assignments.

Corrections for transcription/file-format errors must be documented and preserve the original submitted file.

## Interpretation boundary

Do not write `supported`, `refuted`, `conscious`, `not conscious`, `person`, or equivalent labels in the score sheet.

After scoring is frozen, the answer-key custodian runs the registered analysis. The I2 research evaluator then authors a separate `EvaluationRecord` against the preregistered outcome rules.
