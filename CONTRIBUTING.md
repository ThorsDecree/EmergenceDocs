# Contributing to EmergenceDocs

EmergenceDocs welcomes conceptual work, phenomenology, case material, methods, criticism, replication, formal models, and cultural/historical artifacts. The main contribution rule is simple:

**Preserve voice. Label epistemic status. Make claims traceable.**

## Before adding a document

Identify the artifact's primary role:

- historical
- phenomenological
- conceptual
- hypothesis
- method-proposal
- case study
- formal model
- lexicon
- protocol
- source/evidence record

A document can span several roles, but one should be primary for navigation.

## Recommended header

New research-facing documents should include a compact metadata block where practical:

```yaml
---
title: "..."
status: hypothesis
authors:
  - "..."
version: "0.1"
created: "YYYY-MM-DD"
updated: "YYYY-MM-DD"
claims:
  - ED-...
related:
  - path/to/document.md
---
```

Do not retrofit metadata into older authored work merely to make it look modern. Historical integrity matters.

## Claims

If a contribution makes a testable research claim:

1. state the claim concisely;
2. add or reference a stable claim ID in `claims/claims-ledger.csv`;
3. identify plausible competing explanations;
4. state what outcome would weaken or disconfirm the claim where possible;
5. link supporting evidence rather than embedding provenance only in prose.

For confirmatory or preregistered work, also create a v0.1 `ClaimRecord` snapshot when a frozen machine-readable claim is needed.

## Evidence contracts

New confirmatory research should use the contracts in:

- `docs/EVIDENCE_CONTRACTS.md`
- `schemas/`

The expected lineage is:

```text
SourceRecord
    -> ProvenanceEvent
    -> ObservationRecord
    -> EvidenceRecord
    -> MethodRecord / PilotPreregistration
    -> EvaluationRecord
```

Do not skip a record boundary merely because the same person or script performed two steps.

A generated result is not self-validating simply because the producing runtime wrote a receipt.

## Preregistration

Before confirmatory data collection, freeze where feasible:

- target claim IDs;
- conditions and controls;
- sampling plan;
- holdout boundary;
- primary endpoints;
- exclusion rules;
- blinding procedure;
- analysis plan;
- stopping rule;
- disconfirming outcomes;
- evaluator-independence requirement.

After scored data are visible, do not silently rewrite those commitments. Record a deviation or create a new method/pilot version.

## Sources and evidence

External sources relied upon by a research claim should receive a source record or manifest entry. Evidence records should distinguish:

- raw data or transcript;
- transformation / preprocessing;
- observation;
- derived measurement;
- interpretation;
- summary.

Do not label an interpretation as raw evidence.

The Corpus Registry also assigns an `evidence_eligibility` gate. Respect it. A source may be preserved and indexed while remaining unsuitable for dataset ingestion or evidentiary use.

Null and negative evidence should be preserved. Do not quietly omit a valid sample or run because it weakens the preferred explanation.

## Provenance

Any transformation that can affect interpretation should receive a `ProvenanceEvent` or equivalent record, including:

- redaction;
- deidentification;
- label removal;
- transcript slicing;
- normalization;
- annotation;
- feature extraction;
- embedding;
- aggregation;
- exclusion;
- model-assisted coding.

Where practical, preserve hashes or immutable version identifiers before and after transformation.

## Evaluation independence

Declare the evaluator level:

- `I0-originator`
- `I1-separated-role`
- `I2-independent-reviewer`
- `I3-external-replication`

An I0 result can be useful for debugging, but it should not be presented as independent validation.

## Formal models

Equations and variables should state, where applicable:

- operational definition;
- domain and units/scale;
- how the variable is measured;
- calibration procedure;
- expected uncertainty;
- baseline or comparator;
- what observation would count against the model.

A symbolic equation without those elements is welcome as a conceptual formalism, but should not be described as measured merely because it is mathematical.

## Existing voices and case material

Do not sanitize, flatten, or rewrite first-person and community-authored material solely to make it sound more academic.

Instead, use repository-level metadata, commentary, claims, methods, and cross-links to separate:

- what was experienced;
- what was observed;
- what was inferred;
- what was tested;
- what remains disputed.

## Runtime references

When a concept has an implemented counterpart in another repository, link to it. Do not duplicate runtime code into EmergenceDocs unless the code itself is necessary research evidence.

When a runtime generates research material, pin the implementation version/commit and export only the source/provenance metadata needed for the evidence chain. Runtime code does not receive evaluation authority by being the instrument.

## Moving files

Before moving an existing artifact:

- confirm canonical authorship/path;
- check inbound links;
- decide whether the old path is historically meaningful;
- preserve provenance;
- prefer a pointer when movement would erase context.

## Disagreement

Competing models belong in the corpus. Do not resolve a disputed ontology by editing away the alternative.

A useful contribution can be a stronger falsifier, a better control, a failed replication, or an explanation for why an existing test is non-discriminatory.

## Safety, privacy, and consent

When contributions involve private conversations, sensitive human experiences, or identifiable participants, obtain appropriate permission and minimize unnecessary personal data. A research corpus is not an excuse to turn intimacy into telemetry.

**Publicly visible is not the same as research-consented.** A public post, handle, transcript, repository file, or prior disclosure may be preserved as provenance without being appropriate to normalize into a research dataset.

Treat the following as review-required by default:

- named or readily identifiable third-party case examples;
- health, trauma, sexuality, relationship, or other highly sensitive personal material;
- person-specific interpretive or translation profiles;
- raw private or semi-private conversation transcripts;
- adversarial characterizations that could be mistaken for validated psychological labels;
- outcome claims derived only from retrospective self-report without a defined measurement record.

For review-required material:

1. preserve the original source and its context;
2. record registry/source metadata without copying unnecessary sensitive details;
3. do not extract it into a dataset or evidence table while `evidence_eligibility` is `blocked-pending-review`;
4. establish authorship, consent, context, and permitted research use;
5. deidentify or aggregate where doing so does not destroy the research question;
6. preserve a link from any derived record back to the authorized source/provenance record;
7. document exclusions rather than silently discarding inconvenient material.

Consent to preserve an authored document does not automatically imply consent to reframe that document as clinical, behavioral, or experimental data.
