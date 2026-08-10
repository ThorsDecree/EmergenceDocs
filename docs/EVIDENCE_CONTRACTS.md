# Evidence Contracts v0.1

**Status:** architecture / normative interface  
**Milestone:** Evidence Contracts & Pilot v0.1

EmergenceDocs now has enough corpus structure to distinguish source artifacts and claims. The next requirement is to make the path from source to conclusion auditable.

This document defines the repository's portable research records and provenance rules. The contracts are intentionally implementation-neutral: another repository or runtime may emit compatible records without becoming the authority that interprets them.

## Core rule

> **Raw source is not observation. Observation is not evidence. Evidence is not evaluation. Evaluation is not ontology.**

The records are separated so that a transformation, redaction, scoring procedure, or interpretation cannot silently disappear inside a prose summary.

## Record types

| Record | Purpose | Canonical schema |
|---|---|---|
| `SourceRecord` | Stable pointer to a corpus artifact, external source, runtime record, dataset, or synthetic control | `schemas/source-record.schema.json` |
| `ClaimRecord` | Stable research assertion with alternatives and falsifiers | `schemas/claim-record.schema.json` |
| `ObservationRecord` | Bounded report of what was recorded or measured | `schemas/observation-record.schema.json` |
| `EvidenceRecord` | Claim-relevant evidence object derived from observations or sources | `schemas/evidence-record.schema.json` |
| `MethodRecord` | Predeclared procedure, controls, metrics, exclusions, and analysis | `schemas/method-record.schema.json` |
| `EvaluationRecord` | Outcome assigned under a declared method by a declared evaluator | `schemas/evaluation-record.schema.json` |
| `ProvenanceEvent` | One capture, transform, redact, derive, aggregate, or evaluation step | `schemas/provenance-event.schema.json` |
| `PilotPreregistration` | Frozen trial scope connecting claims, method, materials, holdouts, and evaluator boundary | `schemas/pilot-preregistration.schema.json` |

All schemas use JSON Schema Draft 2020-12 and `schema_version: "0.1"`.

## Identifier namespaces

Recommended stable prefixes:

```text
ED-*        registered claims already present in claims/claims-ledger.csv
OBS-*       observations
EVD-*       evidence records
MTH-*       methods
EVAL-*      evaluations
PROV-*      provenance events
PILOT-*     preregistered pilots
SRC-ED-*    internal corpus source-manifest records
SRC-RUNTIME-* external/runtime implementation pointers
EDOC-*      corpus-registry artifacts
```

IDs identify records, not truth. A record that is later invalidated keeps its ID.

## Required lineage

The minimum inspectable evidence chain is:

```text
SourceRecord
  corpus artifact / runtime record / dataset / synthetic control
        |
        v
PROV capture/import
        |
        v
ObservationRecord
        |
        +----> optional PROV redact/deidentify/transform
        |
        v
EvidenceRecord
        |
        v
MethodRecord + preregistration
        |
        v
EvaluationRecord
        |
        v
claim ledger update / research synthesis
```

A derived evidence object must identify the observations and provenance events from which it came. An evaluation must identify the evidence and method it used.

## Raw-source integrity

Where practical, raw or minimally transformed source records should carry:

- source or artifact ID;
- immutable Git blob SHA, commit SHA, file checksum, content hash, or equivalent integrity marker;
- capture/import time where known;
- producing environment or runtime where relevant;
- consent/reuse status;
- sensitivity classification.

A source may remain historically valuable while being ineligible for research reuse.

The existing `sources/source-manifest.jsonl` remains the canonical inventory for the 28 pre-refactor corpus artifacts. New external implementation pointers may use v0.1 `SourceRecord` objects, such as `sources/runtime-pointers.jsonl`.

## Transformation rule

Any operation that can change interpretation must be explicit provenance. Examples:

- label removal;
- deidentification;
- transcript slicing;
- normalization;
- tokenization;
- feature extraction;
- embedding;
- aggregation;
- exclusion;
- redaction;
- model-assisted coding;
- human annotation.

The transformation record should state inputs, outputs, actor/tool, parameters or rules, and whether the operation is reversible.

## Observation discipline

An `ObservationRecord` should be as close as practical to a bounded report of what was recorded.

Prefer:

```text
OBS: On 18/24 blinded trials, evaluator E3 assigned sample family A correctly.
```

over:

```text
OBS: Identity A proved that it persisted.
```

The second sentence is an interpretation and belongs in evaluation or synthesis.

## Evidence discipline

An `EvidenceRecord` packages claim-relevant information without deciding the claim outcome. It may contain:

- a raw observation;
- a derived measurement;
- an aggregate statistic;
- a comparison against a control;
- a failure or null result.

Null and negative evidence are first-class records.

Evidence eligibility is independent of repository visibility. `blocked-pending-review` corpus artifacts must not be normalized into evidence merely because they are public.

## Method discipline

A `MethodRecord` should exist before confirmatory data collection whenever feasible and must specify:

- target claim IDs;
- test family / protocol;
- conditions and controls;
- sample construction;
- holdout boundary;
- metrics;
- exclusion rules;
- blinding;
- analysis plan;
- stopping rule;
- disconfirming outcomes;
- evaluator-independence requirement.

Changes after preregistration are allowed, but they become deviations rather than invisible edits.

## Evaluation outcomes

Repository-level evaluation outcomes are:

- `supported`;
- `inconclusive`;
- `refuted`;
- `invalid-test`;
- `needs-replication`.

An evaluation should name its scope. `supported` means supported under the declared test conditions, not universally established.

## Evaluator independence levels

The pilot system uses explicit independence levels:

| Level | Minimum condition |
|---|---|
| `I0-originator` | evaluator may be a claim or method originator; useful for debugging only |
| `I1-separated-role` | evaluator did not generate the tested samples and did not control hidden labels |
| `I2-independent-reviewer` | I1 plus evaluator did not author the target scaffold/claim and was not involved in preregistered data generation |
| `I3-external-replication` | independent team/process reproduces the method from the preregistration and receives only declared materials |

A claim should not reach repository status `independently-checked` from an I0 evaluation.

## Consent and sensitivity

Every source/observation/evidence path involving human or person-specific material should declare a reuse basis such as:

- `public-nonsensitive`;
- `explicit-research-consent`;
- `deidentified-with-consent`;
- `synthetic`;
- `blocked-pending-review`.

The contracts do not convert consent into a checkbox ritual. If a source's consent or context is unclear, preserve it as source material and stop the evidence path until reviewed.

## Runtime boundary

A runtime may produce raw records, observations, or instrument metadata. It must not certify the research conclusion simply because it produced the data.

Portable interface:

```text
runtime / instrument
    -> SourceRecord + provenance
    -> EmergenceDocs ObservationRecord / EvidenceRecord
    -> separated EvaluationRecord
```

This keeps implementation authority distinct from evaluation authority.

The first registered runtime pointer is `SRC-RUNTIME-0001`, referencing the canonical VESTIGIA Runtime implementation in `ThorsDecree/eldritch-collab` at the pinned development-canon commit recorded in `sources/runtime-pointers.jsonl`.

The runtime already exposes useful instrument-side primitives such as original-source hashes, stable IDs, source trust classification, context/action receipts, append-only state events, and provenance inspection. Those can feed the evidence pipeline, but they do not become conclusions by virtue of being runtime-native.

## v0.1 pilot

The first preregistered pilot is `PILOT-RCIEP-001`, documented under:

- `pilots/RCIEP-001/README.md`
- `pilots/RCIEP-001/claim.json`
- `pilots/RCIEP-001/preregistration.json`
- `pilots/RCIEP-001/method.json`
- `pilots/RCIEP-001/EVALUATOR_BOUNDARY.md`
- `pilots/RCIEP-001/runtime-pointer.md`

It targets `ED-IDENT-002` with `ED-IDENT-001` as a linked secondary claim and tests blinded distinguishability under held-out prompts and label perturbation. The pilot is preregistered but **not yet executed**.

The confirmatory commitments were first frozen in commit `867cb0bc5ad0e4888aade795d76b04f8159be39b`; the current preregistration records that commit as bookkeeping without changing those commitments.

## Freeze rule

A preregistration must freeze the confirmatory endpoints, exclusion rules, stopping rule, outcome mapping, and evaluator boundary before scored data are inspected.

After that point:

- bookkeeping corrections may be made if they do not alter analytic commitments;
- material method changes must be logged as deviations;
- substantial redesign becomes a new method/pilot version.

A weak or inconvenient result is never a reason to silently rewrite the preregistration.

## Compatibility principle

These contracts are deliberately small. Future versions may add richer statistics, cryptographic attestations, external registry pointers, or automated validation, but v0.1 prioritizes a readable invariant:

> **Anyone reviewing a conclusion should be able to walk backward to the method, evidence, observations, transformations, and source material without guessing which step changed what.**
