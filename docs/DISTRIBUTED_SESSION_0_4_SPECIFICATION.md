# OSTF 5.1.0 — Distributed Session 0.4 normative specification

**Publisher-adopted 4.3 Distributed Session 0.2 is the byte-verified source for this Score 5.1-only profile.** Authoritative structural Schema: `schema/ostf-distributed-session-0.4.schema.json`. It is a separate JSON record family; it does not confer networking, audio/DSP, identity, robotics or plugin-execution authority.

## Identity and score pin

`profile:"OSTF-Distributed-Session-0.4"` plus `recordType:"snapshot"|"event"` are required discriminators. There is **no** `profileVersion` and **no** nested `score` object. Both Snapshot and Event require root fields `sessionId`, `documentId`, `revisionId`, `performancePlanId`, and `scoreSha256` (64-digit lowercase SHA-256 over exact raw UTF-8 OSTF 5.1 Score bytes). The performance plan must be finite and present in the source Score.

## Snapshot

The Snapshot requires `sessionStatus:prepared|playing|stopped`, nonnegative `stateRevision`, `authorityParticipantId`, and at least one `participants[]` item. Every Participant requires `participantId`, `kind:human|softwareAgent|physicalRobot`, and `assignedTrackIds[]`. `playing` requires a `position`; `prepared`/`stopped` may omit it. Accepted phrases are stored separately under `committedPhrases[]`. An optional `commitmentWindow` with `startPerformanceTick` and `endPerformanceTick` asserts complete intersection coverage of accepted phrases in the half-open range. There is no `coverage` property; omit the window instead of making an inaccurate completeness assertion.

## Event and authority

An Event requires `eventId`, `issuerParticipantId`, `baseStateRevision`, `effectivePerformanceTick`, `kind`, and typed `payload`. Event kinds: `phraseProposed`, `phraseCommitted`, `turnRequested`, `cueIssued`, `performanceObserved`, `participantStatus`, `sessionStateChanged`. The last two state-affecting kinds (`phraseCommitted`, `sessionStateChanged`) require `resultStateRevision` equal to `baseStateRevision+1` on acceptance; other kinds prohibit it. Duplicate event IDs, revision collisions, authoritative actor checks, finite Plan/Visit and Tick projection retain official 0.2 semantics.

A `phrase` uses `representation:"midi1Notes"`, positive `durationTicks` and note items with pitch 0..127 and velocity 1..127. A committed phrase uses `commitEventId`. These are session phrases, **not edits to Core notes**. State changes are `sessionStarted`, `visitChanged`, `assignmentChanged`, `sessionStopped`; starting and changing visits require `position` with Plan/Visit/Source/Performance Tick and clock anchor. No resumption of a stopped session is implied.

## Version and migration from pre-release drafts

Distributed 0.2 is pinned to Score 4.3, 0.3 to Score 5.0, and 0.4 to Score 5.1. Score revision requires an explicit new session rather than text-relabeling old events. Earlier unpublished Draft0.7 candidate used incompatible nested `score`, `participant.id`, `phrase.encoding`, `committedPhrase.eventId` and `commitmentWindow.coverage`. The published 0.4 layout restores the official 0.2 wire layout and transforms its example data. No real-time/plugin/DAW/robot execution tests are claimed.


## Binding to 5.1 takes

Version 0.3 binds Score 5.0; 0.4 binds Score 5.1. All seven event kinds and Snapshot/Event grammar are retained; no network actuator is added. Accepting phraseCommitted does not change Score, takeGroups or activeCompId. A separately authorized host import may create source candidates and record sessionId/proposalId/commitEventId in origin. These are provenance, not permissions. Historical events are never silently rebound to new Score bytes.
