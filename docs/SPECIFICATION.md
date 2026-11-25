# Open Song Timeline Format 5.1.0 — Specification

**Release: v5.1.0 · 2026-11-25 · Take & Comp**

This is the integrated written specification of OSTF 5.1.0. It retains the published 5.0 musical and project model and adds optional, non-destructive MIDI and audio Take Groups, Comp maps, saved outputs, finite-Visit selections and live-launch selection policies. The Japanese edition is `SPECIFICATION.ja.md`; both editions state the same current requirements. **MUST**, **MUST NOT**, **SHOULD** and **MAY** express mandatory, prohibited, recommended and optional behavior respectively.

## 1. Forms, scope and normative precedence

The two file forms remain **OSTF TEXT** (`.ostf`, BOM-free UTF-8 JSON Score) and **OSTF PROJECT** (`.ostfp`, ZIP container). Production Session and Distributed Session are separately versioned optional JSON document families. Plugin Context Exchange is a logical host/plugin message contract, not a third required file extension or a standardized real-time plug-in API.

The publisher-adopted 4.3.0 musical grammar, the 5.0 family semantics, and all unchanged mandatory fields remain in force. Score 5.1 changes the exact root version discriminator and adds optional `takeGroups`; Production 0.4 adds optional `audioTakeGroups` and the Score 5.1 binding. A document without takes need not contain either field. The versioned Schemas determine types, required fields, unions, enumerations and numeric bounds; this specification and the current family texts determine cross-reference, time, ownership and behavioral constraints beyond JSON Schema. An explicit current amendment overrides inherited text only for the exact named family/version and subject. An example cannot override a rule.

The exact adopted 4.3 source bytes are retained under `../adopted-4.3/`. Historical Draft labels, obsolete release approvals and older navigation embedded in those archived transcripts are provenance, not the status or release gates of 5.1. The complete manuals and parameter references include the inherited vocabulary and current additions. Unknown meaning is not guessed, unsupported data is preserved for lossless saving or the save is declined, and no document reference automatically authorizes an external download or execution.

### Current document identifiers

| Family | Exact identification | Structural authority | Current semantic text |
|---|---|---|---|
| Score | `format:"OSTF"`, `version:"5.1.0"` | [Core Schema](../schema/ostf-5.1.0.schema.json) | This document, [complete manual](COMPLETE_MANUAL.md), adopted 4.3 Score semantics |
| Production | `profile:"OSTF-Production-Session"`, `profileVersion:"0.4.0"`, `score.formatVersion:"5.1.0"` | [Production Schema](../schema/ostf-production-session-0.4.schema.json) | [Production Session 0.4](PRODUCTION_SESSION_0_4.md), adopted Production 0.2 and retained 5.0 amendments |
| Distributed | `profile:"OSTF-Distributed-Session-0.4"`, `recordType:"snapshot"` or `"event"` | [Distributed Schema](../schema/ostf-distributed-session-0.4.schema.json) | [Distributed Session 0.4](DISTRIBUTED_SESSION_0_4_SPECIFICATION.md) |
| Project manifest | `packageFormat:"OSTFP"`, `packageVersion:"1.1.0"` | [Manifest Schema](../schema/ostf-package-manifest-1.1.schema.json) | [Package specification](PACKAGE_SPECIFICATION.md) |
| Plugin Context | `protocol:"OSTF-Plugin-Context"`, `protocolVersion:"1.1.0"` | [Plugin Schema](../schema/ostf-plugin-context-1.1.schema.json) | [Plugin exchange protocol](PLUGIN_EXCHANGE_PROTOCOL.md) |

Legacy Scores and companion documents remain valid at their own exact versions. Recognition of 5.1 does not relabel 4.3 or 5.0 data, and recognition of 5.0 does not imply acceptance of a 5.1 discriminator.

## 2. Inherited authorities and invariant principles

1. A Score's SHA-256 is calculated on its **original exact UTF-8 bytes**, not reserialized or canonicalized JSON. Even a whitespace-only byte change invalidates the old digest. Package construction MUST NOT rewrite enclosed Score, Production/Distributed or Asset bytes. Package bindings use the established package-root paths and exact identities.
2. Core Harmony, Lyrics, Notes, Directions, Voices, resources and musical intent retain their established authorities. Section names, lane order and display colors do not define identity or playback.
3. Core MIDI CC Volume/Expression/Effect controls and Production mixer Gain/Pan/Sends are separate authorities. Production retains its acyclic channel, send and sidechain graph, typed automation and inert plugin-state model. JSON records cannot instantiate a plug-in or guarantee identical audio.
4. A finite Performance Plan is an opt-in projection of source material. It does not rewrite source Notes or create a second authoritative source timeline. Existing fixed/open/silent realization, role override, source-continuous join, hard-cut and source-tempo rules continue to apply.
5. Distributed Session stores collaboration state and phrase proposals/commitments in its own domain. A `phraseCommitted` record does not automatically mutate a Score, select a Take, replace an audio recording or prove that anything sounded. Root `scoreSha256` pins the original Score bytes.
6. Plugin Context is a read-only partial projection or an untrusted proposal. Only the host may apply authorized changes against the original snapshot and stable identities, commit the complete new state, and acknowledge `applied` after successful save. A partial context MUST NOT be saved as a complete Score.
7. Each implementation MUST declare its exact supported family/version and capabilities. Generic “OSTF compatible” does not imply support for every optional family or behavior.

## 3. Time, scope and containment

Every Take Group, Comp Region and audio transition uses the Score's existing PPQ and **source-global Tick** coordinate system. A group has `startTick >= 0` and `durationTicks > 0`; its interval is half-open `[startTick, startTick + durationTicks)`. Stored Tick values and all derived endpoints, offsets and sums used for these structures MUST remain exact integers in `0..9007199254740991`; positive durations may not collapse to zero. Writers MUST diagnose overflow instead of wrapping or rounding it.

Core Clips retain `start` and `duration`; their Notes and MIDI Events retain clip-local starts. Convert local positions with the actual Clip start before comparing them with Comp ranges. Production audio assets retain decoded frame coordinates. Source Ticks, expanded Performance Ticks, Session clocks, audio frames and UI bar numbers MUST NOT be conflated.

An optional `sectionId` is an editing anchor to an existing Section whose interval intersects the group. It does not require identical boundaries or introduce a Section-relative wire timebase. Song-wide, Section, phrase, bar, chord and sub-beat editing all use the same interval representation. A source Section may therefore be presented as a session clip by one host and as part of an arrangement by another. No particular clip grid, lane layout or launch UI is mandated.

Renaming a Section or changing tempo, meter or bar numbering does not implicitly move stored Ticks. Explicit movement, PPQ conversion or a timeline edit MUST update affected material, ranges, outputs and references atomically. Tempo changes alter `native` audio timing and require the corresponding output/rebinding decision; matching Section labels alone do not prove that an old output is still correct. Source-time conversion to seconds integrates every applicable source-tempo segment, including after a finite-Plan re-entry.

## 4. Take Groups and immutable candidate material

Core `takeGroups[]` items own exactly one existing `trackId`. Production `audioTakeGroups[]` items own exactly one existing `channelId` of type `track` or `audioTrack`, never Bus or Master. Group ranges on the same owner in the same family MUST NOT overlap. MIDI and Production audio are independent domains; their simultaneous authored use remains possible.

Each group contains at least one `takes[]` item. A MIDI Take references one or more existing Clips on its owning Track through `clipIds`; an audio Take references one or more existing Audio Regions on its owning Channel through `audioRegionIds`. Each referenced candidate interval is contained in the group. Candidates may differ in start and length, and a short replacement Take need not cover the whole group. Candidate intervals within one Take MUST NOT overlap; polyphony is represented inside a MIDI Clip. Intervals belonging to different Takes may overlap.

A candidate Clip/Audio Region belongs to exactly one Take and MUST NOT also be another group's material or any Comp output. The same Take may be selected by several Comps without copying its candidate data. Audio Regions may reference a shared underlying audio asset according to inherited asset rules. Core `clipChoices` remains available, but MUST NOT claim candidate or output Clips managed by a Take Group. Existing ID namespaces and reference uniqueness remain unchanged.

All candidate MIDI Clips MUST store `enabled:false`; all candidate Audio Regions MUST store `mute:true`. These flags suppress normal playback, not storage. Preserve original Notes, Note-local enablement, MIDI Events, vocal data, decoded-frame selection, gain and fades. Selecting a Take never turns a candidate into the normal output. Explicit host audition may monitor it separately, but MUST NOT persist an inconsistent normal playback selection.

The group owns its playback range: unrelated Clips or Audio Regions of the same owner/domain MUST NOT overlap that range. A writer must split or otherwise explicitly reconcile such material before admitting the group. Source events of material outside the group must not leak through its range unintentionally. DSP reverberation or release tails are not newly defined by these musical interval constraints.

### Candidate metadata

`kind` is `take` for another performance of the same intent, `variation` for a variation within that scope, or `alternative` for another performance candidate. These labels have identical selection mechanics. They do not authorize replacing Harmony, lyric text or song structure; use the existing appropriate musical structures or a separate revision for those edits. Simultaneously sounding doubles/layers are separate parts, not competing Take selections.

`origin` records optional human, AI, imported, derived or unknown provenance. Prompts, model names, URIs and remote participant/proposal IDs are inert metadata. `parentTakeId` resolves to another Take in the same group, and parent links MUST be acyclic. `ratings` are informational scores in `[0,1]`, not automatic selection instructions. `laneOrder` is only a display hint. A metadata field does not grant authentication, execution, network or asset-access permission.

## 5. Comps and complete selection maps

Each `comps[]` item is one saved complete selection. Its `compRegions[]` MUST be ordered by ascending `startTick` and form a gapless, non-overlapping partition of the whole group. Every region has positive duration. Adjacent boundaries use half-open interval semantics, so a boundary Tick belongs to the following region.

| Region kind | Required meaning | Prohibited inference |
|---|---|---|
| `source` | `takeId` and `clipId` or `audioRegionId` resolve to that Take's candidate; the entire selection lies inside its interval | No hidden shift, loop, stretch, substitution or fallback to another Take |
| `silence` | The selected range is explicitly silent; it has no Take or candidate reference | A missing candidate is not equivalent to declared silence |

Candidate and Comp source Ticks are identical. A selection is a reference to the preserved original, not a destructive cut. A partial Take cannot silently fill uncovered ranges; the Comp explicitly selects other Takes or silence there.

`activeCompId` is required and is a group-local Comp ID or `null`. Null means silence for the group's ordinary saved playback. An empty `comps` array therefore requires `activeCompId:null`; any Visit selections must also select null, and live selection can only be fixed/manual. A single uncut Take is selected through a Comp as well; no competing `activeTakeId` exists. Group IDs are unique within their family. Take IDs, Comp IDs and Comp Region IDs are unique within their respective group-scoped namespaces. All current references must resolve, except the explicitly historical IDs described in §12.

## 6. Materialized output, saved flags and atomicity

The Comp map is the **editing authority**. Independently identified ordinary Clips/Audio Regions listed by `outputClipIds` or `outputAudioRegionIds` are the **playback authority**. Every Comp, including inactive Comps, MUST carry its current materialized output; a consumer need not generate Notes or audio from the map in real time. Each output belongs to the same owner and lies within the group's range. Candidate IDs and output IDs are distinct, and an output ID MUST NOT be shared by different Comps or `clipChoices`.

An entirely silent Comp has an empty output list and no nonempty `noteLinks` or `transitions`. A Comp containing any source region requires at least one output. A MIDI source selection containing no musical events is represented by an output Clip with an empty `notes` array, rather than an absent output. MIDI output Clip intervals within one Comp do not overlap; an output Clip may span an explicit silence interval, but its musical gates and selected material must respect the silence. Necessary release/state events may implement the transition into silence. Audio output overlap is permitted only for the transition windows specified in §8. Candidates and inactive outputs remain stored.

The saved ordinary-playback state is exact:

| Managed object | MIDI `enabled` | Audio `mute` |
|---|---|---|
| Candidate material | `false` | `true` |
| Output of `activeCompId` | `true` | `false` |
| Output of every other Comp, or every Comp when active is null | `false` | `true` |

These flags represent the **saved default selection**. The explicit finite-Visit/live selection overlay in §9 is the only standard selection exception: it substitutes the selected Comp's output eligibility at playback without modifying these stored flags. It never enables candidate material. Higher-level Core Track and Note enablement, Production Channel/automation mute, routing and established realization rules retain their separate authority.

All region-level Production automation targeting any managed candidate or output Audio Region is excluded in 5.1. Use Channel automation or explicitly authored/rendered Comp outputs. In particular, automation may not unmute a stored candidate or inactive output. Unmanaged Audio Regions retain inherited automation capabilities.

A writer MUST save the map, candidate edits, all affected materialized outputs, identities, references and saved flags as one consistent transaction. No stale output may be silently accepted after a map or source edit. Missing outputs, wrong owners, unresolved references, contradictory flags or inconsistent material require a diagnostic and rejection of the affected edit/save. An explicit host repair may create a new consistent revision; a reader must not silently guess one. Schema shape alone cannot prove musical correspondence between map and output, and bit-identical DSP is not claimed.

## 7. MIDI and vocal boundaries

Each MIDI Comp requires `noteBoundary`:

| Value | Materialization rule |
|---|---|
| `truncate` | Select only source Notes whose absolute onsets lie inside a selected source interval; cap each gate at that interval's end. A tail whose onset was before the selected start does not create an attack. |
| `retrigger` | Also include source Notes already held at the interval start, with a new attack at that start and a gate restricted to the interval. |
| `authored` | Preserve explicitly edited materialized boundaries/phrasing as the performed result, while retaining the declared source provenance and explicit-silence constraints. |

Adjacent source selections referencing the same candidate are logically joined before these operations, so subdivision alone does not create extra attacks. Compute source onsets from Clip-local starts and retain disabled Note semantics. Output Notes obtain independent IDs; optional `noteLinks` connects source and output Note IDs, resolving within the relevant candidate/output sets. One-to-many and many-to-one relationships are allowed; duplicate pairs are not.

These are **Comp-authoring** rules, not a replacement for finite-Plan cutting. A fixed Visit subsequently selects the materialized output using the inherited source-onset and hard-cut rules. It MUST NOT invent a retrigger at a Visit entry merely because the Comp used `retrigger` when it was authored. A newly desired entry attack must already be an explicitly authored output Note at that source position, or belong to a separate explicitly materialized performance rendition.

Writers must reconcile CC, sustain, Program Change, Pitch Bend, MPE/channel state, note-targeted data, phoneme timing, singing curves and lyric alignments in the output. The source Take's inactive control stream MUST NOT leak into ordinary playback. Required state initialization or release events must be materialized using the inherited supported structures, or the limitation must be disclosed and the edit declined until a representable result exists. Do not send indiscriminate resets that alter unrelated parts on a shared MIDI bus. A remote instrument's unspecified initial state is not made portable merely by selecting a Take.

Retain clip-local candidate vocal data and update output references to the new output IDs. Selection does not rewrite the authoritative lyric text or imply delivery of a complete lyric alignment when only some Notes survived. An implementation that cannot author these boundaries may play the stored output and preserve the additional data without claiming Comp-edit capability.

## 8. Audio materialization, crop phase and transitions

An Audio Comp requires `outputMode:"regions"` or `"rendered"`. In `regions`, ordinary output Region descriptors represent the selected material. In `rendered`, output Regions reference separate pre-rendered `audioSource` assets. Rendering is before Channel devices/mixer processing; a consumer MUST NOT apply baked Channel processing a second time. Original assets remain preserved.

The inherited frame constraints remain mandatory: `sourceStartFrame >= 0`, `sourceFrameCount > 0`, their sum not greater than the asset's decoded `frameCount`, and `fadeInTicks + fadeOutTicks <= durationTicks`. A crop must retain the original candidate's source phase:

- For a native candidate beginning at source Tick `R`, ideal frame position at `t` is `sourceStartFrame + sampleRateHz × T(R,t)`, where `T` integrates every source-tempo segment. Source frame exhaustion yields silence; it never loops or restarts at the beginning of a Comp region or Visit.
- For a fit candidate of source duration `L`, ideal frame position is `sourceStartFrame + sourceFrameCount × (t-R)/L`. A shortened output must preserve that selected phase and rate relationship, including `pitchPolicy`; retaining the original full frame window for a shorter range would incorrectly stretch it.
- Preserve original candidate gain and original Region-local fade meaning over the selected range. A cut does not automatically restart an old fade. If available Region fields cannot represent the required envelope, crop or transition, the writer must use rendered output or explicitly decline that authoring capability. Fractional-frame rounding and resampling/stretch algorithms remain host-dependent; any approximation affecting interchange must be disclosed.

Optional `transitions[]` describe deliberately authored crossfades. `atTick` is a junction between adjacent source selections of different candidates. The half-open window `[startTick,startTick+durationTicks)` must **strictly contain** that junction, lie inside the group, and be backed by available material on both sides throughout the window. Transition windows do not overlap one another or consume another source/silence junction. No transition bridges an explicit silence region.

`curve` is `linear`, `equalPower` or `customRendered`. `regions` supports only linear amplitude transitions represented by matching output Region overlap and explicit inherited fade-in/fade-out values; incompatible pre-existing envelopes require rendered output. For normalized position `u` across the overlap, the added linear transition weights are `1-u` and `u`. Equal-power uses `cos(pi*u/2)` and `sin(pi*u/2)` as the intended added weights and requires `rendered`; `customRendered` likewise requires rendered output, whose stored asset is authoritative. Gain, correlation, DSP and frame rounding can still affect the resulting sound.

Transition metadata records the edit and MUST NOT be applied again to already materialized fades or rendered samples. Without a transition, the junction is a hard cut; no automatic smoothing is implied. Preserving two muted source Takes is not equivalent to providing a rendered crossfade.

## 9. Finite Visits and free live-session launches

### 9.1 Explicit finite-Visit selection

`visitSelections[]` maps a group-local pair `(performancePlanId, visitId)` to a Comp ID or null. Each pair is unique, resolves to an existing finite Plan/Visit, and the Visit's actual selected source-segment union must intersect the group. A noncontiguous Visit is not treated as one filled bounding range. Null explicitly selects silence and is distinct from an absent override.

Resolve ordinary selection as follows:

1. For a finite Visit, use its exact `visitSelections` entry if present, otherwise the saved `activeCompId`. Do not run free live policies to replace a finite Plan decision.
2. For the intersected group range, suppress the outputs of all other Comps and schedule only the selected Comp's materialized output. This overrides only the managed output `enabled`/`mute` flag that encodes saved default selection. Candidate material remains suppressed; no stored flag is rewritten.
3. For Core MIDI, apply Track/Note enablement and the Visit's inherited Part realization. `silent`, `open` and `unspecified` do not become fixed replay merely because a Comp was selected; only `fixed` replays the stored musical output. An open part may be realized through other explicitly supported mechanisms.
4. Project selected material only over the intersection with each actual source segment. Apply the existing continuous-join versus hard-cut, source state, automation and tempo rules after selection. Do not restart original audio frame or fade phase at a Visit boundary.

**Production independence is retained.** A Production Audio Region is independent of Core fixed-note realization even when its Channel references a Core Track. Consequently, audio Comp selection and ordinary audio output are not automatically suppressed by that Core Track's `enabled` or `realization:"silent"`/`"open"`; Production Channel/Region eligibility, mute and routing govern them. The above selection overlay still replaces which managed audio outputs are eligible and projects them over the Visit source segments. To make an audio Take Group silent for a Visit, explicitly select null or an all-silence Comp, or use the appropriate Production mute authority. This resolves the earlier 5.1 delta's ambiguous suggestion of coupling audio candidates to Core Part realization.

A host that supports 5.1 saved playback but not Visit selections may retain and play the saved default only with an explicit unsupported-feature diagnostic. It MUST NOT claim equivalent reproduction of a Plan containing differing overrides.

### 9.2 Free live launches

Optional `liveSelection` is a launch-time policy for a host's free session mode, outside a resolved finite-Plan Visit decision:

| Mode | Selection |
|---|---|
| `fixed` | Saved `activeCompId` |
| `manual` | Explicit host/user selection of a group Comp or silence; otherwise saved active selection |
| `cycle` | First listed candidate at the first launch, then the next listed candidate cyclically |
| `random` | Uniform choice among listed candidates |
| `weighted` | Choice proportional to each listed nonnegative weight; total weight must be positive |

Cycle/random/weighted require a nonempty list of distinct existing Comp IDs. Weight is mandatory on every weighted candidate and forbidden otherwise. Fixed/manual have no candidate list. Silence can be represented in a dynamic list by a named all-silence Comp. Candidates and metadata do not command an automatic launch.

A resolved launch uses the same output selection overlay as §9.1 and does not mutate `activeCompId`. An unresolved or unsupported live selection falls back to the saved active Comp and the host discloses unsupported dynamic behavior. Selection is resolved at launch; quantization, mid-clip switching, indefinite looping, session transport, cross-track scene coordination and random-seed persistence remain host policies, not newly standardized fields. Repeated launching does not require duplicate source clips or an infinite Visit array.

To exchange a finite recorded performance, author explicit Visit decisions in a finite Plan with `visitSelections`. Unrecorded random or manual choices are not promised reproducible. A multi-Track scene may commit several host selections atomically, but the format does not infer a global scene or same-numbered Take relationship from labels.

## 10. Distributed, AI and plugin integration

Distributed Session 0.4 retains the previous Snapshot/Event grammar, clock model and authority rules while binding to Score 5.1 and its exact original bytes, document/revision and finite Plan. Importing an accepted remote phrase as a Take is an explicit host Score edit that creates candidate material and corresponding consistent outputs; a remote commitment alone never selects or changes a Comp. A new Score revision is not a retroactive replacement of immutable prior accepted events or their Score pins. No new network actuator, automatic Comp synchronization or robot permission is introduced.

Plugin Context 1.1 adds Score 5.1 identity. For that combination only, authorized edit paths may additionally address a group at `/takeGroups/{index}`, its descendants at `/takeGroups/{index}/...`, or append a group at `/takeGroups/-`. Legacy Score bindings retain their previous editable roots. The whole `/takeGroups` array is not an editable replace/create target in this protocol. If absent, the host first initializes it in an explicitly saved revision and reissues a context for the new Score SHA.

For a root-array append, `containerId` identifies the pinned Score's actual `document.id`, the envelope includes matching `score.documentId`, and `newEntityId` equals the appended group's `value.id`. If the Score has no document identity, the host establishes one before issuing such an edit context. Nested operations continue to follow the existing stable owner/entity-ID rules. A proposal must atomically maintain Take Groups, affected Track Clips, all Comp outputs and saved selection flags. Changing only a map or active ID while leaving contradictory output flags is invalid. Unsupported referenced IDs, stale snapshots or unauthorized paths are rejected; protocol version alone grants no access.

Core Plugin Context permissions do not authorize Production audio Comp edits. Hosts may implement a separately authorized Production editing path, retaining all Production binding and transactional constraints. Provenance prompts, ratings, model labels and remote identifiers remain data, never executable instructions.

## 11. Packages, migrations and preservation

OSTFP 1.1 retains the 5.0 ZIP layout, mimetype, safe paths, manifest, exact-byte SHA handling and Asset/Binding rules. The allowed companion matrix is explicit:

| Enclosed Score | Production | Distributed |
|---|---|---|
| 4.3.0 | 0.2.0 | `OSTF-Distributed-Session-0.2` |
| 5.0.0 | 0.3.0 | `OSTF-Distributed-Session-0.3` |
| 5.1.0 | 0.4.0 | `OSTF-Distributed-Session-0.4` |

Optional families may be omitted; their presence must use the row matching the enclosed Score. Package 1.0 retains its original accepted versions. Package 1.1 does not erase or reinterpret a legacy Score's identity. Audio Take media uses existing `productionAsset` bindings. Lossless packaging includes managed original and inactive material and all actually required assets, not merely the audible output. Unresolved external material must be disclosed and is not silently downloaded or substituted.

5.0 to 5.1 is an explicit revision/migration. A take-free Score may retain all musical data, but changes to its version bytes require a new SHA and explicit companion/package rebinding. Relevant document/revision identity, production source-tick meaning and newly emitted plugin contexts must remain consistent. Historical distributed events are not silently repinned; follow the retained session-migration rules.

5.1 to 5.0 is an explicit **projection of the saved active output**. Preserve the selected ordinary output and its musical data; remove the new Take Group structures and downgrade companion/package/protocol identities through the stated migration rules. Report loss of alternative selection maps, metadata, histories and Visit/live decisions. Retained source and inactive output clips must remain disabled/muted; deleting them requires repairing all surviving references, vocal alignments and asset bindings. Preserve the source 5.1 project when non-destructive editing must remain available.

Simple downgrade does not preserve different per-Visit selections. To preserve a chosen finite performance, a host must explicitly materialize it into a new arrangement/rendition with appropriate distinct output identities, tempo/state semantics and a disclosed loss report; it must not silently flatten or relabel the source. A 5.0-only reader is not required to accept a 5.1 Score directly.

## 12. Informational selection history

Optional `takeSelectionHistory[]` stores saved selection history. `sequence` is a strictly increasing nonnegative safe integer within the group; `compId` is the then-selected ID or null. `actorId`, `recordedAt` and `reason` are optional. A historical Comp ID may refer to a deleted Comp, but MUST NOT be used to resolve current playback. History does not override `activeCompId`, `visitSelections` or an explicit live launch, and a complete event log is not required. Capture a reproducible finite performance through finite Plan selections, not by guessing it from incomplete history.

## 13. Capability declarations and release scope

Capabilities are independent, not mandatory cumulative levels: `score-5.1-read`, `score-5.1-write`, `take-preserve`, `midi-comp-edit`, `audio-comp-edit`, `visit-selection`, `live-selection`, `distributed-0.4`, `plugin-context-1.1` and `package-1.1`. An application can support saved playback and preservation without exposing lanes or implementing Comp editing. Lossless writers must retain unsupported standard material and assets they manage, or decline a destructive overwrite and describe the loss.

Semantic conformance includes owner/range containment, reference resolution, group/Comp uniqueness, complete partitioning, valid candidate and output flags, state boundaries, correct family bindings and atomic updates. JSON Schema alone does not establish these obligations or guarantee identical rendering, plugin availability or network timing. User-interface design remains an implementation choice.

**This written specification is adopted for release under the publisher's blanket approval. Runtime, independent parser, DAW, DSP, plug-in, physical-device and WAN execution testing are not release conditions and are not claimed as completed.** Specification release is distinct from publication of a repository/tag or certification of any implementing application. No further individual approval or runtime gate is introduced by archived Draft text.

For complete field declarations and authoring guidance, read [parameter reference](PARAMETER_REFERENCE.md), [complete manual](COMPLETE_MANUAL.md), [migration matrix](MIGRATION_MATRIX.md), [conformance](CONFORMANCE.md), [security](SECURITY.md), the current family texts and the retained adopted sources together.
