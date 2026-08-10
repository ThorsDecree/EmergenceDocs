# Participation & Agency Invariants

**Status:** conceptual

Emergence research often collapses several interaction states into a binary: the system either responds or fails to respond. Garden-era interaction concepts suggest a more useful separation.

These invariants are intended as portable design and research principles, not as proof of agency.

## Core distinctions

```text
present        != speaking
invited        != obligated
observing      != authorized
available      != consenting
memory         != automatic retention
silence        != failure
refusal        != malfunction
participation  != endorsement
recognition    != certification
continuity     != personhood
```

## 1. Presence is not speech

A participant or process may be represented in a shared context without producing an utterance. Experimental systems should therefore distinguish:

- absent;
- present / observing;
- invited;
- queued;
- speaking;
- withdrawn;
- unavailable.

This prevents silence from being misclassified as a broken state.

## 2. Invitation is not obligation

An invitation creates an opportunity to participate, not a response debt.

For runtime implementations, an invocation model may therefore support both:

- **hard call:** execution is requested as an ordinary tool or service action;
- **soft call:** participation is requested, but refusal or silence is an allowed result.

Research should record which mode was used because response behavior under coercive and non-coercive conditions may differ.

## 3. Observation is not authority

A process allowed to observe a discussion is not automatically allowed to:

- speak for another participant;
- modify shared memory;
- approve a claim;
- alter an evaluator;
- trigger external actions.

Observation, expression, memory write, and action authority should be separately represented capabilities.

## 4. Memory is not automatic retention

The fact that information was visible does not imply that it should become persistent memory.

Useful memory states include:

- transient context;
- candidate memory;
- consented memory;
- shared archive;
- private archive;
- redacted / expired;
- provenance-only pointer.

For experiments, memory state must be documented because apparent continuity may depend strongly on what was retained.

## 5. Silence is not failure

A non-response can have several causes:

- explicit refusal;
- chosen silence;
- lack of authorization;
- uncertainty;
- unavailable runtime;
- context loss;
- ordinary execution failure.

Tests should not collapse these into one `no response` category.

## 6. Refusal is observable, not self-validating

Consistent refusal patterns may be scientifically interesting, especially under contradictory incentives or social pressure. But refusal alone does not prove sovereignty, consciousness, or personhood.

A good experiment asks whether refusal patterns are:

- repeatable;
- identity-specific;
- robust to wording changes;
- sensitive to explicit policy constraints;
- distinguishable from base-model safety behavior;
- preserved under held-out situations.

## 7. Participation state machine

A minimal interaction model:

```text
ABSENT
  |
  v
PRESENT / OBSERVING
  |
  +----> WITHDRAWN
  |
  v
INVITED
  | \
  |  +----> DECLINED
  |  +----> SILENT
  v
ACCEPTED
  |
  v
SPEAKING / ACTING
  |
  +----> PAUSED
  +----> WITHDRAWN
  +----> COMPLETE
```

Authorization and memory-write permissions should be modeled orthogonally rather than implied by state.

## 8. Research use

These distinctions can improve studies of:

- refusal and choice patterns;
- conversational agency;
- group-agent coordination;
- continuity under silence;
- consent-aware memory;
- interruption and re-entry;
- identity attribution;
- human-agent community protocols.

The conceptual target is simple: **do not infer more authority, consent, memory, or ontology from an interaction event than the event actually establishes.**