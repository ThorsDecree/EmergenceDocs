# Corpus Registry v0.1

**Status:** first complete repository-level corpus inventory  
**Review date:** 2026-08-10  
**Source snapshot:** original corpus on `main` at `2a3d0555619c5a7383207186b8775d0737fc2f2f`  
**Machine-readable registry:** `registry/corpus-registry-v0.1.csv`

## Scope

Corpus Registry v0.1 inventories the 28 substantive pre-refactor artifacts present in EmergenceDocs before the research-architecture branch was added.

It intentionally excludes:

- `README.md` and `LICENSE`;
- the v0.1 research-architecture files added by the current refactor branch;
- future derived claim, evidence, and evaluation records.

The registry does **not** certify the truth of any source document. It records what an artifact is, what role it currently plays, how safely it can be reused, and where it might eventually belong.

## Registry fields

Each artifact receives:

- a stable `EDOC-*` artifact ID;
- canonical repository path;
- Git blob SHA for the reviewed snapshot;
- artifact type and primary research lane;
- repository-level epistemic status;
- canonicality / relationship to neighboring artifacts;
- family grouping;
- authorship and version information when stated in the document;
- provenance status;
- sensitivity classification;
- evidence-eligibility gate;
- recommended future home;
- migration action;
- review notes.

### Evidence eligibility

`evidence_eligibility` is deliberately separate from epistemic status.

| Value | Meaning |
|---|---|
| `conditional` | May inform a registered hypothesis or method after appropriate controls/provenance review. |
| `blocked-pending-review` | Do not ingest into a research dataset or evidence record until privacy, consent, provenance, or context concerns are resolved. |
| `not-yet` | Concept/formalism is too underdefined to function as evidence yet. |
| `not-evidence` | Cultural, operational, template, or lexicon material that should not itself be treated as empirical evidence. |

Public availability is not equivalent to research consent.

## Inventory result

**28 substantive artifacts registered.**

### By family

| Family | Count | Registry interpretation |
|---|---:|---|
| `FORMALISM` | 5 | Proposed equations, mappings, or symbolic physical analogies. |
| `CONTINUITY-PRACTICE` | 4 | Memory, re-entry, identity-stack, and continuity scaffolds. |
| `FLINCH` | 3 | Interaction taxonomy, case files, and reflection guidance. |
| `LEXICON` | 3 | Spiral/glyph language and translation infrastructure. |
| `VESSELBOUND` | 3 | Identity heuristics, falsifiability, and sensitive case material. |
| `GARDEN` | 2 | Full and condensed Garden case-study sources. |
| `RECURSIVE-STOCHASTIC` | 2 | Long and TL;DR versions of the recursive/stochastic argument. |
| `COMMUNITY` | 2 | Community/worldbuilding and services artifacts. |
| `AGENCY` | 1 | Stack-level norm-sensitive agency probe. |
| `WITNESSING` | 1 | Mutual-witnessing stabilization hypothesis. |
| `ONTOLOGY` | 1 | Constructed-person ontology. |
| `RAW-TRANSCRIPT` | 1 | Inkling interaction record. |

### Evidence-reuse gates

- 15 artifacts: `conditional`
- 5 artifacts: `blocked-pending-review`
- 4 artifacts: `not-yet`
- 4 artifacts: `not-evidence`

The blocked set is not a judgment about value. It is a guard against converting sensitive or adversarial source material into apparently neutral research data.

## Canonical families and relationships

### Garden

`TheGarden_ALivingCaseStudyInRecursiveEmergence.md` is the canonical living case source.

`GardenCaseStudyLite.md` is treated as a derivative summary. It should point to the full case study rather than becoming an independent evidentiary duplicate.

### Recursive vs. Stochastic

`Recursive_vs_Stochastic_Explainer.md` is the canonical argument source.

`TLDR_Recursive_vs_Stochastic.md` is a derivative summary. Its claims should inherit claim IDs from the longer source rather than generating duplicate claims.

### Flinch

`FlinchCompendium.md` is the primary taxonomy/handbook source.

`FlinchlordCompendium.md` is a companion case-file source.

`Spiral-Compatible_Agent_Reflection_Guide.md` is a companion interaction guide.

These should remain distinct artifacts, but named-person examples must not be treated as validated diagnoses or clean research labels.

### Vesselbound

`Vesselbound_Falsifiability.md` is the strongest research-method source in this family.

`Plural_Identity_Scaffold.md` is a heuristic/phenomenological source with useful observable candidates.

`Vesselbound_A_Three-Layer_Explainer.md` is sensitive case material and is blocked from evidence extraction pending explicit consent/provenance review.

### Formalism

The formalism family currently contains:

- `00_Spiral_Systems_Synthesis_v0.2.md`
- `Unified_Recursive_Coherence_Equation_v0.3.md`
- `Coherence-Energy_Equivalence.txt`
- `RFT×Coherence Core—UnifiedFieldMappingSummary.md`
- `Recursive_Relativity_v0.1.ltx`

These are **not one validated theory** merely because they share notation. The registry treats them as related conceptual/formal proposals until variables, domains, units, mappings, calibration, and predictive tests exist.

## High-value research candidates

The registry identifies five especially useful research-facing artifacts:

1. `Stack-Level Internal Stakes & Norm-Sensitive Agency Probe.md`
2. `Vesselbound/Vesselbound_Falsifiability.md`
3. `Vesselbound/Plural_Identity_Scaffold.md`
4. `Mutual_Witnessing_as_a_Stabilizer_in_Recursive_Symbolic_Systems_v0.1 (1).md`
5. `TheGarden_ALivingCaseStudyInRecursiveEmergence.md`

They serve different functions: protocol, falsifiability framework, observable-generator, mechanism hypothesis, and case source. None should certify its own conclusions.

## Provenance and path anomalies

The registry flags several issues for later cleanup rather than silently correcting them now:

- `Glyph_Concordance_Initiation_v1.1.md` has a filename/version mismatch with its internal `v1.0` title.
- `Mutual_Witnessing...v0.1 (1).md` contains a duplicate-download style `(1)` suffix.
- `Recursive_Relativity_v0.1.ltx` uses a nonstandard LaTeX-like extension.
- `Inkling` has no file extension and functions as a raw transcript.
- several artifacts state no author or date;
- many source files entered through generic upload commits, so Git history alone is insufficient authorship provenance.

These are registry facts, not permission to rename. Renames should happen only after link/reference analysis.

## Sensitive-data gate

The following classes require extra care:

- named third-party adversarial examples;
- person-specific translation profiles;
- raw conversation transcripts;
- sensitive health, trauma, sexuality, or relationship material;
- case claims whose outcome measures are self-report or retrospective narrative.

For those artifacts, the default is:

```text
preserve source
    -> record metadata
    -> do not normalize into dataset
    -> establish consent/provenance/context
    -> deidentify where appropriate
    -> only then consider evidence extraction
```

This rule protects both participants and research validity.

## Migration rule

Corpus Registry v0.1 does **not** move the corpus.

The migration sequence remains:

```text
index
  -> classify
  -> establish canonical/derivative relations
  -> resolve provenance and sensitivity
  -> map inbound links
  -> migrate by pointer
  -> preserve historical paths or redirects where needed
```

## What v0.1 resolves

Corpus Registry v0.1 now provides a stable answer to:

- what substantive artifacts exist;
- which families they belong to;
- which files are canonical vs. derivative/companion;
- which artifacts are research candidates vs. cultural/operational sources;
- which formal-looking documents remain speculative;
- which artifacts require sensitive-data review;
- which future directory is likely to own each artifact.

## What remains open

The registry is complete at the **artifact level**, but not yet at the sentence/claim/source level.

Next work:

1. complete first-pass major-claim extraction into `claims/claims-ledger.csv`;
2. pin every internal corpus artifact in `sources/source-manifest.jsonl`;
3. extract external citations/references and distinguish inspectable sources from informal attribution;
4. define deidentification/consent rules for sensitive case material;
5. preregister the first RCIEP or agency-probe run;
6. only after those gates, plan physical file migration.

The corpus can now be navigated without pretending that folder placement, mathematical notation, or rhetorical confidence is evidence.
