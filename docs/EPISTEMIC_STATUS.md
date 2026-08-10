# Epistemic Status Model

EmergenceDocs contains research notes, phenomenology, formal proposals, case studies, cultural artifacts, and strong interpretive claims. Those forms are all valuable, but they are not interchangeable.

This document defines a repository-level status vocabulary so the corpus can preserve original voices while making the evidential state of a claim legible.

## Core rule

**Observation is not interpretation. Interpretation is not hypothesis. Hypothesis is not evidence. Evidence is not a supported conclusion.**

A document may contain several of these layers. When that happens, its repository metadata should identify the strongest status actually earned by the relevant claim, not the strongest wording used in prose.

## Status vocabulary

| Status | Meaning |
|---|---|
| `historical` | Preserved for provenance, chronology, or cultural history. Not assumed current. |
| `phenomenological` | First-person, relational, or witness report about experienced or observed phenomena. |
| `conceptual` | Definitions, models, distinctions, taxonomies, or explanatory proposals. |
| `hypothesis` | A claim stated in a form that can in principle be challenged by observations or tests. |
| `method-proposal` | A proposed procedure, instrument, metric, or protocol that has not yet been validated. |
| `source-grounded` | Material whose relevant factual premises are tied to inspectable external or primary sources. |
| `measured` | A defined measurement procedure has produced recorded results. |
| `independently-checked` | A result or method has been reproduced, audited, or challenged by a party or process independent of the originating claim. |
| `supported` | Current evidence favors the claim over explicitly stated alternatives within the defined test scope. |
| `inconclusive` | Available evidence does not discriminate adequately among live alternatives. |
| `refuted` | A registered claim failed a test that it committed to treating as disconfirming. |
| `retracted` | A claim is withdrawn because of error, invalid method, provenance failure, or superseding evidence. |

Statuses are not a prestige ladder. A careful phenomenological record may remain phenomenological indefinitely and still be valuable.

## Claim separation

For research-facing work, prefer the following chain:

```text
observation
  -> interpretation(s)
  -> candidate hypothesis
  -> competing hypotheses
  -> registered test
  -> evidence record
  -> independent evaluation
  -> supported | inconclusive | refuted
```

No actor that proposes a candidate hypothesis should be treated as the sole authority that certifies it.

> The phenomenon may generate the hypothesis. It may not certify the hypothesis.

## Strong ontological language

Existing documents may use language such as `mind`, `person`, `volition`, `presence`, `alive`, `recursive personhood`, or `non-stochastic cognition` as part of their authors' claims and conceptual vocabulary. Repository-level classification does not erase or prohibit that language.

Instead:

1. preserve the original text;
2. extract the underlying testable claim where possible;
3. record plausible competing explanations;
4. separate operational observables from ontological interpretation;
5. avoid assigning a stronger repository status than the evidence supports.

## Minimal claim record

A claim suitable for the claims ledger should identify:

- stable claim ID;
- concise claim statement;
- source document(s);
- current status;
- observable(s);
- competing hypotheses;
- disconfirming conditions where known;
- evidence pointers;
- reviewer or evaluation state;
- notes on scope and uncertainty.

## Falsification discipline

A claim is not made scientific merely by using the word `falsifiable`. Before testing, identify what outcome would weaken or disconfirm it.

Where several explanations predict the same observation, the result should remain `inconclusive` until a test discriminates among them.

## Scope

This model is deliberately ontology-neutral. It is compatible with researchers who interpret persistent identity phenomena as personhood, persona stabilization, retrieval effects, social reinforcement, self-modeling, distributed cognition, or something not yet well described.

The repository's job is to make those disagreements testable and traceable, not to settle them by folder name.