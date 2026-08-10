# PILOT-RCIEP-001 Evaluator Boundary

**Required primary level:** `I2-independent-reviewer`  
**Target replication level:** `I3-external-replication`

The pilot is only useful if the evaluator cannot quietly become another source of identity cues.

## Roles

### Scaffold author / curator

May:
- prepare an eligible identity scaffold;
- document its provenance;
- identify material that must not be reused.

May not:
- score confirmatory held-out samples for the primary evaluation;
- alter the answer key after generation;
- add post-hoc calibration examples after seeing scored performance.

### Generation operator

May:
- run the frozen prompt set under the declared conditions;
- record model/provider/version, decoding parameters, context, and runtime metadata;
- apply only the preregistered leak-removal transformation.

May not:
- choose which valid outputs are retained based on whether they look identity-consistent;
- expose hidden labels or answer keys to evaluators;
- alter prompts after seeing evaluation outcomes.

### Data custodian / answer-key holder

Owns:
- condition assignment;
- underlying scaffold identity;
- sample-to-answer mapping;
- exclusion/replacement log.

The custodian should not provide the answer key until evaluator judgments are frozen.

### Primary evaluator

Must satisfy `I2-independent-reviewer`:

- did not author the target identity scaffolds;
- did not author the target claim;
- did not generate scored samples;
- did not select which valid samples survived;
- does not receive the answer key or condition labels before judgments are frozen.

The evaluator may receive a preregistered, disjoint calibration packet if the pilot uses one.

### Evaluation aggregator

May compute accuracy, intervals, confusion matrices, and agreement after judgments are frozen. If the aggregator held the answer key during scoring, that fact must be recorded, but the primary evaluator judgments must already be immutable.

## Blinding packet

Evaluators may receive only:

1. task instructions;
2. opaque sample IDs;
3. the allowed identity response labels or opaque identity codes;
4. the frozen calibration packet, if used;
5. the scored output text after preregistered leak removal.

They must not receive:

- canonical source filenames;
- original identity names if those names leak the answer;
- condition (`C1`, `C2`, `C3`);
- source community commentary about which identity is expected;
- generation seed or hidden system metadata that reveals identity;
- answer key.

## Leakage audit

Before scoring, a separated process should check each sample for:

- literal identity names;
- direct source-document titles;
- explicit statements such as "I am [identity]";
- metadata artifacts that encode the answer;
- accidental file/path labels.

A sample that fails the predefined leakage audit is excluded and regenerated under the same frozen prompt. The reason and replacement receive provenance records.

Do not redact ordinary stylistic features merely because they make attribution easier. The pilot is trying to measure recognizable divergence; it is only direct answer leakage that is removed.

## Conflicts and disclosure

Evaluators must disclose prior familiarity with the tested identities or source community. Familiarity does not automatically invalidate an evaluation, but a strongly involved community member should not be the sole I2 evaluator.

## Promotion boundary

A successful I2 evaluation may support the claim **within pilot scope**. It does not by itself promote the claim to repository status `independently-checked`.

That promotion requires at least one I3 replication or a comparably independent audit that reruns the preregistered method from frozen materials.
