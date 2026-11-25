# OSTF Plugin Context Exchange 1.1 — Normative specification (5.1.0)

## 1. Contract, host boundary and version selection

This is a **transport-neutral JSON message contract**, not another OSTF file extension, a VST3/AU/CLAP or Max for Live SDK, an audio/DSP API, or a grant of execution/editing permission. `schema/ostf-plugin-context-1.1.schema.json` defines the envelope of `protocol:"OSTF-Plugin-Context"`, `protocolVersion:"1.1.0"`, unique `messageId`, `operation`, `score`, `scope`, optional `transport`, and operation-dependent `payload`.

`score.format:"OSTF"`, `score.version:"4.3.0"|"5.0.0"|"5.1.0"` and `score.sha256` identify the exact raw UTF-8 Score source bytes. `score.documentId/revisionId`, when present, must match the source. The receiving host must select the correct Score Schema/version rather than infer a Score version from the protocol version. A Plugin Context message does not have authority over Score, Production or Distributed Sessions. Transport/IPCs, plugin lifecycle, permissions and network access are host-specific.

## 2. Scope and transport time

`scope.startTick/durationTicks` describe a nonempty half-open interval `[startTick, startTick+durationTicks)` in **Score PPQ ticks**, with optional `trackIds/sectionIds` as view filters. Scope is not permission. `transport.positionTick` is a **host-PPQ position** with `transport.hostPpq`; `transport.scorePpq` states the Score resolution separately. Adapters must account for the musical Tempo/Meter Map, loops, seeks and discontinuities without equating host and Score ticks or asserting sample-accurate audio execution. `isPlaying` and optional BPM are observations, not instructions.

## 3. Read-only `context`

`payload:{"partial":true,"data":{...}}` is a deliberately **partial projection**, never a complete `.ostf` file. Optional `unavailableFields[]` distinguishes undisclosed data from an empty result. Missing harmony/track/lyric fields cannot be inferred as absent in the original Score. A context Consumer must not serialize the projection as a valid full Score by inventing missing fields, nor expose unprovided data as if authorized. A later Score write requires a separate, host-authorized operation.

## 4. Untrusted atomic `editProposal`

The payload has unique `proposalId`, `baseSha256`, `mode:"atomic"`, one or more `changes[]`, and optional `baseRevisionId`. `baseSha256` must equal `score.sha256` and the active source Score's raw-byte SHA; the Revision, when present, is checked separately. A repeated `proposalId` with the **same parsed content tree** is idempotent; the same ID with different contents is a conflict. An edit proposal carries **no write authority** until the host explicitly grants it.

Each `change` uses `op:"add"|"replace"|"remove"` and a non-root RFC 6901 absolute JSON Pointer `path` (decode `~0` and `~1`). `add` requires `containerId`, `newEntityId`, `value` and may append an array entity via `/-` or insert a previously absent object property only; its inserted entity's stable ID must equal `newEntityId`. `replace` requires `targetId`, `expected`, `value`; `remove` requires `targetId`, `expected`. `expected` compares the original parsed JSON tree with strict type and value equality; numeric/Boolean distinctions cannot be coerced. Stable target ID and Pointer must refer to the same applicable object. The inherited editable roots are `/timeline`, `/harmony`, `/tracks` and `/lyrics`; section 8 adds `/takeGroups` descendants only for Score 5.1 (all subject to external host scope). Score identity, `version`, `ppq`, `document`, vendor extensions and other roots are not editable through this protocol.

All paths, expected values and entity IDs are **resolved against one original immutable Score snapshot**. Reject overlapping parent/child edits, ambiguous array-index shifts, additions that replace existing keys, duplicate entity IDs, and conflicts before attempting to commit. Changes are then applied to a copy in the proposal's declared sequence without changing the snapshot against which old values were checked. Reject **the entire proposal** if any step fails; partial-apply or last-writer-wins is not a supported behavior.

## 5. Host apply and durable `ack`

The host must independently establish caller authority; verify version, Score SHA, optional Revision, scope, stable IDs, JSON Pointer targets and `expected`; construct and validate a new full Score (Schema **and** semantic references); and commit the entire new Score through a host/user-authorized save. Only after actual persistence can it return `ack.payload.status:"applied"` and the actual **new persisted bytes'** `effectiveScoreSha256` (and optionally `appliedRevisionId`). An `ack` references the original message's `messageId` in `payload.inReplyTo`, **not** the `proposalId`.

`status:"received"` means receipt for consideration, not success or durable storage. `status:"rejected"` means nothing was applied. Both **MUST NOT** include `effectiveScoreSha256` or `appliedRevisionId`; the source Score remains unchanged on rejection. A successful Score edit never silently rebinds a Production Session pin or carries forward a Distributed Session's active authorities. Rebinding requires separate explicitly validated processing; changed Score/Plan/Revision requires new Distributed Session as specified.

## 6. Diagnostic and information loss

`diagnostic` operation codes include `invalid`, `unsupported`, `stale`, `scopeViolation`, `permissionDenied`, `conflict`, `informationLoss`, `internalError`. Diagnostics may identify affected JSON Pointers; they do not contain executable instructions. Unsupported features should be reported or preserved, never silently dropped. An edit refusal is not a lossy write and must not be described as if a Score changed.

## 7. Advertised support and non-promises

A third-party instrument, MIDI generator, effect, AI model or Max for Live device may implement only `context` read or proposal creation without Project/Production support. A host may additionally implement edit-apply. Advertise each capability, source Score version and operation separately as in `CONFORMANCE.md`. This document does **not** standardize plug-in binaries, sample-rate conversion, host transport APIs, plugin parameters, exact audio playback, license/DRM, or physical robots.


## 8. Score 5.1 Take Group editing

Only Protocol 1.1 with `score.version:"5.1.0"` adds descendants of `/takeGroups/` to the four inherited editable roots. Adding, replacing or removing the `/takeGroups` array itself is forbidden. This root is not granted for Score 4.3/5.0.

Before the first group is added, the host initializes `takeGroups:[]` and `document.id` through a normal Score edit, and supplies a Context pinned to the new raw bytes. An add to `/takeGroups/-` uses `containerId = Score.document.id`, with the same value in envelope `score.documentId`; `newEntityId` matches the new Group's `id`. Deeper additions use the nearest owning entity under the inherited container rules.

For Comp switching, one atomic proposal should replace the existing Group and the relevant old/new output Clips as whole entities. Every expected value comes from the same unchanged Snapshot. The Host checks all candidate/output references, ownership, activeComp, scope and flags together. Unprovided context is not an empty value; request sufficient context before editing related output beyond the granted scope.

Audio Comp belongs to Production and is not authorized by adding the Core `/takeGroups` edit root. Origin prompts and ratings are inert metadata, not commands, permission or automatic selection.
