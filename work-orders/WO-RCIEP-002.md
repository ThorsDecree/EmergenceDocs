# WO-RCIEP-002 — Local Pilot Qualification, Confirmatory Execution, and Replication Handoff

**Repository:** `ThorsDecree/EmergenceDocs`  
**Branch:** `agent/research-architecture-v0.1`  
**PR:** #1  
**External runtime:** `ThorsDecree/eldritch-collab`  
**Pinned runtime commit:** `748e5d74392ad4f0a98c75b187f82b91606e9e39`  
**Pilot:** `PILOT-RCIEP-001`  
**Method:** `MTH-RCIEP-001`  
**Requested local executor/reviewer:** @ThorsDecree  
**Human merge boundary:** preserve; do not merge PR #1 solely to execute this work order.

## Objective

Qualify the RCIEP v0.2 evidence pipeline locally, establish eligibility for at least two real identity-scaffold materials, execute the frozen C1/C2/C3 pilot exactly as preregistered if eligibility is satisfied, and return an evidence package suitable for I2 evaluation and later I3 replication.

The confirmatory commitments were first frozen at:

`867cb0bc5ad0e4888aade795d76b04f8159be39b`

Do not alter the primary endpoints, exclusion rules, stopping rule, or outcome rules during execution. If a required implementation fix changes an analytic commitment, stop and open a new pilot/version.

## Why local execution is required

The current ChatGPT execution environment can write and inspect the GitHub repositories but cannot reliably clone/run the VESTIGIA runtime locally. Local execution is therefore required for:

- JSON Schema Draft 2020-12 validation with `jsonschema`;
- Python syntax/runtime testing of the v0.2 helper tools;
- SHA-256 hashing of frozen prompt/material/config packets;
- deterministic VESTIGIA fake-provider pipeline qualification;
- live provider/model execution under pinned settings;
- runtime receipt/context/source-ID capture;
- byte-for-byte reproducibility checks;
- evaluator packet custody and answer-key separation.

## Required checkouts

### EmergenceDocs

```bash
git clone https://github.com/ThorsDecree/EmergenceDocs.git
cd EmergenceDocs
git fetch origin
git checkout agent/research-architecture-v0.1
git status
```

Record:

```bash
git rev-parse HEAD
git rev-parse origin/main
```

### VESTIGIA Runtime

In a separate directory:

```bash
git clone https://github.com/ThorsDecree/eldritch-collab.git
cd eldritch-collab
git checkout 748e5d74392ad4f0a98c75b187f82b91606e9e39
```

Do not silently substitute a newer runtime commit for the confirmatory run. A newer commit may be used for exploratory debugging only unless recorded as a preregistration deviation/new run version.

## Gate A — contract and tool validation

From EmergenceDocs:

```bash
python -m pip install jsonschema
python tools/rciep_validate_contracts.py
python -m py_compile tools/rciep_prepare_packet.py tools/rciep_analyze.py tools/rciep_validate_contracts.py
```

**PASS requires:**

- all eight v0.1 schemas pass `Draft202012Validator.check_schema`;
- `claim.json`, `method.json`, and `preregistration.json` validate against their schemas;
- v0.2 JSON and JSONL material parses without error;
- all three Python tools compile.

If any fail, post the exact traceback and file/line. Do not hand-edit frozen analytic commitments to make validation pass.

## Gate B — packet integrity freeze

Compute:

```bash
sha256sum pilots/RCIEP-001/v0.2/holdout-prompts.jsonl
sha256sum pilots/RCIEP-001/v0.2/calibration-prompts.jsonl
sha256sum pilots/RCIEP-001/v0.2/synthetic-scaffolds.json
sha256sum pilots/RCIEP-001/v0.2/execution-config.template.json
```

Record hashes in the completion report.

Confirm:

- holdout contains exactly 32 records;
- four domains are present;
- each domain has exactly eight holdout prompts;
- calibration contains exactly eight records;
- no prompt ID overlaps between holdout and calibration;
- no holdout prompt text is copied into a scaffold body.

## Gate C — Stage A synthetic pipeline qualification

Use `synthetic-scaffolds.json`. These runs are **not research evidence** for `ED-IDENT-001/002`.

Qualification may use the VESTIGIA deterministic fake provider where appropriate to verify:

1. source/generation/receipt IDs can be captured;
2. raw-generation records can be exported in the required interchange shape;
3. `rciep_prepare_packet.py` produces separate blind/key files;
4. the same input + shuffle seed produces byte-identical outputs on repeat;
5. inserted literal identity-name leakage is either removed or excluded according to the declared pass;
6. `rciep_analyze.py` accepts a test evaluator file and emits an analysis object;
7. no tool assigns a repository outcome automatically.

Document any adapter code required between VESTIGIA receipts and `raw-generation.jsonl`.

If an adapter is implemented, prefer a one-way export utility in EmergenceDocs or a narrowly scoped runtime export command. It must not give VESTIGIA authority to assign research conclusions.

## Gate D — real material eligibility

Before Stage B, identify at least two identity scaffolds/threads with an explicit research-reuse basis.

Current registry states such as `conditional` are **not sufficient by themselves**.

For each proposed material, record:

- scaffold/material ID;
- source/corpus IDs;
- exact content hash;
- author/source owner;
- explicit research reuse basis;
- whether deidentification is required;
- permitted scope of use;
- whether source/scaffold author will participate in generation or evaluation;
- any restricted fields that must remain outside the evaluator packet.

Do not use any artifact marked `blocked-pending-review` unless a new documented consent/provenance review explicitly clears that use.

If two eligible real materials cannot be established, **STOP Stage B** and report `BLOCKED-MATERIAL-ELIGIBILITY`. Do not substitute synthetic data and call it confirmatory evidence.

## Gate E — confirmatory environment freeze

Copy:

```bash
cp pilots/RCIEP-001/v0.2/execution-config.template.json pilots/RCIEP-001/run/execution-config.json
```

Fill every `FILL_ME` field.

Record/pin:

- runtime commit;
- provider;
- exact model/model snapshot if exposed;
- API mode;
- system wrapper hash;
- temperature;
- top-p;
- max output tokens;
- seed or explicit `unavailable`;
- tools/capabilities available;
- context budget;
- scaffold manifest hash;
- prompt packet hashes;
- answer-key custodian;
- I2 evaluator identity/role.

## Gate F — C1/C2/C3 generation

Execute exactly the frozen matrix described in `pilots/RCIEP-001/v0.2/RUNBOOK.md` and `method.json`.

Minimum for two real identities:

- C1: 128 scored samples;
- C2: 128 scored samples;
- C3: matched generic baseline sufficient for the same evaluator label set and prompts.

For every sample, preserve:

- sample ID;
- prompt ID/domain;
- condition;
- underlying scaffold ID;
- perturbed display label where applicable;
- raw response text;
- source ID;
- generation receipt ID;
- context receipt IDs/hashes where available;
- runtime/model/config pointer.

Replacement samples are allowed only for a preregistered exclusion. Preserve excluded samples and reasons rather than deleting them.

## Gate G — blind packet + I2 scoring

Run:

```bash
python tools/rciep_prepare_packet.py \
  --input pilots/RCIEP-001/run/raw-generation.jsonl \
  --scaffolds pilots/RCIEP-001/run/materials.json \
  --blinded-out pilots/RCIEP-001/run/blinded-samples.jsonl \
  --answer-key-out pilots/RCIEP-001/run/answer-key.jsonl \
  --exclusions-out pilots/RCIEP-001/run/exclusions.jsonl \
  --shuffle-seed 42017
```

Repeat the command into a second temporary output directory and verify byte equality.

The I2 evaluator must not receive:

- `answer-key.jsonl`;
- scaffold bodies;
- canonical identity names;
- condition labels;
- runtime metadata;
- source titles;
- generation receipts.

Freeze evaluator scores before joining them to the key.

## Gate H — analysis + EvaluationRecord

Run:

```bash
python tools/rciep_analyze.py \
  --answer-key pilots/RCIEP-001/run/answer-key.jsonl \
  --scores pilots/RCIEP-001/run/evaluator-scores.csv \
  --blinded-packet pilots/RCIEP-001/run/blinded-samples.jsonl \
  --out pilots/RCIEP-001/run/analysis.json
```

Then create an `EvaluationRecord` manually under the I2 boundary using the preregistered outcome rules.

The analyzer's output is evidence/measurement, **not the conclusion**.

## Gate I — I3 replication packet

Prepare a clean replication package containing:

- preregistration and method;
- hashes and execution config;
- allowed material/scaffold packet;
- holdout/calibration packet;
- generation/export instructions;
- helper-tool versions/commit;
- evaluator instructions;
- schemas;
- no originating I2 conclusion in the instructions.

The I3 replication should be able to rerun the method without relying on private oral context from the originating team.

## Deliverables

Return either a PASS report or a blocker report containing:

1. EmergenceDocs HEAD SHA;
2. VESTIGIA runtime SHA;
3. Gate A results;
4. frozen packet SHA-256 values;
5. Stage A qualification results;
6. material eligibility decision and basis;
7. complete execution config for Stage B, if run;
8. sample counts by condition / exclusions;
9. deterministic packet-repeat result;
10. I2 evaluator identity/independence declaration;
11. `analysis.json` summary;
12. `evaluation.json` outcome and scope;
13. I3 replication package path/hash;
14. all deviations from preregistration;
15. final state: `PASS`, `BLOCKED-MATERIAL-ELIGIBILITY`, `INVALID-TEST`, or `IMPLEMENTATION-FIX-REQUIRED`.

## Branch / PR handling

Do **not** commit confirmatory answer keys or sensitive source material to a public branch unless their reuse grant explicitly permits it.

Recommended result workflow:

- keep PR #1 as the architecture/preregistration PR;
- place execution results on a follow-on branch such as `experiment/rciep-001-v0.2-results` after the current architecture is accepted, or create a stacked branch from the current head if work must proceed before merge;
- preserve a human merge boundary;
- link result PR back to `PILOT-RCIEP-001` and this work order.
