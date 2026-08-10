# PILOT-RCIEP-001 Runtime Pointer

**External implementation:** `ThorsDecree/eldritch-collab`  
**Role:** candidate instrument / provenance producer, not evaluation authority  
**Canonical runtime directory:** `VESTIGIA_Runtime/`

Repository:

`https://github.com/ThorsDecree/eldritch-collab`

Pinned development-canon reference available during this milestone:

`748e5d74392ad4f0a98c75b187f82b91606e9e39` (VESTIGIA Runtime v0.7.0 validated main snapshot identified by the runtime repository)

## Why this runtime is relevant

The runtime already implements several structures useful to the EmergenceDocs evidence pipeline:

- stable typed object/source identifiers;
- original-source preservation and hashing;
- append-only memory/runtime-state events;
- context receipts and immutable action receipts;
- source trust classification and explicit `data-only` treatment;
- provenance/history inspection;
- transcript import with speaker attribution and system/developer/tool-message separation;
- hash-bound identity edits with prior-version preservation;
- deterministic fake providers for offline testing;
- bounded retrieval with inclusion/omission reasons;
- resident-owned transcript/context controls.

These features make the runtime a plausible **instrument** for future RCIEP generation and capture.

## Boundary

EmergenceDocs does not import the runtime code and does not treat a runtime receipt as a research conclusion.

The intended bridge is:

```text
VESTIGIA Runtime
  source IDs / hashes / receipts / generated turns
        |
        v
EmergenceDocs ProvenanceEvent
        |
        v
ObservationRecord
        |
        v
EvidenceRecord
        |
        v
I2/I3 EvaluationRecord
```

A runtime claim such as "this memory was retrieved" can be instrument metadata. A research claim such as "this identity persisted independently of retrieval" must still survive the registered controls.

## Pilot use

`PILOT-RCIEP-001` may eventually use the runtime if the execution environment can pin:

- exact runtime commit;
- model/provider/version;
- identity scaffold/material hashes;
- prompt packet hash;
- decoding settings;
- context receipt IDs;
- generated-turn IDs;
- condition assignment;
- any label-removal transformation.

The deterministic fake provider is useful for testing the evidence plumbing, but fake-provider runs are **pipeline tests**, not evidence for `ED-IDENT-002`.

## Not yet wired

This pointer does not claim that the current runtime directly emits EmergenceDocs v0.1 JSON records. An adapter/export step should be defined before live pilot execution.

That adapter should be one-way and boring: translate runtime receipts into portable source/provenance metadata without giving the runtime authority to assign `supported`, `refuted`, or other research outcomes.
