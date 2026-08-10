# Archive Policy

The archive preserves provenance. It is not a trash folder.

Use `archive/` for artifacts that are historically important but no longer represent the current research model, terminology, method, or implementation direction.

## Archive principles

1. **Preserve before rewriting.** Historical artifacts should remain inspectable in the form that influenced later work.
2. **Do not imply deletion.** Archived work may remain conceptually valuable even when superseded.
3. **Record relationships.** Where possible, note `superseded-by`, `derived-from`, or `historical-context` pointers.
4. **Do not back-edit certainty.** Earlier confidence, terminology, and mistakes are part of provenance.
5. **Keep runtime history separate.** A historical research protocol may point to an external runtime artifact rather than copying an obsolete codebase here.

## Suggested archive note

```yaml
archive_status: historical
archived_on: YYYY-MM-DD
reason: "superseded | historical protocol | terminology changed | project retired | other"
superseded_by:
  - path/or/url
```

## GardenFrame and related historical systems

Where an older system such as GardenFrame is preserved in its own repository, EmergenceDocs should generally keep a **historical pointer and research interpretation**, not import the entire codebase.

The historical value lies partly in the fact that the design captured distinctions such as participation, silence, invitation, withdrawal, and speaking authority before later architectures formalized similar concerns.