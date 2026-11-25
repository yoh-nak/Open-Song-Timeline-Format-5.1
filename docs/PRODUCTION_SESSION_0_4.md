# OSTF 5 Production Session 0.4 — Interoperability semantics (5.1.0)

> **0.4 inheritance:** All Production 0.3 semantics are retained, with Score 5.1 binding, optional `audioTakeGroups`, and safe-integer time/frame bounds. The original 0.3 Schema is preserved separately. The audio-comp rules below and `SPECIFICATION.md` override earlier exclusions of comping.

**This edition inherits all fourteen named definitions from the byte-verified publisher-adopted 4.3 Production 0.2; the inherited typed automation rules and the explicit 5.1 take additions apply.** The structural authority is `schema/ostf-production-session-0.4.schema.json`. Identify a 5.1 Profile with `profile:"OSTF-Production-Session"`, `profileVersion:"0.4.0"`, `score.formatVersion:"5.1.0"` and the SHA-256 of the exact raw UTF-8 Score bytes. An incompatible family/version must not be silently relabeled.

## References and audio graph

The ID namespaces of Channels, Devices, Assets, Audio Regions, Automation Lanes, Sends (across all Channels) and Sidechains are each unique. Exactly one Master is required. A Track Channel references an existing Core Track; `audioTrack`, Bus and Master do not. Mapping one Core Track into more than one Channel is rejected unless a future explicitly documented duplication rule exists. Every Device is owned once; the order in `deviceIds[]` is the processing order. An Instrument can only be first on a Track Channel, at most once. Bus/Master do not host Instruments. A missing Plugin is not silently replaced by display name.

All non-Master output Channels must resolve. Send targets must be Buses. Sidechains must originate outside the Master, target an Effect Device owned by a different Channel and use a unique `(targetDeviceId,targetPortId)`. Build directed Channel dependencies from Outputs, Sends, and Sidechains (Sidechain target = owning Channel of its Device); cycles and unresolved references are invalid. Do not repair a cycle by deleting a Send without reporting loss.

## Assets and Audio Regions

`stateAssetId` resolves only to a `pluginState` Asset and `sourceAssetId` only to `audioSource`. Require `sourceStartFrame >= 0`, `sourceFrameCount > 0`, `sourceStartFrame + sourceFrameCount <= asset.frameCount`, and `fadeInTicks + fadeOutTicks <= durationTicks`. Audio Regions belong to Track or AudioTrack Channels, not Bus/Master. Source time is in the unmodified Score Tick domain. `native` uses Score Tempo to advance un-stretched frames; `fit` maps the declared source frame interval to Region Tick range with explicit `pitchPolicy`. No implied loops, crossfade, auto normalization, identical DSP algorithm, or waveform identity.

## Automation and ordered semantics

Automation Points use strictly increasing nonnegative Score source Ticks. The same source range played in multiple Visits applies the same source automation again. Duplicate `(target.kind, reference ID, parameter/parameterId)` Lanes are invalid. Boolean controls are Channel Mute, Send Enabled, Audio Region Mute, and DeviceControl Enabled/Bypass, using `valueType:boolean`, `interpolation:step`, and Points containing **both `atTick` and Boolean `value`**. Both fields remain mandatory in every Boolean point.

Numeric ranges: Channel/Send/Region gain in dB according to the field's declared Schema bounds; Pan in -1..1; plugin `device.parameterId` normalized 0..1 unless the Profile specifies otherwise. No implicit clamping. Before the first Point use the static value; after the last Point hold the last. Step holds the previous value, linear interpolation is performed in the declared numeric domain. DeviceControl is not an internal Plugin parameter. MIDI CC7/10/11/91/93 remains performance/instrument control and cannot overwrite Audio Mixer authority.

## Preservation and revisions

A changed Score raw digest invalidates previously pinned companion profiles until an explicit rebind or historical retention decision is made; a Plugin Context `ack` is not automatically an authorization to update Production identity. A Package can carry actual preset bytes but cannot provide Plugin runtime availability, licenses or cross-DAW sound equivalence. Preserve unsupported identities/state and the bytes actually provided, or refuse lossless write and describe the loss. The Profile does not standardize advanced warp, surround, parallel racks, physical I/O, or DSP equivalence.

**Status:** cross-document, timebase and graph semantics are required implementation work beyond JSON Schema shape. The official 4.3 Production 0.2 source has been byte-verified and is included under `adopted-4.3/`; this 0.4 document is an approved written specification. No DAW runtime verification is claimed.

## Automation target type and domain (normative specification)

This edition retains the Production 0.3 repair that excludes Boolean values from numeric automation targets. The versioned 5.0 and 4.3 Schemas remain unchanged.

| Target kind | Parameter | `valueType` | `points[].value` | Meaning |
|---|---|---|---|---|
| `channel` | `gainDb` | `number` | -120 to +24 dB | Audio-channel gain, independent of MIDI CC7 |
| `channel` | `pan` | `number` | -1 to +1 | Audio panning, independent of MIDI CC10 |
| `channel` | `mute` | `boolean` | `true` / `false` | Step interpolation only |
| `send` | `gainDb` | `number` | -120 to +24 dB | Audio send gain |
| `send` | `enabled` | `boolean` | `true` / `false` | Step interpolation only |
| `audioRegion` | `gainDb` | `number` | -120 to +24 dB | Region gain before channel processing |
| `audioRegion` | `mute` | `boolean` | `true` / `false` | Step interpolation only |
| `deviceControl` | `enabled`, `bypass` | `boolean` | `true` / `false` | Not an opaque plugin parameter |
| `device` | `parameterId` | `number` | 0 to 1 | Normalized opaque plugin parameter; actual plugin scale is host-dependent |

**Semantic conditions:** `points[]` contains at least one point; `atTick` must increase strictly without duplicates within each lane, in the original Score global Tick coordinate system. Revisited source sections reapply their original automation points. Duplicate lanes for the exact same target kind, target ID and parameter are invalid; array-order wins are not permitted. Numeric lanes allow `step` or `linear`, whereas boolean lanes allow `step` only. Before the first point, the corresponding static Channel/Send/Device/Region value applies; after the last point, the final point value holds. Missing IDs, unsupported parameters, and out-of-domain values must not be silently coerced; reject or explicitly disclose loss.

**Boundary:** The 0.4 Schema can encode type/domain constraints. It does not independently prove cross-ID integrity, point ordering, duplicate-target exclusion or graph acyclicity; those are separate semantic obligations. It is not a DAW, audio or plugin compatibility certification. See the production examples catalog in `EXAMPLES_GUIDE.md`.


### Exact adopted-source inheritance note

All fourteen named definitions are inherited from the exact publisher-adopted Production Session 0.2 schema, including optional `channel.name`, required `plugin.name`, `plugin.namespace`, `asset.purpose=renderedAudio`, `asset.byteLength`, and `hostExtension.namespace` pattern. `sizeBytes` is a Package Manifest property, not a 0.4 Production Asset property. Version and Score pin were updated for 0.4 and per-target numeric Automation type/domain restrictions were added. See adopted-source reconciliation record.


## Audio Take / Comp — 0.4

`audioTakeGroups[]` owns a source-score Tick interval on one track/audioTrack Channel. Candidate Audio Regions are always `mute:true`. Each Comp has a complete region partition and distinct `outputAudioRegionIds`; only the saved active Comp is unmuted. Region-targeted automation is forbidden for managed regions; use Channel automation. Groups on the same Channel do not overlap.

`regions` output preserves source phase, gain and fade envelopes. Native cropping integrates the original Tempo Map over the full elapsed interval; fit cropping retains the original Region ratio. A linear crossfade must match an explicit transition window and authored output Region/fade descriptors. Use a separately supplied `rendered` audioSource for nonlinear transitions or envelopes that cannot be represented faithfully by Region descriptors. DSP equality is not standardized. Channel processing is applied once after the comp output.

Visit selection is a playback overlay, not an edit to the saved active Comp. It overrides only the selected outputs' selection-related mute flags; candidates remain silent, and Channel mute remains effective. Production Audio remains independent of Core `realized:silent/open`; Core part silence does not silently mute Audio. Use explicit Production control for coordinated muting. Visit cropping applies after Comp materialization.

References, range maps, selection and output must be committed consistently in one production edit. `SPECIFICATION.md` defines the complete take, transition and migration semantics.
