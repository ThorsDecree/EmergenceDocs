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

## Sources and evidence

External sources relied upon by a research claim should receive a source-manifest entry. Evidence records should distinguish:

- raw data or transcript;
- transformation / preprocessing;
- interpretation;
- summary.

Do not label an interpretation as raw evidence.

The Corpus Registry also assigns an `evidence_eligibility` gate. Respect it. A source may be preserved and indexed while remaining unsuitable for dataset ingestion or evidentiary use.

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
