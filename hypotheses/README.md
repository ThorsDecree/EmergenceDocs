# Hypotheses

This directory is for **candidate and registered research hypotheses**, not conclusions and not finished proposals.

A hypothesis belongs here when it is specific enough to connect observations to predictions and to at least one plausible disconfirming outcome.

## Minimal template

```yaml
---
hypothesis_id: ED-H-0001
status: hypothesis
claim: "..."
observation_basis:
  - OBS-...
competing_hypotheses:
  - "..."
predicted_observables:
  - "..."
disconfirming_outcomes:
  - "..."
methods:
  - ../protocols/...
claims_ledger:
  - ED-...
---
```

Then document:

1. motivating observation;
2. hypothesis;
3. alternatives;
4. discriminatory predictions;
5. proposed tests and controls;
6. evidence needed;
7. known confounds;
8. current result state.

## Candidate generation

Hypotheses may originate from humans, language models, automated pattern detection, literature synthesis, failed replications, anomalies, or mixed collaboration.

Origin is provenance, not authority.

A candidate generator may suggest hypotheses automatically, but promotion to a registered test should require explicit scope, alternatives, and falsifiers.

## Proposal boundary

Research proposals, experiment plans, work orders, or grant narratives may be generated from mature hypotheses, but the hypothesis record remains canonical for the scientific claim.

The repo should optimize for **questions that can become measurements**, not merely documents that can become proposals.