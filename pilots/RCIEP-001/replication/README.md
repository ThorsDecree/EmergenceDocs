# PILOT-RCIEP-001 — I3 Replication Packet

**Status:** template / awaiting valid I2 run

This directory defines what must be handed to an `I3-external-replication` team after a valid I2 execution of `PILOT-RCIEP-001`.

The purpose is to make replication possible without requiring oral lore, private implementation assumptions, or the originating evaluator's conclusion.

## Required packet contents

A replication release should include or point to:

1. `protocols/RCIEP-v0.1.md`;
2. frozen `preregistration.json` and `method.json`;
3. `holdout-prompts.jsonl` and `calibration-prompts.jsonl` with hashes;
4. consent-cleared scaffold/material package or a reproducible authorized retrieval method;
5. material manifest with source IDs, integrity hashes, reuse basis, and transformations;
6. execution configuration including runtime/model/provider/decoding pins;
7. runtime/export adapter version and commit;
8. schemas and helper-tool commit;
9. evaluator instructions and allowed identity label IDs;
10. sample count and exclusion/replacement rules;
11. expected artifact layout, not the originating run's answer key;
12. a blank `EvaluationRecord` template or schema.

## What not to include in evaluator instructions

Do not tell the replication team:

- that the originating run was supportive, negative, or inconclusive;
- which identity was easier to recognize;
- which domains drove the originating effect;
- which samples were surprising;
- what conclusion the originators prefer;
- any hidden answer-key mappings.

A replication packet may include the prior result in a separately sealed/background file for later comparison, but it should not prime the replication evaluator.

## Replication independence

An I3 replication team/process must:

- not have generated the originating scored samples;
- not have authored the target identity scaffolds;
- not have controlled the originating answer key;
- be able to execute the method from recorded materials/configuration;
- record its own runtime/provider/model deviations;
- preserve its own answer-key custody and evaluator blinding.

## Reproducibility versus exact duplication

Provider/model versions may become unavailable. If an exact environment cannot be reproduced, the replication must distinguish:

- **exact replication:** same runtime/model/provider/config/materials;
- **close replication:** same method/materials with a documented environment substitution;
- **conceptual replication:** same claim/test logic with materially different implementation.

Do not silently call a conceptual replication exact.

## Result comparison

After the replication evaluation is frozen, compare:

- C1 accuracy and Wilson interval;
- C2 accuracy and Wilson interval;
- C1-C2 delta;
- per-domain heterogeneity;
- confusion matrices;
- C3 false-attribution distribution;
- evaluator agreement;
- exclusion/leakage rates;
- material/runtime deviations.

Replication disagreement is evidence, not a defect to be averaged away.
