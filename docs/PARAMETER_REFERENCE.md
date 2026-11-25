# OSTF 5.1.0 — Complete parameter reference

All **2,341 explicit structural declarations** in the five current Schemas are enumerated below. Each row is a Schema JSON Pointer. Direct-parent required status is separate from conditional application. Descendant if/then/oneOf/allOf branches are included, retaining original types, values, enums, bounds and descriptions. Original Schema descriptions retain their source language.

| Schema | Root $defs | Declarations |
|---|---:|---:|
| [ostf-5.1.0.schema.json](../schema/ostf-5.1.0.schema.json) | 141 | 1470 |
| [ostf-production-session-0.4.schema.json](../schema/ostf-production-session-0.4.schema.json) | 28 | 430 |
| [ostf-distributed-session-0.4.schema.json](../schema/ostf-distributed-session-0.4.schema.json) | 16 | 168 |
| [ostf-package-manifest-1.1.schema.json](../schema/ostf-package-manifest-1.1.schema.json) | 8 | 120 |
| [ostf-plugin-context-1.1.schema.json](../schema/ostf-plugin-context-1.1.schema.json) | 8 | 153 |

## Added data and semantics

| Entry | Meaning |
|---|---|
| `takeGroups` | MIDI candidates, Comps, selections and separate outputs |
| `audioTakeGroups` | Audio candidates, frame references, outputs and transitions |
| `compRegions` | Complete source/silence partition of the Group |
| `activeCompId` | Saved selection; null means silence |
| `visitSelections` | Finite Visit playback overlay |
| `liveSelection` | Launch-time policy |
| `origin/ratings/parentTakeId/takeSelectionHistory` | Provenance, rating, lineage and history; no implicit playback change |

Versioned Schemas govern shape; [SPECIFICATION](SPECIFICATION.md) and the [semantic index](SEMANTIC_REQUIREMENTS.md) govern references, ownership, time and output consistency beyond shape. A declaration is not a guarantee of runtime behavior.

## ostf-5.1.0.schema.json

| Schema Pointer | Required in direct parent | Constraints | Original description |
|---|---|---|---|
| `/` | Context / conditional | $schema: "https://json-schema.org/draft/2020-12/schema"; $id: "https://yoh-nak.github.io/ostf/schema/ostf-5.1.0.schema.json"; type: "object"; properties: 25 entries (see descendant pointers); required: ["format","version","ppq","song","timeline","harmony","tracks","soundSlots","lyrics","resources"]; additionalProperties: false; $defs: 141 entries (see descendant pointers) | Complete OSTF 5.1 musical Core. Inherits the OSTF 5.0/4.3 song, harmony, lyrics, MIDI, phrase, performance-intent and finite-plan definitions; adds optional non-destructive Take Groups and materialized Comp outputs. |
| `/properties/format` | Yes | const: "OSTF" |  |
| `/properties/version` | Yes | const: "5.1.0" |  |
| `/properties/ppq` | Yes | type: "integer"; minimum: 1; maximum: 960000 |  |
| `/properties/song` | Yes | $ref: "#/$defs/song" |  |
| `/properties/timeline` | Yes | $ref: "#/$defs/timeline" |  |
| `/properties/harmony` | Yes | $ref: "#/$defs/harmony" |  |
| `/properties/tracks` | Yes | type: "array"; items: 1 entries (see descendant pointers) |  |
| `/properties/tracks/items` | Context / conditional | $ref: "#/$defs/track" |  |
| `/properties/soundSlots` | Yes | type: "array"; items: 1 entries (see descendant pointers) |  |
| `/properties/soundSlots/items` | Context / conditional | $ref: "#/$defs/soundSlot" |  |
| `/properties/lyrics` | Yes | $ref: "#/$defs/lyrics" |  |
| `/properties/resources` | Yes | type: "array"; items: 1 entries (see descendant pointers) |  |
| `/properties/resources/items` | Context / conditional | $ref: "#/$defs/resource" |  |
| `/properties/extensions` | No | $ref: "#/$defs/legacy33/$defs/extensions" | Optional third-party or verbatim legacy compatibility payloads. Standard Core always remains authoritative. New first-party common information must not be stored only here. |
| `/properties/drumKits` | No | type: "array"; items: 1 entries (see descendant pointers) | Optional multiple percussion-kit definitions; absent = no declared kits (3.0 compatible). |
| `/properties/drumKits/items` | Context / conditional | $ref: "#/$defs/drumKit" |  |
| `/properties/contributors` | No | type: "array"; items: 1 entries (see descendant pointers) | Optional unordered identity records referenced by song.credits. No contributor limit is imposed by this format. |
| `/properties/contributors/items` | Context / conditional | $ref: "#/$defs/contributor" |  |
| `/properties/document` | No | $ref: "#/$defs/documentInfo" |  |
| `/properties/relativePhrases` | No | $ref: "#/$defs/relativePhrases" |  |
| `/properties/generation` | No | $ref: "#/$defs/generation" |  |
| `/properties/presentation` | No | $ref: "#/$defs/presentation" |  |
| `/properties/phraseLibrary` | No | $ref: "#/$defs/phraseLibrary" |  |
| `/properties/clipChoices` | No | $ref: "#/$defs/clipChoices" |  |
| `/properties/localization` | No | $ref: "#/$defs/localization" |  |
| `/properties/provenance` | No | $ref: "#/$defs/provenance" |  |
| `/properties/midi` | No | $ref: "#/$defs/midi" | Optional document-level logical MIDI bus declarations. No physical device or DAW port assignment is encoded. |
| `/properties/ensembleInteractions` | No | type: "array"; items: 1 entries (see descendant pointers) | Optional directed music relationships; these neither materialize notes nor initiate network messages. |
| `/properties/ensembleInteractions/items` | Context / conditional | $ref: "#/$defs/ensembleInteraction" |  |
| `/properties/performancePlans` | No | type: "array"; items: 1 entries (see descendant pointers) | Optional finite source-timeline playthroughs; do not modify source timeline or concrete notes. |
| `/properties/performancePlans/items` | Context / conditional | $ref: "#/$defs/performancePlan" |  |
| `/properties/takeGroups` | No | type: "array"; items: 1 entries (see descendant pointers) |  |
| `/properties/takeGroups/items` | Context / conditional | $ref: "#/$defs/midiTakeGroup51" |  |
| `/$defs/id` | Context / conditional | type: "string"; pattern: "^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$"; not: 1 entries (see descendant pointers) |  |
| `/$defs/id/not` | Context / conditional | pattern: "[\\r\\n\\u2028\\u2029]" |  |
| `/$defs/nonnegative` | Context / conditional | type: "integer"; minimum: 0; maximum: 9007199254740991 |  |
| `/$defs/positive` | Context / conditional | type: "integer"; minimum: 1; maximum: 9007199254740991 |  |
| `/$defs/signed` | Context / conditional | type: "integer"; minimum: -9007199254740991; maximum: 9007199254740991 |  |
| `/$defs/pitch` | Context / conditional | type: "integer"; minimum: 0; maximum: 127 |  |
| `/$defs/ref` | Context / conditional | type: "object"; properties: 2 entries (see descendant pointers); required: ["type","id"]; additionalProperties: false |  |
| `/$defs/ref/properties/type` | Yes | enum: ["section","track","clip","note","chord","scale","soundSlot","drumKit","lyricDocument","lyricPhrase","lyricUnit","lyricAlignment","resource","genre","contributor","credit","alternateTitle","mood","keyChange","phraseTemplate","phraseInstance","clipChoiceGroup","clipCandidate","roleDefinition","generationProcess","provenanceRecord","midiBus","midiEvent","lyricVoice","trackDirection","ensembleInteraction","performancePlan","performanceVisit"] |  |
| `/$defs/ref/properties/id` | Yes | $ref: "#/$defs/id" |  |
| `/$defs/range` | Context / conditional | type: "object"; properties: 2 entries (see descendant pointers); required: ["start","duration"]; additionalProperties: false |  |
| `/$defs/range/properties/start` | Yes | $ref: "#/$defs/nonnegative" |  |
| `/$defs/range/properties/duration` | Yes | $ref: "#/$defs/positive" |  |
| `/$defs/spelledPitchClass` | Context / conditional | type: "object"; properties: 2 entries (see descendant pointers); required: ["step","alter"]; additionalProperties: false |  |
| `/$defs/spelledPitchClass/properties/step` | Yes | enum: ["A","B","C","D","E","F","G"] |  |
| `/$defs/spelledPitchClass/properties/alter` | Yes | type: "integer"; minimum: -2; maximum: 2 |  |
| `/$defs/song` | Context / conditional | type: "object"; properties: 15 entries (see descendant pointers); required: ["title"]; additionalProperties: false |  |
| `/$defs/song/properties/title` | Yes | type: "string" |  |
| `/$defs/song/properties/primaryMelodyTrackId` | No | $ref: "#/$defs/id" |  |
| `/$defs/song/properties/localizedTitles` | No | $ref: "#/$defs/localizedNames" | Optional localized song-title alternatives. song.title is the stable fallback. |
| `/$defs/song/properties/subtitle` | No | type: "string" | Optional original-language subtitle. |
| `/$defs/song/properties/description` | No | type: "string" | Optional original-language description, including Unicode and line breaks. |
| `/$defs/song/properties/alternateTitles` | No | type: "array"; items: 1 entries (see descendant pointers) | Additional stable-ID source-language titles. |
| `/$defs/song/properties/alternateTitles/items` | Context / conditional | $ref: "#/$defs/alternateTitle" |  |
| `/$defs/song/properties/credits` | No | type: "array"; items: 1 entries (see descendant pointers) | Ordered credit assignments to contributors. Multiple roles and duplicate contributors permitted. |
| `/$defs/song/properties/credits/items` | Context / conditional | $ref: "#/$defs/credit" |  |
| `/$defs/song/properties/genres` | No | type: "array"; items: 1 entries (see descendant pointers) | Optional open-ended ordered genre tags; zero or more allowed. Order is authored display preference, first item is primary if a primary label is desired, not a generator weight. Absent means unspecified. |
| `/$defs/song/properties/genres/items` | Context / conditional | $ref: "#/$defs/genre" |  |
| `/$defs/song/properties/key` | No | $ref: "#/$defs/key" |  |
| `/$defs/song/properties/scale` | No | $ref: "#/$defs/scaleDefinition" |  |
| `/$defs/song/properties/languages` | No | type: "array"; items: 3 entries (see descendant pointers); uniqueItems: true |  |
| `/$defs/song/properties/languages/items` | Context / conditional | type: "string"; minLength: 1 | Authored language tag, preferably BCP 47. Unknown spelling is retained; case-insensitive duplicate tags forbidden. |
| `/$defs/song/properties/primaryLyricDocumentId` | No | $ref: "#/$defs/id" |  |
| `/$defs/song/properties/moods` | No | type: "array"; items: 1 entries (see descendant pointers) |  |
| `/$defs/song/properties/moods/items` | Context / conditional | $ref: "#/$defs/mood" |  |
| `/$defs/song/properties/rights` | No | $ref: "#/$defs/rightsStatement" |  |
| `/$defs/song/properties/melodyTrackIds` | No | type: "array"; uniqueItems: true; items: 1 entries (see descendant pointers) | Optional ordered set of tracks explicitly authored as melody-bearing tracks. If present with primaryMelodyTrackId, the primary track must be a member. |
| `/$defs/song/properties/melodyTrackIds/items` | Context / conditional | $ref: "#/$defs/id" |  |
| `/$defs/section` | Context / conditional | type: "object"; properties: 6 entries (see descendant pointers); required: ["id","name","start","duration"]; additionalProperties: false |  |
| `/$defs/section/properties/id` | Yes | $ref: "#/$defs/id" |  |
| `/$defs/section/properties/name` | Yes | type: "string"; minLength: 1 |  |
| `/$defs/section/properties/start` | Yes | $ref: "#/$defs/nonnegative" |  |
| `/$defs/section/properties/duration` | Yes | $ref: "#/$defs/positive" |  |
| `/$defs/section/properties/role` | No | type: "string" |  |
| `/$defs/section/properties/localizedNames` | No | $ref: "#/$defs/localizedNames" | Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity. |
| `/$defs/tempo` | Context / conditional | type: "object"; properties: 2 entries (see descendant pointers); required: ["at","bpm"]; additionalProperties: false |  |
| `/$defs/tempo/properties/at` | Yes | $ref: "#/$defs/nonnegative" |  |
| `/$defs/tempo/properties/bpm` | Yes | type: "number"; exclusiveMinimum: 0; maximum: 1000 |  |
| `/$defs/meter` | Context / conditional | type: "object"; properties: 4 entries (see descendant pointers); required: ["at","numerator","denominator"]; additionalProperties: false |  |
| `/$defs/meter/properties/at` | Yes | $ref: "#/$defs/nonnegative" |  |
| `/$defs/meter/properties/numerator` | Yes | type: "integer"; minimum: 1; maximum: 64 |  |
| `/$defs/meter/properties/denominator` | Yes | enum: [1,2,4,8,16,32,64]; type: "integer" |  |
| `/$defs/meter/properties/beatGroups` | No | type: "array"; items: 3 entries (see descendant pointers); minItems: 1; maxItems: 64 | Optional additive grouping in denominator units. Values must sum to numerator. Descriptive only; does not change note timestamps. |
| `/$defs/meter/properties/beatGroups/items` | Context / conditional | type: "integer"; minimum: 1; maximum: 64 |  |
| `/$defs/timeline` | Context / conditional | type: "object"; properties: 6 entries (see descendant pointers); required: ["sections","tempoChanges","meterChanges"]; additionalProperties: false |  |
| `/$defs/timeline/properties/sections` | Yes | type: "array"; items: 1 entries (see descendant pointers) |  |
| `/$defs/timeline/properties/sections/items` | Context / conditional | $ref: "#/$defs/section" |  |
| `/$defs/timeline/properties/tempoChanges` | Yes | type: "array"; items: 1 entries (see descendant pointers); minItems: 1 |  |
| `/$defs/timeline/properties/tempoChanges/items` | Context / conditional | $ref: "#/$defs/tempo" |  |
| `/$defs/timeline/properties/meterChanges` | Yes | type: "array"; items: 1 entries (see descendant pointers); minItems: 1 |  |
| `/$defs/timeline/properties/meterChanges/items` | Context / conditional | $ref: "#/$defs/meter" |  |
| `/$defs/timeline/properties/keyChanges` | No | type: "array"; items: 1 entries (see descendant pointers) |  |
| `/$defs/timeline/properties/keyChanges/items` | Context / conditional | $ref: "#/$defs/keyChange" |  |
| `/$defs/timeline/properties/duration` | No | $ref: "#/$defs/nonnegative" |  |
| `/$defs/timeline/properties/barOrigin` | No | $ref: "#/$defs/nonnegative" |  |
| `/$defs/chord` | Context / conditional | type: "object"; properties: 8 entries (see descendant pointers); required: ["id","start","duration","label"]; additionalProperties: false; dependentRequired: {"root":["intervals"],"intervals":["root"]} |  |
| `/$defs/chord/properties/id` | Yes | $ref: "#/$defs/id" |  |
| `/$defs/chord/properties/start` | Yes | $ref: "#/$defs/nonnegative" |  |
| `/$defs/chord/properties/duration` | Yes | $ref: "#/$defs/positive" |  |
| `/$defs/chord/properties/label` | Yes | type: "string"; minLength: 1 |  |
| `/$defs/chord/properties/root` | No | $ref: "#/$defs/spelledPitchClass" |  |
| `/$defs/chord/properties/intervals` | No | type: "array"; items: 3 entries (see descendant pointers); minItems: 1; maxItems: 36; uniqueItems: true; contains: 1 entries (see descendant pointers) |  |
| `/$defs/chord/properties/intervals/items` | Context / conditional | type: "integer"; minimum: 0; maximum: 35 |  |
| `/$defs/chord/properties/intervals/contains` | Context / conditional | const: 0 |  |
| `/$defs/chord/properties/bass` | No | $ref: "#/$defs/spelledPitchClass" |  |
| `/$defs/chord/properties/voicing` | No | $ref: "#/$defs/voicing" | Optional pitch snapshot (not an arrangement note sequence). No automatic playback. |
| `/$defs/scale` | Context / conditional | type: "object"; properties: 7 entries (see descendant pointers); required: ["id","start","duration","tonic","intervals"]; additionalProperties: false |  |
| `/$defs/scale/properties/id` | Yes | $ref: "#/$defs/id" |  |
| `/$defs/scale/properties/start` | Yes | $ref: "#/$defs/nonnegative" |  |
| `/$defs/scale/properties/duration` | Yes | $ref: "#/$defs/positive" |  |
| `/$defs/scale/properties/label` | No | type: "string" |  |
| `/$defs/scale/properties/tonic` | Yes | $ref: "#/$defs/spelledPitchClass" |  |
| `/$defs/scale/properties/intervals` | Yes | type: "array"; items: 3 entries (see descendant pointers); minItems: 1; maxItems: 12; uniqueItems: true; contains: 1 entries (see descendant pointers) |  |
| `/$defs/scale/properties/intervals/items` | Context / conditional | type: "integer"; minimum: 0; maximum: 11 |  |
| `/$defs/scale/properties/intervals/contains` | Context / conditional | const: 0 |  |
| `/$defs/scale/properties/targets` | No | type: "array"; items: 1 entries (see descendant pointers); minItems: 1; uniqueItems: true | Optional explicit scope. Absence means general timed context, not a global key. Overlapping contexts are not resolved by array order. |
| `/$defs/scale/properties/targets/items` | Context / conditional | $ref: "#/$defs/scaleTarget" |  |
| `/$defs/harmony` | Context / conditional | type: "object"; properties: 2 entries (see descendant pointers); required: ["chords","scales"]; additionalProperties: false |  |
| `/$defs/harmony/properties/chords` | Yes | type: "array"; items: 1 entries (see descendant pointers) |  |
| `/$defs/harmony/properties/chords/items` | Context / conditional | $ref: "#/$defs/chord" |  |
| `/$defs/harmony/properties/scales` | Yes | type: "array"; items: 1 entries (see descendant pointers) |  |
| `/$defs/harmony/properties/scales/items` | Context / conditional | $ref: "#/$defs/scale" |  |
| `/$defs/instrument` | Context / conditional | type: "object"; properties: 4 entries (see descendant pointers); required: ["name"]; additionalProperties: false |  |
| `/$defs/instrument/properties/name` | Yes | type: "string" |  |
| `/$defs/instrument/properties/family` | No | type: "string" |  |
| `/$defs/instrument/properties/localizedNames` | No | $ref: "#/$defs/localizedNames" | Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity. |
| `/$defs/instrument/properties/playablePitchRange` | No | $ref: "#/$defs/playablePitchRange" |  |
| `/$defs/note` | Context / conditional | type: "object"; properties: 12 entries (see descendant pointers); required: ["id","start","duration"]; additionalProperties: false; oneOf: 2 branches (see descendant pointers); dependentRequired: {"velocityDeviation":["velocity"]}; allOf: 1 branches (see descendant pointers) | Concrete Core DAW-note event. The event target is pitch or soundSlotId. Optional 3.5 note-local properties preserve mute, release velocity, probability and velocity variation. pitchRole=fixedTrigger marks a literal MIDI key trigger that must not be musically transposed or analyzed. |
| `/$defs/note/properties/id` | Yes | $ref: "#/$defs/id" |  |
| `/$defs/note/properties/start` | Yes | $ref: "#/$defs/signed" |  |
| `/$defs/note/properties/duration` | Yes | $ref: "#/$defs/positive" | Positive note gate in ticks, not the guaranteed audible duration of a one-shot percussion sample. |
| `/$defs/note/properties/pitch` | No | $ref: "#/$defs/pitch" |  |
| `/$defs/note/properties/soundSlotId` | No | $ref: "#/$defs/id" | Document-local Sound Slot ID. Distinct events and IDs stay distinct even if several slots share a MIDI key; a renderer decides the acoustic timbre. |
| `/$defs/note/properties/velocity` | No | type: "integer"; minimum: 1; maximum: 127 | Optional authored note-on velocity for performed Core notes, 1–127; omit to mean unspecified. It is not a note-off velocity, controller stream, chord tone, or a sound-rendering guarantee. Never insert an inferred default when saving. |
| `/$defs/note/properties/enabled` | No | type: "boolean"; default: true | Optional note-local enable state. Omitted means enabled. False preserves the note but suppresses scheduling/playback; it is distinct from probability=0. |
| `/$defs/note/properties/releaseVelocity` | No | type: "integer"; minimum: 0; maximum: 127 | Optional MIDI Note Off/release velocity, 0-127. Omit when unspecified; readers must not invent and write back a default. |
| `/$defs/note/properties/probability` | No | type: "number"; minimum: 0; maximum: 1; default: 1 | Optional note-playback probability from 0.0 to 1.0. Omitted means 1.0. Random sequence identity is not standardized; materialize notes for deterministic interchange. |
| `/$defs/note/properties/velocityDeviation` | No | type: "integer"; minimum: -126; maximum: 126; default: 0 | Optional note-local velocity variation endpoint relative to velocity. Requires velocity. Semantic rule: velocity + velocityDeviation must remain within 1..127. Omitted means 0. |
| `/$defs/note/properties/pitchRole` | No | enum: ["musical","fixedTrigger"]; default: "musical" | Meaning of a pitch note. musical participates in pitch/harmony/transpose operations; fixedTrigger is an exact MIDI key trigger (for example a keyswitch) and is never transposed or used as musical-pitch evidence. Allowed only on pitch notes. |
| `/$defs/note/properties/channel` | No | $ref: "#/$defs/midiChannel" | Optional concrete MIDI channel for this performed note. In singleChannel mode it may be omitted and inherited from the track; in multiChannel/MPE mode semantic rules require explicit channel where channel identity matters. |
| `/$defs/note/oneOf/0` | Context / conditional | required: ["pitch"]; not: 1 entries (see descendant pointers) |  |
| `/$defs/note/oneOf/0/not` | Context / conditional | required: ["soundSlotId"] |  |
| `/$defs/note/oneOf/1` | Context / conditional | required: ["soundSlotId"]; not: 1 entries (see descendant pointers) |  |
| `/$defs/note/oneOf/1/not` | Context / conditional | required: ["pitch"] |  |
| `/$defs/note/allOf/0` | Context / conditional | if: 1 entries (see descendant pointers); then: 1 entries (see descendant pointers) |  |
| `/$defs/note/allOf/0/if` | Context / conditional | required: ["soundSlotId"] |  |
| `/$defs/note/allOf/0/then` | Context / conditional | not: 1 entries (see descendant pointers) |  |
| `/$defs/note/allOf/0/then/not` | Context / conditional | required: ["pitchRole"] |  |
| `/$defs/clip` | Context / conditional | type: "object"; properties: 9 entries (see descendant pointers); required: ["id","start","duration","notes"]; additionalProperties: false |  |
| `/$defs/clip/properties/id` | Yes | $ref: "#/$defs/id" |  |
| `/$defs/clip/properties/name` | No | type: "string" |  |
| `/$defs/clip/properties/start` | Yes | $ref: "#/$defs/nonnegative" |  |
| `/$defs/clip/properties/duration` | Yes | $ref: "#/$defs/positive" |  |
| `/$defs/clip/properties/enabled` | No | type: "boolean"; default: true |  |
| `/$defs/clip/properties/notes` | Yes | type: "array"; items: 1 entries (see descendant pointers) |  |
| `/$defs/clip/properties/notes/items` | Context / conditional | $ref: "#/$defs/note" |  |
| `/$defs/clip/properties/localizedNames` | No | $ref: "#/$defs/localizedNames" | Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity. |
| `/$defs/clip/properties/midiEvents` | No | type: "array"; items: 1 entries (see descendant pointers) | Optional clip-local MIDI performance/control events. start is local to the clip and may be negative if absolute time remains nonnegative. Notes remain authoritative in notes[]. |
| `/$defs/clip/properties/midiEvents/items` | Context / conditional | $ref: "#/$defs/midiEvent" |  |
| `/$defs/clip/properties/vocalPerformances` | No | type: "array"; items: 1 entries (see descendant pointers); minItems: 1 | Optional voice-specific phoneme and singing-performance data; references lyrics.voices. Notes/MIDI remain authoritative for MIDI playback. |
| `/$defs/clip/properties/vocalPerformances/items` | Context / conditional | $ref: "#/$defs/vocalPerformance" |  |
| `/$defs/track` | Context / conditional | type: "object"; properties: 14 entries (see descendant pointers); required: ["id","name","clips"]; additionalProperties: false; allOf: 1 branches (see descendant pointers) |  |
| `/$defs/track/properties/id` | Yes | $ref: "#/$defs/id" |  |
| `/$defs/track/properties/name` | Yes | type: "string" |  |
| `/$defs/track/properties/role` | No | type: "string" |  |
| `/$defs/track/properties/instrument` | No | $ref: "#/$defs/instrument" |  |
| `/$defs/track/properties/enabled` | No | type: "boolean"; default: true |  |
| `/$defs/track/properties/clips` | Yes | type: "array"; items: 1 entries (see descendant pointers) |  |
| `/$defs/track/properties/clips/items` | Context / conditional | $ref: "#/$defs/clip" |  |
| `/$defs/track/properties/trackType` | No | enum: ["melodic","drum","mixed"] | Semantic event-target category; optional; missing/empty-note tracks may be unknown. It is not a DAW track class. |
| `/$defs/track/properties/preferredView` | No | enum: ["auto","pianoRoll","drumGrid"]; default: "auto" | Non-binding presentation preference. Does not change note meaning. |
| `/$defs/track/properties/soundSource` | No | $ref: "#/$defs/soundSource" | Optional sound-source selection hint, not a plug-in state, preset blob, or sound guarantee. |
| `/$defs/track/properties/localizedNames` | No | $ref: "#/$defs/localizedNames" | Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity. |
| `/$defs/track/properties/drumKitId` | No | $ref: "#/$defs/id" | Optional reference to a declared drumKit; only for a drum/mixed or empty inferred track. All stored slot events in the track must belong to the referenced kit. |
| `/$defs/track/properties/midi` | No | $ref: "#/$defs/trackMidi" |  |
| `/$defs/track/properties/directions` | No | type: "array"; items: 1 entries (see descendant pointers) | Optional typed semantic instructions for performance, interpretation, or generation. Uses the global OSTF timebase; it is not a second timeline. |
| `/$defs/track/properties/directions/items` | Context / conditional | $ref: "#/$defs/trackDirection" |  |
| `/$defs/track/properties/performanceRequirements` | No | $ref: "#/$defs/performanceRequirements" | Portable requirements for realizing this track, not a robot/device capability report. |
| `/$defs/track/allOf/0` | Context / conditional | if: 2 entries (see descendant pointers); then: 1 entries (see descendant pointers) |  |
| `/$defs/track/allOf/0/if` | Context / conditional | properties: 1 entries (see descendant pointers); required: ["trackType"] |  |
| `/$defs/track/allOf/0/if/properties/trackType` | Yes | const: "melodic" |  |
| `/$defs/track/allOf/0/then` | Context / conditional | not: 1 entries (see descendant pointers) |  |
| `/$defs/track/allOf/0/then/not` | Context / conditional | required: ["drumKitId"] |  |
| `/$defs/soundSlot` | Context / conditional | type: "object"; properties: 6 entries (see descendant pointers); required: ["id","name"]; additionalProperties: false | Document-local stable logical percussion target. Equal roles, names or MIDI note mappings never merge distinct slot IDs. No sample/audio identity is encoded. |
| `/$defs/soundSlot/properties/id` | Yes | $ref: "#/$defs/id" |  |
| `/$defs/soundSlot/properties/name` | Yes | type: "string" |  |
| `/$defs/soundSlot/properties/role` | No | type: "string" | Optional free-text musical role; not a standardized GM instrument code or an acoustic sample identifier. |
| `/$defs/soundSlot/properties/midiNote` | No | $ref: "#/$defs/pitch" | Legacy 3.0 MIDI note hint only; not a GM1 declaration or preview timbre identity. |
| `/$defs/soundSlot/properties/midiMapping` | No | $ref: "#/$defs/midiMapping" | Explicit external MIDI1 output mapping; standard=gm1 is separate from custom even for an equal note number. Not a unique slot or audio identity. |
| `/$defs/soundSlot/properties/localizedNames` | No | $ref: "#/$defs/localizedNames" | Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity. |
| `/$defs/lyricDocument` | Context / conditional | type: "object"; properties: 3 entries (see descendant pointers); required: ["id"]; additionalProperties: false |  |
| `/$defs/lyricDocument/properties/id` | Yes | $ref: "#/$defs/id" |  |
| `/$defs/lyricDocument/properties/title` | No | type: "string" |  |
| `/$defs/lyricDocument/properties/language` | No | type: "string" |  |
| `/$defs/lyricPhrase` | Context / conditional | type: "object"; properties: 6 entries (see descendant pointers); required: ["id","documentId","text"]; additionalProperties: false; dependentRequired: {"start":["duration"],"duration":["start"]} |  |
| `/$defs/lyricPhrase/properties/id` | Yes | $ref: "#/$defs/id" |  |
| `/$defs/lyricPhrase/properties/documentId` | Yes | $ref: "#/$defs/id" |  |
| `/$defs/lyricPhrase/properties/text` | Yes | type: "string" |  |
| `/$defs/lyricPhrase/properties/pronunciation` | No | type: "string" |  |
| `/$defs/lyricPhrase/properties/start` | No | $ref: "#/$defs/nonnegative" |  |
| `/$defs/lyricPhrase/properties/duration` | No | $ref: "#/$defs/positive" |  |
| `/$defs/lyricUnit` | Context / conditional | type: "object"; properties: 7 entries (see descendant pointers); required: ["id","phraseId","text"]; additionalProperties: false; dependentRequired: {"start":["duration"],"duration":["start"]} |  |
| `/$defs/lyricUnit/properties/id` | Yes | $ref: "#/$defs/id" |  |
| `/$defs/lyricUnit/properties/phraseId` | Yes | $ref: "#/$defs/id" |  |
| `/$defs/lyricUnit/properties/text` | Yes | type: "string" |  |
| `/$defs/lyricUnit/properties/pronunciation` | No | type: "string" |  |
| `/$defs/lyricUnit/properties/start` | No | $ref: "#/$defs/nonnegative" |  |
| `/$defs/lyricUnit/properties/duration` | No | $ref: "#/$defs/positive" |  |
| `/$defs/lyricUnit/properties/phonetics` | No | type: "array"; items: 1 entries (see descendant pointers); minItems: 1 | Optional alternate phoneme token sequences. Do not alter text/pronunciation. Multiple alphabets are permitted. |
| `/$defs/lyricUnit/properties/phonetics/items` | Context / conditional | $ref: "#/$defs/vocalPhonetics" |  |
| `/$defs/lyricAlignment` | Context / conditional | type: "object"; properties: 4 entries (see descendant pointers); required: ["id","unitIds","noteIds"]; additionalProperties: false |  |
| `/$defs/lyricAlignment/properties/id` | Yes | $ref: "#/$defs/id" |  |
| `/$defs/lyricAlignment/properties/unitIds` | Yes | type: "array"; items: 1 entries (see descendant pointers); uniqueItems: true; minItems: 1 |  |
| `/$defs/lyricAlignment/properties/unitIds/items` | Context / conditional | $ref: "#/$defs/id" |  |
| `/$defs/lyricAlignment/properties/noteIds` | Yes | type: "array"; items: 1 entries (see descendant pointers); uniqueItems: true; minItems: 1 |  |
| `/$defs/lyricAlignment/properties/noteIds/items` | Context / conditional | $ref: "#/$defs/id" |  |
| `/$defs/lyricAlignment/properties/voiceId` | No | $ref: "#/$defs/id" | Optional lyricVoice association. When present, aligned units must belong to that voice document and aligned notes must belong to that voice track. |
| `/$defs/lyrics` | Context / conditional | type: "object"; properties: 5 entries (see descendant pointers); required: ["documents","phrases","units","alignments"]; additionalProperties: false |  |
| `/$defs/lyrics/properties/documents` | Yes | type: "array"; items: 1 entries (see descendant pointers) |  |
| `/$defs/lyrics/properties/documents/items` | Context / conditional | $ref: "#/$defs/lyricDocument" |  |
| `/$defs/lyrics/properties/phrases` | Yes | type: "array"; items: 1 entries (see descendant pointers) |  |
| `/$defs/lyrics/properties/phrases/items` | Context / conditional | $ref: "#/$defs/lyricPhrase" |  |
| `/$defs/lyrics/properties/units` | Yes | type: "array"; items: 1 entries (see descendant pointers) |  |
| `/$defs/lyrics/properties/units/items` | Context / conditional | $ref: "#/$defs/lyricUnit" |  |
| `/$defs/lyrics/properties/alignments` | Yes | type: "array"; items: 1 entries (see descendant pointers) |  |
| `/$defs/lyrics/properties/alignments/items` | Context / conditional | $ref: "#/$defs/lyricAlignment" |  |
| `/$defs/lyrics/properties/voices` | No | type: "array"; items: 1 entries (see descendant pointers) | Optional explicit vocal-part relationships for multi-voice, harmony and chorus lyrics. |
| `/$defs/lyrics/properties/voices/items` | Context / conditional | $ref: "#/$defs/lyricVoice" |  |
| `/$defs/sha256` | Context / conditional | type: "string"; pattern: "^[0-9a-f]{64}$"; not: 1 entries (see descendant pointers) |  |
| `/$defs/sha256/not` | Context / conditional | pattern: "[\\r\\n\\u2028\\u2029]" |  |
| `/$defs/resource` | Context / conditional | type: "object"; properties: 5 entries (see descendant pointers); required: ["id","kind","uri"]; additionalProperties: false |  |
| `/$defs/resource/properties/id` | Yes | $ref: "#/$defs/id" |  |
| `/$defs/resource/properties/kind` | Yes | enum: ["audio","midi","text","other"] |  |
| `/$defs/resource/properties/uri` | Yes | type: "string"; minLength: 1 |  |
| `/$defs/resource/properties/name` | No | type: "string" |  |
| `/$defs/resource/properties/sha256` | No | $ref: "#/$defs/sha256" |  |
| `/$defs/dependencies` | Context / conditional | oneOf: 2 branches (see descendant pointers) |  |
| `/$defs/dependencies/oneOf/0` | Context / conditional | type: "object"; properties: 1 entries (see descendant pointers); required: ["scope"]; additionalProperties: false |  |
| `/$defs/dependencies/oneOf/0/properties/scope` | Yes | enum: ["document","none"] |  |
| `/$defs/dependencies/oneOf/1` | Context / conditional | type: "object"; properties: 2 entries (see descendant pointers); required: ["scope","refs"]; additionalProperties: false |  |
| `/$defs/dependencies/oneOf/1/properties/scope` | Yes | const: "objects" |  |
| `/$defs/dependencies/oneOf/1/properties/refs` | Yes | type: "array"; items: 1 entries (see descendant pointers); minItems: 1; uniqueItems: true |  |
| `/$defs/dependencies/oneOf/1/properties/refs/items` | Context / conditional | $ref: "#/$defs/ref" |  |
| `/$defs/relativeAssignment` | Context / conditional | type: "object"; properties: 6 entries (see descendant pointers); required: ["noteId","basis","contextId","anchorPitch","index","chromaticOffset"]; additionalProperties: false; allOf: 1 branches (see descendant pointers) |  |
| `/$defs/relativeAssignment/properties/noteId` | Yes | $ref: "#/$defs/id" |  |
| `/$defs/relativeAssignment/properties/basis` | Yes | enum: ["chordTone","scaleDegree"] |  |
| `/$defs/relativeAssignment/properties/contextId` | Yes | $ref: "#/$defs/id" |  |
| `/$defs/relativeAssignment/properties/anchorPitch` | Yes | $ref: "#/$defs/pitch" |  |
| `/$defs/relativeAssignment/properties/index` | Yes | type: "integer"; minimum: 1; maximum: 36 |  |
| `/$defs/relativeAssignment/properties/chromaticOffset` | Yes | type: "integer"; minimum: -24; maximum: 24 |  |
| `/$defs/relativeAssignment/allOf/0` | Context / conditional | if: 2 entries (see descendant pointers); then: 1 entries (see descendant pointers) |  |
| `/$defs/relativeAssignment/allOf/0/if` | Context / conditional | properties: 1 entries (see descendant pointers); required: ["basis"] |  |
| `/$defs/relativeAssignment/allOf/0/if/properties/basis` | Yes | const: "scaleDegree" |  |
| `/$defs/relativeAssignment/allOf/0/then` | Context / conditional | properties: 1 entries (see descendant pointers) |  |
| `/$defs/relativeAssignment/allOf/0/then/properties/index` | No | maximum: 12 |  |
| `/$defs/generator` | Context / conditional | type: "object"; properties: 2 entries (see descendant pointers); required: ["id","version"]; additionalProperties: false |  |
| `/$defs/generator/properties/id` | Yes | type: "string"; minLength: 1 |  |
| `/$defs/generator/properties/version` | Yes | type: "string"; minLength: 1 |  |
| `/$defs/generationInput` | Context / conditional | type: "object"; properties: 3 entries (see descendant pointers); required: ["role","ref"]; additionalProperties: false |  |
| `/$defs/generationInput/properties/role` | Yes | type: "string"; minLength: 1 |  |
| `/$defs/generationInput/properties/ref` | Yes | $ref: "#/$defs/ref" |  |
| `/$defs/generationInput/properties/readRange` | No | $ref: "#/$defs/range" |  |
| `/$defs/generationProcess` | Context / conditional | type: "object"; properties: 7 entries (see descendant pointers); required: ["id","generator","inputs","outputs","protectedNoteIds"]; additionalProperties: false |  |
| `/$defs/generationProcess/properties/id` | Yes | $ref: "#/$defs/id" |  |
| `/$defs/generationProcess/properties/generator` | Yes | $ref: "#/$defs/generator" |  |
| `/$defs/generationProcess/properties/inputs` | Yes | type: "array"; items: 1 entries (see descendant pointers) |  |
| `/$defs/generationProcess/properties/inputs/items` | Context / conditional | $ref: "#/$defs/generationInput" |  |
| `/$defs/generationProcess/properties/outputs` | Yes | type: "array"; items: 1 entries (see descendant pointers); minItems: 1 |  |
| `/$defs/generationProcess/properties/outputs/items` | Context / conditional | $ref: "#/$defs/ref" |  |
| `/$defs/generationProcess/properties/targetRange` | No | $ref: "#/$defs/range" |  |
| `/$defs/generationProcess/properties/protectedNoteIds` | Yes | type: "array"; items: 1 entries (see descendant pointers); uniqueItems: true |  |
| `/$defs/generationProcess/properties/protectedNoteIds/items` | Context / conditional | $ref: "#/$defs/id" |  |
| `/$defs/generationProcess/properties/intent` | No | $ref: "#/$defs/generationIntent" |  |
| `/$defs/color` | Context / conditional | type: "string"; pattern: "^#[0-9A-Fa-f]{6}$"; not: 1 entries (see descendant pointers) |  |
| `/$defs/color/not` | Context / conditional | pattern: "[\\r\\n\\u2028\\u2029]" |  |
| `/$defs/roleDefinition` | Context / conditional | type: "object"; properties: 3 entries (see descendant pointers); required: ["id","name"]; additionalProperties: false |  |
| `/$defs/roleDefinition/properties/id` | Yes | $ref: "#/$defs/id" |  |
| `/$defs/roleDefinition/properties/name` | Yes | type: "string"; minLength: 1 |  |
| `/$defs/roleDefinition/properties/baseRole` | No | type: "string" |  |
| `/$defs/roleColorMap` | Context / conditional | type: "object"; additionalProperties: 1 entries (see descendant pointers) |  |
| `/$defs/roleColorMap/additionalProperties` | Context / conditional | $ref: "#/$defs/color" |  |
| `/$defs/customRoleColorMap` | Context / conditional | type: "object"; propertyNames: 1 entries (see descendant pointers); additionalProperties: 1 entries (see descendant pointers) |  |
| `/$defs/customRoleColorMap/propertyNames` | Context / conditional | $ref: "#/$defs/id" |  |
| `/$defs/customRoleColorMap/additionalProperties` | Context / conditional | $ref: "#/$defs/color" |  |
| `/$defs/objectColor` | Context / conditional | type: "object"; properties: 2 entries (see descendant pointers); required: ["target","color"]; additionalProperties: false |  |
| `/$defs/objectColor/properties/target` | Yes | $ref: "#/$defs/ref" |  |
| `/$defs/objectColor/properties/color` | Yes | $ref: "#/$defs/color" |  |
| `/$defs/phraseTemplate` | Context / conditional | type: "object"; properties: 4 entries (see descendant pointers); required: ["id","duration","notes"]; additionalProperties: false |  |
| `/$defs/phraseTemplate/properties/id` | Yes | $ref: "#/$defs/id" |  |
| `/$defs/phraseTemplate/properties/duration` | Yes | $ref: "#/$defs/positive" |  |
| `/$defs/phraseTemplate/properties/notes` | Yes | type: "array"; items: 1 entries (see descendant pointers) |  |
| `/$defs/phraseTemplate/properties/notes/items` | Context / conditional | $ref: "#/$defs/corePhraseSourceNote" |  |
| `/$defs/phraseTemplate/properties/name` | No | type: "string" |  |
| `/$defs/phraseNoteMapping` | Context / conditional | type: "object"; properties: 3 entries (see descendant pointers); required: ["templateNoteId","repeatIndex","noteId"]; additionalProperties: false |  |
| `/$defs/phraseNoteMapping/properties/templateNoteId` | Yes | $ref: "#/$defs/id" |  |
| `/$defs/phraseNoteMapping/properties/repeatIndex` | Yes | $ref: "#/$defs/nonnegative" |  |
| `/$defs/phraseNoteMapping/properties/noteId` | Yes | $ref: "#/$defs/id" |  |
| `/$defs/phraseInstance` | Context / conditional | type: "object"; properties: 8 entries (see descendant pointers); required: ["id","templateId","clipId","repeatCount","transpose","noteMap"]; additionalProperties: false |  |
| `/$defs/phraseInstance/properties/id` | Yes | $ref: "#/$defs/id" |  |
| `/$defs/phraseInstance/properties/templateId` | Yes | $ref: "#/$defs/id" |  |
| `/$defs/phraseInstance/properties/clipId` | Yes | $ref: "#/$defs/id" |  |
| `/$defs/phraseInstance/properties/repeatCount` | Yes | $ref: "#/$defs/positive" |  |
| `/$defs/phraseInstance/properties/transpose` | Yes | type: "integer"; minimum: -127; maximum: 127 |  |
| `/$defs/phraseInstance/properties/noteMap` | Yes | type: "array"; items: 1 entries (see descendant pointers) |  |
| `/$defs/phraseInstance/properties/noteMap/items` | Context / conditional | $ref: "#/$defs/phraseNoteMapping" |  |
| `/$defs/phraseInstance/properties/velocityMode` | No | enum: ["independent","linked"]; default: "independent" | independent preserves concrete velocities on refresh; linked requires exact presence/value equality with the template. This field does not trigger refresh on load. |
| `/$defs/phraseInstance/properties/noteStateMode` | No | enum: ["independent","linked"]; default: "independent" | Controls enabled/releaseVelocity/probability/velocityDeviation after materialization. independent preserves concrete note-state values on refresh; linked requires exact presence/value equality with the template. pitchRole is structural and must always remain semantically equal between a source pitch note and its mapped concrete note. |
| `/$defs/clipCandidate` | Context / conditional | type: "object"; properties: 3 entries (see descendant pointers); required: ["id","clipIds"]; additionalProperties: false |  |
| `/$defs/clipCandidate/properties/id` | Yes | $ref: "#/$defs/id" |  |
| `/$defs/clipCandidate/properties/clipIds` | Yes | type: "array"; items: 1 entries (see descendant pointers); uniqueItems: true |  |
| `/$defs/clipCandidate/properties/clipIds/items` | Context / conditional | $ref: "#/$defs/id" |  |
| `/$defs/clipCandidate/properties/name` | No | type: "string" |  |
| `/$defs/clipChoiceGroup` | Context / conditional | type: "object"; properties: 4 entries (see descendant pointers); required: ["id","candidates","selectedCandidateId"]; additionalProperties: false |  |
| `/$defs/clipChoiceGroup/properties/id` | Yes | $ref: "#/$defs/id" |  |
| `/$defs/clipChoiceGroup/properties/candidates` | Yes | type: "array"; items: 1 entries (see descendant pointers); minItems: 1 |  |
| `/$defs/clipChoiceGroup/properties/candidates/items` | Context / conditional | $ref: "#/$defs/clipCandidate" |  |
| `/$defs/clipChoiceGroup/properties/selectedCandidateId` | Yes | anyOf: 2 branches (see descendant pointers) |  |
| `/$defs/clipChoiceGroup/properties/selectedCandidateId/anyOf/0` | Context / conditional | $ref: "#/$defs/id" |  |
| `/$defs/clipChoiceGroup/properties/selectedCandidateId/anyOf/1` | Context / conditional | type: "null" |  |
| `/$defs/clipChoiceGroup/properties/name` | No | type: "string" |  |
| `/$defs/midiMapping` | Context / conditional | type: "object"; properties: 2 entries (see descendant pointers); required: ["standard","note"]; additionalProperties: false; allOf: 1 branches (see descendant pointers) |  |
| `/$defs/midiMapping/properties/standard` | Yes | enum: ["gm1","custom"] | gm1=GM Level 1 percussion key 35..81; custom=explicit arbitrary MIDI1 note number. |
| `/$defs/midiMapping/properties/note` | Yes | $ref: "#/$defs/pitch" | MIDI1 note number in 0..127; for gm1 restrict to 35..81. |
| `/$defs/midiMapping/allOf/0` | Context / conditional | if: 2 entries (see descendant pointers); then: 1 entries (see descendant pointers) |  |
| `/$defs/midiMapping/allOf/0/if` | Context / conditional | properties: 1 entries (see descendant pointers); required: ["standard"] |  |
| `/$defs/midiMapping/allOf/0/if/properties/standard` | Yes | const: "gm1" |  |
| `/$defs/midiMapping/allOf/0/then` | Context / conditional | properties: 1 entries (see descendant pointers) |  |
| `/$defs/midiMapping/allOf/0/then/properties/note` | No | type: "integer"; minimum: 35; maximum: 81 |  |
| `/$defs/soundSource` | Context / conditional | type: "object"; properties: 2 entries (see descendant pointers); required: ["kind"]; additionalProperties: false; allOf: 1 branches (see descendant pointers) | Optional informational rendering class or opaque destination hint. In OSTF 4.0, track.midi.busId is the Core logical MIDI routing reference; soundSource does not bind a physical device, plugin state or preset. |
| `/$defs/soundSource/properties/kind` | Yes | enum: ["unassigned","gm1","externalMidi","plugin","hostManaged"] |  |
| `/$defs/soundSource/properties/identifier` | No | type: "string"; minLength: 1 | Opaque informational target identifier (for example a URI or plug-in identifier), not a physical MIDI-port binding or loading command. |
| `/$defs/soundSource/allOf/0` | Context / conditional | if: 2 entries (see descendant pointers); then: 1 entries (see descendant pointers) |  |
| `/$defs/soundSource/allOf/0/if` | Context / conditional | properties: 1 entries (see descendant pointers); required: ["kind"] |  |
| `/$defs/soundSource/allOf/0/if/properties/kind` | Yes | enum: ["gm1","unassigned"] |  |
| `/$defs/soundSource/allOf/0/then` | Context / conditional | not: 1 entries (see descendant pointers) |  |
| `/$defs/soundSource/allOf/0/then/not` | Context / conditional | required: ["identifier"] |  |
| `/$defs/localizedNames` | Context / conditional | type: "object"; minProperties: 1; propertyNames: 2 entries (see descendant pointers); additionalProperties: 2 entries (see descendant pointers) | Optional translations indexed by a conservative BCP 47 language-tag subset. The original name/title remains authoritative and is never rewritten by locale changes. Case-insensitive duplicate tags are forbidden semantically. |
| `/$defs/localizedNames/propertyNames` | Context / conditional | type: "string"; pattern: "^(?:[A-Za-z]{2,3}\|[A-Za-z]{5,8})(?:-[A-Za-z0-9]{2,8})*$" |  |
| `/$defs/localizedNames/additionalProperties` | Context / conditional | type: "string"; minLength: 1 |  |
| `/$defs/drumKit` | Context / conditional | type: "object"; properties: 4 entries (see descendant pointers); required: ["id","name","soundSlotIds"]; additionalProperties: false | Optional named ordered membership of global Sound Slot IDs. Does not define plugin preset, sample loading, choke or a kit-local MIDI remapping. |
| `/$defs/drumKit/properties/id` | Yes | $ref: "#/$defs/id" |  |
| `/$defs/drumKit/properties/name` | Yes | type: "string" |  |
| `/$defs/drumKit/properties/localizedNames` | No | $ref: "#/$defs/localizedNames" |  |
| `/$defs/drumKit/properties/soundSlotIds` | Yes | type: "array"; uniqueItems: true; items: 1 entries (see descendant pointers) | Ordered, unique references to global soundSlots; may be empty. |
| `/$defs/drumKit/properties/soundSlotIds/items` | Context / conditional | $ref: "#/$defs/id" |  |
| `/$defs/voicing` | Context / conditional | type: "object"; additionalProperties: false; properties: 2 entries (see descendant pointers); required: ["pitches"] | Optional informational chord voicing snapshot, not a played Core note collection. Repeated pitches and original array order have meaning for lossless preservation. Per-entry velocity is an optional voicing-preview hint. |
| `/$defs/voicing/properties/pitches` | Yes | type: "array"; minItems: 1; items: 1 entries (see descendant pointers) | Ordered multiset of concrete absolute pitches, 0-127. Duplicates allowed. |
| `/$defs/voicing/properties/pitches/items` | Context / conditional | $ref: "#/$defs/pitch" |  |
| `/$defs/voicing/properties/velocities` | No | type: "array"; minItems: 1; items: 1 entries (see descendant pointers) | Optional positional velocities aligned one-to-one to pitches. Null means unspecified at this index, not 0. Exact equal-length rule is semantic. |
| `/$defs/voicing/properties/velocities/items` | Context / conditional | anyOf: 2 branches (see descendant pointers) |  |
| `/$defs/voicing/properties/velocities/items/anyOf/0` | Context / conditional | type: "integer"; minimum: 1; maximum: 127 |  |
| `/$defs/voicing/properties/velocities/items/anyOf/1` | Context / conditional | type: "null" |  |
| `/$defs/contributor` | Context / conditional | type: "object"; additionalProperties: false; properties: 4 entries (see descendant pointers); required: ["id","name"] | One song-local identity; same contributor can receive multiple credit roles. Unicode source name is authoritative. |
| `/$defs/contributor/properties/id` | Yes | $ref: "#/$defs/id" |  |
| `/$defs/contributor/properties/name` | Yes | type: "string"; minLength: 1 |  |
| `/$defs/contributor/properties/kind` | No | enum: ["person","organization","other"] |  |
| `/$defs/contributor/properties/localizedNames` | No | $ref: "#/$defs/localizedNames" |  |
| `/$defs/credit` | Context / conditional | type: "object"; additionalProperties: false; properties: 4 entries (see descendant pointers); required: ["id","contributorId","role"] | Ordered credit assignment referencing one contributor; role is an open semantic token, not a translated label. |
| `/$defs/credit/properties/id` | Yes | $ref: "#/$defs/id" |  |
| `/$defs/credit/properties/contributorId` | Yes | $ref: "#/$defs/id" |  |
| `/$defs/credit/properties/role` | Yes | type: "string"; pattern: "^[a-z][a-z0-9.-]*$" |  |
| `/$defs/credit/properties/label` | No | type: "string" |  |
| `/$defs/alternateTitle` | Context / conditional | type: "object"; additionalProperties: false; properties: 2 entries (see descendant pointers); required: ["id","title"] | Stable-ID song title alternative; array position and title text do not identify it. |
| `/$defs/alternateTitle/properties/id` | Yes | $ref: "#/$defs/id" |  |
| `/$defs/alternateTitle/properties/title` | Yes | type: "string"; minLength: 1 |  |
| `/$defs/languageMap32` | Context / conditional | type: "object"; minProperties: 1; propertyNames: 2 entries (see descendant pointers); additionalProperties: 1 entries (see descendant pointers) | Open BCP 47 language-tag dictionary. Schema checks loose subtag structure; full BCP 47 well-formedness and case-insensitive uniqueness are semantic requirements. String may be empty if intentionally blank. |
| `/$defs/languageMap32/propertyNames` | Context / conditional | type: "string"; pattern: "^[A-Za-z]{1,8}(?:-[A-Za-z0-9]{1,8})*$" |  |
| `/$defs/languageMap32/additionalProperties` | Context / conditional | type: "string" |  |
| `/$defs/localizationTarget` | Context / conditional | type: "object"; additionalProperties: false; properties: 2 entries (see descendant pointers); required: ["kind"]; allOf: 1 branches (see descendant pointers) | Core target; song is ID-less, all others use global Core ID. No namespace/profile selector. |
| `/$defs/localizationTarget/properties/kind` | Yes | enum: ["song","alternateTitle","contributor","credit","section","track","clip","soundSlot","drumKit","lyricDocument","resource","phraseTemplate","clipCandidate","clipChoiceGroup","roleDefinition","genre","mood","keyChange","scale","midiBus","lyricVoice"] |  |
| `/$defs/localizationTarget/properties/id` | No | $ref: "#/$defs/id" |  |
| `/$defs/localizationTarget/allOf/0` | Context / conditional | if: 2 entries (see descendant pointers); then: 1 entries (see descendant pointers); else: 1 entries (see descendant pointers) |  |
| `/$defs/localizationTarget/allOf/0/if` | Context / conditional | properties: 1 entries (see descendant pointers); required: ["kind"] |  |
| `/$defs/localizationTarget/allOf/0/if/properties/kind` | Yes | const: "song" |  |
| `/$defs/localizationTarget/allOf/0/then` | Context / conditional | not: 1 entries (see descendant pointers) |  |
| `/$defs/localizationTarget/allOf/0/then/not` | Context / conditional | required: ["id"] |  |
| `/$defs/localizationTarget/allOf/0/else` | Context / conditional | required: ["id"] |  |
| `/$defs/localizationEntry` | Context / conditional | type: "object"; additionalProperties: false; properties: 3 entries (see descendant pointers); required: ["target","field","values"] | Independent translations for one stable source field. Original source text remains authoritative as fallback. |
| `/$defs/localizationEntry/properties/target` | Yes | $ref: "#/$defs/localizationTarget" |  |
| `/$defs/localizationEntry/properties/field` | Yes | type: "string"; minLength: 1 | Exact allowed source text field for this target kind (see normative matrix). No arbitrary path or musical value fields. |
| `/$defs/localizationEntry/properties/values` | Yes | $ref: "#/$defs/languageMap32" |  |
| `/$defs/genre` | Context / conditional | type: "object"; properties: 3 entries (see descendant pointers); required: ["id","name"]; additionalProperties: false | One song-local open genre tag. The label is authored Unicode text and not a predefined controlled taxonomy; ID is stable for metadata merges and localization. |
| `/$defs/genre/properties/id` | Yes | $ref: "#/$defs/id" | Stable song-local ID unique among all Core objects. |
| `/$defs/genre/properties/name` | Yes | type: "string"; minLength: 1 | Original Unicode genre label, never normalized or rewritten during import. |
| `/$defs/genre/properties/externalUri` | No | type: "string"; minLength: 1; format: "uri" | Optional external taxonomy URI hint; never authoritative for a local genre label, and never auto-dereferenced. |
| `/$defs/legacy33` | Context / conditional | $defs: 65 entries (see descendant pointers) |  |
| `/$defs/legacy33/$defs/id` | Context / conditional | type: "string"; pattern: "^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$"; not: 1 entries (see descendant pointers) |  |
| `/$defs/legacy33/$defs/id/not` | Context / conditional | pattern: "[\\r\\n\\u2028\\u2029]" |  |
| `/$defs/legacy33/$defs/nonnegative` | Context / conditional | type: "integer"; minimum: 0; maximum: 9007199254740991 |  |
| `/$defs/legacy33/$defs/positive` | Context / conditional | type: "integer"; minimum: 1; maximum: 9007199254740991 |  |
| `/$defs/legacy33/$defs/signed` | Context / conditional | type: "integer"; minimum: -9007199254740991; maximum: 9007199254740991 |  |
| `/$defs/legacy33/$defs/pitch` | Context / conditional | type: "integer"; minimum: 0; maximum: 127 |  |
| `/$defs/legacy33/$defs/ref` | Context / conditional | type: "object"; properties: 2 entries (see descendant pointers); required: ["type","id"]; additionalProperties: false |  |
| `/$defs/legacy33/$defs/ref/properties/type` | Yes | enum: ["section","track","clip","note","chord","scale","soundSlot","drumKit","lyricDocument","lyricPhrase","lyricUnit","lyricAlignment","resource","genre"] |  |
| `/$defs/legacy33/$defs/ref/properties/id` | Yes | $ref: "#/$defs/legacy33/$defs/id" |  |
| `/$defs/legacy33/$defs/range` | Context / conditional | type: "object"; properties: 2 entries (see descendant pointers); required: ["start","duration"]; additionalProperties: false |  |
| `/$defs/legacy33/$defs/range/properties/start` | Yes | $ref: "#/$defs/legacy33/$defs/nonnegative" |  |
| `/$defs/legacy33/$defs/range/properties/duration` | Yes | $ref: "#/$defs/legacy33/$defs/positive" |  |
| `/$defs/legacy33/$defs/spelledPitchClass` | Context / conditional | type: "object"; properties: 2 entries (see descendant pointers); required: ["step","alter"]; additionalProperties: false |  |
| `/$defs/legacy33/$defs/spelledPitchClass/properties/step` | Yes | enum: ["A","B","C","D","E","F","G"] |  |
| `/$defs/legacy33/$defs/spelledPitchClass/properties/alter` | Yes | type: "integer"; minimum: -2; maximum: 2 |  |
| `/$defs/legacy33/$defs/song` | Context / conditional | type: "object"; properties: 8 entries (see descendant pointers); required: ["title"]; additionalProperties: false |  |
| `/$defs/legacy33/$defs/song/properties/title` | Yes | type: "string" |  |
| `/$defs/legacy33/$defs/song/properties/primaryMelodyTrackId` | No | $ref: "#/$defs/legacy33/$defs/id" |  |
| `/$defs/legacy33/$defs/song/properties/localizedTitles` | No | $ref: "#/$defs/legacy33/$defs/localizedNames" | Optional localized song-title alternatives. song.title is the stable fallback. |
| `/$defs/legacy33/$defs/song/properties/subtitle` | No | type: "string" | Optional original-language subtitle. |
| `/$defs/legacy33/$defs/song/properties/description` | No | type: "string" | Optional original-language description, including Unicode and line breaks. |
| `/$defs/legacy33/$defs/song/properties/alternateTitles` | No | type: "array"; items: 1 entries (see descendant pointers) | Additional stable-ID source-language titles. |
| `/$defs/legacy33/$defs/song/properties/alternateTitles/items` | Context / conditional | $ref: "#/$defs/legacy33/$defs/alternateTitle" |  |
| `/$defs/legacy33/$defs/song/properties/credits` | No | type: "array"; items: 1 entries (see descendant pointers) | Ordered credit assignments to contributors. Multiple roles and duplicate contributors permitted. |
| `/$defs/legacy33/$defs/song/properties/credits/items` | Context / conditional | $ref: "#/$defs/legacy33/$defs/credit" |  |
| `/$defs/legacy33/$defs/song/properties/genres` | No | type: "array"; items: 1 entries (see descendant pointers) | Optional open-ended ordered genre tags; zero or more allowed. Order is authored display preference, first item is primary if a primary label is desired, not a generator weight. Absent means unspecified. |
| `/$defs/legacy33/$defs/song/properties/genres/items` | Context / conditional | $ref: "#/$defs/legacy33/$defs/genre" |  |
| `/$defs/legacy33/$defs/section` | Context / conditional | type: "object"; properties: 6 entries (see descendant pointers); required: ["id","name","start","duration"]; additionalProperties: false |  |
| `/$defs/legacy33/$defs/section/properties/id` | Yes | $ref: "#/$defs/legacy33/$defs/id" |  |
| `/$defs/legacy33/$defs/section/properties/name` | Yes | type: "string"; minLength: 1 |  |
| `/$defs/legacy33/$defs/section/properties/start` | Yes | $ref: "#/$defs/legacy33/$defs/nonnegative" |  |
| `/$defs/legacy33/$defs/section/properties/duration` | Yes | $ref: "#/$defs/legacy33/$defs/positive" |  |
| `/$defs/legacy33/$defs/section/properties/role` | No | type: "string" |  |
| `/$defs/legacy33/$defs/section/properties/localizedNames` | No | $ref: "#/$defs/legacy33/$defs/localizedNames" | Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity. |
| `/$defs/legacy33/$defs/tempo` | Context / conditional | type: "object"; properties: 2 entries (see descendant pointers); required: ["at","bpm"]; additionalProperties: false |  |
| `/$defs/legacy33/$defs/tempo/properties/at` | Yes | $ref: "#/$defs/legacy33/$defs/nonnegative" |  |
| `/$defs/legacy33/$defs/tempo/properties/bpm` | Yes | type: "number"; exclusiveMinimum: 0; maximum: 1000 |  |
| `/$defs/legacy33/$defs/meter` | Context / conditional | type: "object"; properties: 3 entries (see descendant pointers); required: ["at","numerator","denominator"]; additionalProperties: false |  |
| `/$defs/legacy33/$defs/meter/properties/at` | Yes | $ref: "#/$defs/legacy33/$defs/nonnegative" |  |
| `/$defs/legacy33/$defs/meter/properties/numerator` | Yes | type: "integer"; minimum: 1; maximum: 64 |  |
| `/$defs/legacy33/$defs/meter/properties/denominator` | Yes | enum: [1,2,4,8,16,32,64]; type: "integer" |  |
| `/$defs/legacy33/$defs/timeline` | Context / conditional | type: "object"; properties: 3 entries (see descendant pointers); required: ["sections","tempoChanges","meterChanges"]; additionalProperties: false |  |
| `/$defs/legacy33/$defs/timeline/properties/sections` | Yes | type: "array"; items: 1 entries (see descendant pointers) |  |
| `/$defs/legacy33/$defs/timeline/properties/sections/items` | Context / conditional | $ref: "#/$defs/legacy33/$defs/section" |  |
| `/$defs/legacy33/$defs/timeline/properties/tempoChanges` | Yes | type: "array"; items: 1 entries (see descendant pointers); minItems: 1 |  |
| `/$defs/legacy33/$defs/timeline/properties/tempoChanges/items` | Context / conditional | $ref: "#/$defs/legacy33/$defs/tempo" |  |
| `/$defs/legacy33/$defs/timeline/properties/meterChanges` | Yes | type: "array"; items: 1 entries (see descendant pointers); minItems: 1 |  |
| `/$defs/legacy33/$defs/timeline/properties/meterChanges/items` | Context / conditional | $ref: "#/$defs/legacy33/$defs/meter" |  |
| `/$defs/legacy33/$defs/chord` | Context / conditional | type: "object"; properties: 8 entries (see descendant pointers); required: ["id","start","duration","label"]; additionalProperties: false; dependentRequired: {"root":["intervals"],"intervals":["root"]} |  |
| `/$defs/legacy33/$defs/chord/properties/id` | Yes | $ref: "#/$defs/legacy33/$defs/id" |  |
| `/$defs/legacy33/$defs/chord/properties/start` | Yes | $ref: "#/$defs/legacy33/$defs/nonnegative" |  |
| `/$defs/legacy33/$defs/chord/properties/duration` | Yes | $ref: "#/$defs/legacy33/$defs/positive" |  |
| `/$defs/legacy33/$defs/chord/properties/label` | Yes | type: "string"; minLength: 1 |  |
| `/$defs/legacy33/$defs/chord/properties/root` | No | $ref: "#/$defs/legacy33/$defs/spelledPitchClass" |  |
| `/$defs/legacy33/$defs/chord/properties/intervals` | No | type: "array"; items: 3 entries (see descendant pointers); minItems: 1; maxItems: 36; uniqueItems: true; contains: 1 entries (see descendant pointers) |  |
| `/$defs/legacy33/$defs/chord/properties/intervals/items` | Context / conditional | type: "integer"; minimum: 0; maximum: 35 |  |
| `/$defs/legacy33/$defs/chord/properties/intervals/contains` | Context / conditional | const: 0 |  |
| `/$defs/legacy33/$defs/chord/properties/bass` | No | $ref: "#/$defs/legacy33/$defs/spelledPitchClass" |  |
| `/$defs/legacy33/$defs/chord/properties/voicing` | No | $ref: "#/$defs/legacy33/$defs/voicing" | Optional pitch snapshot (not an arrangement note sequence). No automatic playback. |
| `/$defs/legacy33/$defs/scale` | Context / conditional | type: "object"; properties: 6 entries (see descendant pointers); required: ["id","start","duration","tonic","intervals"]; additionalProperties: false |  |
| `/$defs/legacy33/$defs/scale/properties/id` | Yes | $ref: "#/$defs/legacy33/$defs/id" |  |
| `/$defs/legacy33/$defs/scale/properties/start` | Yes | $ref: "#/$defs/legacy33/$defs/nonnegative" |  |
| `/$defs/legacy33/$defs/scale/properties/duration` | Yes | $ref: "#/$defs/legacy33/$defs/positive" |  |
| `/$defs/legacy33/$defs/scale/properties/label` | No | type: "string" |  |
| `/$defs/legacy33/$defs/scale/properties/tonic` | Yes | $ref: "#/$defs/legacy33/$defs/spelledPitchClass" |  |
| `/$defs/legacy33/$defs/scale/properties/intervals` | Yes | type: "array"; items: 3 entries (see descendant pointers); minItems: 1; maxItems: 12; uniqueItems: true; contains: 1 entries (see descendant pointers) |  |
| `/$defs/legacy33/$defs/scale/properties/intervals/items` | Context / conditional | type: "integer"; minimum: 0; maximum: 11 |  |
| `/$defs/legacy33/$defs/scale/properties/intervals/contains` | Context / conditional | const: 0 |  |
| `/$defs/legacy33/$defs/harmony` | Context / conditional | type: "object"; properties: 2 entries (see descendant pointers); required: ["chords","scales"]; additionalProperties: false |  |
| `/$defs/legacy33/$defs/harmony/properties/chords` | Yes | type: "array"; items: 1 entries (see descendant pointers) |  |
| `/$defs/legacy33/$defs/harmony/properties/chords/items` | Context / conditional | $ref: "#/$defs/legacy33/$defs/chord" |  |
| `/$defs/legacy33/$defs/harmony/properties/scales` | Yes | type: "array"; items: 1 entries (see descendant pointers) |  |
| `/$defs/legacy33/$defs/harmony/properties/scales/items` | Context / conditional | $ref: "#/$defs/legacy33/$defs/scale" |  |
| `/$defs/legacy33/$defs/instrument` | Context / conditional | type: "object"; properties: 3 entries (see descendant pointers); required: ["name"]; additionalProperties: false |  |
| `/$defs/legacy33/$defs/instrument/properties/name` | Yes | type: "string" |  |
| `/$defs/legacy33/$defs/instrument/properties/family` | No | type: "string" |  |
| `/$defs/legacy33/$defs/instrument/properties/localizedNames` | No | $ref: "#/$defs/legacy33/$defs/localizedNames" | Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity. |
| `/$defs/legacy33/$defs/note` | Context / conditional | type: "object"; properties: 6 entries (see descendant pointers); required: ["id","start","duration"]; additionalProperties: false; oneOf: 2 branches (see descendant pointers) | Concrete Core note; optional velocity is a note-on attribute. Phrase templates use a separate version-frozen sourceNote shape. |
| `/$defs/legacy33/$defs/note/properties/id` | Yes | $ref: "#/$defs/legacy33/$defs/id" |  |
| `/$defs/legacy33/$defs/note/properties/start` | Yes | $ref: "#/$defs/legacy33/$defs/signed" |  |
| `/$defs/legacy33/$defs/note/properties/duration` | Yes | $ref: "#/$defs/legacy33/$defs/positive" | Positive note gate in ticks, not the guaranteed audible duration of a one-shot percussion sample. |
| `/$defs/legacy33/$defs/note/properties/pitch` | No | $ref: "#/$defs/legacy33/$defs/pitch" |  |
| `/$defs/legacy33/$defs/note/properties/soundSlotId` | No | $ref: "#/$defs/legacy33/$defs/id" | Document-local Sound Slot ID. Distinct events and IDs stay distinct even if several slots share a MIDI key; a renderer decides the acoustic timbre. |
| `/$defs/legacy33/$defs/note/properties/velocity` | No | type: "integer"; minimum: 1; maximum: 127 | Optional authored note-on velocity for performed Core notes, 1–127; omit to mean unspecified. It is not a note-off velocity, controller stream, chord tone, or a sound-rendering guarantee. Never insert an inferred default when saving. |
| `/$defs/legacy33/$defs/note/oneOf/0` | Context / conditional | required: ["pitch"]; not: 1 entries (see descendant pointers) |  |
| `/$defs/legacy33/$defs/note/oneOf/0/not` | Context / conditional | required: ["soundSlotId"] |  |
| `/$defs/legacy33/$defs/note/oneOf/1` | Context / conditional | required: ["soundSlotId"]; not: 1 entries (see descendant pointers) |  |
| `/$defs/legacy33/$defs/note/oneOf/1/not` | Context / conditional | required: ["pitch"] |  |
| `/$defs/legacy33/$defs/clip` | Context / conditional | type: "object"; properties: 7 entries (see descendant pointers); required: ["id","start","duration","notes"]; additionalProperties: false |  |
| `/$defs/legacy33/$defs/clip/properties/id` | Yes | $ref: "#/$defs/legacy33/$defs/id" |  |
| `/$defs/legacy33/$defs/clip/properties/name` | No | type: "string" |  |
| `/$defs/legacy33/$defs/clip/properties/start` | Yes | $ref: "#/$defs/legacy33/$defs/nonnegative" |  |
| `/$defs/legacy33/$defs/clip/properties/duration` | Yes | $ref: "#/$defs/legacy33/$defs/positive" |  |
| `/$defs/legacy33/$defs/clip/properties/enabled` | No | type: "boolean"; default: true |  |
| `/$defs/legacy33/$defs/clip/properties/notes` | Yes | type: "array"; items: 1 entries (see descendant pointers) |  |
| `/$defs/legacy33/$defs/clip/properties/notes/items` | Context / conditional | $ref: "#/$defs/legacy33/$defs/note" |  |
| `/$defs/legacy33/$defs/clip/properties/localizedNames` | No | $ref: "#/$defs/legacy33/$defs/localizedNames" | Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity. |
| `/$defs/legacy33/$defs/track` | Context / conditional | type: "object"; properties: 11 entries (see descendant pointers); required: ["id","name","clips"]; additionalProperties: false; allOf: 1 branches (see descendant pointers) |  |
| `/$defs/legacy33/$defs/track/properties/id` | Yes | $ref: "#/$defs/legacy33/$defs/id" |  |
| `/$defs/legacy33/$defs/track/properties/name` | Yes | type: "string" |  |
| `/$defs/legacy33/$defs/track/properties/role` | No | type: "string" |  |
| `/$defs/legacy33/$defs/track/properties/instrument` | No | $ref: "#/$defs/legacy33/$defs/instrument" |  |
| `/$defs/legacy33/$defs/track/properties/enabled` | No | type: "boolean"; default: true |  |
| `/$defs/legacy33/$defs/track/properties/clips` | Yes | type: "array"; items: 1 entries (see descendant pointers) |  |
| `/$defs/legacy33/$defs/track/properties/clips/items` | Context / conditional | $ref: "#/$defs/legacy33/$defs/clip" |  |
| `/$defs/legacy33/$defs/track/properties/trackType` | No | enum: ["melodic","drum","mixed"] | Semantic event-target category; optional; missing/empty-note tracks may be unknown. It is not a DAW track class. |
| `/$defs/legacy33/$defs/track/properties/preferredView` | No | enum: ["auto","pianoRoll","drumGrid"]; default: "auto" | Non-binding presentation preference. Does not change note meaning. |
| `/$defs/legacy33/$defs/track/properties/soundSource` | No | $ref: "#/$defs/legacy33/$defs/soundSource" | Optional sound-source selection hint, not a plug-in state, preset blob, or sound guarantee. |
| `/$defs/legacy33/$defs/track/properties/localizedNames` | No | $ref: "#/$defs/legacy33/$defs/localizedNames" | Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity. |
| `/$defs/legacy33/$defs/track/properties/drumKitId` | No | $ref: "#/$defs/legacy33/$defs/id" | Optional reference to a declared drumKit; only for a drum/mixed or empty inferred track. All stored slot events in the track must belong to the referenced kit. |
| `/$defs/legacy33/$defs/track/allOf/0` | Context / conditional | if: 2 entries (see descendant pointers); then: 1 entries (see descendant pointers) |  |
| `/$defs/legacy33/$defs/track/allOf/0/if` | Context / conditional | properties: 1 entries (see descendant pointers); required: ["trackType"] |  |
| `/$defs/legacy33/$defs/track/allOf/0/if/properties/trackType` | Yes | const: "melodic" |  |
| `/$defs/legacy33/$defs/track/allOf/0/then` | Context / conditional | not: 1 entries (see descendant pointers) |  |
| `/$defs/legacy33/$defs/track/allOf/0/then/not` | Context / conditional | required: ["drumKitId"] |  |
| `/$defs/legacy33/$defs/soundSlot` | Context / conditional | type: "object"; properties: 6 entries (see descendant pointers); required: ["id","name"]; additionalProperties: false | Document-local stable logical percussion target. Equal roles, names or MIDI note mappings never merge distinct slot IDs. No sample/audio identity is encoded. |
| `/$defs/legacy33/$defs/soundSlot/properties/id` | Yes | $ref: "#/$defs/legacy33/$defs/id" |  |
| `/$defs/legacy33/$defs/soundSlot/properties/name` | Yes | type: "string" |  |
| `/$defs/legacy33/$defs/soundSlot/properties/role` | No | type: "string" | Optional free-text musical role; not a standardized GM instrument code or an acoustic sample identifier. |
| `/$defs/legacy33/$defs/soundSlot/properties/midiNote` | No | $ref: "#/$defs/legacy33/$defs/pitch" | Legacy 3.0 MIDI note hint only; not a GM1 declaration or preview timbre identity. |
| `/$defs/legacy33/$defs/soundSlot/properties/midiMapping` | No | $ref: "#/$defs/legacy33/$defs/midiMapping" | Explicit external MIDI1 output mapping; standard=gm1 is separate from custom even for an equal note number. Not a unique slot or audio identity. |
| `/$defs/legacy33/$defs/soundSlot/properties/localizedNames` | No | $ref: "#/$defs/legacy33/$defs/localizedNames" | Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity. |
| `/$defs/legacy33/$defs/lyricDocument` | Context / conditional | type: "object"; properties: 3 entries (see descendant pointers); required: ["id"]; additionalProperties: false |  |
| `/$defs/legacy33/$defs/lyricDocument/properties/id` | Yes | $ref: "#/$defs/legacy33/$defs/id" |  |
| `/$defs/legacy33/$defs/lyricDocument/properties/title` | No | type: "string" |  |
| `/$defs/legacy33/$defs/lyricDocument/properties/language` | No | type: "string" |  |
| `/$defs/legacy33/$defs/lyricPhrase` | Context / conditional | type: "object"; properties: 6 entries (see descendant pointers); required: ["id","documentId","text"]; additionalProperties: false; dependentRequired: {"start":["duration"],"duration":["start"]} |  |
| `/$defs/legacy33/$defs/lyricPhrase/properties/id` | Yes | $ref: "#/$defs/legacy33/$defs/id" |  |
| `/$defs/legacy33/$defs/lyricPhrase/properties/documentId` | Yes | $ref: "#/$defs/legacy33/$defs/id" |  |
| `/$defs/legacy33/$defs/lyricPhrase/properties/text` | Yes | type: "string" |  |
| `/$defs/legacy33/$defs/lyricPhrase/properties/pronunciation` | No | type: "string" |  |
| `/$defs/legacy33/$defs/lyricPhrase/properties/start` | No | $ref: "#/$defs/legacy33/$defs/nonnegative" |  |
| `/$defs/legacy33/$defs/lyricPhrase/properties/duration` | No | $ref: "#/$defs/legacy33/$defs/positive" |  |
| `/$defs/legacy33/$defs/lyricUnit` | Context / conditional | type: "object"; properties: 6 entries (see descendant pointers); required: ["id","phraseId","text"]; additionalProperties: false; dependentRequired: {"start":["duration"],"duration":["start"]} |  |
| `/$defs/legacy33/$defs/lyricUnit/properties/id` | Yes | $ref: "#/$defs/legacy33/$defs/id" |  |
| `/$defs/legacy33/$defs/lyricUnit/properties/phraseId` | Yes | $ref: "#/$defs/legacy33/$defs/id" |  |
| `/$defs/legacy33/$defs/lyricUnit/properties/text` | Yes | type: "string" |  |
| `/$defs/legacy33/$defs/lyricUnit/properties/pronunciation` | No | type: "string" |  |
| `/$defs/legacy33/$defs/lyricUnit/properties/start` | No | $ref: "#/$defs/legacy33/$defs/nonnegative" |  |
| `/$defs/legacy33/$defs/lyricUnit/properties/duration` | No | $ref: "#/$defs/legacy33/$defs/positive" |  |
| `/$defs/legacy33/$defs/lyricAlignment` | Context / conditional | type: "object"; properties: 3 entries (see descendant pointers); required: ["id","unitIds","noteIds"]; additionalProperties: false |  |
| `/$defs/legacy33/$defs/lyricAlignment/properties/id` | Yes | $ref: "#/$defs/legacy33/$defs/id" |  |
| `/$defs/legacy33/$defs/lyricAlignment/properties/unitIds` | Yes | type: "array"; items: 1 entries (see descendant pointers); uniqueItems: true; minItems: 1 |  |
| `/$defs/legacy33/$defs/lyricAlignment/properties/unitIds/items` | Context / conditional | $ref: "#/$defs/legacy33/$defs/id" |  |
| `/$defs/legacy33/$defs/lyricAlignment/properties/noteIds` | Yes | type: "array"; items: 1 entries (see descendant pointers); uniqueItems: true; minItems: 1 |  |
| `/$defs/legacy33/$defs/lyricAlignment/properties/noteIds/items` | Context / conditional | $ref: "#/$defs/legacy33/$defs/id" |  |
| `/$defs/legacy33/$defs/lyrics` | Context / conditional | type: "object"; properties: 4 entries (see descendant pointers); required: ["documents","phrases","units","alignments"]; additionalProperties: false |  |
| `/$defs/legacy33/$defs/lyrics/properties/documents` | Yes | type: "array"; items: 1 entries (see descendant pointers) |  |
| `/$defs/legacy33/$defs/lyrics/properties/documents/items` | Context / conditional | $ref: "#/$defs/legacy33/$defs/lyricDocument" |  |
| `/$defs/legacy33/$defs/lyrics/properties/phrases` | Yes | type: "array"; items: 1 entries (see descendant pointers) |  |
| `/$defs/legacy33/$defs/lyrics/properties/phrases/items` | Context / conditional | $ref: "#/$defs/legacy33/$defs/lyricPhrase" |  |
| `/$defs/legacy33/$defs/lyrics/properties/units` | Yes | type: "array"; items: 1 entries (see descendant pointers) |  |
| `/$defs/legacy33/$defs/lyrics/properties/units/items` | Context / conditional | $ref: "#/$defs/legacy33/$defs/lyricUnit" |  |
| `/$defs/legacy33/$defs/lyrics/properties/alignments` | Yes | type: "array"; items: 1 entries (see descendant pointers) |  |
| `/$defs/legacy33/$defs/lyrics/properties/alignments/items` | Context / conditional | $ref: "#/$defs/legacy33/$defs/lyricAlignment" |  |
| `/$defs/legacy33/$defs/sha256` | Context / conditional | type: "string"; pattern: "^[0-9a-f]{64}$"; not: 1 entries (see descendant pointers) |  |
| `/$defs/legacy33/$defs/sha256/not` | Context / conditional | pattern: "[\\r\\n\\u2028\\u2029]" |  |
| `/$defs/legacy33/$defs/resource` | Context / conditional | type: "object"; properties: 5 entries (see descendant pointers); required: ["id","kind","uri"]; additionalProperties: false |  |
| `/$defs/legacy33/$defs/resource/properties/id` | Yes | $ref: "#/$defs/legacy33/$defs/id" |  |
| `/$defs/legacy33/$defs/resource/properties/kind` | Yes | enum: ["audio","midi","text","other"] |  |
| `/$defs/legacy33/$defs/resource/properties/uri` | Yes | type: "string"; minLength: 1 |  |
| `/$defs/legacy33/$defs/resource/properties/name` | No | type: "string" |  |
| `/$defs/legacy33/$defs/resource/properties/sha256` | No | $ref: "#/$defs/legacy33/$defs/sha256" |  |
| `/$defs/legacy33/$defs/dependencies` | Context / conditional | oneOf: 2 branches (see descendant pointers) |  |
| `/$defs/legacy33/$defs/dependencies/oneOf/0` | Context / conditional | type: "object"; properties: 1 entries (see descendant pointers); required: ["scope"]; additionalProperties: false |  |
| `/$defs/legacy33/$defs/dependencies/oneOf/0/properties/scope` | Yes | enum: ["document","none"] |  |
| `/$defs/legacy33/$defs/dependencies/oneOf/1` | Context / conditional | type: "object"; properties: 2 entries (see descendant pointers); required: ["scope","refs"]; additionalProperties: false |  |
| `/$defs/legacy33/$defs/dependencies/oneOf/1/properties/scope` | Yes | const: "objects" |  |
| `/$defs/legacy33/$defs/dependencies/oneOf/1/properties/refs` | Yes | type: "array"; items: 1 entries (see descendant pointers); minItems: 1; uniqueItems: true |  |
| `/$defs/legacy33/$defs/dependencies/oneOf/1/properties/refs/items` | Context / conditional | $ref: "#/$defs/legacy33/$defs/ref" |  |
| `/$defs/legacy33/$defs/extension` | Context / conditional | type: "object"; properties: 4 entries (see descendant pointers); required: ["version","status","dependencies","data"]; additionalProperties: false |  |
| `/$defs/legacy33/$defs/extension/properties/version` | Yes | type: "string"; minLength: 1 |  |
| `/$defs/legacy33/$defs/extension/properties/status` | Yes | enum: ["current","stale","unverified"] |  |
| `/$defs/legacy33/$defs/extension/properties/dependencies` | Yes | $ref: "#/$defs/legacy33/$defs/dependencies" |  |
| `/$defs/legacy33/$defs/relativeAssignment` | Context / conditional | type: "object"; properties: 6 entries (see descendant pointers); required: ["noteId","basis","contextId","anchorPitch","index","chromaticOffset"]; additionalProperties: false; allOf: 1 branches (see descendant pointers) |  |
| `/$defs/legacy33/$defs/relativeAssignment/properties/noteId` | Yes | $ref: "#/$defs/legacy33/$defs/id" |  |
| `/$defs/legacy33/$defs/relativeAssignment/properties/basis` | Yes | enum: ["chordTone","scaleDegree"] |  |
| `/$defs/legacy33/$defs/relativeAssignment/properties/contextId` | Yes | $ref: "#/$defs/legacy33/$defs/id" |  |
| `/$defs/legacy33/$defs/relativeAssignment/properties/anchorPitch` | Yes | $ref: "#/$defs/legacy33/$defs/pitch" |  |
| `/$defs/legacy33/$defs/relativeAssignment/properties/index` | Yes | type: "integer"; minimum: 1; maximum: 36 |  |
| `/$defs/legacy33/$defs/relativeAssignment/properties/chromaticOffset` | Yes | type: "integer"; minimum: -24; maximum: 24 |  |
| `/$defs/legacy33/$defs/relativeAssignment/allOf/0` | Context / conditional | if: 2 entries (see descendant pointers); then: 1 entries (see descendant pointers) |  |
| `/$defs/legacy33/$defs/relativeAssignment/allOf/0/if` | Context / conditional | properties: 1 entries (see descendant pointers); required: ["basis"] |  |
| `/$defs/legacy33/$defs/relativeAssignment/allOf/0/if/properties/basis` | Yes | const: "scaleDegree" |  |
| `/$defs/legacy33/$defs/relativeAssignment/allOf/0/then` | Context / conditional | properties: 1 entries (see descendant pointers) |  |
| `/$defs/legacy33/$defs/relativeAssignment/allOf/0/then/properties/index` | No | maximum: 12 |  |
| `/$defs/legacy33/$defs/relativeData` | Context / conditional | type: "object"; properties: 1 entries (see descendant pointers); required: ["assignments"]; additionalProperties: false |  |
| `/$defs/legacy33/$defs/relativeData/properties/assignments` | Yes | type: "array"; items: 1 entries (see descendant pointers) |  |
| `/$defs/legacy33/$defs/relativeData/properties/assignments/items` | Context / conditional | $ref: "#/$defs/legacy33/$defs/relativeAssignment" |  |
| `/$defs/legacy33/$defs/generator` | Context / conditional | type: "object"; properties: 2 entries (see descendant pointers); required: ["id","version"]; additionalProperties: false |  |
| `/$defs/legacy33/$defs/generator/properties/id` | Yes | type: "string"; minLength: 1 |  |
| `/$defs/legacy33/$defs/generator/properties/version` | Yes | type: "string"; minLength: 1 |  |
| `/$defs/legacy33/$defs/generationInput` | Context / conditional | type: "object"; properties: 3 entries (see descendant pointers); required: ["role","ref"]; additionalProperties: false |  |
| `/$defs/legacy33/$defs/generationInput/properties/role` | Yes | type: "string"; minLength: 1 |  |
| `/$defs/legacy33/$defs/generationInput/properties/ref` | Yes | $ref: "#/$defs/legacy33/$defs/ref" |  |
| `/$defs/legacy33/$defs/generationInput/properties/readRange` | No | $ref: "#/$defs/legacy33/$defs/range" |  |
| `/$defs/legacy33/$defs/generationProcess` | Context / conditional | type: "object"; properties: 7 entries (see descendant pointers); required: ["id","generator","inputs","outputs","protectedNoteIds"]; additionalProperties: false |  |
| `/$defs/legacy33/$defs/generationProcess/properties/id` | Yes | $ref: "#/$defs/legacy33/$defs/id" |  |
| `/$defs/legacy33/$defs/generationProcess/properties/generator` | Yes | $ref: "#/$defs/legacy33/$defs/generator" |  |
| `/$defs/legacy33/$defs/generationProcess/properties/inputs` | Yes | type: "array"; items: 1 entries (see descendant pointers) |  |
| `/$defs/legacy33/$defs/generationProcess/properties/inputs/items` | Context / conditional | $ref: "#/$defs/legacy33/$defs/generationInput" |  |
| `/$defs/legacy33/$defs/generationProcess/properties/outputs` | Yes | type: "array"; items: 1 entries (see descendant pointers); minItems: 1 |  |
| `/$defs/legacy33/$defs/generationProcess/properties/outputs/items` | Context / conditional | $ref: "#/$defs/legacy33/$defs/ref" |  |
| `/$defs/legacy33/$defs/generationProcess/properties/targetRange` | No | $ref: "#/$defs/legacy33/$defs/range" |  |
| `/$defs/legacy33/$defs/generationProcess/properties/protectedNoteIds` | Yes | type: "array"; items: 1 entries (see descendant pointers); uniqueItems: true |  |
| `/$defs/legacy33/$defs/generationProcess/properties/protectedNoteIds/items` | Context / conditional | $ref: "#/$defs/legacy33/$defs/id" |  |
| `/$defs/legacy33/$defs/generationProcess/properties/vendorExtension` | No | type: "string"; minLength: 1 |  |
| `/$defs/legacy33/$defs/generationData` | Context / conditional | type: "object"; properties: 1 entries (see descendant pointers); required: ["processes"]; additionalProperties: false |  |
| `/$defs/legacy33/$defs/generationData/properties/processes` | Yes | type: "array"; items: 1 entries (see descendant pointers) |  |
| `/$defs/legacy33/$defs/generationData/properties/processes/items` | Context / conditional | $ref: "#/$defs/legacy33/$defs/generationProcess" |  |
| `/$defs/legacy33/$defs/color` | Context / conditional | type: "string"; pattern: "^#[0-9A-Fa-f]{6}$"; not: 1 entries (see descendant pointers) |  |
| `/$defs/legacy33/$defs/color/not` | Context / conditional | pattern: "[\\r\\n\\u2028\\u2029]" |  |
| `/$defs/legacy33/$defs/roleDefinition` | Context / conditional | type: "object"; properties: 3 entries (see descendant pointers); required: ["id","name"]; additionalProperties: false |  |
| `/$defs/legacy33/$defs/roleDefinition/properties/id` | Yes | $ref: "#/$defs/legacy33/$defs/id" |  |
| `/$defs/legacy33/$defs/roleDefinition/properties/name` | Yes | type: "string"; minLength: 1 |  |
| `/$defs/legacy33/$defs/roleDefinition/properties/baseRole` | No | type: "string" |  |
| `/$defs/legacy33/$defs/roleColorMap` | Context / conditional | type: "object"; additionalProperties: 1 entries (see descendant pointers) |  |
| `/$defs/legacy33/$defs/roleColorMap/additionalProperties` | Context / conditional | $ref: "#/$defs/legacy33/$defs/color" |  |
| `/$defs/legacy33/$defs/customRoleColorMap` | Context / conditional | type: "object"; propertyNames: 1 entries (see descendant pointers); additionalProperties: 1 entries (see descendant pointers) |  |
| `/$defs/legacy33/$defs/customRoleColorMap/propertyNames` | Context / conditional | $ref: "#/$defs/legacy33/$defs/id" |  |
| `/$defs/legacy33/$defs/customRoleColorMap/additionalProperties` | Context / conditional | $ref: "#/$defs/legacy33/$defs/color" |  |
| `/$defs/legacy33/$defs/objectColor` | Context / conditional | type: "object"; properties: 2 entries (see descendant pointers); required: ["target","color"]; additionalProperties: false |  |
| `/$defs/legacy33/$defs/objectColor/properties/target` | Yes | $ref: "#/$defs/legacy33/$defs/ref" |  |
| `/$defs/legacy33/$defs/objectColor/properties/color` | Yes | $ref: "#/$defs/legacy33/$defs/color" |  |
| `/$defs/legacy33/$defs/appearanceData` | Context / conditional | type: "object"; properties: 3 entries (see descendant pointers); required: ["roleDefinitions","sectionRoleAssignments","appearance"]; additionalProperties: false |  |
| `/$defs/legacy33/$defs/appearanceData/properties/roleDefinitions` | Yes | type: "array"; items: 1 entries (see descendant pointers) |  |
| `/$defs/legacy33/$defs/appearanceData/properties/roleDefinitions/items` | Context / conditional | $ref: "#/$defs/legacy33/$defs/roleDefinition" |  |
| `/$defs/legacy33/$defs/appearanceData/properties/sectionRoleAssignments` | Yes | type: "object"; propertyNames: 1 entries (see descendant pointers); additionalProperties: 1 entries (see descendant pointers) |  |
| `/$defs/legacy33/$defs/appearanceData/properties/sectionRoleAssignments/propertyNames` | Context / conditional | $ref: "#/$defs/legacy33/$defs/id" |  |
| `/$defs/legacy33/$defs/appearanceData/properties/sectionRoleAssignments/additionalProperties` | Context / conditional | $ref: "#/$defs/legacy33/$defs/id" |  |
| `/$defs/legacy33/$defs/appearanceData/properties/appearance` | Yes | type: "object"; properties: 3 entries (see descendant pointers); required: ["roleColors","customRoleColors","objectColors"]; additionalProperties: false |  |
| `/$defs/legacy33/$defs/appearanceData/properties/appearance/properties/roleColors` | Yes | $ref: "#/$defs/legacy33/$defs/roleColorMap" |  |
| `/$defs/legacy33/$defs/appearanceData/properties/appearance/properties/customRoleColors` | Yes | $ref: "#/$defs/legacy33/$defs/customRoleColorMap" |  |
| `/$defs/legacy33/$defs/appearanceData/properties/appearance/properties/objectColors` | Yes | type: "array"; items: 1 entries (see descendant pointers) |  |
| `/$defs/legacy33/$defs/appearanceData/properties/appearance/properties/objectColors/items` | Context / conditional | $ref: "#/$defs/legacy33/$defs/objectColor" |  |
| `/$defs/legacy33/$defs/legacyData` | Context / conditional | type: "object"; properties: 4 entries (see descendant pointers); required: ["sourceVersion","sourceSha256","sourceText","conversionReport"]; additionalProperties: false |  |
| `/$defs/legacy33/$defs/legacyData/properties/sourceVersion` | Yes | const: "2.3.0" |  |
| `/$defs/legacy33/$defs/legacyData/properties/sourceSha256` | Yes | $ref: "#/$defs/legacy33/$defs/sha256" |  |
| `/$defs/legacy33/$defs/legacyData/properties/sourceText` | Yes | type: "string"; minLength: 1 |  |
| `/$defs/legacy33/$defs/legacyData/properties/conversionReport` | Yes | type: "object" |  |
| `/$defs/legacy33/$defs/extensions` | Context / conditional | type: "object"; propertyNames: 2 entries (see descendant pointers); properties: 7 entries (see descendant pointers); additionalProperties: 1 entries (see descendant pointers) |  |
| `/$defs/legacy33/$defs/extensions/propertyNames` | Context / conditional | pattern: "^[a-z][a-z0-9-]*(?:\\.[a-z][a-z0-9-]*){2,}$"; not: 1 entries (see descendant pointers) |  |
| `/$defs/legacy33/$defs/extensions/propertyNames/not` | Context / conditional | pattern: "[\\r\\n\\u2028\\u2029]" |  |
| `/$defs/legacy33/$defs/extensions/properties/org.ostf.relative-phrase.v1` | No | allOf: 2 branches (see descendant pointers) |  |
| `/$defs/legacy33/$defs/extensions/properties/org.ostf.relative-phrase.v1/allOf/0` | Context / conditional | $ref: "#/$defs/legacy33/$defs/extension" |  |
| `/$defs/legacy33/$defs/extensions/properties/org.ostf.relative-phrase.v1/allOf/1` | Context / conditional | if: 2 entries (see descendant pointers); then: 1 entries (see descendant pointers) |  |
| `/$defs/legacy33/$defs/extensions/properties/org.ostf.relative-phrase.v1/allOf/1/if` | Context / conditional | properties: 1 entries (see descendant pointers); required: ["version"] |  |
| `/$defs/legacy33/$defs/extensions/properties/org.ostf.relative-phrase.v1/allOf/1/if/properties/version` | Yes | const: "1.0.0-draft.1" |  |
| `/$defs/legacy33/$defs/extensions/properties/org.ostf.relative-phrase.v1/allOf/1/then` | Context / conditional | properties: 1 entries (see descendant pointers) |  |
| `/$defs/legacy33/$defs/extensions/properties/org.ostf.relative-phrase.v1/allOf/1/then/properties/data` | No | $ref: "#/$defs/legacy33/$defs/relativeData" |  |
| `/$defs/legacy33/$defs/extensions/properties/org.ostf.generation-context.v1` | No | allOf: 2 branches (see descendant pointers) |  |
| `/$defs/legacy33/$defs/extensions/properties/org.ostf.generation-context.v1/allOf/0` | Context / conditional | $ref: "#/$defs/legacy33/$defs/extension" |  |
| `/$defs/legacy33/$defs/extensions/properties/org.ostf.generation-context.v1/allOf/1` | Context / conditional | if: 2 entries (see descendant pointers); then: 1 entries (see descendant pointers) |  |
| `/$defs/legacy33/$defs/extensions/properties/org.ostf.generation-context.v1/allOf/1/if` | Context / conditional | properties: 1 entries (see descendant pointers); required: ["version"] |  |
| `/$defs/legacy33/$defs/extensions/properties/org.ostf.generation-context.v1/allOf/1/if/properties/version` | Yes | const: "1.0.0-draft.1" |  |
| `/$defs/legacy33/$defs/extensions/properties/org.ostf.generation-context.v1/allOf/1/then` | Context / conditional | properties: 1 entries (see descendant pointers) |  |
| `/$defs/legacy33/$defs/extensions/properties/org.ostf.generation-context.v1/allOf/1/then/properties/data` | No | $ref: "#/$defs/legacy33/$defs/generationData" |  |
| `/$defs/legacy33/$defs/extensions/properties/org.ostf.appearance.v1` | No | allOf: 2 branches (see descendant pointers) |  |
| `/$defs/legacy33/$defs/extensions/properties/org.ostf.appearance.v1/allOf/0` | Context / conditional | $ref: "#/$defs/legacy33/$defs/extension" |  |
| `/$defs/legacy33/$defs/extensions/properties/org.ostf.appearance.v1/allOf/1` | Context / conditional | if: 2 entries (see descendant pointers); then: 1 entries (see descendant pointers) |  |
| `/$defs/legacy33/$defs/extensions/properties/org.ostf.appearance.v1/allOf/1/if` | Context / conditional | properties: 1 entries (see descendant pointers); required: ["version"] |  |
| `/$defs/legacy33/$defs/extensions/properties/org.ostf.appearance.v1/allOf/1/if/properties/version` | Yes | const: "1.0.0-draft.1" |  |
| `/$defs/legacy33/$defs/extensions/properties/org.ostf.appearance.v1/allOf/1/then` | Context / conditional | properties: 1 entries (see descendant pointers) |  |
| `/$defs/legacy33/$defs/extensions/properties/org.ostf.appearance.v1/allOf/1/then/properties/data` | No | $ref: "#/$defs/legacy33/$defs/appearanceData" |  |
| `/$defs/legacy33/$defs/extensions/properties/org.ostf.legacy-import.v1` | No | allOf: 2 branches (see descendant pointers) |  |
| `/$defs/legacy33/$defs/extensions/properties/org.ostf.legacy-import.v1/allOf/0` | Context / conditional | $ref: "#/$defs/legacy33/$defs/extension" |  |
| `/$defs/legacy33/$defs/extensions/properties/org.ostf.legacy-import.v1/allOf/1` | Context / conditional | if: 2 entries (see descendant pointers); then: 1 entries (see descendant pointers) |  |
| `/$defs/legacy33/$defs/extensions/properties/org.ostf.legacy-import.v1/allOf/1/if` | Context / conditional | properties: 1 entries (see descendant pointers); required: ["version"] |  |
| `/$defs/legacy33/$defs/extensions/properties/org.ostf.legacy-import.v1/allOf/1/if/properties/version` | Yes | const: "1.0.0-draft.1" |  |
| `/$defs/legacy33/$defs/extensions/properties/org.ostf.legacy-import.v1/allOf/1/then` | Context / conditional | properties: 1 entries (see descendant pointers) |  |
| `/$defs/legacy33/$defs/extensions/properties/org.ostf.legacy-import.v1/allOf/1/then/properties/data` | No | $ref: "#/$defs/legacy33/$defs/legacyData" |  |
| `/$defs/legacy33/$defs/extensions/properties/org.ostf.phrase-library.v1` | No | allOf: 2 branches (see descendant pointers) |  |
| `/$defs/legacy33/$defs/extensions/properties/org.ostf.phrase-library.v1/allOf/0` | Context / conditional | $ref: "#/$defs/legacy33/$defs/extension" |  |
| `/$defs/legacy33/$defs/extensions/properties/org.ostf.phrase-library.v1/allOf/1` | Context / conditional | if: 2 entries (see descendant pointers); then: 1 entries (see descendant pointers) |  |
| `/$defs/legacy33/$defs/extensions/properties/org.ostf.phrase-library.v1/allOf/1/if` | Context / conditional | properties: 1 entries (see descendant pointers); required: ["version"] |  |
| `/$defs/legacy33/$defs/extensions/properties/org.ostf.phrase-library.v1/allOf/1/if/properties/version` | Yes | const: "1.0.0-draft.1" |  |
| `/$defs/legacy33/$defs/extensions/properties/org.ostf.phrase-library.v1/allOf/1/then` | Context / conditional | properties: 1 entries (see descendant pointers) |  |
| `/$defs/legacy33/$defs/extensions/properties/org.ostf.phrase-library.v1/allOf/1/then/properties/data` | No | $ref: "#/$defs/legacy33/$defs/phraseLibraryData" |  |
| `/$defs/legacy33/$defs/extensions/properties/org.ostf.clip-choices.v1` | No | allOf: 2 branches (see descendant pointers) |  |
| `/$defs/legacy33/$defs/extensions/properties/org.ostf.clip-choices.v1/allOf/0` | Context / conditional | $ref: "#/$defs/legacy33/$defs/extension" |  |
| `/$defs/legacy33/$defs/extensions/properties/org.ostf.clip-choices.v1/allOf/1` | Context / conditional | if: 2 entries (see descendant pointers); then: 1 entries (see descendant pointers) |  |
| `/$defs/legacy33/$defs/extensions/properties/org.ostf.clip-choices.v1/allOf/1/if` | Context / conditional | properties: 1 entries (see descendant pointers); required: ["version"] |  |
| `/$defs/legacy33/$defs/extensions/properties/org.ostf.clip-choices.v1/allOf/1/if/properties/version` | Yes | const: "1.0.0-draft.1" |  |
| `/$defs/legacy33/$defs/extensions/properties/org.ostf.clip-choices.v1/allOf/1/then` | Context / conditional | properties: 1 entries (see descendant pointers) |  |
| `/$defs/legacy33/$defs/extensions/properties/org.ostf.clip-choices.v1/allOf/1/then/properties/data` | No | $ref: "#/$defs/legacy33/$defs/clipChoicesData" |  |
| `/$defs/legacy33/$defs/extensions/properties/org.ostf.localization.v1` | No | allOf: 2 branches (see descendant pointers) |  |
| `/$defs/legacy33/$defs/extensions/properties/org.ostf.localization.v1/allOf/0` | Context / conditional | $ref: "#/$defs/legacy33/$defs/extension" |  |
| `/$defs/legacy33/$defs/extensions/properties/org.ostf.localization.v1/allOf/1` | Context / conditional | if: 2 entries (see descendant pointers); then: 1 entries (see descendant pointers) |  |
| `/$defs/legacy33/$defs/extensions/properties/org.ostf.localization.v1/allOf/1/if` | Context / conditional | properties: 1 entries (see descendant pointers); required: ["version"] |  |
| `/$defs/legacy33/$defs/extensions/properties/org.ostf.localization.v1/allOf/1/if/properties/version` | Yes | const: "1.0.0" |  |
| `/$defs/legacy33/$defs/extensions/properties/org.ostf.localization.v1/allOf/1/then` | Context / conditional | properties: 1 entries (see descendant pointers) |  |
| `/$defs/legacy33/$defs/extensions/properties/org.ostf.localization.v1/allOf/1/then/properties/data` | No | $ref: "#/$defs/legacy33/$defs/localizationData" |  |
| `/$defs/legacy33/$defs/extensions/additionalProperties` | Context / conditional | $ref: "#/$defs/legacy33/$defs/extension" |  |
| `/$defs/legacy33/$defs/phraseTemplate` | Context / conditional | type: "object"; properties: 4 entries (see descendant pointers); required: ["id","duration","notes"]; additionalProperties: false |  |
| `/$defs/legacy33/$defs/phraseTemplate/properties/id` | Yes | $ref: "#/$defs/legacy33/$defs/id" |  |
| `/$defs/legacy33/$defs/phraseTemplate/properties/duration` | Yes | $ref: "#/$defs/legacy33/$defs/positive" |  |
| `/$defs/legacy33/$defs/phraseTemplate/properties/notes` | Yes | type: "array"; items: 1 entries (see descendant pointers) |  |
| `/$defs/legacy33/$defs/phraseTemplate/properties/notes/items` | Context / conditional | $ref: "#/$defs/legacy33/$defs/phraseSourceNote" |  |
| `/$defs/legacy33/$defs/phraseTemplate/properties/name` | No | type: "string" |  |
| `/$defs/legacy33/$defs/phraseNoteMapping` | Context / conditional | type: "object"; properties: 3 entries (see descendant pointers); required: ["templateNoteId","repeatIndex","noteId"]; additionalProperties: false |  |
| `/$defs/legacy33/$defs/phraseNoteMapping/properties/templateNoteId` | Yes | $ref: "#/$defs/legacy33/$defs/id" |  |
| `/$defs/legacy33/$defs/phraseNoteMapping/properties/repeatIndex` | Yes | $ref: "#/$defs/legacy33/$defs/nonnegative" |  |
| `/$defs/legacy33/$defs/phraseNoteMapping/properties/noteId` | Yes | $ref: "#/$defs/legacy33/$defs/id" |  |
| `/$defs/legacy33/$defs/phraseInstance` | Context / conditional | type: "object"; properties: 6 entries (see descendant pointers); required: ["id","templateId","clipId","repeatCount","transpose","noteMap"]; additionalProperties: false |  |
| `/$defs/legacy33/$defs/phraseInstance/properties/id` | Yes | $ref: "#/$defs/legacy33/$defs/id" |  |
| `/$defs/legacy33/$defs/phraseInstance/properties/templateId` | Yes | $ref: "#/$defs/legacy33/$defs/id" |  |
| `/$defs/legacy33/$defs/phraseInstance/properties/clipId` | Yes | $ref: "#/$defs/legacy33/$defs/id" |  |
| `/$defs/legacy33/$defs/phraseInstance/properties/repeatCount` | Yes | $ref: "#/$defs/legacy33/$defs/positive" |  |
| `/$defs/legacy33/$defs/phraseInstance/properties/transpose` | Yes | type: "integer"; minimum: -127; maximum: 127 |  |
| `/$defs/legacy33/$defs/phraseInstance/properties/noteMap` | Yes | type: "array"; items: 1 entries (see descendant pointers) |  |
| `/$defs/legacy33/$defs/phraseInstance/properties/noteMap/items` | Context / conditional | $ref: "#/$defs/legacy33/$defs/phraseNoteMapping" |  |
| `/$defs/legacy33/$defs/phraseLibraryData` | Context / conditional | type: "object"; properties: 2 entries (see descendant pointers); required: ["templates","instances"]; additionalProperties: false |  |
| `/$defs/legacy33/$defs/phraseLibraryData/properties/templates` | Yes | type: "array"; items: 1 entries (see descendant pointers) |  |
| `/$defs/legacy33/$defs/phraseLibraryData/properties/templates/items` | Context / conditional | $ref: "#/$defs/legacy33/$defs/phraseTemplate" |  |
| `/$defs/legacy33/$defs/phraseLibraryData/properties/instances` | Yes | type: "array"; items: 1 entries (see descendant pointers) |  |
| `/$defs/legacy33/$defs/phraseLibraryData/properties/instances/items` | Context / conditional | $ref: "#/$defs/legacy33/$defs/phraseInstance" |  |
| `/$defs/legacy33/$defs/clipCandidate` | Context / conditional | type: "object"; properties: 3 entries (see descendant pointers); required: ["id","clipIds"]; additionalProperties: false |  |
| `/$defs/legacy33/$defs/clipCandidate/properties/id` | Yes | $ref: "#/$defs/legacy33/$defs/id" |  |
| `/$defs/legacy33/$defs/clipCandidate/properties/clipIds` | Yes | type: "array"; items: 1 entries (see descendant pointers); uniqueItems: true |  |
| `/$defs/legacy33/$defs/clipCandidate/properties/clipIds/items` | Context / conditional | $ref: "#/$defs/legacy33/$defs/id" |  |
| `/$defs/legacy33/$defs/clipCandidate/properties/name` | No | type: "string" |  |
| `/$defs/legacy33/$defs/clipChoiceGroup` | Context / conditional | type: "object"; properties: 4 entries (see descendant pointers); required: ["id","candidates","selectedCandidateId"]; additionalProperties: false |  |
| `/$defs/legacy33/$defs/clipChoiceGroup/properties/id` | Yes | $ref: "#/$defs/legacy33/$defs/id" |  |
| `/$defs/legacy33/$defs/clipChoiceGroup/properties/candidates` | Yes | type: "array"; items: 1 entries (see descendant pointers); minItems: 1 |  |
| `/$defs/legacy33/$defs/clipChoiceGroup/properties/candidates/items` | Context / conditional | $ref: "#/$defs/legacy33/$defs/clipCandidate" |  |
| `/$defs/legacy33/$defs/clipChoiceGroup/properties/selectedCandidateId` | Yes | anyOf: 2 branches (see descendant pointers) |  |
| `/$defs/legacy33/$defs/clipChoiceGroup/properties/selectedCandidateId/anyOf/0` | Context / conditional | $ref: "#/$defs/legacy33/$defs/id" |  |
| `/$defs/legacy33/$defs/clipChoiceGroup/properties/selectedCandidateId/anyOf/1` | Context / conditional | type: "null" |  |
| `/$defs/legacy33/$defs/clipChoiceGroup/properties/name` | No | type: "string" |  |
| `/$defs/legacy33/$defs/clipChoicesData` | Context / conditional | type: "object"; properties: 1 entries (see descendant pointers); required: ["groups"]; additionalProperties: false |  |
| `/$defs/legacy33/$defs/clipChoicesData/properties/groups` | Yes | type: "array"; items: 1 entries (see descendant pointers) |  |
| `/$defs/legacy33/$defs/clipChoicesData/properties/groups/items` | Context / conditional | $ref: "#/$defs/legacy33/$defs/clipChoiceGroup" |  |
| `/$defs/legacy33/$defs/midiMapping` | Context / conditional | type: "object"; properties: 2 entries (see descendant pointers); required: ["standard","note"]; additionalProperties: false; allOf: 1 branches (see descendant pointers) |  |
| `/$defs/legacy33/$defs/midiMapping/properties/standard` | Yes | enum: ["gm1","custom"] | gm1=GM Level 1 percussion key 35..81; custom=explicit arbitrary MIDI1 note number. |
| `/$defs/legacy33/$defs/midiMapping/properties/note` | Yes | $ref: "#/$defs/legacy33/$defs/pitch" | MIDI1 note number in 0..127; for gm1 restrict to 35..81. |
| `/$defs/legacy33/$defs/midiMapping/allOf/0` | Context / conditional | if: 2 entries (see descendant pointers); then: 1 entries (see descendant pointers) |  |
| `/$defs/legacy33/$defs/midiMapping/allOf/0/if` | Context / conditional | properties: 1 entries (see descendant pointers); required: ["standard"] |  |
| `/$defs/legacy33/$defs/midiMapping/allOf/0/if/properties/standard` | Yes | const: "gm1" |  |
| `/$defs/legacy33/$defs/midiMapping/allOf/0/then` | Context / conditional | properties: 1 entries (see descendant pointers) |  |
| `/$defs/legacy33/$defs/midiMapping/allOf/0/then/properties/note` | No | type: "integer"; minimum: 35; maximum: 81 |  |
| `/$defs/legacy33/$defs/soundSource` | Context / conditional | type: "object"; properties: 2 entries (see descendant pointers); required: ["kind"]; additionalProperties: false; allOf: 1 branches (see descendant pointers) | Optional informational rendering class or opaque destination hint. Program Change, Bank Select and plugin presets are not standardized by Core. |
| `/$defs/legacy33/$defs/soundSource/properties/kind` | Yes | enum: ["unassigned","gm1","externalMidi","plugin","hostManaged"] |  |
| `/$defs/legacy33/$defs/soundSource/properties/identifier` | No | type: "string"; minLength: 1 | Opaque target identifier, e.g. URI, plug-in identifier or port alias, not a loading command. |
| `/$defs/legacy33/$defs/soundSource/allOf/0` | Context / conditional | if: 2 entries (see descendant pointers); then: 1 entries (see descendant pointers) |  |
| `/$defs/legacy33/$defs/soundSource/allOf/0/if` | Context / conditional | properties: 1 entries (see descendant pointers); required: ["kind"] |  |
| `/$defs/legacy33/$defs/soundSource/allOf/0/if/properties/kind` | Yes | enum: ["gm1","unassigned"] |  |
| `/$defs/legacy33/$defs/soundSource/allOf/0/then` | Context / conditional | not: 1 entries (see descendant pointers) |  |
| `/$defs/legacy33/$defs/soundSource/allOf/0/then/not` | Context / conditional | required: ["identifier"] |  |
| `/$defs/legacy33/$defs/localizedNames` | Context / conditional | type: "object"; minProperties: 1; propertyNames: 2 entries (see descendant pointers); additionalProperties: 2 entries (see descendant pointers) | Optional translations indexed by a conservative BCP 47 language-tag subset. The original name/title remains authoritative and is never rewritten by locale changes. Case-insensitive duplicate tags are forbidden semantically. |
| `/$defs/legacy33/$defs/localizedNames/propertyNames` | Context / conditional | type: "string"; pattern: "^(?:[A-Za-z]{2,3}\|[A-Za-z]{5,8})(?:-[A-Za-z0-9]{2,8})*$" |  |
| `/$defs/legacy33/$defs/localizedNames/additionalProperties` | Context / conditional | type: "string"; minLength: 1 |  |
| `/$defs/legacy33/$defs/drumKit` | Context / conditional | type: "object"; properties: 4 entries (see descendant pointers); required: ["id","name","soundSlotIds"]; additionalProperties: false | Optional named ordered membership of global Sound Slot IDs. Does not define plugin preset, sample loading, choke or a kit-local MIDI remapping. |
| `/$defs/legacy33/$defs/drumKit/properties/id` | Yes | $ref: "#/$defs/legacy33/$defs/id" |  |
| `/$defs/legacy33/$defs/drumKit/properties/name` | Yes | type: "string" |  |
| `/$defs/legacy33/$defs/drumKit/properties/localizedNames` | No | $ref: "#/$defs/legacy33/$defs/localizedNames" |  |
| `/$defs/legacy33/$defs/drumKit/properties/soundSlotIds` | Yes | type: "array"; uniqueItems: true; items: 1 entries (see descendant pointers) | Ordered, unique references to global soundSlots; may be empty. |
| `/$defs/legacy33/$defs/drumKit/properties/soundSlotIds/items` | Context / conditional | $ref: "#/$defs/legacy33/$defs/id" |  |
| `/$defs/legacy33/$defs/phraseSourceNote` | Context / conditional | type: "object"; properties: 5 entries (see descendant pointers); required: ["id","start","duration"]; additionalProperties: false; oneOf: 2 branches (see descendant pointers) | Version-frozen 1.0.0-draft.1 phrase source note. Does NOT admit velocity; a linked Core instance may independently set velocity. |
| `/$defs/legacy33/$defs/phraseSourceNote/properties/id` | Yes | $ref: "#/$defs/legacy33/$defs/id" |  |
| `/$defs/legacy33/$defs/phraseSourceNote/properties/start` | Yes | $ref: "#/$defs/legacy33/$defs/signed" |  |
| `/$defs/legacy33/$defs/phraseSourceNote/properties/duration` | Yes | $ref: "#/$defs/legacy33/$defs/positive" |  |
| `/$defs/legacy33/$defs/phraseSourceNote/properties/pitch` | No | $ref: "#/$defs/legacy33/$defs/pitch" |  |
| `/$defs/legacy33/$defs/phraseSourceNote/properties/soundSlotId` | No | $ref: "#/$defs/legacy33/$defs/id" |  |
| `/$defs/legacy33/$defs/phraseSourceNote/oneOf/0` | Context / conditional | required: ["pitch"]; not: 1 entries (see descendant pointers) |  |
| `/$defs/legacy33/$defs/phraseSourceNote/oneOf/0/not` | Context / conditional | required: ["soundSlotId"] |  |
| `/$defs/legacy33/$defs/phraseSourceNote/oneOf/1` | Context / conditional | required: ["soundSlotId"]; not: 1 entries (see descendant pointers) |  |
| `/$defs/legacy33/$defs/phraseSourceNote/oneOf/1/not` | Context / conditional | required: ["pitch"] |  |
| `/$defs/legacy33/$defs/voicing` | Context / conditional | type: "object"; additionalProperties: false; properties: 2 entries (see descendant pointers); required: ["pitches"] | Optional informational chord voicing snapshot, not a played Core note collection. Repeated pitches and original array order have meaning for lossless preservation. Per-entry velocity is an optional voicing-preview hint. |
| `/$defs/legacy33/$defs/voicing/properties/pitches` | Yes | type: "array"; minItems: 1; items: 1 entries (see descendant pointers) | Ordered multiset of concrete absolute pitches, 0-127. Duplicates allowed. |
| `/$defs/legacy33/$defs/voicing/properties/pitches/items` | Context / conditional | $ref: "#/$defs/legacy33/$defs/pitch" |  |
| `/$defs/legacy33/$defs/voicing/properties/velocities` | No | type: "array"; minItems: 1; items: 1 entries (see descendant pointers) | Optional positional velocities aligned one-to-one to pitches. Null means unspecified at this index, not 0. Exact equal-length rule is semantic. |
| `/$defs/legacy33/$defs/voicing/properties/velocities/items` | Context / conditional | anyOf: 2 branches (see descendant pointers) |  |
| `/$defs/legacy33/$defs/voicing/properties/velocities/items/anyOf/0` | Context / conditional | type: "integer"; minimum: 1; maximum: 127 |  |
| `/$defs/legacy33/$defs/voicing/properties/velocities/items/anyOf/1` | Context / conditional | type: "null" |  |
| `/$defs/legacy33/$defs/contributor` | Context / conditional | type: "object"; additionalProperties: false; properties: 4 entries (see descendant pointers); required: ["id","name"] | One song-local identity; same contributor can receive multiple credit roles. Unicode source name is authoritative. |
| `/$defs/legacy33/$defs/contributor/properties/id` | Yes | $ref: "#/$defs/legacy33/$defs/id" |  |
| `/$defs/legacy33/$defs/contributor/properties/name` | Yes | type: "string"; minLength: 1 |  |
| `/$defs/legacy33/$defs/contributor/properties/kind` | No | enum: ["person","organization","other"] |  |
| `/$defs/legacy33/$defs/contributor/properties/localizedNames` | No | $ref: "#/$defs/legacy33/$defs/localizedNames" |  |
| `/$defs/legacy33/$defs/credit` | Context / conditional | type: "object"; additionalProperties: false; properties: 4 entries (see descendant pointers); required: ["id","contributorId","role"] | Ordered credit assignment referencing one contributor; role is an open semantic token, not a translated label. |
| `/$defs/legacy33/$defs/credit/properties/id` | Yes | $ref: "#/$defs/legacy33/$defs/id" |  |
| `/$defs/legacy33/$defs/credit/properties/contributorId` | Yes | $ref: "#/$defs/legacy33/$defs/id" |  |
| `/$defs/legacy33/$defs/credit/properties/role` | Yes | type: "string"; pattern: "^[a-z][a-z0-9.-]*$" |  |
| `/$defs/legacy33/$defs/credit/properties/label` | No | type: "string" |  |
| `/$defs/legacy33/$defs/alternateTitle` | Context / conditional | type: "object"; additionalProperties: false; properties: 2 entries (see descendant pointers); required: ["id","title"] | Stable-ID song title alternative; array position and title text do not identify it. |
| `/$defs/legacy33/$defs/alternateTitle/properties/id` | Yes | $ref: "#/$defs/legacy33/$defs/id" |  |
| `/$defs/legacy33/$defs/alternateTitle/properties/title` | Yes | type: "string"; minLength: 1 |  |
| `/$defs/legacy33/$defs/languageMap32` | Context / conditional | type: "object"; minProperties: 1; propertyNames: 2 entries (see descendant pointers); additionalProperties: 1 entries (see descendant pointers) | Open BCP 47 language-tag dictionary. Schema checks loose subtag structure; full BCP 47 well-formedness and case-insensitive uniqueness are semantic requirements. String may be empty if intentionally blank. |
| `/$defs/legacy33/$defs/languageMap32/propertyNames` | Context / conditional | type: "string"; pattern: "^[A-Za-z]{1,8}(?:-[A-Za-z0-9]{1,8})*$" |  |
| `/$defs/legacy33/$defs/languageMap32/additionalProperties` | Context / conditional | type: "string" |  |
| `/$defs/legacy33/$defs/localizationTarget` | Context / conditional | type: "object"; additionalProperties: false; properties: 3 entries (see descendant pointers); required: ["kind"]; allOf: 2 branches (see descendant pointers) | Stable target by Core ID or profile-local scoped ID; song is the only ID-less target. No array indexes or mutable names as locators. |
| `/$defs/legacy33/$defs/localizationTarget/properties/kind` | Yes | enum: ["song","alternateTitle","contributor","credit","section","track","clip","soundSlot","drumKit","lyricDocument","resource","phraseTemplate","clipCandidate","clipChoiceGroup","roleDefinition","genre"] |  |
| `/$defs/legacy33/$defs/localizationTarget/properties/id` | No | $ref: "#/$defs/legacy33/$defs/id" |  |
| `/$defs/legacy33/$defs/localizationTarget/properties/profile` | No | type: "string"; enum: ["org.ostf.phrase-library.v1","org.ostf.clip-choices.v1","org.ostf.appearance.v1"] |  |
| `/$defs/legacy33/$defs/localizationTarget/allOf/0` | Context / conditional | if: 2 entries (see descendant pointers); then: 1 entries (see descendant pointers); else: 1 entries (see descendant pointers) |  |
| `/$defs/legacy33/$defs/localizationTarget/allOf/0/if` | Context / conditional | properties: 1 entries (see descendant pointers); required: ["kind"] |  |
| `/$defs/legacy33/$defs/localizationTarget/allOf/0/if/properties/kind` | Yes | const: "song" |  |
| `/$defs/legacy33/$defs/localizationTarget/allOf/0/then` | Context / conditional | not: 1 entries (see descendant pointers) |  |
| `/$defs/legacy33/$defs/localizationTarget/allOf/0/then/not` | Context / conditional | anyOf: 2 branches (see descendant pointers) |  |
| `/$defs/legacy33/$defs/localizationTarget/allOf/0/then/not/anyOf/0` | Context / conditional | required: ["id"] |  |
| `/$defs/legacy33/$defs/localizationTarget/allOf/0/then/not/anyOf/1` | Context / conditional | required: ["profile"] |  |
| `/$defs/legacy33/$defs/localizationTarget/allOf/0/else` | Context / conditional | required: ["id"] |  |
| `/$defs/legacy33/$defs/localizationTarget/allOf/1` | Context / conditional | if: 2 entries (see descendant pointers); then: 1 entries (see descendant pointers); else: 1 entries (see descendant pointers) |  |
| `/$defs/legacy33/$defs/localizationTarget/allOf/1/if` | Context / conditional | properties: 1 entries (see descendant pointers); required: ["kind"] |  |
| `/$defs/legacy33/$defs/localizationTarget/allOf/1/if/properties/kind` | Yes | enum: ["phraseTemplate","clipCandidate","clipChoiceGroup","roleDefinition"] |  |
| `/$defs/legacy33/$defs/localizationTarget/allOf/1/then` | Context / conditional | required: ["profile"] |  |
| `/$defs/legacy33/$defs/localizationTarget/allOf/1/else` | Context / conditional | not: 1 entries (see descendant pointers) |  |
| `/$defs/legacy33/$defs/localizationTarget/allOf/1/else/not` | Context / conditional | required: ["profile"] |  |
| `/$defs/legacy33/$defs/localizationEntry` | Context / conditional | type: "object"; additionalProperties: false; properties: 3 entries (see descendant pointers); required: ["target","field","values"] | Independent translations for one stable source field. Original source text remains authoritative as fallback. |
| `/$defs/legacy33/$defs/localizationEntry/properties/target` | Yes | $ref: "#/$defs/legacy33/$defs/localizationTarget" |  |
| `/$defs/legacy33/$defs/localizationEntry/properties/field` | Yes | type: "string"; minLength: 1 | Exact allowed source text field for this target kind (see normative matrix). No arbitrary path or musical value fields. |
| `/$defs/legacy33/$defs/localizationEntry/properties/values` | Yes | $ref: "#/$defs/legacy33/$defs/languageMap32" |  |
| `/$defs/legacy33/$defs/localizationData` | Context / conditional | type: "object"; additionalProperties: false; properties: 1 entries (see descendant pointers); required: ["entries"] | Language-map translations indexed by stable kind/id/field, never by names or array positions. |
| `/$defs/legacy33/$defs/localizationData/properties/entries` | Yes | type: "array"; items: 1 entries (see descendant pointers) |  |
| `/$defs/legacy33/$defs/localizationData/properties/entries/items` | Context / conditional | $ref: "#/$defs/legacy33/$defs/localizationEntry" |  |
| `/$defs/legacy33/$defs/genre` | Context / conditional | type: "object"; properties: 3 entries (see descendant pointers); required: ["id","name"]; additionalProperties: false | One song-local open genre tag. The label is authored Unicode text and not a predefined controlled taxonomy; ID is stable for metadata merges and localization. |
| `/$defs/legacy33/$defs/genre/properties/id` | Yes | $ref: "#/$defs/legacy33/$defs/id" | Stable song-local ID unique among all Core objects. |
| `/$defs/legacy33/$defs/genre/properties/name` | Yes | type: "string"; minLength: 1 | Original Unicode genre label, never normalized or rewritten during import. |
| `/$defs/legacy33/$defs/genre/properties/externalUri` | No | type: "string"; minLength: 1; format: "uri" | Optional external taxonomy URI hint; never authoritative for a local genre label, and never auto-dereferenced. |
| `/$defs/opaqueDocumentId` | Context / conditional | type: "string"; minLength: 1 | Stable URI or UUID-style identifier for a document lineage. Compared as exact Unicode text; never fetched. |
| `/$defs/revisionRef` | Context / conditional | type: "object"; properties: 3 entries (see descendant pointers); required: ["documentId","revisionId"]; additionalProperties: false |  |
| `/$defs/revisionRef/properties/documentId` | Yes | $ref: "#/$defs/opaqueDocumentId" |  |
| `/$defs/revisionRef/properties/revisionId` | Yes | $ref: "#/$defs/opaqueDocumentId" |  |
| `/$defs/revisionRef/properties/sha256` | No | $ref: "#/$defs/sha256" |  |
| `/$defs/software` | Context / conditional | type: "object"; properties: 2 entries (see descendant pointers); required: ["name"]; additionalProperties: false |  |
| `/$defs/software/properties/name` | Yes | type: "string"; minLength: 1 |  |
| `/$defs/software/properties/version` | No | type: "string"; minLength: 1 |  |
| `/$defs/documentInfo` | Context / conditional | type: "object"; properties: 5 entries (see descendant pointers); required: ["id","revisionId"]; additionalProperties: false |  |
| `/$defs/documentInfo/properties/id` | Yes | $ref: "#/$defs/opaqueDocumentId" |  |
| `/$defs/documentInfo/properties/revisionId` | Yes | $ref: "#/$defs/opaqueDocumentId" |  |
| `/$defs/documentInfo/properties/parents` | No | type: "array"; items: 1 entries (see descendant pointers); uniqueItems: true |  |
| `/$defs/documentInfo/properties/parents/items` | Context / conditional | $ref: "#/$defs/revisionRef" |  |
| `/$defs/documentInfo/properties/createdBy` | No | $ref: "#/$defs/software" |  |
| `/$defs/documentInfo/properties/modifiedBy` | No | $ref: "#/$defs/software" |  |
| `/$defs/key` | Context / conditional | type: "object"; properties: 4 entries (see descendant pointers); required: ["state"]; additionalProperties: false; allOf: 1 branches (see descendant pointers) |  |
| `/$defs/key/properties/state` | Yes | enum: ["tonal","atonal","unspecified"] |  |
| `/$defs/key/properties/tonic` | No | $ref: "#/$defs/spelledPitchClass" |  |
| `/$defs/key/properties/mode` | No | type: "string"; minLength: 1 | Authored mode identifier. Canonical recognized values include major, minor, dorian, phrygian, lydian, mixolydian, locrian. Unknown values are preserved, never converted to major/minor. |
| `/$defs/key/properties/label` | No | type: "string" |  |
| `/$defs/key/allOf/0` | Context / conditional | if: 2 entries (see descendant pointers); then: 1 entries (see descendant pointers); else: 1 entries (see descendant pointers) |  |
| `/$defs/key/allOf/0/if` | Context / conditional | properties: 1 entries (see descendant pointers); required: ["state"] |  |
| `/$defs/key/allOf/0/if/properties/state` | Yes | const: "tonal" |  |
| `/$defs/key/allOf/0/then` | Context / conditional | required: ["tonic","mode"] |  |
| `/$defs/key/allOf/0/else` | Context / conditional | not: 1 entries (see descendant pointers) |  |
| `/$defs/key/allOf/0/else/not` | Context / conditional | anyOf: 2 branches (see descendant pointers) |  |
| `/$defs/key/allOf/0/else/not/anyOf/0` | Context / conditional | required: ["tonic"] |  |
| `/$defs/key/allOf/0/else/not/anyOf/1` | Context / conditional | required: ["mode"] |  |
| `/$defs/keyChange` | Context / conditional | type: "object"; properties: 4 entries (see descendant pointers); required: ["id","at","key"]; additionalProperties: false | A change after tick zero; initial key is stored only at song.key. Change at tick 0 is forbidden to prevent dual authority. |
| `/$defs/keyChange/properties/id` | Yes | $ref: "#/$defs/id" |  |
| `/$defs/keyChange/properties/at` | Yes | $ref: "#/$defs/positive" |  |
| `/$defs/keyChange/properties/key` | Yes | $ref: "#/$defs/key" |  |
| `/$defs/keyChange/properties/label` | No | type: "string" |  |
| `/$defs/scaleDefinition` | Context / conditional | type: "object"; properties: 4 entries (see descendant pointers); required: ["id","tonic","intervals"]; additionalProperties: false |  |
| `/$defs/scaleDefinition/properties/id` | Yes | $ref: "#/$defs/id" |  |
| `/$defs/scaleDefinition/properties/tonic` | Yes | $ref: "#/$defs/spelledPitchClass" |  |
| `/$defs/scaleDefinition/properties/intervals` | Yes | type: "array"; items: 3 entries (see descendant pointers); minItems: 1; maxItems: 12; uniqueItems: true; contains: 1 entries (see descendant pointers) |  |
| `/$defs/scaleDefinition/properties/intervals/items` | Context / conditional | type: "integer"; minimum: 0; maximum: 11 |  |
| `/$defs/scaleDefinition/properties/intervals/contains` | Context / conditional | const: 0 |  |
| `/$defs/scaleDefinition/properties/label` | No | type: "string" |  |
| `/$defs/scaleTarget` | Context / conditional | type: "object"; properties: 2 entries (see descendant pointers); required: ["type","id"]; additionalProperties: false |  |
| `/$defs/scaleTarget/properties/type` | Yes | enum: ["section","track","clip","chord","note"] |  |
| `/$defs/scaleTarget/properties/id` | Yes | $ref: "#/$defs/id" |  |
| `/$defs/mood` | Context / conditional | type: "object"; properties: 3 entries (see descendant pointers); required: ["id","name"]; additionalProperties: false | Authored descriptive mood tag; not a generator preset or a probability. |
| `/$defs/mood/properties/id` | Yes | $ref: "#/$defs/id" | Stable song-local ID unique among all Core objects. |
| `/$defs/mood/properties/name` | Yes | type: "string"; minLength: 1 | Original Unicode genre label, never normalized or rewritten during import. |
| `/$defs/mood/properties/externalUri` | No | type: "string"; minLength: 1; format: "uri" | Optional external vocabulary URI hint; never authoritative for the authored mood name and never auto-dereferenced. |
| `/$defs/rightsStatement` | Context / conditional | type: "object"; properties: 3 entries (see descendant pointers); required: []; additionalProperties: false; minProperties: 1 | Authored rights statement only; no rights or permissions are inferred or granted by the format. |
| `/$defs/rightsStatement/properties/notice` | No | type: "string" |  |
| `/$defs/rightsStatement/properties/licenseUri` | No | type: "string"; minLength: 1 |  |
| `/$defs/rightsStatement/properties/rightsHolderIds` | No | type: "array"; items: 1 entries (see descendant pointers); uniqueItems: true |  |
| `/$defs/rightsStatement/properties/rightsHolderIds/items` | Context / conditional | $ref: "#/$defs/id" |  |
| `/$defs/grooveIntent` | Context / conditional | type: "object"; properties: 4 entries (see descendant pointers); required: []; additionalProperties: false; minProperties: 1; dependentRequired: {"unitTicks":["longWeight","shortWeight"],"longWeight":["unitTicks","shortWeight"],"shortWeight":["unitTicks","longWeight"]} | Descriptive generation intent only. Never re-apply to already stored notes. unitTicks is one unswung subdivision; two subdivisions form a pair. |
| `/$defs/grooveIntent/properties/name` | No | type: "string" |  |
| `/$defs/grooveIntent/properties/unitTicks` | No | $ref: "#/$defs/positive" |  |
| `/$defs/grooveIntent/properties/longWeight` | No | type: "integer"; minimum: 1; maximum: 1000000 |  |
| `/$defs/grooveIntent/properties/shortWeight` | No | type: "integer"; minimum: 1; maximum: 1000000 |  |
| `/$defs/generationIntent` | Context / conditional | type: "object"; properties: 5 entries (see descendant pointers); required: []; additionalProperties: false | Portable description of intent, not a promise to reproduce an algorithm. Does not change song.genres or song.moods. |
| `/$defs/generationIntent/properties/genreNames` | No | type: "array"; items: 2 entries (see descendant pointers) |  |
| `/$defs/generationIntent/properties/genreNames/items` | Context / conditional | type: "string"; minLength: 1 |  |
| `/$defs/generationIntent/properties/moodNames` | No | type: "array"; items: 2 entries (see descendant pointers) |  |
| `/$defs/generationIntent/properties/moodNames/items` | Context / conditional | type: "string"; minLength: 1 |  |
| `/$defs/generationIntent/properties/groove` | No | $ref: "#/$defs/grooveIntent" |  |
| `/$defs/generationIntent/properties/prompt` | No | type: "string" |  |
| `/$defs/generationIntent/properties/seed` | No | type: "string" |  |
| `/$defs/relativePhrases` | Context / conditional | type: "object"; properties: 3 entries (see descendant pointers); required: ["status","dependencies","assignments"]; additionalProperties: false | Standard optional Core object under root version 4.0.0, not an extension. Current relationships must be consistent with saved Core; loading never performs editing or generation. |
| `/$defs/relativePhrases/properties/status` | Yes | enum: ["current","stale","unverified"] |  |
| `/$defs/relativePhrases/properties/dependencies` | Yes | $ref: "#/$defs/dependencies" |  |
| `/$defs/relativePhrases/properties/assignments` | Yes | type: "array"; items: 1 entries (see descendant pointers) |  |
| `/$defs/relativePhrases/properties/assignments/items` | Context / conditional | $ref: "#/$defs/relativeAssignment" |  |
| `/$defs/generation` | Context / conditional | type: "object"; properties: 3 entries (see descendant pointers); required: ["status","dependencies","processes"]; additionalProperties: false | Standard optional Core object under root version 4.0.0, not an extension. Current relationships must be consistent with saved Core; loading never performs editing or generation. |
| `/$defs/generation/properties/status` | Yes | enum: ["current","stale","unverified"] |  |
| `/$defs/generation/properties/dependencies` | Yes | $ref: "#/$defs/dependencies" |  |
| `/$defs/generation/properties/processes` | Yes | type: "array"; items: 1 entries (see descendant pointers) |  |
| `/$defs/generation/properties/processes/items` | Context / conditional | $ref: "#/$defs/generationProcess" |  |
| `/$defs/presentation` | Context / conditional | type: "object"; properties: 5 entries (see descendant pointers); required: ["status","dependencies","roleDefinitions","sectionRoleAssignments","appearance"]; additionalProperties: false | Standard optional Core object under root version 4.0.0, not an extension. Current relationships must be consistent with saved Core; loading never performs editing or generation. |
| `/$defs/presentation/properties/status` | Yes | enum: ["current","stale","unverified"] |  |
| `/$defs/presentation/properties/dependencies` | Yes | $ref: "#/$defs/dependencies" |  |
| `/$defs/presentation/properties/roleDefinitions` | Yes | type: "array"; items: 1 entries (see descendant pointers) |  |
| `/$defs/presentation/properties/roleDefinitions/items` | Context / conditional | $ref: "#/$defs/roleDefinition" |  |
| `/$defs/presentation/properties/sectionRoleAssignments` | Yes | type: "object"; propertyNames: 1 entries (see descendant pointers); additionalProperties: 1 entries (see descendant pointers) |  |
| `/$defs/presentation/properties/sectionRoleAssignments/propertyNames` | Context / conditional | $ref: "#/$defs/id" |  |
| `/$defs/presentation/properties/sectionRoleAssignments/additionalProperties` | Context / conditional | $ref: "#/$defs/id" |  |
| `/$defs/presentation/properties/appearance` | Yes | type: "object"; properties: 3 entries (see descendant pointers); required: ["roleColors","customRoleColors","objectColors"]; additionalProperties: false |  |
| `/$defs/presentation/properties/appearance/properties/roleColors` | Yes | $ref: "#/$defs/roleColorMap" |  |
| `/$defs/presentation/properties/appearance/properties/customRoleColors` | Yes | $ref: "#/$defs/customRoleColorMap" |  |
| `/$defs/presentation/properties/appearance/properties/objectColors` | Yes | type: "array"; items: 1 entries (see descendant pointers) |  |
| `/$defs/presentation/properties/appearance/properties/objectColors/items` | Context / conditional | $ref: "#/$defs/objectColor" |  |
| `/$defs/phraseLibrary` | Context / conditional | type: "object"; properties: 4 entries (see descendant pointers); required: ["status","dependencies","templates","instances"]; additionalProperties: false | Standard optional Core object under root version 4.0.0, not an extension. Current relationships must be consistent with saved Core; loading never performs editing or generation. |
| `/$defs/phraseLibrary/properties/status` | Yes | enum: ["current","stale","unverified"] |  |
| `/$defs/phraseLibrary/properties/dependencies` | Yes | $ref: "#/$defs/dependencies" |  |
| `/$defs/phraseLibrary/properties/templates` | Yes | type: "array"; items: 1 entries (see descendant pointers) |  |
| `/$defs/phraseLibrary/properties/templates/items` | Context / conditional | $ref: "#/$defs/phraseTemplate" |  |
| `/$defs/phraseLibrary/properties/instances` | Yes | type: "array"; items: 1 entries (see descendant pointers) |  |
| `/$defs/phraseLibrary/properties/instances/items` | Context / conditional | $ref: "#/$defs/phraseInstance" |  |
| `/$defs/clipChoices` | Context / conditional | type: "object"; properties: 3 entries (see descendant pointers); required: ["status","dependencies","groups"]; additionalProperties: false | Standard optional Core object under root version 4.0.0, not an extension. Current relationships must be consistent with saved Core; loading never performs editing or generation. |
| `/$defs/clipChoices/properties/status` | Yes | enum: ["current","stale","unverified"] |  |
| `/$defs/clipChoices/properties/dependencies` | Yes | $ref: "#/$defs/dependencies" |  |
| `/$defs/clipChoices/properties/groups` | Yes | type: "array"; items: 1 entries (see descendant pointers) |  |
| `/$defs/clipChoices/properties/groups/items` | Context / conditional | $ref: "#/$defs/clipChoiceGroup" |  |
| `/$defs/localization` | Context / conditional | type: "object"; additionalProperties: false; properties: 3 entries (see descendant pointers); required: ["status","dependencies","entries"] | Standard optional Core object under root version 4.0.0, not an extension. Current relationships must be consistent with saved Core; loading never performs editing or generation. |
| `/$defs/localization/properties/status` | Yes | enum: ["current","stale","unverified"] |  |
| `/$defs/localization/properties/dependencies` | Yes | $ref: "#/$defs/dependencies" |  |
| `/$defs/localization/properties/entries` | Yes | type: "array"; items: 1 entries (see descendant pointers) |  |
| `/$defs/localization/properties/entries/items` | Context / conditional | $ref: "#/$defs/localizationEntry" |  |
| `/$defs/corePhraseSourceNote` | Context / conditional | type: "object"; properties: 11 entries (see descendant pointers); required: ["id","start","duration"]; additionalProperties: false; oneOf: 2 branches (see descendant pointers); dependentRequired: {"velocityDeviation":["velocity"]}; allOf: 1 branches (see descendant pointers) | Template-local source note for phrase materialization. It carries the same note-local 3.5 properties as concrete notes. It is not performed by itself; concrete track notes remain the saved playback events. |
| `/$defs/corePhraseSourceNote/properties/id` | Yes | $ref: "#/$defs/id" |  |
| `/$defs/corePhraseSourceNote/properties/start` | Yes | $ref: "#/$defs/signed" |  |
| `/$defs/corePhraseSourceNote/properties/duration` | Yes | $ref: "#/$defs/positive" | Positive note gate in ticks, not the guaranteed audible duration of a one-shot percussion sample. |
| `/$defs/corePhraseSourceNote/properties/pitch` | No | $ref: "#/$defs/pitch" |  |
| `/$defs/corePhraseSourceNote/properties/soundSlotId` | No | $ref: "#/$defs/id" | Document-local Sound Slot ID. Distinct events and IDs stay distinct even if several slots share a MIDI key; a renderer decides the acoustic timbre. |
| `/$defs/corePhraseSourceNote/properties/velocity` | No | type: "integer"; minimum: 1; maximum: 127 | Optional template note-on velocity, 1–127. Applied only by an explicit materialization/update according to instance.velocityMode; never a performed event by itself. |
| `/$defs/corePhraseSourceNote/properties/enabled` | No | type: "boolean"; default: true | Optional note-local enable state. Omitted means enabled. False preserves the note but suppresses scheduling/playback; it is distinct from probability=0. |
| `/$defs/corePhraseSourceNote/properties/releaseVelocity` | No | type: "integer"; minimum: 0; maximum: 127 | Optional MIDI Note Off/release velocity, 0-127. Omit when unspecified; readers must not invent and write back a default. |
| `/$defs/corePhraseSourceNote/properties/probability` | No | type: "number"; minimum: 0; maximum: 1; default: 1 | Optional note-playback probability from 0.0 to 1.0. Omitted means 1.0. Random sequence identity is not standardized; materialize notes for deterministic interchange. |
| `/$defs/corePhraseSourceNote/properties/velocityDeviation` | No | type: "integer"; minimum: -126; maximum: 126; default: 0 | Optional note-local velocity variation endpoint relative to velocity. Requires velocity. Semantic rule: velocity + velocityDeviation must remain within 1..127. Omitted means 0. |
| `/$defs/corePhraseSourceNote/properties/pitchRole` | No | enum: ["musical","fixedTrigger"]; default: "musical" | Meaning of a pitch note. musical participates in pitch/harmony/transpose operations; fixedTrigger is an exact MIDI key trigger (for example a keyswitch) and is never transposed or used as musical-pitch evidence. Allowed only on pitch notes. |
| `/$defs/corePhraseSourceNote/oneOf/0` | Context / conditional | required: ["pitch"]; not: 1 entries (see descendant pointers) |  |
| `/$defs/corePhraseSourceNote/oneOf/0/not` | Context / conditional | required: ["soundSlotId"] |  |
| `/$defs/corePhraseSourceNote/oneOf/1` | Context / conditional | required: ["soundSlotId"]; not: 1 entries (see descendant pointers) |  |
| `/$defs/corePhraseSourceNote/oneOf/1/not` | Context / conditional | required: ["pitch"] |  |
| `/$defs/corePhraseSourceNote/allOf/0` | Context / conditional | if: 1 entries (see descendant pointers); then: 1 entries (see descendant pointers) |  |
| `/$defs/corePhraseSourceNote/allOf/0/if` | Context / conditional | required: ["soundSlotId"] |  |
| `/$defs/corePhraseSourceNote/allOf/0/then` | Context / conditional | not: 1 entries (see descendant pointers) |  |
| `/$defs/corePhraseSourceNote/allOf/0/then/not` | Context / conditional | required: ["pitchRole"] |  |
| `/$defs/provenanceSource` | Context / conditional | type: "object"; properties: 7 entries (see descendant pointers); required: []; additionalProperties: false; minProperties: 1; dependentRequired: {"revisionId":["documentId"]} | Historical source; hashes refer to exact source bytes, not the current document. No automatic retrieval. |
| `/$defs/provenanceSource/properties/format` | No | type: "string"; minLength: 1 |  |
| `/$defs/provenanceSource/properties/version` | No | type: "string"; minLength: 1 |  |
| `/$defs/provenanceSource/properties/sha256` | No | $ref: "#/$defs/sha256" |  |
| `/$defs/provenanceSource/properties/uri` | No | type: "string"; minLength: 1 |  |
| `/$defs/provenanceSource/properties/documentId` | No | $ref: "#/$defs/opaqueDocumentId" |  |
| `/$defs/provenanceSource/properties/revisionId` | No | $ref: "#/$defs/opaqueDocumentId" |  |
| `/$defs/provenanceSource/properties/resourceId` | No | $ref: "#/$defs/id" |  |
| `/$defs/provenanceRecord` | Context / conditional | type: "object"; properties: 8 entries (see descendant pointers); required: ["id","action"]; additionalProperties: false; allOf: 1 branches (see descendant pointers) |  |
| `/$defs/provenanceRecord/properties/id` | Yes | $ref: "#/$defs/id" |  |
| `/$defs/provenanceRecord/properties/action` | Yes | enum: ["create","import","conversion","edit","transpose","merge","generation","other"] |  |
| `/$defs/provenanceRecord/properties/description` | No | type: "string" |  |
| `/$defs/provenanceRecord/properties/tool` | No | $ref: "#/$defs/software" |  |
| `/$defs/provenanceRecord/properties/sources` | No | type: "array"; items: 1 entries (see descendant pointers) |  |
| `/$defs/provenanceRecord/properties/sources/items` | Context / conditional | $ref: "#/$defs/provenanceSource" |  |
| `/$defs/provenanceRecord/properties/semitones` | No | type: "integer"; minimum: -127; maximum: 127 |  |
| `/$defs/provenanceRecord/properties/beforeKey` | No | $ref: "#/$defs/key" |  |
| `/$defs/provenanceRecord/properties/afterKey` | No | $ref: "#/$defs/key" |  |
| `/$defs/provenanceRecord/allOf/0` | Context / conditional | if: 1 entries (see descendant pointers); then: 1 entries (see descendant pointers) |  |
| `/$defs/provenanceRecord/allOf/0/if` | Context / conditional | not: 2 entries (see descendant pointers) |  |
| `/$defs/provenanceRecord/allOf/0/if/not` | Context / conditional | properties: 1 entries (see descendant pointers); required: ["action"] |  |
| `/$defs/provenanceRecord/allOf/0/if/not/properties/action` | Yes | const: "transpose" |  |
| `/$defs/provenanceRecord/allOf/0/then` | Context / conditional | not: 1 entries (see descendant pointers) |  |
| `/$defs/provenanceRecord/allOf/0/then/not` | Context / conditional | required: ["semitones"] |  |
| `/$defs/provenance` | Context / conditional | type: "object"; properties: 1 entries (see descendant pointers); required: ["records"]; additionalProperties: false | Non-executable historical assertions; not composer credits and not a substitute for current metadata. Does not prove authorship or operation correctness. |
| `/$defs/provenance/properties/records` | Yes | type: "array"; items: 1 entries (see descendant pointers) |  |
| `/$defs/provenance/properties/records/items` | Context / conditional | $ref: "#/$defs/provenanceRecord" |  |
| `/$defs/midiChannel` | Context / conditional | type: "integer"; minimum: 1; maximum: 16 | Human-readable MIDI 1.0 channel number 1..16. Wire status-nibble channel = value - 1. |
| `/$defs/midiBus` | Context / conditional | type: "object"; properties: 2 entries (see descendant pointers); required: ["id","name"]; additionalProperties: false | Document-local logical MIDI destination. Each bus has its own MIDI channel namespace. It is not a physical OS/USB/DAW port binding. |
| `/$defs/midiBus/properties/id` | Yes | $ref: "#/$defs/id" |  |
| `/$defs/midiBus/properties/name` | Yes | type: "string" |  |
| `/$defs/midi` | Context / conditional | type: "object"; properties: 1 entries (see descendant pointers); required: ["buses"]; additionalProperties: false |  |
| `/$defs/midi/properties/buses` | Yes | type: "array"; items: 1 entries (see descendant pointers) |  |
| `/$defs/midi/properties/buses/items` | Context / conditional | $ref: "#/$defs/midiBus" |  |
| `/$defs/mpeSettings` | Context / conditional | type: "object"; properties: 2 entries (see descendant pointers); required: ["zone","memberChannelCount"]; additionalProperties: false | Semantic MPE zone declaration. Lower-zone master is channel 1 and upper-zone master is channel 16; member channels are derived contiguously from memberChannelCount. |
| `/$defs/mpeSettings/properties/zone` | Yes | enum: ["lower","upper"] |  |
| `/$defs/mpeSettings/properties/memberChannelCount` | Yes | type: "integer"; minimum: 1; maximum: 15 |  |
| `/$defs/trackMidi` | Context / conditional | type: "object"; properties: 4 entries (see descendant pointers); required: ["mode"]; additionalProperties: false; allOf: 3 branches (see descendant pointers) | Optional MIDI channel/routing interpretation for a track. busId is a logical OSTF bus, never a physical MIDI port. |
| `/$defs/trackMidi/properties/busId` | No | $ref: "#/$defs/id" |  |
| `/$defs/trackMidi/properties/mode` | Yes | enum: ["singleChannel","multiChannel","mpe"] |  |
| `/$defs/trackMidi/properties/channel` | No | $ref: "#/$defs/midiChannel" |  |
| `/$defs/trackMidi/properties/mpe` | No | $ref: "#/$defs/mpeSettings" |  |
| `/$defs/trackMidi/allOf/0` | Context / conditional | if: 2 entries (see descendant pointers); then: 2 entries (see descendant pointers) |  |
| `/$defs/trackMidi/allOf/0/if` | Context / conditional | properties: 1 entries (see descendant pointers); required: ["mode"] |  |
| `/$defs/trackMidi/allOf/0/if/properties/mode` | Yes | const: "singleChannel" |  |
| `/$defs/trackMidi/allOf/0/then` | Context / conditional | required: ["channel"]; not: 1 entries (see descendant pointers) |  |
| `/$defs/trackMidi/allOf/0/then/not` | Context / conditional | required: ["mpe"] |  |
| `/$defs/trackMidi/allOf/1` | Context / conditional | if: 2 entries (see descendant pointers); then: 1 entries (see descendant pointers) |  |
| `/$defs/trackMidi/allOf/1/if` | Context / conditional | properties: 1 entries (see descendant pointers); required: ["mode"] |  |
| `/$defs/trackMidi/allOf/1/if/properties/mode` | Yes | const: "multiChannel" |  |
| `/$defs/trackMidi/allOf/1/then` | Context / conditional | not: 1 entries (see descendant pointers) |  |
| `/$defs/trackMidi/allOf/1/then/not` | Context / conditional | anyOf: 2 branches (see descendant pointers) |  |
| `/$defs/trackMidi/allOf/1/then/not/anyOf/0` | Context / conditional | required: ["channel"] |  |
| `/$defs/trackMidi/allOf/1/then/not/anyOf/1` | Context / conditional | required: ["mpe"] |  |
| `/$defs/trackMidi/allOf/2` | Context / conditional | if: 2 entries (see descendant pointers); then: 2 entries (see descendant pointers) |  |
| `/$defs/trackMidi/allOf/2/if` | Context / conditional | properties: 1 entries (see descendant pointers); required: ["mode"] |  |
| `/$defs/trackMidi/allOf/2/if/properties/mode` | Yes | const: "mpe" |  |
| `/$defs/trackMidi/allOf/2/then` | Context / conditional | required: ["mpe"]; not: 1 entries (see descendant pointers) |  |
| `/$defs/trackMidi/allOf/2/then/not` | Context / conditional | required: ["channel"] |  |
| `/$defs/controlChangeEvent` | Context / conditional | type: "object"; properties: 8 entries (see descendant pointers); required: ["id","start","type","controller","value"]; additionalProperties: false | MIDI 1.0 Control Change. Controllers 120..127 use channelMode instead. |
| `/$defs/controlChangeEvent/properties/id` | Yes | $ref: "#/$defs/id" |  |
| `/$defs/controlChangeEvent/properties/start` | Yes | $ref: "#/$defs/signed" |  |
| `/$defs/controlChangeEvent/properties/order` | No | $ref: "#/$defs/signed"; default: 1 | Same-tick ordering key. Omitted means 1. Note Off has implicit order 0 and Note On implicit order 2; ties are resolved by the normative ordering rules. |
| `/$defs/controlChangeEvent/properties/channel` | No | $ref: "#/$defs/midiChannel" |  |
| `/$defs/controlChangeEvent/properties/type` | Yes | const: "controlChange" |  |
| `/$defs/controlChangeEvent/properties/targetNoteId` | No | $ref: "#/$defs/id" | Optional semantic association with an existing concrete note. It does not replace channel/pitch wire semantics. |
| `/$defs/controlChangeEvent/properties/controller` | Yes | type: "integer"; minimum: 0; maximum: 119 |  |
| `/$defs/controlChangeEvent/properties/value` | Yes | type: "integer"; minimum: 0; maximum: 127 |  |
| `/$defs/channelModeEvent` | Context / conditional | type: "object"; properties: 7 entries (see descendant pointers); required: ["id","start","type","controller","value"]; additionalProperties: false | MIDI 1.0 Channel Mode message represented separately from ordinary Control Change. |
| `/$defs/channelModeEvent/properties/id` | Yes | $ref: "#/$defs/id" |  |
| `/$defs/channelModeEvent/properties/start` | Yes | $ref: "#/$defs/signed" |  |
| `/$defs/channelModeEvent/properties/order` | No | $ref: "#/$defs/signed"; default: 1 | Same-tick ordering key. Omitted means 1. Note Off has implicit order 0 and Note On implicit order 2; ties are resolved by the normative ordering rules. |
| `/$defs/channelModeEvent/properties/channel` | No | $ref: "#/$defs/midiChannel" |  |
| `/$defs/channelModeEvent/properties/type` | Yes | const: "channelMode" |  |
| `/$defs/channelModeEvent/properties/controller` | Yes | type: "integer"; minimum: 120; maximum: 127 |  |
| `/$defs/channelModeEvent/properties/value` | Yes | type: "integer"; minimum: 0; maximum: 127 |  |
| `/$defs/programChangeEvent` | Context / conditional | type: "object"; properties: 6 entries (see descendant pointers); required: ["id","start","type","program"]; additionalProperties: false | MIDI 1.0 Program Change using the wire data value 0..127. UI may display 1..128. |
| `/$defs/programChangeEvent/properties/id` | Yes | $ref: "#/$defs/id" |  |
| `/$defs/programChangeEvent/properties/start` | Yes | $ref: "#/$defs/signed" |  |
| `/$defs/programChangeEvent/properties/order` | No | $ref: "#/$defs/signed"; default: 1 | Same-tick ordering key. Omitted means 1. Note Off has implicit order 0 and Note On implicit order 2; ties are resolved by the normative ordering rules. |
| `/$defs/programChangeEvent/properties/channel` | No | $ref: "#/$defs/midiChannel" |  |
| `/$defs/programChangeEvent/properties/type` | Yes | const: "programChange" |  |
| `/$defs/programChangeEvent/properties/program` | Yes | type: "integer"; minimum: 0; maximum: 127 |  |
| `/$defs/pitchBendEvent` | Context / conditional | type: "object"; properties: 7 entries (see descendant pointers); required: ["id","start","type","value14"]; additionalProperties: false | MIDI 1.0 14-bit Pitch Bend Change. Bend range is receiver state/RPN data, not encoded in value14. |
| `/$defs/pitchBendEvent/properties/id` | Yes | $ref: "#/$defs/id" |  |
| `/$defs/pitchBendEvent/properties/start` | Yes | $ref: "#/$defs/signed" |  |
| `/$defs/pitchBendEvent/properties/order` | No | $ref: "#/$defs/signed"; default: 1 | Same-tick ordering key. Omitted means 1. Note Off has implicit order 0 and Note On implicit order 2; ties are resolved by the normative ordering rules. |
| `/$defs/pitchBendEvent/properties/channel` | No | $ref: "#/$defs/midiChannel" |  |
| `/$defs/pitchBendEvent/properties/type` | Yes | const: "pitchBend" |  |
| `/$defs/pitchBendEvent/properties/targetNoteId` | No | $ref: "#/$defs/id" | Optional semantic association with an existing concrete note. It does not replace channel/pitch wire semantics. |
| `/$defs/pitchBendEvent/properties/value14` | Yes | type: "integer"; minimum: 0; maximum: 16383 | Raw MIDI 1.0 14-bit pitch-bend value; center is 8192. |
| `/$defs/channelPressureEvent` | Context / conditional | type: "object"; properties: 7 entries (see descendant pointers); required: ["id","start","type","value"]; additionalProperties: false | MIDI 1.0 Channel Pressure (channel aftertouch). |
| `/$defs/channelPressureEvent/properties/id` | Yes | $ref: "#/$defs/id" |  |
| `/$defs/channelPressureEvent/properties/start` | Yes | $ref: "#/$defs/signed" |  |
| `/$defs/channelPressureEvent/properties/order` | No | $ref: "#/$defs/signed"; default: 1 | Same-tick ordering key. Omitted means 1. Note Off has implicit order 0 and Note On implicit order 2; ties are resolved by the normative ordering rules. |
| `/$defs/channelPressureEvent/properties/channel` | No | $ref: "#/$defs/midiChannel" |  |
| `/$defs/channelPressureEvent/properties/type` | Yes | const: "channelPressure" |  |
| `/$defs/channelPressureEvent/properties/targetNoteId` | No | $ref: "#/$defs/id" | Optional semantic association with an existing concrete note. It does not replace channel/pitch wire semantics. |
| `/$defs/channelPressureEvent/properties/value` | Yes | type: "integer"; minimum: 0; maximum: 127 |  |
| `/$defs/polyPressureEvent` | Context / conditional | type: "object"; properties: 8 entries (see descendant pointers); required: ["id","start","type","pitch","value"]; additionalProperties: false | MIDI 1.0 Polyphonic Key Pressure (poly aftertouch). |
| `/$defs/polyPressureEvent/properties/id` | Yes | $ref: "#/$defs/id" |  |
| `/$defs/polyPressureEvent/properties/start` | Yes | $ref: "#/$defs/signed" |  |
| `/$defs/polyPressureEvent/properties/order` | No | $ref: "#/$defs/signed"; default: 1 | Same-tick ordering key. Omitted means 1. Note Off has implicit order 0 and Note On implicit order 2; ties are resolved by the normative ordering rules. |
| `/$defs/polyPressureEvent/properties/channel` | No | $ref: "#/$defs/midiChannel" |  |
| `/$defs/polyPressureEvent/properties/type` | Yes | const: "polyPressure" |  |
| `/$defs/polyPressureEvent/properties/targetNoteId` | No | $ref: "#/$defs/id" | Optional semantic association with an existing concrete note. It does not replace channel/pitch wire semantics. |
| `/$defs/polyPressureEvent/properties/pitch` | Yes | $ref: "#/$defs/pitch" |  |
| `/$defs/polyPressureEvent/properties/value` | Yes | type: "integer"; minimum: 0; maximum: 127 |  |
| `/$defs/midiEvent` | Context / conditional | oneOf: 6 branches (see descendant pointers) |  |
| `/$defs/midiEvent/oneOf/0` | Context / conditional | $ref: "#/$defs/controlChangeEvent" |  |
| `/$defs/midiEvent/oneOf/1` | Context / conditional | $ref: "#/$defs/channelModeEvent" |  |
| `/$defs/midiEvent/oneOf/2` | Context / conditional | $ref: "#/$defs/programChangeEvent" |  |
| `/$defs/midiEvent/oneOf/3` | Context / conditional | $ref: "#/$defs/pitchBendEvent" |  |
| `/$defs/midiEvent/oneOf/4` | Context / conditional | $ref: "#/$defs/channelPressureEvent" |  |
| `/$defs/midiEvent/oneOf/5` | Context / conditional | $ref: "#/$defs/polyPressureEvent" |  |
| `/$defs/lyricVoice` | Context / conditional | type: "object"; properties: 6 entries (see descendant pointers); required: ["id","trackId","documentId"]; additionalProperties: false | Explicit relationship between a vocal/melody track and a lyric document. Several voices may reference the same lyric document without duplicating text. |
| `/$defs/lyricVoice/properties/id` | Yes | $ref: "#/$defs/id" |  |
| `/$defs/lyricVoice/properties/name` | No | type: "string" |  |
| `/$defs/lyricVoice/properties/role` | No | type: "string"; minLength: 1 | Open authored role. Recommended values include lead, harmony, backing, unison, double, counter, adlib, response. |
| `/$defs/lyricVoice/properties/trackId` | Yes | $ref: "#/$defs/id" |  |
| `/$defs/lyricVoice/properties/documentId` | Yes | $ref: "#/$defs/id" |  |
| `/$defs/lyricVoice/properties/vocalProfile` | No | $ref: "#/$defs/vocalProfile" | Optional engine-neutral vocal defaults; absence does not mean an instrument voice. |
| `/$defs/playablePitchRange` | Context / conditional | type: "object"; properties: 2 entries (see descendant pointers); required: ["lowPitch","highPitch"]; additionalProperties: false | Authored playable pitch capability in the same 0..127 pitch-number domain as melodic notes. Semantic rule: lowPitch <= highPitch. |
| `/$defs/playablePitchRange/properties/lowPitch` | Yes | $ref: "#/$defs/pitch" |  |
| `/$defs/playablePitchRange/properties/highPitch` | Yes | $ref: "#/$defs/pitch" |  |
| `/$defs/directionPitchCollection` | Context / conditional | type: "object"; properties: 3 entries (see descendant pointers); required: ["tonic","intervals"]; additionalProperties: false | Direction-local pitch-class collection relative to tonic. It is not a harmonic scale-context object and has no independent timeline identity. |
| `/$defs/directionPitchCollection/properties/tonic` | Yes | $ref: "#/$defs/spelledPitchClass" |  |
| `/$defs/directionPitchCollection/properties/intervals` | Yes | type: "array"; items: 3 entries (see descendant pointers); minItems: 1; maxItems: 12; uniqueItems: true; contains: 1 entries (see descendant pointers) |  |
| `/$defs/directionPitchCollection/properties/intervals/items` | Context / conditional | type: "integer"; minimum: 0; maximum: 11 |  |
| `/$defs/directionPitchCollection/properties/intervals/contains` | Context / conditional | const: 0 |  |
| `/$defs/directionPitchCollection/properties/label` | No | type: "string" |  |
| `/$defs/directionPitchSource` | Context / conditional | oneOf: 4 branches (see descendant pointers) | Source of pitch vocabulary for an improvisation Direction. |
| `/$defs/directionPitchSource/oneOf/0` | Context / conditional | type: "object"; properties: 1 entries (see descendant pointers); required: ["type"]; additionalProperties: false |  |
| `/$defs/directionPitchSource/oneOf/0/properties/type` | Yes | const: "effectiveKeyScale" |  |
| `/$defs/directionPitchSource/oneOf/1` | Context / conditional | type: "object"; properties: 1 entries (see descendant pointers); required: ["type"]; additionalProperties: false |  |
| `/$defs/directionPitchSource/oneOf/1/properties/type` | Yes | const: "songScale" |  |
| `/$defs/directionPitchSource/oneOf/2` | Context / conditional | type: "object"; properties: 2 entries (see descendant pointers); required: ["type","scaleIds"]; additionalProperties: false |  |
| `/$defs/directionPitchSource/oneOf/2/properties/type` | Yes | const: "harmonyScales" |  |
| `/$defs/directionPitchSource/oneOf/2/properties/scaleIds` | Yes | type: "array"; items: 1 entries (see descendant pointers); minItems: 1; uniqueItems: true |  |
| `/$defs/directionPitchSource/oneOf/2/properties/scaleIds/items` | Context / conditional | $ref: "#/$defs/id" |  |
| `/$defs/directionPitchSource/oneOf/3` | Context / conditional | type: "object"; properties: 2 entries (see descendant pointers); required: ["type","scale"]; additionalProperties: false |  |
| `/$defs/directionPitchSource/oneOf/3/properties/type` | Yes | const: "explicitScale" |  |
| `/$defs/directionPitchSource/oneOf/3/properties/scale` | Yes | $ref: "#/$defs/directionPitchCollection" |  |
| `/$defs/improvisationDirectionParameters` | Context / conditional | type: "object"; properties: 2 entries (see descendant pointers); required: ["pitchSource","adherence"]; additionalProperties: false |  |
| `/$defs/improvisationDirectionParameters/properties/pitchSource` | Yes | $ref: "#/$defs/directionPitchSource" |  |
| `/$defs/improvisationDirectionParameters/properties/adherence` | Yes | enum: ["strict","preferred"] |  |
| `/$defs/playingRoleDirectionParameters` | Context / conditional | type: "object"; properties: 1 entries (see descendant pointers); required: ["role"]; additionalProperties: false |  |
| `/$defs/playingRoleDirectionParameters/properties/role` | Yes | type: "string"; minLength: 1 |  |
| `/$defs/pitchRangeDirectionParameters` | Context / conditional | type: "object"; properties: 3 entries (see descendant pointers); required: ["lowPitch","highPitch","constraint"]; additionalProperties: false |  |
| `/$defs/pitchRangeDirectionParameters/properties/lowPitch` | Yes | $ref: "#/$defs/pitch" |  |
| `/$defs/pitchRangeDirectionParameters/properties/highPitch` | Yes | $ref: "#/$defs/pitch" |  |
| `/$defs/pitchRangeDirectionParameters/properties/constraint` | Yes | enum: ["strict","preferred"] |  |
| `/$defs/vendorDirectionParameters` | Context / conditional | type: "object"; properties: 4 entries (see descendant pointers); required: ["namespace","name","data"]; additionalProperties: false |  |
| `/$defs/vendorDirectionParameters/properties/namespace` | Yes | type: "string"; minLength: 3; pattern: "^[a-z][a-z0-9-]*(?:\\.[a-z][a-z0-9-]*){2,}$"; not: 1 entries (see descendant pointers) |  |
| `/$defs/vendorDirectionParameters/properties/namespace/not` | Context / conditional | pattern: "^org\\.ostf(?:\\.\|$)" |  |
| `/$defs/vendorDirectionParameters/properties/name` | Yes | type: "string"; minLength: 1 |  |
| `/$defs/vendorDirectionParameters/properties/version` | No | type: "string"; minLength: 1 |  |
| `/$defs/vendorDirectionParameters/properties/data` | Yes | type: "object" |  |
| `/$defs/improvisationDirection` | Context / conditional | type: "object"; properties: 7 entries (see descendant pointers); required: ["id","start","duration","type","parameters"]; additionalProperties: false |  |
| `/$defs/improvisationDirection/properties/id` | Yes | $ref: "#/$defs/id" |  |
| `/$defs/improvisationDirection/properties/start` | Yes | $ref: "#/$defs/nonnegative" |  |
| `/$defs/improvisationDirection/properties/duration` | Yes | $ref: "#/$defs/positive" |  |
| `/$defs/improvisationDirection/properties/label` | No | type: "string" |  |
| `/$defs/improvisationDirection/properties/instruction` | No | type: "string" | Supplemental human/AI-readable semantic instruction. Structured Core parameters remain authoritative. |
| `/$defs/improvisationDirection/properties/type` | Yes | const: "improvisation" |  |
| `/$defs/improvisationDirection/properties/parameters` | Yes | $ref: "#/$defs/improvisationDirectionParameters" |  |
| `/$defs/playingRoleDirection` | Context / conditional | type: "object"; properties: 7 entries (see descendant pointers); required: ["id","start","duration","type","parameters"]; additionalProperties: false |  |
| `/$defs/playingRoleDirection/properties/id` | Yes | $ref: "#/$defs/id" |  |
| `/$defs/playingRoleDirection/properties/start` | Yes | $ref: "#/$defs/nonnegative" |  |
| `/$defs/playingRoleDirection/properties/duration` | Yes | $ref: "#/$defs/positive" |  |
| `/$defs/playingRoleDirection/properties/label` | No | type: "string" |  |
| `/$defs/playingRoleDirection/properties/instruction` | No | type: "string" | Supplemental human/AI-readable semantic instruction. Structured Core parameters remain authoritative. |
| `/$defs/playingRoleDirection/properties/type` | Yes | const: "playingRole" |  |
| `/$defs/playingRoleDirection/properties/parameters` | Yes | $ref: "#/$defs/playingRoleDirectionParameters" |  |
| `/$defs/pitchRangeDirection` | Context / conditional | type: "object"; properties: 7 entries (see descendant pointers); required: ["id","start","duration","type","parameters"]; additionalProperties: false |  |
| `/$defs/pitchRangeDirection/properties/id` | Yes | $ref: "#/$defs/id" |  |
| `/$defs/pitchRangeDirection/properties/start` | Yes | $ref: "#/$defs/nonnegative" |  |
| `/$defs/pitchRangeDirection/properties/duration` | Yes | $ref: "#/$defs/positive" |  |
| `/$defs/pitchRangeDirection/properties/label` | No | type: "string" |  |
| `/$defs/pitchRangeDirection/properties/instruction` | No | type: "string" | Supplemental human/AI-readable semantic instruction. Structured Core parameters remain authoritative. |
| `/$defs/pitchRangeDirection/properties/type` | Yes | const: "pitchRange" |  |
| `/$defs/pitchRangeDirection/properties/parameters` | Yes | $ref: "#/$defs/pitchRangeDirectionParameters" |  |
| `/$defs/vendorRangeDirection` | Context / conditional | type: "object"; properties: 7 entries (see descendant pointers); required: ["id","start","duration","type","parameters"]; additionalProperties: false |  |
| `/$defs/vendorRangeDirection/properties/id` | Yes | $ref: "#/$defs/id" |  |
| `/$defs/vendorRangeDirection/properties/start` | Yes | $ref: "#/$defs/nonnegative" |  |
| `/$defs/vendorRangeDirection/properties/duration` | Yes | $ref: "#/$defs/positive" |  |
| `/$defs/vendorRangeDirection/properties/label` | No | type: "string" |  |
| `/$defs/vendorRangeDirection/properties/instruction` | No | type: "string" | Supplemental human/AI-readable semantic instruction. Structured Core parameters remain authoritative. |
| `/$defs/vendorRangeDirection/properties/type` | Yes | const: "vendor" |  |
| `/$defs/vendorRangeDirection/properties/parameters` | Yes | $ref: "#/$defs/vendorDirectionParameters" |  |
| `/$defs/vendorPointDirection` | Context / conditional | type: "object"; properties: 6 entries (see descendant pointers); required: ["id","at","type","parameters"]; additionalProperties: false |  |
| `/$defs/vendorPointDirection/properties/id` | Yes | $ref: "#/$defs/id" |  |
| `/$defs/vendorPointDirection/properties/at` | Yes | $ref: "#/$defs/nonnegative" |  |
| `/$defs/vendorPointDirection/properties/type` | Yes | const: "vendor" |  |
| `/$defs/vendorPointDirection/properties/parameters` | Yes | $ref: "#/$defs/vendorDirectionParameters" |  |
| `/$defs/vendorPointDirection/properties/label` | No | type: "string" |  |
| `/$defs/vendorPointDirection/properties/instruction` | No | type: "string" | Supplemental human/AI-readable semantic instruction. Structured/vendor parameters remain authoritative. |
| `/$defs/trackDirection` | Context / conditional | oneOf: 7 branches (see descendant pointers) | Typed semantic instruction owned by a track and positioned on the OSTF global timebase. |
| `/$defs/trackDirection/oneOf/0` | Context / conditional | $ref: "#/$defs/improvisationDirection" |  |
| `/$defs/trackDirection/oneOf/1` | Context / conditional | $ref: "#/$defs/playingRoleDirection" |  |
| `/$defs/trackDirection/oneOf/2` | Context / conditional | $ref: "#/$defs/pitchRangeDirection" |  |
| `/$defs/trackDirection/oneOf/3` | Context / conditional | $ref: "#/$defs/vendorRangeDirection" |  |
| `/$defs/trackDirection/oneOf/4` | Context / conditional | $ref: "#/$defs/vendorPointDirection" |  |
| `/$defs/trackDirection/oneOf/5` | Context / conditional | $ref: "#/$defs/phrasingDirection" |  |
| `/$defs/trackDirection/oneOf/6` | Context / conditional | $ref: "#/$defs/vocalFreedomDirection" |  |
| `/$defs/vocalPhonetics` | Context / conditional | type: "object"; properties: 5 entries (see descendant pointers); required: ["alphabet","symbols"]; additionalProperties: false; allOf: 1 branches (see descendant pointers) | Ordered phoneme symbols for a lyric unit, not an absolute pronunciation engine command. |
| `/$defs/vocalPhonetics/properties/alphabet` | Yes | enum: ["ipa","xsampa","arpabet","other"] |  |
| `/$defs/vocalPhonetics/properties/language` | No | type: "string"; minLength: 1 |  |
| `/$defs/vocalPhonetics/properties/symbols` | Yes | type: "array"; minItems: 1; items: 2 entries (see descendant pointers) |  |
| `/$defs/vocalPhonetics/properties/symbols/items` | Context / conditional | type: "string"; minLength: 1 |  |
| `/$defs/vocalPhonetics/properties/namespace` | No | type: "string"; minLength: 1 |  |
| `/$defs/vocalPhonetics/properties/preferred` | No | type: "boolean" | Optional preference only within the same (alphabet, language) set for this lyricUnit. At most one preferred variant per key; absent does not imply false or a guaranteed conversion. |
| `/$defs/vocalPhonetics/allOf/0` | Context / conditional | if: 2 entries (see descendant pointers); then: 1 entries (see descendant pointers) |  |
| `/$defs/vocalPhonetics/allOf/0/if` | Context / conditional | properties: 1 entries (see descendant pointers); required: ["alphabet"] |  |
| `/$defs/vocalPhonetics/allOf/0/if/properties/alphabet` | Yes | const: "other" |  |
| `/$defs/vocalPhonetics/allOf/0/then` | Context / conditional | required: ["namespace"] |  |
| `/$defs/vocalProfile` | Context / conditional | type: "object"; properties: 3 entries (see descendant pointers); additionalProperties: false | Voice default independent of commercial singer preset or license. |
| `/$defs/vocalProfile/properties/language` | No | type: "string"; minLength: 1 |  |
| `/$defs/vocalProfile/properties/deliveryMode` | No | enum: ["sing","rap","speak","hum"] |  |
| `/$defs/vocalProfile/properties/voiceDescription` | No | type: "string"; minLength: 1 |  |
| `/$defs/vocalPerformance` | Context / conditional | type: "object"; properties: 8 entries (see descendant pointers); required: ["id","voiceId"]; additionalProperties: false | Performance belonging to exactly one lyric voice within a containing clip. |
| `/$defs/vocalPerformance/properties/id` | Yes | $ref: "#/$defs/id" |  |
| `/$defs/vocalPerformance/properties/voiceId` | Yes | $ref: "#/$defs/id" |  |
| `/$defs/vocalPerformance/properties/phonemeEvents` | No | type: "array"; items: 1 entries (see descendant pointers) |  |
| `/$defs/vocalPerformance/properties/phonemeEvents/items` | Context / conditional | $ref: "#/$defs/vocalPhonemeEvent" |  |
| `/$defs/vocalPerformance/properties/pitchCurves` | No | type: "array"; items: 1 entries (see descendant pointers) |  |
| `/$defs/vocalPerformance/properties/pitchCurves/items` | Context / conditional | $ref: "#/$defs/vocalPitchCurve" |  |
| `/$defs/vocalPerformance/properties/expressionCurves` | No | type: "array"; items: 1 entries (see descendant pointers) |  |
| `/$defs/vocalPerformance/properties/expressionCurves/items` | Context / conditional | $ref: "#/$defs/vocalExpressionCurve" |  |
| `/$defs/vocalPerformance/properties/techniques` | No | type: "array"; items: 1 entries (see descendant pointers) |  |
| `/$defs/vocalPerformance/properties/techniques/items` | Context / conditional | $ref: "#/$defs/vocalTechnique" |  |
| `/$defs/vocalPerformance/properties/breathEvents` | No | type: "array"; items: 1 entries (see descendant pointers) |  |
| `/$defs/vocalPerformance/properties/breathEvents/items` | Context / conditional | $ref: "#/$defs/vocalBreathEvent" |  |
| `/$defs/vocalPerformance/properties/noteIds` | No | type: "array"; items: 1 entries (see descendant pointers); minItems: 1; uniqueItems: true | Optional exact list of existing note IDs performed by this voice in the containing clip. No duplicate note objects. When present it includes all locally aligned note IDs for that voice. When absent, derive ownership only from voice-specific alignments. Never infer from song.melodyTrackIds. |
| `/$defs/vocalPerformance/properties/noteIds/items` | Context / conditional | $ref: "#/$defs/id" |  |
| `/$defs/vocalPhonemeEvent` | Context / conditional | type: "object"; properties: 9 entries (see descendant pointers); required: ["id","unitId","alphabet","symbol","start","duration"]; additionalProperties: false; allOf: 1 branches (see descendant pointers) | Explicit phoneme timing, expressed in clip-relative ppq ticks, negative allowed with nonnegative absolute song time. |
| `/$defs/vocalPhonemeEvent/properties/id` | Yes | $ref: "#/$defs/id" |  |
| `/$defs/vocalPhonemeEvent/properties/unitId` | Yes | $ref: "#/$defs/id" |  |
| `/$defs/vocalPhonemeEvent/properties/noteId` | No | $ref: "#/$defs/id" |  |
| `/$defs/vocalPhonemeEvent/properties/alphabet` | Yes | enum: ["ipa","xsampa","arpabet","other"] |  |
| `/$defs/vocalPhonemeEvent/properties/namespace` | No | type: "string"; minLength: 1 |  |
| `/$defs/vocalPhonemeEvent/properties/symbol` | Yes | type: "string"; minLength: 1 |  |
| `/$defs/vocalPhonemeEvent/properties/start` | Yes | $ref: "#/$defs/signed" |  |
| `/$defs/vocalPhonemeEvent/properties/duration` | Yes | $ref: "#/$defs/positive" |  |
| `/$defs/vocalPhonemeEvent/properties/order` | No | type: "integer" | Optional deterministic ordering when multiple phonemeEvents for one voice share the same start tick; distinct within a (voiceId, start) tie group. Not an audio rendering priority. |
| `/$defs/vocalPhonemeEvent/allOf/0` | Context / conditional | if: 2 entries (see descendant pointers); then: 1 entries (see descendant pointers) |  |
| `/$defs/vocalPhonemeEvent/allOf/0/if` | Context / conditional | properties: 1 entries (see descendant pointers); required: ["alphabet"] |  |
| `/$defs/vocalPhonemeEvent/allOf/0/if/properties/alphabet` | Yes | const: "other" |  |
| `/$defs/vocalPhonemeEvent/allOf/0/then` | Context / conditional | required: ["namespace"] |  |
| `/$defs/vocalCurvePointPitch` | Context / conditional | type: "object"; properties: 2 entries (see descendant pointers); required: ["at","value"]; additionalProperties: false |  |
| `/$defs/vocalCurvePointPitch/properties/at` | Yes | $ref: "#/$defs/signed" |  |
| `/$defs/vocalCurvePointPitch/properties/value` | Yes | type: "number" | Semitone offset from the targeted MIDI note, in cents (signed). |
| `/$defs/vocalCurvePointNormalized` | Context / conditional | type: "object"; properties: 2 entries (see descendant pointers); required: ["at","value"]; additionalProperties: false |  |
| `/$defs/vocalCurvePointNormalized/properties/at` | Yes | $ref: "#/$defs/signed" |  |
| `/$defs/vocalCurvePointNormalized/properties/value` | Yes | type: "number"; minimum: 0; maximum: 1 |  |
| `/$defs/vocalPitchCurve` | Context / conditional | type: "object"; properties: 5 entries (see descendant pointers); required: ["id","targetNoteId","unit","interpolation","points"]; additionalProperties: false | Specific vocal pitch offset for a single concrete Note, in cents; sample points use clip-relative ppq ticks. |
| `/$defs/vocalPitchCurve/properties/id` | Yes | $ref: "#/$defs/id" |  |
| `/$defs/vocalPitchCurve/properties/targetNoteId` | Yes | $ref: "#/$defs/id" |  |
| `/$defs/vocalPitchCurve/properties/unit` | Yes | const: "cents" |  |
| `/$defs/vocalPitchCurve/properties/interpolation` | Yes | enum: ["step","linear"] |  |
| `/$defs/vocalPitchCurve/properties/points` | Yes | type: "array"; minItems: 1; items: 1 entries (see descendant pointers) |  |
| `/$defs/vocalPitchCurve/properties/points/items` | Context / conditional | $ref: "#/$defs/vocalCurvePointPitch" |  |
| `/$defs/vocalExpressionCurve` | Context / conditional | type: "object"; properties: 5 entries (see descendant pointers); required: ["id","parameter","interpolation","points"]; additionalProperties: false | Portable vocal parameters, each normalized 0..1, with no promise of perceptually identical output across engines. |
| `/$defs/vocalExpressionCurve/properties/id` | Yes | $ref: "#/$defs/id" |  |
| `/$defs/vocalExpressionCurve/properties/parameter` | Yes | enum: ["dynamics","breathiness","tension","brightness","voicing"] |  |
| `/$defs/vocalExpressionCurve/properties/interpolation` | Yes | enum: ["step","linear"] |  |
| `/$defs/vocalExpressionCurve/properties/points` | Yes | type: "array"; minItems: 1; items: 1 entries (see descendant pointers) |  |
| `/$defs/vocalExpressionCurve/properties/points/items` | Context / conditional | $ref: "#/$defs/vocalCurvePointNormalized" |  |
| `/$defs/vocalExpressionCurve/properties/targetNoteId` | No | $ref: "#/$defs/id" | Optional note-specific replacement of a clip-scoped curve of the same parameter while the note is active. Points still use clip-relative ticks. Do not sum both curves. |
| `/$defs/vocalTechnique` | Context / conditional | type: "object"; properties: 6 entries (see descendant pointers); required: ["id","start","duration","kind"]; additionalProperties: false | Semantic artistic intention, not deterministic rendering or an extra pitch source. |
| `/$defs/vocalTechnique/properties/id` | Yes | $ref: "#/$defs/id" |  |
| `/$defs/vocalTechnique/properties/start` | Yes | $ref: "#/$defs/signed" |  |
| `/$defs/vocalTechnique/properties/duration` | Yes | $ref: "#/$defs/positive" |  |
| `/$defs/vocalTechnique/properties/kind` | Yes | enum: ["scoop","fall","vibrato","portamento","legato","staccato","accent","whisper","growl","falsetto","humming","rap","melisma"] |  |
| `/$defs/vocalTechnique/properties/intensity` | No | type: "number"; minimum: 0; maximum: 1 |  |
| `/$defs/vocalTechnique/properties/targetNoteId` | No | $ref: "#/$defs/id" |  |
| `/$defs/vocalBreathEvent` | Context / conditional | type: "object"; properties: 5 entries (see descendant pointers); required: ["id","start","duration","kind"]; additionalProperties: false | Optional breath marker. The renderer decides whether to synthesize audible breath. |
| `/$defs/vocalBreathEvent/properties/id` | Yes | $ref: "#/$defs/id" |  |
| `/$defs/vocalBreathEvent/properties/start` | Yes | $ref: "#/$defs/signed" |  |
| `/$defs/vocalBreathEvent/properties/duration` | Yes | $ref: "#/$defs/positive" |  |
| `/$defs/vocalBreathEvent/properties/kind` | Yes | enum: ["inhale","exhale"] |  |
| `/$defs/vocalBreathEvent/properties/intensity` | No | type: "number"; minimum: 0; maximum: 1 |  |
| `/$defs/positiveIntRange` | Context / conditional | type: "object"; properties: 2 entries (see descendant pointers); required: ["min","max"]; additionalProperties: false | Inclusive tick bounds; semantic check min <= max. |
| `/$defs/positiveIntRange/properties/min` | Yes | $ref: "#/$defs/positive" |  |
| `/$defs/positiveIntRange/properties/max` | Yes | $ref: "#/$defs/positive" |  |
| `/$defs/nonnegativeNumberRange` | Context / conditional | type: "object"; properties: 2 entries (see descendant pointers); required: ["min","max"]; additionalProperties: false | Inclusive range; semantic check min <= max. Count distinct note-on groups at equal onset ticks as one onset. |
| `/$defs/nonnegativeNumberRange/properties/min` | Yes | type: "number"; minimum: 0; maximum: 128 |  |
| `/$defs/nonnegativeNumberRange/properties/max` | Yes | type: "number"; minimum: 0; maximum: 128 |  |
| `/$defs/phrasingDirectionParameters` | Context / conditional | type: "object"; properties: 7 entries (see descendant pointers); required: ["adherence"]; additionalProperties: false; minProperties: 2 | At least one musical property beyond adherence must be authored; motifRef resolves to phraseLibrary.templates[].id. |
| `/$defs/phrasingDirectionParameters/properties/phraseLengthTicks` | No | $ref: "#/$defs/positiveIntRange" |  |
| `/$defs/phrasingDirectionParameters/properties/onsetGroupsPerQuarter` | No | $ref: "#/$defs/nonnegativeNumberRange" |  |
| `/$defs/phrasingDirectionParameters/properties/development` | No | enum: ["repetition","motivicVariation","sequence","contrast","free"] |  |
| `/$defs/phrasingDirectionParameters/properties/contour` | No | enum: ["ascending","descending","arch","valley","stable","free"] |  |
| `/$defs/phrasingDirectionParameters/properties/energyShape` | No | enum: ["rising","falling","arch","valley","stable","free"] | Abstract musical-energy direction; not equivalent to output velocity or volume. |
| `/$defs/phrasingDirectionParameters/properties/motifRef` | No | $ref: "#/$defs/id" |  |
| `/$defs/phrasingDirectionParameters/properties/adherence` | Yes | enum: ["strict","preferred"] |  |
| `/$defs/phrasingDirection` | Context / conditional | type: "object"; properties: 7 entries (see descendant pointers); required: ["id","type","start","duration","parameters"]; additionalProperties: false | 4.3 optional phrasing Track Direction, using global source-timeline ticks. |
| `/$defs/phrasingDirection/properties/id` | Yes | $ref: "#/$defs/id" |  |
| `/$defs/phrasingDirection/properties/type` | Yes | const: "phrasing" |  |
| `/$defs/phrasingDirection/properties/start` | Yes | $ref: "#/$defs/nonnegative" |  |
| `/$defs/phrasingDirection/properties/duration` | Yes | $ref: "#/$defs/positive" |  |
| `/$defs/phrasingDirection/properties/label` | No | type: "string" |  |
| `/$defs/phrasingDirection/properties/instruction` | No | type: "string" | Non-executable music-text context, subordinate to structured fields. |
| `/$defs/phrasingDirection/properties/parameters` | Yes | $ref: "#/$defs/phrasingDirectionParameters" |  |
| `/$defs/lyricCandidateSet` | Context / conditional | type: "object"; properties: 1 entries (see descendant pointers); required: ["phraseIds"]; additionalProperties: false | One ordered candidate sequence of authored Lyric Phrase IDs. No implicit note alignment. |
| `/$defs/lyricCandidateSet/properties/phraseIds` | Yes | type: "array"; items: 1 entries (see descendant pointers); minItems: 1; uniqueItems: true |  |
| `/$defs/lyricCandidateSet/properties/phraseIds/items` | Context / conditional | $ref: "#/$defs/id" |  |
| `/$defs/vocalFreedomDirectionParameters` | Context / conditional | type: "object"; properties: 6 entries (see descendant pointers); required: ["voiceId","textPolicy","melodyPolicy","adherence"]; additionalProperties: false; if: 2 entries (see descendant pointers); then: 1 entries (see descendant pointers); else: 1 entries (see descendant pointers) | Voice-specific freedom policy. Fixed text does not automatically imply fixed melody or vice versa. |
| `/$defs/vocalFreedomDirectionParameters/properties/voiceId` | Yes | $ref: "#/$defs/id" |  |
| `/$defs/vocalFreedomDirectionParameters/properties/textPolicy` | Yes | enum: ["fixed","alternatives","open"] |  |
| `/$defs/vocalFreedomDirectionParameters/properties/melodyPolicy` | Yes | enum: ["fixed","ornamentable","open"] |  |
| `/$defs/vocalFreedomDirectionParameters/properties/vocalizationKind` | No | enum: ["lexical","scat","humming","nonLexical"] |  |
| `/$defs/vocalFreedomDirectionParameters/properties/candidatePhraseSets` | No | type: "array"; items: 1 entries (see descendant pointers); minItems: 2 |  |
| `/$defs/vocalFreedomDirectionParameters/properties/candidatePhraseSets/items` | Context / conditional | $ref: "#/$defs/lyricCandidateSet" |  |
| `/$defs/vocalFreedomDirectionParameters/properties/adherence` | Yes | enum: ["strict","preferred"] |  |
| `/$defs/vocalFreedomDirectionParameters/if` | Context / conditional | properties: 1 entries (see descendant pointers); required: ["textPolicy"] |  |
| `/$defs/vocalFreedomDirectionParameters/if/properties/textPolicy` | Yes | const: "alternatives" |  |
| `/$defs/vocalFreedomDirectionParameters/then` | Context / conditional | required: ["candidatePhraseSets"] |  |
| `/$defs/vocalFreedomDirectionParameters/else` | Context / conditional | not: 1 entries (see descendant pointers) |  |
| `/$defs/vocalFreedomDirectionParameters/else/not` | Context / conditional | required: ["candidatePhraseSets"] |  |
| `/$defs/vocalFreedomDirection` | Context / conditional | type: "object"; properties: 7 entries (see descendant pointers); required: ["id","type","start","duration","parameters"]; additionalProperties: false | 4.3 optional vocalFreedom Track Direction, using global source-timeline ticks. |
| `/$defs/vocalFreedomDirection/properties/id` | Yes | $ref: "#/$defs/id" |  |
| `/$defs/vocalFreedomDirection/properties/type` | Yes | const: "vocalFreedom" |  |
| `/$defs/vocalFreedomDirection/properties/start` | Yes | $ref: "#/$defs/nonnegative" |  |
| `/$defs/vocalFreedomDirection/properties/duration` | Yes | $ref: "#/$defs/positive" |  |
| `/$defs/vocalFreedomDirection/properties/label` | No | type: "string" |  |
| `/$defs/vocalFreedomDirection/properties/instruction` | No | type: "string" | Non-executable music-text context, subordinate to structured fields. |
| `/$defs/vocalFreedomDirection/properties/parameters` | Yes | $ref: "#/$defs/vocalFreedomDirectionParameters" |  |
| `/$defs/performanceRequirements` | Context / conditional | type: "object"; properties: 4 entries (see descendant pointers); required: []; additionalProperties: false; minProperties: 1 | Minimum/peak musical capabilities required to realize this authored part, not an assertion about the performer. No robot mechanics or safety commands. |
| `/$defs/performanceRequirements/properties/requiredPolyphony` | No | type: "integer"; minimum: 1; maximum: 128 |  |
| `/$defs/performanceRequirements/properties/requiredPitchRange` | No | $ref: "#/$defs/playablePitchRange" |  |
| `/$defs/performanceRequirements/properties/requiredArticulations` | No | type: "array"; items: 2 entries (see descendant pointers); minItems: 1; uniqueItems: true |  |
| `/$defs/performanceRequirements/properties/requiredArticulations/items` | Context / conditional | type: "string"; minLength: 1 |  |
| `/$defs/performanceRequirements/properties/peakOnsetGroupsPerQuarter` | No | type: "number"; exclusiveMinimum: 0; maximum: 128 |  |
| `/$defs/performanceScope` | Context / conditional | type: "object"; properties: 2 entries (see descendant pointers); required: ["performancePlanId","visitId"]; additionalProperties: false | Bind to exactly one finite visit within a specific plan. |
| `/$defs/performanceScope/properties/performancePlanId` | Yes | $ref: "#/$defs/id" |  |
| `/$defs/performanceScope/properties/visitId` | Yes | $ref: "#/$defs/id" |  |
| `/$defs/ensembleInteraction` | Context / conditional | type: "object"; properties: 11 entries (see descendant pointers); required: ["id","actorTrackId","partnerTrackId","relation","adherence"]; additionalProperties: false; anyOf: 2 branches (see descendant pointers); dependentRequired: {"start":["duration"],"duration":["start"]} | Directed actor/partner relationship: different Tracks, or the same Track only with both explicit and different Lyric Voice IDs whose trackId equals the shared Track. Use source tick range, visit scope, or both. No audio, real-time event, or motor control is implied. Same Track without two distinct owned Voices is a semantic error (JSON Schema cannot compare sibling ID values). |
| `/$defs/ensembleInteraction/properties/id` | Yes | $ref: "#/$defs/id" |  |
| `/$defs/ensembleInteraction/properties/actorTrackId` | Yes | $ref: "#/$defs/id" |  |
| `/$defs/ensembleInteraction/properties/partnerTrackId` | Yes | $ref: "#/$defs/id" |  |
| `/$defs/ensembleInteraction/properties/actorVoiceId` | No | $ref: "#/$defs/id" |  |
| `/$defs/ensembleInteraction/properties/partnerVoiceId` | No | $ref: "#/$defs/id" |  |
| `/$defs/ensembleInteraction/properties/relation` | Yes | enum: ["respondTo","followRhythm","alternateWith","leaveSpaceFor","reinforce"] |  |
| `/$defs/ensembleInteraction/properties/start` | No | $ref: "#/$defs/nonnegative" |  |
| `/$defs/ensembleInteraction/properties/duration` | No | $ref: "#/$defs/positive" |  |
| `/$defs/ensembleInteraction/properties/scope` | No | $ref: "#/$defs/performanceScope" |  |
| `/$defs/ensembleInteraction/properties/responseWindowTicks` | No | $ref: "#/$defs/positive" |  |
| `/$defs/ensembleInteraction/properties/adherence` | Yes | enum: ["strict","preferred"] |  |
| `/$defs/ensembleInteraction/anyOf/0` | Context / conditional | required: ["start","duration"] |  |
| `/$defs/ensembleInteraction/anyOf/1` | Context / conditional | required: ["scope"] |  |
| `/$defs/visitPart` | Context / conditional | type: "object"; properties: 4 entries (see descendant pointers); required: ["trackId","realization"]; additionalProperties: false | A part rule within one performance visit, not a mutation of the source Track. |
| `/$defs/visitPart/properties/trackId` | Yes | $ref: "#/$defs/id" |  |
| `/$defs/visitPart/properties/role` | No | type: "string"; minLength: 1 | Visit-scoped role override of Track default; timed playingRole conflict requires explicitly listed replacement. |
| `/$defs/visitPart/properties/realization` | Yes | enum: ["fixed","open","silent"] |  |
| `/$defs/visitPart/properties/replacesDirectionIds` | No | type: "array"; items: 1 entries (see descendant pointers); uniqueItems: true | Only explicit source-track playingRole Direction IDs may be replaced by the visit role. |
| `/$defs/visitPart/properties/replacesDirectionIds/items` | Context / conditional | $ref: "#/$defs/id" |  |
| `/$defs/performanceVisit` | Context / conditional | type: "object"; properties: 6 entries (see descendant pointers); required: ["id","ordinal","parts"]; additionalProperties: false; oneOf: 2 branches (see descendant pointers); not: 1 entries (see descendant pointers) | Finite visit; exactly one source selector. Ordinals must be 0..N-1 in unique sequence within one plan. |
| `/$defs/performanceVisit/properties/id` | Yes | $ref: "#/$defs/id" |  |
| `/$defs/performanceVisit/properties/ordinal` | Yes | $ref: "#/$defs/nonnegative" |  |
| `/$defs/performanceVisit/properties/label` | No | type: "string" |  |
| `/$defs/performanceVisit/properties/sourceSectionIds` | No | type: "array"; items: 1 entries (see descendant pointers); minItems: 1 |  |
| `/$defs/performanceVisit/properties/sourceSectionIds/items` | Context / conditional | $ref: "#/$defs/id" |  |
| `/$defs/performanceVisit/properties/sourceRange` | No | $ref: "#/$defs/range" |  |
| `/$defs/performanceVisit/properties/parts` | Yes | type: "array"; items: 1 entries (see descendant pointers) |  |
| `/$defs/performanceVisit/properties/parts/items` | Context / conditional | $ref: "#/$defs/visitPart" |  |
| `/$defs/performanceVisit/oneOf/0` | Context / conditional | required: ["sourceSectionIds"] |  |
| `/$defs/performanceVisit/oneOf/1` | Context / conditional | required: ["sourceRange"] |  |
| `/$defs/performanceVisit/not` | Context / conditional | required: ["sourceSectionIds","sourceRange"] |  |
| `/$defs/performancePlan` | Context / conditional | type: "object"; properties: 5 entries (see descendant pointers); required: ["id","mode","defaultRealization","visits"]; additionalProperties: false | Opt-in finite expanded playthrough. Source Section/Tick remains authoritative. No implicit cues, indefinite loops, or network session state. |
| `/$defs/performancePlan/properties/id` | Yes | $ref: "#/$defs/id" |  |
| `/$defs/performancePlan/properties/name` | No | type: "string" |  |
| `/$defs/performancePlan/properties/mode` | Yes | const: "orderedFinite" |  |
| `/$defs/performancePlan/properties/defaultRealization` | Yes | enum: ["fixed","silent","unspecified"] | Explicit policy for unlisted tracks per visit; unspecified cannot claim deterministic replay. |
| `/$defs/performancePlan/properties/visits` | Yes | type: "array"; items: 1 entries (see descendant pointers); minItems: 1 |  |
| `/$defs/performancePlan/properties/visits/items` | Context / conditional | $ref: "#/$defs/performanceVisit" |  |
| `/$defs/takeId51` | Context / conditional | type: "string"; pattern: "^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$"; not: 1 entries (see descendant pointers) |  |
| `/$defs/takeId51/not` | Context / conditional | pattern: "[\\r\\n\\u2028\\u2029]" |  |
| `/$defs/takeTick51` | Context / conditional | type: "integer"; minimum: 0; maximum: 9007199254740991 |  |
| `/$defs/takeDuration51` | Context / conditional | type: "integer"; minimum: 1; maximum: 9007199254740991 |  |
| `/$defs/takeOrigin51` | Context / conditional | type: "object"; additionalProperties: false; properties: 10 entries (see descendant pointers); required: ["kind"] | Optional inert provenance. Actor/session/proposal identifiers and prompts do not confer permissions or perform any network or generation action. |
| `/$defs/takeOrigin51/properties/kind` | Yes | enum: ["human","ai","import","derived","unknown"] |  |
| `/$defs/takeOrigin51/properties/actorId` | No | type: "string"; pattern: "^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$"; not: 1 entries (see descendant pointers) |  |
| `/$defs/takeOrigin51/properties/actorId/not` | Context / conditional | pattern: "[\\r\\n\\u2028\\u2029]" |  |
| `/$defs/takeOrigin51/properties/participantId` | No | type: "string"; pattern: "^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$"; not: 1 entries (see descendant pointers) |  |
| `/$defs/takeOrigin51/properties/participantId/not` | Context / conditional | pattern: "[\\r\\n\\u2028\\u2029]" |  |
| `/$defs/takeOrigin51/properties/sessionId` | No | type: "string"; pattern: "^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$"; not: 1 entries (see descendant pointers) |  |
| `/$defs/takeOrigin51/properties/sessionId/not` | Context / conditional | pattern: "[\\r\\n\\u2028\\u2029]" |  |
| `/$defs/takeOrigin51/properties/proposalId` | No | type: "string"; pattern: "^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$"; not: 1 entries (see descendant pointers) |  |
| `/$defs/takeOrigin51/properties/proposalId/not` | Context / conditional | pattern: "[\\r\\n\\u2028\\u2029]" |  |
| `/$defs/takeOrigin51/properties/commitEventId` | No | type: "string"; pattern: "^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$"; not: 1 entries (see descendant pointers) |  |
| `/$defs/takeOrigin51/properties/commitEventId/not` | Context / conditional | pattern: "[\\r\\n\\u2028\\u2029]" |  |
| `/$defs/takeOrigin51/properties/prompt` | No | type: "string" |  |
| `/$defs/takeOrigin51/properties/createdAt` | No | type: "string"; format: "date-time" |  |
| `/$defs/takeOrigin51/properties/model` | No | type: "string" |  |
| `/$defs/takeOrigin51/properties/sourceUri` | No | type: "string" |  |
| `/$defs/takeRating51` | Context / conditional | type: "object"; additionalProperties: false; properties: 3 entries (see descendant pointers); required: ["evaluatorId","score"] |  |
| `/$defs/takeRating51/properties/evaluatorId` | Yes | type: "string"; pattern: "^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$"; not: 1 entries (see descendant pointers) |  |
| `/$defs/takeRating51/properties/evaluatorId/not` | Context / conditional | pattern: "[\\r\\n\\u2028\\u2029]" |  |
| `/$defs/takeRating51/properties/score` | Yes | type: "number"; minimum: 0; maximum: 1 |  |
| `/$defs/takeRating51/properties/comment` | No | type: "string" |  |
| `/$defs/takeVisitSelection51` | Context / conditional | type: "object"; additionalProperties: false; properties: 3 entries (see descendant pointers); required: ["performancePlanId","visitId","compId"] | Comp selection overlay for one existing finite Performance Plan Visit. The Plan/Visit pair must be unique per Group. null denotes silence. Only the Group/Visit source-range intersection is selected. |
| `/$defs/takeVisitSelection51/properties/performancePlanId` | Yes | type: "string"; pattern: "^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$"; not: 1 entries (see descendant pointers) |  |
| `/$defs/takeVisitSelection51/properties/performancePlanId/not` | Context / conditional | pattern: "[\\r\\n\\u2028\\u2029]" |  |
| `/$defs/takeVisitSelection51/properties/visitId` | Yes | type: "string"; pattern: "^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$"; not: 1 entries (see descendant pointers) |  |
| `/$defs/takeVisitSelection51/properties/visitId/not` | Context / conditional | pattern: "[\\r\\n\\u2028\\u2029]" |  |
| `/$defs/takeVisitSelection51/properties/compId` | Yes | anyOf: 2 branches (see descendant pointers) |  |
| `/$defs/takeVisitSelection51/properties/compId/anyOf/0` | Context / conditional | type: "string"; pattern: "^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$"; not: 1 entries (see descendant pointers) |  |
| `/$defs/takeVisitSelection51/properties/compId/anyOf/0/not` | Context / conditional | pattern: "[\\r\\n\\u2028\\u2029]" |  |
| `/$defs/takeVisitSelection51/properties/compId/anyOf/1` | Context / conditional | type: "null" |  |
| `/$defs/takeLiveCandidate51` | Context / conditional | type: "object"; additionalProperties: false; properties: 2 entries (see descendant pointers); required: ["compId"] |  |
| `/$defs/takeLiveCandidate51/properties/compId` | Yes | type: "string"; pattern: "^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$"; not: 1 entries (see descendant pointers) |  |
| `/$defs/takeLiveCandidate51/properties/compId/not` | Context / conditional | pattern: "[\\r\\n\\u2028\\u2029]" |  |
| `/$defs/takeLiveCandidate51/properties/weight` | No | type: "number"; minimum: 0 |  |
| `/$defs/takeSelectionHistory51` | Context / conditional | type: "object"; additionalProperties: false; properties: 5 entries (see descendant pointers); required: ["sequence","compId"] | Informational saved-selection history, strictly increasing in sequence within its Group. Historical deleted Comp IDs may be retained; history never changes current selection or playback. |
| `/$defs/takeSelectionHistory51/properties/sequence` | Yes | type: "integer"; minimum: 0; maximum: 9007199254740991 |  |
| `/$defs/takeSelectionHistory51/properties/compId` | Yes | anyOf: 2 branches (see descendant pointers) |  |
| `/$defs/takeSelectionHistory51/properties/compId/anyOf/0` | Context / conditional | type: "string"; pattern: "^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$"; not: 1 entries (see descendant pointers) |  |
| `/$defs/takeSelectionHistory51/properties/compId/anyOf/0/not` | Context / conditional | pattern: "[\\r\\n\\u2028\\u2029]" |  |
| `/$defs/takeSelectionHistory51/properties/compId/anyOf/1` | Context / conditional | type: "null" |  |
| `/$defs/takeSelectionHistory51/properties/actorId` | No | type: "string"; pattern: "^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$"; not: 1 entries (see descendant pointers) |  |
| `/$defs/takeSelectionHistory51/properties/actorId/not` | Context / conditional | pattern: "[\\r\\n\\u2028\\u2029]" |  |
| `/$defs/takeSelectionHistory51/properties/recordedAt` | No | type: "string"; format: "date-time" |  |
| `/$defs/takeSelectionHistory51/properties/reason` | No | type: "string" |  |
| `/$defs/takeNoteLink51` | Context / conditional | type: "object"; additionalProperties: false; properties: 2 entries (see descendant pointers); required: ["sourceNoteId","outputNoteId"] |  |
| `/$defs/takeNoteLink51/properties/sourceNoteId` | Yes | type: "string"; pattern: "^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$"; not: 1 entries (see descendant pointers) |  |
| `/$defs/takeNoteLink51/properties/sourceNoteId/not` | Context / conditional | pattern: "[\\r\\n\\u2028\\u2029]" |  |
| `/$defs/takeNoteLink51/properties/outputNoteId` | Yes | type: "string"; pattern: "^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$"; not: 1 entries (see descendant pointers) |  |
| `/$defs/takeNoteLink51/properties/outputNoteId/not` | Context / conditional | pattern: "[\\r\\n\\u2028\\u2029]" |  |
| `/$defs/takeLiveSelection51` | Context / conditional | type: "object"; additionalProperties: false; properties: 2 entries (see descendant pointers); required: ["mode"]; allOf: 2 branches (see descendant pointers) | Optional launch-time selection policy. fixed/manual have no candidates; cycle/random/weighted require distinct Comp IDs. weighted requires all nonnegative weights and at least one positive weight. Distinct compId values and reference resolution are semantic constraints. |
| `/$defs/takeLiveSelection51/properties/mode` | Yes | enum: ["fixed","manual","cycle","random","weighted"] |  |
| `/$defs/takeLiveSelection51/properties/candidates` | No | type: "array"; items: 1 entries (see descendant pointers); minItems: 1; uniqueItems: true |  |
| `/$defs/takeLiveSelection51/properties/candidates/items` | Context / conditional | $ref: "#/$defs/takeLiveCandidate51" |  |
| `/$defs/takeLiveSelection51/allOf/0` | Context / conditional | if: 2 entries (see descendant pointers); then: 1 entries (see descendant pointers); else: 1 entries (see descendant pointers) |  |
| `/$defs/takeLiveSelection51/allOf/0/if` | Context / conditional | properties: 1 entries (see descendant pointers); required: ["mode"] |  |
| `/$defs/takeLiveSelection51/allOf/0/if/properties/mode` | Yes | enum: ["cycle","random","weighted"] |  |
| `/$defs/takeLiveSelection51/allOf/0/then` | Context / conditional | required: ["candidates"] |  |
| `/$defs/takeLiveSelection51/allOf/0/else` | Context / conditional | not: 1 entries (see descendant pointers) |  |
| `/$defs/takeLiveSelection51/allOf/0/else/not` | Context / conditional | required: ["candidates"] |  |
| `/$defs/takeLiveSelection51/allOf/1` | Context / conditional | if: 2 entries (see descendant pointers); then: 1 entries (see descendant pointers); else: 1 entries (see descendant pointers) |  |
| `/$defs/takeLiveSelection51/allOf/1/if` | Context / conditional | properties: 1 entries (see descendant pointers); required: ["mode"] |  |
| `/$defs/takeLiveSelection51/allOf/1/if/properties/mode` | Yes | const: "weighted" |  |
| `/$defs/takeLiveSelection51/allOf/1/then` | Context / conditional | properties: 1 entries (see descendant pointers) |  |
| `/$defs/takeLiveSelection51/allOf/1/then/properties/candidates` | No | items: 1 entries (see descendant pointers); contains: 3 entries (see descendant pointers); minContains: 1 |  |
| `/$defs/takeLiveSelection51/allOf/1/then/properties/candidates/items` | Context / conditional | required: ["weight"] |  |
| `/$defs/takeLiveSelection51/allOf/1/then/properties/candidates/contains` | Context / conditional | type: "object"; properties: 1 entries (see descendant pointers); required: ["weight"] |  |
| `/$defs/takeLiveSelection51/allOf/1/then/properties/candidates/contains/properties/weight` | Yes | type: "number"; exclusiveMinimum: 0 |  |
| `/$defs/takeLiveSelection51/allOf/1/else` | Context / conditional | properties: 1 entries (see descendant pointers) |  |
| `/$defs/takeLiveSelection51/allOf/1/else/properties/candidates` | No | items: 1 entries (see descendant pointers) |  |
| `/$defs/takeLiveSelection51/allOf/1/else/properties/candidates/items` | Context / conditional | not: 1 entries (see descendant pointers) |  |
| `/$defs/takeLiveSelection51/allOf/1/else/properties/candidates/items/not` | Context / conditional | required: ["weight"] |  |
| `/$defs/midiTake51` | Context / conditional | type: "object"; additionalProperties: false; properties: 8 entries (see descendant pointers); required: ["id","kind","clipIds"] |  |
| `/$defs/midiTake51/properties/id` | Yes | type: "string"; pattern: "^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$"; not: 1 entries (see descendant pointers) |  |
| `/$defs/midiTake51/properties/id/not` | Context / conditional | pattern: "[\\r\\n\\u2028\\u2029]" |  |
| `/$defs/midiTake51/properties/name` | No | type: "string" |  |
| `/$defs/midiTake51/properties/kind` | Yes | enum: ["take","variation","alternative"] |  |
| `/$defs/midiTake51/properties/clipIds` | Yes | type: "array"; items: 3 entries (see descendant pointers); minItems: 1; uniqueItems: true |  |
| `/$defs/midiTake51/properties/clipIds/items` | Context / conditional | type: "string"; pattern: "^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$"; not: 1 entries (see descendant pointers) |  |
| `/$defs/midiTake51/properties/clipIds/items/not` | Context / conditional | pattern: "[\\r\\n\\u2028\\u2029]" |  |
| `/$defs/midiTake51/properties/laneOrder` | No | type: "integer"; minimum: 0; maximum: 9007199254740991 |  |
| `/$defs/midiTake51/properties/parentTakeId` | No | type: "string"; pattern: "^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$"; not: 1 entries (see descendant pointers) |  |
| `/$defs/midiTake51/properties/parentTakeId/not` | Context / conditional | pattern: "[\\r\\n\\u2028\\u2029]" |  |
| `/$defs/midiTake51/properties/origin` | No | $ref: "#/$defs/takeOrigin51" |  |
| `/$defs/midiTake51/properties/ratings` | No | type: "array"; items: 1 entries (see descendant pointers); minItems: 0 |  |
| `/$defs/midiTake51/properties/ratings/items` | Context / conditional | $ref: "#/$defs/takeRating51" |  |
| `/$defs/midiCompRegion51` | Context / conditional | oneOf: 2 branches (see descendant pointers) |  |
| `/$defs/midiCompRegion51/oneOf/0` | Context / conditional | type: "object"; additionalProperties: false; properties: 6 entries (see descendant pointers); required: ["id","kind","startTick","durationTicks","takeId","clipId"] |  |
| `/$defs/midiCompRegion51/oneOf/0/properties/id` | Yes | type: "string"; pattern: "^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$"; not: 1 entries (see descendant pointers) |  |
| `/$defs/midiCompRegion51/oneOf/0/properties/id/not` | Context / conditional | pattern: "[\\r\\n\\u2028\\u2029]" |  |
| `/$defs/midiCompRegion51/oneOf/0/properties/startTick` | Yes | type: "integer"; minimum: 0; maximum: 9007199254740991 |  |
| `/$defs/midiCompRegion51/oneOf/0/properties/durationTicks` | Yes | type: "integer"; minimum: 1; maximum: 9007199254740991 |  |
| `/$defs/midiCompRegion51/oneOf/0/properties/kind` | Yes | const: "source" |  |
| `/$defs/midiCompRegion51/oneOf/0/properties/takeId` | Yes | type: "string"; pattern: "^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$"; not: 1 entries (see descendant pointers) |  |
| `/$defs/midiCompRegion51/oneOf/0/properties/takeId/not` | Context / conditional | pattern: "[\\r\\n\\u2028\\u2029]" |  |
| `/$defs/midiCompRegion51/oneOf/0/properties/clipId` | Yes | type: "string"; pattern: "^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$"; not: 1 entries (see descendant pointers) |  |
| `/$defs/midiCompRegion51/oneOf/0/properties/clipId/not` | Context / conditional | pattern: "[\\r\\n\\u2028\\u2029]" |  |
| `/$defs/midiCompRegion51/oneOf/1` | Context / conditional | type: "object"; additionalProperties: false; properties: 4 entries (see descendant pointers); required: ["id","kind","startTick","durationTicks"] |  |
| `/$defs/midiCompRegion51/oneOf/1/properties/id` | Yes | type: "string"; pattern: "^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$"; not: 1 entries (see descendant pointers) |  |
| `/$defs/midiCompRegion51/oneOf/1/properties/id/not` | Context / conditional | pattern: "[\\r\\n\\u2028\\u2029]" |  |
| `/$defs/midiCompRegion51/oneOf/1/properties/startTick` | Yes | type: "integer"; minimum: 0; maximum: 9007199254740991 |  |
| `/$defs/midiCompRegion51/oneOf/1/properties/durationTicks` | Yes | type: "integer"; minimum: 1; maximum: 9007199254740991 |  |
| `/$defs/midiCompRegion51/oneOf/1/properties/kind` | Yes | const: "silence" |  |
| `/$defs/midiComp51` | Context / conditional | type: "object"; additionalProperties: false; properties: 6 entries (see descendant pointers); required: ["id","compRegions","outputClipIds","noteBoundary"]; allOf: 1 branches (see descendant pointers) | A complete ordered partition of the Group's range into selected source or explicit-silence regions. The map is the editing authority; ordinary materialized output is playback authority. All-silence Comp has no outputs; any source region requires at least one output descriptor (MIDI may contain an empty notes array). IDs and ranges must resolve consistently in a single authoring transaction. |
| `/$defs/midiComp51/properties/id` | Yes | type: "string"; pattern: "^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$"; not: 1 entries (see descendant pointers) |  |
| `/$defs/midiComp51/properties/id/not` | Context / conditional | pattern: "[\\r\\n\\u2028\\u2029]" |  |
| `/$defs/midiComp51/properties/name` | No | type: "string" |  |
| `/$defs/midiComp51/properties/compRegions` | Yes | type: "array"; items: 1 entries (see descendant pointers); minItems: 1 |  |
| `/$defs/midiComp51/properties/compRegions/items` | Context / conditional | $ref: "#/$defs/midiCompRegion51" |  |
| `/$defs/midiComp51/properties/outputClipIds` | Yes | type: "array"; items: 3 entries (see descendant pointers); minItems: 0; uniqueItems: true |  |
| `/$defs/midiComp51/properties/outputClipIds/items` | Context / conditional | type: "string"; pattern: "^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$"; not: 1 entries (see descendant pointers) |  |
| `/$defs/midiComp51/properties/outputClipIds/items/not` | Context / conditional | pattern: "[\\r\\n\\u2028\\u2029]" |  |
| `/$defs/midiComp51/properties/noteBoundary` | Yes | enum: ["truncate","retrigger","authored"] |  |
| `/$defs/midiComp51/properties/noteLinks` | No | type: "array"; items: 1 entries (see descendant pointers); minItems: 0; uniqueItems: true |  |
| `/$defs/midiComp51/properties/noteLinks/items` | Context / conditional | $ref: "#/$defs/takeNoteLink51" |  |
| `/$defs/midiComp51/allOf/0` | Context / conditional | if: 2 entries (see descendant pointers); then: 1 entries (see descendant pointers); else: 1 entries (see descendant pointers) |  |
| `/$defs/midiComp51/allOf/0/if` | Context / conditional | properties: 1 entries (see descendant pointers); required: ["compRegions"] |  |
| `/$defs/midiComp51/allOf/0/if/properties/compRegions` | Yes | contains: 2 entries (see descendant pointers); minContains: 1 |  |
| `/$defs/midiComp51/allOf/0/if/properties/compRegions/contains` | Context / conditional | properties: 1 entries (see descendant pointers); required: ["kind"] |  |
| `/$defs/midiComp51/allOf/0/if/properties/compRegions/contains/properties/kind` | Yes | const: "source" |  |
| `/$defs/midiComp51/allOf/0/then` | Context / conditional | properties: 1 entries (see descendant pointers) |  |
| `/$defs/midiComp51/allOf/0/then/properties/outputClipIds` | No | minItems: 1 |  |
| `/$defs/midiComp51/allOf/0/else` | Context / conditional | properties: 2 entries (see descendant pointers) |  |
| `/$defs/midiComp51/allOf/0/else/properties/outputClipIds` | No | maxItems: 0 |  |
| `/$defs/midiComp51/allOf/0/else/properties/noteLinks` | No | maxItems: 0 |  |
| `/$defs/midiTakeGroup51` | Context / conditional | type: "object"; additionalProperties: false; properties: 12 entries (see descendant pointers); required: ["id","trackId","startTick","durationTicks","takes","comps","activeCompId"]; allOf: 1 branches (see descendant pointers) | Non-overlapping source-score Tick range owned by trackId. All ranges use Score PPQ, are half-open, and have safe-integer endpoints. Sources and independently identified materialized outputs remain on the existing timeline; source candidates never play as ordinary active clips. References, ownership, range sums, unique scoped IDs and flags require semantic validation in addition to this schema. |
| `/$defs/midiTakeGroup51/properties/id` | Yes | type: "string"; pattern: "^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$"; not: 1 entries (see descendant pointers) |  |
| `/$defs/midiTakeGroup51/properties/id/not` | Context / conditional | pattern: "[\\r\\n\\u2028\\u2029]" |  |
| `/$defs/midiTakeGroup51/properties/trackId` | Yes | type: "string"; pattern: "^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$"; not: 1 entries (see descendant pointers) |  |
| `/$defs/midiTakeGroup51/properties/trackId/not` | Context / conditional | pattern: "[\\r\\n\\u2028\\u2029]" |  |
| `/$defs/midiTakeGroup51/properties/startTick` | Yes | type: "integer"; minimum: 0; maximum: 9007199254740991 |  |
| `/$defs/midiTakeGroup51/properties/durationTicks` | Yes | type: "integer"; minimum: 1; maximum: 9007199254740991 |  |
| `/$defs/midiTakeGroup51/properties/name` | No | type: "string" |  |
| `/$defs/midiTakeGroup51/properties/sectionId` | No | type: "string"; pattern: "^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$"; not: 1 entries (see descendant pointers) |  |
| `/$defs/midiTakeGroup51/properties/sectionId/not` | Context / conditional | pattern: "[\\r\\n\\u2028\\u2029]" |  |
| `/$defs/midiTakeGroup51/properties/takes` | Yes | type: "array"; items: 1 entries (see descendant pointers); minItems: 1 |  |
| `/$defs/midiTakeGroup51/properties/takes/items` | Context / conditional | $ref: "#/$defs/midiTake51" |  |
| `/$defs/midiTakeGroup51/properties/comps` | Yes | type: "array"; items: 1 entries (see descendant pointers); minItems: 0 |  |
| `/$defs/midiTakeGroup51/properties/comps/items` | Context / conditional | $ref: "#/$defs/midiComp51" |  |
| `/$defs/midiTakeGroup51/properties/activeCompId` | Yes | anyOf: 2 branches (see descendant pointers) | One Comp ID in this Group, or null for silence. Empty comps requires null. This saved selection controls the ordinary output flags; Visit/live selection overlays do not rewrite these saved flags. |
| `/$defs/midiTakeGroup51/properties/activeCompId/anyOf/0` | Context / conditional | type: "string"; pattern: "^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$"; not: 1 entries (see descendant pointers) |  |
| `/$defs/midiTakeGroup51/properties/activeCompId/anyOf/0/not` | Context / conditional | pattern: "[\\r\\n\\u2028\\u2029]" |  |
| `/$defs/midiTakeGroup51/properties/activeCompId/anyOf/1` | Context / conditional | type: "null" |  |
| `/$defs/midiTakeGroup51/properties/visitSelections` | No | type: "array"; items: 1 entries (see descendant pointers); minItems: 0; uniqueItems: true |  |
| `/$defs/midiTakeGroup51/properties/visitSelections/items` | Context / conditional | $ref: "#/$defs/takeVisitSelection51" |  |
| `/$defs/midiTakeGroup51/properties/liveSelection` | No | $ref: "#/$defs/takeLiveSelection51" |  |
| `/$defs/midiTakeGroup51/properties/takeSelectionHistory` | No | type: "array"; items: 1 entries (see descendant pointers); minItems: 0 |  |
| `/$defs/midiTakeGroup51/properties/takeSelectionHistory/items` | Context / conditional | $ref: "#/$defs/takeSelectionHistory51" |  |
| `/$defs/midiTakeGroup51/allOf/0` | Context / conditional | if: 2 entries (see descendant pointers); then: 1 entries (see descendant pointers) |  |
| `/$defs/midiTakeGroup51/allOf/0/if` | Context / conditional | properties: 1 entries (see descendant pointers); required: ["comps"] |  |
| `/$defs/midiTakeGroup51/allOf/0/if/properties/comps` | Yes | maxItems: 0 |  |
| `/$defs/midiTakeGroup51/allOf/0/then` | Context / conditional | properties: 3 entries (see descendant pointers) |  |
| `/$defs/midiTakeGroup51/allOf/0/then/properties/activeCompId` | No | type: "null" |  |
| `/$defs/midiTakeGroup51/allOf/0/then/properties/visitSelections` | No | items: 1 entries (see descendant pointers) |  |
| `/$defs/midiTakeGroup51/allOf/0/then/properties/visitSelections/items` | Context / conditional | properties: 1 entries (see descendant pointers) |  |
| `/$defs/midiTakeGroup51/allOf/0/then/properties/visitSelections/items/properties/compId` | No | type: "null" |  |
| `/$defs/midiTakeGroup51/allOf/0/then/properties/liveSelection` | No | properties: 1 entries (see descendant pointers) |  |
| `/$defs/midiTakeGroup51/allOf/0/then/properties/liveSelection/properties/mode` | No | enum: ["fixed","manual"] |  |

## ostf-production-session-0.4.schema.json

| Schema Pointer | Required in direct parent | Constraints | Original description |
|---|---|---|---|
| `/` | Context / conditional | $schema: "https://json-schema.org/draft/2020-12/schema"; $id: "https://yoh-nak.github.io/ostf/schema/ostf-production-session-0.4.schema.json"; type: "object"; additionalProperties: false; properties: 12 entries (see descendant pointers); required: ["profile","profileVersion","score","channels"]; $defs: 28 entries (see descendant pointers) | Complete Production 0.4, pinned to exact Score 5.1.0 bytes. Inherits Production 0.3 channels, devices, assets, automation and Audio Regions, and adds optional non-destructive Audio Take Groups. |
| `/properties/profile` | Yes | const: "OSTF-Production-Session" |  |
| `/properties/profileVersion` | Yes | const: "0.4.0" |  |
| `/properties/score` | Yes | $ref: "#/$defs/score" |  |
| `/properties/channels` | Yes | type: "array"; items: 1 entries (see descendant pointers); minItems: 1 |  |
| `/properties/channels/items` | Context / conditional | $ref: "#/$defs/channel" |  |
| `/properties/devices` | No | type: "array"; items: 1 entries (see descendant pointers); minItems: 0 |  |
| `/properties/devices/items` | Context / conditional | $ref: "#/$defs/device" |  |
| `/properties/assets` | No | type: "array"; items: 1 entries (see descendant pointers); minItems: 0 |  |
| `/properties/assets/items` | Context / conditional | $ref: "#/$defs/asset" |  |
| `/properties/automation` | No | type: "array"; items: 1 entries (see descendant pointers); minItems: 0 |  |
| `/properties/automation/items` | Context / conditional | $ref: "#/$defs/automation" |  |
| `/properties/notes` | No | type: "string" |  |
| `/properties/hostExtensions` | No | type: "array"; items: 1 entries (see descendant pointers) |  |
| `/properties/hostExtensions/items` | Context / conditional | $ref: "#/$defs/hostExtension" |  |
| `/properties/audioRegions` | No | type: "array"; items: 1 entries (see descendant pointers); minItems: 0 | Optional authored audio-region arrangement in source-score global Tick time. Does not modify OSTF Core Clips/Notes. |
| `/properties/audioRegions/items` | Context / conditional | $ref: "#/$defs/audioRegion" |  |
| `/properties/sidechainConnections` | No | type: "array"; items: 1 entries (see descendant pointers); minItems: 0 | Optional typed, acyclic audio detector/key inputs to effect plugin ports; not part of normal audible output routing. |
| `/properties/sidechainConnections/items` | Context / conditional | $ref: "#/$defs/sidechainConnection" |  |
| `/properties/audioTakeGroups` | No | type: "array"; items: 1 entries (see descendant pointers) |  |
| `/properties/audioTakeGroups/items` | Context / conditional | $ref: "#/$defs/audioTakeGroup51" |  |
| `/$defs/id` | Context / conditional | type: "string"; minLength: 1; pattern: "^\\S+$" |  |
| `/$defs/sha256` | Context / conditional | type: "string"; pattern: "^[0-9a-f]{64}$" |  |
| `/$defs/score` | Context / conditional | type: "object"; properties: 5 entries (see descendant pointers); required: ["formatVersion","sha256"]; additionalProperties: false |  |
| `/$defs/score/properties/formatVersion` | Yes | const: "5.1.0" |  |
| `/$defs/score/properties/sha256` | Yes | $ref: "#/$defs/sha256" |  |
| `/$defs/score/properties/documentId` | No | $ref: "#/$defs/id" |  |
| `/$defs/score/properties/revisionId` | No | $ref: "#/$defs/id" |  |
| `/$defs/score/properties/sourceUri` | No | type: "string"; minLength: 1 |  |
| `/$defs/channel` | Context / conditional | type: "object"; properties: 13 entries (see descendant pointers); required: ["id","kind","audioChannels","gainDb","pan","mute","solo","soloSafe","deviceIds"]; additionalProperties: false |  |
| `/$defs/channel/properties/id` | Yes | $ref: "#/$defs/id" |  |
| `/$defs/channel/properties/kind` | Yes | enum: ["track","audioTrack","bus","master"] | audioTrack is a production-only recorded-audio channel, and MUST NOT claim a Core trackId. kind track still maps an OSTF Track exactly as in 0.1. |
| `/$defs/channel/properties/name` | No | type: "string"; minLength: 1 |  |
| `/$defs/channel/properties/trackId` | No | $ref: "#/$defs/id" |  |
| `/$defs/channel/properties/audioChannels` | Yes | enum: [1,2] |  |
| `/$defs/channel/properties/gainDb` | Yes | type: "number"; minimum: -120; maximum: 24 |  |
| `/$defs/channel/properties/pan` | Yes | type: "number"; minimum: -1; maximum: 1 |  |
| `/$defs/channel/properties/mute` | Yes | type: "boolean" |  |
| `/$defs/channel/properties/solo` | Yes | type: "boolean" |  |
| `/$defs/channel/properties/soloSafe` | Yes | type: "boolean" |  |
| `/$defs/channel/properties/outputChannelId` | No | $ref: "#/$defs/id" |  |
| `/$defs/channel/properties/deviceIds` | Yes | type: "array"; items: 1 entries (see descendant pointers); minItems: 0; uniqueItems: true |  |
| `/$defs/channel/properties/deviceIds/items` | Context / conditional | $ref: "#/$defs/id" |  |
| `/$defs/channel/properties/sends` | No | type: "array"; items: 1 entries (see descendant pointers); minItems: 0 |  |
| `/$defs/channel/properties/sends/items` | Context / conditional | $ref: "#/$defs/send" |  |
| `/$defs/send` | Context / conditional | type: "object"; properties: 5 entries (see descendant pointers); required: ["id","targetChannelId","gainDb","preFader","enabled"]; additionalProperties: false |  |
| `/$defs/send/properties/id` | Yes | $ref: "#/$defs/id" |  |
| `/$defs/send/properties/targetChannelId` | Yes | $ref: "#/$defs/id" |  |
| `/$defs/send/properties/gainDb` | Yes | type: "number"; minimum: -120; maximum: 24 |  |
| `/$defs/send/properties/preFader` | Yes | type: "boolean" |  |
| `/$defs/send/properties/enabled` | Yes | type: "boolean" |  |
| `/$defs/device` | Context / conditional | type: "object"; properties: 7 entries (see descendant pointers); required: ["id","role","plugin","enabled","bypass"]; additionalProperties: false |  |
| `/$defs/device/properties/id` | Yes | $ref: "#/$defs/id" |  |
| `/$defs/device/properties/role` | Yes | enum: ["instrument","effect","utility"] |  |
| `/$defs/device/properties/plugin` | Yes | $ref: "#/$defs/plugin" |  |
| `/$defs/device/properties/enabled` | Yes | type: "boolean" |  |
| `/$defs/device/properties/bypass` | Yes | type: "boolean" |  |
| `/$defs/device/properties/stateAssetId` | No | $ref: "#/$defs/id" |  |
| `/$defs/device/properties/onUnavailable` | No | enum: ["reportAndPreserve","preserveAndBypass","preserveAndSilence"] |  |
| `/$defs/plugin` | Context / conditional | type: "object"; properties: 6 entries (see descendant pointers); required: ["format","pluginId","name"]; additionalProperties: false |  |
| `/$defs/plugin/properties/format` | Yes | enum: ["vst2","vst3","clap","au","aax","builtin","hostNative","other"] |  |
| `/$defs/plugin/properties/pluginId` | Yes | type: "string"; minLength: 1 |  |
| `/$defs/plugin/properties/vendor` | No | type: "string"; minLength: 1 |  |
| `/$defs/plugin/properties/name` | Yes | type: "string"; minLength: 1 |  |
| `/$defs/plugin/properties/version` | No | type: "string"; minLength: 1 |  |
| `/$defs/plugin/properties/namespace` | No | type: "string"; minLength: 1 |  |
| `/$defs/asset` | Context / conditional | type: "object"; properties: 9 entries (see descendant pointers); required: ["id","purpose","uri","sha256"]; additionalProperties: false; allOf: 1 branches (see descendant pointers) | Opaque asset descriptors. audioSource requires sampling metadata for frame-accurate regions; plug-in state remains uninterpreted and never executable merely by presence in JSON. |
| `/$defs/asset/properties/id` | Yes | $ref: "#/$defs/id" |  |
| `/$defs/asset/properties/purpose` | Yes | enum: ["pluginState","renderedAudio","other","audioSource"] |  |
| `/$defs/asset/properties/uri` | Yes | type: "string"; minLength: 1 |  |
| `/$defs/asset/properties/sha256` | Yes | $ref: "#/$defs/sha256" |  |
| `/$defs/asset/properties/mediaType` | No | type: "string"; minLength: 1 |  |
| `/$defs/asset/properties/byteLength` | No | type: "integer"; minimum: 0 |  |
| `/$defs/asset/properties/sampleRateHz` | No | type: "integer"; minimum: 1; maximum: 768000 | Audio-source decoded sample frames per second; required only for purpose audioSource. |
| `/$defs/asset/properties/frameCount` | No | type: "integer"; minimum: 1; maximum: 9007199254740991 | Number of decoded sample frames in the complete audio source asset; required for audioSource. |
| `/$defs/asset/properties/audioChannels` | No | type: "integer"; enum: [1,2] | Mono/stereo decoded source-channel count; required only for audioSource in 0.2. |
| `/$defs/asset/allOf/0` | Context / conditional | if: 2 entries (see descendant pointers); then: 1 entries (see descendant pointers); else: 1 entries (see descendant pointers) |  |
| `/$defs/asset/allOf/0/if` | Context / conditional | properties: 1 entries (see descendant pointers); required: ["purpose"] |  |
| `/$defs/asset/allOf/0/if/properties/purpose` | Yes | const: "audioSource" |  |
| `/$defs/asset/allOf/0/then` | Context / conditional | required: ["sampleRateHz","frameCount","audioChannels","mediaType"] |  |
| `/$defs/asset/allOf/0/else` | Context / conditional | not: 1 entries (see descendant pointers) |  |
| `/$defs/asset/allOf/0/else/not` | Context / conditional | anyOf: 3 branches (see descendant pointers) |  |
| `/$defs/asset/allOf/0/else/not/anyOf/0` | Context / conditional | required: ["sampleRateHz"] |  |
| `/$defs/asset/allOf/0/else/not/anyOf/1` | Context / conditional | required: ["frameCount"] |  |
| `/$defs/asset/allOf/0/else/not/anyOf/2` | Context / conditional | required: ["audioChannels"] |  |
| `/$defs/automation` | Context / conditional | type: "object"; properties: 5 entries (see descendant pointers); required: ["id","target","valueType","interpolation","points"]; additionalProperties: false; allOf: 14 branches (see descendant pointers) | Unique source-global-Tick automation lane. Boolean controls use step interpolation. A single lane per exact target; static value acts as baseline before first point where available. Device plugin parameters are normalized 0..1, while deviceControl.enabled/bypass are explicit booleans. Draft 0.8 adds exact numeric domain constraints (Channel/Send/Region dB, Pan, normalized Plugin Parameter), and boolean target type enforcement. |
| `/$defs/automation/properties/id` | Yes | $ref: "#/$defs/id" |  |
| `/$defs/automation/properties/target` | Yes | $ref: "#/$defs/automationTarget" |  |
| `/$defs/automation/properties/valueType` | Yes | enum: ["number","boolean"] |  |
| `/$defs/automation/properties/interpolation` | Yes | enum: ["step","linear"] |  |
| `/$defs/automation/properties/points` | Yes | type: "array"; items: 1 entries (see descendant pointers); minItems: 1 |  |
| `/$defs/automation/properties/points/items` | Context / conditional | $ref: "#/$defs/point" |  |
| `/$defs/automation/allOf/0` | Context / conditional | if: 2 entries (see descendant pointers); then: 1 entries (see descendant pointers) |  |
| `/$defs/automation/allOf/0/if` | Context / conditional | properties: 1 entries (see descendant pointers); required: ["valueType"] |  |
| `/$defs/automation/allOf/0/if/properties/valueType` | Yes | const: "boolean" |  |
| `/$defs/automation/allOf/0/then` | Context / conditional | properties: 1 entries (see descendant pointers) |  |
| `/$defs/automation/allOf/0/then/properties/interpolation` | No | const: "step" |  |
| `/$defs/automation/allOf/1` | Context / conditional | if: 2 entries (see descendant pointers); then: 1 entries (see descendant pointers) |  |
| `/$defs/automation/allOf/1/if` | Context / conditional | properties: 1 entries (see descendant pointers); required: ["valueType"] |  |
| `/$defs/automation/allOf/1/if/properties/valueType` | Yes | const: "boolean" |  |
| `/$defs/automation/allOf/1/then` | Context / conditional | properties: 2 entries (see descendant pointers) |  |
| `/$defs/automation/allOf/1/then/properties/interpolation` | No | const: "step" |  |
| `/$defs/automation/allOf/1/then/properties/points` | No | type: "array"; items: 4 entries (see descendant pointers) |  |
| `/$defs/automation/allOf/1/then/properties/points/items` | Context / conditional | type: "object"; properties: 2 entries (see descendant pointers); required: ["atTick","value"]; additionalProperties: false |  |
| `/$defs/automation/allOf/1/then/properties/points/items/properties/value` | Yes | type: "boolean" |  |
| `/$defs/automation/allOf/1/then/properties/points/items/properties/atTick` | Yes | type: "integer"; minimum: 0; maximum: 9007199254740991 |  |
| `/$defs/automation/allOf/2` | Context / conditional | if: 2 entries (see descendant pointers); then: 1 entries (see descendant pointers) |  |
| `/$defs/automation/allOf/2/if` | Context / conditional | properties: 1 entries (see descendant pointers); required: ["valueType"] |  |
| `/$defs/automation/allOf/2/if/properties/valueType` | Yes | const: "number" |  |
| `/$defs/automation/allOf/2/then` | Context / conditional | properties: 1 entries (see descendant pointers) |  |
| `/$defs/automation/allOf/2/then/properties/points` | No | type: "array"; items: 2 entries (see descendant pointers) |  |
| `/$defs/automation/allOf/2/then/properties/points/items` | Context / conditional | properties: 1 entries (see descendant pointers); required: ["value"] |  |
| `/$defs/automation/allOf/2/then/properties/points/items/properties/value` | Yes | type: "number" |  |
| `/$defs/automation/allOf/3` | Context / conditional | if: 2 entries (see descendant pointers); then: 1 entries (see descendant pointers) |  |
| `/$defs/automation/allOf/3/if` | Context / conditional | properties: 1 entries (see descendant pointers); required: ["target"] |  |
| `/$defs/automation/allOf/3/if/properties/target` | Yes | properties: 2 entries (see descendant pointers); required: ["kind","parameter"] |  |
| `/$defs/automation/allOf/3/if/properties/target/properties/kind` | Yes | const: "channel" |  |
| `/$defs/automation/allOf/3/if/properties/target/properties/parameter` | Yes | const: "mute" |  |
| `/$defs/automation/allOf/3/then` | Context / conditional | properties: 1 entries (see descendant pointers) |  |
| `/$defs/automation/allOf/3/then/properties/valueType` | No | const: "boolean" |  |
| `/$defs/automation/allOf/4` | Context / conditional | if: 2 entries (see descendant pointers); then: 1 entries (see descendant pointers) |  |
| `/$defs/automation/allOf/4/if` | Context / conditional | properties: 1 entries (see descendant pointers); required: ["target"] |  |
| `/$defs/automation/allOf/4/if/properties/target` | Yes | properties: 2 entries (see descendant pointers); required: ["kind","parameter"] |  |
| `/$defs/automation/allOf/4/if/properties/target/properties/kind` | Yes | const: "send" |  |
| `/$defs/automation/allOf/4/if/properties/target/properties/parameter` | Yes | const: "enabled" |  |
| `/$defs/automation/allOf/4/then` | Context / conditional | properties: 1 entries (see descendant pointers) |  |
| `/$defs/automation/allOf/4/then/properties/valueType` | No | const: "boolean" |  |
| `/$defs/automation/allOf/5` | Context / conditional | if: 2 entries (see descendant pointers); then: 1 entries (see descendant pointers) |  |
| `/$defs/automation/allOf/5/if` | Context / conditional | properties: 1 entries (see descendant pointers); required: ["target"] |  |
| `/$defs/automation/allOf/5/if/properties/target` | Yes | properties: 2 entries (see descendant pointers); required: ["kind","parameter"] |  |
| `/$defs/automation/allOf/5/if/properties/target/properties/kind` | Yes | const: "audioRegion" |  |
| `/$defs/automation/allOf/5/if/properties/target/properties/parameter` | Yes | const: "mute" |  |
| `/$defs/automation/allOf/5/then` | Context / conditional | properties: 1 entries (see descendant pointers) |  |
| `/$defs/automation/allOf/5/then/properties/valueType` | No | const: "boolean" |  |
| `/$defs/automation/allOf/6` | Context / conditional | if: 2 entries (see descendant pointers); then: 1 entries (see descendant pointers) |  |
| `/$defs/automation/allOf/6/if` | Context / conditional | properties: 1 entries (see descendant pointers); required: ["target"] |  |
| `/$defs/automation/allOf/6/if/properties/target` | Yes | properties: 2 entries (see descendant pointers); required: ["kind","parameter"] |  |
| `/$defs/automation/allOf/6/if/properties/target/properties/kind` | Yes | const: "deviceControl" |  |
| `/$defs/automation/allOf/6/if/properties/target/properties/parameter` | Yes | const: "enabled" |  |
| `/$defs/automation/allOf/6/then` | Context / conditional | properties: 1 entries (see descendant pointers) |  |
| `/$defs/automation/allOf/6/then/properties/valueType` | No | const: "boolean" |  |
| `/$defs/automation/allOf/7` | Context / conditional | if: 2 entries (see descendant pointers); then: 1 entries (see descendant pointers) |  |
| `/$defs/automation/allOf/7/if` | Context / conditional | properties: 1 entries (see descendant pointers); required: ["target"] |  |
| `/$defs/automation/allOf/7/if/properties/target` | Yes | properties: 2 entries (see descendant pointers); required: ["kind","parameter"] |  |
| `/$defs/automation/allOf/7/if/properties/target/properties/kind` | Yes | const: "deviceControl" |  |
| `/$defs/automation/allOf/7/if/properties/target/properties/parameter` | Yes | const: "bypass" |  |
| `/$defs/automation/allOf/7/then` | Context / conditional | properties: 1 entries (see descendant pointers) |  |
| `/$defs/automation/allOf/7/then/properties/valueType` | No | const: "boolean" |  |
| `/$defs/automation/allOf/8` | Context / conditional | if: 2 entries (see descendant pointers); then: 1 entries (see descendant pointers) |  |
| `/$defs/automation/allOf/8/if` | Context / conditional | properties: 1 entries (see descendant pointers); required: ["target"] |  |
| `/$defs/automation/allOf/8/if/properties/target` | Yes | properties: 1 entries (see descendant pointers); required: ["kind"] |  |
| `/$defs/automation/allOf/8/if/properties/target/properties/kind` | Yes | const: "device" |  |
| `/$defs/automation/allOf/8/then` | Context / conditional | properties: 1 entries (see descendant pointers) |  |
| `/$defs/automation/allOf/8/then/properties/valueType` | No | const: "number" |  |
| `/$defs/automation/allOf/9` | Context / conditional | if: 2 entries (see descendant pointers); then: 1 entries (see descendant pointers) |  |
| `/$defs/automation/allOf/9/if` | Context / conditional | properties: 1 entries (see descendant pointers); required: ["target"] |  |
| `/$defs/automation/allOf/9/if/properties/target` | Yes | properties: 2 entries (see descendant pointers); required: ["kind","parameter"] |  |
| `/$defs/automation/allOf/9/if/properties/target/properties/kind` | Yes | const: "channel" |  |
| `/$defs/automation/allOf/9/if/properties/target/properties/parameter` | Yes | const: "gainDb" |  |
| `/$defs/automation/allOf/9/then` | Context / conditional | properties: 2 entries (see descendant pointers) |  |
| `/$defs/automation/allOf/9/then/properties/valueType` | No | const: "number" |  |
| `/$defs/automation/allOf/9/then/properties/points` | No | items: 1 entries (see descendant pointers) |  |
| `/$defs/automation/allOf/9/then/properties/points/items` | Context / conditional | properties: 1 entries (see descendant pointers) |  |
| `/$defs/automation/allOf/9/then/properties/points/items/properties/value` | No | type: "number"; minimum: -120; maximum: 24 |  |
| `/$defs/automation/allOf/10` | Context / conditional | if: 2 entries (see descendant pointers); then: 1 entries (see descendant pointers) |  |
| `/$defs/automation/allOf/10/if` | Context / conditional | properties: 1 entries (see descendant pointers); required: ["target"] |  |
| `/$defs/automation/allOf/10/if/properties/target` | Yes | properties: 2 entries (see descendant pointers); required: ["kind","parameter"] |  |
| `/$defs/automation/allOf/10/if/properties/target/properties/kind` | Yes | const: "channel" |  |
| `/$defs/automation/allOf/10/if/properties/target/properties/parameter` | Yes | const: "pan" |  |
| `/$defs/automation/allOf/10/then` | Context / conditional | properties: 2 entries (see descendant pointers) |  |
| `/$defs/automation/allOf/10/then/properties/valueType` | No | const: "number" |  |
| `/$defs/automation/allOf/10/then/properties/points` | No | items: 1 entries (see descendant pointers) |  |
| `/$defs/automation/allOf/10/then/properties/points/items` | Context / conditional | properties: 1 entries (see descendant pointers) |  |
| `/$defs/automation/allOf/10/then/properties/points/items/properties/value` | No | type: "number"; minimum: -1; maximum: 1 |  |
| `/$defs/automation/allOf/11` | Context / conditional | if: 2 entries (see descendant pointers); then: 1 entries (see descendant pointers) |  |
| `/$defs/automation/allOf/11/if` | Context / conditional | properties: 1 entries (see descendant pointers); required: ["target"] |  |
| `/$defs/automation/allOf/11/if/properties/target` | Yes | properties: 2 entries (see descendant pointers); required: ["kind","parameter"] |  |
| `/$defs/automation/allOf/11/if/properties/target/properties/kind` | Yes | const: "send" |  |
| `/$defs/automation/allOf/11/if/properties/target/properties/parameter` | Yes | const: "gainDb" |  |
| `/$defs/automation/allOf/11/then` | Context / conditional | properties: 2 entries (see descendant pointers) |  |
| `/$defs/automation/allOf/11/then/properties/valueType` | No | const: "number" |  |
| `/$defs/automation/allOf/11/then/properties/points` | No | items: 1 entries (see descendant pointers) |  |
| `/$defs/automation/allOf/11/then/properties/points/items` | Context / conditional | properties: 1 entries (see descendant pointers) |  |
| `/$defs/automation/allOf/11/then/properties/points/items/properties/value` | No | type: "number"; minimum: -120; maximum: 24 |  |
| `/$defs/automation/allOf/12` | Context / conditional | if: 2 entries (see descendant pointers); then: 1 entries (see descendant pointers) |  |
| `/$defs/automation/allOf/12/if` | Context / conditional | properties: 1 entries (see descendant pointers); required: ["target"] |  |
| `/$defs/automation/allOf/12/if/properties/target` | Yes | properties: 2 entries (see descendant pointers); required: ["kind","parameter"] |  |
| `/$defs/automation/allOf/12/if/properties/target/properties/kind` | Yes | const: "audioRegion" |  |
| `/$defs/automation/allOf/12/if/properties/target/properties/parameter` | Yes | const: "gainDb" |  |
| `/$defs/automation/allOf/12/then` | Context / conditional | properties: 2 entries (see descendant pointers) |  |
| `/$defs/automation/allOf/12/then/properties/valueType` | No | const: "number" |  |
| `/$defs/automation/allOf/12/then/properties/points` | No | items: 1 entries (see descendant pointers) |  |
| `/$defs/automation/allOf/12/then/properties/points/items` | Context / conditional | properties: 1 entries (see descendant pointers) |  |
| `/$defs/automation/allOf/12/then/properties/points/items/properties/value` | No | type: "number"; minimum: -120; maximum: 24 |  |
| `/$defs/automation/allOf/13` | Context / conditional | if: 2 entries (see descendant pointers); then: 1 entries (see descendant pointers) |  |
| `/$defs/automation/allOf/13/if` | Context / conditional | properties: 1 entries (see descendant pointers); required: ["target"] |  |
| `/$defs/automation/allOf/13/if/properties/target` | Yes | properties: 1 entries (see descendant pointers); required: ["kind"] |  |
| `/$defs/automation/allOf/13/if/properties/target/properties/kind` | Yes | const: "device" |  |
| `/$defs/automation/allOf/13/then` | Context / conditional | properties: 2 entries (see descendant pointers) |  |
| `/$defs/automation/allOf/13/then/properties/valueType` | No | const: "number" |  |
| `/$defs/automation/allOf/13/then/properties/points` | No | items: 1 entries (see descendant pointers) |  |
| `/$defs/automation/allOf/13/then/properties/points/items` | Context / conditional | properties: 1 entries (see descendant pointers) |  |
| `/$defs/automation/allOf/13/then/properties/points/items/properties/value` | No | type: "number"; minimum: 0; maximum: 1 |  |
| `/$defs/automationTarget` | Context / conditional | oneOf: 5 branches (see descendant pointers) | Channel, plugin parameter, Send, audio Region, or Device slot control automation target. Non-channel options added to the unpublished 0.2 development draft. References resolve within this Production Profile, not into MIDI CC or Core Note IDs. |
| `/$defs/automationTarget/oneOf/0` | Context / conditional | type: "object"; properties: 3 entries (see descendant pointers); required: ["kind","channelId","parameter"]; additionalProperties: false |  |
| `/$defs/automationTarget/oneOf/0/properties/kind` | Yes | const: "channel" |  |
| `/$defs/automationTarget/oneOf/0/properties/channelId` | Yes | $ref: "#/$defs/id" |  |
| `/$defs/automationTarget/oneOf/0/properties/parameter` | Yes | enum: ["gainDb","pan","mute"] |  |
| `/$defs/automationTarget/oneOf/1` | Context / conditional | type: "object"; properties: 3 entries (see descendant pointers); required: ["kind","deviceId","parameterId"]; additionalProperties: false |  |
| `/$defs/automationTarget/oneOf/1/properties/kind` | Yes | const: "device" |  |
| `/$defs/automationTarget/oneOf/1/properties/deviceId` | Yes | $ref: "#/$defs/id" |  |
| `/$defs/automationTarget/oneOf/1/properties/parameterId` | Yes | type: "string"; minLength: 1 |  |
| `/$defs/automationTarget/oneOf/2` | Context / conditional | type: "object"; additionalProperties: false; properties: 3 entries (see descendant pointers); required: ["kind","sendId","parameter"] |  |
| `/$defs/automationTarget/oneOf/2/properties/kind` | Yes | const: "send" |  |
| `/$defs/automationTarget/oneOf/2/properties/sendId` | Yes | $ref: "#/$defs/id" |  |
| `/$defs/automationTarget/oneOf/2/properties/parameter` | Yes | enum: ["gainDb","enabled"] |  |
| `/$defs/automationTarget/oneOf/3` | Context / conditional | type: "object"; additionalProperties: false; properties: 3 entries (see descendant pointers); required: ["kind","audioRegionId","parameter"] |  |
| `/$defs/automationTarget/oneOf/3/properties/kind` | Yes | const: "audioRegion" |  |
| `/$defs/automationTarget/oneOf/3/properties/audioRegionId` | Yes | $ref: "#/$defs/id" |  |
| `/$defs/automationTarget/oneOf/3/properties/parameter` | Yes | enum: ["gainDb","mute"] |  |
| `/$defs/automationTarget/oneOf/4` | Context / conditional | type: "object"; additionalProperties: false; properties: 3 entries (see descendant pointers); required: ["kind","deviceId","parameter"] |  |
| `/$defs/automationTarget/oneOf/4/properties/kind` | Yes | const: "deviceControl" |  |
| `/$defs/automationTarget/oneOf/4/properties/deviceId` | Yes | $ref: "#/$defs/id" |  |
| `/$defs/automationTarget/oneOf/4/properties/parameter` | Yes | enum: ["enabled","bypass"] |  |
| `/$defs/point` | Context / conditional | type: "object"; properties: 2 entries (see descendant pointers); required: ["atTick","value"]; additionalProperties: false |  |
| `/$defs/point/properties/atTick` | Yes | type: "integer"; minimum: 0; maximum: 9007199254740991 |  |
| `/$defs/point/properties/value` | Yes | oneOf: 2 branches (see descendant pointers) |  |
| `/$defs/point/properties/value/oneOf/0` | Context / conditional | type: "number" |  |
| `/$defs/point/properties/value/oneOf/1` | Context / conditional | type: "boolean" |  |
| `/$defs/hostExtension` | Context / conditional | type: "object"; properties: 3 entries (see descendant pointers); required: ["namespace","data"]; additionalProperties: false |  |
| `/$defs/hostExtension/properties/namespace` | Yes | type: "string"; pattern: "^[A-Za-z0-9]+(?:\\.[A-Za-z0-9-]+)+$" |  |
| `/$defs/hostExtension/properties/version` | No | type: "string"; minLength: 1 |  |
| `/$defs/hostExtension/properties/data` | Yes | type: "object" |  |
| `/$defs/audioRegion` | Context / conditional | type: "object"; additionalProperties: false; properties: 13 entries (see descendant pointers); required: ["id","channelId","sourceAssetId","startTick","durationTicks","sourceStartFrame","sourceFrameCount","playbackMode","gainDb","mute"]; allOf: 1 branches (see descendant pointers) | Source-score-tick audio segment on a production track or score-bound track channel, referencing a bounded range of exact audioSource PCM-decoded frames. |
| `/$defs/audioRegion/properties/id` | Yes | $ref: "#/$defs/id" |  |
| `/$defs/audioRegion/properties/channelId` | Yes | $ref: "#/$defs/id" |  |
| `/$defs/audioRegion/properties/sourceAssetId` | Yes | $ref: "#/$defs/id" |  |
| `/$defs/audioRegion/properties/startTick` | Yes | type: "integer"; minimum: 0; maximum: 9007199254740991 |  |
| `/$defs/audioRegion/properties/durationTicks` | Yes | type: "integer"; minimum: 1; maximum: 9007199254740991 |  |
| `/$defs/audioRegion/properties/sourceStartFrame` | Yes | type: "integer"; minimum: 0; maximum: 9007199254740991 |  |
| `/$defs/audioRegion/properties/sourceFrameCount` | Yes | type: "integer"; minimum: 1; maximum: 9007199254740991 |  |
| `/$defs/audioRegion/properties/playbackMode` | Yes | enum: ["native","fit"] | native maps ideal source-time seconds to sample frames at sampleRateHz; fit uniformly maps authored global Tick progress to the selected frame interval. |
| `/$defs/audioRegion/properties/pitchPolicy` | No | enum: ["preserve","followRate"] | Required for fit; preserve means retain source pitch as a musical goal, followRate means speed/rate-based pitch change. Both are DSP/host dependent. |
| `/$defs/audioRegion/properties/gainDb` | Yes | type: "number"; minimum: -120; maximum: 24 |  |
| `/$defs/audioRegion/properties/mute` | Yes | type: "boolean" |  |
| `/$defs/audioRegion/properties/fadeInTicks` | No | type: "integer"; minimum: 0; maximum: 9007199254740991 |  |
| `/$defs/audioRegion/properties/fadeOutTicks` | No | type: "integer"; minimum: 0; maximum: 9007199254740991 |  |
| `/$defs/audioRegion/allOf/0` | Context / conditional | if: 2 entries (see descendant pointers); then: 1 entries (see descendant pointers); else: 1 entries (see descendant pointers) |  |
| `/$defs/audioRegion/allOf/0/if` | Context / conditional | properties: 1 entries (see descendant pointers); required: ["playbackMode"] |  |
| `/$defs/audioRegion/allOf/0/if/properties/playbackMode` | Yes | const: "fit" |  |
| `/$defs/audioRegion/allOf/0/then` | Context / conditional | required: ["pitchPolicy"] |  |
| `/$defs/audioRegion/allOf/0/else` | Context / conditional | not: 1 entries (see descendant pointers) |  |
| `/$defs/audioRegion/allOf/0/else/not` | Context / conditional | required: ["pitchPolicy"] |  |
| `/$defs/sidechainConnection` | Context / conditional | type: "object"; additionalProperties: false; properties: 8 entries (see descendant pointers); required: ["id","sourceChannelId","targetDeviceId","targetPortId","tapPoint","followMute","gainDb","enabled"] | Directed detector/key signal from sourceChannelId to named key input port of an effect Device belonging to a different audio channel. Does not mix into its audible output path. |
| `/$defs/sidechainConnection/properties/id` | Yes | $ref: "#/$defs/id" |  |
| `/$defs/sidechainConnection/properties/sourceChannelId` | Yes | $ref: "#/$defs/id" |  |
| `/$defs/sidechainConnection/properties/targetDeviceId` | Yes | $ref: "#/$defs/id" |  |
| `/$defs/sidechainConnection/properties/targetPortId` | Yes | $ref: "#/$defs/id" | Opaque plugin-format-scoped sidechain input identifier. A host must verify the port actually exists; no port auto-matching by label. |
| `/$defs/sidechainConnection/properties/tapPoint` | Yes | enum: ["preFader","postFader"] |  |
| `/$defs/sidechainConnection/properties/followMute` | Yes | type: "boolean" | If true, source channel mute suppresses this sidechain; if false, the detector feed can remain present even when that source channel is muted audibly. |
| `/$defs/sidechainConnection/properties/gainDb` | Yes | type: "number"; minimum: -120; maximum: 24 |  |
| `/$defs/sidechainConnection/properties/enabled` | Yes | type: "boolean" |  |
| `/$defs/takeId51` | Context / conditional | type: "string"; pattern: "^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$"; not: 1 entries (see descendant pointers) |  |
| `/$defs/takeId51/not` | Context / conditional | pattern: "[\\r\\n\\u2028\\u2029]" |  |
| `/$defs/takeTick51` | Context / conditional | type: "integer"; minimum: 0; maximum: 9007199254740991 |  |
| `/$defs/takeDuration51` | Context / conditional | type: "integer"; minimum: 1; maximum: 9007199254740991 |  |
| `/$defs/takeOrigin51` | Context / conditional | type: "object"; additionalProperties: false; properties: 10 entries (see descendant pointers); required: ["kind"] | Optional inert provenance. Actor/session/proposal identifiers and prompts do not confer permissions or perform any network or generation action. |
| `/$defs/takeOrigin51/properties/kind` | Yes | enum: ["human","ai","import","derived","unknown"] |  |
| `/$defs/takeOrigin51/properties/actorId` | No | type: "string"; pattern: "^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$"; not: 1 entries (see descendant pointers) |  |
| `/$defs/takeOrigin51/properties/actorId/not` | Context / conditional | pattern: "[\\r\\n\\u2028\\u2029]" |  |
| `/$defs/takeOrigin51/properties/participantId` | No | type: "string"; pattern: "^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$"; not: 1 entries (see descendant pointers) |  |
| `/$defs/takeOrigin51/properties/participantId/not` | Context / conditional | pattern: "[\\r\\n\\u2028\\u2029]" |  |
| `/$defs/takeOrigin51/properties/sessionId` | No | type: "string"; pattern: "^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$"; not: 1 entries (see descendant pointers) |  |
| `/$defs/takeOrigin51/properties/sessionId/not` | Context / conditional | pattern: "[\\r\\n\\u2028\\u2029]" |  |
| `/$defs/takeOrigin51/properties/proposalId` | No | type: "string"; pattern: "^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$"; not: 1 entries (see descendant pointers) |  |
| `/$defs/takeOrigin51/properties/proposalId/not` | Context / conditional | pattern: "[\\r\\n\\u2028\\u2029]" |  |
| `/$defs/takeOrigin51/properties/commitEventId` | No | type: "string"; pattern: "^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$"; not: 1 entries (see descendant pointers) |  |
| `/$defs/takeOrigin51/properties/commitEventId/not` | Context / conditional | pattern: "[\\r\\n\\u2028\\u2029]" |  |
| `/$defs/takeOrigin51/properties/prompt` | No | type: "string" |  |
| `/$defs/takeOrigin51/properties/createdAt` | No | type: "string"; format: "date-time" |  |
| `/$defs/takeOrigin51/properties/model` | No | type: "string" |  |
| `/$defs/takeOrigin51/properties/sourceUri` | No | type: "string" |  |
| `/$defs/takeRating51` | Context / conditional | type: "object"; additionalProperties: false; properties: 3 entries (see descendant pointers); required: ["evaluatorId","score"] |  |
| `/$defs/takeRating51/properties/evaluatorId` | Yes | type: "string"; pattern: "^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$"; not: 1 entries (see descendant pointers) |  |
| `/$defs/takeRating51/properties/evaluatorId/not` | Context / conditional | pattern: "[\\r\\n\\u2028\\u2029]" |  |
| `/$defs/takeRating51/properties/score` | Yes | type: "number"; minimum: 0; maximum: 1 |  |
| `/$defs/takeRating51/properties/comment` | No | type: "string" |  |
| `/$defs/takeVisitSelection51` | Context / conditional | type: "object"; additionalProperties: false; properties: 3 entries (see descendant pointers); required: ["performancePlanId","visitId","compId"] | Comp selection overlay for one existing finite Performance Plan Visit. The Plan/Visit pair must be unique per Group. null denotes silence. Only the Group/Visit source-range intersection is selected. |
| `/$defs/takeVisitSelection51/properties/performancePlanId` | Yes | type: "string"; pattern: "^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$"; not: 1 entries (see descendant pointers) |  |
| `/$defs/takeVisitSelection51/properties/performancePlanId/not` | Context / conditional | pattern: "[\\r\\n\\u2028\\u2029]" |  |
| `/$defs/takeVisitSelection51/properties/visitId` | Yes | type: "string"; pattern: "^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$"; not: 1 entries (see descendant pointers) |  |
| `/$defs/takeVisitSelection51/properties/visitId/not` | Context / conditional | pattern: "[\\r\\n\\u2028\\u2029]" |  |
| `/$defs/takeVisitSelection51/properties/compId` | Yes | anyOf: 2 branches (see descendant pointers) |  |
| `/$defs/takeVisitSelection51/properties/compId/anyOf/0` | Context / conditional | type: "string"; pattern: "^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$"; not: 1 entries (see descendant pointers) |  |
| `/$defs/takeVisitSelection51/properties/compId/anyOf/0/not` | Context / conditional | pattern: "[\\r\\n\\u2028\\u2029]" |  |
| `/$defs/takeVisitSelection51/properties/compId/anyOf/1` | Context / conditional | type: "null" |  |
| `/$defs/takeLiveCandidate51` | Context / conditional | type: "object"; additionalProperties: false; properties: 2 entries (see descendant pointers); required: ["compId"] |  |
| `/$defs/takeLiveCandidate51/properties/compId` | Yes | type: "string"; pattern: "^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$"; not: 1 entries (see descendant pointers) |  |
| `/$defs/takeLiveCandidate51/properties/compId/not` | Context / conditional | pattern: "[\\r\\n\\u2028\\u2029]" |  |
| `/$defs/takeLiveCandidate51/properties/weight` | No | type: "number"; minimum: 0 |  |
| `/$defs/takeSelectionHistory51` | Context / conditional | type: "object"; additionalProperties: false; properties: 5 entries (see descendant pointers); required: ["sequence","compId"] | Informational saved-selection history, strictly increasing in sequence within its Group. Historical deleted Comp IDs may be retained; history never changes current selection or playback. |
| `/$defs/takeSelectionHistory51/properties/sequence` | Yes | type: "integer"; minimum: 0; maximum: 9007199254740991 |  |
| `/$defs/takeSelectionHistory51/properties/compId` | Yes | anyOf: 2 branches (see descendant pointers) |  |
| `/$defs/takeSelectionHistory51/properties/compId/anyOf/0` | Context / conditional | type: "string"; pattern: "^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$"; not: 1 entries (see descendant pointers) |  |
| `/$defs/takeSelectionHistory51/properties/compId/anyOf/0/not` | Context / conditional | pattern: "[\\r\\n\\u2028\\u2029]" |  |
| `/$defs/takeSelectionHistory51/properties/compId/anyOf/1` | Context / conditional | type: "null" |  |
| `/$defs/takeSelectionHistory51/properties/actorId` | No | type: "string"; pattern: "^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$"; not: 1 entries (see descendant pointers) |  |
| `/$defs/takeSelectionHistory51/properties/actorId/not` | Context / conditional | pattern: "[\\r\\n\\u2028\\u2029]" |  |
| `/$defs/takeSelectionHistory51/properties/recordedAt` | No | type: "string"; format: "date-time" |  |
| `/$defs/takeSelectionHistory51/properties/reason` | No | type: "string" |  |
| `/$defs/takeTransition51` | Context / conditional | type: "object"; additionalProperties: false; properties: 4 entries (see descendant pointers); required: ["atTick","startTick","durationTicks","curve"] | Declared crossfade window strictly containing an adjacent different-source junction at atTick. Windows must be disjoint, inside the Group, and backed by both source handles. regions output supports linear only; equalPower/customRendered are already baked into rendered output and must not be reapplied. |
| `/$defs/takeTransition51/properties/atTick` | Yes | type: "integer"; minimum: 0; maximum: 9007199254740991 |  |
| `/$defs/takeTransition51/properties/startTick` | Yes | type: "integer"; minimum: 0; maximum: 9007199254740991 |  |
| `/$defs/takeTransition51/properties/durationTicks` | Yes | type: "integer"; minimum: 1; maximum: 9007199254740991 |  |
| `/$defs/takeTransition51/properties/curve` | Yes | enum: ["linear","equalPower","customRendered"] |  |
| `/$defs/takeLiveSelection51` | Context / conditional | type: "object"; additionalProperties: false; properties: 2 entries (see descendant pointers); required: ["mode"]; allOf: 2 branches (see descendant pointers) | Optional launch-time selection policy. fixed/manual have no candidates; cycle/random/weighted require distinct Comp IDs. weighted requires all nonnegative weights and at least one positive weight. Distinct compId values and reference resolution are semantic constraints. |
| `/$defs/takeLiveSelection51/properties/mode` | Yes | enum: ["fixed","manual","cycle","random","weighted"] |  |
| `/$defs/takeLiveSelection51/properties/candidates` | No | type: "array"; items: 1 entries (see descendant pointers); minItems: 1; uniqueItems: true |  |
| `/$defs/takeLiveSelection51/properties/candidates/items` | Context / conditional | $ref: "#/$defs/takeLiveCandidate51" |  |
| `/$defs/takeLiveSelection51/allOf/0` | Context / conditional | if: 2 entries (see descendant pointers); then: 1 entries (see descendant pointers); else: 1 entries (see descendant pointers) |  |
| `/$defs/takeLiveSelection51/allOf/0/if` | Context / conditional | properties: 1 entries (see descendant pointers); required: ["mode"] |  |
| `/$defs/takeLiveSelection51/allOf/0/if/properties/mode` | Yes | enum: ["cycle","random","weighted"] |  |
| `/$defs/takeLiveSelection51/allOf/0/then` | Context / conditional | required: ["candidates"] |  |
| `/$defs/takeLiveSelection51/allOf/0/else` | Context / conditional | not: 1 entries (see descendant pointers) |  |
| `/$defs/takeLiveSelection51/allOf/0/else/not` | Context / conditional | required: ["candidates"] |  |
| `/$defs/takeLiveSelection51/allOf/1` | Context / conditional | if: 2 entries (see descendant pointers); then: 1 entries (see descendant pointers); else: 1 entries (see descendant pointers) |  |
| `/$defs/takeLiveSelection51/allOf/1/if` | Context / conditional | properties: 1 entries (see descendant pointers); required: ["mode"] |  |
| `/$defs/takeLiveSelection51/allOf/1/if/properties/mode` | Yes | const: "weighted" |  |
| `/$defs/takeLiveSelection51/allOf/1/then` | Context / conditional | properties: 1 entries (see descendant pointers) |  |
| `/$defs/takeLiveSelection51/allOf/1/then/properties/candidates` | No | items: 1 entries (see descendant pointers); contains: 3 entries (see descendant pointers); minContains: 1 |  |
| `/$defs/takeLiveSelection51/allOf/1/then/properties/candidates/items` | Context / conditional | required: ["weight"] |  |
| `/$defs/takeLiveSelection51/allOf/1/then/properties/candidates/contains` | Context / conditional | type: "object"; properties: 1 entries (see descendant pointers); required: ["weight"] |  |
| `/$defs/takeLiveSelection51/allOf/1/then/properties/candidates/contains/properties/weight` | Yes | type: "number"; exclusiveMinimum: 0 |  |
| `/$defs/takeLiveSelection51/allOf/1/else` | Context / conditional | properties: 1 entries (see descendant pointers) |  |
| `/$defs/takeLiveSelection51/allOf/1/else/properties/candidates` | No | items: 1 entries (see descendant pointers) |  |
| `/$defs/takeLiveSelection51/allOf/1/else/properties/candidates/items` | Context / conditional | not: 1 entries (see descendant pointers) |  |
| `/$defs/takeLiveSelection51/allOf/1/else/properties/candidates/items/not` | Context / conditional | required: ["weight"] |  |
| `/$defs/audioTake51` | Context / conditional | type: "object"; additionalProperties: false; properties: 8 entries (see descendant pointers); required: ["id","kind","audioRegionIds"] |  |
| `/$defs/audioTake51/properties/id` | Yes | type: "string"; pattern: "^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$"; not: 1 entries (see descendant pointers) |  |
| `/$defs/audioTake51/properties/id/not` | Context / conditional | pattern: "[\\r\\n\\u2028\\u2029]" |  |
| `/$defs/audioTake51/properties/name` | No | type: "string" |  |
| `/$defs/audioTake51/properties/kind` | Yes | enum: ["take","variation","alternative"] |  |
| `/$defs/audioTake51/properties/audioRegionIds` | Yes | type: "array"; items: 3 entries (see descendant pointers); minItems: 1; uniqueItems: true |  |
| `/$defs/audioTake51/properties/audioRegionIds/items` | Context / conditional | type: "string"; pattern: "^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$"; not: 1 entries (see descendant pointers) |  |
| `/$defs/audioTake51/properties/audioRegionIds/items/not` | Context / conditional | pattern: "[\\r\\n\\u2028\\u2029]" |  |
| `/$defs/audioTake51/properties/laneOrder` | No | type: "integer"; minimum: 0; maximum: 9007199254740991 |  |
| `/$defs/audioTake51/properties/parentTakeId` | No | type: "string"; pattern: "^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$"; not: 1 entries (see descendant pointers) |  |
| `/$defs/audioTake51/properties/parentTakeId/not` | Context / conditional | pattern: "[\\r\\n\\u2028\\u2029]" |  |
| `/$defs/audioTake51/properties/origin` | No | $ref: "#/$defs/takeOrigin51" |  |
| `/$defs/audioTake51/properties/ratings` | No | type: "array"; items: 1 entries (see descendant pointers); minItems: 0 |  |
| `/$defs/audioTake51/properties/ratings/items` | Context / conditional | $ref: "#/$defs/takeRating51" |  |
| `/$defs/audioCompRegion51` | Context / conditional | oneOf: 2 branches (see descendant pointers) |  |
| `/$defs/audioCompRegion51/oneOf/0` | Context / conditional | type: "object"; additionalProperties: false; properties: 6 entries (see descendant pointers); required: ["id","kind","startTick","durationTicks","takeId","audioRegionId"] |  |
| `/$defs/audioCompRegion51/oneOf/0/properties/id` | Yes | type: "string"; pattern: "^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$"; not: 1 entries (see descendant pointers) |  |
| `/$defs/audioCompRegion51/oneOf/0/properties/id/not` | Context / conditional | pattern: "[\\r\\n\\u2028\\u2029]" |  |
| `/$defs/audioCompRegion51/oneOf/0/properties/startTick` | Yes | type: "integer"; minimum: 0; maximum: 9007199254740991 |  |
| `/$defs/audioCompRegion51/oneOf/0/properties/durationTicks` | Yes | type: "integer"; minimum: 1; maximum: 9007199254740991 |  |
| `/$defs/audioCompRegion51/oneOf/0/properties/kind` | Yes | const: "source" |  |
| `/$defs/audioCompRegion51/oneOf/0/properties/takeId` | Yes | type: "string"; pattern: "^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$"; not: 1 entries (see descendant pointers) |  |
| `/$defs/audioCompRegion51/oneOf/0/properties/takeId/not` | Context / conditional | pattern: "[\\r\\n\\u2028\\u2029]" |  |
| `/$defs/audioCompRegion51/oneOf/0/properties/audioRegionId` | Yes | type: "string"; pattern: "^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$"; not: 1 entries (see descendant pointers) |  |
| `/$defs/audioCompRegion51/oneOf/0/properties/audioRegionId/not` | Context / conditional | pattern: "[\\r\\n\\u2028\\u2029]" |  |
| `/$defs/audioCompRegion51/oneOf/1` | Context / conditional | type: "object"; additionalProperties: false; properties: 4 entries (see descendant pointers); required: ["id","kind","startTick","durationTicks"] |  |
| `/$defs/audioCompRegion51/oneOf/1/properties/id` | Yes | type: "string"; pattern: "^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$"; not: 1 entries (see descendant pointers) |  |
| `/$defs/audioCompRegion51/oneOf/1/properties/id/not` | Context / conditional | pattern: "[\\r\\n\\u2028\\u2029]" |  |
| `/$defs/audioCompRegion51/oneOf/1/properties/startTick` | Yes | type: "integer"; minimum: 0; maximum: 9007199254740991 |  |
| `/$defs/audioCompRegion51/oneOf/1/properties/durationTicks` | Yes | type: "integer"; minimum: 1; maximum: 9007199254740991 |  |
| `/$defs/audioCompRegion51/oneOf/1/properties/kind` | Yes | const: "silence" |  |
| `/$defs/audioComp51` | Context / conditional | type: "object"; additionalProperties: false; properties: 6 entries (see descendant pointers); required: ["id","compRegions","outputAudioRegionIds","outputMode"]; allOf: 2 branches (see descendant pointers) | A complete ordered partition of the Group's range into selected source or explicit-silence regions. The map is the editing authority; ordinary materialized output is playback authority. All-silence Comp has no outputs; any source region requires at least one output descriptor (MIDI may contain an empty notes array). IDs and ranges must resolve consistently in a single authoring transaction. |
| `/$defs/audioComp51/properties/id` | Yes | type: "string"; pattern: "^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$"; not: 1 entries (see descendant pointers) |  |
| `/$defs/audioComp51/properties/id/not` | Context / conditional | pattern: "[\\r\\n\\u2028\\u2029]" |  |
| `/$defs/audioComp51/properties/name` | No | type: "string" |  |
| `/$defs/audioComp51/properties/compRegions` | Yes | type: "array"; items: 1 entries (see descendant pointers); minItems: 1 |  |
| `/$defs/audioComp51/properties/compRegions/items` | Context / conditional | $ref: "#/$defs/audioCompRegion51" |  |
| `/$defs/audioComp51/properties/outputAudioRegionIds` | Yes | type: "array"; items: 3 entries (see descendant pointers); minItems: 0; uniqueItems: true |  |
| `/$defs/audioComp51/properties/outputAudioRegionIds/items` | Context / conditional | type: "string"; pattern: "^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$"; not: 1 entries (see descendant pointers) |  |
| `/$defs/audioComp51/properties/outputAudioRegionIds/items/not` | Context / conditional | pattern: "[\\r\\n\\u2028\\u2029]" |  |
| `/$defs/audioComp51/properties/outputMode` | Yes | enum: ["regions","rendered"] |  |
| `/$defs/audioComp51/properties/transitions` | No | type: "array"; items: 1 entries (see descendant pointers); minItems: 0; uniqueItems: true |  |
| `/$defs/audioComp51/properties/transitions/items` | Context / conditional | $ref: "#/$defs/takeTransition51" |  |
| `/$defs/audioComp51/allOf/0` | Context / conditional | if: 2 entries (see descendant pointers); then: 1 entries (see descendant pointers) |  |
| `/$defs/audioComp51/allOf/0/if` | Context / conditional | properties: 1 entries (see descendant pointers); required: ["outputMode"] |  |
| `/$defs/audioComp51/allOf/0/if/properties/outputMode` | Yes | const: "regions" |  |
| `/$defs/audioComp51/allOf/0/then` | Context / conditional | properties: 1 entries (see descendant pointers) |  |
| `/$defs/audioComp51/allOf/0/then/properties/transitions` | No | items: 1 entries (see descendant pointers) |  |
| `/$defs/audioComp51/allOf/0/then/properties/transitions/items` | Context / conditional | properties: 1 entries (see descendant pointers) |  |
| `/$defs/audioComp51/allOf/0/then/properties/transitions/items/properties/curve` | No | const: "linear" |  |
| `/$defs/audioComp51/allOf/1` | Context / conditional | if: 2 entries (see descendant pointers); then: 1 entries (see descendant pointers); else: 1 entries (see descendant pointers) |  |
| `/$defs/audioComp51/allOf/1/if` | Context / conditional | properties: 1 entries (see descendant pointers); required: ["compRegions"] |  |
| `/$defs/audioComp51/allOf/1/if/properties/compRegions` | Yes | contains: 2 entries (see descendant pointers); minContains: 1 |  |
| `/$defs/audioComp51/allOf/1/if/properties/compRegions/contains` | Context / conditional | properties: 1 entries (see descendant pointers); required: ["kind"] |  |
| `/$defs/audioComp51/allOf/1/if/properties/compRegions/contains/properties/kind` | Yes | const: "source" |  |
| `/$defs/audioComp51/allOf/1/then` | Context / conditional | properties: 1 entries (see descendant pointers) |  |
| `/$defs/audioComp51/allOf/1/then/properties/outputAudioRegionIds` | No | minItems: 1 |  |
| `/$defs/audioComp51/allOf/1/else` | Context / conditional | properties: 2 entries (see descendant pointers) |  |
| `/$defs/audioComp51/allOf/1/else/properties/outputAudioRegionIds` | No | maxItems: 0 |  |
| `/$defs/audioComp51/allOf/1/else/properties/transitions` | No | maxItems: 0 |  |
| `/$defs/audioTakeGroup51` | Context / conditional | type: "object"; additionalProperties: false; properties: 12 entries (see descendant pointers); required: ["id","channelId","startTick","durationTicks","takes","comps","activeCompId"]; allOf: 1 branches (see descendant pointers) | Non-overlapping source-score Tick range owned by channelId. All ranges use Score PPQ, are half-open, and have safe-integer endpoints. Sources and independently identified materialized outputs remain on the existing timeline; source candidates never play as ordinary active clips. References, ownership, range sums, unique scoped IDs and flags require semantic validation in addition to this schema. |
| `/$defs/audioTakeGroup51/properties/id` | Yes | type: "string"; pattern: "^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$"; not: 1 entries (see descendant pointers) |  |
| `/$defs/audioTakeGroup51/properties/id/not` | Context / conditional | pattern: "[\\r\\n\\u2028\\u2029]" |  |
| `/$defs/audioTakeGroup51/properties/channelId` | Yes | type: "string"; pattern: "^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$"; not: 1 entries (see descendant pointers) |  |
| `/$defs/audioTakeGroup51/properties/channelId/not` | Context / conditional | pattern: "[\\r\\n\\u2028\\u2029]" |  |
| `/$defs/audioTakeGroup51/properties/startTick` | Yes | type: "integer"; minimum: 0; maximum: 9007199254740991 |  |
| `/$defs/audioTakeGroup51/properties/durationTicks` | Yes | type: "integer"; minimum: 1; maximum: 9007199254740991 |  |
| `/$defs/audioTakeGroup51/properties/name` | No | type: "string" |  |
| `/$defs/audioTakeGroup51/properties/sectionId` | No | type: "string"; pattern: "^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$"; not: 1 entries (see descendant pointers) |  |
| `/$defs/audioTakeGroup51/properties/sectionId/not` | Context / conditional | pattern: "[\\r\\n\\u2028\\u2029]" |  |
| `/$defs/audioTakeGroup51/properties/takes` | Yes | type: "array"; items: 1 entries (see descendant pointers); minItems: 1 |  |
| `/$defs/audioTakeGroup51/properties/takes/items` | Context / conditional | $ref: "#/$defs/audioTake51" |  |
| `/$defs/audioTakeGroup51/properties/comps` | Yes | type: "array"; items: 1 entries (see descendant pointers); minItems: 0 |  |
| `/$defs/audioTakeGroup51/properties/comps/items` | Context / conditional | $ref: "#/$defs/audioComp51" |  |
| `/$defs/audioTakeGroup51/properties/activeCompId` | Yes | anyOf: 2 branches (see descendant pointers) | One Comp ID in this Group, or null for silence. Empty comps requires null. This saved selection controls the ordinary output flags; Visit/live selection overlays do not rewrite these saved flags. |
| `/$defs/audioTakeGroup51/properties/activeCompId/anyOf/0` | Context / conditional | type: "string"; pattern: "^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$"; not: 1 entries (see descendant pointers) |  |
| `/$defs/audioTakeGroup51/properties/activeCompId/anyOf/0/not` | Context / conditional | pattern: "[\\r\\n\\u2028\\u2029]" |  |
| `/$defs/audioTakeGroup51/properties/activeCompId/anyOf/1` | Context / conditional | type: "null" |  |
| `/$defs/audioTakeGroup51/properties/visitSelections` | No | type: "array"; items: 1 entries (see descendant pointers); minItems: 0; uniqueItems: true |  |
| `/$defs/audioTakeGroup51/properties/visitSelections/items` | Context / conditional | $ref: "#/$defs/takeVisitSelection51" |  |
| `/$defs/audioTakeGroup51/properties/liveSelection` | No | $ref: "#/$defs/takeLiveSelection51" |  |
| `/$defs/audioTakeGroup51/properties/takeSelectionHistory` | No | type: "array"; items: 1 entries (see descendant pointers); minItems: 0 |  |
| `/$defs/audioTakeGroup51/properties/takeSelectionHistory/items` | Context / conditional | $ref: "#/$defs/takeSelectionHistory51" |  |
| `/$defs/audioTakeGroup51/allOf/0` | Context / conditional | if: 2 entries (see descendant pointers); then: 1 entries (see descendant pointers) |  |
| `/$defs/audioTakeGroup51/allOf/0/if` | Context / conditional | properties: 1 entries (see descendant pointers); required: ["comps"] |  |
| `/$defs/audioTakeGroup51/allOf/0/if/properties/comps` | Yes | maxItems: 0 |  |
| `/$defs/audioTakeGroup51/allOf/0/then` | Context / conditional | properties: 3 entries (see descendant pointers) |  |
| `/$defs/audioTakeGroup51/allOf/0/then/properties/activeCompId` | No | type: "null" |  |
| `/$defs/audioTakeGroup51/allOf/0/then/properties/visitSelections` | No | items: 1 entries (see descendant pointers) |  |
| `/$defs/audioTakeGroup51/allOf/0/then/properties/visitSelections/items` | Context / conditional | properties: 1 entries (see descendant pointers) |  |
| `/$defs/audioTakeGroup51/allOf/0/then/properties/visitSelections/items/properties/compId` | No | type: "null" |  |
| `/$defs/audioTakeGroup51/allOf/0/then/properties/liveSelection` | No | properties: 1 entries (see descendant pointers) |  |
| `/$defs/audioTakeGroup51/allOf/0/then/properties/liveSelection/properties/mode` | No | enum: ["fixed","manual"] |  |

## ostf-distributed-session-0.4.schema.json

| Schema Pointer | Required in direct parent | Constraints | Original description |
|---|---|---|---|
| `/` | Context / conditional | $schema: "https://json-schema.org/draft/2020-12/schema"; $id: "https://yoh-nak.github.io/ostf/schema/ostf-distributed-session-0.4.schema.json"; oneOf: 2 branches (see descendant pointers); $defs: 16 entries (see descendant pointers) | Complete Distributed 0.4 Snapshot/Event grammar, retaining 0.3 session semantics and pinned to exact Score 5.1.0 bytes. Accepted session phrases are not automatic Score/Take/Comp edits. |
| `/oneOf/0` | Context / conditional | $ref: "#/$defs/snapshot" |  |
| `/oneOf/1` | Context / conditional | $ref: "#/$defs/event" |  |
| `/$defs/id` | Context / conditional | type: "string"; minLength: 1 |  |
| `/$defs/participant` | Context / conditional | type: "object"; properties: 5 entries (see descendant pointers); required: ["participantId","kind","assignedTrackIds"]; additionalProperties: false |  |
| `/$defs/participant/properties/participantId` | Yes | $ref: "#/$defs/id" |  |
| `/$defs/participant/properties/kind` | Yes | enum: ["human","softwareAgent","physicalRobot"] |  |
| `/$defs/participant/properties/assignedTrackIds` | Yes | type: "array"; items: 1 entries (see descendant pointers); uniqueItems: true |  |
| `/$defs/participant/properties/assignedTrackIds/items` | Context / conditional | $ref: "#/$defs/id" |  |
| `/$defs/participant/properties/supportedFeatures` | No | type: "array"; items: 2 entries (see descendant pointers); uniqueItems: true |  |
| `/$defs/participant/properties/supportedFeatures/items` | Context / conditional | type: "string"; minLength: 1 |  |
| `/$defs/participant/properties/capabilities` | No | type: "object"; additionalProperties: true | Untrusted advisory data, not robot actuator authorization |
| `/$defs/position` | Context / conditional | type: "object"; properties: 8 entries (see descendant pointers); required: ["performancePlanId","visitId","sourceTick","performanceTick","clockDomainId","epochUtc","uncertaintyMs"]; additionalProperties: false | epochUtc denotes the clock-domain estimate for the explicitly stated performanceTick (at the sourceTick). Clock synchronization algorithm is out of scope. |
| `/$defs/position/properties/performancePlanId` | Yes | $ref: "#/$defs/id" |  |
| `/$defs/position/properties/visitId` | Yes | $ref: "#/$defs/id" |  |
| `/$defs/position/properties/sourceTick` | Yes | type: "integer"; minimum: 0; maximum: 9007199254740991 |  |
| `/$defs/position/properties/performanceTick` | Yes | type: "integer"; minimum: 0; maximum: 9007199254740991 |  |
| `/$defs/position/properties/clockDomainId` | Yes | $ref: "#/$defs/id" |  |
| `/$defs/position/properties/epochUtc` | Yes | type: "string"; format: "date-time" |  |
| `/$defs/position/properties/uncertaintyMs` | Yes | type: "number"; minimum: 0 |  |
| `/$defs/position/properties/tempoBpm` | No | type: "number"; exclusiveMinimum: 0 |  |
| `/$defs/note` | Context / conditional | type: "object"; properties: 4 entries (see descendant pointers); required: ["startTick","durationTicks","pitch","velocity"]; additionalProperties: false | MIDI-like note within a proposed session phrase, not a new authoritative OSTF Core Note. |
| `/$defs/note/properties/startTick` | Yes | type: "integer"; minimum: 0; maximum: 9007199254740991 |  |
| `/$defs/note/properties/durationTicks` | Yes | type: "integer"; minimum: 1; maximum: 9007199254740991 |  |
| `/$defs/note/properties/pitch` | Yes | type: "integer"; minimum: 0; maximum: 127 |  |
| `/$defs/note/properties/velocity` | Yes | type: "integer"; minimum: 1; maximum: 127 |  |
| `/$defs/phrase` | Context / conditional | type: "object"; properties: 3 entries (see descendant pointers); required: ["representation","durationTicks","notes"]; additionalProperties: false | A portable minimal pitched-note session phrase. No lyrics, MPE, instrument actuation or audio realization is implied. Notes are relative to phrase start/effectivePerformanceTick. |
| `/$defs/phrase/properties/representation` | Yes | const: "midi1Notes" |  |
| `/$defs/phrase/properties/durationTicks` | Yes | type: "integer"; minimum: 1; maximum: 9007199254740991 |  |
| `/$defs/phrase/properties/notes` | Yes | type: "array"; items: 1 entries (see descendant pointers); minItems: 1 |  |
| `/$defs/phrase/properties/notes/items` | Context / conditional | $ref: "#/$defs/note" |  |
| `/$defs/committedPhrase` | Context / conditional | type: "object"; properties: 5 entries (see descendant pointers); required: ["commitEventId","proposalId","targetTrackId","effectivePerformanceTick","phrase"]; additionalProperties: false |  |
| `/$defs/committedPhrase/properties/commitEventId` | Yes | $ref: "#/$defs/id" |  |
| `/$defs/committedPhrase/properties/proposalId` | Yes | $ref: "#/$defs/id" |  |
| `/$defs/committedPhrase/properties/targetTrackId` | Yes | $ref: "#/$defs/id" |  |
| `/$defs/committedPhrase/properties/effectivePerformanceTick` | Yes | type: "integer"; minimum: 0; maximum: 9007199254740991 |  |
| `/$defs/committedPhrase/properties/phrase` | Yes | $ref: "#/$defs/phrase" |  |
| `/$defs/snapshot` | Context / conditional | type: "object"; properties: 14 entries (see descendant pointers); required: ["profile","recordType","sessionId","documentId","revisionId","performancePlanId","scoreSha256","sessionStatus","stateRevision","authorityParticipantId","participants"]; additionalProperties: false; allOf: 2 branches (see descendant pointers) | Authoritative session state, pinned to one Score 5.1 document, revision and finite Plan. Playing requires position; prepared/stopped may omit it. Optional commitmentWindow asserts complete accepted-phrase coverage at stateRevision. At least one Participant is required for authority resolution. |
| `/$defs/snapshot/properties/profile` | Yes | const: "OSTF-Distributed-Session-0.4" |  |
| `/$defs/snapshot/properties/recordType` | Yes | const: "snapshot" |  |
| `/$defs/snapshot/properties/sessionId` | Yes | $ref: "#/$defs/id" |  |
| `/$defs/snapshot/properties/documentId` | Yes | $ref: "#/$defs/id" |  |
| `/$defs/snapshot/properties/revisionId` | Yes | $ref: "#/$defs/id" |  |
| `/$defs/snapshot/properties/performancePlanId` | Yes | $ref: "#/$defs/id" | Required pinned finite OSTF 5.1 Core performancePlans[].id; positions must match this ID. |
| `/$defs/snapshot/properties/scoreSha256` | Yes | type: "string"; pattern: "^[0-9a-f]{64}$" | SHA-256 lowercase hex over the exact UTF-8 OSTF source document bytes after HTTP Content-Encoding removal and before parsing; byte identity pin only, not authentication or semantic normalization. |
| `/$defs/snapshot/properties/sessionStatus` | Yes | enum: ["prepared","playing","stopped"] | Authoritative session lifecycle state; not participant availability or network connection status. |
| `/$defs/snapshot/properties/stateRevision` | Yes | type: "integer"; minimum: 0 |  |
| `/$defs/snapshot/properties/authorityParticipantId` | Yes | $ref: "#/$defs/id" |  |
| `/$defs/snapshot/properties/participants` | Yes | type: "array"; items: 1 entries (see descendant pointers); minItems: 1 |  |
| `/$defs/snapshot/properties/participants/items` | Context / conditional | $ref: "#/$defs/participant" |  |
| `/$defs/snapshot/properties/position` | No | $ref: "#/$defs/position" |  |
| `/$defs/snapshot/properties/committedPhrases` | No | type: "array"; items: 1 entries (see descendant pointers) | Self-contained accepted phrases for late joiners; only active/future material is required for live join, full archive required for full replay claims. |
| `/$defs/snapshot/properties/committedPhrases/items` | Context / conditional | $ref: "#/$defs/committedPhrase" |  |
| `/$defs/snapshot/properties/commitmentWindow` | No | $ref: "#/$defs/commitmentWindow" | Optional truthful late-join phrase completeness assertion. Only allowed in playing Snapshots with position; absent means no completeness claim, not an empty session. |
| `/$defs/snapshot/allOf/0` | Context / conditional | if: 2 entries (see descendant pointers); then: 1 entries (see descendant pointers) |  |
| `/$defs/snapshot/allOf/0/if` | Context / conditional | properties: 1 entries (see descendant pointers); required: ["sessionStatus"] |  |
| `/$defs/snapshot/allOf/0/if/properties/sessionStatus` | Yes | const: "playing" |  |
| `/$defs/snapshot/allOf/0/then` | Context / conditional | required: ["position"] |  |
| `/$defs/snapshot/allOf/1` | Context / conditional | if: 1 entries (see descendant pointers); then: 2 entries (see descendant pointers) |  |
| `/$defs/snapshot/allOf/1/if` | Context / conditional | required: ["commitmentWindow"] |  |
| `/$defs/snapshot/allOf/1/then` | Context / conditional | required: ["position","committedPhrases"]; properties: 1 entries (see descendant pointers) |  |
| `/$defs/snapshot/allOf/1/then/properties/sessionStatus` | No | const: "playing" |  |
| `/$defs/phraseProposedPayload` | Context / conditional | type: "object"; properties: 3 entries (see descendant pointers); required: ["proposalId","targetTrackId","phrase"]; additionalProperties: false |  |
| `/$defs/phraseProposedPayload/properties/proposalId` | Yes | $ref: "#/$defs/id" |  |
| `/$defs/phraseProposedPayload/properties/targetTrackId` | Yes | $ref: "#/$defs/id" |  |
| `/$defs/phraseProposedPayload/properties/phrase` | Yes | $ref: "#/$defs/phrase" |  |
| `/$defs/phraseCommittedPayload` | Context / conditional | type: "object"; properties: 3 entries (see descendant pointers); required: ["proposalId","targetTrackId","phrase"]; additionalProperties: false |  |
| `/$defs/phraseCommittedPayload/properties/proposalId` | Yes | $ref: "#/$defs/id" |  |
| `/$defs/phraseCommittedPayload/properties/targetTrackId` | Yes | $ref: "#/$defs/id" |  |
| `/$defs/phraseCommittedPayload/properties/phrase` | Yes | $ref: "#/$defs/phrase" |  |
| `/$defs/turnRequestedPayload` | Context / conditional | type: "object"; properties: 3 entries (see descendant pointers); required: ["targetTrackId","requestedRole"]; additionalProperties: false |  |
| `/$defs/turnRequestedPayload/properties/targetTrackId` | Yes | $ref: "#/$defs/id" |  |
| `/$defs/turnRequestedPayload/properties/requestedRole` | Yes | type: "string"; minLength: 1 |  |
| `/$defs/turnRequestedPayload/properties/requestedVisitId` | No | $ref: "#/$defs/id" |  |
| `/$defs/cueIssuedPayload` | Context / conditional | type: "object"; properties: 2 entries (see descendant pointers); required: ["cueId"]; additionalProperties: false |  |
| `/$defs/cueIssuedPayload/properties/cueId` | Yes | $ref: "#/$defs/id" |  |
| `/$defs/cueIssuedPayload/properties/targetVisitId` | No | $ref: "#/$defs/id" |  |
| `/$defs/performanceObservedPayload` | Context / conditional | type: "object"; properties: 4 entries (see descendant pointers); required: ["observedParticipantId","sourceTrackId","confidence"]; additionalProperties: false |  |
| `/$defs/performanceObservedPayload/properties/observedParticipantId` | Yes | $ref: "#/$defs/id" |  |
| `/$defs/performanceObservedPayload/properties/sourceTrackId` | Yes | $ref: "#/$defs/id" |  |
| `/$defs/performanceObservedPayload/properties/confidence` | Yes | type: "number"; minimum: 0; maximum: 1 |  |
| `/$defs/performanceObservedPayload/properties/features` | No | type: "object"; additionalProperties: true |  |
| `/$defs/participantStatusPayload` | Context / conditional | type: "object"; properties: 3 entries (see descendant pointers); required: ["participantId","availability"]; additionalProperties: false |  |
| `/$defs/participantStatusPayload/properties/participantId` | Yes | $ref: "#/$defs/id" |  |
| `/$defs/participantStatusPayload/properties/availability` | Yes | enum: ["ready","busy","disconnected"] |  |
| `/$defs/participantStatusPayload/properties/message` | No | type: "string" |  |
| `/$defs/sessionStateChangedPayload` | Context / conditional | type: "object"; properties: 5 entries (see descendant pointers); required: ["changeKind"]; additionalProperties: false; allOf: 4 branches (see descendant pointers) | Authoritative sessionStarted and visitChanged both supply an explicit musical/UTC Position anchor. assignmentChanged changes assignments only and MUST NOT carry position or targetVisitId; sessionStopped is immediate. |
| `/$defs/sessionStateChangedPayload/properties/changeKind` | Yes | enum: ["sessionStarted","visitChanged","assignmentChanged","sessionStopped"] |  |
| `/$defs/sessionStateChangedPayload/properties/targetVisitId` | No | $ref: "#/$defs/id" |  |
| `/$defs/sessionStateChangedPayload/properties/participantId` | No | $ref: "#/$defs/id" |  |
| `/$defs/sessionStateChangedPayload/properties/assignedTrackIds` | No | type: "array"; items: 1 entries (see descendant pointers); uniqueItems: true |  |
| `/$defs/sessionStateChangedPayload/properties/assignedTrackIds/items` | Context / conditional | $ref: "#/$defs/id" |  |
| `/$defs/sessionStateChangedPayload/properties/position` | No | $ref: "#/$defs/position" | Authoritative Plan/Visit/source/performance Tick and clock-domain/UTC anchor. Required for sessionStarted and visitChanged; position.performanceTick MUST equal event effectivePerformanceTick. For visitChanged, position.visitId MUST equal targetVisitId at that Visit start. |
| `/$defs/sessionStateChangedPayload/allOf/0` | Context / conditional | if: 2 entries (see descendant pointers); then: 2 entries (see descendant pointers) |  |
| `/$defs/sessionStateChangedPayload/allOf/0/if` | Context / conditional | properties: 1 entries (see descendant pointers); required: ["changeKind"] |  |
| `/$defs/sessionStateChangedPayload/allOf/0/if/properties/changeKind` | Yes | const: "sessionStarted" |  |
| `/$defs/sessionStateChangedPayload/allOf/0/then` | Context / conditional | required: ["position"]; not: 1 entries (see descendant pointers) |  |
| `/$defs/sessionStateChangedPayload/allOf/0/then/not` | Context / conditional | anyOf: 3 branches (see descendant pointers) |  |
| `/$defs/sessionStateChangedPayload/allOf/0/then/not/anyOf/0` | Context / conditional | required: ["targetVisitId"] |  |
| `/$defs/sessionStateChangedPayload/allOf/0/then/not/anyOf/1` | Context / conditional | required: ["participantId"] |  |
| `/$defs/sessionStateChangedPayload/allOf/0/then/not/anyOf/2` | Context / conditional | required: ["assignedTrackIds"] |  |
| `/$defs/sessionStateChangedPayload/allOf/1` | Context / conditional | if: 2 entries (see descendant pointers); then: 2 entries (see descendant pointers) |  |
| `/$defs/sessionStateChangedPayload/allOf/1/if` | Context / conditional | properties: 1 entries (see descendant pointers); required: ["changeKind"] |  |
| `/$defs/sessionStateChangedPayload/allOf/1/if/properties/changeKind` | Yes | const: "visitChanged" |  |
| `/$defs/sessionStateChangedPayload/allOf/1/then` | Context / conditional | required: ["targetVisitId","position"]; not: 1 entries (see descendant pointers) |  |
| `/$defs/sessionStateChangedPayload/allOf/1/then/not` | Context / conditional | anyOf: 2 branches (see descendant pointers) |  |
| `/$defs/sessionStateChangedPayload/allOf/1/then/not/anyOf/0` | Context / conditional | required: ["participantId"] |  |
| `/$defs/sessionStateChangedPayload/allOf/1/then/not/anyOf/1` | Context / conditional | required: ["assignedTrackIds"] |  |
| `/$defs/sessionStateChangedPayload/allOf/2` | Context / conditional | if: 2 entries (see descendant pointers); then: 2 entries (see descendant pointers) |  |
| `/$defs/sessionStateChangedPayload/allOf/2/if` | Context / conditional | properties: 1 entries (see descendant pointers); required: ["changeKind"] |  |
| `/$defs/sessionStateChangedPayload/allOf/2/if/properties/changeKind` | Yes | const: "assignmentChanged" |  |
| `/$defs/sessionStateChangedPayload/allOf/2/then` | Context / conditional | required: ["participantId","assignedTrackIds"]; not: 1 entries (see descendant pointers) |  |
| `/$defs/sessionStateChangedPayload/allOf/2/then/not` | Context / conditional | anyOf: 2 branches (see descendant pointers) |  |
| `/$defs/sessionStateChangedPayload/allOf/2/then/not/anyOf/0` | Context / conditional | required: ["targetVisitId"] |  |
| `/$defs/sessionStateChangedPayload/allOf/2/then/not/anyOf/1` | Context / conditional | required: ["position"] |  |
| `/$defs/sessionStateChangedPayload/allOf/3` | Context / conditional | if: 2 entries (see descendant pointers); then: 1 entries (see descendant pointers) |  |
| `/$defs/sessionStateChangedPayload/allOf/3/if` | Context / conditional | properties: 1 entries (see descendant pointers); required: ["changeKind"] |  |
| `/$defs/sessionStateChangedPayload/allOf/3/if/properties/changeKind` | Yes | const: "sessionStopped" |  |
| `/$defs/sessionStateChangedPayload/allOf/3/then` | Context / conditional | not: 1 entries (see descendant pointers) |  |
| `/$defs/sessionStateChangedPayload/allOf/3/then/not` | Context / conditional | anyOf: 4 branches (see descendant pointers) |  |
| `/$defs/sessionStateChangedPayload/allOf/3/then/not/anyOf/0` | Context / conditional | required: ["targetVisitId"] |  |
| `/$defs/sessionStateChangedPayload/allOf/3/then/not/anyOf/1` | Context / conditional | required: ["participantId"] |  |
| `/$defs/sessionStateChangedPayload/allOf/3/then/not/anyOf/2` | Context / conditional | required: ["assignedTrackIds"] |  |
| `/$defs/sessionStateChangedPayload/allOf/3/then/not/anyOf/3` | Context / conditional | required: ["position"] |  |
| `/$defs/event` | Context / conditional | type: "object"; properties: 14 entries (see descendant pointers); required: ["profile","recordType","eventId","sessionId","documentId","revisionId","performancePlanId","scoreSha256","baseStateRevision","issuerParticipantId","kind","effectivePerformanceTick","payload"]; additionalProperties: false; oneOf: 7 branches (see descendant pointers) | Session event under inherited authority and state-machine rules. Accepted phraseCommitted/sessionStateChanged increments revision exactly once. sessionStarted/visitChanged require clock-anchored Position with matching effectivePerformanceTick. These relationships are semantic constraints. |
| `/$defs/event/properties/profile` | Yes | const: "OSTF-Distributed-Session-0.4" |  |
| `/$defs/event/properties/recordType` | Yes | const: "event" |  |
| `/$defs/event/properties/eventId` | Yes | $ref: "#/$defs/id" |  |
| `/$defs/event/properties/sessionId` | Yes | $ref: "#/$defs/id" |  |
| `/$defs/event/properties/documentId` | Yes | $ref: "#/$defs/id" |  |
| `/$defs/event/properties/revisionId` | Yes | $ref: "#/$defs/id" |  |
| `/$defs/event/properties/performancePlanId` | Yes | $ref: "#/$defs/id" | Required pinned finite OSTF 5.1 Core performancePlans[].id; positions must match this ID. |
| `/$defs/event/properties/scoreSha256` | Yes | type: "string"; pattern: "^[0-9a-f]{64}$" | SHA-256 lowercase hex over the exact UTF-8 OSTF source document bytes after HTTP Content-Encoding removal and before parsing; byte identity pin only, not authentication or semantic normalization. |
| `/$defs/event/properties/baseStateRevision` | Yes | type: "integer"; minimum: 0 |  |
| `/$defs/event/properties/resultStateRevision` | No | type: "integer"; minimum: 0 |  |
| `/$defs/event/properties/issuerParticipantId` | Yes | $ref: "#/$defs/id" |  |
| `/$defs/event/properties/kind` | Yes | enum: ["phraseProposed","phraseCommitted","turnRequested","cueIssued","performanceObserved","participantStatus","sessionStateChanged"] |  |
| `/$defs/event/properties/effectivePerformanceTick` | Yes | type: "integer"; minimum: 0; maximum: 9007199254740991 |  |
| `/$defs/event/properties/payload` | Yes | type: "object" |  |
| `/$defs/event/oneOf/0` | Context / conditional | properties: 2 entries (see descendant pointers); required: ["kind","payload"]; not: 1 entries (see descendant pointers) |  |
| `/$defs/event/oneOf/0/properties/kind` | Yes | const: "phraseProposed" |  |
| `/$defs/event/oneOf/0/properties/payload` | Yes | $ref: "#/$defs/phraseProposedPayload" |  |
| `/$defs/event/oneOf/0/not` | Context / conditional | required: ["resultStateRevision"] |  |
| `/$defs/event/oneOf/1` | Context / conditional | properties: 2 entries (see descendant pointers); required: ["kind","payload","resultStateRevision"] |  |
| `/$defs/event/oneOf/1/properties/kind` | Yes | const: "phraseCommitted" |  |
| `/$defs/event/oneOf/1/properties/payload` | Yes | $ref: "#/$defs/phraseCommittedPayload" |  |
| `/$defs/event/oneOf/2` | Context / conditional | properties: 2 entries (see descendant pointers); required: ["kind","payload"]; not: 1 entries (see descendant pointers) |  |
| `/$defs/event/oneOf/2/properties/kind` | Yes | const: "turnRequested" |  |
| `/$defs/event/oneOf/2/properties/payload` | Yes | $ref: "#/$defs/turnRequestedPayload" |  |
| `/$defs/event/oneOf/2/not` | Context / conditional | required: ["resultStateRevision"] |  |
| `/$defs/event/oneOf/3` | Context / conditional | properties: 2 entries (see descendant pointers); required: ["kind","payload"]; not: 1 entries (see descendant pointers) |  |
| `/$defs/event/oneOf/3/properties/kind` | Yes | const: "cueIssued" |  |
| `/$defs/event/oneOf/3/properties/payload` | Yes | $ref: "#/$defs/cueIssuedPayload" |  |
| `/$defs/event/oneOf/3/not` | Context / conditional | required: ["resultStateRevision"] |  |
| `/$defs/event/oneOf/4` | Context / conditional | properties: 2 entries (see descendant pointers); required: ["kind","payload"]; not: 1 entries (see descendant pointers) |  |
| `/$defs/event/oneOf/4/properties/kind` | Yes | const: "performanceObserved" |  |
| `/$defs/event/oneOf/4/properties/payload` | Yes | $ref: "#/$defs/performanceObservedPayload" |  |
| `/$defs/event/oneOf/4/not` | Context / conditional | required: ["resultStateRevision"] |  |
| `/$defs/event/oneOf/5` | Context / conditional | properties: 2 entries (see descendant pointers); required: ["kind","payload"]; not: 1 entries (see descendant pointers) |  |
| `/$defs/event/oneOf/5/properties/kind` | Yes | const: "participantStatus" |  |
| `/$defs/event/oneOf/5/properties/payload` | Yes | $ref: "#/$defs/participantStatusPayload" |  |
| `/$defs/event/oneOf/5/not` | Context / conditional | required: ["resultStateRevision"] |  |
| `/$defs/event/oneOf/6` | Context / conditional | properties: 2 entries (see descendant pointers); required: ["kind","payload","resultStateRevision"] |  |
| `/$defs/event/oneOf/6/properties/kind` | Yes | const: "sessionStateChanged" |  |
| `/$defs/event/oneOf/6/properties/payload` | Yes | $ref: "#/$defs/sessionStateChangedPayload" |  |
| `/$defs/commitmentWindow` | Context / conditional | type: "object"; properties: 2 entries (see descendant pointers); required: ["startPerformanceTick","endPerformanceTick"]; additionalProperties: false | Optional assertion that all accepted committed phrases intersecting half-open [startPerformanceTick, endPerformanceTick) are listed in committedPhrases for the Snapshot stateRevision. Semantic validator MUST check start < end and intersection/completeness against authority log. |
| `/$defs/commitmentWindow/properties/startPerformanceTick` | Yes | type: "integer"; minimum: 0; maximum: 9007199254740991 |  |
| `/$defs/commitmentWindow/properties/endPerformanceTick` | Yes | type: "integer"; minimum: 1; maximum: 9007199254740991 |  |

## ostf-package-manifest-1.1.schema.json

| Schema Pointer | Required in direct parent | Constraints | Original description |
|---|---|---|---|
| `/` | Context / conditional | $schema: "https://json-schema.org/draft/2020-12/schema"; $id: "https://yoh-nak.github.io/ostf/schema/ostf-package-manifest-1.1.schema.json"; type: "object"; additionalProperties: false; properties: 11 entries (see descendant pointers); required: ["packageFormat","packageVersion","projectId","title","score","documents","assets","bindings"]; $defs: 8 entries (see descendant pointers); allOf: 3 branches (see descendant pointers) | OSTF Project Package Manifest 1.1 |
| `/properties/packageFormat` | Yes | const: "OSTFP" |  |
| `/properties/packageVersion` | Yes | const: "1.1.0" |  |
| `/properties/projectId` | Yes | type: "string"; pattern: "^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$" |  |
| `/properties/title` | Yes | type: "string"; minLength: 1 |  |
| `/properties/score` | Yes | $ref: "#/$defs/score" |  |
| `/properties/documents` | Yes | type: "array"; items: 1 entries (see descendant pointers) |  |
| `/properties/documents/items` | Context / conditional | $ref: "#/$defs/document" |  |
| `/properties/assets` | Yes | type: "array"; items: 1 entries (see descendant pointers) |  |
| `/properties/assets/items` | Context / conditional | $ref: "#/$defs/asset" |  |
| `/properties/bindings` | Yes | type: "array"; items: 1 entries (see descendant pointers) | No ambiguous duplicates of (documentPath,resourceKind,resourceId); referents and SHA matching are semantic constraints. |
| `/properties/bindings/items` | Context / conditional | $ref: "#/$defs/binding" |  |
| `/properties/externalAssets` | No | type: "array"; items: 1 entries (see descendant pointers) |  |
| `/properties/externalAssets/items` | Context / conditional | $ref: "#/$defs/externalAsset" |  |
| `/properties/metadata` | No | type: "object"; additionalProperties: true |  |
| `/properties/extensions` | No | type: "object"; additionalProperties: true |  |
| `/$defs/sha256` | Context / conditional | type: "string"; pattern: "^[a-f0-9]{64}$" |  |
| `/$defs/path` | Context / conditional | type: "string"; minLength: 1; maxLength: 1024; pattern: "^(?!/)(?!.*(?:^\|/)\\.\\.?/)(?!.*\\\\)(?!.*://)[^\\x00-\\x1F\\x7F]+$" | POSIX package-relative NFC path; further semantic checks prohibit dot-segments, drive letters, encoded traversal, duplicate normalized names, symlinks. |
| `/$defs/id` | Context / conditional | type: "string"; pattern: "^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$" |  |
| `/$defs/score` | Context / conditional | type: "object"; additionalProperties: false; properties: 4 entries (see descendant pointers); required: ["path","format","version","sha256"] |  |
| `/$defs/score/properties/path` | Yes | $ref: "#/$defs/path" |  |
| `/$defs/score/properties/format` | Yes | const: "OSTF" |  |
| `/$defs/score/properties/version` | Yes | enum: ["4.3.0","5.0.0","5.1.0"] |  |
| `/$defs/score/properties/sha256` | Yes | $ref: "#/$defs/sha256" |  |
| `/$defs/document` | Context / conditional | type: "object"; additionalProperties: false; properties: 7 entries (see descendant pointers); required: ["id","role","path","family","version","sha256"]; allOf: 2 branches (see descendant pointers) | Descriptor of exact embedded bytes. Recognized Session families must use their corresponding role; companion versions are selected by the root Score version. SHA and discriminator agreement with actual member bytes is a semantic container constraint. |
| `/$defs/document/properties/id` | Yes | $ref: "#/$defs/id" |  |
| `/$defs/document/properties/role` | Yes | enum: ["productionSession","distributedSession","supplement","metadata"] |  |
| `/$defs/document/properties/path` | Yes | $ref: "#/$defs/path" |  |
| `/$defs/document/properties/family` | Yes | type: "string"; minLength: 1 |  |
| `/$defs/document/properties/version` | Yes | type: "string"; minLength: 1 |  |
| `/$defs/document/properties/sha256` | Yes | $ref: "#/$defs/sha256" |  |
| `/$defs/document/properties/required` | No | type: "boolean"; default: false | Whether host application requires this optional document to claim its requested portable level; absence of this field means false. |
| `/$defs/document/allOf/0` | Context / conditional | if: 2 entries (see descendant pointers); then: 1 entries (see descendant pointers) |  |
| `/$defs/document/allOf/0/if` | Context / conditional | properties: 1 entries (see descendant pointers); required: ["family"] |  |
| `/$defs/document/allOf/0/if/properties/family` | Yes | const: "OSTF-Production-Session" |  |
| `/$defs/document/allOf/0/then` | Context / conditional | properties: 1 entries (see descendant pointers) |  |
| `/$defs/document/allOf/0/then/properties/role` | No | const: "productionSession" |  |
| `/$defs/document/allOf/1` | Context / conditional | if: 2 entries (see descendant pointers); then: 1 entries (see descendant pointers) |  |
| `/$defs/document/allOf/1/if` | Context / conditional | properties: 1 entries (see descendant pointers); required: ["family"] |  |
| `/$defs/document/allOf/1/if/properties/family` | Yes | enum: ["OSTF-Distributed-Session-0.2","OSTF-Distributed-Session-0.3","OSTF-Distributed-Session-0.4"] |  |
| `/$defs/document/allOf/1/then` | Context / conditional | properties: 1 entries (see descendant pointers) |  |
| `/$defs/document/allOf/1/then/properties/role` | No | const: "distributedSession" |  |
| `/$defs/asset` | Context / conditional | type: "object"; additionalProperties: false; properties: 8 entries (see descendant pointers); required: ["id","path","purpose","sha256","mediaType","sizeBytes"] |  |
| `/$defs/asset/properties/id` | Yes | $ref: "#/$defs/id" |  |
| `/$defs/asset/properties/path` | Yes | $ref: "#/$defs/path" |  |
| `/$defs/asset/properties/purpose` | Yes | enum: ["audioSource","pluginState","midi","preset","scoreAttachment","other"] |  |
| `/$defs/asset/properties/sha256` | Yes | $ref: "#/$defs/sha256" |  |
| `/$defs/asset/properties/mediaType` | Yes | type: "string"; minLength: 3 |  |
| `/$defs/asset/properties/sizeBytes` | Yes | type: "integer"; minimum: 0 |  |
| `/$defs/asset/properties/license` | No | type: "string" | Informational claim by the packager only; must not be treated as a license grant. |
| `/$defs/asset/properties/copyright` | No | type: "string" |  |
| `/$defs/binding` | Context / conditional | type: "object"; additionalProperties: false; properties: 4 entries (see descendant pointers); required: ["documentPath","resourceId","assetId","resourceKind"] | Package binding is a byte-resolution map scoped by documentPath; it must not rewrite origin JSON URI fields or imply execution permissions. |
| `/$defs/binding/properties/documentPath` | Yes | $ref: "#/$defs/path" |  |
| `/$defs/binding/properties/resourceId` | Yes | $ref: "#/$defs/id" |  |
| `/$defs/binding/properties/assetId` | Yes | $ref: "#/$defs/id" |  |
| `/$defs/binding/properties/resourceKind` | Yes | enum: ["coreResource","productionAsset"] |  |
| `/$defs/externalAsset` | Context / conditional | type: "object"; additionalProperties: false; properties: 6 entries (see descendant pointers); required: ["id","uri","purpose","onMissing","authorizationRequired"] |  |
| `/$defs/externalAsset/properties/id` | Yes | $ref: "#/$defs/id" |  |
| `/$defs/externalAsset/properties/uri` | Yes | type: "string"; pattern: "^https://" |  |
| `/$defs/externalAsset/properties/sha256` | No | $ref: "#/$defs/sha256" |  |
| `/$defs/externalAsset/properties/purpose` | Yes | type: "string"; minLength: 1 |  |
| `/$defs/externalAsset/properties/onMissing` | Yes | enum: ["warn","fail"] |  |
| `/$defs/externalAsset/properties/authorizationRequired` | Yes | const: true |  |
| `/allOf/0` | Context / conditional | if: 2 entries (see descendant pointers); then: 1 entries (see descendant pointers) |  |
| `/allOf/0/if` | Context / conditional | properties: 1 entries (see descendant pointers); required: ["score"] |  |
| `/allOf/0/if/properties/score` | Yes | properties: 1 entries (see descendant pointers); required: ["version"] |  |
| `/allOf/0/if/properties/score/properties/version` | Yes | const: "4.3.0" |  |
| `/allOf/0/then` | Context / conditional | properties: 1 entries (see descendant pointers) |  |
| `/allOf/0/then/properties/documents` | No | items: 1 entries (see descendant pointers) |  |
| `/allOf/0/then/properties/documents/items` | Context / conditional | allOf: 2 branches (see descendant pointers) |  |
| `/allOf/0/then/properties/documents/items/allOf/0` | Context / conditional | if: 2 entries (see descendant pointers); then: 1 entries (see descendant pointers) |  |
| `/allOf/0/then/properties/documents/items/allOf/0/if` | Context / conditional | properties: 1 entries (see descendant pointers); required: ["role"] |  |
| `/allOf/0/then/properties/documents/items/allOf/0/if/properties/role` | Yes | const: "productionSession" |  |
| `/allOf/0/then/properties/documents/items/allOf/0/then` | Context / conditional | properties: 2 entries (see descendant pointers) |  |
| `/allOf/0/then/properties/documents/items/allOf/0/then/properties/family` | No | const: "OSTF-Production-Session" |  |
| `/allOf/0/then/properties/documents/items/allOf/0/then/properties/version` | No | const: "0.2.0" |  |
| `/allOf/0/then/properties/documents/items/allOf/1` | Context / conditional | if: 2 entries (see descendant pointers); then: 1 entries (see descendant pointers) |  |
| `/allOf/0/then/properties/documents/items/allOf/1/if` | Context / conditional | properties: 1 entries (see descendant pointers); required: ["role"] |  |
| `/allOf/0/then/properties/documents/items/allOf/1/if/properties/role` | Yes | const: "distributedSession" |  |
| `/allOf/0/then/properties/documents/items/allOf/1/then` | Context / conditional | properties: 2 entries (see descendant pointers) |  |
| `/allOf/0/then/properties/documents/items/allOf/1/then/properties/family` | No | const: "OSTF-Distributed-Session-0.2" |  |
| `/allOf/0/then/properties/documents/items/allOf/1/then/properties/version` | No | const: "0.2" |  |
| `/allOf/1` | Context / conditional | if: 2 entries (see descendant pointers); then: 1 entries (see descendant pointers) |  |
| `/allOf/1/if` | Context / conditional | properties: 1 entries (see descendant pointers); required: ["score"] |  |
| `/allOf/1/if/properties/score` | Yes | properties: 1 entries (see descendant pointers); required: ["version"] |  |
| `/allOf/1/if/properties/score/properties/version` | Yes | const: "5.0.0" |  |
| `/allOf/1/then` | Context / conditional | properties: 1 entries (see descendant pointers) |  |
| `/allOf/1/then/properties/documents` | No | items: 1 entries (see descendant pointers) |  |
| `/allOf/1/then/properties/documents/items` | Context / conditional | allOf: 2 branches (see descendant pointers) |  |
| `/allOf/1/then/properties/documents/items/allOf/0` | Context / conditional | if: 2 entries (see descendant pointers); then: 1 entries (see descendant pointers) |  |
| `/allOf/1/then/properties/documents/items/allOf/0/if` | Context / conditional | properties: 1 entries (see descendant pointers); required: ["role"] |  |
| `/allOf/1/then/properties/documents/items/allOf/0/if/properties/role` | Yes | const: "productionSession" |  |
| `/allOf/1/then/properties/documents/items/allOf/0/then` | Context / conditional | properties: 2 entries (see descendant pointers) |  |
| `/allOf/1/then/properties/documents/items/allOf/0/then/properties/family` | No | const: "OSTF-Production-Session" |  |
| `/allOf/1/then/properties/documents/items/allOf/0/then/properties/version` | No | const: "0.3.0" |  |
| `/allOf/1/then/properties/documents/items/allOf/1` | Context / conditional | if: 2 entries (see descendant pointers); then: 1 entries (see descendant pointers) |  |
| `/allOf/1/then/properties/documents/items/allOf/1/if` | Context / conditional | properties: 1 entries (see descendant pointers); required: ["role"] |  |
| `/allOf/1/then/properties/documents/items/allOf/1/if/properties/role` | Yes | const: "distributedSession" |  |
| `/allOf/1/then/properties/documents/items/allOf/1/then` | Context / conditional | properties: 2 entries (see descendant pointers) |  |
| `/allOf/1/then/properties/documents/items/allOf/1/then/properties/family` | No | const: "OSTF-Distributed-Session-0.3" |  |
| `/allOf/1/then/properties/documents/items/allOf/1/then/properties/version` | No | const: "0.3" |  |
| `/allOf/2` | Context / conditional | if: 2 entries (see descendant pointers); then: 1 entries (see descendant pointers) |  |
| `/allOf/2/if` | Context / conditional | properties: 1 entries (see descendant pointers); required: ["score"] |  |
| `/allOf/2/if/properties/score` | Yes | properties: 1 entries (see descendant pointers); required: ["version"] |  |
| `/allOf/2/if/properties/score/properties/version` | Yes | const: "5.1.0" |  |
| `/allOf/2/then` | Context / conditional | properties: 1 entries (see descendant pointers) |  |
| `/allOf/2/then/properties/documents` | No | items: 1 entries (see descendant pointers) |  |
| `/allOf/2/then/properties/documents/items` | Context / conditional | allOf: 2 branches (see descendant pointers) |  |
| `/allOf/2/then/properties/documents/items/allOf/0` | Context / conditional | if: 2 entries (see descendant pointers); then: 1 entries (see descendant pointers) |  |
| `/allOf/2/then/properties/documents/items/allOf/0/if` | Context / conditional | properties: 1 entries (see descendant pointers); required: ["role"] |  |
| `/allOf/2/then/properties/documents/items/allOf/0/if/properties/role` | Yes | const: "productionSession" |  |
| `/allOf/2/then/properties/documents/items/allOf/0/then` | Context / conditional | properties: 2 entries (see descendant pointers) |  |
| `/allOf/2/then/properties/documents/items/allOf/0/then/properties/family` | No | const: "OSTF-Production-Session" |  |
| `/allOf/2/then/properties/documents/items/allOf/0/then/properties/version` | No | const: "0.4.0" |  |
| `/allOf/2/then/properties/documents/items/allOf/1` | Context / conditional | if: 2 entries (see descendant pointers); then: 1 entries (see descendant pointers) |  |
| `/allOf/2/then/properties/documents/items/allOf/1/if` | Context / conditional | properties: 1 entries (see descendant pointers); required: ["role"] |  |
| `/allOf/2/then/properties/documents/items/allOf/1/if/properties/role` | Yes | const: "distributedSession" |  |
| `/allOf/2/then/properties/documents/items/allOf/1/then` | Context / conditional | properties: 2 entries (see descendant pointers) |  |
| `/allOf/2/then/properties/documents/items/allOf/1/then/properties/family` | No | const: "OSTF-Distributed-Session-0.4" |  |
| `/allOf/2/then/properties/documents/items/allOf/1/then/properties/version` | No | const: "0.4" |  |

## ostf-plugin-context-1.1.schema.json

| Schema Pointer | Required in direct parent | Constraints | Original description |
|---|---|---|---|
| `/` | Context / conditional | $schema: "https://json-schema.org/draft/2020-12/schema"; $id: "https://yoh-nak.github.io/ostf/schema/ostf-plugin-context-1.1.schema.json"; type: "object"; additionalProperties: false; properties: 9 entries (see descendant pointers); required: ["protocol","protocolVersion","messageId","operation","score","scope","payload"]; $defs: 8 entries (see descendant pointers); allOf: 5 branches (see descendant pointers) | OSTF Plugin Context Exchange 1.1 |
| `/properties/protocol` | Yes | const: "OSTF-Plugin-Context" |  |
| `/properties/protocolVersion` | Yes | const: "1.1.0" |  |
| `/properties/messageId` | Yes | type: "string"; pattern: "^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$" |  |
| `/properties/operation` | Yes | enum: ["context","editProposal","ack","diagnostic"] |  |
| `/properties/score` | Yes | type: "object"; additionalProperties: false; properties: 5 entries (see descendant pointers); required: ["format","version","sha256"] |  |
| `/properties/score/properties/format` | Yes | const: "OSTF" |  |
| `/properties/score/properties/version` | Yes | enum: ["4.3.0","5.0.0","5.1.0"] |  |
| `/properties/score/properties/sha256` | Yes | type: "string"; pattern: "^[a-f0-9]{64}$" |  |
| `/properties/score/properties/documentId` | No | type: "string"; pattern: "^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$" |  |
| `/properties/score/properties/revisionId` | No | type: "string"; pattern: "^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$" |  |
| `/properties/scope` | Yes | type: "object"; additionalProperties: false; properties: 4 entries (see descendant pointers); required: ["startTick","durationTicks"] | A view filter, not an authorization grant. The authority is the host, never this JSON payload. |
| `/properties/scope/properties/startTick` | Yes | type: "integer"; minimum: 0; maximum: 9007199254740991 |  |
| `/properties/scope/properties/durationTicks` | Yes | type: "integer"; minimum: 1; maximum: 9007199254740991 |  |
| `/properties/scope/properties/trackIds` | No | type: "array"; uniqueItems: true; items: 2 entries (see descendant pointers) |  |
| `/properties/scope/properties/trackIds/items` | Context / conditional | type: "string"; pattern: "^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$" |  |
| `/properties/scope/properties/sectionIds` | No | type: "array"; uniqueItems: true; items: 2 entries (see descendant pointers) |  |
| `/properties/scope/properties/sectionIds/items` | Context / conditional | type: "string"; pattern: "^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$" |  |
| `/properties/transport` | No | type: "object"; additionalProperties: false; properties: 8 entries (see descendant pointers); required: ["isPlaying","positionTick","hostPpq","scorePpq"] |  |
| `/properties/transport/properties/isPlaying` | Yes | type: "boolean" |  |
| `/properties/transport/properties/positionTick` | Yes | type: "integer"; minimum: 0; maximum: 9007199254740991 |  |
| `/properties/transport/properties/hostPpq` | Yes | type: "integer"; minimum: 1; maximum: 9007199254740991 |  |
| `/properties/transport/properties/scorePpq` | Yes | type: "integer"; minimum: 1; maximum: 9007199254740991 |  |
| `/properties/transport/properties/bpm` | No | type: "number"; exclusiveMinimum: 0 |  |
| `/properties/transport/properties/meterNumerator` | No | type: "integer"; minimum: 1 |  |
| `/properties/transport/properties/meterDenominator` | No | type: "integer"; minimum: 1 |  |
| `/properties/transport/properties/loopActive` | No | type: "boolean" |  |
| `/properties/payload` | Yes | type: "object" | Required operation-specific payload; see allOf conditional contracts. |
| `/properties/diagnostics` | No | type: "array"; items: 4 entries (see descendant pointers) |  |
| `/properties/diagnostics/items` | Context / conditional | type: "object"; properties: 3 entries (see descendant pointers); required: ["code","severity"]; additionalProperties: false |  |
| `/properties/diagnostics/items/properties/code` | Yes | type: "string" |  |
| `/properties/diagnostics/items/properties/message` | No | type: "string" |  |
| `/properties/diagnostics/items/properties/severity` | Yes | enum: ["info","warning","error"] |  |
| `/$defs/sha256` | Context / conditional | type: "string"; pattern: "^[0-9a-f]{64}$" |  |
| `/$defs/pointer` | Context / conditional | type: "string"; pattern: "^/"; minLength: 2 | Non-root absolute RFC 6901 JSON Pointer. Syntax and referents require semantic validation; this reusable definition is also used in diagnostics. |
| `/$defs/change` | Context / conditional | type: "object"; additionalProperties: false; properties: 8 entries (see descendant pointers); required: ["op","path"]; allOf: 4 branches (see descendant pointers) |  |
| `/$defs/change/properties/op` | Yes | enum: ["add","replace","remove"] |  |
| `/$defs/change/properties/path` | Yes | $ref: "#/$defs/editPointer51" |  |
| `/$defs/change/properties/targetId` | No | type: "string"; minLength: 1 |  |
| `/$defs/change/properties/containerId` | No | type: "string"; minLength: 1 |  |
| `/$defs/change/properties/newEntityId` | No | type: "string"; minLength: 1 |  |
| `/$defs/change/properties/expected` | No | (schema annotation) | Original JSON value at path, required for replace/remove; compare structurally, without numeric/string coercion. |
| `/$defs/change/properties/value` | No | (schema annotation) | Proposed new JSON value; required for add/replace. |
| `/$defs/change/properties/reason` | No | type: "string" |  |
| `/$defs/change/allOf/0` | Context / conditional | if: 2 entries (see descendant pointers); then: 2 entries (see descendant pointers) |  |
| `/$defs/change/allOf/0/if` | Context / conditional | properties: 1 entries (see descendant pointers); required: ["op"] |  |
| `/$defs/change/allOf/0/if/properties/op` | Yes | const: "add" |  |
| `/$defs/change/allOf/0/then` | Context / conditional | required: ["containerId","newEntityId","value"]; not: 1 entries (see descendant pointers) |  |
| `/$defs/change/allOf/0/then/not` | Context / conditional | required: ["expected"] |  |
| `/$defs/change/allOf/1` | Context / conditional | if: 2 entries (see descendant pointers); then: 1 entries (see descendant pointers) |  |
| `/$defs/change/allOf/1/if` | Context / conditional | properties: 1 entries (see descendant pointers); required: ["op"] |  |
| `/$defs/change/allOf/1/if/properties/op` | Yes | const: "replace" |  |
| `/$defs/change/allOf/1/then` | Context / conditional | required: ["targetId","expected","value"] |  |
| `/$defs/change/allOf/2` | Context / conditional | if: 2 entries (see descendant pointers); then: 2 entries (see descendant pointers) |  |
| `/$defs/change/allOf/2/if` | Context / conditional | properties: 1 entries (see descendant pointers); required: ["op"] |  |
| `/$defs/change/allOf/2/if/properties/op` | Yes | const: "remove" |  |
| `/$defs/change/allOf/2/then` | Context / conditional | required: ["targetId","expected"]; not: 1 entries (see descendant pointers) |  |
| `/$defs/change/allOf/2/then/not` | Context / conditional | required: ["value"] |  |
| `/$defs/change/allOf/3` | Context / conditional | if: 2 entries (see descendant pointers); then: 1 entries (see descendant pointers) |  |
| `/$defs/change/allOf/3/if` | Context / conditional | properties: 1 entries (see descendant pointers); required: ["path"] |  |
| `/$defs/change/allOf/3/if/properties/path` | Yes | pattern: "^/takeGroups/-" |  |
| `/$defs/change/allOf/3/then` | Context / conditional | properties: 2 entries (see descendant pointers) |  |
| `/$defs/change/allOf/3/then/properties/path` | No | const: "/takeGroups/-" |  |
| `/$defs/change/allOf/3/then/properties/op` | No | const: "add" |  |
| `/$defs/contextPayload` | Context / conditional | type: "object"; additionalProperties: false; properties: 3 entries (see descendant pointers); required: ["partial","data"] |  |
| `/$defs/contextPayload/properties/partial` | Yes | const: true |  |
| `/$defs/contextPayload/properties/data` | Yes | type: "object" | Selected musical attributes only; not a standalone valid .ostf document. |
| `/$defs/contextPayload/properties/unavailableFields` | No | type: "array"; items: 1 entries (see descendant pointers) |  |
| `/$defs/contextPayload/properties/unavailableFields/items` | Context / conditional | type: "string" |  |
| `/$defs/proposalPayload` | Context / conditional | type: "object"; additionalProperties: false; properties: 6 entries (see descendant pointers); required: ["proposalId","baseSha256","mode","changes"] | Untrusted atomic proposal checked against one immutable pinned Score. A /takeGroups/- add uses containerId equal to the pinned Score.document.id and envelope score.documentId, with newEntityId equal to value.id. The takeGroups array must already exist. Values must resolve to exact stable IDs and map/source/output edits must remain consistent. |
| `/$defs/proposalPayload/properties/proposalId` | Yes | type: "string"; minLength: 1 |  |
| `/$defs/proposalPayload/properties/baseSha256` | Yes | $ref: "#/$defs/sha256" |  |
| `/$defs/proposalPayload/properties/mode` | Yes | const: "atomic" |  |
| `/$defs/proposalPayload/properties/changes` | Yes | type: "array"; minItems: 1; items: 1 entries (see descendant pointers) |  |
| `/$defs/proposalPayload/properties/changes/items` | Context / conditional | $ref: "#/$defs/change" |  |
| `/$defs/proposalPayload/properties/reason` | No | type: "string"; maxLength: 8000 |  |
| `/$defs/proposalPayload/properties/baseRevisionId` | No | type: "string"; minLength: 1 | Optional Core revision pin; if provided host must compare independently of SHA. |
| `/$defs/ackPayload` | Context / conditional | type: "object"; additionalProperties: false; properties: 5 entries (see descendant pointers); required: ["inReplyTo","status"]; allOf: 3 branches (see descendant pointers) |  |
| `/$defs/ackPayload/properties/inReplyTo` | Yes | type: "string"; minLength: 1 |  |
| `/$defs/ackPayload/properties/status` | Yes | enum: ["received","rejected","applied"] |  |
| `/$defs/ackPayload/properties/effectiveScoreSha256` | No | $ref: "#/$defs/sha256" |  |
| `/$defs/ackPayload/properties/diagnosticCodes` | No | type: "array"; uniqueItems: true; items: 2 entries (see descendant pointers) |  |
| `/$defs/ackPayload/properties/diagnosticCodes/items` | Context / conditional | type: "string"; minLength: 1 |  |
| `/$defs/ackPayload/properties/appliedRevisionId` | No | type: "string"; minLength: 1 | Allowed only when status=applied and persisted new Score revision is known; never state a new revision when merely received/rejected. |
| `/$defs/ackPayload/allOf/0` | Context / conditional | if: 2 entries (see descendant pointers); then: 1 entries (see descendant pointers) |  |
| `/$defs/ackPayload/allOf/0/if` | Context / conditional | properties: 1 entries (see descendant pointers); required: ["status"] |  |
| `/$defs/ackPayload/allOf/0/if/properties/status` | Yes | const: "applied" |  |
| `/$defs/ackPayload/allOf/0/then` | Context / conditional | required: ["effectiveScoreSha256"] |  |
| `/$defs/ackPayload/allOf/1` | Context / conditional | if: 2 entries (see descendant pointers); then: 1 entries (see descendant pointers) |  |
| `/$defs/ackPayload/allOf/1/if` | Context / conditional | properties: 1 entries (see descendant pointers); required: ["status"] |  |
| `/$defs/ackPayload/allOf/1/if/properties/status` | Yes | enum: ["received","rejected"] |  |
| `/$defs/ackPayload/allOf/1/then` | Context / conditional | not: 1 entries (see descendant pointers) |  |
| `/$defs/ackPayload/allOf/1/then/not` | Context / conditional | anyOf: 2 branches (see descendant pointers) |  |
| `/$defs/ackPayload/allOf/1/then/not/anyOf/0` | Context / conditional | required: ["effectiveScoreSha256"] |  |
| `/$defs/ackPayload/allOf/1/then/not/anyOf/1` | Context / conditional | required: ["appliedRevisionId"] |  |
| `/$defs/ackPayload/allOf/2` | Context / conditional | if: 2 entries (see descendant pointers); then: 1 entries (see descendant pointers) |  |
| `/$defs/ackPayload/allOf/2/if` | Context / conditional | properties: 1 entries (see descendant pointers); required: ["status"] |  |
| `/$defs/ackPayload/allOf/2/if/properties/status` | Yes | const: "applied" |  |
| `/$defs/ackPayload/allOf/2/then` | Context / conditional | not: 1 entries (see descendant pointers) |  |
| `/$defs/ackPayload/allOf/2/then/not` | Context / conditional | properties: 1 entries (see descendant pointers) |  |
| `/$defs/ackPayload/allOf/2/then/not/properties/effectiveScoreSha256` | No | const: "0000000000000000000000000000000000000000000000000000000000000000" |  |
| `/$defs/diagnosticPayload` | Context / conditional | type: "object"; additionalProperties: false; properties: 4 entries (see descendant pointers); required: ["status"] |  |
| `/$defs/diagnosticPayload/properties/inReplyTo` | No | type: "string"; minLength: 1 |  |
| `/$defs/diagnosticPayload/properties/status` | Yes | enum: ["invalid","unsupported","stale","scopeViolation","permissionDenied","conflict","informationLoss","internalError"] |  |
| `/$defs/diagnosticPayload/properties/paths` | No | type: "array"; items: 1 entries (see descendant pointers) |  |
| `/$defs/diagnosticPayload/properties/paths/items` | Context / conditional | $ref: "#/$defs/pointer" |  |
| `/$defs/diagnosticPayload/properties/detail` | No | type: "string"; maxLength: 16000 |  |
| `/$defs/editPointer51` | Context / conditional | allOf: 3 branches (see descendant pointers) | Edit roots remain timeline/harmony/tracks/lyrics. Score 5.1 may add or edit individual takeGroups entities. Whole root takeGroups array insertion/replacement is not a protocol operation. The host must initialize an absent array and issue a newly pinned Context. |
| `/$defs/editPointer51/allOf/0` | Context / conditional | $ref: "#/$defs/pointer" |  |
| `/$defs/editPointer51/allOf/1` | Context / conditional | pattern: "^(?:/(?:timeline\|harmony\|tracks\|lyrics)(?:/\|$)\|/takeGroups/(?:0\|[1-9][0-9]*\|-)(?:/\|$))" |  |
| `/$defs/editPointer51/allOf/2` | Context / conditional | pattern: "^(?:/(?:[^~/]\|~[01])*)+$" |  |
| `/allOf/0` | Context / conditional | if: 2 entries (see descendant pointers); then: 1 entries (see descendant pointers) |  |
| `/allOf/0/if` | Context / conditional | properties: 1 entries (see descendant pointers); required: ["operation"] |  |
| `/allOf/0/if/properties/operation` | Yes | const: "context" |  |
| `/allOf/0/then` | Context / conditional | properties: 1 entries (see descendant pointers) |  |
| `/allOf/0/then/properties/payload` | No | $ref: "#/$defs/contextPayload" |  |
| `/allOf/1` | Context / conditional | if: 2 entries (see descendant pointers); then: 1 entries (see descendant pointers) |  |
| `/allOf/1/if` | Context / conditional | properties: 1 entries (see descendant pointers); required: ["operation"] |  |
| `/allOf/1/if/properties/operation` | Yes | const: "editProposal" |  |
| `/allOf/1/then` | Context / conditional | properties: 1 entries (see descendant pointers) |  |
| `/allOf/1/then/properties/payload` | No | $ref: "#/$defs/proposalPayload" |  |
| `/allOf/2` | Context / conditional | if: 2 entries (see descendant pointers); then: 1 entries (see descendant pointers) |  |
| `/allOf/2/if` | Context / conditional | properties: 1 entries (see descendant pointers); required: ["operation"] |  |
| `/allOf/2/if/properties/operation` | Yes | const: "ack" |  |
| `/allOf/2/then` | Context / conditional | properties: 1 entries (see descendant pointers) |  |
| `/allOf/2/then/properties/payload` | No | $ref: "#/$defs/ackPayload" |  |
| `/allOf/3` | Context / conditional | if: 2 entries (see descendant pointers); then: 1 entries (see descendant pointers) |  |
| `/allOf/3/if` | Context / conditional | properties: 1 entries (see descendant pointers); required: ["operation"] |  |
| `/allOf/3/if/properties/operation` | Yes | const: "diagnostic" |  |
| `/allOf/3/then` | Context / conditional | properties: 1 entries (see descendant pointers) |  |
| `/allOf/3/then/properties/payload` | No | $ref: "#/$defs/diagnosticPayload" |  |
| `/allOf/4` | Context / conditional | if: 2 entries (see descendant pointers); then: 1 entries (see descendant pointers) |  |
| `/allOf/4/if` | Context / conditional | properties: 1 entries (see descendant pointers); required: ["operation"] |  |
| `/allOf/4/if/properties/operation` | Yes | const: "editProposal" |  |
| `/allOf/4/then` | Context / conditional | allOf: 2 branches (see descendant pointers) |  |
| `/allOf/4/then/allOf/0` | Context / conditional | if: 2 entries (see descendant pointers); then: 1 entries (see descendant pointers) |  |
| `/allOf/4/then/allOf/0/if` | Context / conditional | properties: 1 entries (see descendant pointers); required: ["score"] |  |
| `/allOf/4/then/allOf/0/if/properties/score` | Yes | properties: 1 entries (see descendant pointers); required: ["version"] |  |
| `/allOf/4/then/allOf/0/if/properties/score/properties/version` | Yes | enum: ["4.3.0","5.0.0"] |  |
| `/allOf/4/then/allOf/0/then` | Context / conditional | properties: 1 entries (see descendant pointers) |  |
| `/allOf/4/then/allOf/0/then/properties/payload` | No | properties: 1 entries (see descendant pointers) |  |
| `/allOf/4/then/allOf/0/then/properties/payload/properties/changes` | No | items: 1 entries (see descendant pointers) |  |
| `/allOf/4/then/allOf/0/then/properties/payload/properties/changes/items` | Context / conditional | properties: 1 entries (see descendant pointers) |  |
| `/allOf/4/then/allOf/0/then/properties/payload/properties/changes/items/properties/path` | No | pattern: "^/(?:timeline\|harmony\|tracks\|lyrics)(?:/\|$)" |  |
| `/allOf/4/then/allOf/1` | Context / conditional | if: 2 entries (see descendant pointers); then: 1 entries (see descendant pointers) |  |
| `/allOf/4/then/allOf/1/if` | Context / conditional | properties: 1 entries (see descendant pointers); required: ["payload"] |  |
| `/allOf/4/then/allOf/1/if/properties/payload` | Yes | properties: 1 entries (see descendant pointers); required: ["changes"] |  |
| `/allOf/4/then/allOf/1/if/properties/payload/properties/changes` | Yes | contains: 2 entries (see descendant pointers); minContains: 1 |  |
| `/allOf/4/then/allOf/1/if/properties/payload/properties/changes/contains` | Context / conditional | properties: 2 entries (see descendant pointers); required: ["op","path"] |  |
| `/allOf/4/then/allOf/1/if/properties/payload/properties/changes/contains/properties/op` | Yes | const: "add" |  |
| `/allOf/4/then/allOf/1/if/properties/payload/properties/changes/contains/properties/path` | Yes | const: "/takeGroups/-" |  |
| `/allOf/4/then/allOf/1/then` | Context / conditional | properties: 1 entries (see descendant pointers) |  |
| `/allOf/4/then/allOf/1/then/properties/score` | No | required: ["documentId"] |  |

## Complete inherited field explanations

The following are publisher-adopted source references. Historical Draft/version/approval labels do not describe current 5.1 status. Current Schema values and explicit 5.1 rules take precedence.


<details>
<summary>Inherited complete Core field reference</summary>

> **Current document edition: Draft 0.69 (unratified).** Older Draft headings and snapshot notes are retained as history. D01–D05 remain pending.

> **Historical editorial snapshot: Draft 0.59 (unratified).** Existing headings referring to earlier Drafts describe cumulative editorial proposals, not competing active document versions. The exact versioned Schemas remain unchanged; the single current release gate is RELEASE_READINESS.md (historical reference: `RELEASE_READINESS.md`). Publisher acceptance D01–D05 is still pending; runtime/independent tests are excluded, not passed.

# OSTF 4.3.0 — Complete Parameter Reference (Draft 0.53 editorial edition; Core Schema unchanged)

Full root and all `$defs`, generated from the actual `schema/ostf-4.3.0.schema.json` of this package. Contains the exact inherited **official** 4.2.0 schema plus 4.3 additions. All object-level constraints are reproduced in JSON blocks. Structural validity does not imply semantic validity or software interoperability.

**Source:** `docs/SOURCE_RECONCILIATION.md` documents the byte-perfect official 4.2 SHA256 match.

Schema definitions: **127**. Root fields: **24**.

## Index

- [Root](#root)
- [id](#def-id)
- [nonnegative](#def-nonnegative)
- [positive](#def-positive)
- [signed](#def-signed)
- [pitch](#def-pitch)
- [ref](#def-ref)
- [range](#def-range)
- [spelledPitchClass](#def-spelledpitchclass)
- [song](#def-song)
- [section](#def-section)
- [tempo](#def-tempo)
- [meter](#def-meter)
- [timeline](#def-timeline)
- [chord](#def-chord)
- [scale](#def-scale)
- [harmony](#def-harmony)
- [instrument](#def-instrument)
- [note](#def-note)
- [clip](#def-clip)
- [track](#def-track)
- [soundSlot](#def-soundslot)
- [lyricDocument](#def-lyricdocument)
- [lyricPhrase](#def-lyricphrase)
- [lyricUnit](#def-lyricunit)
- [lyricAlignment](#def-lyricalignment)
- [lyrics](#def-lyrics)
- [sha256](#def-sha256)
- [resource](#def-resource)
- [dependencies](#def-dependencies)
- [relativeAssignment](#def-relativeassignment)
- [generator](#def-generator)
- [generationInput](#def-generationinput)
- [generationProcess](#def-generationprocess)
- [color](#def-color)
- [roleDefinition](#def-roledefinition)
- [roleColorMap](#def-rolecolormap)
- [customRoleColorMap](#def-customrolecolormap)
- [objectColor](#def-objectcolor)
- [phraseTemplate](#def-phrasetemplate)
- [phraseNoteMapping](#def-phrasenotemapping)
- [phraseInstance](#def-phraseinstance)
- [clipCandidate](#def-clipcandidate)
- [clipChoiceGroup](#def-clipchoicegroup)
- [midiMapping](#def-midimapping)
- [soundSource](#def-soundsource)
- [localizedNames](#def-localizednames)
- [drumKit](#def-drumkit)
- [voicing](#def-voicing)
- [contributor](#def-contributor)
- [credit](#def-credit)
- [alternateTitle](#def-alternatetitle)
- [languageMap32](#def-languagemap32)
- [localizationTarget](#def-localizationtarget)
- [localizationEntry](#def-localizationentry)
- [genre](#def-genre)
- [legacy33](#def-legacy33)
- [opaqueDocumentId](#def-opaquedocumentid)
- [revisionRef](#def-revisionref)
- [software](#def-software)
- [documentInfo](#def-documentinfo)
- [key](#def-key)
- [keyChange](#def-keychange)
- [scaleDefinition](#def-scaledefinition)
- [scaleTarget](#def-scaletarget)
- [mood](#def-mood)
- [rightsStatement](#def-rightsstatement)
- [grooveIntent](#def-grooveintent)
- [generationIntent](#def-generationintent)
- [relativePhrases](#def-relativephrases)
- [generation](#def-generation)
- [presentation](#def-presentation)
- [phraseLibrary](#def-phraselibrary)
- [clipChoices](#def-clipchoices)
- [localization](#def-localization)
- [corePhraseSourceNote](#def-corephrasesourcenote)
- [provenanceSource](#def-provenancesource)
- [provenanceRecord](#def-provenancerecord)
- [provenance](#def-provenance)
- [midiChannel](#def-midichannel)
- [midiBus](#def-midibus)
- [midi](#def-midi)
- [mpeSettings](#def-mpesettings)
- [trackMidi](#def-trackmidi)
- [controlChangeEvent](#def-controlchangeevent)
- [channelModeEvent](#def-channelmodeevent)
- [programChangeEvent](#def-programchangeevent)
- [pitchBendEvent](#def-pitchbendevent)
- [channelPressureEvent](#def-channelpressureevent)
- [polyPressureEvent](#def-polypressureevent)
- [midiEvent](#def-midievent)
- [lyricVoice](#def-lyricvoice)
- [playablePitchRange](#def-playablepitchrange)
- [directionPitchCollection](#def-directionpitchcollection)
- [directionPitchSource](#def-directionpitchsource)
- [improvisationDirectionParameters](#def-improvisationdirectionparameters)
- [playingRoleDirectionParameters](#def-playingroledirectionparameters)
- [pitchRangeDirectionParameters](#def-pitchrangedirectionparameters)
- [vendorDirectionParameters](#def-vendordirectionparameters)
- [improvisationDirection](#def-improvisationdirection)
- [playingRoleDirection](#def-playingroledirection)
- [pitchRangeDirection](#def-pitchrangedirection)
- [vendorRangeDirection](#def-vendorrangedirection)
- [vendorPointDirection](#def-vendorpointdirection)
- [trackDirection](#def-trackdirection)
- [vocalPhonetics](#def-vocalphonetics)
- [vocalProfile](#def-vocalprofile)
- [vocalPerformance](#def-vocalperformance)
- [vocalPhonemeEvent](#def-vocalphonemeevent)
- [vocalCurvePointPitch](#def-vocalcurvepointpitch)
- [vocalCurvePointNormalized](#def-vocalcurvepointnormalized)
- [vocalPitchCurve](#def-vocalpitchcurve)
- [vocalExpressionCurve](#def-vocalexpressioncurve)
- [vocalTechnique](#def-vocaltechnique)
- [vocalBreathEvent](#def-vocalbreathevent)
- [positiveIntRange](#def-positiveintrange)
- [nonnegativeNumberRange](#def-nonnegativenumberrange)
- [phrasingDirectionParameters](#def-phrasingdirectionparameters)
- [phrasingDirection](#def-phrasingdirection)
- [lyricCandidateSet](#def-lyriccandidateset)
- [vocalFreedomDirectionParameters](#def-vocalfreedomdirectionparameters)
- [vocalFreedomDirection](#def-vocalfreedomdirection)
- [performanceRequirements](#def-performancerequirements)
- [performanceScope](#def-performancescope)
- [ensembleInteraction](#def-ensembleinteraction)
- [visitPart](#def-visitpart)
- [performanceVisit](#def-performancevisit)
- [performancePlan](#def-performanceplan)

<a id="root"></a>
## Root

Additive OSTF 4.3 development draft, based on the byte-verified public OSTF 4.2.0 schema. Optional Phrasing, Vocal Freedom, Ensemble Interactions, finite Performance Plans, and musical performance requirements.

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `format` | `const "OSTF"` | Yes |  |
| `version` | `const "4.3.0"` | Yes |  |
| `ppq` | `integer` | Yes |  |
| `song` | `#/$defs/song` | Yes |  |
| `timeline` | `#/$defs/timeline` | Yes |  |
| `harmony` | `#/$defs/harmony` | Yes |  |
| `tracks` | `array<#/$defs/track>` | Yes |  |
| `soundSlots` | `array<#/$defs/soundSlot>` | Yes |  |
| `lyrics` | `#/$defs/lyrics` | Yes |  |
| `resources` | `array<#/$defs/resource>` | Yes |  |
| `extensions` | `#/$defs/legacy33/$defs/extensions` | No/conditional | Optional third-party or verbatim legacy compatibility payloads. Standard Core always remains authoritative. New first-party common information... |
| `drumKits` | `array<#/$defs/drumKit>` | No/conditional | Optional multiple percussion-kit definitions; absent = no declared kits (3.0 compatible). |
| `contributors` | `array<#/$defs/contributor>` | No/conditional | Optional unordered identity records referenced by song.credits. No contributor limit is imposed by this format. |
| `document` | `#/$defs/documentInfo` | No/conditional |  |
| `relativePhrases` | `#/$defs/relativePhrases` | No/conditional |  |
| `generation` | `#/$defs/generation` | No/conditional |  |
| `presentation` | `#/$defs/presentation` | No/conditional |  |
| `phraseLibrary` | `#/$defs/phraseLibrary` | No/conditional |  |
| `clipChoices` | `#/$defs/clipChoices` | No/conditional |  |
| `localization` | `#/$defs/localization` | No/conditional |  |
| `provenance` | `#/$defs/provenance` | No/conditional |  |
| `midi` | `#/$defs/midi` | No/conditional | Optional document-level logical MIDI bus declarations. No physical device or DAW port assignment is encoded. |
| `ensembleInteractions` | `array<#/$defs/ensembleInteraction>` | No/conditional | Optional directed music relationships; these neither materialize notes nor initiate network messages. |
| `performancePlans` | `array<#/$defs/performancePlan>` | No/conditional | Optional finite source-timeline playthroughs; do not modify source timeline or concrete notes. |

### Exact JSON Schema object

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://yoh-nak.github.io/ostf/schema/ostf-4.3.0.schema.json",
  "title": "Open Song Timeline Format (OSTF) 4.3.0 — Draft 0.4",
  "description": "Additive OSTF 4.3 development draft, based on the byte-verified public OSTF 4.2.0 schema. Optional Phrasing, Vocal Freedom, Ensemble Interactions, finite Performance Plans, and musical performance requirements.",
  "$comment": "Unreleased Draft 0.4. The inherited 4.2.0 baseline has published SHA256 6933e2b52332e8b58b9c34b53ca7e101c3f0b689fd5f50f593809480b35e0fa2. See docs/SPECIFICATION.md for normative proposals, and SOURCE_RECONCILIATION.md for source evidence. Not an interoperability certification.",
  "type": "object",
  "properties": {
    "format": {
      "const": "OSTF"
    },
    "version": {
      "const": "4.3.0"
    },
    "ppq": {
      "type": "integer",
      "minimum": 1,
      "maximum": 960000
    },
    "song": {
      "$ref": "#/$defs/song"
    },
    "timeline": {
      "$ref": "#/$defs/timeline"
    },
    "harmony": {
      "$ref": "#/$defs/harmony"
    },
    "tracks": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/track"
      }
    },
    "soundSlots": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/soundSlot"
      }
    },
    "lyrics": {
      "$ref": "#/$defs/lyrics"
    },
    "resources": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/resource"
      }
    },
    "extensions": {
      "$ref": "#/$defs/legacy33/$defs/extensions",
      "description": "Optional third-party or verbatim legacy compatibility payloads. Standard Core always remains authoritative. New first-party common information must not be stored only here."
    },
    "drumKits": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/drumKit"
      },
      "description": "Optional multiple percussion-kit definitions; absent = no declared kits (3.0 compatible)."
    },
    "contributors": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/contributor"
      },
      "description": "Optional unordered identity records referenced by song.credits. No contributor limit is imposed by this format."
    },
    "document": {
      "$ref": "#/$defs/documentInfo"
    },
    "relativePhrases": {
      "$ref": "#/$defs/relativePhrases"
    },
    "generation": {
      "$ref": "#/$defs/generation"
    },
    "presentation": {
      "$ref": "#/$defs/presentation"
    },
    "phraseLibrary": {
      "$ref": "#/$defs/phraseLibrary"
    },
    "clipChoices": {
      "$ref": "#/$defs/clipChoices"
    },
    "localization": {
      "$ref": "#/$defs/localization"
    },
    "provenance": {
      "$ref": "#/$defs/provenance"
    },
    "midi": {
      "$ref": "#/$defs/midi",
      "description": "Optional document-level logical MIDI bus declarations. No physical device or DAW port assignment is encoded."
    },
    "ensembleInteractions": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/ensembleInteraction"
      },
      "description": "Optional directed music relationships; these neither materialize notes nor initiate network messages."
    },
    "performancePlans": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/performancePlan"
      },
      "description": "Optional finite source-timeline playthroughs; do not modify source timeline or concrete notes."
    }
  },
  "required": [
    "format",
    "version",
    "ppq",
    "song",
    "timeline",
    "harmony",
    "tracks",
    "soundSlots",
    "lyrics",
    "resources"
  ],
  "additionalProperties": false,
  "$defs": {
    "id": {
      "type": "string",
      "pattern": "^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$",
      "not": {
        "pattern": "[\\r\\n\\u2028\\u2029]"
      }
    },
    "nonnegative": {
      "type": "integer",
      "minimum": 0,
      "maximum": 9007199254740991
    },
    "positive": {
      "type": "integer",
      "minimum": 1,
      "maximum": 9007199254740991
    },
    "signed": {
      "type": "integer",
      "minimum": -9007199254740991,
      "maximum": 9007199254740991
    },
    "pitch": {
      "type": "integer",
      "minimum": 0,
      "maximum": 127
    },
    "ref": {
      "type": "object",
      "properties": {
        "type": {
          "enum": [
            "section",
            "track",
            "clip",
            "note",
            "chord",
            "scale",
            "soundSlot",
            "drumKit",
            "lyricDocument",
            "lyricPhrase",
            "lyricUnit",
            "lyricAlignment",
            "resource",
            "genre",
            "contributor",
            "credit",
            "alternateTitle",
            "mood",
            "keyChange",
            "phraseTemplate",
            "phraseInstance",
            "clipChoiceGroup",
            "clipCandidate",
            "roleDefinition",
            "generationProcess",
            "provenanceRecord",
            "midiBus",
            "midiEvent",
            "lyricVoice",
            "trackDirection",
            "ensembleInteraction",
            "performancePlan",
            "performanceVisit"
          ]
        },
        "id": {
          "$ref": "#/$defs/id"
        }
      },
      "required": [
        "type",
        "id"
      ],
      "additionalProperties": false
    },
    "range": {
      "type": "object",
      "properties": {
        "start": {
          "$ref": "#/$defs/nonnegative"
        },
        "duration": {
          "$ref": "#/$defs/positive"
        }
      },
      "required": [
        "start",
        "duration"
      ],
      "additionalProperties": false
    },
    "spelledPitchClass": {
      "type": "object",
      "properties": {
        "step": {
          "enum": [
            "A",
            "B",
            "C",
            "D",
            "E",
            "F",
            "G"
          ]
        },
        "alter": {
          "type": "integer",
          "minimum": -2,
          "maximum": 2
        }
      },
      "required": [
        "step",
        "alter"
      ],
      "additionalProperties": false
    },
    "song": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string"
        },
        "primaryMelodyTrackId": {
          "$ref": "#/$defs/id"
        },
        "localizedTitles": {
          "$ref": "#/$defs/localizedNames",
          "description": "Optional localized song-title alternatives. song.title is the stable fallback."
        },
        "subtitle": {
          "type": "string",
          "description": "Optional original-language subtitle."
        },
        "description": {
          "type": "string",
          "description": "Optional original-language description, including Unicode and line breaks."
        },
        "alternateTitles": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/alternateTitle"
          },
          "description": "Additional stable-ID source-language titles."
        },
        "credits": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/credit"
          },
          "description": "Ordered credit assignments to contributors. Multiple roles and duplicate contributors permitted."
        },
        "genres": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/genre"
          },
          "description": "Optional open-ended ordered genre tags; zero or more allowed. Order is authored display preference, first item is primary if a primary label is desired, not a generator weight. Absent means unspecified."
        },
        "key": {
          "$ref": "#/$defs/key"
        },
        "scale": {
          "$ref": "#/$defs/scaleDefinition"
        },
        "languages": {
          "type": "array",
          "items": {
            "type": "string",
            "minLength": 1,
            "description": "Authored language tag, preferably BCP 47. Unknown spelling is retained; case-insensitive duplicate tags forbidden."
          },
          "uniqueItems": true
        },
        "primaryLyricDocumentId": {
          "$ref": "#/$defs/id"
        },
        "moods": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/mood"
          }
        },
        "rights": {
          "$ref": "#/$defs/rightsStatement"
        },
        "melodyTrackIds": {
          "type": "array",
          "uniqueItems": true,
          "items": {
            "$ref": "#/$defs/id"
          },
          "description": "Optional ordered set of tracks explicitly authored as melody-bearing tracks. If present with primaryMelodyTrackId, the primary track must be a member."
        }
      },
      "required": [
        "title"
      ],
      "additionalProperties": false
    },
    "section": {
      "type": "object",
      "properties": {
        "id": {
          "$ref": "#/$defs/id"
        },
        "name": {
          "type": "string",
          "minLength": 1
        },
        "start": {
          "$ref": "#/$defs/nonnegative"
        },
        "duration": {
          "$ref": "#/$defs/positive"
        },
        "role": {
          "type": "string"
        },
        "localizedNames": {
          "$ref": "#/$defs/localizedNames",
          "description": "Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity."
        }
      },
      "required": [
        "id",
        "name",
        "start",
        "duration"
      ],
      "additionalProperties": false
    },
    "tempo": {
      "type": "object",
      "properties": {
        "at": {
          "$ref": "#/$defs/nonnegative"
        },
        "bpm": {
          "type": "number",
          "exclusiveMinimum": 0,
          "maximum": 1000
        }
      },
      "required": [
        "at",
        "bpm"
      ],
      "additionalProperties": false
    },
    "meter": {
      "type": "object",
      "properties": {
        "at": {
          "$ref": "#/$defs/nonnegative"
        },
        "numerator": {
          "type": "integer",
          "minimum": 1,
          "maximum": 64
        },
        "denominator": {
          "enum": [
            1,
            2,
            4,
            8,
            16,
            32,
            64
          ],
          "type": "integer"
        },
        "beatGroups": {
          "type": "array",
          "items": {
            "type": "integer",
            "minimum": 1,
            "maximum": 64
          },
          "minItems": 1,
          "maxItems": 64,
          "description": "Optional additive grouping in denominator units. Values must sum to numerator. Descriptive only; does not change note timestamps."
        }
      },
      "required": [
        "at",
        "numerator",
        "denominator"
      ],
      "additionalProperties": false
    },
    "timeline": {
      "type": "object",
      "properties": {
        "sections": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/section"
          }
        },
        "tempoChanges": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/tempo"
          },
          "minItems": 1
        },
        "meterChanges": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/meter"
          },
          "minItems": 1
        },
        "keyChanges": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/keyChange"
          }
        },
        "duration": {
          "$ref": "#/$defs/nonnegative"
        },
        "barOrigin": {
          "$ref": "#/$defs/nonnegative"
        }
      },
      "required": [
        "sections",
        "tempoChanges",
        "meterChanges"
      ],
      "additionalProperties": false
    },
    "chord": {
      "type": "object",
      "properties": {
        "id": {
          "$ref": "#/$defs/id"
        },
        "start": {
          "$ref": "#/$defs/nonnegative"
        },
        "duration": {
          "$ref": "#/$defs/positive"
        },
        "label": {
          "type": "string",
          "minLength": 1
        },
        "root": {
          "$ref": "#/$defs/spelledPitchClass"
        },
        "intervals": {
          "type": "array",
          "items": {
            "type": "integer",
            "minimum": 0,
            "maximum": 35
          },
          "minItems": 1,
          "maxItems": 36,
          "uniqueItems": true,
          "contains": {
            "const": 0
          }
        },
        "bass": {
          "$ref": "#/$defs/spelledPitchClass"
        },
        "voicing": {
          "$ref": "#/$defs/voicing",
          "description": "Optional pitch snapshot (not an arrangement note sequence). No automatic playback."
        }
      },
      "required": [
        "id",
        "start",
        "duration",
        "label"
      ],
      "additionalProperties": false,
      "dependentRequired": {
        "root": [
          "intervals"
        ],
        "intervals": [
          "root"
        ]
      }
    },
    "scale": {
      "type": "object",
      "properties": {
        "id": {
          "$ref": "#/$defs/id"
        },
        "start": {
          "$ref": "#/$defs/nonnegative"
        },
        "duration": {
          "$ref": "#/$defs/positive"
        },
        "label": {
          "type": "string"
        },
        "tonic": {
          "$ref": "#/$defs/spelledPitchClass"
        },
        "intervals": {
          "type": "array",
          "items": {
            "type": "integer",
            "minimum": 0,
            "maximum": 11
          },
          "minItems": 1,
          "maxItems": 12,
          "uniqueItems": true,
          "contains": {
            "const": 0
          }
        },
        "targets": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/scaleTarget"
          },
          "minItems": 1,
          "uniqueItems": true,
          "description": "Optional explicit scope. Absence means general timed context, not a global key. Overlapping contexts are not resolved by array order."
        }
      },
      "required": [
        "id",
        "start",
        "duration",
        "tonic",
        "intervals"
      ],
      "additionalProperties": false
    },
    "harmony": {
      "type": "object",
      "properties": {
        "chords": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/chord"
          }
        },
        "scales": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/scale"
          }
        }
      },
      "required": [
        "chords",
        "scales"
      ],
      "additionalProperties": false
    },
    "instrument": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "family": {
          "type": "string"
        },
        "localizedNames": {
          "$ref": "#/$defs/localizedNames",
          "description": "Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity."
        },
        "playablePitchRange": {
          "$ref": "#/$defs/playablePitchRange"
        }
      },
      "required": [
        "name"
      ],
      "additionalProperties": false
    },
    "note": {
      "type": "object",
      "properties": {
        "id": {
          "$ref": "#/$defs/id"
        },
        "start": {
          "$ref": "#/$defs/signed"
        },
        "duration": {
          "$ref": "#/$defs/positive",
          "description": "Positive note gate in ticks, not the guaranteed audible duration of a one-shot percussion sample."
        },
        "pitch": {
          "$ref": "#/$defs/pitch"
        },
        "soundSlotId": {
          "$ref": "#/$defs/id",
          "description": "Document-local Sound Slot ID. Distinct events and IDs stay distinct even if several slots share a MIDI key; a renderer decides the acoustic timbre."
        },
        "velocity": {
          "type": "integer",
          "minimum": 1,
          "maximum": 127,
          "description": "Optional authored note-on velocity for performed Core notes, 1–127; omit to mean unspecified. It is not a note-off velocity, controller stream, chord tone, or a sound-rendering guarantee. Never insert an inferred default when saving."
        },
        "enabled": {
          "type": "boolean",
          "default": true,
          "description": "Optional note-local enable state. Omitted means enabled. False preserves the note but suppresses scheduling/playback; it is distinct from probability=0."
        },
        "releaseVelocity": {
          "type": "integer",
          "minimum": 0,
          "maximum": 127,
          "description": "Optional MIDI Note Off/release velocity, 0-127. Omit when unspecified; readers must not invent and write back a default."
        },
        "probability": {
          "type": "number",
          "minimum": 0,
          "maximum": 1,
          "default": 1,
          "description": "Optional note-playback probability from 0.0 to 1.0. Omitted means 1.0. Random sequence identity is not standardized; materialize notes for deterministic interchange."
        },
        "velocityDeviation": {
          "type": "integer",
          "minimum": -126,
          "maximum": 126,
          "default": 0,
          "description": "Optional note-local velocity variation endpoint relative to velocity. Requires velocity. Semantic rule: velocity + velocityDeviation must remain within 1..127. Omitted means 0."
        },
        "pitchRole": {
          "enum": [
            "musical",
            "fixedTrigger"
          ],
          "default": "musical",
          "description": "Meaning of a pitch note. musical participates in pitch/harmony/transpose operations; fixedTrigger is an exact MIDI key trigger (for example a keyswitch) and is never transposed or used as musical-pitch evidence. Allowed only on pitch notes."
        },
        "channel": {
          "$ref": "#/$defs/midiChannel",
          "description": "Optional concrete MIDI channel for this performed note. In singleChannel mode it may be omitted and inherited from the track; in multiChannel/MPE mode semantic rules require explicit channel where channel identity matters."
        }
      },
      "required": [
        "id",
        "start",
        "duration"
      ],
      "additionalProperties": false,
      "oneOf": [
        {
          "required": [
            "pitch"
          ],
          "not": {
            "required": [
              "soundSlotId"
            ]
          }
        },
        {
          "required": [
            "soundSlotId"
          ],
          "not": {
            "required": [
              "pitch"
            ]
          }
        }
      ],
      "description": "Concrete Core DAW-note event. The event target is pitch or soundSlotId. Optional 3.5 note-local properties preserve mute, release velocity, probability and velocity variation. pitchRole=fixedTrigger marks a literal MIDI key trigger that must not be musically transposed or analyzed.",
      "dependentRequired": {
        "velocityDeviation": [
          "velocity"
        ]
      },
      "allOf": [
        {
          "if": {
            "required": [
              "soundSlotId"
            ]
          },
          "then": {
            "not": {
              "required": [
                "pitchRole"
              ]
            }
          }
        }
      ]
    },
    "clip": {
      "type": "object",
      "properties": {
        "id": {
          "$ref": "#/$defs/id"
        },
        "name": {
          "type": "string"
        },
        "start": {
          "$ref": "#/$defs/nonnegative"
        },
        "duration": {
          "$ref": "#/$defs/positive"
        },
        "enabled": {
          "type": "boolean",
          "default": true
        },
        "notes": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/note"
          }
        },
        "localizedNames": {
          "$ref": "#/$defs/localizedNames",
          "description": "Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity."
        },
        "midiEvents": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/midiEvent"
          },
          "description": "Optional clip-local MIDI performance/control events. start is local to the clip and may be negative if absolute time remains nonnegative. Notes remain authoritative in notes[]."
        },
        "vocalPerformances": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/vocalPerformance"
          },
          "minItems": 1,
          "description": "Optional voice-specific phoneme and singing-performance data; references lyrics.voices. Notes/MIDI remain authoritative for MIDI playback."
        }
      },
      "required": [
        "id",
        "start",
        "duration",
        "notes"
      ],
      "additionalProperties": false
    },
    "track": {
      "type": "object",
      "properties": {
        "id": {
          "$ref": "#/$defs/id"
        },
        "name": {
          "type": "string"
        },
        "role": {
          "type": "string"
        },
        "instrument": {
          "$ref": "#/$defs/instrument"
        },
        "enabled": {
          "type": "boolean",
          "default": true
        },
        "clips": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/clip"
          }
        },
        "trackType": {
          "enum": [
            "melodic",
            "drum",
            "mixed"
          ],
          "description": "Semantic event-target category; optional; missing/empty-note tracks may be unknown. It is not a DAW track class."
        },
        "preferredView": {
          "enum": [
            "auto",
            "pianoRoll",
            "drumGrid"
          ],
          "default": "auto",
          "description": "Non-binding presentation preference. Does not change note meaning."
        },
        "soundSource": {
          "$ref": "#/$defs/soundSource",
          "description": "Optional sound-source selection hint, not a plug-in state, preset blob, or sound guarantee."
        },
        "localizedNames": {
          "$ref": "#/$defs/localizedNames",
          "description": "Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity."
        },
        "drumKitId": {
          "$ref": "#/$defs/id",
          "description": "Optional reference to a declared drumKit; only for a drum/mixed or empty inferred track. All stored slot events in the track must belong to the referenced kit."
        },
        "midi": {
          "$ref": "#/$defs/trackMidi"
        },
        "directions": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/trackDirection"
          },
          "description": "Optional typed semantic instructions for performance, interpretation, or generation. Uses the global OSTF timebase; it is not a second timeline."
        },
        "performanceRequirements": {
          "$ref": "#/$defs/performanceRequirements",
          "description": "Portable requirements for realizing this track, not a robot/device capability report."
        }
      },
      "required": [
        "id",
        "name",
        "clips"
      ],
      "additionalProperties": false,
      "allOf": [
        {
          "if": {
            "properties": {
              "trackType": {
                "const": "melodic"
              }
            },
            "required": [
              "trackType"
            ]
          },
          "then": {
            "not": {
              "required": [
                "drumKitId"
              ]
            }
          }
        }
      ]
    },
    "soundSlot": {
      "type": "object",
      "properties": {
        "id": {
          "$ref": "#/$defs/id"
        },
        "name": {
          "type": "string"
        },
        "role": {
          "type": "string",
          "description": "Optional free-text musical role; not a standardized GM instrument code or an acoustic sample identifier."
        },
        "midiNote": {
          "$ref": "#/$defs/pitch",
          "description": "Legacy 3.0 MIDI note hint only; not a GM1 declaration or preview timbre identity."
        },
        "midiMapping": {
          "$ref": "#/$defs/midiMapping",
          "description": "Explicit external MIDI1 output mapping; standard=gm1 is separate from custom even for an equal note number. Not a unique slot or audio identity."
        },
        "localizedNames": {
          "$ref": "#/$defs/localizedNames",
          "description": "Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity."
        }
      },
      "required": [
        "id",
        "name"
      ],
      "additionalProperties": false,
      "description": "Document-local stable logical percussion target. Equal roles, names or MIDI note mappings never merge distinct slot IDs. No sample/audio identity is encoded."
    },
    "lyricDocument": {
      "type": "object",
      "properties": {
        "id": {
          "$ref": "#/$defs/id"
        },
        "title": {
          "type": "string"
        },
        "language": {
          "type": "string"
        }
      },
      "required": [
        "id"
      ],
      "additionalProperties": false
    },
    "lyricPhrase": {
      "type": "object",
      "properties": {
        "id": {
          "$ref": "#/$defs/id"
        },
        "documentId": {
          "$ref": "#/$defs/id"
        },
        "text": {
          "type": "string"
        },
        "pronunciation": {
          "type": "string"
        },
        "start": {
          "$ref": "#/$defs/nonnegative"
        },
        "duration": {
          "$ref": "#/$defs/positive"
        }
      },
      "required": [
        "id",
        "documentId",
        "text"
      ],
      "additionalProperties": false,
      "dependentRequired": {
        "start": [
          "duration"
        ],
        "duration": [
          "start"
        ]
      }
    },
    "lyricUnit": {
      "type": "object",
      "properties": {
        "id": {
          "$ref": "#/$defs/id"
        },
        "phraseId": {
          "$ref": "#/$defs/id"
        },
        "text": {
          "type": "string"
        },
        "pronunciation": {
          "type": "string"
        },
        "start": {
          "$ref": "#/$defs/nonnegative"
        },
        "duration": {
          "$ref": "#/$defs/positive"
        },
        "phonetics": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/vocalPhonetics"
          },
          "minItems": 1,
          "description": "Optional alternate phoneme token sequences. Do not alter text/pronunciation. Multiple alphabets are permitted."
        }
      },
      "required": [
        "id",
        "phraseId",
        "text"
      ],
      "additionalProperties": false,
      "dependentRequired": {
        "start": [
          "duration"
        ],
        "duration": [
          "start"
        ]
      }
    },
    "lyricAlignment": {
      "type": "object",
      "properties": {
        "id": {
          "$ref": "#/$defs/id"
        },
        "unitIds": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/id"
          },
          "uniqueItems": true,
          "minItems": 1
        },
        "noteIds": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/id"
          },
          "uniqueItems": true,
          "minItems": 1
        },
        "voiceId": {
          "$ref": "#/$defs/id",
          "description": "Optional lyricVoice association. When present, aligned units must belong to that voice document and aligned notes must belong to that voice track."
        }
      },
      "required": [
        "id",
        "unitIds",
        "noteIds"
      ],
      "additionalProperties": false
    },
    "lyrics": {
      "type": "object",
      "properties": {
        "documents": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/lyricDocument"
          }
        },
        "phrases": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/lyricPhrase"
          }
        },
        "units": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/lyricUnit"
          }
        },
        "alignments": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/lyricAlignment"
          }
        },
        "voices": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/lyricVoice"
          },
          "description": "Optional explicit vocal-part relationships for multi-voice, harmony and chorus lyrics."
        }
      },
      "required": [
        "documents",
        "phrases",
        "units",
        "alignments"
      ],
      "additionalProperties": false
    },
    "sha256": {
      "type": "string",
      "pattern": "^[0-9a-f]{64}$",
      "not": {
        "pattern": "[\\r\\n\\u2028\\u2029]"
      }
    },
    "resource": {
      "type": "object",
      "properties": {
        "id": {
          "$ref": "#/$defs/id"
        },
        "kind": {
          "enum": [
            "audio",
            "midi",
            "text",
            "other"
          ]
        },
        "uri": {
          "type": "string",
          "minLength": 1
        },
        "name": {
          "type": "string"
        },
        "sha256": {
          "$ref": "#/$defs/sha256"
        }
      },
      "required": [
        "id",
        "kind",
        "uri"
      ],
      "additionalProperties": false
    },
    "dependencies": {
      "oneOf": [
        {
          "type": "object",
          "properties": {
            "scope": {
              "enum": [
                "document",
                "none"
              ]
            }
          },
          "required": [
            "scope"
          ],
          "additionalProperties": false
        },
        {
          "type": "object",
          "properties": {
            "scope": {
              "const": "objects"
            },
            "refs": {
              "type": "array",
              "items": {
                "$ref": "#/$defs/ref"
              },
              "minItems": 1,
              "uniqueItems": true
            }
          },
          "required": [
            "scope",
            "refs"
          ],
          "additionalProperties": false
        }
      ]
    },
    "relativeAssignment": {
      "type": "object",
      "properties": {
        "noteId": {
          "$ref": "#/$defs/id"
        },
        "basis": {
          "enum": [
            "chordTone",
            "scaleDegree"
          ]
        },
        "contextId": {
          "$ref": "#/$defs/id"
        },
        "anchorPitch": {
          "$ref": "#/$defs/pitch"
        },
        "index": {
          "type": "integer",
          "minimum": 1,
          "maximum": 36
        },
        "chromaticOffset": {
          "type": "integer",
          "minimum": -24,
          "maximum": 24
        }
      },
      "required": [
        "noteId",
        "basis",
        "contextId",
        "anchorPitch",
        "index",
        "chromaticOffset"
      ],
      "additionalProperties": false,
      "allOf": [
        {
          "if": {
            "properties": {
              "basis": {
                "const": "scaleDegree"
              }
            },
            "required": [
              "basis"
            ]
          },
          "then": {
            "properties": {
              "index": {
                "maximum": 12
              }
            }
          }
        }
      ]
    },
    "generator": {
      "type": "object",
      "properties": {
        "id": {
          "type": "string",
          "minLength": 1
        },
        "version": {
          "type": "string",
          "minLength": 1
        }
      },
      "required": [
        "id",
        "version"
      ],
      "additionalProperties": false
    },
    "generationInput": {
      "type": "object",
      "properties": {
        "role": {
          "type": "string",
          "minLength": 1
        },
        "ref": {
          "$ref": "#/$defs/ref"
        },
        "readRange": {
          "$ref": "#/$defs/range"
        }
      },
      "required": [
        "role",
        "ref"
      ],
      "additionalProperties": false
    },
    "generationProcess": {
      "type": "object",
      "properties": {
        "id": {
          "$ref": "#/$defs/id"
        },
        "generator": {
          "$ref": "#/$defs/generator"
        },
        "inputs": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/generationInput"
          }
        },
        "outputs": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/ref"
          },
          "minItems": 1
        },
        "targetRange": {
          "$ref": "#/$defs/range"
        },
        "protectedNoteIds": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/id"
          },
          "uniqueItems": true
        },
        "intent": {
          "$ref": "#/$defs/generationIntent"
        }
      },
      "required": [
        "id",
        "generator",
        "inputs",
        "outputs",
        "protectedNoteIds"
      ],
      "additionalProperties": false
    },
    "color": {
      "type": "string",
      "pattern": "^#[0-9A-Fa-f]{6}$",
      "not": {
        "pattern": "[\\r\\n\\u2028\\u2029]"
      }
    },
    "roleDefinition": {
      "type": "object",
      "properties": {
        "id": {
          "$ref": "#/$defs/id"
        },
        "name": {
          "type": "string",
          "minLength": 1
        },
        "baseRole": {
          "type": "string"
        }
      },
      "required": [
        "id",
        "name"
      ],
      "additionalProperties": false
    },
    "roleColorMap": {
      "type": "object",
      "additionalProperties": {
        "$ref": "#/$defs/color"
      }
    },
    "customRoleColorMap": {
      "type": "object",
      "propertyNames": {
        "$ref": "#/$defs/id"
      },
      "additionalProperties": {
        "$ref": "#/$defs/color"
      }
    },
    "objectColor": {
      "type": "object",
      "properties": {
        "target": {
          "$ref": "#/$defs/ref"
        },
        "color": {
          "$ref": "#/$defs/color"
        }
      },
      "required": [
        "target",
        "color"
      ],
      "additionalProperties": false
    },
    "phraseTemplate": {
      "type": "object",
      "properties": {
        "id": {
          "$ref": "#/$defs/id"
        },
        "duration": {
          "$ref": "#/$defs/positive"
        },
        "notes": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/corePhraseSourceNote"
          }
        },
        "name": {
          "type": "string"
        }
      },
      "required": [
        "id",
        "duration",
        "notes"
      ],
      "additionalProperties": false
    },
    "phraseNoteMapping": {
      "type": "object",
      "properties": {
        "templateNoteId": {
          "$ref": "#/$defs/id"
        },
        "repeatIndex": {
          "$ref": "#/$defs/nonnegative"
        },
        "noteId": {
          "$ref": "#/$defs/id"
        }
      },
      "required": [
        "templateNoteId",
        "repeatIndex",
        "noteId"
      ],
      "additionalProperties": false
    },
    "phraseInstance": {
      "type": "object",
      "properties": {
        "id": {
          "$ref": "#/$defs/id"
        },
        "templateId": {
          "$ref": "#/$defs/id"
        },
        "clipId": {
          "$ref": "#/$defs/id"
        },
        "repeatCount": {
          "$ref": "#/$defs/positive"
        },
        "transpose": {
          "type": "integer",
          "minimum": -127,
          "maximum": 127
        },
        "noteMap": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/phraseNoteMapping"
          }
        },
        "velocityMode": {
          "enum": [
            "independent",
            "linked"
          ],
          "default": "independent",
          "description": "independent preserves concrete velocities on refresh; linked requires exact presence/value equality with the template. This field does not trigger refresh on load."
        },
        "noteStateMode": {
          "enum": [
            "independent",
            "linked"
          ],
          "default": "independent",
          "description": "Controls enabled/releaseVelocity/probability/velocityDeviation after materialization. independent preserves concrete note-state values on refresh; linked requires exact presence/value equality with the template. pitchRole is structural and must always remain semantically equal between a source pitch note and its mapped concrete note."
        }
      },
      "required": [
        "id",
        "templateId",
        "clipId",
        "repeatCount",
        "transpose",
        "noteMap"
      ],
      "additionalProperties": false
    },
    "clipCandidate": {
      "type": "object",
      "properties": {
        "id": {
          "$ref": "#/$defs/id"
        },
        "clipIds": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/id"
          },
          "uniqueItems": true
        },
        "name": {
          "type": "string"
        }
      },
      "required": [
        "id",
        "clipIds"
      ],
      "additionalProperties": false
    },
    "clipChoiceGroup": {
      "type": "object",
      "properties": {
        "id": {
          "$ref": "#/$defs/id"
        },
        "candidates": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/clipCandidate"
          },
          "minItems": 1
        },
        "selectedCandidateId": {
          "anyOf": [
            {
              "$ref": "#/$defs/id"
            },
            {
              "type": "null"
            }
          ]
        },
        "name": {
          "type": "string"
        }
      },
      "required": [
        "id",
        "candidates",
        "selectedCandidateId"
      ],
      "additionalProperties": false
    },
    "midiMapping": {
      "type": "object",
      "properties": {
        "standard": {
          "enum": [
            "gm1",
            "custom"
          ],
          "description": "gm1=GM Level 1 percussion key 35..81; custom=explicit arbitrary MIDI1 note number."
        },
        "note": {
          "$ref": "#/$defs/pitch",
          "description": "MIDI1 note number in 0..127; for gm1 restrict to 35..81."
        }
      },
      "required": [
        "standard",
        "note"
      ],
      "additionalProperties": false,
      "allOf": [
        {
          "if": {
            "properties": {
              "standard": {
                "const": "gm1"
              }
            },
            "required": [
              "standard"
            ]
          },
          "then": {
            "properties": {
              "note": {
                "type": "integer",
                "minimum": 35,
                "maximum": 81
              }
            }
          }
        }
      ]
    },
    "soundSource": {
      "type": "object",
      "description": "Optional informational rendering class or opaque destination hint. In OSTF 4.0, track.midi.busId is the Core logical MIDI routing reference; soundSource does not bind a physical device, plugin state or preset.",
      "properties": {
        "kind": {
          "enum": [
            "unassigned",
            "gm1",
            "externalMidi",
            "plugin",
            "hostManaged"
          ]
        },
        "identifier": {
          "type": "string",
          "minLength": 1,
          "description": "Opaque informational target identifier (for example a URI or plug-in identifier), not a physical MIDI-port binding or loading command."
        }
      },
      "required": [
        "kind"
      ],
      "additionalProperties": false,
      "allOf": [
        {
          "if": {
            "properties": {
              "kind": {
                "enum": [
                  "gm1",
                  "unassigned"
                ]
              }
            },
            "required": [
              "kind"
            ]
          },
          "then": {
            "not": {
              "required": [
                "identifier"
              ]
            }
          }
        }
      ]
    },
    "localizedNames": {
      "type": "object",
      "minProperties": 1,
      "propertyNames": {
        "type": "string",
        "pattern": "^(?:[A-Za-z]{2,3}|[A-Za-z]{5,8})(?:-[A-Za-z0-9]{2,8})*$"
      },
      "additionalProperties": {
        "type": "string",
        "minLength": 1
      },
      "description": "Optional translations indexed by a conservative BCP 47 language-tag subset. The original name/title remains authoritative and is never rewritten by locale changes. Case-insensitive duplicate tags are forbidden semantically."
    },
    "drumKit": {
      "type": "object",
      "description": "Optional named ordered membership of global Sound Slot IDs. Does not define plugin preset, sample loading, choke or a kit-local MIDI remapping.",
      "properties": {
        "id": {
          "$ref": "#/$defs/id"
        },
        "name": {
          "type": "string"
        },
        "localizedNames": {
          "$ref": "#/$defs/localizedNames"
        },
        "soundSlotIds": {
          "type": "array",
          "uniqueItems": true,
          "items": {
            "$ref": "#/$defs/id"
          },
          "description": "Ordered, unique references to global soundSlots; may be empty."
        }
      },
      "required": [
        "id",
        "name",
        "soundSlotIds"
      ],
      "additionalProperties": false
    },
    "voicing": {
      "type": "object",
      "additionalProperties": false,
      "description": "Optional informational chord voicing snapshot, not a played Core note collection. Repeated pitches and original array order have meaning for lossless preservation. Per-entry velocity is an optional voicing-preview hint.",
      "properties": {
        "pitches": {
          "type": "array",
          "minItems": 1,
          "items": {
            "$ref": "#/$defs/pitch"
          },
          "description": "Ordered multiset of concrete absolute pitches, 0-127. Duplicates allowed."
        },
        "velocities": {
          "type": "array",
          "minItems": 1,
          "items": {
            "anyOf": [
              {
                "type": "integer",
                "minimum": 1,
                "maximum": 127
              },
              {
                "type": "null"
              }
            ]
          },
          "description": "Optional positional velocities aligned one-to-one to pitches. Null means unspecified at this index, not 0. Exact equal-length rule is semantic."
        }
      },
      "required": [
        "pitches"
      ]
    },
    "contributor": {
      "type": "object",
      "additionalProperties": false,
      "description": "One song-local identity; same contributor can receive multiple credit roles. Unicode source name is authoritative.",
      "properties": {
        "id": {
          "$ref": "#/$defs/id"
        },
        "name": {
          "type": "string",
          "minLength": 1
        },
        "kind": {
          "enum": [
            "person",
            "organization",
            "other"
          ]
        },
        "localizedNames": {
          "$ref": "#/$defs/localizedNames"
        }
      },
      "required": [
        "id",
        "name"
      ]
    },
    "credit": {
      "type": "object",
      "additionalProperties": false,
      "description": "Ordered credit assignment referencing one contributor; role is an open semantic token, not a translated label.",
      "properties": {
        "id": {
          "$ref": "#/$defs/id"
        },
        "contributorId": {
          "$ref": "#/$defs/id"
        },
        "role": {
          "type": "string",
          "pattern": "^[a-z][a-z0-9.-]*$"
        },
        "label": {
          "type": "string"
        }
      },
      "required": [
        "id",
        "contributorId",
        "role"
      ]
    },
    "alternateTitle": {
      "type": "object",
      "additionalProperties": false,
      "description": "Stable-ID song title alternative; array position and title text do not identify it.",
      "properties": {
        "id": {
          "$ref": "#/$defs/id"
        },
        "title": {
          "type": "string",
          "minLength": 1
        }
      },
      "required": [
        "id",
        "title"
      ]
    },
    "languageMap32": {
      "type": "object",
      "minProperties": 1,
      "propertyNames": {
        "type": "string",
        "pattern": "^[A-Za-z]{1,8}(?:-[A-Za-z0-9]{1,8})*$"
      },
      "additionalProperties": {
        "type": "string"
      },
      "description": "Open BCP 47 language-tag dictionary. Schema checks loose subtag structure; full BCP 47 well-formedness and case-insensitive uniqueness are semantic requirements. String may be empty if intentionally blank."
    },
    "localizationTarget": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "kind": {
          "enum": [
            "song",
            "alternateTitle",
            "contributor",
            "credit",
            "section",
            "track",
            "clip",
            "soundSlot",
            "drumKit",
            "lyricDocument",
            "resource",
            "phraseTemplate",
            "clipCandidate",
            "clipChoiceGroup",
            "roleDefinition",
            "genre",
            "mood",
            "keyChange",
            "scale",
            "midiBus",
            "lyricVoice"
          ]
        },
        "id": {
          "$ref": "#/$defs/id"
        }
      },
      "required": [
        "kind"
      ],
      "allOf": [
        {
          "if": {
            "properties": {
              "kind": {
                "const": "song"
              }
            },
            "required": [
              "kind"
            ]
          },
          "then": {
            "not": {
              "required": [
                "id"
              ]
            }
          },
          "else": {
            "required": [
              "id"
            ]
          }
        }
      ],
      "description": "Core target; song is ID-less, all others use global Core ID. No namespace/profile selector."
    },
    "localizationEntry": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "target": {
          "$ref": "#/$defs/localizationTarget"
        },
        "field": {
          "type": "string",
          "minLength": 1,
          "description": "Exact allowed source text field for this target kind (see normative matrix). No arbitrary path or musical value fields."
        },
        "values": {
          "$ref": "#/$defs/languageMap32"
        }
      },
      "required": [
        "target",
        "field",
        "values"
      ],
      "description": "Independent translations for one stable source field. Original source text remains authoritative as fallback."
    },
    "genre": {
      "type": "object",
      "description": "One song-local open genre tag. The label is authored Unicode text and not a predefined controlled taxonomy; ID is stable for metadata merges and localization.",
      "properties": {
        "id": {
          "$ref": "#/$defs/id",
          "description": "Stable song-local ID unique among all Core objects."
        },
        "name": {
          "type": "string",
          "minLength": 1,
          "description": "Original Unicode genre label, never normalized or rewritten during import."
        },
        "externalUri": {
          "type": "string",
          "minLength": 1,
          "format": "uri",
          "description": "Optional external taxonomy URI hint; never authoritative for a local genre label, and never auto-dereferenced."
        }
      },
      "required": [
        "id",
        "name"
      ],
      "additionalProperties": false
    },
    "legacy33": {
      "$defs": {
        "id": {
          "type": "string",
          "pattern": "^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$",
          "not": {
            "pattern": "[\\r\\n\\u2028\\u2029]"
          }
        },
        "nonnegative": {
          "type": "integer",
          "minimum": 0,
          "maximum": 9007199254740991
        },
        "positive": {
          "type": "integer",
          "minimum": 1,
          "maximum": 9007199254740991
        },
        "signed": {
          "type": "integer",
          "minimum": -9007199254740991,
          "maximum": 9007199254740991
        },
        "pitch": {
          "type": "integer",
          "minimum": 0,
          "maximum": 127
        },
        "ref": {
          "type": "object",
          "properties": {
            "type": {
              "enum": [
                "section",
                "track",
                "clip",
                "note",
                "chord",
                "scale",
                "soundSlot",
                "drumKit",
                "lyricDocument",
                "lyricPhrase",
                "lyricUnit",
                "lyricAlignment",
                "resource",
                "genre"
              ]
            },
            "id": {
              "$ref": "#/$defs/legacy33/$defs/id"
            }
          },
          "required": [
            "type",
            "id"
          ],
          "additionalProperties": false
        },
        "range": {
          "type": "object",
          "properties": {
            "start": {
              "$ref": "#/$defs/legacy33/$defs/nonnegative"
            },
            "duration": {
              "$ref": "#/$defs/legacy33/$defs/positive"
            }
          },
          "required": [
            "start",
            "duration"
          ],
          "additionalProperties": false
        },
        "spelledPitchClass": {
          "type": "object",
          "properties": {
            "step": {
              "enum": [
                "A",
                "B",
                "C",
                "D",
                "E",
                "F",
                "G"
              ]
            },
            "alter": {
              "type": "integer",
              "minimum": -2,
              "maximum": 2
            }
          },
          "required": [
            "step",
            "alter"
          ],
          "additionalProperties": false
        },
        "song": {
          "type": "object",
          "properties": {
            "title": {
              "type": "string"
            },
            "primaryMelodyTrackId": {
              "$ref": "#/$defs/legacy33/$defs/id"
            },
            "localizedTitles": {
              "$ref": "#/$defs/legacy33/$defs/localizedNames",
              "description": "Optional localized song-title alternatives. song.title is the stable fallback."
            },
            "subtitle": {
              "type": "string",
              "description": "Optional original-language subtitle."
            },
            "description": {
              "type": "string",
              "description": "Optional original-language description, including Unicode and line breaks."
            },
            "alternateTitles": {
              "type": "array",
              "items": {
                "$ref": "#/$defs/legacy33/$defs/alternateTitle"
              },
              "description": "Additional stable-ID source-language titles."
            },
            "credits": {
              "type": "array",
              "items": {
                "$ref": "#/$defs/legacy33/$defs/credit"
              },
              "description": "Ordered credit assignments to contributors. Multiple roles and duplicate contributors permitted."
            },
            "genres": {
              "type": "array",
              "items": {
                "$ref": "#/$defs/legacy33/$defs/genre"
              },
              "description": "Optional open-ended ordered genre tags; zero or more allowed. Order is authored display preference, first item is primary if a primary label is desired, not a generator weight. Absent means unspecified."
            }
          },
          "required": [
            "title"
          ],
          "additionalProperties": false
        },
        "section": {
          "type": "object",
          "properties": {
            "id": {
              "$ref": "#/$defs/legacy33/$defs/id"
            },
            "name": {
              "type": "string",
              "minLength": 1
            },
            "start": {
              "$ref": "#/$defs/legacy33/$defs/nonnegative"
            },
            "duration": {
              "$ref": "#/$defs/legacy33/$defs/positive"
            },
            "role": {
              "type": "string"
            },
            "localizedNames": {
              "$ref": "#/$defs/legacy33/$defs/localizedNames",
              "description": "Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity."
            }
          },
          "required": [
            "id",
            "name",
            "start",
            "duration"
          ],
          "additionalProperties": false
        },
        "tempo": {
          "type": "object",
          "properties": {
            "at": {
              "$ref": "#/$defs/legacy33/$defs/nonnegative"
            },
            "bpm": {
              "type": "number",
              "exclusiveMinimum": 0,
              "maximum": 1000
            }
          },
          "required": [
            "at",
            "bpm"
          ],
          "additionalProperties": false
        },
        "meter": {
          "type": "object",
          "properties": {
            "at": {
              "$ref": "#/$defs/legacy33/$defs/nonnegative"
            },
            "numerator": {
              "type": "integer",
              "minimum": 1,
              "maximum": 64
            },
            "denominator": {
              "enum": [
                1,
                2,
                4,
                8,
                16,
                32,
                64
              ],
              "type": "integer"
            }
          },
          "required": [
            "at",
            "numerator",
            "denominator"
          ],
          "additionalProperties": false
        },
        "timeline": {
          "type": "object",
          "properties": {
            "sections": {
              "type": "array",
              "items": {
                "$ref": "#/$defs/legacy33/$defs/section"
              }
            },
            "tempoChanges": {
              "type": "array",
              "items": {
                "$ref": "#/$defs/legacy33/$defs/tempo"
              },
              "minItems": 1
            },
            "meterChanges": {
              "type": "array",
              "items": {
                "$ref": "#/$defs/legacy33/$defs/meter"
              },
              "minItems": 1
            }
          },
          "required": [
            "sections",
            "tempoChanges",
            "meterChanges"
          ],
          "additionalProperties": false
        },
        "chord": {
          "type": "object",
          "properties": {
            "id": {
              "$ref": "#/$defs/legacy33/$defs/id"
            },
            "start": {
              "$ref": "#/$defs/legacy33/$defs/nonnegative"
            },
            "duration": {
              "$ref": "#/$defs/legacy33/$defs/positive"
            },
            "label": {
              "type": "string",
              "minLength": 1
            },
            "root": {
              "$ref": "#/$defs/legacy33/$defs/spelledPitchClass"
            },
            "intervals": {
              "type": "array",
              "items": {
                "type": "integer",
                "minimum": 0,
                "maximum": 35
              },
              "minItems": 1,
              "maxItems": 36,
              "uniqueItems": true,
              "contains": {
                "const": 0
              }
            },
            "bass": {
              "$ref": "#/$defs/legacy33/$defs/spelledPitchClass"
            },
            "voicing": {
              "$ref": "#/$defs/legacy33/$defs/voicing",
              "description": "Optional pitch snapshot (not an arrangement note sequence). No automatic playback."
            }
          },
          "required": [
            "id",
            "start",
            "duration",
            "label"
          ],
          "additionalProperties": false,
          "dependentRequired": {
            "root": [
              "intervals"
            ],
            "intervals": [
              "root"
            ]
          }
        },
        "scale": {
          "type": "object",
          "properties": {
            "id": {
              "$ref": "#/$defs/legacy33/$defs/id"
            },
            "start": {
              "$ref": "#/$defs/legacy33/$defs/nonnegative"
            },
            "duration": {
              "$ref": "#/$defs/legacy33/$defs/positive"
            },
            "label": {
              "type": "string"
            },
            "tonic": {
              "$ref": "#/$defs/legacy33/$defs/spelledPitchClass"
            },
            "intervals": {
              "type": "array",
              "items": {
                "type": "integer",
                "minimum": 0,
                "maximum": 11
              },
              "minItems": 1,
              "maxItems": 12,
              "uniqueItems": true,
              "contains": {
                "const": 0
              }
            }
          },
          "required": [
            "id",
            "start",
            "duration",
            "tonic",
            "intervals"
          ],
          "additionalProperties": false
        },
        "harmony": {
          "type": "object",
          "properties": {
            "chords": {
              "type": "array",
              "items": {
                "$ref": "#/$defs/legacy33/$defs/chord"
              }
            },
            "scales": {
              "type": "array",
              "items": {
                "$ref": "#/$defs/legacy33/$defs/scale"
              }
            }
          },
          "required": [
            "chords",
            "scales"
          ],
          "additionalProperties": false
        },
        "instrument": {
          "type": "object",
          "properties": {
            "name": {
              "type": "string"
            },
            "family": {
              "type": "string"
            },
            "localizedNames": {
              "$ref": "#/$defs/legacy33/$defs/localizedNames",
              "description": "Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity."
            }
          },
          "required": [
            "name"
          ],
          "additionalProperties": false
        },
        "note": {
          "type": "object",
          "properties": {
            "id": {
              "$ref": "#/$defs/legacy33/$defs/id"
            },
            "start": {
              "$ref": "#/$defs/legacy33/$defs/signed"
            },
            "duration": {
              "$ref": "#/$defs/legacy33/$defs/positive",
              "description": "Positive note gate in ticks, not the guaranteed audible duration of a one-shot percussion sample."
            },
            "pitch": {
              "$ref": "#/$defs/legacy33/$defs/pitch"
            },
            "soundSlotId": {
              "$ref": "#/$defs/legacy33/$defs/id",
              "description": "Document-local Sound Slot ID. Distinct events and IDs stay distinct even if several slots share a MIDI key; a renderer decides the acoustic timbre."
            },
            "velocity": {
              "type": "integer",
              "minimum": 1,
              "maximum": 127,
              "description": "Optional authored note-on velocity for performed Core notes, 1–127; omit to mean unspecified. It is not a note-off velocity, controller stream, chord tone, or a sound-rendering guarantee. Never insert an inferred default when saving."
            }
          },
          "required": [
            "id",
            "start",
            "duration"
          ],
          "additionalProperties": false,
          "oneOf": [
            {
              "required": [
                "pitch"
              ],
              "not": {
                "required": [
                  "soundSlotId"
                ]
              }
            },
            {
              "required": [
                "soundSlotId"
              ],
              "not": {
                "required": [
                  "pitch"
                ]
              }
            }
          ],
          "description": "Concrete Core note; optional velocity is a note-on attribute. Phrase templates use a separate version-frozen sourceNote shape."
        },
        "clip": {
          "type": "object",
          "properties": {
            "id": {
              "$ref": "#/$defs/legacy33/$defs/id"
            },
            "name": {
              "type": "string"
            },
            "start": {
              "$ref": "#/$defs/legacy33/$defs/nonnegative"
            },
            "duration": {
              "$ref": "#/$defs/legacy33/$defs/positive"
            },
            "enabled": {
              "type": "boolean",
              "default": true
            },
            "notes": {
              "type": "array",
              "items": {
                "$ref": "#/$defs/legacy33/$defs/note"
              }
            },
            "localizedNames": {
              "$ref": "#/$defs/legacy33/$defs/localizedNames",
              "description": "Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity."
            }
          },
          "required": [
            "id",
            "start",
            "duration",
            "notes"
          ],
          "additionalProperties": false
        },
        "track": {
          "type": "object",
          "properties": {
            "id": {
              "$ref": "#/$defs/legacy33/$defs/id"
            },
            "name": {
              "type": "string"
            },
            "role": {
              "type": "string"
            },
            "instrument": {
              "$ref": "#/$defs/legacy33/$defs/instrument"
            },
            "enabled": {
              "type": "boolean",
              "default": true
            },
            "clips": {
              "type": "array",
              "items": {
                "$ref": "#/$defs/legacy33/$defs/clip"
              }
            },
            "trackType": {
              "enum": [
                "melodic",
                "drum",
                "mixed"
              ],
              "description": "Semantic event-target category; optional; missing/empty-note tracks may be unknown. It is not a DAW track class."
            },
            "preferredView": {
              "enum": [
                "auto",
                "pianoRoll",
                "drumGrid"
              ],
              "default": "auto",
              "description": "Non-binding presentation preference. Does not change note meaning."
            },
            "soundSource": {
              "$ref": "#/$defs/legacy33/$defs/soundSource",
              "description": "Optional sound-source selection hint, not a plug-in state, preset blob, or sound guarantee."
            },
            "localizedNames": {
              "$ref": "#/$defs/legacy33/$defs/localizedNames",
              "description": "Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity."
            },
            "drumKitId": {
              "$ref": "#/$defs/legacy33/$defs/id",
              "description": "Optional reference to a declared drumKit; only for a drum/mixed or empty inferred track. All stored slot events in the track must belong to the referenced kit."
            }
          },
          "required": [
            "id",
            "name",
            "clips"
          ],
          "additionalProperties": false,
          "allOf": [
            {
              "if": {
                "properties": {
                  "trackType": {
                    "const": "melodic"
                  }
                },
                "required": [
                  "trackType"
                ]
              },
              "then": {
                "not": {
                  "required": [
                    "drumKitId"
                  ]
                }
              }
            }
          ]
        },
        "soundSlot": {
          "type": "object",
          "properties": {
            "id": {
              "$ref": "#/$defs/legacy33/$defs/id"
            },
            "name": {
              "type": "string"
            },
            "role": {
              "type": "string",
              "description": "Optional free-text musical role; not a standardized GM instrument code or an acoustic sample identifier."
            },
            "midiNote": {
              "$ref": "#/$defs/legacy33/$defs/pitch",
              "description": "Legacy 3.0 MIDI note hint only; not a GM1 declaration or preview timbre identity."
            },
            "midiMapping": {
              "$ref": "#/$defs/legacy33/$defs/midiMapping",
              "description": "Explicit external MIDI1 output mapping; standard=gm1 is separate from custom even for an equal note number. Not a unique slot or audio identity."
            },
            "localizedNames": {
              "$ref": "#/$defs/legacy33/$defs/localizedNames",
              "description": "Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity."
            }
          },
          "required": [
            "id",
            "name"
          ],
          "additionalProperties": false,
          "description": "Document-local stable logical percussion target. Equal roles, names or MIDI note mappings never merge distinct slot IDs. No sample/audio identity is encoded."
        },
        "lyricDocument": {
          "type": "object",
          "properties": {
            "id": {
              "$ref": "#/$defs/legacy33/$defs/id"
            },
            "title": {
              "type": "string"
            },
            "language": {
              "type": "string"
            }
          },
          "required": [
            "id"
          ],
          "additionalProperties": false
        },
        "lyricPhrase": {
          "type": "object",
          "properties": {
            "id": {
              "$ref": "#/$defs/legacy33/$defs/id"
            },
            "documentId": {
              "$ref": "#/$defs/legacy33/$defs/id"
            },
            "text": {
              "type": "string"
            },
            "pronunciation": {
              "type": "string"
            },
            "start": {
              "$ref": "#/$defs/legacy33/$defs/nonnegative"
            },
            "duration": {
              "$ref": "#/$defs/legacy33/$defs/positive"
            }
          },
          "required": [
            "id",
            "documentId",
            "text"
          ],
          "additionalProperties": false,
          "dependentRequired": {
            "start": [
              "duration"
            ],
            "duration": [
              "start"
            ]
          }
        },
        "lyricUnit": {
          "type": "object",
          "properties": {
            "id": {
              "$ref": "#/$defs/legacy33/$defs/id"
            },
            "phraseId": {
              "$ref": "#/$defs/legacy33/$defs/id"
            },
            "text": {
              "type": "string"
            },
            "pronunciation": {
              "type": "string"
            },
            "start": {
              "$ref": "#/$defs/legacy33/$defs/nonnegative"
            },
            "duration": {
              "$ref": "#/$defs/legacy33/$defs/positive"
            }
          },
          "required": [
            "id",
            "phraseId",
            "text"
          ],
          "additionalProperties": false,
          "dependentRequired": {
            "start": [
              "duration"
            ],
            "duration": [
              "start"
            ]
          }
        },
        "lyricAlignment": {
          "type": "object",
          "properties": {
            "id": {
              "$ref": "#/$defs/legacy33/$defs/id"
            },
            "unitIds": {
              "type": "array",
              "items": {
                "$ref": "#/$defs/legacy33/$defs/id"
              },
              "uniqueItems": true,
              "minItems": 1
            },
            "noteIds": {
              "type": "array",
              "items": {
                "$ref": "#/$defs/legacy33/$defs/id"
              },
              "uniqueItems": true,
              "minItems": 1
            }
          },
          "required": [
            "id",
            "unitIds",
            "noteIds"
          ],
          "additionalProperties": false
        },
        "lyrics": {
          "type": "object",
          "properties": {
            "documents": {
              "type": "array",
              "items": {
                "$ref": "#/$defs/legacy33/$defs/lyricDocument"
              }
            },
            "phrases": {
              "type": "array",
              "items": {
                "$ref": "#/$defs/legacy33/$defs/lyricPhrase"
              }
            },
            "units": {
              "type": "array",
              "items": {
                "$ref": "#/$defs/legacy33/$defs/lyricUnit"
              }
            },
            "alignments": {
              "type": "array",
              "items": {
                "$ref": "#/$defs/legacy33/$defs/lyricAlignment"
              }
            }
          },
          "required": [
            "documents",
            "phrases",
            "units",
            "alignments"
          ],
          "additionalProperties": false
        },
        "sha256": {
          "type": "string",
          "pattern": "^[0-9a-f]{64}$",
          "not": {
            "pattern": "[\\r\\n\\u2028\\u2029]"
          }
        },
        "resource": {
          "type": "object",
          "properties": {
            "id": {
              "$ref": "#/$defs/legacy33/$defs/id"
            },
            "kind": {
              "enum": [
                "audio",
                "midi",
                "text",
                "other"
              ]
            },
            "uri": {
              "type": "string",
              "minLength": 1
            },
            "name": {
              "type": "string"
            },
            "sha256": {
              "$ref": "#/$defs/legacy33/$defs/sha256"
            }
          },
          "required": [
            "id",
            "kind",
            "uri"
          ],
          "additionalProperties": false
        },
        "dependencies": {
          "oneOf": [
            {
              "type": "object",
              "properties": {
                "scope": {
                  "enum": [
                    "document",
                    "none"
                  ]
                }
              },
              "required": [
                "scope"
              ],
              "additionalProperties": false
            },
            {
              "type": "object",
              "properties": {
                "scope": {
                  "const": "objects"
                },
                "refs": {
                  "type": "array",
                  "items": {
                    "$ref": "#/$defs/legacy33/$defs/ref"
                  },
                  "minItems": 1,
                  "uniqueItems": true
                }
              },
              "required": [
                "scope",
                "refs"
              ],
              "additionalProperties": false
            }
          ]
        },
        "extension": {
          "type": "object",
          "properties": {
            "version": {
              "type": "string",
              "minLength": 1
            },
            "status": {
              "enum": [
                "current",
                "stale",
                "unverified"
              ]
            },
            "dependencies": {
              "$ref": "#/$defs/legacy33/$defs/dependencies"
            },
            "data": {}
          },
          "required": [
            "version",
            "status",
            "dependencies",
            "data"
          ],
          "additionalProperties": false
        },
        "relativeAssignment": {
          "type": "object",
          "properties": {
            "noteId": {
              "$ref": "#/$defs/legacy33/$defs/id"
            },
            "basis": {
              "enum": [
                "chordTone",
                "scaleDegree"
              ]
            },
            "contextId": {
              "$ref": "#/$defs/legacy33/$defs/id"
            },
            "anchorPitch": {
              "$ref": "#/$defs/legacy33/$defs/pitch"
            },
            "index": {
              "type": "integer",
              "minimum": 1,
              "maximum": 36
            },
            "chromaticOffset": {
              "type": "integer",
              "minimum": -24,
              "maximum": 24
            }
          },
          "required": [
            "noteId",
            "basis",
            "contextId",
            "anchorPitch",
            "index",
            "chromaticOffset"
          ],
          "additionalProperties": false,
          "allOf": [
            {
              "if": {
                "properties": {
                  "basis": {
                    "const": "scaleDegree"
                  }
                },
                "required": [
                  "basis"
                ]
              },
              "then": {
                "properties": {
                  "index": {
                    "maximum": 12
                  }
                }
              }
            }
          ]
        },
        "relativeData": {
          "type": "object",
          "properties": {
            "assignments": {
              "type": "array",
              "items": {
                "$ref": "#/$defs/legacy33/$defs/relativeAssignment"
              }
            }
          },
          "required": [
            "assignments"
          ],
          "additionalProperties": false
        },
        "generator": {
          "type": "object",
          "properties": {
            "id": {
              "type": "string",
              "minLength": 1
            },
            "version": {
              "type": "string",
              "minLength": 1
            }
          },
          "required": [
            "id",
            "version"
          ],
          "additionalProperties": false
        },
        "generationInput": {
          "type": "object",
          "properties": {
            "role": {
              "type": "string",
              "minLength": 1
            },
            "ref": {
              "$ref": "#/$defs/legacy33/$defs/ref"
            },
            "readRange": {
              "$ref": "#/$defs/legacy33/$defs/range"
            }
          },
          "required": [
            "role",
            "ref"
          ],
          "additionalProperties": false
        },
        "generationProcess": {
          "type": "object",
          "properties": {
            "id": {
              "$ref": "#/$defs/legacy33/$defs/id"
            },
            "generator": {
              "$ref": "#/$defs/legacy33/$defs/generator"
            },
            "inputs": {
              "type": "array",
              "items": {
                "$ref": "#/$defs/legacy33/$defs/generationInput"
              }
            },
            "outputs": {
              "type": "array",
              "items": {
                "$ref": "#/$defs/legacy33/$defs/ref"
              },
              "minItems": 1
            },
            "targetRange": {
              "$ref": "#/$defs/legacy33/$defs/range"
            },
            "protectedNoteIds": {
              "type": "array",
              "items": {
                "$ref": "#/$defs/legacy33/$defs/id"
              },
              "uniqueItems": true
            },
            "vendorExtension": {
              "type": "string",
              "minLength": 1
            }
          },
          "required": [
            "id",
            "generator",
            "inputs",
            "outputs",
            "protectedNoteIds"
          ],
          "additionalProperties": false
        },
        "generationData": {
          "type": "object",
          "properties": {
            "processes": {
              "type": "array",
              "items": {
                "$ref": "#/$defs/legacy33/$defs/generationProcess"
              }
            }
          },
          "required": [
            "processes"
          ],
          "additionalProperties": false
        },
        "color": {
          "type": "string",
          "pattern": "^#[0-9A-Fa-f]{6}$",
          "not": {
            "pattern": "[\\r\\n\\u2028\\u2029]"
          }
        },
        "roleDefinition": {
          "type": "object",
          "properties": {
            "id": {
              "$ref": "#/$defs/legacy33/$defs/id"
            },
            "name": {
              "type": "string",
              "minLength": 1
            },
            "baseRole": {
              "type": "string"
            }
          },
          "required": [
            "id",
            "name"
          ],
          "additionalProperties": false
        },
        "roleColorMap": {
          "type": "object",
          "additionalProperties": {
            "$ref": "#/$defs/legacy33/$defs/color"
          }
        },
        "customRoleColorMap": {
          "type": "object",
          "propertyNames": {
            "$ref": "#/$defs/legacy33/$defs/id"
          },
          "additionalProperties": {
            "$ref": "#/$defs/legacy33/$defs/color"
          }
        },
        "objectColor": {
          "type": "object",
          "properties": {
            "target": {
              "$ref": "#/$defs/legacy33/$defs/ref"
            },
            "color": {
              "$ref": "#/$defs/legacy33/$defs/color"
            }
          },
          "required": [
            "target",
            "color"
          ],
          "additionalProperties": false
        },
        "appearanceData": {
          "type": "object",
          "properties": {
            "roleDefinitions": {
              "type": "array",
              "items": {
                "$ref": "#/$defs/legacy33/$defs/roleDefinition"
              }
            },
            "sectionRoleAssignments": {
              "type": "object",
              "propertyNames": {
                "$ref": "#/$defs/legacy33/$defs/id"
              },
              "additionalProperties": {
                "$ref": "#/$defs/legacy33/$defs/id"
              }
            },
            "appearance": {
              "type": "object",
              "properties": {
                "roleColors": {
                  "$ref": "#/$defs/legacy33/$defs/roleColorMap"
                },
                "customRoleColors": {
                  "$ref": "#/$defs/legacy33/$defs/customRoleColorMap"
                },
                "objectColors": {
                  "type": "array",
                  "items": {
                    "$ref": "#/$defs/legacy33/$defs/objectColor"
                  }
                }
              },
              "required": [
                "roleColors",
                "customRoleColors",
                "objectColors"
              ],
              "additionalProperties": false
            }
          },
          "required": [
            "roleDefinitions",
            "sectionRoleAssignments",
            "appearance"
          ],
          "additionalProperties": false
        },
        "legacyData": {
          "type": "object",
          "properties": {
            "sourceVersion": {
              "const": "2.3.0"
            },
            "sourceSha256": {
              "$ref": "#/$defs/legacy33/$defs/sha256"
            },
            "sourceText": {
              "type": "string",
              "minLength": 1
            },
            "conversionReport": {
              "type": "object"
            }
          },
          "required": [
            "sourceVersion",
            "sourceSha256",
            "sourceText",
            "conversionReport"
          ],
          "additionalProperties": false
        },
        "extensions": {
          "type": "object",
          "propertyNames": {
            "pattern": "^[a-z][a-z0-9-]*(?:\\.[a-z][a-z0-9-]*){2,}$",
            "not": {
              "pattern": "[\\r\\n\\u2028\\u2029]"
            }
          },
          "properties": {
            "org.ostf.relative-phrase.v1": {
              "allOf": [
                {
                  "$ref": "#/$defs/legacy33/$defs/extension"
                },
                {
                  "if": {
                    "properties": {
                      "version": {
                        "const": "1.0.0-draft.1"
                      }
                    },
                    "required": [
                      "version"
                    ]
                  },
                  "then": {
                    "properties": {
                      "data": {
                        "$ref": "#/$defs/legacy33/$defs/relativeData"
                      }
                    }
                  }
                }
              ]
            },
            "org.ostf.generation-context.v1": {
              "allOf": [
                {
                  "$ref": "#/$defs/legacy33/$defs/extension"
                },
                {
                  "if": {
                    "properties": {
                      "version": {
                        "const": "1.0.0-draft.1"
                      }
                    },
                    "required": [
                      "version"
                    ]
                  },
                  "then": {
                    "properties": {
                      "data": {
                        "$ref": "#/$defs/legacy33/$defs/generationData"
                      }
                    }
                  }
                }
              ]
            },
            "org.ostf.appearance.v1": {
              "allOf": [
                {
                  "$ref": "#/$defs/legacy33/$defs/extension"
                },
                {
                  "if": {
                    "properties": {
                      "version": {
                        "const": "1.0.0-draft.1"
                      }
                    },
                    "required": [
                      "version"
                    ]
                  },
                  "then": {
                    "properties": {
                      "data": {
                        "$ref": "#/$defs/legacy33/$defs/appearanceData"
                      }
                    }
                  }
                }
              ]
            },
            "org.ostf.legacy-import.v1": {
              "allOf": [
                {
                  "$ref": "#/$defs/legacy33/$defs/extension"
                },
                {
                  "if": {
                    "properties": {
                      "version": {
                        "const": "1.0.0-draft.1"
                      }
                    },
                    "required": [
                      "version"
                    ]
                  },
                  "then": {
                    "properties": {
                      "data": {
                        "$ref": "#/$defs/legacy33/$defs/legacyData"
                      }
                    }
                  }
                }
              ]
            },
            "org.ostf.phrase-library.v1": {
              "allOf": [
                {
                  "$ref": "#/$defs/legacy33/$defs/extension"
                },
                {
                  "if": {
                    "properties": {
                      "version": {
                        "const": "1.0.0-draft.1"
                      }
                    },
                    "required": [
                      "version"
                    ]
                  },
                  "then": {
                    "properties": {
                      "data": {
                        "$ref": "#/$defs/legacy33/$defs/phraseLibraryData"
                      }
                    }
                  }
                }
              ]
            },
            "org.ostf.clip-choices.v1": {
              "allOf": [
                {
                  "$ref": "#/$defs/legacy33/$defs/extension"
                },
                {
                  "if": {
                    "properties": {
                      "version": {
                        "const": "1.0.0-draft.1"
                      }
                    },
                    "required": [
                      "version"
                    ]
                  },
                  "then": {
                    "properties": {
                      "data": {
                        "$ref": "#/$defs/legacy33/$defs/clipChoicesData"
                      }
                    }
                  }
                }
              ]
            },
            "org.ostf.localization.v1": {
              "allOf": [
                {
                  "$ref": "#/$defs/legacy33/$defs/extension"
                },
                {
                  "if": {
                    "properties": {
                      "version": {
                        "const": "1.0.0"
                      }
                    },
                    "required": [
                      "version"
                    ]
                  },
                  "then": {
                    "properties": {
                      "data": {
                        "$ref": "#/$defs/legacy33/$defs/localizationData"
                      }
                    }
                  }
                }
              ]
            }
          },
          "additionalProperties": {
            "$ref": "#/$defs/legacy33/$defs/extension"
          }
        },
        "phraseTemplate": {
          "type": "object",
          "properties": {
            "id": {
              "$ref": "#/$defs/legacy33/$defs/id"
            },
            "duration": {
              "$ref": "#/$defs/legacy33/$defs/positive"
            },
            "notes": {
              "type": "array",
              "items": {
                "$ref": "#/$defs/legacy33/$defs/phraseSourceNote"
              }
            },
            "name": {
              "type": "string"
            }
          },
          "required": [
            "id",
            "duration",
            "notes"
          ],
          "additionalProperties": false
        },
        "phraseNoteMapping": {
          "type": "object",
          "properties": {
            "templateNoteId": {
              "$ref": "#/$defs/legacy33/$defs/id"
            },
            "repeatIndex": {
              "$ref": "#/$defs/legacy33/$defs/nonnegative"
            },
            "noteId": {
              "$ref": "#/$defs/legacy33/$defs/id"
            }
          },
          "required": [
            "templateNoteId",
            "repeatIndex",
            "noteId"
          ],
          "additionalProperties": false
        },
        "phraseInstance": {
          "type": "object",
          "properties": {
            "id": {
              "$ref": "#/$defs/legacy33/$defs/id"
            },
            "templateId": {
              "$ref": "#/$defs/legacy33/$defs/id"
            },
            "clipId": {
              "$ref": "#/$defs/legacy33/$defs/id"
            },
            "repeatCount": {
              "$ref": "#/$defs/legacy33/$defs/positive"
            },
            "transpose": {
              "type": "integer",
              "minimum": -127,
              "maximum": 127
            },
            "noteMap": {
              "type": "array",
              "items": {
                "$ref": "#/$defs/legacy33/$defs/phraseNoteMapping"
              }
            }
          },
          "required": [
            "id",
            "templateId",
            "clipId",
            "repeatCount",
            "transpose",
            "noteMap"
          ],
          "additionalProperties": false
        },
        "phraseLibraryData": {
          "type": "object",
          "properties": {
            "templates": {
              "type": "array",
              "items": {
                "$ref": "#/$defs/legacy33/$defs/phraseTemplate"
              }
            },
            "instances": {
              "type": "array",
              "items": {
                "$ref": "#/$defs/legacy33/$defs/phraseInstance"
              }
            }
          },
          "required": [
            "templates",
            "instances"
          ],
          "additionalProperties": false
        },
        "clipCandidate": {
          "type": "object",
          "properties": {
            "id": {
              "$ref": "#/$defs/legacy33/$defs/id"
            },
            "clipIds": {
              "type": "array",
              "items": {
                "$ref": "#/$defs/legacy33/$defs/id"
              },
              "uniqueItems": true
            },
            "name": {
              "type": "string"
            }
          },
          "required": [
            "id",
            "clipIds"
          ],
          "additionalProperties": false
        },
        "clipChoiceGroup": {
          "type": "object",
          "properties": {
            "id": {
              "$ref": "#/$defs/legacy33/$defs/id"
            },
            "candidates": {
              "type": "array",
              "items": {
                "$ref": "#/$defs/legacy33/$defs/clipCandidate"
              },
              "minItems": 1
            },
            "selectedCandidateId": {
              "anyOf": [
                {
                  "$ref": "#/$defs/legacy33/$defs/id"
                },
                {
                  "type": "null"
                }
              ]
            },
            "name": {
              "type": "string"
            }
          },
          "required": [
            "id",
            "candidates",
            "selectedCandidateId"
          ],
          "additionalProperties": false
        },
        "clipChoicesData": {
          "type": "object",
          "properties": {
            "groups": {
              "type": "array",
              "items": {
                "$ref": "#/$defs/legacy33/$defs/clipChoiceGroup"
              }
            }
          },
          "required": [
            "groups"
          ],
          "additionalProperties": false
        },
        "midiMapping": {
          "type": "object",
          "properties": {
            "standard": {
              "enum": [
                "gm1",
                "custom"
              ],
              "description": "gm1=GM Level 1 percussion key 35..81; custom=explicit arbitrary MIDI1 note number."
            },
            "note": {
              "$ref": "#/$defs/legacy33/$defs/pitch",
              "description": "MIDI1 note number in 0..127; for gm1 restrict to 35..81."
            }
          },
          "required": [
            "standard",
            "note"
          ],
          "additionalProperties": false,
          "allOf": [
            {
              "if": {
                "properties": {
                  "standard": {
                    "const": "gm1"
                  }
                },
                "required": [
                  "standard"
                ]
              },
              "then": {
                "properties": {
                  "note": {
                    "type": "integer",
                    "minimum": 35,
                    "maximum": 81
                  }
                }
              }
            }
          ]
        },
        "soundSource": {
          "type": "object",
          "description": "Optional informational rendering class or opaque destination hint. Program Change, Bank Select and plugin presets are not standardized by Core.",
          "properties": {
            "kind": {
              "enum": [
                "unassigned",
                "gm1",
                "externalMidi",
                "plugin",
                "hostManaged"
              ]
            },
            "identifier": {
              "type": "string",
              "minLength": 1,
              "description": "Opaque target identifier, e.g. URI, plug-in identifier or port alias, not a loading command."
            }
          },
          "required": [
            "kind"
          ],
          "additionalProperties": false,
          "allOf": [
            {
              "if": {
                "properties": {
                  "kind": {
                    "enum": [
                      "gm1",
                      "unassigned"
                    ]
                  }
                },
                "required": [
                  "kind"
                ]
              },
              "then": {
                "not": {
                  "required": [
                    "identifier"
                  ]
                }
              }
            }
          ]
        },
        "localizedNames": {
          "type": "object",
          "minProperties": 1,
          "propertyNames": {
            "type": "string",
            "pattern": "^(?:[A-Za-z]{2,3}|[A-Za-z]{5,8})(?:-[A-Za-z0-9]{2,8})*$"
          },
          "additionalProperties": {
            "type": "string",
            "minLength": 1
          },
          "description": "Optional translations indexed by a conservative BCP 47 language-tag subset. The original name/title remains authoritative and is never rewritten by locale changes. Case-insensitive duplicate tags are forbidden semantically."
        },
        "drumKit": {
          "type": "object",
          "description": "Optional named ordered membership of global Sound Slot IDs. Does not define plugin preset, sample loading, choke or a kit-local MIDI remapping.",
          "properties": {
            "id": {
              "$ref": "#/$defs/legacy33/$defs/id"
            },
            "name": {
              "type": "string"
            },
            "localizedNames": {
              "$ref": "#/$defs/legacy33/$defs/localizedNames"
            },
            "soundSlotIds": {
              "type": "array",
              "uniqueItems": true,
              "items": {
                "$ref": "#/$defs/legacy33/$defs/id"
              },
              "description": "Ordered, unique references to global soundSlots; may be empty."
            }
          },
          "required": [
            "id",
            "name",
            "soundSlotIds"
          ],
          "additionalProperties": false
        },
        "phraseSourceNote": {
          "type": "object",
          "properties": {
            "id": {
              "$ref": "#/$defs/legacy33/$defs/id"
            },
            "start": {
              "$ref": "#/$defs/legacy33/$defs/signed"
            },
            "duration": {
              "$ref": "#/$defs/legacy33/$defs/positive"
            },
            "pitch": {
              "$ref": "#/$defs/legacy33/$defs/pitch"
            },
            "soundSlotId": {
              "$ref": "#/$defs/legacy33/$defs/id"
            }
          },
          "required": [
            "id",
            "start",
            "duration"
          ],
          "additionalProperties": false,
          "oneOf": [
            {
              "required": [
                "pitch"
              ],
              "not": {
                "required": [
                  "soundSlotId"
                ]
              }
            },
            {
              "required": [
                "soundSlotId"
              ],
              "not": {
                "required": [
                  "pitch"
                ]
              }
            }
          ],
          "description": "Version-frozen 1.0.0-draft.1 phrase source note. Does NOT admit velocity; a linked Core instance may independently set velocity."
        },
        "voicing": {
          "type": "object",
          "additionalProperties": false,
          "description": "Optional informational chord voicing snapshot, not a played Core note collection. Repeated pitches and original array order have meaning for lossless preservation. Per-entry velocity is an optional voicing-preview hint.",
          "properties": {
            "pitches": {
              "type": "array",
              "minItems": 1,
              "items": {
                "$ref": "#/$defs/legacy33/$defs/pitch"
              },
              "description": "Ordered multiset of concrete absolute pitches, 0-127. Duplicates allowed."
            },
            "velocities": {
              "type": "array",
              "minItems": 1,
              "items": {
                "anyOf": [
                  {
                    "type": "integer",
                    "minimum": 1,
                    "maximum": 127
                  },
                  {
                    "type": "null"
                  }
                ]
              },
              "description": "Optional positional velocities aligned one-to-one to pitches. Null means unspecified at this index, not 0. Exact equal-length rule is semantic."
            }
          },
          "required": [
            "pitches"
          ]
        },
        "contributor": {
          "type": "object",
          "additionalProperties": false,
          "description": "One song-local identity; same contributor can receive multiple credit roles. Unicode source name is authoritative.",
          "properties": {
            "id": {
              "$ref": "#/$defs/legacy33/$defs/id"
            },
            "name": {
              "type": "string",
              "minLength": 1
            },
            "kind": {
              "enum": [
                "person",
                "organization",
                "other"
              ]
            },
            "localizedNames": {
              "$ref": "#/$defs/legacy33/$defs/localizedNames"
            }
          },
          "required": [
            "id",
            "name"
          ]
        },
        "credit": {
          "type": "object",
          "additionalProperties": false,
          "description": "Ordered credit assignment referencing one contributor; role is an open semantic token, not a translated label.",
          "properties": {
            "id": {
              "$ref": "#/$defs/legacy33/$defs/id"
            },
            "contributorId": {
              "$ref": "#/$defs/legacy33/$defs/id"
            },
            "role": {
              "type": "string",
              "pattern": "^[a-z][a-z0-9.-]*$"
            },
            "label": {
              "type": "string"
            }
          },
          "required": [
            "id",
            "contributorId",
            "role"
          ]
        },
        "alternateTitle": {
          "type": "object",
          "additionalProperties": false,
          "description": "Stable-ID song title alternative; array position and title text do not identify it.",
          "properties": {
            "id": {
              "$ref": "#/$defs/legacy33/$defs/id"
            },
            "title": {
              "type": "string",
              "minLength": 1
            }
          },
          "required": [
            "id",
            "title"
          ]
        },
        "languageMap32": {
          "type": "object",
          "minProperties": 1,
          "propertyNames": {
            "type": "string",
            "pattern": "^[A-Za-z]{1,8}(?:-[A-Za-z0-9]{1,8})*$"
          },
          "additionalProperties": {
            "type": "string"
          },
          "description": "Open BCP 47 language-tag dictionary. Schema checks loose subtag structure; full BCP 47 well-formedness and case-insensitive uniqueness are semantic requirements. String may be empty if intentionally blank."
        },
        "localizationTarget": {
          "type": "object",
          "additionalProperties": false,
          "properties": {
            "kind": {
              "enum": [
                "song",
                "alternateTitle",
                "contributor",
                "credit",
                "section",
                "track",
                "clip",
                "soundSlot",
                "drumKit",
                "lyricDocument",
                "resource",
                "phraseTemplate",
                "clipCandidate",
                "clipChoiceGroup",
                "roleDefinition",
                "genre"
              ]
            },
            "id": {
              "$ref": "#/$defs/legacy33/$defs/id"
            },
            "profile": {
              "type": "string",
              "enum": [
                "org.ostf.phrase-library.v1",
                "org.ostf.clip-choices.v1",
                "org.ostf.appearance.v1"
              ]
            }
          },
          "required": [
            "kind"
          ],
          "allOf": [
            {
              "if": {
                "properties": {
                  "kind": {
                    "const": "song"
                  }
                },
                "required": [
                  "kind"
                ]
              },
              "then": {
                "not": {
                  "anyOf": [
                    {
                      "required": [
                        "id"
                      ]
                    },
                    {
                      "required": [
                        "profile"
                      ]
                    }
                  ]
                }
              },
              "else": {
                "required": [
                  "id"
                ]
              }
            },
            {
              "if": {
                "properties": {
                  "kind": {
                    "enum": [
                      "phraseTemplate",
                      "clipCandidate",
                      "clipChoiceGroup",
                      "roleDefinition"
                    ]
                  }
                },
                "required": [
                  "kind"
                ]
              },
              "then": {
                "required": [
                  "profile"
                ]
              },
              "else": {
                "not": {
                  "required": [
                    "profile"
                  ]
                }
              }
            }
          ],
          "description": "Stable target by Core ID or profile-local scoped ID; song is the only ID-less target. No array indexes or mutable names as locators."
        },
        "localizationEntry": {
          "type": "object",
          "additionalProperties": false,
          "properties": {
            "target": {
              "$ref": "#/$defs/legacy33/$defs/localizationTarget"
            },
            "field": {
              "type": "string",
              "minLength": 1,
              "description": "Exact allowed source text field for this target kind (see normative matrix). No arbitrary path or musical value fields."
            },
            "values": {
              "$ref": "#/$defs/legacy33/$defs/languageMap32"
            }
          },
          "required": [
            "target",
            "field",
            "values"
          ],
          "description": "Independent translations for one stable source field. Original source text remains authoritative as fallback."
        },
        "localizationData": {
          "type": "object",
          "additionalProperties": false,
          "properties": {
            "entries": {
              "type": "array",
              "items": {
                "$ref": "#/$defs/legacy33/$defs/localizationEntry"
              }
            }
          },
          "required": [
            "entries"
          ],
          "description": "Language-map translations indexed by stable kind/id/field, never by names or array positions."
        },
        "genre": {
          "type": "object",
          "description": "One song-local open genre tag. The label is authored Unicode text and not a predefined controlled taxonomy; ID is stable for metadata merges and localization.",
          "properties": {
            "id": {
              "$ref": "#/$defs/legacy33/$defs/id",
              "description": "Stable song-local ID unique among all Core objects."
            },
            "name": {
              "type": "string",
              "minLength": 1,
              "description": "Original Unicode genre label, never normalized or rewritten during import."
            },
            "externalUri": {
              "type": "string",
              "minLength": 1,
              "format": "uri",
              "description": "Optional external taxonomy URI hint; never authoritative for a local genre label, and never auto-dereferenced."
            }
          },
          "required": [
            "id",
            "name"
          ],
          "additionalProperties": false
        }
      }
    },
    "opaqueDocumentId": {
      "type": "string",
      "minLength": 1,
      "description": "Stable URI or UUID-style identifier for a document lineage. Compared as exact Unicode text; never fetched."
    },
    "revisionRef": {
      "type": "object",
      "properties": {
        "documentId": {
          "$ref": "#/$defs/opaqueDocumentId"
        },
        "revisionId": {
          "$ref": "#/$defs/opaqueDocumentId"
        },
        "sha256": {
          "$ref": "#/$defs/sha256"
        }
      },
      "required": [
        "documentId",
        "revisionId"
      ],
      "additionalProperties": false
    },
    "software": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "minLength": 1
        },
        "version": {
          "type": "string",
          "minLength": 1
        }
      },
      "required": [
        "name"
      ],
      "additionalProperties": false
    },
    "documentInfo": {
      "type": "object",
      "properties": {
        "id": {
          "$ref": "#/$defs/opaqueDocumentId"
        },
        "revisionId": {
          "$ref": "#/$defs/opaqueDocumentId"
        },
        "parents": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/revisionRef"
          },
          "uniqueItems": true
        },
        "createdBy": {
          "$ref": "#/$defs/software"
        },
        "modifiedBy": {
          "$ref": "#/$defs/software"
        }
      },
      "required": [
        "id",
        "revisionId"
      ],
      "additionalProperties": false
    },
    "key": {
      "type": "object",
      "properties": {
        "state": {
          "enum": [
            "tonal",
            "atonal",
            "unspecified"
          ]
        },
        "tonic": {
          "$ref": "#/$defs/spelledPitchClass"
        },
        "mode": {
          "type": "string",
          "minLength": 1,
          "description": "Authored mode identifier. Canonical recognized values include major, minor, dorian, phrygian, lydian, mixolydian, locrian. Unknown values are preserved, never converted to major/minor."
        },
        "label": {
          "type": "string"
        }
      },
      "required": [
        "state"
      ],
      "additionalProperties": false,
      "allOf": [
        {
          "if": {
            "properties": {
              "state": {
                "const": "tonal"
              }
            },
            "required": [
              "state"
            ]
          },
          "then": {
            "required": [
              "tonic",
              "mode"
            ]
          },
          "else": {
            "not": {
              "anyOf": [
                {
                  "required": [
                    "tonic"
                  ]
                },
                {
                  "required": [
                    "mode"
                  ]
                }
              ]
            }
          }
        }
      ]
    },
    "keyChange": {
      "type": "object",
      "properties": {
        "id": {
          "$ref": "#/$defs/id"
        },
        "at": {
          "$ref": "#/$defs/positive"
        },
        "key": {
          "$ref": "#/$defs/key"
        },
        "label": {
          "type": "string"
        }
      },
      "required": [
        "id",
        "at",
        "key"
      ],
      "additionalProperties": false,
      "description": "A change after tick zero; initial key is stored only at song.key. Change at tick 0 is forbidden to prevent dual authority."
    },
    "scaleDefinition": {
      "type": "object",
      "properties": {
        "id": {
          "$ref": "#/$defs/id"
        },
        "tonic": {
          "$ref": "#/$defs/spelledPitchClass"
        },
        "intervals": {
          "type": "array",
          "items": {
            "type": "integer",
            "minimum": 0,
            "maximum": 11
          },
          "minItems": 1,
          "maxItems": 12,
          "uniqueItems": true,
          "contains": {
            "const": 0
          }
        },
        "label": {
          "type": "string"
        }
      },
      "required": [
        "id",
        "tonic",
        "intervals"
      ],
      "additionalProperties": false
    },
    "scaleTarget": {
      "type": "object",
      "properties": {
        "type": {
          "enum": [
            "section",
            "track",
            "clip",
            "chord",
            "note"
          ]
        },
        "id": {
          "$ref": "#/$defs/id"
        }
      },
      "required": [
        "type",
        "id"
      ],
      "additionalProperties": false
    },
    "mood": {
      "type": "object",
      "description": "Authored descriptive mood tag; not a generator preset or a probability.",
      "properties": {
        "id": {
          "$ref": "#/$defs/id",
          "description": "Stable song-local ID unique among all Core objects."
        },
        "name": {
          "type": "string",
          "minLength": 1,
          "description": "Original Unicode genre label, never normalized or rewritten during import."
        },
        "externalUri": {
          "type": "string",
          "minLength": 1,
          "format": "uri",
          "description": "Optional external vocabulary URI hint; never authoritative for the authored mood name and never auto-dereferenced."
        }
      },
      "required": [
        "id",
        "name"
      ],
      "additionalProperties": false
    },
    "rightsStatement": {
      "type": "object",
      "properties": {
        "notice": {
          "type": "string"
        },
        "licenseUri": {
          "type": "string",
          "minLength": 1
        },
        "rightsHolderIds": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/id"
          },
          "uniqueItems": true
        }
      },
      "required": [],
      "additionalProperties": false,
      "description": "Authored rights statement only; no rights or permissions are inferred or granted by the format.",
      "minProperties": 1
    },
    "grooveIntent": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "unitTicks": {
          "$ref": "#/$defs/positive"
        },
        "longWeight": {
          "type": "integer",
          "minimum": 1,
          "maximum": 1000000
        },
        "shortWeight": {
          "type": "integer",
          "minimum": 1,
          "maximum": 1000000
        }
      },
      "required": [],
      "additionalProperties": false,
      "description": "Descriptive generation intent only. Never re-apply to already stored notes. unitTicks is one unswung subdivision; two subdivisions form a pair.",
      "minProperties": 1,
      "dependentRequired": {
        "unitTicks": [
          "longWeight",
          "shortWeight"
        ],
        "longWeight": [
          "unitTicks",
          "shortWeight"
        ],
        "shortWeight": [
          "unitTicks",
          "longWeight"
        ]
      }
    },
    "generationIntent": {
      "type": "object",
      "properties": {
        "genreNames": {
          "type": "array",
          "items": {
            "type": "string",
            "minLength": 1
          }
        },
        "moodNames": {
          "type": "array",
          "items": {
            "type": "string",
            "minLength": 1
          }
        },
        "groove": {
          "$ref": "#/$defs/grooveIntent"
        },
        "prompt": {
          "type": "string"
        },
        "seed": {
          "type": "string"
        }
      },
      "required": [],
      "additionalProperties": false,
      "description": "Portable description of intent, not a promise to reproduce an algorithm. Does not change song.genres or song.moods."
    },
    "relativePhrases": {
      "type": "object",
      "properties": {
        "status": {
          "enum": [
            "current",
            "stale",
            "unverified"
          ]
        },
        "dependencies": {
          "$ref": "#/$defs/dependencies"
        },
        "assignments": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/relativeAssignment"
          }
        }
      },
      "required": [
        "status",
        "dependencies",
        "assignments"
      ],
      "additionalProperties": false,
      "description": "Standard optional Core object under root version 4.0.0, not an extension. Current relationships must be consistent with saved Core; loading never performs editing or generation."
    },
    "generation": {
      "type": "object",
      "properties": {
        "status": {
          "enum": [
            "current",
            "stale",
            "unverified"
          ]
        },
        "dependencies": {
          "$ref": "#/$defs/dependencies"
        },
        "processes": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/generationProcess"
          }
        }
      },
      "required": [
        "status",
        "dependencies",
        "processes"
      ],
      "additionalProperties": false,
      "description": "Standard optional Core object under root version 4.0.0, not an extension. Current relationships must be consistent with saved Core; loading never performs editing or generation."
    },
    "presentation": {
      "type": "object",
      "properties": {
        "status": {
          "enum": [
            "current",
            "stale",
            "unverified"
          ]
        },
        "dependencies": {
          "$ref": "#/$defs/dependencies"
        },
        "roleDefinitions": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/roleDefinition"
          }
        },
        "sectionRoleAssignments": {
          "type": "object",
          "propertyNames": {
            "$ref": "#/$defs/id"
          },
          "additionalProperties": {
            "$ref": "#/$defs/id"
          }
        },
        "appearance": {
          "type": "object",
          "properties": {
            "roleColors": {
              "$ref": "#/$defs/roleColorMap"
            },
            "customRoleColors": {
              "$ref": "#/$defs/customRoleColorMap"
            },
            "objectColors": {
              "type": "array",
              "items": {
                "$ref": "#/$defs/objectColor"
              }
            }
          },
          "required": [
            "roleColors",
            "customRoleColors",
            "objectColors"
          ],
          "additionalProperties": false
        }
      },
      "required": [
        "status",
        "dependencies",
        "roleDefinitions",
        "sectionRoleAssignments",
        "appearance"
      ],
      "additionalProperties": false,
      "description": "Standard optional Core object under root version 4.0.0, not an extension. Current relationships must be consistent with saved Core; loading never performs editing or generation."
    },
    "phraseLibrary": {
      "type": "object",
      "properties": {
        "status": {
          "enum": [
            "current",
            "stale",
            "unverified"
          ]
        },
        "dependencies": {
          "$ref": "#/$defs/dependencies"
        },
        "templates": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/phraseTemplate"
          }
        },
        "instances": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/phraseInstance"
          }
        }
      },
      "required": [
        "status",
        "dependencies",
        "templates",
        "instances"
      ],
      "additionalProperties": false,
      "description": "Standard optional Core object under root version 4.0.0, not an extension. Current relationships must be consistent with saved Core; loading never performs editing or generation."
    },
    "clipChoices": {
      "type": "object",
      "properties": {
        "status": {
          "enum": [
            "current",
            "stale",
            "unverified"
          ]
        },
        "dependencies": {
          "$ref": "#/$defs/dependencies"
        },
        "groups": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/clipChoiceGroup"
          }
        }
      },
      "required": [
        "status",
        "dependencies",
        "groups"
      ],
      "additionalProperties": false,
      "description": "Standard optional Core object under root version 4.0.0, not an extension. Current relationships must be consistent with saved Core; loading never performs editing or generation."
    },
    "localization": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "status": {
          "enum": [
            "current",
            "stale",
            "unverified"
          ]
        },
        "dependencies": {
          "$ref": "#/$defs/dependencies"
        },
        "entries": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/localizationEntry"
          }
        }
      },
      "required": [
        "status",
        "dependencies",
        "entries"
      ],
      "description": "Standard optional Core object under root version 4.0.0, not an extension. Current relationships must be consistent with saved Core; loading never performs editing or generation."
    },
    "corePhraseSourceNote": {
      "type": "object",
      "properties": {
        "id": {
          "$ref": "#/$defs/id"
        },
        "start": {
          "$ref": "#/$defs/signed"
        },
        "duration": {
          "$ref": "#/$defs/positive",
          "description": "Positive note gate in ticks, not the guaranteed audible duration of a one-shot percussion sample."
        },
        "pitch": {
          "$ref": "#/$defs/pitch"
        },
        "soundSlotId": {
          "$ref": "#/$defs/id",
          "description": "Document-local Sound Slot ID. Distinct events and IDs stay distinct even if several slots share a MIDI key; a renderer decides the acoustic timbre."
        },
        "velocity": {
          "type": "integer",
          "minimum": 1,
          "maximum": 127,
          "description": "Optional template note-on velocity, 1–127. Applied only by an explicit materialization/update according to instance.velocityMode; never a performed event by itself."
        },
        "enabled": {
          "type": "boolean",
          "default": true,
          "description": "Optional note-local enable state. Omitted means enabled. False preserves the note but suppresses scheduling/playback; it is distinct from probability=0."
        },
        "releaseVelocity": {
          "type": "integer",
          "minimum": 0,
          "maximum": 127,
          "description": "Optional MIDI Note Off/release velocity, 0-127. Omit when unspecified; readers must not invent and write back a default."
        },
        "probability": {
          "type": "number",
          "minimum": 0,
          "maximum": 1,
          "default": 1,
          "description": "Optional note-playback probability from 0.0 to 1.0. Omitted means 1.0. Random sequence identity is not standardized; materialize notes for deterministic interchange."
        },
        "velocityDeviation": {
          "type": "integer",
          "minimum": -126,
          "maximum": 126,
          "default": 0,
          "description": "Optional note-local velocity variation endpoint relative to velocity. Requires velocity. Semantic rule: velocity + velocityDeviation must remain within 1..127. Omitted means 0."
        },
        "pitchRole": {
          "enum": [
            "musical",
            "fixedTrigger"
          ],
          "default": "musical",
          "description": "Meaning of a pitch note. musical participates in pitch/harmony/transpose operations; fixedTrigger is an exact MIDI key trigger (for example a keyswitch) and is never transposed or used as musical-pitch evidence. Allowed only on pitch notes."
        }
      },
      "required": [
        "id",
        "start",
        "duration"
      ],
      "additionalProperties": false,
      "oneOf": [
        {
          "required": [
            "pitch"
          ],
          "not": {
            "required": [
              "soundSlotId"
            ]
          }
        },
        {
          "required": [
            "soundSlotId"
          ],
          "not": {
            "required": [
              "pitch"
            ]
          }
        }
      ],
      "description": "Template-local source note for phrase materialization. It carries the same note-local 3.5 properties as concrete notes. It is not performed by itself; concrete track notes remain the saved playback events.",
      "dependentRequired": {
        "velocityDeviation": [
          "velocity"
        ]
      },
      "allOf": [
        {
          "if": {
            "required": [
              "soundSlotId"
            ]
          },
          "then": {
            "not": {
              "required": [
                "pitchRole"
              ]
            }
          }
        }
      ]
    },
    "provenanceSource": {
      "type": "object",
      "properties": {
        "format": {
          "type": "string",
          "minLength": 1
        },
        "version": {
          "type": "string",
          "minLength": 1
        },
        "sha256": {
          "$ref": "#/$defs/sha256"
        },
        "uri": {
          "type": "string",
          "minLength": 1
        },
        "documentId": {
          "$ref": "#/$defs/opaqueDocumentId"
        },
        "revisionId": {
          "$ref": "#/$defs/opaqueDocumentId"
        },
        "resourceId": {
          "$ref": "#/$defs/id"
        }
      },
      "required": [],
      "additionalProperties": false,
      "description": "Historical source; hashes refer to exact source bytes, not the current document. No automatic retrieval.",
      "minProperties": 1,
      "dependentRequired": {
        "revisionId": [
          "documentId"
        ]
      }
    },
    "provenanceRecord": {
      "type": "object",
      "properties": {
        "id": {
          "$ref": "#/$defs/id"
        },
        "action": {
          "enum": [
            "create",
            "import",
            "conversion",
            "edit",
            "transpose",
            "merge",
            "generation",
            "other"
          ]
        },
        "description": {
          "type": "string"
        },
        "tool": {
          "$ref": "#/$defs/software"
        },
        "sources": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/provenanceSource"
          }
        },
        "semitones": {
          "type": "integer",
          "minimum": -127,
          "maximum": 127
        },
        "beforeKey": {
          "$ref": "#/$defs/key"
        },
        "afterKey": {
          "$ref": "#/$defs/key"
        }
      },
      "required": [
        "id",
        "action"
      ],
      "additionalProperties": false,
      "allOf": [
        {
          "if": {
            "not": {
              "properties": {
                "action": {
                  "const": "transpose"
                }
              },
              "required": [
                "action"
              ]
            }
          },
          "then": {
            "not": {
              "required": [
                "semitones"
              ]
            }
          }
        }
      ]
    },
    "provenance": {
      "type": "object",
      "properties": {
        "records": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/provenanceRecord"
          }
        }
      },
      "required": [
        "records"
      ],
      "additionalProperties": false,
      "description": "Non-executable historical assertions; not composer credits and not a substitute for current metadata. Does not prove authorship or operation correctness."
    },
    "midiChannel": {
      "type": "integer",
      "minimum": 1,
      "maximum": 16,
      "description": "Human-readable MIDI 1.0 channel number 1..16. Wire status-nibble channel = value - 1."
    },
    "midiBus": {
      "type": "object",
      "description": "Document-local logical MIDI destination. Each bus has its own MIDI channel namespace. It is not a physical OS/USB/DAW port binding.",
      "properties": {
        "id": {
          "$ref": "#/$defs/id"
        },
        "name": {
          "type": "string"
        }
      },
      "required": [
        "id",
        "name"
      ],
      "additionalProperties": false
    },
    "midi": {
      "type": "object",
      "properties": {
        "buses": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/midiBus"
          }
        }
      },
      "required": [
        "buses"
      ],
      "additionalProperties": false
    },
    "mpeSettings": {
      "type": "object",
      "description": "Semantic MPE zone declaration. Lower-zone master is channel 1 and upper-zone master is channel 16; member channels are derived contiguously from memberChannelCount.",
      "properties": {
        "zone": {
          "enum": [
            "lower",
            "upper"
          ]
        },
        "memberChannelCount": {
          "type": "integer",
          "minimum": 1,
          "maximum": 15
        }
      },
      "required": [
        "zone",
        "memberChannelCount"
      ],
      "additionalProperties": false
    },
    "trackMidi": {
      "type": "object",
      "description": "Optional MIDI channel/routing interpretation for a track. busId is a logical OSTF bus, never a physical MIDI port.",
      "properties": {
        "busId": {
          "$ref": "#/$defs/id"
        },
        "mode": {
          "enum": [
            "singleChannel",
            "multiChannel",
            "mpe"
          ]
        },
        "channel": {
          "$ref": "#/$defs/midiChannel"
        },
        "mpe": {
          "$ref": "#/$defs/mpeSettings"
        }
      },
      "required": [
        "mode"
      ],
      "additionalProperties": false,
      "allOf": [
        {
          "if": {
            "properties": {
              "mode": {
                "const": "singleChannel"
              }
            },
            "required": [
              "mode"
            ]
          },
          "then": {
            "required": [
              "channel"
            ],
            "not": {
              "required": [
                "mpe"
              ]
            }
          }
        },
        {
          "if": {
            "properties": {
              "mode": {
                "const": "multiChannel"
              }
            },
            "required": [
              "mode"
            ]
          },
          "then": {
            "not": {
              "anyOf": [
                {
                  "required": [
                    "channel"
                  ]
                },
                {
                  "required": [
                    "mpe"
                  ]
                }
              ]
            }
          }
        },
        {
          "if": {
            "properties": {
              "mode": {
                "const": "mpe"
              }
            },
            "required": [
              "mode"
            ]
          },
          "then": {
            "required": [
              "mpe"
            ],
            "not": {
              "required": [
                "channel"
              ]
            }
          }
        }
      ]
    },
    "controlChangeEvent": {
      "type": "object",
      "description": "MIDI 1.0 Control Change. Controllers 120..127 use channelMode instead.",
      "properties": {
        "id": {
          "$ref": "#/$defs/id"
        },
        "start": {
          "$ref": "#/$defs/signed"
        },
        "order": {
          "$ref": "#/$defs/signed",
          "default": 1,
          "description": "Same-tick ordering key. Omitted means 1. Note Off has implicit order 0 and Note On implicit order 2; ties are resolved by the normative ordering rules."
        },
        "channel": {
          "$ref": "#/$defs/midiChannel"
        },
        "type": {
          "const": "controlChange"
        },
        "targetNoteId": {
          "$ref": "#/$defs/id",
          "description": "Optional semantic association with an existing concrete note. It does not replace channel/pitch wire semantics."
        },
        "controller": {
          "type": "integer",
          "minimum": 0,
          "maximum": 119
        },
        "value": {
          "type": "integer",
          "minimum": 0,
          "maximum": 127
        }
      },
      "required": [
        "id",
        "start",
        "type",
        "controller",
        "value"
      ],
      "additionalProperties": false
    },
    "channelModeEvent": {
      "type": "object",
      "description": "MIDI 1.0 Channel Mode message represented separately from ordinary Control Change.",
      "properties": {
        "id": {
          "$ref": "#/$defs/id"
        },
        "start": {
          "$ref": "#/$defs/signed"
        },
        "order": {
          "$ref": "#/$defs/signed",
          "default": 1,
          "description": "Same-tick ordering key. Omitted means 1. Note Off has implicit order 0 and Note On implicit order 2; ties are resolved by the normative ordering rules."
        },
        "channel": {
          "$ref": "#/$defs/midiChannel"
        },
        "type": {
          "const": "channelMode"
        },
        "controller": {
          "type": "integer",
          "minimum": 120,
          "maximum": 127
        },
        "value": {
          "type": "integer",
          "minimum": 0,
          "maximum": 127
        }
      },
      "required": [
        "id",
        "start",
        "type",
        "controller",
        "value"
      ],
      "additionalProperties": false
    },
    "programChangeEvent": {
      "type": "object",
      "description": "MIDI 1.0 Program Change using the wire data value 0..127. UI may display 1..128.",
      "properties": {
        "id": {
          "$ref": "#/$defs/id"
        },
        "start": {
          "$ref": "#/$defs/signed"
        },
        "order": {
          "$ref": "#/$defs/signed",
          "default": 1,
          "description": "Same-tick ordering key. Omitted means 1. Note Off has implicit order 0 and Note On implicit order 2; ties are resolved by the normative ordering rules."
        },
        "channel": {
          "$ref": "#/$defs/midiChannel"
        },
        "type": {
          "const": "programChange"
        },
        "program": {
          "type": "integer",
          "minimum": 0,
          "maximum": 127
        }
      },
      "required": [
        "id",
        "start",
        "type",
        "program"
      ],
      "additionalProperties": false
    },
    "pitchBendEvent": {
      "type": "object",
      "description": "MIDI 1.0 14-bit Pitch Bend Change. Bend range is receiver state/RPN data, not encoded in value14.",
      "properties": {
        "id": {
          "$ref": "#/$defs/id"
        },
        "start": {
          "$ref": "#/$defs/signed"
        },
        "order": {
          "$ref": "#/$defs/signed",
          "default": 1,
          "description": "Same-tick ordering key. Omitted means 1. Note Off has implicit order 0 and Note On implicit order 2; ties are resolved by the normative ordering rules."
        },
        "channel": {
          "$ref": "#/$defs/midiChannel"
        },
        "type": {
          "const": "pitchBend"
        },
        "targetNoteId": {
          "$ref": "#/$defs/id",
          "description": "Optional semantic association with an existing concrete note. It does not replace channel/pitch wire semantics."
        },
        "value14": {
          "type": "integer",
          "minimum": 0,
          "maximum": 16383,
          "description": "Raw MIDI 1.0 14-bit pitch-bend value; center is 8192."
        }
      },
      "required": [
        "id",
        "start",
        "type",
        "value14"
      ],
      "additionalProperties": false
    },
    "channelPressureEvent": {
      "type": "object",
      "description": "MIDI 1.0 Channel Pressure (channel aftertouch).",
      "properties": {
        "id": {
          "$ref": "#/$defs/id"
        },
        "start": {
          "$ref": "#/$defs/signed"
        },
        "order": {
          "$ref": "#/$defs/signed",
          "default": 1,
          "description": "Same-tick ordering key. Omitted means 1. Note Off has implicit order 0 and Note On implicit order 2; ties are resolved by the normative ordering rules."
        },
        "channel": {
          "$ref": "#/$defs/midiChannel"
        },
        "type": {
          "const": "channelPressure"
        },
        "targetNoteId": {
          "$ref": "#/$defs/id",
          "description": "Optional semantic association with an existing concrete note. It does not replace channel/pitch wire semantics."
        },
        "value": {
          "type": "integer",
          "minimum": 0,
          "maximum": 127
        }
      },
      "required": [
        "id",
        "start",
        "type",
        "value"
      ],
      "additionalProperties": false
    },
    "polyPressureEvent": {
      "type": "object",
      "description": "MIDI 1.0 Polyphonic Key Pressure (poly aftertouch).",
      "properties": {
        "id": {
          "$ref": "#/$defs/id"
        },
        "start": {
          "$ref": "#/$defs/signed"
        },
        "order": {
          "$ref": "#/$defs/signed",
          "default": 1,
          "description": "Same-tick ordering key. Omitted means 1. Note Off has implicit order 0 and Note On implicit order 2; ties are resolved by the normative ordering rules."
        },
        "channel": {
          "$ref": "#/$defs/midiChannel"
        },
        "type": {
          "const": "polyPressure"
        },
        "targetNoteId": {
          "$ref": "#/$defs/id",
          "description": "Optional semantic association with an existing concrete note. It does not replace channel/pitch wire semantics."
        },
        "pitch": {
          "$ref": "#/$defs/pitch"
        },
        "value": {
          "type": "integer",
          "minimum": 0,
          "maximum": 127
        }
      },
      "required": [
        "id",
        "start",
        "type",
        "pitch",
        "value"
      ],
      "additionalProperties": false
    },
    "midiEvent": {
      "oneOf": [
        {
          "$ref": "#/$defs/controlChangeEvent"
        },
        {
          "$ref": "#/$defs/channelModeEvent"
        },
        {
          "$ref": "#/$defs/programChangeEvent"
        },
        {
          "$ref": "#/$defs/pitchBendEvent"
        },
        {
          "$ref": "#/$defs/channelPressureEvent"
        },
        {
          "$ref": "#/$defs/polyPressureEvent"
        }
      ]
    },
    "lyricVoice": {
      "type": "object",
      "description": "Explicit relationship between a vocal/melody track and a lyric document. Several voices may reference the same lyric document without duplicating text.",
      "properties": {
        "id": {
          "$ref": "#/$defs/id"
        },
        "name": {
          "type": "string"
        },
        "role": {
          "type": "string",
          "minLength": 1,
          "description": "Open authored role. Recommended values include lead, harmony, backing, unison, double, counter, adlib, response."
        },
        "trackId": {
          "$ref": "#/$defs/id"
        },
        "documentId": {
          "$ref": "#/$defs/id"
        },
        "vocalProfile": {
          "$ref": "#/$defs/vocalProfile",
          "description": "Optional engine-neutral vocal defaults; absence does not mean an instrument voice."
        }
      },
      "required": [
        "id",
        "trackId",
        "documentId"
      ],
      "additionalProperties": false
    },
    "playablePitchRange": {
      "type": "object",
      "properties": {
        "lowPitch": {
          "$ref": "#/$defs/pitch"
        },
        "highPitch": {
          "$ref": "#/$defs/pitch"
        }
      },
      "required": [
        "lowPitch",
        "highPitch"
      ],
      "additionalProperties": false,
      "description": "Authored playable pitch capability in the same 0..127 pitch-number domain as melodic notes. Semantic rule: lowPitch <= highPitch."
    },
    "directionPitchCollection": {
      "type": "object",
      "properties": {
        "tonic": {
          "$ref": "#/$defs/spelledPitchClass"
        },
        "intervals": {
          "type": "array",
          "items": {
            "type": "integer",
            "minimum": 0,
            "maximum": 11
          },
          "minItems": 1,
          "maxItems": 12,
          "uniqueItems": true,
          "contains": {
            "const": 0
          }
        },
        "label": {
          "type": "string"
        }
      },
      "required": [
        "tonic",
        "intervals"
      ],
      "additionalProperties": false,
      "description": "Direction-local pitch-class collection relative to tonic. It is not a harmonic scale-context object and has no independent timeline identity."
    },
    "directionPitchSource": {
      "oneOf": [
        {
          "type": "object",
          "properties": {
            "type": {
              "const": "effectiveKeyScale"
            }
          },
          "required": [
            "type"
          ],
          "additionalProperties": false
        },
        {
          "type": "object",
          "properties": {
            "type": {
              "const": "songScale"
            }
          },
          "required": [
            "type"
          ],
          "additionalProperties": false
        },
        {
          "type": "object",
          "properties": {
            "type": {
              "const": "harmonyScales"
            },
            "scaleIds": {
              "type": "array",
              "items": {
                "$ref": "#/$defs/id"
              },
              "minItems": 1,
              "uniqueItems": true
            }
          },
          "required": [
            "type",
            "scaleIds"
          ],
          "additionalProperties": false
        },
        {
          "type": "object",
          "properties": {
            "type": {
              "const": "explicitScale"
            },
            "scale": {
              "$ref": "#/$defs/directionPitchCollection"
            }
          },
          "required": [
            "type",
            "scale"
          ],
          "additionalProperties": false
        }
      ],
      "description": "Source of pitch vocabulary for an improvisation Direction."
    },
    "improvisationDirectionParameters": {
      "type": "object",
      "properties": {
        "pitchSource": {
          "$ref": "#/$defs/directionPitchSource"
        },
        "adherence": {
          "enum": [
            "strict",
            "preferred"
          ]
        }
      },
      "required": [
        "pitchSource",
        "adherence"
      ],
      "additionalProperties": false
    },
    "playingRoleDirectionParameters": {
      "type": "object",
      "properties": {
        "role": {
          "type": "string",
          "minLength": 1
        }
      },
      "required": [
        "role"
      ],
      "additionalProperties": false
    },
    "pitchRangeDirectionParameters": {
      "type": "object",
      "properties": {
        "lowPitch": {
          "$ref": "#/$defs/pitch"
        },
        "highPitch": {
          "$ref": "#/$defs/pitch"
        },
        "constraint": {
          "enum": [
            "strict",
            "preferred"
          ]
        }
      },
      "required": [
        "lowPitch",
        "highPitch",
        "constraint"
      ],
      "additionalProperties": false
    },
    "vendorDirectionParameters": {
      "type": "object",
      "properties": {
        "namespace": {
          "type": "string",
          "minLength": 3,
          "pattern": "^[a-z][a-z0-9-]*(?:\\.[a-z][a-z0-9-]*){2,}$",
          "not": {
            "pattern": "^org\\.ostf(?:\\.|$)"
          }
        },
        "name": {
          "type": "string",
          "minLength": 1
        },
        "version": {
          "type": "string",
          "minLength": 1
        },
        "data": {
          "type": "object"
        }
      },
      "required": [
        "namespace",
        "name",
        "data"
      ],
      "additionalProperties": false
    },
    "improvisationDirection": {
      "type": "object",
      "properties": {
        "id": {
          "$ref": "#/$defs/id"
        },
        "start": {
          "$ref": "#/$defs/nonnegative"
        },
        "duration": {
          "$ref": "#/$defs/positive"
        },
        "label": {
          "type": "string"
        },
        "instruction": {
          "type": "string",
          "description": "Supplemental human/AI-readable semantic instruction. Structured Core parameters remain authoritative."
        },
        "type": {
          "const": "improvisation"
        },
        "parameters": {
          "$ref": "#/$defs/improvisationDirectionParameters"
        }
      },
      "required": [
        "id",
        "start",
        "duration",
        "type",
        "parameters"
      ],
      "additionalProperties": false
    },
    "playingRoleDirection": {
      "type": "object",
      "properties": {
        "id": {
          "$ref": "#/$defs/id"
        },
        "start": {
          "$ref": "#/$defs/nonnegative"
        },
        "duration": {
          "$ref": "#/$defs/positive"
        },
        "label": {
          "type": "string"
        },
        "instruction": {
          "type": "string",
          "description": "Supplemental human/AI-readable semantic instruction. Structured Core parameters remain authoritative."
        },
        "type": {
          "const": "playingRole"
        },
        "parameters": {
          "$ref": "#/$defs/playingRoleDirectionParameters"
        }
      },
      "required": [
        "id",
        "start",
        "duration",
        "type",
        "parameters"
      ],
      "additionalProperties": false
    },
    "pitchRangeDirection": {
      "type": "object",
      "properties": {
        "id": {
          "$ref": "#/$defs/id"
        },
        "start": {
          "$ref": "#/$defs/nonnegative"
        },
        "duration": {
          "$ref": "#/$defs/positive"
        },
        "label": {
          "type": "string"
        },
        "instruction": {
          "type": "string",
          "description": "Supplemental human/AI-readable semantic instruction. Structured Core parameters remain authoritative."
        },
        "type": {
          "const": "pitchRange"
        },
        "parameters": {
          "$ref": "#/$defs/pitchRangeDirectionParameters"
        }
      },
      "required": [
        "id",
        "start",
        "duration",
        "type",
        "parameters"
      ],
      "additionalProperties": false
    },
    "vendorRangeDirection": {
      "type": "object",
      "properties": {
        "id": {
          "$ref": "#/$defs/id"
        },
        "start": {
          "$ref": "#/$defs/nonnegative"
        },
        "duration": {
          "$ref": "#/$defs/positive"
        },
        "label": {
          "type": "string"
        },
        "instruction": {
          "type": "string",
          "description": "Supplemental human/AI-readable semantic instruction. Structured Core parameters remain authoritative."
        },
        "type": {
          "const": "vendor"
        },
        "parameters": {
          "$ref": "#/$defs/vendorDirectionParameters"
        }
      },
      "required": [
        "id",
        "start",
        "duration",
        "type",
        "parameters"
      ],
      "additionalProperties": false
    },
    "vendorPointDirection": {
      "type": "object",
      "properties": {
        "id": {
          "$ref": "#/$defs/id"
        },
        "at": {
          "$ref": "#/$defs/nonnegative"
        },
        "type": {
          "const": "vendor"
        },
        "parameters": {
          "$ref": "#/$defs/vendorDirectionParameters"
        },
        "label": {
          "type": "string"
        },
        "instruction": {
          "type": "string",
          "description": "Supplemental human/AI-readable semantic instruction. Structured/vendor parameters remain authoritative."
        }
      },
      "required": [
        "id",
        "at",
        "type",
        "parameters"
      ],
      "additionalProperties": false
    },
    "trackDirection": {
      "oneOf": [
        {
          "$ref": "#/$defs/improvisationDirection"
        },
        {
          "$ref": "#/$defs/playingRoleDirection"
        },
        {
          "$ref": "#/$defs/pitchRangeDirection"
        },
        {
          "$ref": "#/$defs/vendorRangeDirection"
        },
        {
          "$ref": "#/$defs/vendorPointDirection"
        },
        {
          "$ref": "#/$defs/phrasingDirection"
        },
        {
          "$ref": "#/$defs/vocalFreedomDirection"
        }
      ],
      "description": "Typed semantic instruction owned by a track and positioned on the OSTF global timebase."
    },
    "vocalPhonetics": {
      "type": "object",
      "description": "Ordered phoneme symbols for a lyric unit, not an absolute pronunciation engine command.",
      "properties": {
        "alphabet": {
          "enum": [
            "ipa",
            "xsampa",
            "arpabet",
            "other"
          ]
        },
        "language": {
          "type": "string",
          "minLength": 1
        },
        "symbols": {
          "type": "array",
          "minItems": 1,
          "items": {
            "type": "string",
            "minLength": 1
          }
        },
        "namespace": {
          "type": "string",
          "minLength": 1
        },
        "preferred": {
          "type": "boolean",
          "description": "Optional preference only within the same (alphabet, language) set for this lyricUnit. At most one preferred variant per key; absent does not imply false or a guaranteed conversion."
        }
      },
      "required": [
        "alphabet",
        "symbols"
      ],
      "additionalProperties": false,
      "allOf": [
        {
          "if": {
            "properties": {
              "alphabet": {
                "const": "other"
              }
            },
            "required": [
              "alphabet"
            ]
          },
          "then": {
            "required": [
              "namespace"
            ]
          }
        }
      ]
    },
    "vocalProfile": {
      "type": "object",
      "description": "Voice default independent of commercial singer preset or license.",
      "properties": {
        "language": {
          "type": "string",
          "minLength": 1
        },
        "deliveryMode": {
          "enum": [
            "sing",
            "rap",
            "speak",
            "hum"
          ]
        },
        "voiceDescription": {
          "type": "string",
          "minLength": 1
        }
      },
      "additionalProperties": false
    },
    "vocalPerformance": {
      "type": "object",
      "description": "Performance belonging to exactly one lyric voice within a containing clip.",
      "properties": {
        "id": {
          "$ref": "#/$defs/id"
        },
        "voiceId": {
          "$ref": "#/$defs/id"
        },
        "phonemeEvents": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/vocalPhonemeEvent"
          }
        },
        "pitchCurves": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/vocalPitchCurve"
          }
        },
        "expressionCurves": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/vocalExpressionCurve"
          }
        },
        "techniques": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/vocalTechnique"
          }
        },
        "breathEvents": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/vocalBreathEvent"
          }
        },
        "noteIds": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/id"
          },
          "minItems": 1,
          "uniqueItems": true,
          "description": "Optional exact list of existing note IDs performed by this voice in the containing clip. No duplicate note objects. When present it includes all locally aligned note IDs for that voice. When absent, derive ownership only from voice-specific alignments. Never infer from song.melodyTrackIds."
        }
      },
      "required": [
        "id",
        "voiceId"
      ],
      "additionalProperties": false
    },
    "vocalPhonemeEvent": {
      "type": "object",
      "description": "Explicit phoneme timing, expressed in clip-relative ppq ticks, negative allowed with nonnegative absolute song time.",
      "properties": {
        "id": {
          "$ref": "#/$defs/id"
        },
        "unitId": {
          "$ref": "#/$defs/id"
        },
        "noteId": {
          "$ref": "#/$defs/id"
        },
        "alphabet": {
          "enum": [
            "ipa",
            "xsampa",
            "arpabet",
            "other"
          ]
        },
        "namespace": {
          "type": "string",
          "minLength": 1
        },
        "symbol": {
          "type": "string",
          "minLength": 1
        },
        "start": {
          "$ref": "#/$defs/signed"
        },
        "duration": {
          "$ref": "#/$defs/positive"
        },
        "order": {
          "type": "integer",
          "description": "Optional deterministic ordering when multiple phonemeEvents for one voice share the same start tick; distinct within a (voiceId, start) tie group. Not an audio rendering priority."
        }
      },
      "required": [
        "id",
        "unitId",
        "alphabet",
        "symbol",
        "start",
        "duration"
      ],
      "additionalProperties": false,
      "allOf": [
        {
          "if": {
            "properties": {
              "alphabet": {
                "const": "other"
              }
            },
            "required": [
              "alphabet"
            ]
          },
          "then": {
            "required": [
              "namespace"
            ]
          }
        }
      ]
    },
    "vocalCurvePointPitch": {
      "type": "object",
      "properties": {
        "at": {
          "$ref": "#/$defs/signed"
        },
        "value": {
          "type": "number",
          "description": "Semitone offset from the targeted MIDI note, in cents (signed)."
        }
      },
      "required": [
        "at",
        "value"
      ],
      "additionalProperties": false
    },
    "vocalCurvePointNormalized": {
      "type": "object",
      "properties": {
        "at": {
          "$ref": "#/$defs/signed"
        },
        "value": {
          "type": "number",
          "minimum": 0,
          "maximum": 1
        }
      },
      "required": [
        "at",
        "value"
      ],
      "additionalProperties": false
    },
    "vocalPitchCurve": {
      "type": "object",
      "description": "Specific vocal pitch offset for a single concrete Note, in cents; sample points use clip-relative ppq ticks.",
      "properties": {
        "id": {
          "$ref": "#/$defs/id"
        },
        "targetNoteId": {
          "$ref": "#/$defs/id"
        },
        "unit": {
          "const": "cents"
        },
        "interpolation": {
          "enum": [
            "step",
            "linear"
          ]
        },
        "points": {
          "type": "array",
          "minItems": 1,
          "items": {
            "$ref": "#/$defs/vocalCurvePointPitch"
          }
        }
      },
      "required": [
        "id",
        "targetNoteId",
        "unit",
        "interpolation",
        "points"
      ],
      "additionalProperties": false
    },
    "vocalExpressionCurve": {
      "type": "object",
      "description": "Portable vocal parameters, each normalized 0..1, with no promise of perceptually identical output across engines.",
      "properties": {
        "id": {
          "$ref": "#/$defs/id"
        },
        "parameter": {
          "enum": [
            "dynamics",
            "breathiness",
            "tension",
            "brightness",
            "voicing"
          ]
        },
        "interpolation": {
          "enum": [
            "step",
            "linear"
          ]
        },
        "points": {
          "type": "array",
          "minItems": 1,
          "items": {
            "$ref": "#/$defs/vocalCurvePointNormalized"
          }
        },
        "targetNoteId": {
          "$ref": "#/$defs/id",
          "description": "Optional note-specific replacement of a clip-scoped curve of the same parameter while the note is active. Points still use clip-relative ticks. Do not sum both curves."
        }
      },
      "required": [
        "id",
        "parameter",
        "interpolation",
        "points"
      ],
      "additionalProperties": false
    },
    "vocalTechnique": {
      "type": "object",
      "description": "Semantic artistic intention, not deterministic rendering or an extra pitch source.",
      "properties": {
        "id": {
          "$ref": "#/$defs/id"
        },
        "start": {
          "$ref": "#/$defs/signed"
        },
        "duration": {
          "$ref": "#/$defs/positive"
        },
        "kind": {
          "enum": [
            "scoop",
            "fall",
            "vibrato",
            "portamento",
            "legato",
            "staccato",
            "accent",
            "whisper",
            "growl",
            "falsetto",
            "humming",
            "rap",
            "melisma"
          ]
        },
        "intensity": {
          "type": "number",
          "minimum": 0,
          "maximum": 1
        },
        "targetNoteId": {
          "$ref": "#/$defs/id"
        }
      },
      "required": [
        "id",
        "start",
        "duration",
        "kind"
      ],
      "additionalProperties": false
    },
    "vocalBreathEvent": {
      "type": "object",
      "description": "Optional breath marker. The renderer decides whether to synthesize audible breath.",
      "properties": {
        "id": {
          "$ref": "#/$defs/id"
        },
        "start": {
          "$ref": "#/$defs/signed"
        },
        "duration": {
          "$ref": "#/$defs/positive"
        },
        "kind": {
          "enum": [
            "inhale",
            "exhale"
          ]
        },
        "intensity": {
          "type": "number",
          "minimum": 0,
          "maximum": 1
        }
      },
      "required": [
        "id",
        "start",
        "duration",
        "kind"
      ],
      "additionalProperties": false
    },
    "positiveIntRange": {
      "type": "object",
      "properties": {
        "min": {
          "$ref": "#/$defs/positive"
        },
        "max": {
          "$ref": "#/$defs/positive"
        }
      },
      "required": [
        "min",
        "max"
      ],
      "additionalProperties": false,
      "description": "Inclusive tick bounds; semantic check min <= max."
    },
    "nonnegativeNumberRange": {
      "type": "object",
      "properties": {
        "min": {
          "type": "number",
          "minimum": 0,
          "maximum": 128
        },
        "max": {
          "type": "number",
          "minimum": 0,
          "maximum": 128
        }
      },
      "required": [
        "min",
        "max"
      ],
      "additionalProperties": false,
      "description": "Inclusive range; semantic check min <= max. Count distinct note-on groups at equal onset ticks as one onset."
    },
    "phrasingDirectionParameters": {
      "type": "object",
      "properties": {
        "phraseLengthTicks": {
          "$ref": "#/$defs/positiveIntRange"
        },
        "onsetGroupsPerQuarter": {
          "$ref": "#/$defs/nonnegativeNumberRange"
        },
        "development": {
          "enum": [
            "repetition",
            "motivicVariation",
            "sequence",
            "contrast",
            "free"
          ]
        },
        "contour": {
          "enum": [
            "ascending",
            "descending",
            "arch",
            "valley",
            "stable",
            "free"
          ]
        },
        "energyShape": {
          "enum": [
            "rising",
            "falling",
            "arch",
            "valley",
            "stable",
            "free"
          ],
          "description": "Abstract musical-energy direction; not equivalent to output velocity or volume."
        },
        "motifRef": {
          "$ref": "#/$defs/id"
        },
        "adherence": {
          "enum": [
            "strict",
            "preferred"
          ]
        }
      },
      "required": [
        "adherence"
      ],
      "additionalProperties": false,
      "description": "At least one musical property beyond adherence must be authored; motifRef resolves to phraseLibrary.templates[].id.",
      "minProperties": 2
    },
    "phrasingDirection": {
      "type": "object",
      "properties": {
        "id": {
          "$ref": "#/$defs/id"
        },
        "type": {
          "const": "phrasing"
        },
        "start": {
          "$ref": "#/$defs/nonnegative"
        },
        "duration": {
          "$ref": "#/$defs/positive"
        },
        "label": {
          "type": "string"
        },
        "instruction": {
          "type": "string",
          "description": "Non-executable music-text context, subordinate to structured fields."
        },
        "parameters": {
          "$ref": "#/$defs/phrasingDirectionParameters"
        }
      },
      "required": [
        "id",
        "type",
        "start",
        "duration",
        "parameters"
      ],
      "additionalProperties": false,
      "description": "4.3 optional phrasing Track Direction, using global source-timeline ticks."
    },
    "lyricCandidateSet": {
      "type": "object",
      "properties": {
        "phraseIds": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/id"
          },
          "minItems": 1,
          "uniqueItems": true
        }
      },
      "required": [
        "phraseIds"
      ],
      "additionalProperties": false,
      "description": "One ordered candidate sequence of authored Lyric Phrase IDs. No implicit note alignment."
    },
    "vocalFreedomDirectionParameters": {
      "type": "object",
      "properties": {
        "voiceId": {
          "$ref": "#/$defs/id"
        },
        "textPolicy": {
          "enum": [
            "fixed",
            "alternatives",
            "open"
          ]
        },
        "melodyPolicy": {
          "enum": [
            "fixed",
            "ornamentable",
            "open"
          ]
        },
        "vocalizationKind": {
          "enum": [
            "lexical",
            "scat",
            "humming",
            "nonLexical"
          ]
        },
        "candidatePhraseSets": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/lyricCandidateSet"
          },
          "minItems": 2
        },
        "adherence": {
          "enum": [
            "strict",
            "preferred"
          ]
        }
      },
      "required": [
        "voiceId",
        "textPolicy",
        "melodyPolicy",
        "adherence"
      ],
      "additionalProperties": false,
      "description": "Voice-specific freedom policy. Fixed text does not automatically imply fixed melody or vice versa.",
      "if": {
        "properties": {
          "textPolicy": {
            "const": "alternatives"
          }
        },
        "required": [
          "textPolicy"
        ]
      },
      "then": {
        "required": [
          "candidatePhraseSets"
        ]
      },
      "else": {
        "not": {
          "required": [
            "candidatePhraseSets"
          ]
        }
      }
    },
    "vocalFreedomDirection": {
      "type": "object",
      "properties": {
        "id": {
          "$ref": "#/$defs/id"
        },
        "type": {
          "const": "vocalFreedom"
        },
        "start": {
          "$ref": "#/$defs/nonnegative"
        },
        "duration": {
          "$ref": "#/$defs/positive"
        },
        "label": {
          "type": "string"
        },
        "instruction": {
          "type": "string",
          "description": "Non-executable music-text context, subordinate to structured fields."
        },
        "parameters": {
          "$ref": "#/$defs/vocalFreedomDirectionParameters"
        }
      },
      "required": [
        "id",
        "type",
        "start",
        "duration",
        "parameters"
      ],
      "additionalProperties": false,
      "description": "4.3 optional vocalFreedom Track Direction, using global source-timeline ticks."
    },
    "performanceRequirements": {
      "type": "object",
      "properties": {
        "requiredPolyphony": {
          "type": "integer",
          "minimum": 1,
          "maximum": 128
        },
        "requiredPitchRange": {
          "$ref": "#/$defs/playablePitchRange"
        },
        "requiredArticulations": {
          "type": "array",
          "items": {
            "type": "string",
            "minLength": 1
          },
          "minItems": 1,
          "uniqueItems": true
        },
        "peakOnsetGroupsPerQuarter": {
          "type": "number",
          "exclusiveMinimum": 0,
          "maximum": 128
        }
      },
      "required": [],
      "additionalProperties": false,
      "description": "Minimum/peak musical capabilities required to realize this authored part, not an assertion about the performer. No robot mechanics or safety commands.",
      "minProperties": 1
    },
    "performanceScope": {
      "type": "object",
      "properties": {
        "performancePlanId": {
          "$ref": "#/$defs/id"
        },
        "visitId": {
          "$ref": "#/$defs/id"
        }
      },
      "required": [
        "performancePlanId",
        "visitId"
      ],
      "additionalProperties": false,
      "description": "Bind to exactly one finite visit within a specific plan."
    },
    "ensembleInteraction": {
      "type": "object",
      "properties": {
        "id": {
          "$ref": "#/$defs/id"
        },
        "actorTrackId": {
          "$ref": "#/$defs/id"
        },
        "partnerTrackId": {
          "$ref": "#/$defs/id"
        },
        "actorVoiceId": {
          "$ref": "#/$defs/id"
        },
        "partnerVoiceId": {
          "$ref": "#/$defs/id"
        },
        "relation": {
          "enum": [
            "respondTo",
            "followRhythm",
            "alternateWith",
            "leaveSpaceFor",
            "reinforce"
          ]
        },
        "start": {
          "$ref": "#/$defs/nonnegative"
        },
        "duration": {
          "$ref": "#/$defs/positive"
        },
        "scope": {
          "$ref": "#/$defs/performanceScope"
        },
        "responseWindowTicks": {
          "$ref": "#/$defs/positive"
        },
        "adherence": {
          "enum": [
            "strict",
            "preferred"
          ]
        }
      },
      "required": [
        "id",
        "actorTrackId",
        "partnerTrackId",
        "relation",
        "adherence"
      ],
      "additionalProperties": false,
      "description": "Directed actor/partner relationship: different Tracks, or the same Track only with both explicit and different Lyric Voice IDs whose trackId equals the shared Track. Use source tick range, visit scope, or both. No audio, real-time event, or motor control is implied. Same Track without two distinct owned Voices is a semantic error (JSON Schema cannot compare sibling ID values).",
      "anyOf": [
        {
          "required": [
            "start",
            "duration"
          ]
        },
        {
          "required": [
            "scope"
          ]
        }
      ],
      "dependentRequired": {
        "start": [
          "duration"
        ],
        "duration": [
          "start"
        ]
      }
    },
    "visitPart": {
      "type": "object",
      "properties": {
        "trackId": {
          "$ref": "#/$defs/id"
        },
        "role": {
          "type": "string",
          "minLength": 1,
          "description": "Visit-scoped role override of Track default; timed playingRole conflict requires explicitly listed replacement."
        },
        "realization": {
          "enum": [
            "fixed",
            "open",
            "silent"
          ]
        },
        "replacesDirectionIds": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/id"
          },
          "uniqueItems": true,
          "description": "Only explicit source-track playingRole Direction IDs may be replaced by the visit role."
        }
      },
      "required": [
        "trackId",
        "realization"
      ],
      "additionalProperties": false,
      "description": "A part rule within one performance visit, not a mutation of the source Track."
    },
    "performanceVisit": {
      "type": "object",
      "properties": {
        "id": {
          "$ref": "#/$defs/id"
        },
        "ordinal": {
          "$ref": "#/$defs/nonnegative"
        },
        "label": {
          "type": "string"
        },
        "sourceSectionIds": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/id"
          },
          "minItems": 1
        },
        "sourceRange": {
          "$ref": "#/$defs/range"
        },
        "parts": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/visitPart"
          }
        }
      },
      "required": [
        "id",
        "ordinal",
        "parts"
      ],
      "additionalProperties": false,
      "description": "Finite visit; exactly one source selector. Ordinals must be 0..N-1 in unique sequence within one plan.",
      "oneOf": [
        {
          "required": [
            "sourceSectionIds"
          ]
        },
        {
          "required": [
            "sourceRange"
          ]
        }
      ],
      "not": {
        "required": [
          "sourceSectionIds",
          "sourceRange"
        ]
      }
    },
    "performancePlan": {
      "type": "object",
      "properties": {
        "id": {
          "$ref": "#/$defs/id"
        },
        "name": {
          "type": "string"
        },
        "mode": {
          "const": "orderedFinite"
        },
        "defaultRealization": {
          "enum": [
            "fixed",
            "silent",
            "unspecified"
          ],
          "description": "Explicit policy for unlisted tracks per visit; unspecified cannot claim deterministic replay."
        },
        "visits": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/performanceVisit"
          },
          "minItems": 1
        }
      },
      "required": [
        "id",
        "mode",
        "defaultRealization",
        "visits"
      ],
      "additionalProperties": false,
      "description": "Opt-in finite expanded playthrough. Source Section/Tick remains authoritative. No implicit cues, indefinite loops, or network session state."
    }
  }
}
```

<a id="def-id"></a>
## id

No direct `properties` table (object may be an enum, scalar, array or a composition).

### Exact JSON Schema object

```json
{
  "type": "string",
  "pattern": "^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$",
  "not": {
    "pattern": "[\\r\\n\\u2028\\u2029]"
  }
}
```

<a id="def-nonnegative"></a>
## nonnegative

No direct `properties` table (object may be an enum, scalar, array or a composition).

### Exact JSON Schema object

```json
{
  "type": "integer",
  "minimum": 0,
  "maximum": 9007199254740991
}
```

<a id="def-positive"></a>
## positive

No direct `properties` table (object may be an enum, scalar, array or a composition).

### Exact JSON Schema object

```json
{
  "type": "integer",
  "minimum": 1,
  "maximum": 9007199254740991
}
```

<a id="def-signed"></a>
## signed

No direct `properties` table (object may be an enum, scalar, array or a composition).

### Exact JSON Schema object

```json
{
  "type": "integer",
  "minimum": -9007199254740991,
  "maximum": 9007199254740991
}
```

<a id="def-pitch"></a>
## pitch

No direct `properties` table (object may be an enum, scalar, array or a composition).

### Exact JSON Schema object

```json
{
  "type": "integer",
  "minimum": 0,
  "maximum": 127
}
```

<a id="def-ref"></a>
## ref

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `type` | `enum ["section", "track", "clip", "note", "chord", "scale", "soundSlot", "drumKit", "lyricDocument", "lyricPhrase", "lyricUnit", "lyricAlignment", "resource", "genre", "contributor", "credit", "alternateTitle", "mood", "keyChange", "phraseTemplate", "phraseInstance", "clipChoiceGroup", "clipCandidate", "roleDefinition", "generationProcess", "provenanceRecord", "midiBus", "midiEvent", "lyricVoice", "trackDirection", "ensembleInteraction", "performancePlan", "performanceVisit"]` | Yes |  |
| `id` | `#/$defs/id` | Yes |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "type": {
      "enum": [
        "section",
        "track",
        "clip",
        "note",
        "chord",
        "scale",
        "soundSlot",
        "drumKit",
        "lyricDocument",
        "lyricPhrase",
        "lyricUnit",
        "lyricAlignment",
        "resource",
        "genre",
        "contributor",
        "credit",
        "alternateTitle",
        "mood",
        "keyChange",
        "phraseTemplate",
        "phraseInstance",
        "clipChoiceGroup",
        "clipCandidate",
        "roleDefinition",
        "generationProcess",
        "provenanceRecord",
        "midiBus",
        "midiEvent",
        "lyricVoice",
        "trackDirection",
        "ensembleInteraction",
        "performancePlan",
        "performanceVisit"
      ]
    },
    "id": {
      "$ref": "#/$defs/id"
    }
  },
  "required": [
    "type",
    "id"
  ],
  "additionalProperties": false
}
```

<a id="def-range"></a>
## range

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `start` | `#/$defs/nonnegative` | Yes |  |
| `duration` | `#/$defs/positive` | Yes |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "start": {
      "$ref": "#/$defs/nonnegative"
    },
    "duration": {
      "$ref": "#/$defs/positive"
    }
  },
  "required": [
    "start",
    "duration"
  ],
  "additionalProperties": false
}
```

<a id="def-spelledpitchclass"></a>
## spelledPitchClass

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `step` | `enum ["A", "B", "C", "D", "E", "F", "G"]` | Yes |  |
| `alter` | `integer` | Yes |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "step": {
      "enum": [
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G"
      ]
    },
    "alter": {
      "type": "integer",
      "minimum": -2,
      "maximum": 2
    }
  },
  "required": [
    "step",
    "alter"
  ],
  "additionalProperties": false
}
```

<a id="def-song"></a>
## song

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `title` | `string` | Yes |  |
| `primaryMelodyTrackId` | `#/$defs/id` | No/conditional |  |
| `localizedTitles` | `#/$defs/localizedNames` | No/conditional | Optional localized song-title alternatives. song.title is the stable fallback. |
| `subtitle` | `string` | No/conditional | Optional original-language subtitle. |
| `description` | `string` | No/conditional | Optional original-language description, including Unicode and line breaks. |
| `alternateTitles` | `array<#/$defs/alternateTitle>` | No/conditional | Additional stable-ID source-language titles. |
| `credits` | `array<#/$defs/credit>` | No/conditional | Ordered credit assignments to contributors. Multiple roles and duplicate contributors permitted. |
| `genres` | `array<#/$defs/genre>` | No/conditional | Optional open-ended ordered genre tags; zero or more allowed. Order is authored display preference, first item is primary if a primary label i... |
| `key` | `#/$defs/key` | No/conditional |  |
| `scale` | `#/$defs/scaleDefinition` | No/conditional |  |
| `languages` | `array<string>` | No/conditional |  |
| `primaryLyricDocumentId` | `#/$defs/id` | No/conditional |  |
| `moods` | `array<#/$defs/mood>` | No/conditional |  |
| `rights` | `#/$defs/rightsStatement` | No/conditional |  |
| `melodyTrackIds` | `array<#/$defs/id>` | No/conditional | Optional ordered set of tracks explicitly authored as melody-bearing tracks. If present with primaryMelodyTrackId, the primary track must be a... |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "title": {
      "type": "string"
    },
    "primaryMelodyTrackId": {
      "$ref": "#/$defs/id"
    },
    "localizedTitles": {
      "$ref": "#/$defs/localizedNames",
      "description": "Optional localized song-title alternatives. song.title is the stable fallback."
    },
    "subtitle": {
      "type": "string",
      "description": "Optional original-language subtitle."
    },
    "description": {
      "type": "string",
      "description": "Optional original-language description, including Unicode and line breaks."
    },
    "alternateTitles": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/alternateTitle"
      },
      "description": "Additional stable-ID source-language titles."
    },
    "credits": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/credit"
      },
      "description": "Ordered credit assignments to contributors. Multiple roles and duplicate contributors permitted."
    },
    "genres": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/genre"
      },
      "description": "Optional open-ended ordered genre tags; zero or more allowed. Order is authored display preference, first item is primary if a primary label is desired, not a generator weight. Absent means unspecified."
    },
    "key": {
      "$ref": "#/$defs/key"
    },
    "scale": {
      "$ref": "#/$defs/scaleDefinition"
    },
    "languages": {
      "type": "array",
      "items": {
        "type": "string",
        "minLength": 1,
        "description": "Authored language tag, preferably BCP 47. Unknown spelling is retained; case-insensitive duplicate tags forbidden."
      },
      "uniqueItems": true
    },
    "primaryLyricDocumentId": {
      "$ref": "#/$defs/id"
    },
    "moods": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/mood"
      }
    },
    "rights": {
      "$ref": "#/$defs/rightsStatement"
    },
    "melodyTrackIds": {
      "type": "array",
      "uniqueItems": true,
      "items": {
        "$ref": "#/$defs/id"
      },
      "description": "Optional ordered set of tracks explicitly authored as melody-bearing tracks. If present with primaryMelodyTrackId, the primary track must be a member."
    }
  },
  "required": [
    "title"
  ],
  "additionalProperties": false
}
```

<a id="def-section"></a>
## section

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `id` | `#/$defs/id` | Yes |  |
| `name` | `string` | Yes |  |
| `start` | `#/$defs/nonnegative` | Yes |  |
| `duration` | `#/$defs/positive` | Yes |  |
| `role` | `string` | No/conditional |  |
| `localizedNames` | `#/$defs/localizedNames` | No/conditional | Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity. |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "name": {
      "type": "string",
      "minLength": 1
    },
    "start": {
      "$ref": "#/$defs/nonnegative"
    },
    "duration": {
      "$ref": "#/$defs/positive"
    },
    "role": {
      "type": "string"
    },
    "localizedNames": {
      "$ref": "#/$defs/localizedNames",
      "description": "Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity."
    }
  },
  "required": [
    "id",
    "name",
    "start",
    "duration"
  ],
  "additionalProperties": false
}
```

<a id="def-tempo"></a>
## tempo

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `at` | `#/$defs/nonnegative` | Yes |  |
| `bpm` | `number` | Yes |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "at": {
      "$ref": "#/$defs/nonnegative"
    },
    "bpm": {
      "type": "number",
      "exclusiveMinimum": 0,
      "maximum": 1000
    }
  },
  "required": [
    "at",
    "bpm"
  ],
  "additionalProperties": false
}
```

<a id="def-meter"></a>
## meter

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `at` | `#/$defs/nonnegative` | Yes |  |
| `numerator` | `integer` | Yes |  |
| `denominator` | `enum [1, 2, 4, 8, 16, 32, 64]` | Yes |  |
| `beatGroups` | `array<integer>` | No/conditional | Optional additive grouping in denominator units. Values must sum to numerator. Descriptive only; does not change note timestamps. |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "at": {
      "$ref": "#/$defs/nonnegative"
    },
    "numerator": {
      "type": "integer",
      "minimum": 1,
      "maximum": 64
    },
    "denominator": {
      "enum": [
        1,
        2,
        4,
        8,
        16,
        32,
        64
      ],
      "type": "integer"
    },
    "beatGroups": {
      "type": "array",
      "items": {
        "type": "integer",
        "minimum": 1,
        "maximum": 64
      },
      "minItems": 1,
      "maxItems": 64,
      "description": "Optional additive grouping in denominator units. Values must sum to numerator. Descriptive only; does not change note timestamps."
    }
  },
  "required": [
    "at",
    "numerator",
    "denominator"
  ],
  "additionalProperties": false
}
```

<a id="def-timeline"></a>
## timeline

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `sections` | `array<#/$defs/section>` | Yes |  |
| `tempoChanges` | `array<#/$defs/tempo>` | Yes |  |
| `meterChanges` | `array<#/$defs/meter>` | Yes |  |
| `keyChanges` | `array<#/$defs/keyChange>` | No/conditional |  |
| `duration` | `#/$defs/nonnegative` | No/conditional |  |
| `barOrigin` | `#/$defs/nonnegative` | No/conditional |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "sections": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/section"
      }
    },
    "tempoChanges": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/tempo"
      },
      "minItems": 1
    },
    "meterChanges": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/meter"
      },
      "minItems": 1
    },
    "keyChanges": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/keyChange"
      }
    },
    "duration": {
      "$ref": "#/$defs/nonnegative"
    },
    "barOrigin": {
      "$ref": "#/$defs/nonnegative"
    }
  },
  "required": [
    "sections",
    "tempoChanges",
    "meterChanges"
  ],
  "additionalProperties": false
}
```

<a id="def-chord"></a>
## chord

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `id` | `#/$defs/id` | Yes |  |
| `start` | `#/$defs/nonnegative` | Yes |  |
| `duration` | `#/$defs/positive` | Yes |  |
| `label` | `string` | Yes |  |
| `root` | `#/$defs/spelledPitchClass` | No/conditional |  |
| `intervals` | `array<integer>` | No/conditional |  |
| `bass` | `#/$defs/spelledPitchClass` | No/conditional |  |
| `voicing` | `#/$defs/voicing` | No/conditional | Optional pitch snapshot (not an arrangement note sequence). No automatic playback. |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "start": {
      "$ref": "#/$defs/nonnegative"
    },
    "duration": {
      "$ref": "#/$defs/positive"
    },
    "label": {
      "type": "string",
      "minLength": 1
    },
    "root": {
      "$ref": "#/$defs/spelledPitchClass"
    },
    "intervals": {
      "type": "array",
      "items": {
        "type": "integer",
        "minimum": 0,
        "maximum": 35
      },
      "minItems": 1,
      "maxItems": 36,
      "uniqueItems": true,
      "contains": {
        "const": 0
      }
    },
    "bass": {
      "$ref": "#/$defs/spelledPitchClass"
    },
    "voicing": {
      "$ref": "#/$defs/voicing",
      "description": "Optional pitch snapshot (not an arrangement note sequence). No automatic playback."
    }
  },
  "required": [
    "id",
    "start",
    "duration",
    "label"
  ],
  "additionalProperties": false,
  "dependentRequired": {
    "root": [
      "intervals"
    ],
    "intervals": [
      "root"
    ]
  }
}
```

<a id="def-scale"></a>
## scale

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `id` | `#/$defs/id` | Yes |  |
| `start` | `#/$defs/nonnegative` | Yes |  |
| `duration` | `#/$defs/positive` | Yes |  |
| `label` | `string` | No/conditional |  |
| `tonic` | `#/$defs/spelledPitchClass` | Yes |  |
| `intervals` | `array<integer>` | Yes |  |
| `targets` | `array<#/$defs/scaleTarget>` | No/conditional | Optional explicit scope. Absence means general timed context, not a global key. Overlapping contexts are not resolved by array order. |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "start": {
      "$ref": "#/$defs/nonnegative"
    },
    "duration": {
      "$ref": "#/$defs/positive"
    },
    "label": {
      "type": "string"
    },
    "tonic": {
      "$ref": "#/$defs/spelledPitchClass"
    },
    "intervals": {
      "type": "array",
      "items": {
        "type": "integer",
        "minimum": 0,
        "maximum": 11
      },
      "minItems": 1,
      "maxItems": 12,
      "uniqueItems": true,
      "contains": {
        "const": 0
      }
    },
    "targets": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/scaleTarget"
      },
      "minItems": 1,
      "uniqueItems": true,
      "description": "Optional explicit scope. Absence means general timed context, not a global key. Overlapping contexts are not resolved by array order."
    }
  },
  "required": [
    "id",
    "start",
    "duration",
    "tonic",
    "intervals"
  ],
  "additionalProperties": false
}
```

<a id="def-harmony"></a>
## harmony

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `chords` | `array<#/$defs/chord>` | Yes |  |
| `scales` | `array<#/$defs/scale>` | Yes |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "chords": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/chord"
      }
    },
    "scales": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/scale"
      }
    }
  },
  "required": [
    "chords",
    "scales"
  ],
  "additionalProperties": false
}
```

<a id="def-instrument"></a>
## instrument

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `name` | `string` | Yes |  |
| `family` | `string` | No/conditional |  |
| `localizedNames` | `#/$defs/localizedNames` | No/conditional | Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity. |
| `playablePitchRange` | `#/$defs/playablePitchRange` | No/conditional |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "name": {
      "type": "string"
    },
    "family": {
      "type": "string"
    },
    "localizedNames": {
      "$ref": "#/$defs/localizedNames",
      "description": "Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity."
    },
    "playablePitchRange": {
      "$ref": "#/$defs/playablePitchRange"
    }
  },
  "required": [
    "name"
  ],
  "additionalProperties": false
}
```

<a id="def-note"></a>
## note

Concrete Core DAW-note event. The event target is pitch or soundSlotId. Optional 3.5 note-local properties preserve mute, release velocity, probability and velocity variation. pitchRole=fixedTrigger marks a literal MIDI key trigger that must not be musically transposed or analyzed.

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `id` | `#/$defs/id` | Yes |  |
| `start` | `#/$defs/signed` | Yes |  |
| `duration` | `#/$defs/positive` | Yes | Positive note gate in ticks, not the guaranteed audible duration of a one-shot percussion sample. |
| `pitch` | `#/$defs/pitch` | No/conditional |  |
| `soundSlotId` | `#/$defs/id` | No/conditional | Document-local Sound Slot ID. Distinct events and IDs stay distinct even if several slots share a MIDI key; a renderer decides the acoustic ti... |
| `velocity` | `integer` | No/conditional | Optional authored note-on velocity for performed Core notes, 1–127; omit to mean unspecified. It is not a note-off velocity, controller stream... |
| `enabled` | `boolean` | No/conditional | Optional note-local enable state. Omitted means enabled. False preserves the note but suppresses scheduling/playback; it is distinct from prob... |
| `releaseVelocity` | `integer` | No/conditional | Optional MIDI Note Off/release velocity, 0-127. Omit when unspecified; readers must not invent and write back a default. |
| `probability` | `number` | No/conditional | Optional note-playback probability from 0.0 to 1.0. Omitted means 1.0. Random sequence identity is not standardized; materialize notes for det... |
| `velocityDeviation` | `integer` | No/conditional | Optional note-local velocity variation endpoint relative to velocity. Requires velocity. Semantic rule: velocity + velocityDeviation must rema... |
| `pitchRole` | `enum ["musical", "fixedTrigger"]` | No/conditional | Meaning of a pitch note. musical participates in pitch/harmony/transpose operations; fixedTrigger is an exact MIDI key trigger (for example a ... |
| `channel` | `#/$defs/midiChannel` | No/conditional | Optional concrete MIDI channel for this performed note. In singleChannel mode it may be omitted and inherited from the track; in multiChannel/... |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "start": {
      "$ref": "#/$defs/signed"
    },
    "duration": {
      "$ref": "#/$defs/positive",
      "description": "Positive note gate in ticks, not the guaranteed audible duration of a one-shot percussion sample."
    },
    "pitch": {
      "$ref": "#/$defs/pitch"
    },
    "soundSlotId": {
      "$ref": "#/$defs/id",
      "description": "Document-local Sound Slot ID. Distinct events and IDs stay distinct even if several slots share a MIDI key; a renderer decides the acoustic timbre."
    },
    "velocity": {
      "type": "integer",
      "minimum": 1,
      "maximum": 127,
      "description": "Optional authored note-on velocity for performed Core notes, 1–127; omit to mean unspecified. It is not a note-off velocity, controller stream, chord tone, or a sound-rendering guarantee. Never insert an inferred default when saving."
    },
    "enabled": {
      "type": "boolean",
      "default": true,
      "description": "Optional note-local enable state. Omitted means enabled. False preserves the note but suppresses scheduling/playback; it is distinct from probability=0."
    },
    "releaseVelocity": {
      "type": "integer",
      "minimum": 0,
      "maximum": 127,
      "description": "Optional MIDI Note Off/release velocity, 0-127. Omit when unspecified; readers must not invent and write back a default."
    },
    "probability": {
      "type": "number",
      "minimum": 0,
      "maximum": 1,
      "default": 1,
      "description": "Optional note-playback probability from 0.0 to 1.0. Omitted means 1.0. Random sequence identity is not standardized; materialize notes for deterministic interchange."
    },
    "velocityDeviation": {
      "type": "integer",
      "minimum": -126,
      "maximum": 126,
      "default": 0,
      "description": "Optional note-local velocity variation endpoint relative to velocity. Requires velocity. Semantic rule: velocity + velocityDeviation must remain within 1..127. Omitted means 0."
    },
    "pitchRole": {
      "enum": [
        "musical",
        "fixedTrigger"
      ],
      "default": "musical",
      "description": "Meaning of a pitch note. musical participates in pitch/harmony/transpose operations; fixedTrigger is an exact MIDI key trigger (for example a keyswitch) and is never transposed or used as musical-pitch evidence. Allowed only on pitch notes."
    },
    "channel": {
      "$ref": "#/$defs/midiChannel",
      "description": "Optional concrete MIDI channel for this performed note. In singleChannel mode it may be omitted and inherited from the track; in multiChannel/MPE mode semantic rules require explicit channel where channel identity matters."
    }
  },
  "required": [
    "id",
    "start",
    "duration"
  ],
  "additionalProperties": false,
  "oneOf": [
    {
      "required": [
        "pitch"
      ],
      "not": {
        "required": [
          "soundSlotId"
        ]
      }
    },
    {
      "required": [
        "soundSlotId"
      ],
      "not": {
        "required": [
          "pitch"
        ]
      }
    }
  ],
  "description": "Concrete Core DAW-note event. The event target is pitch or soundSlotId. Optional 3.5 note-local properties preserve mute, release velocity, probability and velocity variation. pitchRole=fixedTrigger marks a literal MIDI key trigger that must not be musically transposed or analyzed.",
  "dependentRequired": {
    "velocityDeviation": [
      "velocity"
    ]
  },
  "allOf": [
    {
      "if": {
        "required": [
          "soundSlotId"
        ]
      },
      "then": {
        "not": {
          "required": [
            "pitchRole"
          ]
        }
      }
    }
  ]
}
```

<a id="def-clip"></a>
## clip

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `id` | `#/$defs/id` | Yes |  |
| `name` | `string` | No/conditional |  |
| `start` | `#/$defs/nonnegative` | Yes |  |
| `duration` | `#/$defs/positive` | Yes |  |
| `enabled` | `boolean` | No/conditional |  |
| `notes` | `array<#/$defs/note>` | Yes |  |
| `localizedNames` | `#/$defs/localizedNames` | No/conditional | Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity. |
| `midiEvents` | `array<#/$defs/midiEvent>` | No/conditional | Optional clip-local MIDI performance/control events. start is local to the clip and may be negative if absolute time remains nonnegative. Note... |
| `vocalPerformances` | `array<#/$defs/vocalPerformance>` | No/conditional | Optional voice-specific phoneme and singing-performance data; references lyrics.voices. Notes/MIDI remain authoritative for MIDI playback. |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "name": {
      "type": "string"
    },
    "start": {
      "$ref": "#/$defs/nonnegative"
    },
    "duration": {
      "$ref": "#/$defs/positive"
    },
    "enabled": {
      "type": "boolean",
      "default": true
    },
    "notes": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/note"
      }
    },
    "localizedNames": {
      "$ref": "#/$defs/localizedNames",
      "description": "Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity."
    },
    "midiEvents": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/midiEvent"
      },
      "description": "Optional clip-local MIDI performance/control events. start is local to the clip and may be negative if absolute time remains nonnegative. Notes remain authoritative in notes[]."
    },
    "vocalPerformances": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/vocalPerformance"
      },
      "minItems": 1,
      "description": "Optional voice-specific phoneme and singing-performance data; references lyrics.voices. Notes/MIDI remain authoritative for MIDI playback."
    }
  },
  "required": [
    "id",
    "start",
    "duration",
    "notes"
  ],
  "additionalProperties": false
}
```

<a id="def-track"></a>
## track

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `id` | `#/$defs/id` | Yes |  |
| `name` | `string` | Yes |  |
| `role` | `string` | No/conditional |  |
| `instrument` | `#/$defs/instrument` | No/conditional |  |
| `enabled` | `boolean` | No/conditional |  |
| `clips` | `array<#/$defs/clip>` | Yes |  |
| `trackType` | `enum ["melodic", "drum", "mixed"]` | No/conditional | Semantic event-target category; optional; missing/empty-note tracks may be unknown. It is not a DAW track class. |
| `preferredView` | `enum ["auto", "pianoRoll", "drumGrid"]` | No/conditional | Non-binding presentation preference. Does not change note meaning. |
| `soundSource` | `#/$defs/soundSource` | No/conditional | Optional sound-source selection hint, not a plug-in state, preset blob, or sound guarantee. |
| `localizedNames` | `#/$defs/localizedNames` | No/conditional | Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity. |
| `drumKitId` | `#/$defs/id` | No/conditional | Optional reference to a declared drumKit; only for a drum/mixed or empty inferred track. All stored slot events in the track must belong to th... |
| `midi` | `#/$defs/trackMidi` | No/conditional |  |
| `directions` | `array<#/$defs/trackDirection>` | No/conditional | Optional typed semantic instructions for performance, interpretation, or generation. Uses the global OSTF timebase; it is not a second timeline. |
| `performanceRequirements` | `#/$defs/performanceRequirements` | No/conditional | Portable requirements for realizing this track, not a robot/device capability report. |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "name": {
      "type": "string"
    },
    "role": {
      "type": "string"
    },
    "instrument": {
      "$ref": "#/$defs/instrument"
    },
    "enabled": {
      "type": "boolean",
      "default": true
    },
    "clips": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/clip"
      }
    },
    "trackType": {
      "enum": [
        "melodic",
        "drum",
        "mixed"
      ],
      "description": "Semantic event-target category; optional; missing/empty-note tracks may be unknown. It is not a DAW track class."
    },
    "preferredView": {
      "enum": [
        "auto",
        "pianoRoll",
        "drumGrid"
      ],
      "default": "auto",
      "description": "Non-binding presentation preference. Does not change note meaning."
    },
    "soundSource": {
      "$ref": "#/$defs/soundSource",
      "description": "Optional sound-source selection hint, not a plug-in state, preset blob, or sound guarantee."
    },
    "localizedNames": {
      "$ref": "#/$defs/localizedNames",
      "description": "Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity."
    },
    "drumKitId": {
      "$ref": "#/$defs/id",
      "description": "Optional reference to a declared drumKit; only for a drum/mixed or empty inferred track. All stored slot events in the track must belong to the referenced kit."
    },
    "midi": {
      "$ref": "#/$defs/trackMidi"
    },
    "directions": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/trackDirection"
      },
      "description": "Optional typed semantic instructions for performance, interpretation, or generation. Uses the global OSTF timebase; it is not a second timeline."
    },
    "performanceRequirements": {
      "$ref": "#/$defs/performanceRequirements",
      "description": "Portable requirements for realizing this track, not a robot/device capability report."
    }
  },
  "required": [
    "id",
    "name",
    "clips"
  ],
  "additionalProperties": false,
  "allOf": [
    {
      "if": {
        "properties": {
          "trackType": {
            "const": "melodic"
          }
        },
        "required": [
          "trackType"
        ]
      },
      "then": {
        "not": {
          "required": [
            "drumKitId"
          ]
        }
      }
    }
  ]
}
```

<a id="def-soundslot"></a>
## soundSlot

Document-local stable logical percussion target. Equal roles, names or MIDI note mappings never merge distinct slot IDs. No sample/audio identity is encoded.

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `id` | `#/$defs/id` | Yes |  |
| `name` | `string` | Yes |  |
| `role` | `string` | No/conditional | Optional free-text musical role; not a standardized GM instrument code or an acoustic sample identifier. |
| `midiNote` | `#/$defs/pitch` | No/conditional | Legacy 3.0 MIDI note hint only; not a GM1 declaration or preview timbre identity. |
| `midiMapping` | `#/$defs/midiMapping` | No/conditional | Explicit external MIDI1 output mapping; standard=gm1 is separate from custom even for an equal note number. Not a unique slot or audio identity. |
| `localizedNames` | `#/$defs/localizedNames` | No/conditional | Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity. |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "name": {
      "type": "string"
    },
    "role": {
      "type": "string",
      "description": "Optional free-text musical role; not a standardized GM instrument code or an acoustic sample identifier."
    },
    "midiNote": {
      "$ref": "#/$defs/pitch",
      "description": "Legacy 3.0 MIDI note hint only; not a GM1 declaration or preview timbre identity."
    },
    "midiMapping": {
      "$ref": "#/$defs/midiMapping",
      "description": "Explicit external MIDI1 output mapping; standard=gm1 is separate from custom even for an equal note number. Not a unique slot or audio identity."
    },
    "localizedNames": {
      "$ref": "#/$defs/localizedNames",
      "description": "Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity."
    }
  },
  "required": [
    "id",
    "name"
  ],
  "additionalProperties": false,
  "description": "Document-local stable logical percussion target. Equal roles, names or MIDI note mappings never merge distinct slot IDs. No sample/audio identity is encoded."
}
```

<a id="def-lyricdocument"></a>
## lyricDocument

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `id` | `#/$defs/id` | Yes |  |
| `title` | `string` | No/conditional |  |
| `language` | `string` | No/conditional |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "title": {
      "type": "string"
    },
    "language": {
      "type": "string"
    }
  },
  "required": [
    "id"
  ],
  "additionalProperties": false
}
```

<a id="def-lyricphrase"></a>
## lyricPhrase

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `id` | `#/$defs/id` | Yes |  |
| `documentId` | `#/$defs/id` | Yes |  |
| `text` | `string` | Yes |  |
| `pronunciation` | `string` | No/conditional |  |
| `start` | `#/$defs/nonnegative` | No/conditional |  |
| `duration` | `#/$defs/positive` | No/conditional |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "documentId": {
      "$ref": "#/$defs/id"
    },
    "text": {
      "type": "string"
    },
    "pronunciation": {
      "type": "string"
    },
    "start": {
      "$ref": "#/$defs/nonnegative"
    },
    "duration": {
      "$ref": "#/$defs/positive"
    }
  },
  "required": [
    "id",
    "documentId",
    "text"
  ],
  "additionalProperties": false,
  "dependentRequired": {
    "start": [
      "duration"
    ],
    "duration": [
      "start"
    ]
  }
}
```

<a id="def-lyricunit"></a>
## lyricUnit

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `id` | `#/$defs/id` | Yes |  |
| `phraseId` | `#/$defs/id` | Yes |  |
| `text` | `string` | Yes |  |
| `pronunciation` | `string` | No/conditional |  |
| `start` | `#/$defs/nonnegative` | No/conditional |  |
| `duration` | `#/$defs/positive` | No/conditional |  |
| `phonetics` | `array<#/$defs/vocalPhonetics>` | No/conditional | Optional alternate phoneme token sequences. Do not alter text/pronunciation. Multiple alphabets are permitted. |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "phraseId": {
      "$ref": "#/$defs/id"
    },
    "text": {
      "type": "string"
    },
    "pronunciation": {
      "type": "string"
    },
    "start": {
      "$ref": "#/$defs/nonnegative"
    },
    "duration": {
      "$ref": "#/$defs/positive"
    },
    "phonetics": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/vocalPhonetics"
      },
      "minItems": 1,
      "description": "Optional alternate phoneme token sequences. Do not alter text/pronunciation. Multiple alphabets are permitted."
    }
  },
  "required": [
    "id",
    "phraseId",
    "text"
  ],
  "additionalProperties": false,
  "dependentRequired": {
    "start": [
      "duration"
    ],
    "duration": [
      "start"
    ]
  }
}
```

<a id="def-lyricalignment"></a>
## lyricAlignment

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `id` | `#/$defs/id` | Yes |  |
| `unitIds` | `array<#/$defs/id>` | Yes |  |
| `noteIds` | `array<#/$defs/id>` | Yes |  |
| `voiceId` | `#/$defs/id` | No/conditional | Optional lyricVoice association. When present, aligned units must belong to that voice document and aligned notes must belong to that voice tr... |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "unitIds": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/id"
      },
      "uniqueItems": true,
      "minItems": 1
    },
    "noteIds": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/id"
      },
      "uniqueItems": true,
      "minItems": 1
    },
    "voiceId": {
      "$ref": "#/$defs/id",
      "description": "Optional lyricVoice association. When present, aligned units must belong to that voice document and aligned notes must belong to that voice track."
    }
  },
  "required": [
    "id",
    "unitIds",
    "noteIds"
  ],
  "additionalProperties": false
}
```

<a id="def-lyrics"></a>
## lyrics

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `documents` | `array<#/$defs/lyricDocument>` | Yes |  |
| `phrases` | `array<#/$defs/lyricPhrase>` | Yes |  |
| `units` | `array<#/$defs/lyricUnit>` | Yes |  |
| `alignments` | `array<#/$defs/lyricAlignment>` | Yes |  |
| `voices` | `array<#/$defs/lyricVoice>` | No/conditional | Optional explicit vocal-part relationships for multi-voice, harmony and chorus lyrics. |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "documents": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/lyricDocument"
      }
    },
    "phrases": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/lyricPhrase"
      }
    },
    "units": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/lyricUnit"
      }
    },
    "alignments": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/lyricAlignment"
      }
    },
    "voices": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/lyricVoice"
      },
      "description": "Optional explicit vocal-part relationships for multi-voice, harmony and chorus lyrics."
    }
  },
  "required": [
    "documents",
    "phrases",
    "units",
    "alignments"
  ],
  "additionalProperties": false
}
```

<a id="def-sha256"></a>
## sha256

No direct `properties` table (object may be an enum, scalar, array or a composition).

### Exact JSON Schema object

```json
{
  "type": "string",
  "pattern": "^[0-9a-f]{64}$",
  "not": {
    "pattern": "[\\r\\n\\u2028\\u2029]"
  }
}
```

<a id="def-resource"></a>
## resource

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `id` | `#/$defs/id` | Yes |  |
| `kind` | `enum ["audio", "midi", "text", "other"]` | Yes |  |
| `uri` | `string` | Yes |  |
| `name` | `string` | No/conditional |  |
| `sha256` | `#/$defs/sha256` | No/conditional |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "kind": {
      "enum": [
        "audio",
        "midi",
        "text",
        "other"
      ]
    },
    "uri": {
      "type": "string",
      "minLength": 1
    },
    "name": {
      "type": "string"
    },
    "sha256": {
      "$ref": "#/$defs/sha256"
    }
  },
  "required": [
    "id",
    "kind",
    "uri"
  ],
  "additionalProperties": false
}
```

<a id="def-dependencies"></a>
## dependencies

No direct `properties` table (object may be an enum, scalar, array or a composition).

### Exact JSON Schema object

```json
{
  "oneOf": [
    {
      "type": "object",
      "properties": {
        "scope": {
          "enum": [
            "document",
            "none"
          ]
        }
      },
      "required": [
        "scope"
      ],
      "additionalProperties": false
    },
    {
      "type": "object",
      "properties": {
        "scope": {
          "const": "objects"
        },
        "refs": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/ref"
          },
          "minItems": 1,
          "uniqueItems": true
        }
      },
      "required": [
        "scope",
        "refs"
      ],
      "additionalProperties": false
    }
  ]
}
```

<a id="def-relativeassignment"></a>
## relativeAssignment

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `noteId` | `#/$defs/id` | Yes |  |
| `basis` | `enum ["chordTone", "scaleDegree"]` | Yes |  |
| `contextId` | `#/$defs/id` | Yes |  |
| `anchorPitch` | `#/$defs/pitch` | Yes |  |
| `index` | `integer` | Yes |  |
| `chromaticOffset` | `integer` | Yes |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "noteId": {
      "$ref": "#/$defs/id"
    },
    "basis": {
      "enum": [
        "chordTone",
        "scaleDegree"
      ]
    },
    "contextId": {
      "$ref": "#/$defs/id"
    },
    "anchorPitch": {
      "$ref": "#/$defs/pitch"
    },
    "index": {
      "type": "integer",
      "minimum": 1,
      "maximum": 36
    },
    "chromaticOffset": {
      "type": "integer",
      "minimum": -24,
      "maximum": 24
    }
  },
  "required": [
    "noteId",
    "basis",
    "contextId",
    "anchorPitch",
    "index",
    "chromaticOffset"
  ],
  "additionalProperties": false,
  "allOf": [
    {
      "if": {
        "properties": {
          "basis": {
            "const": "scaleDegree"
          }
        },
        "required": [
          "basis"
        ]
      },
      "then": {
        "properties": {
          "index": {
            "maximum": 12
          }
        }
      }
    }
  ]
}
```

<a id="def-generator"></a>
## generator

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes |  |
| `version` | `string` | Yes |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "id": {
      "type": "string",
      "minLength": 1
    },
    "version": {
      "type": "string",
      "minLength": 1
    }
  },
  "required": [
    "id",
    "version"
  ],
  "additionalProperties": false
}
```

<a id="def-generationinput"></a>
## generationInput

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `role` | `string` | Yes |  |
| `ref` | `#/$defs/ref` | Yes |  |
| `readRange` | `#/$defs/range` | No/conditional |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "role": {
      "type": "string",
      "minLength": 1
    },
    "ref": {
      "$ref": "#/$defs/ref"
    },
    "readRange": {
      "$ref": "#/$defs/range"
    }
  },
  "required": [
    "role",
    "ref"
  ],
  "additionalProperties": false
}
```

<a id="def-generationprocess"></a>
## generationProcess

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `id` | `#/$defs/id` | Yes |  |
| `generator` | `#/$defs/generator` | Yes |  |
| `inputs` | `array<#/$defs/generationInput>` | Yes |  |
| `outputs` | `array<#/$defs/ref>` | Yes |  |
| `targetRange` | `#/$defs/range` | No/conditional |  |
| `protectedNoteIds` | `array<#/$defs/id>` | Yes |  |
| `intent` | `#/$defs/generationIntent` | No/conditional |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "generator": {
      "$ref": "#/$defs/generator"
    },
    "inputs": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/generationInput"
      }
    },
    "outputs": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/ref"
      },
      "minItems": 1
    },
    "targetRange": {
      "$ref": "#/$defs/range"
    },
    "protectedNoteIds": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/id"
      },
      "uniqueItems": true
    },
    "intent": {
      "$ref": "#/$defs/generationIntent"
    }
  },
  "required": [
    "id",
    "generator",
    "inputs",
    "outputs",
    "protectedNoteIds"
  ],
  "additionalProperties": false
}
```

<a id="def-color"></a>
## color

No direct `properties` table (object may be an enum, scalar, array or a composition).

### Exact JSON Schema object

```json
{
  "type": "string",
  "pattern": "^#[0-9A-Fa-f]{6}$",
  "not": {
    "pattern": "[\\r\\n\\u2028\\u2029]"
  }
}
```

<a id="def-roledefinition"></a>
## roleDefinition

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `id` | `#/$defs/id` | Yes |  |
| `name` | `string` | Yes |  |
| `baseRole` | `string` | No/conditional |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "name": {
      "type": "string",
      "minLength": 1
    },
    "baseRole": {
      "type": "string"
    }
  },
  "required": [
    "id",
    "name"
  ],
  "additionalProperties": false
}
```

<a id="def-rolecolormap"></a>
## roleColorMap

No direct `properties` table (object may be an enum, scalar, array or a composition).

### Exact JSON Schema object

```json
{
  "type": "object",
  "additionalProperties": {
    "$ref": "#/$defs/color"
  }
}
```

<a id="def-customrolecolormap"></a>
## customRoleColorMap

No direct `properties` table (object may be an enum, scalar, array or a composition).

### Exact JSON Schema object

```json
{
  "type": "object",
  "propertyNames": {
    "$ref": "#/$defs/id"
  },
  "additionalProperties": {
    "$ref": "#/$defs/color"
  }
}
```

<a id="def-objectcolor"></a>
## objectColor

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `target` | `#/$defs/ref` | Yes |  |
| `color` | `#/$defs/color` | Yes |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "target": {
      "$ref": "#/$defs/ref"
    },
    "color": {
      "$ref": "#/$defs/color"
    }
  },
  "required": [
    "target",
    "color"
  ],
  "additionalProperties": false
}
```

<a id="def-phrasetemplate"></a>
## phraseTemplate

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `id` | `#/$defs/id` | Yes |  |
| `duration` | `#/$defs/positive` | Yes |  |
| `notes` | `array<#/$defs/corePhraseSourceNote>` | Yes |  |
| `name` | `string` | No/conditional |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "duration": {
      "$ref": "#/$defs/positive"
    },
    "notes": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/corePhraseSourceNote"
      }
    },
    "name": {
      "type": "string"
    }
  },
  "required": [
    "id",
    "duration",
    "notes"
  ],
  "additionalProperties": false
}
```

<a id="def-phrasenotemapping"></a>
## phraseNoteMapping

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `templateNoteId` | `#/$defs/id` | Yes |  |
| `repeatIndex` | `#/$defs/nonnegative` | Yes |  |
| `noteId` | `#/$defs/id` | Yes |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "templateNoteId": {
      "$ref": "#/$defs/id"
    },
    "repeatIndex": {
      "$ref": "#/$defs/nonnegative"
    },
    "noteId": {
      "$ref": "#/$defs/id"
    }
  },
  "required": [
    "templateNoteId",
    "repeatIndex",
    "noteId"
  ],
  "additionalProperties": false
}
```

<a id="def-phraseinstance"></a>
## phraseInstance

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `id` | `#/$defs/id` | Yes |  |
| `templateId` | `#/$defs/id` | Yes |  |
| `clipId` | `#/$defs/id` | Yes |  |
| `repeatCount` | `#/$defs/positive` | Yes |  |
| `transpose` | `integer` | Yes |  |
| `noteMap` | `array<#/$defs/phraseNoteMapping>` | Yes |  |
| `velocityMode` | `enum ["independent", "linked"]` | No/conditional | independent preserves concrete velocities on refresh; linked requires exact presence/value equality with the template. This field does not tri... |
| `noteStateMode` | `enum ["independent", "linked"]` | No/conditional | Controls enabled/releaseVelocity/probability/velocityDeviation after materialization. independent preserves concrete note-state values on refr... |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "templateId": {
      "$ref": "#/$defs/id"
    },
    "clipId": {
      "$ref": "#/$defs/id"
    },
    "repeatCount": {
      "$ref": "#/$defs/positive"
    },
    "transpose": {
      "type": "integer",
      "minimum": -127,
      "maximum": 127
    },
    "noteMap": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/phraseNoteMapping"
      }
    },
    "velocityMode": {
      "enum": [
        "independent",
        "linked"
      ],
      "default": "independent",
      "description": "independent preserves concrete velocities on refresh; linked requires exact presence/value equality with the template. This field does not trigger refresh on load."
    },
    "noteStateMode": {
      "enum": [
        "independent",
        "linked"
      ],
      "default": "independent",
      "description": "Controls enabled/releaseVelocity/probability/velocityDeviation after materialization. independent preserves concrete note-state values on refresh; linked requires exact presence/value equality with the template. pitchRole is structural and must always remain semantically equal between a source pitch note and its mapped concrete note."
    }
  },
  "required": [
    "id",
    "templateId",
    "clipId",
    "repeatCount",
    "transpose",
    "noteMap"
  ],
  "additionalProperties": false
}
```

<a id="def-clipcandidate"></a>
## clipCandidate

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `id` | `#/$defs/id` | Yes |  |
| `clipIds` | `array<#/$defs/id>` | Yes |  |
| `name` | `string` | No/conditional |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "clipIds": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/id"
      },
      "uniqueItems": true
    },
    "name": {
      "type": "string"
    }
  },
  "required": [
    "id",
    "clipIds"
  ],
  "additionalProperties": false
}
```

<a id="def-clipchoicegroup"></a>
## clipChoiceGroup

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `id` | `#/$defs/id` | Yes |  |
| `candidates` | `array<#/$defs/clipCandidate>` | Yes |  |
| `selectedCandidateId` | `anyOf[2]` | Yes |  |
| `name` | `string` | No/conditional |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "candidates": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/clipCandidate"
      },
      "minItems": 1
    },
    "selectedCandidateId": {
      "anyOf": [
        {
          "$ref": "#/$defs/id"
        },
        {
          "type": "null"
        }
      ]
    },
    "name": {
      "type": "string"
    }
  },
  "required": [
    "id",
    "candidates",
    "selectedCandidateId"
  ],
  "additionalProperties": false
}
```

<a id="def-midimapping"></a>
## midiMapping

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `standard` | `enum ["gm1", "custom"]` | Yes | gm1=GM Level 1 percussion key 35..81; custom=explicit arbitrary MIDI1 note number. |
| `note` | `#/$defs/pitch` | Yes | MIDI1 note number in 0..127; for gm1 restrict to 35..81. |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "standard": {
      "enum": [
        "gm1",
        "custom"
      ],
      "description": "gm1=GM Level 1 percussion key 35..81; custom=explicit arbitrary MIDI1 note number."
    },
    "note": {
      "$ref": "#/$defs/pitch",
      "description": "MIDI1 note number in 0..127; for gm1 restrict to 35..81."
    }
  },
  "required": [
    "standard",
    "note"
  ],
  "additionalProperties": false,
  "allOf": [
    {
      "if": {
        "properties": {
          "standard": {
            "const": "gm1"
          }
        },
        "required": [
          "standard"
        ]
      },
      "then": {
        "properties": {
          "note": {
            "type": "integer",
            "minimum": 35,
            "maximum": 81
          }
        }
      }
    }
  ]
}
```

<a id="def-soundsource"></a>
## soundSource

Optional informational rendering class or opaque destination hint. In OSTF 4.0, track.midi.busId is the Core logical MIDI routing reference; soundSource does not bind a physical device, plugin state or preset.

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `kind` | `enum ["unassigned", "gm1", "externalMidi", "plugin", "hostManaged"]` | Yes |  |
| `identifier` | `string` | No/conditional | Opaque informational target identifier (for example a URI or plug-in identifier), not a physical MIDI-port binding or loading command. |

### Exact JSON Schema object

```json
{
  "type": "object",
  "description": "Optional informational rendering class or opaque destination hint. In OSTF 4.0, track.midi.busId is the Core logical MIDI routing reference; soundSource does not bind a physical device, plugin state or preset.",
  "properties": {
    "kind": {
      "enum": [
        "unassigned",
        "gm1",
        "externalMidi",
        "plugin",
        "hostManaged"
      ]
    },
    "identifier": {
      "type": "string",
      "minLength": 1,
      "description": "Opaque informational target identifier (for example a URI or plug-in identifier), not a physical MIDI-port binding or loading command."
    }
  },
  "required": [
    "kind"
  ],
  "additionalProperties": false,
  "allOf": [
    {
      "if": {
        "properties": {
          "kind": {
            "enum": [
              "gm1",
              "unassigned"
            ]
          }
        },
        "required": [
          "kind"
        ]
      },
      "then": {
        "not": {
          "required": [
            "identifier"
          ]
        }
      }
    }
  ]
}
```

<a id="def-localizednames"></a>
## localizedNames

Optional translations indexed by a conservative BCP 47 language-tag subset. The original name/title remains authoritative and is never rewritten by locale changes. Case-insensitive duplicate tags are forbidden semantically.

No direct `properties` table (object may be an enum, scalar, array or a composition).

### Exact JSON Schema object

```json
{
  "type": "object",
  "minProperties": 1,
  "propertyNames": {
    "type": "string",
    "pattern": "^(?:[A-Za-z]{2,3}|[A-Za-z]{5,8})(?:-[A-Za-z0-9]{2,8})*$"
  },
  "additionalProperties": {
    "type": "string",
    "minLength": 1
  },
  "description": "Optional translations indexed by a conservative BCP 47 language-tag subset. The original name/title remains authoritative and is never rewritten by locale changes. Case-insensitive duplicate tags are forbidden semantically."
}
```

<a id="def-drumkit"></a>
## drumKit

Optional named ordered membership of global Sound Slot IDs. Does not define plugin preset, sample loading, choke or a kit-local MIDI remapping.

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `id` | `#/$defs/id` | Yes |  |
| `name` | `string` | Yes |  |
| `localizedNames` | `#/$defs/localizedNames` | No/conditional |  |
| `soundSlotIds` | `array<#/$defs/id>` | Yes | Ordered, unique references to global soundSlots; may be empty. |

### Exact JSON Schema object

```json
{
  "type": "object",
  "description": "Optional named ordered membership of global Sound Slot IDs. Does not define plugin preset, sample loading, choke or a kit-local MIDI remapping.",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "name": {
      "type": "string"
    },
    "localizedNames": {
      "$ref": "#/$defs/localizedNames"
    },
    "soundSlotIds": {
      "type": "array",
      "uniqueItems": true,
      "items": {
        "$ref": "#/$defs/id"
      },
      "description": "Ordered, unique references to global soundSlots; may be empty."
    }
  },
  "required": [
    "id",
    "name",
    "soundSlotIds"
  ],
  "additionalProperties": false
}
```

<a id="def-voicing"></a>
## voicing

Optional informational chord voicing snapshot, not a played Core note collection. Repeated pitches and original array order have meaning for lossless preservation. Per-entry velocity is an optional voicing-preview hint.

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `pitches` | `array<#/$defs/pitch>` | Yes | Ordered multiset of concrete absolute pitches, 0-127. Duplicates allowed. |
| `velocities` | `array<anyOf[2]>` | No/conditional | Optional positional velocities aligned one-to-one to pitches. Null means unspecified at this index, not 0. Exact equal-length rule is semantic. |

### Exact JSON Schema object

```json
{
  "type": "object",
  "additionalProperties": false,
  "description": "Optional informational chord voicing snapshot, not a played Core note collection. Repeated pitches and original array order have meaning for lossless preservation. Per-entry velocity is an optional voicing-preview hint.",
  "properties": {
    "pitches": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/$defs/pitch"
      },
      "description": "Ordered multiset of concrete absolute pitches, 0-127. Duplicates allowed."
    },
    "velocities": {
      "type": "array",
      "minItems": 1,
      "items": {
        "anyOf": [
          {
            "type": "integer",
            "minimum": 1,
            "maximum": 127
          },
          {
            "type": "null"
          }
        ]
      },
      "description": "Optional positional velocities aligned one-to-one to pitches. Null means unspecified at this index, not 0. Exact equal-length rule is semantic."
    }
  },
  "required": [
    "pitches"
  ]
}
```

<a id="def-contributor"></a>
## contributor

One song-local identity; same contributor can receive multiple credit roles. Unicode source name is authoritative.

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `id` | `#/$defs/id` | Yes |  |
| `name` | `string` | Yes |  |
| `kind` | `enum ["person", "organization", "other"]` | No/conditional |  |
| `localizedNames` | `#/$defs/localizedNames` | No/conditional |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "additionalProperties": false,
  "description": "One song-local identity; same contributor can receive multiple credit roles. Unicode source name is authoritative.",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "name": {
      "type": "string",
      "minLength": 1
    },
    "kind": {
      "enum": [
        "person",
        "organization",
        "other"
      ]
    },
    "localizedNames": {
      "$ref": "#/$defs/localizedNames"
    }
  },
  "required": [
    "id",
    "name"
  ]
}
```

<a id="def-credit"></a>
## credit

Ordered credit assignment referencing one contributor; role is an open semantic token, not a translated label.

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `id` | `#/$defs/id` | Yes |  |
| `contributorId` | `#/$defs/id` | Yes |  |
| `role` | `string` | Yes |  |
| `label` | `string` | No/conditional |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "additionalProperties": false,
  "description": "Ordered credit assignment referencing one contributor; role is an open semantic token, not a translated label.",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "contributorId": {
      "$ref": "#/$defs/id"
    },
    "role": {
      "type": "string",
      "pattern": "^[a-z][a-z0-9.-]*$"
    },
    "label": {
      "type": "string"
    }
  },
  "required": [
    "id",
    "contributorId",
    "role"
  ]
}
```

<a id="def-alternatetitle"></a>
## alternateTitle

Stable-ID song title alternative; array position and title text do not identify it.

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `id` | `#/$defs/id` | Yes |  |
| `title` | `string` | Yes |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "additionalProperties": false,
  "description": "Stable-ID song title alternative; array position and title text do not identify it.",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "title": {
      "type": "string",
      "minLength": 1
    }
  },
  "required": [
    "id",
    "title"
  ]
}
```

<a id="def-languagemap32"></a>
## languageMap32

Open BCP 47 language-tag dictionary. Schema checks loose subtag structure; full BCP 47 well-formedness and case-insensitive uniqueness are semantic requirements. String may be empty if intentionally blank.

No direct `properties` table (object may be an enum, scalar, array or a composition).

### Exact JSON Schema object

```json
{
  "type": "object",
  "minProperties": 1,
  "propertyNames": {
    "type": "string",
    "pattern": "^[A-Za-z]{1,8}(?:-[A-Za-z0-9]{1,8})*$"
  },
  "additionalProperties": {
    "type": "string"
  },
  "description": "Open BCP 47 language-tag dictionary. Schema checks loose subtag structure; full BCP 47 well-formedness and case-insensitive uniqueness are semantic requirements. String may be empty if intentionally blank."
}
```

<a id="def-localizationtarget"></a>
## localizationTarget

Core target; song is ID-less, all others use global Core ID. No namespace/profile selector.

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `kind` | `enum ["song", "alternateTitle", "contributor", "credit", "section", "track", "clip", "soundSlot", "drumKit", "lyricDocument", "resource", "phraseTemplate", "clipCandidate", "clipChoiceGroup", "roleDefinition", "genre", "mood", "keyChange", "scale", "midiBus", "lyricVoice"]` | Yes |  |
| `id` | `#/$defs/id` | No/conditional |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "kind": {
      "enum": [
        "song",
        "alternateTitle",
        "contributor",
        "credit",
        "section",
        "track",
        "clip",
        "soundSlot",
        "drumKit",
        "lyricDocument",
        "resource",
        "phraseTemplate",
        "clipCandidate",
        "clipChoiceGroup",
        "roleDefinition",
        "genre",
        "mood",
        "keyChange",
        "scale",
        "midiBus",
        "lyricVoice"
      ]
    },
    "id": {
      "$ref": "#/$defs/id"
    }
  },
  "required": [
    "kind"
  ],
  "allOf": [
    {
      "if": {
        "properties": {
          "kind": {
            "const": "song"
          }
        },
        "required": [
          "kind"
        ]
      },
      "then": {
        "not": {
          "required": [
            "id"
          ]
        }
      },
      "else": {
        "required": [
          "id"
        ]
      }
    }
  ],
  "description": "Core target; song is ID-less, all others use global Core ID. No namespace/profile selector."
}
```

<a id="def-localizationentry"></a>
## localizationEntry

Independent translations for one stable source field. Original source text remains authoritative as fallback.

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `target` | `#/$defs/localizationTarget` | Yes |  |
| `field` | `string` | Yes | Exact allowed source text field for this target kind (see normative matrix). No arbitrary path or musical value fields. |
| `values` | `#/$defs/languageMap32` | Yes |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "target": {
      "$ref": "#/$defs/localizationTarget"
    },
    "field": {
      "type": "string",
      "minLength": 1,
      "description": "Exact allowed source text field for this target kind (see normative matrix). No arbitrary path or musical value fields."
    },
    "values": {
      "$ref": "#/$defs/languageMap32"
    }
  },
  "required": [
    "target",
    "field",
    "values"
  ],
  "description": "Independent translations for one stable source field. Original source text remains authoritative as fallback."
}
```

<a id="def-genre"></a>
## genre

One song-local open genre tag. The label is authored Unicode text and not a predefined controlled taxonomy; ID is stable for metadata merges and localization.

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `id` | `#/$defs/id` | Yes | Stable song-local ID unique among all Core objects. |
| `name` | `string` | Yes | Original Unicode genre label, never normalized or rewritten during import. |
| `externalUri` | `string` | No/conditional | Optional external taxonomy URI hint; never authoritative for a local genre label, and never auto-dereferenced. |

### Exact JSON Schema object

```json
{
  "type": "object",
  "description": "One song-local open genre tag. The label is authored Unicode text and not a predefined controlled taxonomy; ID is stable for metadata merges and localization.",
  "properties": {
    "id": {
      "$ref": "#/$defs/id",
      "description": "Stable song-local ID unique among all Core objects."
    },
    "name": {
      "type": "string",
      "minLength": 1,
      "description": "Original Unicode genre label, never normalized or rewritten during import."
    },
    "externalUri": {
      "type": "string",
      "minLength": 1,
      "format": "uri",
      "description": "Optional external taxonomy URI hint; never authoritative for a local genre label, and never auto-dereferenced."
    }
  },
  "required": [
    "id",
    "name"
  ],
  "additionalProperties": false
}
```

<a id="def-legacy33"></a>
## legacy33

No direct `properties` table (object may be an enum, scalar, array or a composition).

### Exact JSON Schema object

```json
{
  "$defs": {
    "id": {
      "type": "string",
      "pattern": "^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$",
      "not": {
        "pattern": "[\\r\\n\\u2028\\u2029]"
      }
    },
    "nonnegative": {
      "type": "integer",
      "minimum": 0,
      "maximum": 9007199254740991
    },
    "positive": {
      "type": "integer",
      "minimum": 1,
      "maximum": 9007199254740991
    },
    "signed": {
      "type": "integer",
      "minimum": -9007199254740991,
      "maximum": 9007199254740991
    },
    "pitch": {
      "type": "integer",
      "minimum": 0,
      "maximum": 127
    },
    "ref": {
      "type": "object",
      "properties": {
        "type": {
          "enum": [
            "section",
            "track",
            "clip",
            "note",
            "chord",
            "scale",
            "soundSlot",
            "drumKit",
            "lyricDocument",
            "lyricPhrase",
            "lyricUnit",
            "lyricAlignment",
            "resource",
            "genre"
          ]
        },
        "id": {
          "$ref": "#/$defs/legacy33/$defs/id"
        }
      },
      "required": [
        "type",
        "id"
      ],
      "additionalProperties": false
    },
    "range": {
      "type": "object",
      "properties": {
        "start": {
          "$ref": "#/$defs/legacy33/$defs/nonnegative"
        },
        "duration": {
          "$ref": "#/$defs/legacy33/$defs/positive"
        }
      },
      "required": [
        "start",
        "duration"
      ],
      "additionalProperties": false
    },
    "spelledPitchClass": {
      "type": "object",
      "properties": {
        "step": {
          "enum": [
            "A",
            "B",
            "C",
            "D",
            "E",
            "F",
            "G"
          ]
        },
        "alter": {
          "type": "integer",
          "minimum": -2,
          "maximum": 2
        }
      },
      "required": [
        "step",
        "alter"
      ],
      "additionalProperties": false
    },
    "song": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string"
        },
        "primaryMelodyTrackId": {
          "$ref": "#/$defs/legacy33/$defs/id"
        },
        "localizedTitles": {
          "$ref": "#/$defs/legacy33/$defs/localizedNames",
          "description": "Optional localized song-title alternatives. song.title is the stable fallback."
        },
        "subtitle": {
          "type": "string",
          "description": "Optional original-language subtitle."
        },
        "description": {
          "type": "string",
          "description": "Optional original-language description, including Unicode and line breaks."
        },
        "alternateTitles": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/legacy33/$defs/alternateTitle"
          },
          "description": "Additional stable-ID source-language titles."
        },
        "credits": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/legacy33/$defs/credit"
          },
          "description": "Ordered credit assignments to contributors. Multiple roles and duplicate contributors permitted."
        },
        "genres": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/legacy33/$defs/genre"
          },
          "description": "Optional open-ended ordered genre tags; zero or more allowed. Order is authored display preference, first item is primary if a primary label is desired, not a generator weight. Absent means unspecified."
        }
      },
      "required": [
        "title"
      ],
      "additionalProperties": false
    },
    "section": {
      "type": "object",
      "properties": {
        "id": {
          "$ref": "#/$defs/legacy33/$defs/id"
        },
        "name": {
          "type": "string",
          "minLength": 1
        },
        "start": {
          "$ref": "#/$defs/legacy33/$defs/nonnegative"
        },
        "duration": {
          "$ref": "#/$defs/legacy33/$defs/positive"
        },
        "role": {
          "type": "string"
        },
        "localizedNames": {
          "$ref": "#/$defs/legacy33/$defs/localizedNames",
          "description": "Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity."
        }
      },
      "required": [
        "id",
        "name",
        "start",
        "duration"
      ],
      "additionalProperties": false
    },
    "tempo": {
      "type": "object",
      "properties": {
        "at": {
          "$ref": "#/$defs/legacy33/$defs/nonnegative"
        },
        "bpm": {
          "type": "number",
          "exclusiveMinimum": 0,
          "maximum": 1000
        }
      },
      "required": [
        "at",
        "bpm"
      ],
      "additionalProperties": false
    },
    "meter": {
      "type": "object",
      "properties": {
        "at": {
          "$ref": "#/$defs/legacy33/$defs/nonnegative"
        },
        "numerator": {
          "type": "integer",
          "minimum": 1,
          "maximum": 64
        },
        "denominator": {
          "enum": [
            1,
            2,
            4,
            8,
            16,
            32,
            64
          ],
          "type": "integer"
        }
      },
      "required": [
        "at",
        "numerator",
        "denominator"
      ],
      "additionalProperties": false
    },
    "timeline": {
      "type": "object",
      "properties": {
        "sections": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/legacy33/$defs/section"
          }
        },
        "tempoChanges": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/legacy33/$defs/tempo"
          },
          "minItems": 1
        },
        "meterChanges": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/legacy33/$defs/meter"
          },
          "minItems": 1
        }
      },
      "required": [
        "sections",
        "tempoChanges",
        "meterChanges"
      ],
      "additionalProperties": false
    },
    "chord": {
      "type": "object",
      "properties": {
        "id": {
          "$ref": "#/$defs/legacy33/$defs/id"
        },
        "start": {
          "$ref": "#/$defs/legacy33/$defs/nonnegative"
        },
        "duration": {
          "$ref": "#/$defs/legacy33/$defs/positive"
        },
        "label": {
          "type": "string",
          "minLength": 1
        },
        "root": {
          "$ref": "#/$defs/legacy33/$defs/spelledPitchClass"
        },
        "intervals": {
          "type": "array",
          "items": {
            "type": "integer",
            "minimum": 0,
            "maximum": 35
          },
          "minItems": 1,
          "maxItems": 36,
          "uniqueItems": true,
          "contains": {
            "const": 0
          }
        },
        "bass": {
          "$ref": "#/$defs/legacy33/$defs/spelledPitchClass"
        },
        "voicing": {
          "$ref": "#/$defs/legacy33/$defs/voicing",
          "description": "Optional pitch snapshot (not an arrangement note sequence). No automatic playback."
        }
      },
      "required": [
        "id",
        "start",
        "duration",
        "label"
      ],
      "additionalProperties": false,
      "dependentRequired": {
        "root": [
          "intervals"
        ],
        "intervals": [
          "root"
        ]
      }
    },
    "scale": {
      "type": "object",
      "properties": {
        "id": {
          "$ref": "#/$defs/legacy33/$defs/id"
        },
        "start": {
          "$ref": "#/$defs/legacy33/$defs/nonnegative"
        },
        "duration": {
          "$ref": "#/$defs/legacy33/$defs/positive"
        },
        "label": {
          "type": "string"
        },
        "tonic": {
          "$ref": "#/$defs/legacy33/$defs/spelledPitchClass"
        },
        "intervals": {
          "type": "array",
          "items": {
            "type": "integer",
            "minimum": 0,
            "maximum": 11
          },
          "minItems": 1,
          "maxItems": 12,
          "uniqueItems": true,
          "contains": {
            "const": 0
          }
        }
      },
      "required": [
        "id",
        "start",
        "duration",
        "tonic",
        "intervals"
      ],
      "additionalProperties": false
    },
    "harmony": {
      "type": "object",
      "properties": {
        "chords": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/legacy33/$defs/chord"
          }
        },
        "scales": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/legacy33/$defs/scale"
          }
        }
      },
      "required": [
        "chords",
        "scales"
      ],
      "additionalProperties": false
    },
    "instrument": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "family": {
          "type": "string"
        },
        "localizedNames": {
          "$ref": "#/$defs/legacy33/$defs/localizedNames",
          "description": "Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity."
        }
      },
      "required": [
        "name"
      ],
      "additionalProperties": false
    },
    "note": {
      "type": "object",
      "properties": {
        "id": {
          "$ref": "#/$defs/legacy33/$defs/id"
        },
        "start": {
          "$ref": "#/$defs/legacy33/$defs/signed"
        },
        "duration": {
          "$ref": "#/$defs/legacy33/$defs/positive",
          "description": "Positive note gate in ticks, not the guaranteed audible duration of a one-shot percussion sample."
        },
        "pitch": {
          "$ref": "#/$defs/legacy33/$defs/pitch"
        },
        "soundSlotId": {
          "$ref": "#/$defs/legacy33/$defs/id",
          "description": "Document-local Sound Slot ID. Distinct events and IDs stay distinct even if several slots share a MIDI key; a renderer decides the acoustic timbre."
        },
        "velocity": {
          "type": "integer",
          "minimum": 1,
          "maximum": 127,
          "description": "Optional authored note-on velocity for performed Core notes, 1–127; omit to mean unspecified. It is not a note-off velocity, controller stream, chord tone, or a sound-rendering guarantee. Never insert an inferred default when saving."
        }
      },
      "required": [
        "id",
        "start",
        "duration"
      ],
      "additionalProperties": false,
      "oneOf": [
        {
          "required": [
            "pitch"
          ],
          "not": {
            "required": [
              "soundSlotId"
            ]
          }
        },
        {
          "required": [
            "soundSlotId"
          ],
          "not": {
            "required": [
              "pitch"
            ]
          }
        }
      ],
      "description": "Concrete Core note; optional velocity is a note-on attribute. Phrase templates use a separate version-frozen sourceNote shape."
    },
    "clip": {
      "type": "object",
      "properties": {
        "id": {
          "$ref": "#/$defs/legacy33/$defs/id"
        },
        "name": {
          "type": "string"
        },
        "start": {
          "$ref": "#/$defs/legacy33/$defs/nonnegative"
        },
        "duration": {
          "$ref": "#/$defs/legacy33/$defs/positive"
        },
        "enabled": {
          "type": "boolean",
          "default": true
        },
        "notes": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/legacy33/$defs/note"
          }
        },
        "localizedNames": {
          "$ref": "#/$defs/legacy33/$defs/localizedNames",
          "description": "Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity."
        }
      },
      "required": [
        "id",
        "start",
        "duration",
        "notes"
      ],
      "additionalProperties": false
    },
    "track": {
      "type": "object",
      "properties": {
        "id": {
          "$ref": "#/$defs/legacy33/$defs/id"
        },
        "name": {
          "type": "string"
        },
        "role": {
          "type": "string"
        },
        "instrument": {
          "$ref": "#/$defs/legacy33/$defs/instrument"
        },
        "enabled": {
          "type": "boolean",
          "default": true
        },
        "clips": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/legacy33/$defs/clip"
          }
        },
        "trackType": {
          "enum": [
            "melodic",
            "drum",
            "mixed"
          ],
          "description": "Semantic event-target category; optional; missing/empty-note tracks may be unknown. It is not a DAW track class."
        },
        "preferredView": {
          "enum": [
            "auto",
            "pianoRoll",
            "drumGrid"
          ],
          "default": "auto",
          "description": "Non-binding presentation preference. Does not change note meaning."
        },
        "soundSource": {
          "$ref": "#/$defs/legacy33/$defs/soundSource",
          "description": "Optional sound-source selection hint, not a plug-in state, preset blob, or sound guarantee."
        },
        "localizedNames": {
          "$ref": "#/$defs/legacy33/$defs/localizedNames",
          "description": "Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity."
        },
        "drumKitId": {
          "$ref": "#/$defs/legacy33/$defs/id",
          "description": "Optional reference to a declared drumKit; only for a drum/mixed or empty inferred track. All stored slot events in the track must belong to the referenced kit."
        }
      },
      "required": [
        "id",
        "name",
        "clips"
      ],
      "additionalProperties": false,
      "allOf": [
        {
          "if": {
            "properties": {
              "trackType": {
                "const": "melodic"
              }
            },
            "required": [
              "trackType"
            ]
          },
          "then": {
            "not": {
              "required": [
                "drumKitId"
              ]
            }
          }
        }
      ]
    },
    "soundSlot": {
      "type": "object",
      "properties": {
        "id": {
          "$ref": "#/$defs/legacy33/$defs/id"
        },
        "name": {
          "type": "string"
        },
        "role": {
          "type": "string",
          "description": "Optional free-text musical role; not a standardized GM instrument code or an acoustic sample identifier."
        },
        "midiNote": {
          "$ref": "#/$defs/legacy33/$defs/pitch",
          "description": "Legacy 3.0 MIDI note hint only; not a GM1 declaration or preview timbre identity."
        },
        "midiMapping": {
          "$ref": "#/$defs/legacy33/$defs/midiMapping",
          "description": "Explicit external MIDI1 output mapping; standard=gm1 is separate from custom even for an equal note number. Not a unique slot or audio identity."
        },
        "localizedNames": {
          "$ref": "#/$defs/legacy33/$defs/localizedNames",
          "description": "Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity."
        }
      },
      "required": [
        "id",
        "name"
      ],
      "additionalProperties": false,
      "description": "Document-local stable logical percussion target. Equal roles, names or MIDI note mappings never merge distinct slot IDs. No sample/audio identity is encoded."
    },
    "lyricDocument": {
      "type": "object",
      "properties": {
        "id": {
          "$ref": "#/$defs/legacy33/$defs/id"
        },
        "title": {
          "type": "string"
        },
        "language": {
          "type": "string"
        }
      },
      "required": [
        "id"
      ],
      "additionalProperties": false
    },
    "lyricPhrase": {
      "type": "object",
      "properties": {
        "id": {
          "$ref": "#/$defs/legacy33/$defs/id"
        },
        "documentId": {
          "$ref": "#/$defs/legacy33/$defs/id"
        },
        "text": {
          "type": "string"
        },
        "pronunciation": {
          "type": "string"
        },
        "start": {
          "$ref": "#/$defs/legacy33/$defs/nonnegative"
        },
        "duration": {
          "$ref": "#/$defs/legacy33/$defs/positive"
        }
      },
      "required": [
        "id",
        "documentId",
        "text"
      ],
      "additionalProperties": false,
      "dependentRequired": {
        "start": [
          "duration"
        ],
        "duration": [
          "start"
        ]
      }
    },
    "lyricUnit": {
      "type": "object",
      "properties": {
        "id": {
          "$ref": "#/$defs/legacy33/$defs/id"
        },
        "phraseId": {
          "$ref": "#/$defs/legacy33/$defs/id"
        },
        "text": {
          "type": "string"
        },
        "pronunciation": {
          "type": "string"
        },
        "start": {
          "$ref": "#/$defs/legacy33/$defs/nonnegative"
        },
        "duration": {
          "$ref": "#/$defs/legacy33/$defs/positive"
        }
      },
      "required": [
        "id",
        "phraseId",
        "text"
      ],
      "additionalProperties": false,
      "dependentRequired": {
        "start": [
          "duration"
        ],
        "duration": [
          "start"
        ]
      }
    },
    "lyricAlignment": {
      "type": "object",
      "properties": {
        "id": {
          "$ref": "#/$defs/legacy33/$defs/id"
        },
        "unitIds": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/legacy33/$defs/id"
          },
          "uniqueItems": true,
          "minItems": 1
        },
        "noteIds": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/legacy33/$defs/id"
          },
          "uniqueItems": true,
          "minItems": 1
        }
      },
      "required": [
        "id",
        "unitIds",
        "noteIds"
      ],
      "additionalProperties": false
    },
    "lyrics": {
      "type": "object",
      "properties": {
        "documents": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/legacy33/$defs/lyricDocument"
          }
        },
        "phrases": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/legacy33/$defs/lyricPhrase"
          }
        },
        "units": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/legacy33/$defs/lyricUnit"
          }
        },
        "alignments": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/legacy33/$defs/lyricAlignment"
          }
        }
      },
      "required": [
        "documents",
        "phrases",
        "units",
        "alignments"
      ],
      "additionalProperties": false
    },
    "sha256": {
      "type": "string",
      "pattern": "^[0-9a-f]{64}$",
      "not": {
        "pattern": "[\\r\\n\\u2028\\u2029]"
      }
    },
    "resource": {
      "type": "object",
      "properties": {
        "id": {
          "$ref": "#/$defs/legacy33/$defs/id"
        },
        "kind": {
          "enum": [
            "audio",
            "midi",
            "text",
            "other"
          ]
        },
        "uri": {
          "type": "string",
          "minLength": 1
        },
        "name": {
          "type": "string"
        },
        "sha256": {
          "$ref": "#/$defs/legacy33/$defs/sha256"
        }
      },
      "required": [
        "id",
        "kind",
        "uri"
      ],
      "additionalProperties": false
    },
    "dependencies": {
      "oneOf": [
        {
          "type": "object",
          "properties": {
            "scope": {
              "enum": [
                "document",
                "none"
              ]
            }
          },
          "required": [
            "scope"
          ],
          "additionalProperties": false
        },
        {
          "type": "object",
          "properties": {
            "scope": {
              "const": "objects"
            },
            "refs": {
              "type": "array",
              "items": {
                "$ref": "#/$defs/legacy33/$defs/ref"
              },
              "minItems": 1,
              "uniqueItems": true
            }
          },
          "required": [
            "scope",
            "refs"
          ],
          "additionalProperties": false
        }
      ]
    },
    "extension": {
      "type": "object",
      "properties": {
        "version": {
          "type": "string",
          "minLength": 1
        },
        "status": {
          "enum": [
            "current",
            "stale",
            "unverified"
          ]
        },
        "dependencies": {
          "$ref": "#/$defs/legacy33/$defs/dependencies"
        },
        "data": {}
      },
      "required": [
        "version",
        "status",
        "dependencies",
        "data"
      ],
      "additionalProperties": false
    },
    "relativeAssignment": {
      "type": "object",
      "properties": {
        "noteId": {
          "$ref": "#/$defs/legacy33/$defs/id"
        },
        "basis": {
          "enum": [
            "chordTone",
            "scaleDegree"
          ]
        },
        "contextId": {
          "$ref": "#/$defs/legacy33/$defs/id"
        },
        "anchorPitch": {
          "$ref": "#/$defs/legacy33/$defs/pitch"
        },
        "index": {
          "type": "integer",
          "minimum": 1,
          "maximum": 36
        },
        "chromaticOffset": {
          "type": "integer",
          "minimum": -24,
          "maximum": 24
        }
      },
      "required": [
        "noteId",
        "basis",
        "contextId",
        "anchorPitch",
        "index",
        "chromaticOffset"
      ],
      "additionalProperties": false,
      "allOf": [
        {
          "if": {
            "properties": {
              "basis": {
                "const": "scaleDegree"
              }
            },
            "required": [
              "basis"
            ]
          },
          "then": {
            "properties": {
              "index": {
                "maximum": 12
              }
            }
          }
        }
      ]
    },
    "relativeData": {
      "type": "object",
      "properties": {
        "assignments": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/legacy33/$defs/relativeAssignment"
          }
        }
      },
      "required": [
        "assignments"
      ],
      "additionalProperties": false
    },
    "generator": {
      "type": "object",
      "properties": {
        "id": {
          "type": "string",
          "minLength": 1
        },
        "version": {
          "type": "string",
          "minLength": 1
        }
      },
      "required": [
        "id",
        "version"
      ],
      "additionalProperties": false
    },
    "generationInput": {
      "type": "object",
      "properties": {
        "role": {
          "type": "string",
          "minLength": 1
        },
        "ref": {
          "$ref": "#/$defs/legacy33/$defs/ref"
        },
        "readRange": {
          "$ref": "#/$defs/legacy33/$defs/range"
        }
      },
      "required": [
        "role",
        "ref"
      ],
      "additionalProperties": false
    },
    "generationProcess": {
      "type": "object",
      "properties": {
        "id": {
          "$ref": "#/$defs/legacy33/$defs/id"
        },
        "generator": {
          "$ref": "#/$defs/legacy33/$defs/generator"
        },
        "inputs": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/legacy33/$defs/generationInput"
          }
        },
        "outputs": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/legacy33/$defs/ref"
          },
          "minItems": 1
        },
        "targetRange": {
          "$ref": "#/$defs/legacy33/$defs/range"
        },
        "protectedNoteIds": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/legacy33/$defs/id"
          },
          "uniqueItems": true
        },
        "vendorExtension": {
          "type": "string",
          "minLength": 1
        }
      },
      "required": [
        "id",
        "generator",
        "inputs",
        "outputs",
        "protectedNoteIds"
      ],
      "additionalProperties": false
    },
    "generationData": {
      "type": "object",
      "properties": {
        "processes": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/legacy33/$defs/generationProcess"
          }
        }
      },
      "required": [
        "processes"
      ],
      "additionalProperties": false
    },
    "color": {
      "type": "string",
      "pattern": "^#[0-9A-Fa-f]{6}$",
      "not": {
        "pattern": "[\\r\\n\\u2028\\u2029]"
      }
    },
    "roleDefinition": {
      "type": "object",
      "properties": {
        "id": {
          "$ref": "#/$defs/legacy33/$defs/id"
        },
        "name": {
          "type": "string",
          "minLength": 1
        },
        "baseRole": {
          "type": "string"
        }
      },
      "required": [
        "id",
        "name"
      ],
      "additionalProperties": false
    },
    "roleColorMap": {
      "type": "object",
      "additionalProperties": {
        "$ref": "#/$defs/legacy33/$defs/color"
      }
    },
    "customRoleColorMap": {
      "type": "object",
      "propertyNames": {
        "$ref": "#/$defs/legacy33/$defs/id"
      },
      "additionalProperties": {
        "$ref": "#/$defs/legacy33/$defs/color"
      }
    },
    "objectColor": {
      "type": "object",
      "properties": {
        "target": {
          "$ref": "#/$defs/legacy33/$defs/ref"
        },
        "color": {
          "$ref": "#/$defs/legacy33/$defs/color"
        }
      },
      "required": [
        "target",
        "color"
      ],
      "additionalProperties": false
    },
    "appearanceData": {
      "type": "object",
      "properties": {
        "roleDefinitions": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/legacy33/$defs/roleDefinition"
          }
        },
        "sectionRoleAssignments": {
          "type": "object",
          "propertyNames": {
            "$ref": "#/$defs/legacy33/$defs/id"
          },
          "additionalProperties": {
            "$ref": "#/$defs/legacy33/$defs/id"
          }
        },
        "appearance": {
          "type": "object",
          "properties": {
            "roleColors": {
              "$ref": "#/$defs/legacy33/$defs/roleColorMap"
            },
            "customRoleColors": {
              "$ref": "#/$defs/legacy33/$defs/customRoleColorMap"
            },
            "objectColors": {
              "type": "array",
              "items": {
                "$ref": "#/$defs/legacy33/$defs/objectColor"
              }
            }
          },
          "required": [
            "roleColors",
            "customRoleColors",
            "objectColors"
          ],
          "additionalProperties": false
        }
      },
      "required": [
        "roleDefinitions",
        "sectionRoleAssignments",
        "appearance"
      ],
      "additionalProperties": false
    },
    "legacyData": {
      "type": "object",
      "properties": {
        "sourceVersion": {
          "const": "2.3.0"
        },
        "sourceSha256": {
          "$ref": "#/$defs/legacy33/$defs/sha256"
        },
        "sourceText": {
          "type": "string",
          "minLength": 1
        },
        "conversionReport": {
          "type": "object"
        }
      },
      "required": [
        "sourceVersion",
        "sourceSha256",
        "sourceText",
        "conversionReport"
      ],
      "additionalProperties": false
    },
    "extensions": {
      "type": "object",
      "propertyNames": {
        "pattern": "^[a-z][a-z0-9-]*(?:\\.[a-z][a-z0-9-]*){2,}$",
        "not": {
          "pattern": "[\\r\\n\\u2028\\u2029]"
        }
      },
      "properties": {
        "org.ostf.relative-phrase.v1": {
          "allOf": [
            {
              "$ref": "#/$defs/legacy33/$defs/extension"
            },
            {
              "if": {
                "properties": {
                  "version": {
                    "const": "1.0.0-draft.1"
                  }
                },
                "required": [
                  "version"
                ]
              },
              "then": {
                "properties": {
                  "data": {
                    "$ref": "#/$defs/legacy33/$defs/relativeData"
                  }
                }
              }
            }
          ]
        },
        "org.ostf.generation-context.v1": {
          "allOf": [
            {
              "$ref": "#/$defs/legacy33/$defs/extension"
            },
            {
              "if": {
                "properties": {
                  "version": {
                    "const": "1.0.0-draft.1"
                  }
                },
                "required": [
                  "version"
                ]
              },
              "then": {
                "properties": {
                  "data": {
                    "$ref": "#/$defs/legacy33/$defs/generationData"
                  }
                }
              }
            }
          ]
        },
        "org.ostf.appearance.v1": {
          "allOf": [
            {
              "$ref": "#/$defs/legacy33/$defs/extension"
            },
            {
              "if": {
                "properties": {
                  "version": {
                    "const": "1.0.0-draft.1"
                  }
                },
                "required": [
                  "version"
                ]
              },
              "then": {
                "properties": {
                  "data": {
                    "$ref": "#/$defs/legacy33/$defs/appearanceData"
                  }
                }
              }
            }
          ]
        },
        "org.ostf.legacy-import.v1": {
          "allOf": [
            {
              "$ref": "#/$defs/legacy33/$defs/extension"
            },
            {
              "if": {
                "properties": {
                  "version": {
                    "const": "1.0.0-draft.1"
                  }
                },
                "required": [
                  "version"
                ]
              },
              "then": {
                "properties": {
                  "data": {
                    "$ref": "#/$defs/legacy33/$defs/legacyData"
                  }
                }
              }
            }
          ]
        },
        "org.ostf.phrase-library.v1": {
          "allOf": [
            {
              "$ref": "#/$defs/legacy33/$defs/extension"
            },
            {
              "if": {
                "properties": {
                  "version": {
                    "const": "1.0.0-draft.1"
                  }
                },
                "required": [
                  "version"
                ]
              },
              "then": {
                "properties": {
                  "data": {
                    "$ref": "#/$defs/legacy33/$defs/phraseLibraryData"
                  }
                }
              }
            }
          ]
        },
        "org.ostf.clip-choices.v1": {
          "allOf": [
            {
              "$ref": "#/$defs/legacy33/$defs/extension"
            },
            {
              "if": {
                "properties": {
                  "version": {
                    "const": "1.0.0-draft.1"
                  }
                },
                "required": [
                  "version"
                ]
              },
              "then": {
                "properties": {
                  "data": {
                    "$ref": "#/$defs/legacy33/$defs/clipChoicesData"
                  }
                }
              }
            }
          ]
        },
        "org.ostf.localization.v1": {
          "allOf": [
            {
              "$ref": "#/$defs/legacy33/$defs/extension"
            },
            {
              "if": {
                "properties": {
                  "version": {
                    "const": "1.0.0"
                  }
                },
                "required": [
                  "version"
                ]
              },
              "then": {
                "properties": {
                  "data": {
                    "$ref": "#/$defs/legacy33/$defs/localizationData"
                  }
                }
              }
            }
          ]
        }
      },
      "additionalProperties": {
        "$ref": "#/$defs/legacy33/$defs/extension"
      }
    },
    "phraseTemplate": {
      "type": "object",
      "properties": {
        "id": {
          "$ref": "#/$defs/legacy33/$defs/id"
        },
        "duration": {
          "$ref": "#/$defs/legacy33/$defs/positive"
        },
        "notes": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/legacy33/$defs/phraseSourceNote"
          }
        },
        "name": {
          "type": "string"
        }
      },
      "required": [
        "id",
        "duration",
        "notes"
      ],
      "additionalProperties": false
    },
    "phraseNoteMapping": {
      "type": "object",
      "properties": {
        "templateNoteId": {
          "$ref": "#/$defs/legacy33/$defs/id"
        },
        "repeatIndex": {
          "$ref": "#/$defs/legacy33/$defs/nonnegative"
        },
        "noteId": {
          "$ref": "#/$defs/legacy33/$defs/id"
        }
      },
      "required": [
        "templateNoteId",
        "repeatIndex",
        "noteId"
      ],
      "additionalProperties": false
    },
    "phraseInstance": {
      "type": "object",
      "properties": {
        "id": {
          "$ref": "#/$defs/legacy33/$defs/id"
        },
        "templateId": {
          "$ref": "#/$defs/legacy33/$defs/id"
        },
        "clipId": {
          "$ref": "#/$defs/legacy33/$defs/id"
        },
        "repeatCount": {
          "$ref": "#/$defs/legacy33/$defs/positive"
        },
        "transpose": {
          "type": "integer",
          "minimum": -127,
          "maximum": 127
        },
        "noteMap": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/legacy33/$defs/phraseNoteMapping"
          }
        }
      },
      "required": [
        "id",
        "templateId",
        "clipId",
        "repeatCount",
        "transpose",
        "noteMap"
      ],
      "additionalProperties": false
    },
    "phraseLibraryData": {
      "type": "object",
      "properties": {
        "templates": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/legacy33/$defs/phraseTemplate"
          }
        },
        "instances": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/legacy33/$defs/phraseInstance"
          }
        }
      },
      "required": [
        "templates",
        "instances"
      ],
      "additionalProperties": false
    },
    "clipCandidate": {
      "type": "object",
      "properties": {
        "id": {
          "$ref": "#/$defs/legacy33/$defs/id"
        },
        "clipIds": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/legacy33/$defs/id"
          },
          "uniqueItems": true
        },
        "name": {
          "type": "string"
        }
      },
      "required": [
        "id",
        "clipIds"
      ],
      "additionalProperties": false
    },
    "clipChoiceGroup": {
      "type": "object",
      "properties": {
        "id": {
          "$ref": "#/$defs/legacy33/$defs/id"
        },
        "candidates": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/legacy33/$defs/clipCandidate"
          },
          "minItems": 1
        },
        "selectedCandidateId": {
          "anyOf": [
            {
              "$ref": "#/$defs/legacy33/$defs/id"
            },
            {
              "type": "null"
            }
          ]
        },
        "name": {
          "type": "string"
        }
      },
      "required": [
        "id",
        "candidates",
        "selectedCandidateId"
      ],
      "additionalProperties": false
    },
    "clipChoicesData": {
      "type": "object",
      "properties": {
        "groups": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/legacy33/$defs/clipChoiceGroup"
          }
        }
      },
      "required": [
        "groups"
      ],
      "additionalProperties": false
    },
    "midiMapping": {
      "type": "object",
      "properties": {
        "standard": {
          "enum": [
            "gm1",
            "custom"
          ],
          "description": "gm1=GM Level 1 percussion key 35..81; custom=explicit arbitrary MIDI1 note number."
        },
        "note": {
          "$ref": "#/$defs/legacy33/$defs/pitch",
          "description": "MIDI1 note number in 0..127; for gm1 restrict to 35..81."
        }
      },
      "required": [
        "standard",
        "note"
      ],
      "additionalProperties": false,
      "allOf": [
        {
          "if": {
            "properties": {
              "standard": {
                "const": "gm1"
              }
            },
            "required": [
              "standard"
            ]
          },
          "then": {
            "properties": {
              "note": {
                "type": "integer",
                "minimum": 35,
                "maximum": 81
              }
            }
          }
        }
      ]
    },
    "soundSource": {
      "type": "object",
      "description": "Optional informational rendering class or opaque destination hint. Program Change, Bank Select and plugin presets are not standardized by Core.",
      "properties": {
        "kind": {
          "enum": [
            "unassigned",
            "gm1",
            "externalMidi",
            "plugin",
            "hostManaged"
          ]
        },
        "identifier": {
          "type": "string",
          "minLength": 1,
          "description": "Opaque target identifier, e.g. URI, plug-in identifier or port alias, not a loading command."
        }
      },
      "required": [
        "kind"
      ],
      "additionalProperties": false,
      "allOf": [
        {
          "if": {
            "properties": {
              "kind": {
                "enum": [
                  "gm1",
                  "unassigned"
                ]
              }
            },
            "required": [
              "kind"
            ]
          },
          "then": {
            "not": {
              "required": [
                "identifier"
              ]
            }
          }
        }
      ]
    },
    "localizedNames": {
      "type": "object",
      "minProperties": 1,
      "propertyNames": {
        "type": "string",
        "pattern": "^(?:[A-Za-z]{2,3}|[A-Za-z]{5,8})(?:-[A-Za-z0-9]{2,8})*$"
      },
      "additionalProperties": {
        "type": "string",
        "minLength": 1
      },
      "description": "Optional translations indexed by a conservative BCP 47 language-tag subset. The original name/title remains authoritative and is never rewritten by locale changes. Case-insensitive duplicate tags are forbidden semantically."
    },
    "drumKit": {
      "type": "object",
      "description": "Optional named ordered membership of global Sound Slot IDs. Does not define plugin preset, sample loading, choke or a kit-local MIDI remapping.",
      "properties": {
        "id": {
          "$ref": "#/$defs/legacy33/$defs/id"
        },
        "name": {
          "type": "string"
        },
        "localizedNames": {
          "$ref": "#/$defs/legacy33/$defs/localizedNames"
        },
        "soundSlotIds": {
          "type": "array",
          "uniqueItems": true,
          "items": {
            "$ref": "#/$defs/legacy33/$defs/id"
          },
          "description": "Ordered, unique references to global soundSlots; may be empty."
        }
      },
      "required": [
        "id",
        "name",
        "soundSlotIds"
      ],
      "additionalProperties": false
    },
    "phraseSourceNote": {
      "type": "object",
      "properties": {
        "id": {
          "$ref": "#/$defs/legacy33/$defs/id"
        },
        "start": {
          "$ref": "#/$defs/legacy33/$defs/signed"
        },
        "duration": {
          "$ref": "#/$defs/legacy33/$defs/positive"
        },
        "pitch": {
          "$ref": "#/$defs/legacy33/$defs/pitch"
        },
        "soundSlotId": {
          "$ref": "#/$defs/legacy33/$defs/id"
        }
      },
      "required": [
        "id",
        "start",
        "duration"
      ],
      "additionalProperties": false,
      "oneOf": [
        {
          "required": [
            "pitch"
          ],
          "not": {
            "required": [
              "soundSlotId"
            ]
          }
        },
        {
          "required": [
            "soundSlotId"
          ],
          "not": {
            "required": [
              "pitch"
            ]
          }
        }
      ],
      "description": "Version-frozen 1.0.0-draft.1 phrase source note. Does NOT admit velocity; a linked Core instance may independently set velocity."
    },
    "voicing": {
      "type": "object",
      "additionalProperties": false,
      "description": "Optional informational chord voicing snapshot, not a played Core note collection. Repeated pitches and original array order have meaning for lossless preservation. Per-entry velocity is an optional voicing-preview hint.",
      "properties": {
        "pitches": {
          "type": "array",
          "minItems": 1,
          "items": {
            "$ref": "#/$defs/legacy33/$defs/pitch"
          },
          "description": "Ordered multiset of concrete absolute pitches, 0-127. Duplicates allowed."
        },
        "velocities": {
          "type": "array",
          "minItems": 1,
          "items": {
            "anyOf": [
              {
                "type": "integer",
                "minimum": 1,
                "maximum": 127
              },
              {
                "type": "null"
              }
            ]
          },
          "description": "Optional positional velocities aligned one-to-one to pitches. Null means unspecified at this index, not 0. Exact equal-length rule is semantic."
        }
      },
      "required": [
        "pitches"
      ]
    },
    "contributor": {
      "type": "object",
      "additionalProperties": false,
      "description": "One song-local identity; same contributor can receive multiple credit roles. Unicode source name is authoritative.",
      "properties": {
        "id": {
          "$ref": "#/$defs/legacy33/$defs/id"
        },
        "name": {
          "type": "string",
          "minLength": 1
        },
        "kind": {
          "enum": [
            "person",
            "organization",
            "other"
          ]
        },
        "localizedNames": {
          "$ref": "#/$defs/legacy33/$defs/localizedNames"
        }
      },
      "required": [
        "id",
        "name"
      ]
    },
    "credit": {
      "type": "object",
      "additionalProperties": false,
      "description": "Ordered credit assignment referencing one contributor; role is an open semantic token, not a translated label.",
      "properties": {
        "id": {
          "$ref": "#/$defs/legacy33/$defs/id"
        },
        "contributorId": {
          "$ref": "#/$defs/legacy33/$defs/id"
        },
        "role": {
          "type": "string",
          "pattern": "^[a-z][a-z0-9.-]*$"
        },
        "label": {
          "type": "string"
        }
      },
      "required": [
        "id",
        "contributorId",
        "role"
      ]
    },
    "alternateTitle": {
      "type": "object",
      "additionalProperties": false,
      "description": "Stable-ID song title alternative; array position and title text do not identify it.",
      "properties": {
        "id": {
          "$ref": "#/$defs/legacy33/$defs/id"
        },
        "title": {
          "type": "string",
          "minLength": 1
        }
      },
      "required": [
        "id",
        "title"
      ]
    },
    "languageMap32": {
      "type": "object",
      "minProperties": 1,
      "propertyNames": {
        "type": "string",
        "pattern": "^[A-Za-z]{1,8}(?:-[A-Za-z0-9]{1,8})*$"
      },
      "additionalProperties": {
        "type": "string"
      },
      "description": "Open BCP 47 language-tag dictionary. Schema checks loose subtag structure; full BCP 47 well-formedness and case-insensitive uniqueness are semantic requirements. String may be empty if intentionally blank."
    },
    "localizationTarget": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "kind": {
          "enum": [
            "song",
            "alternateTitle",
            "contributor",
            "credit",
            "section",
            "track",
            "clip",
            "soundSlot",
            "drumKit",
            "lyricDocument",
            "resource",
            "phraseTemplate",
            "clipCandidate",
            "clipChoiceGroup",
            "roleDefinition",
            "genre"
          ]
        },
        "id": {
          "$ref": "#/$defs/legacy33/$defs/id"
        },
        "profile": {
          "type": "string",
          "enum": [
            "org.ostf.phrase-library.v1",
            "org.ostf.clip-choices.v1",
            "org.ostf.appearance.v1"
          ]
        }
      },
      "required": [
        "kind"
      ],
      "allOf": [
        {
          "if": {
            "properties": {
              "kind": {
                "const": "song"
              }
            },
            "required": [
              "kind"
            ]
          },
          "then": {
            "not": {
              "anyOf": [
                {
                  "required": [
                    "id"
                  ]
                },
                {
                  "required": [
                    "profile"
                  ]
                }
              ]
            }
          },
          "else": {
            "required": [
              "id"
            ]
          }
        },
        {
          "if": {
            "properties": {
              "kind": {
                "enum": [
                  "phraseTemplate",
                  "clipCandidate",
                  "clipChoiceGroup",
                  "roleDefinition"
                ]
              }
            },
            "required": [
              "kind"
            ]
          },
          "then": {
            "required": [
              "profile"
            ]
          },
          "else": {
            "not": {
              "required": [
                "profile"
              ]
            }
          }
        }
      ],
      "description": "Stable target by Core ID or profile-local scoped ID; song is the only ID-less target. No array indexes or mutable names as locators."
    },
    "localizationEntry": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "target": {
          "$ref": "#/$defs/legacy33/$defs/localizationTarget"
        },
        "field": {
          "type": "string",
          "minLength": 1,
          "description": "Exact allowed source text field for this target kind (see normative matrix). No arbitrary path or musical value fields."
        },
        "values": {
          "$ref": "#/$defs/legacy33/$defs/languageMap32"
        }
      },
      "required": [
        "target",
        "field",
        "values"
      ],
      "description": "Independent translations for one stable source field. Original source text remains authoritative as fallback."
    },
    "localizationData": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "entries": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/legacy33/$defs/localizationEntry"
          }
        }
      },
      "required": [
        "entries"
      ],
      "description": "Language-map translations indexed by stable kind/id/field, never by names or array positions."
    },
    "genre": {
      "type": "object",
      "description": "One song-local open genre tag. The label is authored Unicode text and not a predefined controlled taxonomy; ID is stable for metadata merges and localization.",
      "properties": {
        "id": {
          "$ref": "#/$defs/legacy33/$defs/id",
          "description": "Stable song-local ID unique among all Core objects."
        },
        "name": {
          "type": "string",
          "minLength": 1,
          "description": "Original Unicode genre label, never normalized or rewritten during import."
        },
        "externalUri": {
          "type": "string",
          "minLength": 1,
          "format": "uri",
          "description": "Optional external taxonomy URI hint; never authoritative for a local genre label, and never auto-dereferenced."
        }
      },
      "required": [
        "id",
        "name"
      ],
      "additionalProperties": false
    }
  }
}
```

<a id="def-opaquedocumentid"></a>
## opaqueDocumentId

Stable URI or UUID-style identifier for a document lineage. Compared as exact Unicode text; never fetched.

No direct `properties` table (object may be an enum, scalar, array or a composition).

### Exact JSON Schema object

```json
{
  "type": "string",
  "minLength": 1,
  "description": "Stable URI or UUID-style identifier for a document lineage. Compared as exact Unicode text; never fetched."
}
```

<a id="def-revisionref"></a>
## revisionRef

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `documentId` | `#/$defs/opaqueDocumentId` | Yes |  |
| `revisionId` | `#/$defs/opaqueDocumentId` | Yes |  |
| `sha256` | `#/$defs/sha256` | No/conditional |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "documentId": {
      "$ref": "#/$defs/opaqueDocumentId"
    },
    "revisionId": {
      "$ref": "#/$defs/opaqueDocumentId"
    },
    "sha256": {
      "$ref": "#/$defs/sha256"
    }
  },
  "required": [
    "documentId",
    "revisionId"
  ],
  "additionalProperties": false
}
```

<a id="def-software"></a>
## software

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `name` | `string` | Yes |  |
| `version` | `string` | No/conditional |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "name": {
      "type": "string",
      "minLength": 1
    },
    "version": {
      "type": "string",
      "minLength": 1
    }
  },
  "required": [
    "name"
  ],
  "additionalProperties": false
}
```

<a id="def-documentinfo"></a>
## documentInfo

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `id` | `#/$defs/opaqueDocumentId` | Yes |  |
| `revisionId` | `#/$defs/opaqueDocumentId` | Yes |  |
| `parents` | `array<#/$defs/revisionRef>` | No/conditional |  |
| `createdBy` | `#/$defs/software` | No/conditional |  |
| `modifiedBy` | `#/$defs/software` | No/conditional |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/opaqueDocumentId"
    },
    "revisionId": {
      "$ref": "#/$defs/opaqueDocumentId"
    },
    "parents": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/revisionRef"
      },
      "uniqueItems": true
    },
    "createdBy": {
      "$ref": "#/$defs/software"
    },
    "modifiedBy": {
      "$ref": "#/$defs/software"
    }
  },
  "required": [
    "id",
    "revisionId"
  ],
  "additionalProperties": false
}
```

<a id="def-key"></a>
## key

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `state` | `enum ["tonal", "atonal", "unspecified"]` | Yes |  |
| `tonic` | `#/$defs/spelledPitchClass` | No/conditional |  |
| `mode` | `string` | No/conditional | Authored mode identifier. Canonical recognized values include major, minor, dorian, phrygian, lydian, mixolydian, locrian. Unknown values are ... |
| `label` | `string` | No/conditional |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "state": {
      "enum": [
        "tonal",
        "atonal",
        "unspecified"
      ]
    },
    "tonic": {
      "$ref": "#/$defs/spelledPitchClass"
    },
    "mode": {
      "type": "string",
      "minLength": 1,
      "description": "Authored mode identifier. Canonical recognized values include major, minor, dorian, phrygian, lydian, mixolydian, locrian. Unknown values are preserved, never converted to major/minor."
    },
    "label": {
      "type": "string"
    }
  },
  "required": [
    "state"
  ],
  "additionalProperties": false,
  "allOf": [
    {
      "if": {
        "properties": {
          "state": {
            "const": "tonal"
          }
        },
        "required": [
          "state"
        ]
      },
      "then": {
        "required": [
          "tonic",
          "mode"
        ]
      },
      "else": {
        "not": {
          "anyOf": [
            {
              "required": [
                "tonic"
              ]
            },
            {
              "required": [
                "mode"
              ]
            }
          ]
        }
      }
    }
  ]
}
```

<a id="def-keychange"></a>
## keyChange

A change after tick zero; initial key is stored only at song.key. Change at tick 0 is forbidden to prevent dual authority.

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `id` | `#/$defs/id` | Yes |  |
| `at` | `#/$defs/positive` | Yes |  |
| `key` | `#/$defs/key` | Yes |  |
| `label` | `string` | No/conditional |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "at": {
      "$ref": "#/$defs/positive"
    },
    "key": {
      "$ref": "#/$defs/key"
    },
    "label": {
      "type": "string"
    }
  },
  "required": [
    "id",
    "at",
    "key"
  ],
  "additionalProperties": false,
  "description": "A change after tick zero; initial key is stored only at song.key. Change at tick 0 is forbidden to prevent dual authority."
}
```

<a id="def-scaledefinition"></a>
## scaleDefinition

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `id` | `#/$defs/id` | Yes |  |
| `tonic` | `#/$defs/spelledPitchClass` | Yes |  |
| `intervals` | `array<integer>` | Yes |  |
| `label` | `string` | No/conditional |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "tonic": {
      "$ref": "#/$defs/spelledPitchClass"
    },
    "intervals": {
      "type": "array",
      "items": {
        "type": "integer",
        "minimum": 0,
        "maximum": 11
      },
      "minItems": 1,
      "maxItems": 12,
      "uniqueItems": true,
      "contains": {
        "const": 0
      }
    },
    "label": {
      "type": "string"
    }
  },
  "required": [
    "id",
    "tonic",
    "intervals"
  ],
  "additionalProperties": false
}
```

<a id="def-scaletarget"></a>
## scaleTarget

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `type` | `enum ["section", "track", "clip", "chord", "note"]` | Yes |  |
| `id` | `#/$defs/id` | Yes |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "type": {
      "enum": [
        "section",
        "track",
        "clip",
        "chord",
        "note"
      ]
    },
    "id": {
      "$ref": "#/$defs/id"
    }
  },
  "required": [
    "type",
    "id"
  ],
  "additionalProperties": false
}
```

<a id="def-mood"></a>
## mood

Authored descriptive mood tag; not a generator preset or a probability.

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `id` | `#/$defs/id` | Yes | Stable song-local ID unique among all Core objects. |
| `name` | `string` | Yes | Original Unicode genre label, never normalized or rewritten during import. |
| `externalUri` | `string` | No/conditional | Optional external vocabulary URI hint; never authoritative for the authored mood name and never auto-dereferenced. |

### Exact JSON Schema object

```json
{
  "type": "object",
  "description": "Authored descriptive mood tag; not a generator preset or a probability.",
  "properties": {
    "id": {
      "$ref": "#/$defs/id",
      "description": "Stable song-local ID unique among all Core objects."
    },
    "name": {
      "type": "string",
      "minLength": 1,
      "description": "Original Unicode genre label, never normalized or rewritten during import."
    },
    "externalUri": {
      "type": "string",
      "minLength": 1,
      "format": "uri",
      "description": "Optional external vocabulary URI hint; never authoritative for the authored mood name and never auto-dereferenced."
    }
  },
  "required": [
    "id",
    "name"
  ],
  "additionalProperties": false
}
```

<a id="def-rightsstatement"></a>
## rightsStatement

Authored rights statement only; no rights or permissions are inferred or granted by the format.

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `notice` | `string` | No/conditional |  |
| `licenseUri` | `string` | No/conditional |  |
| `rightsHolderIds` | `array<#/$defs/id>` | No/conditional |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "notice": {
      "type": "string"
    },
    "licenseUri": {
      "type": "string",
      "minLength": 1
    },
    "rightsHolderIds": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/id"
      },
      "uniqueItems": true
    }
  },
  "required": [],
  "additionalProperties": false,
  "description": "Authored rights statement only; no rights or permissions are inferred or granted by the format.",
  "minProperties": 1
}
```

<a id="def-grooveintent"></a>
## grooveIntent

Descriptive generation intent only. Never re-apply to already stored notes. unitTicks is one unswung subdivision; two subdivisions form a pair.

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `name` | `string` | No/conditional |  |
| `unitTicks` | `#/$defs/positive` | No/conditional |  |
| `longWeight` | `integer` | No/conditional |  |
| `shortWeight` | `integer` | No/conditional |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "name": {
      "type": "string"
    },
    "unitTicks": {
      "$ref": "#/$defs/positive"
    },
    "longWeight": {
      "type": "integer",
      "minimum": 1,
      "maximum": 1000000
    },
    "shortWeight": {
      "type": "integer",
      "minimum": 1,
      "maximum": 1000000
    }
  },
  "required": [],
  "additionalProperties": false,
  "description": "Descriptive generation intent only. Never re-apply to already stored notes. unitTicks is one unswung subdivision; two subdivisions form a pair.",
  "minProperties": 1,
  "dependentRequired": {
    "unitTicks": [
      "longWeight",
      "shortWeight"
    ],
    "longWeight": [
      "unitTicks",
      "shortWeight"
    ],
    "shortWeight": [
      "unitTicks",
      "longWeight"
    ]
  }
}
```

<a id="def-generationintent"></a>
## generationIntent

Portable description of intent, not a promise to reproduce an algorithm. Does not change song.genres or song.moods.

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `genreNames` | `array<string>` | No/conditional |  |
| `moodNames` | `array<string>` | No/conditional |  |
| `groove` | `#/$defs/grooveIntent` | No/conditional |  |
| `prompt` | `string` | No/conditional |  |
| `seed` | `string` | No/conditional |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "genreNames": {
      "type": "array",
      "items": {
        "type": "string",
        "minLength": 1
      }
    },
    "moodNames": {
      "type": "array",
      "items": {
        "type": "string",
        "minLength": 1
      }
    },
    "groove": {
      "$ref": "#/$defs/grooveIntent"
    },
    "prompt": {
      "type": "string"
    },
    "seed": {
      "type": "string"
    }
  },
  "required": [],
  "additionalProperties": false,
  "description": "Portable description of intent, not a promise to reproduce an algorithm. Does not change song.genres or song.moods."
}
```

<a id="def-relativephrases"></a>
## relativePhrases

Standard optional Core object under root version 4.0.0, not an extension. Current relationships must be consistent with saved Core; loading never performs editing or generation.

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `status` | `enum ["current", "stale", "unverified"]` | Yes |  |
| `dependencies` | `#/$defs/dependencies` | Yes |  |
| `assignments` | `array<#/$defs/relativeAssignment>` | Yes |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "status": {
      "enum": [
        "current",
        "stale",
        "unverified"
      ]
    },
    "dependencies": {
      "$ref": "#/$defs/dependencies"
    },
    "assignments": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/relativeAssignment"
      }
    }
  },
  "required": [
    "status",
    "dependencies",
    "assignments"
  ],
  "additionalProperties": false,
  "description": "Standard optional Core object under root version 4.0.0, not an extension. Current relationships must be consistent with saved Core; loading never performs editing or generation."
}
```

<a id="def-generation"></a>
## generation

Standard optional Core object under root version 4.0.0, not an extension. Current relationships must be consistent with saved Core; loading never performs editing or generation.

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `status` | `enum ["current", "stale", "unverified"]` | Yes |  |
| `dependencies` | `#/$defs/dependencies` | Yes |  |
| `processes` | `array<#/$defs/generationProcess>` | Yes |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "status": {
      "enum": [
        "current",
        "stale",
        "unverified"
      ]
    },
    "dependencies": {
      "$ref": "#/$defs/dependencies"
    },
    "processes": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/generationProcess"
      }
    }
  },
  "required": [
    "status",
    "dependencies",
    "processes"
  ],
  "additionalProperties": false,
  "description": "Standard optional Core object under root version 4.0.0, not an extension. Current relationships must be consistent with saved Core; loading never performs editing or generation."
}
```

<a id="def-presentation"></a>
## presentation

Standard optional Core object under root version 4.0.0, not an extension. Current relationships must be consistent with saved Core; loading never performs editing or generation.

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `status` | `enum ["current", "stale", "unverified"]` | Yes |  |
| `dependencies` | `#/$defs/dependencies` | Yes |  |
| `roleDefinitions` | `array<#/$defs/roleDefinition>` | Yes |  |
| `sectionRoleAssignments` | `object` | Yes |  |
| `appearance` | `object` | Yes |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "status": {
      "enum": [
        "current",
        "stale",
        "unverified"
      ]
    },
    "dependencies": {
      "$ref": "#/$defs/dependencies"
    },
    "roleDefinitions": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/roleDefinition"
      }
    },
    "sectionRoleAssignments": {
      "type": "object",
      "propertyNames": {
        "$ref": "#/$defs/id"
      },
      "additionalProperties": {
        "$ref": "#/$defs/id"
      }
    },
    "appearance": {
      "type": "object",
      "properties": {
        "roleColors": {
          "$ref": "#/$defs/roleColorMap"
        },
        "customRoleColors": {
          "$ref": "#/$defs/customRoleColorMap"
        },
        "objectColors": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/objectColor"
          }
        }
      },
      "required": [
        "roleColors",
        "customRoleColors",
        "objectColors"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "status",
    "dependencies",
    "roleDefinitions",
    "sectionRoleAssignments",
    "appearance"
  ],
  "additionalProperties": false,
  "description": "Standard optional Core object under root version 4.0.0, not an extension. Current relationships must be consistent with saved Core; loading never performs editing or generation."
}
```

<a id="def-phraselibrary"></a>
## phraseLibrary

Standard optional Core object under root version 4.0.0, not an extension. Current relationships must be consistent with saved Core; loading never performs editing or generation.

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `status` | `enum ["current", "stale", "unverified"]` | Yes |  |
| `dependencies` | `#/$defs/dependencies` | Yes |  |
| `templates` | `array<#/$defs/phraseTemplate>` | Yes |  |
| `instances` | `array<#/$defs/phraseInstance>` | Yes |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "status": {
      "enum": [
        "current",
        "stale",
        "unverified"
      ]
    },
    "dependencies": {
      "$ref": "#/$defs/dependencies"
    },
    "templates": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/phraseTemplate"
      }
    },
    "instances": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/phraseInstance"
      }
    }
  },
  "required": [
    "status",
    "dependencies",
    "templates",
    "instances"
  ],
  "additionalProperties": false,
  "description": "Standard optional Core object under root version 4.0.0, not an extension. Current relationships must be consistent with saved Core; loading never performs editing or generation."
}
```

<a id="def-clipchoices"></a>
## clipChoices

Standard optional Core object under root version 4.0.0, not an extension. Current relationships must be consistent with saved Core; loading never performs editing or generation.

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `status` | `enum ["current", "stale", "unverified"]` | Yes |  |
| `dependencies` | `#/$defs/dependencies` | Yes |  |
| `groups` | `array<#/$defs/clipChoiceGroup>` | Yes |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "status": {
      "enum": [
        "current",
        "stale",
        "unverified"
      ]
    },
    "dependencies": {
      "$ref": "#/$defs/dependencies"
    },
    "groups": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/clipChoiceGroup"
      }
    }
  },
  "required": [
    "status",
    "dependencies",
    "groups"
  ],
  "additionalProperties": false,
  "description": "Standard optional Core object under root version 4.0.0, not an extension. Current relationships must be consistent with saved Core; loading never performs editing or generation."
}
```

<a id="def-localization"></a>
## localization

Standard optional Core object under root version 4.0.0, not an extension. Current relationships must be consistent with saved Core; loading never performs editing or generation.

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `status` | `enum ["current", "stale", "unverified"]` | Yes |  |
| `dependencies` | `#/$defs/dependencies` | Yes |  |
| `entries` | `array<#/$defs/localizationEntry>` | Yes |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "status": {
      "enum": [
        "current",
        "stale",
        "unverified"
      ]
    },
    "dependencies": {
      "$ref": "#/$defs/dependencies"
    },
    "entries": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/localizationEntry"
      }
    }
  },
  "required": [
    "status",
    "dependencies",
    "entries"
  ],
  "description": "Standard optional Core object under root version 4.0.0, not an extension. Current relationships must be consistent with saved Core; loading never performs editing or generation."
}
```

<a id="def-corephrasesourcenote"></a>
## corePhraseSourceNote

Template-local source note for phrase materialization. It carries the same note-local 3.5 properties as concrete notes. It is not performed by itself; concrete track notes remain the saved playback events.

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `id` | `#/$defs/id` | Yes |  |
| `start` | `#/$defs/signed` | Yes |  |
| `duration` | `#/$defs/positive` | Yes | Positive note gate in ticks, not the guaranteed audible duration of a one-shot percussion sample. |
| `pitch` | `#/$defs/pitch` | No/conditional |  |
| `soundSlotId` | `#/$defs/id` | No/conditional | Document-local Sound Slot ID. Distinct events and IDs stay distinct even if several slots share a MIDI key; a renderer decides the acoustic ti... |
| `velocity` | `integer` | No/conditional | Optional template note-on velocity, 1–127. Applied only by an explicit materialization/update according to instance.velocityMode; never a perf... |
| `enabled` | `boolean` | No/conditional | Optional note-local enable state. Omitted means enabled. False preserves the note but suppresses scheduling/playback; it is distinct from prob... |
| `releaseVelocity` | `integer` | No/conditional | Optional MIDI Note Off/release velocity, 0-127. Omit when unspecified; readers must not invent and write back a default. |
| `probability` | `number` | No/conditional | Optional note-playback probability from 0.0 to 1.0. Omitted means 1.0. Random sequence identity is not standardized; materialize notes for det... |
| `velocityDeviation` | `integer` | No/conditional | Optional note-local velocity variation endpoint relative to velocity. Requires velocity. Semantic rule: velocity + velocityDeviation must rema... |
| `pitchRole` | `enum ["musical", "fixedTrigger"]` | No/conditional | Meaning of a pitch note. musical participates in pitch/harmony/transpose operations; fixedTrigger is an exact MIDI key trigger (for example a ... |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "start": {
      "$ref": "#/$defs/signed"
    },
    "duration": {
      "$ref": "#/$defs/positive",
      "description": "Positive note gate in ticks, not the guaranteed audible duration of a one-shot percussion sample."
    },
    "pitch": {
      "$ref": "#/$defs/pitch"
    },
    "soundSlotId": {
      "$ref": "#/$defs/id",
      "description": "Document-local Sound Slot ID. Distinct events and IDs stay distinct even if several slots share a MIDI key; a renderer decides the acoustic timbre."
    },
    "velocity": {
      "type": "integer",
      "minimum": 1,
      "maximum": 127,
      "description": "Optional template note-on velocity, 1–127. Applied only by an explicit materialization/update according to instance.velocityMode; never a performed event by itself."
    },
    "enabled": {
      "type": "boolean",
      "default": true,
      "description": "Optional note-local enable state. Omitted means enabled. False preserves the note but suppresses scheduling/playback; it is distinct from probability=0."
    },
    "releaseVelocity": {
      "type": "integer",
      "minimum": 0,
      "maximum": 127,
      "description": "Optional MIDI Note Off/release velocity, 0-127. Omit when unspecified; readers must not invent and write back a default."
    },
    "probability": {
      "type": "number",
      "minimum": 0,
      "maximum": 1,
      "default": 1,
      "description": "Optional note-playback probability from 0.0 to 1.0. Omitted means 1.0. Random sequence identity is not standardized; materialize notes for deterministic interchange."
    },
    "velocityDeviation": {
      "type": "integer",
      "minimum": -126,
      "maximum": 126,
      "default": 0,
      "description": "Optional note-local velocity variation endpoint relative to velocity. Requires velocity. Semantic rule: velocity + velocityDeviation must remain within 1..127. Omitted means 0."
    },
    "pitchRole": {
      "enum": [
        "musical",
        "fixedTrigger"
      ],
      "default": "musical",
      "description": "Meaning of a pitch note. musical participates in pitch/harmony/transpose operations; fixedTrigger is an exact MIDI key trigger (for example a keyswitch) and is never transposed or used as musical-pitch evidence. Allowed only on pitch notes."
    }
  },
  "required": [
    "id",
    "start",
    "duration"
  ],
  "additionalProperties": false,
  "oneOf": [
    {
      "required": [
        "pitch"
      ],
      "not": {
        "required": [
          "soundSlotId"
        ]
      }
    },
    {
      "required": [
        "soundSlotId"
      ],
      "not": {
        "required": [
          "pitch"
        ]
      }
    }
  ],
  "description": "Template-local source note for phrase materialization. It carries the same note-local 3.5 properties as concrete notes. It is not performed by itself; concrete track notes remain the saved playback events.",
  "dependentRequired": {
    "velocityDeviation": [
      "velocity"
    ]
  },
  "allOf": [
    {
      "if": {
        "required": [
          "soundSlotId"
        ]
      },
      "then": {
        "not": {
          "required": [
            "pitchRole"
          ]
        }
      }
    }
  ]
}
```

<a id="def-provenancesource"></a>
## provenanceSource

Historical source; hashes refer to exact source bytes, not the current document. No automatic retrieval.

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `format` | `string` | No/conditional |  |
| `version` | `string` | No/conditional |  |
| `sha256` | `#/$defs/sha256` | No/conditional |  |
| `uri` | `string` | No/conditional |  |
| `documentId` | `#/$defs/opaqueDocumentId` | No/conditional |  |
| `revisionId` | `#/$defs/opaqueDocumentId` | No/conditional |  |
| `resourceId` | `#/$defs/id` | No/conditional |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "format": {
      "type": "string",
      "minLength": 1
    },
    "version": {
      "type": "string",
      "minLength": 1
    },
    "sha256": {
      "$ref": "#/$defs/sha256"
    },
    "uri": {
      "type": "string",
      "minLength": 1
    },
    "documentId": {
      "$ref": "#/$defs/opaqueDocumentId"
    },
    "revisionId": {
      "$ref": "#/$defs/opaqueDocumentId"
    },
    "resourceId": {
      "$ref": "#/$defs/id"
    }
  },
  "required": [],
  "additionalProperties": false,
  "description": "Historical source; hashes refer to exact source bytes, not the current document. No automatic retrieval.",
  "minProperties": 1,
  "dependentRequired": {
    "revisionId": [
      "documentId"
    ]
  }
}
```

<a id="def-provenancerecord"></a>
## provenanceRecord

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `id` | `#/$defs/id` | Yes |  |
| `action` | `enum ["create", "import", "conversion", "edit", "transpose", "merge", "generation", "other"]` | Yes |  |
| `description` | `string` | No/conditional |  |
| `tool` | `#/$defs/software` | No/conditional |  |
| `sources` | `array<#/$defs/provenanceSource>` | No/conditional |  |
| `semitones` | `integer` | No/conditional |  |
| `beforeKey` | `#/$defs/key` | No/conditional |  |
| `afterKey` | `#/$defs/key` | No/conditional |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "action": {
      "enum": [
        "create",
        "import",
        "conversion",
        "edit",
        "transpose",
        "merge",
        "generation",
        "other"
      ]
    },
    "description": {
      "type": "string"
    },
    "tool": {
      "$ref": "#/$defs/software"
    },
    "sources": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/provenanceSource"
      }
    },
    "semitones": {
      "type": "integer",
      "minimum": -127,
      "maximum": 127
    },
    "beforeKey": {
      "$ref": "#/$defs/key"
    },
    "afterKey": {
      "$ref": "#/$defs/key"
    }
  },
  "required": [
    "id",
    "action"
  ],
  "additionalProperties": false,
  "allOf": [
    {
      "if": {
        "not": {
          "properties": {
            "action": {
              "const": "transpose"
            }
          },
          "required": [
            "action"
          ]
        }
      },
      "then": {
        "not": {
          "required": [
            "semitones"
          ]
        }
      }
    }
  ]
}
```

<a id="def-provenance"></a>
## provenance

Non-executable historical assertions; not composer credits and not a substitute for current metadata. Does not prove authorship or operation correctness.

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `records` | `array<#/$defs/provenanceRecord>` | Yes |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "records": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/provenanceRecord"
      }
    }
  },
  "required": [
    "records"
  ],
  "additionalProperties": false,
  "description": "Non-executable historical assertions; not composer credits and not a substitute for current metadata. Does not prove authorship or operation correctness."
}
```

<a id="def-midichannel"></a>
## midiChannel

Human-readable MIDI 1.0 channel number 1..16. Wire status-nibble channel = value - 1.

No direct `properties` table (object may be an enum, scalar, array or a composition).

### Exact JSON Schema object

```json
{
  "type": "integer",
  "minimum": 1,
  "maximum": 16,
  "description": "Human-readable MIDI 1.0 channel number 1..16. Wire status-nibble channel = value - 1."
}
```

<a id="def-midibus"></a>
## midiBus

Document-local logical MIDI destination. Each bus has its own MIDI channel namespace. It is not a physical OS/USB/DAW port binding.

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `id` | `#/$defs/id` | Yes |  |
| `name` | `string` | Yes |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "description": "Document-local logical MIDI destination. Each bus has its own MIDI channel namespace. It is not a physical OS/USB/DAW port binding.",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "name": {
      "type": "string"
    }
  },
  "required": [
    "id",
    "name"
  ],
  "additionalProperties": false
}
```

<a id="def-midi"></a>
## midi

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `buses` | `array<#/$defs/midiBus>` | Yes |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "buses": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/midiBus"
      }
    }
  },
  "required": [
    "buses"
  ],
  "additionalProperties": false
}
```

<a id="def-mpesettings"></a>
## mpeSettings

Semantic MPE zone declaration. Lower-zone master is channel 1 and upper-zone master is channel 16; member channels are derived contiguously from memberChannelCount.

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `zone` | `enum ["lower", "upper"]` | Yes |  |
| `memberChannelCount` | `integer` | Yes |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "description": "Semantic MPE zone declaration. Lower-zone master is channel 1 and upper-zone master is channel 16; member channels are derived contiguously from memberChannelCount.",
  "properties": {
    "zone": {
      "enum": [
        "lower",
        "upper"
      ]
    },
    "memberChannelCount": {
      "type": "integer",
      "minimum": 1,
      "maximum": 15
    }
  },
  "required": [
    "zone",
    "memberChannelCount"
  ],
  "additionalProperties": false
}
```

<a id="def-trackmidi"></a>
## trackMidi

Optional MIDI channel/routing interpretation for a track. busId is a logical OSTF bus, never a physical MIDI port.

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `busId` | `#/$defs/id` | No/conditional |  |
| `mode` | `enum ["singleChannel", "multiChannel", "mpe"]` | Yes |  |
| `channel` | `#/$defs/midiChannel` | No/conditional |  |
| `mpe` | `#/$defs/mpeSettings` | No/conditional |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "description": "Optional MIDI channel/routing interpretation for a track. busId is a logical OSTF bus, never a physical MIDI port.",
  "properties": {
    "busId": {
      "$ref": "#/$defs/id"
    },
    "mode": {
      "enum": [
        "singleChannel",
        "multiChannel",
        "mpe"
      ]
    },
    "channel": {
      "$ref": "#/$defs/midiChannel"
    },
    "mpe": {
      "$ref": "#/$defs/mpeSettings"
    }
  },
  "required": [
    "mode"
  ],
  "additionalProperties": false,
  "allOf": [
    {
      "if": {
        "properties": {
          "mode": {
            "const": "singleChannel"
          }
        },
        "required": [
          "mode"
        ]
      },
      "then": {
        "required": [
          "channel"
        ],
        "not": {
          "required": [
            "mpe"
          ]
        }
      }
    },
    {
      "if": {
        "properties": {
          "mode": {
            "const": "multiChannel"
          }
        },
        "required": [
          "mode"
        ]
      },
      "then": {
        "not": {
          "anyOf": [
            {
              "required": [
                "channel"
              ]
            },
            {
              "required": [
                "mpe"
              ]
            }
          ]
        }
      }
    },
    {
      "if": {
        "properties": {
          "mode": {
            "const": "mpe"
          }
        },
        "required": [
          "mode"
        ]
      },
      "then": {
        "required": [
          "mpe"
        ],
        "not": {
          "required": [
            "channel"
          ]
        }
      }
    }
  ]
}
```

<a id="def-controlchangeevent"></a>
## controlChangeEvent

MIDI 1.0 Control Change. Controllers 120..127 use channelMode instead.

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `id` | `#/$defs/id` | Yes |  |
| `start` | `#/$defs/signed` | Yes |  |
| `order` | `#/$defs/signed` | No/conditional | Same-tick ordering key. Omitted means 1. Note Off has implicit order 0 and Note On implicit order 2; ties are resolved by the normative orderi... |
| `channel` | `#/$defs/midiChannel` | No/conditional |  |
| `type` | `const "controlChange"` | Yes |  |
| `targetNoteId` | `#/$defs/id` | No/conditional | Optional semantic association with an existing concrete note. It does not replace channel/pitch wire semantics. |
| `controller` | `integer` | Yes |  |
| `value` | `integer` | Yes |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "description": "MIDI 1.0 Control Change. Controllers 120..127 use channelMode instead.",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "start": {
      "$ref": "#/$defs/signed"
    },
    "order": {
      "$ref": "#/$defs/signed",
      "default": 1,
      "description": "Same-tick ordering key. Omitted means 1. Note Off has implicit order 0 and Note On implicit order 2; ties are resolved by the normative ordering rules."
    },
    "channel": {
      "$ref": "#/$defs/midiChannel"
    },
    "type": {
      "const": "controlChange"
    },
    "targetNoteId": {
      "$ref": "#/$defs/id",
      "description": "Optional semantic association with an existing concrete note. It does not replace channel/pitch wire semantics."
    },
    "controller": {
      "type": "integer",
      "minimum": 0,
      "maximum": 119
    },
    "value": {
      "type": "integer",
      "minimum": 0,
      "maximum": 127
    }
  },
  "required": [
    "id",
    "start",
    "type",
    "controller",
    "value"
  ],
  "additionalProperties": false
}
```

<a id="def-channelmodeevent"></a>
## channelModeEvent

MIDI 1.0 Channel Mode message represented separately from ordinary Control Change.

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `id` | `#/$defs/id` | Yes |  |
| `start` | `#/$defs/signed` | Yes |  |
| `order` | `#/$defs/signed` | No/conditional | Same-tick ordering key. Omitted means 1. Note Off has implicit order 0 and Note On implicit order 2; ties are resolved by the normative orderi... |
| `channel` | `#/$defs/midiChannel` | No/conditional |  |
| `type` | `const "channelMode"` | Yes |  |
| `controller` | `integer` | Yes |  |
| `value` | `integer` | Yes |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "description": "MIDI 1.0 Channel Mode message represented separately from ordinary Control Change.",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "start": {
      "$ref": "#/$defs/signed"
    },
    "order": {
      "$ref": "#/$defs/signed",
      "default": 1,
      "description": "Same-tick ordering key. Omitted means 1. Note Off has implicit order 0 and Note On implicit order 2; ties are resolved by the normative ordering rules."
    },
    "channel": {
      "$ref": "#/$defs/midiChannel"
    },
    "type": {
      "const": "channelMode"
    },
    "controller": {
      "type": "integer",
      "minimum": 120,
      "maximum": 127
    },
    "value": {
      "type": "integer",
      "minimum": 0,
      "maximum": 127
    }
  },
  "required": [
    "id",
    "start",
    "type",
    "controller",
    "value"
  ],
  "additionalProperties": false
}
```

<a id="def-programchangeevent"></a>
## programChangeEvent

MIDI 1.0 Program Change using the wire data value 0..127. UI may display 1..128.

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `id` | `#/$defs/id` | Yes |  |
| `start` | `#/$defs/signed` | Yes |  |
| `order` | `#/$defs/signed` | No/conditional | Same-tick ordering key. Omitted means 1. Note Off has implicit order 0 and Note On implicit order 2; ties are resolved by the normative orderi... |
| `channel` | `#/$defs/midiChannel` | No/conditional |  |
| `type` | `const "programChange"` | Yes |  |
| `program` | `integer` | Yes |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "description": "MIDI 1.0 Program Change using the wire data value 0..127. UI may display 1..128.",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "start": {
      "$ref": "#/$defs/signed"
    },
    "order": {
      "$ref": "#/$defs/signed",
      "default": 1,
      "description": "Same-tick ordering key. Omitted means 1. Note Off has implicit order 0 and Note On implicit order 2; ties are resolved by the normative ordering rules."
    },
    "channel": {
      "$ref": "#/$defs/midiChannel"
    },
    "type": {
      "const": "programChange"
    },
    "program": {
      "type": "integer",
      "minimum": 0,
      "maximum": 127
    }
  },
  "required": [
    "id",
    "start",
    "type",
    "program"
  ],
  "additionalProperties": false
}
```

<a id="def-pitchbendevent"></a>
## pitchBendEvent

MIDI 1.0 14-bit Pitch Bend Change. Bend range is receiver state/RPN data, not encoded in value14.

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `id` | `#/$defs/id` | Yes |  |
| `start` | `#/$defs/signed` | Yes |  |
| `order` | `#/$defs/signed` | No/conditional | Same-tick ordering key. Omitted means 1. Note Off has implicit order 0 and Note On implicit order 2; ties are resolved by the normative orderi... |
| `channel` | `#/$defs/midiChannel` | No/conditional |  |
| `type` | `const "pitchBend"` | Yes |  |
| `targetNoteId` | `#/$defs/id` | No/conditional | Optional semantic association with an existing concrete note. It does not replace channel/pitch wire semantics. |
| `value14` | `integer` | Yes | Raw MIDI 1.0 14-bit pitch-bend value; center is 8192. |

### Exact JSON Schema object

```json
{
  "type": "object",
  "description": "MIDI 1.0 14-bit Pitch Bend Change. Bend range is receiver state/RPN data, not encoded in value14.",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "start": {
      "$ref": "#/$defs/signed"
    },
    "order": {
      "$ref": "#/$defs/signed",
      "default": 1,
      "description": "Same-tick ordering key. Omitted means 1. Note Off has implicit order 0 and Note On implicit order 2; ties are resolved by the normative ordering rules."
    },
    "channel": {
      "$ref": "#/$defs/midiChannel"
    },
    "type": {
      "const": "pitchBend"
    },
    "targetNoteId": {
      "$ref": "#/$defs/id",
      "description": "Optional semantic association with an existing concrete note. It does not replace channel/pitch wire semantics."
    },
    "value14": {
      "type": "integer",
      "minimum": 0,
      "maximum": 16383,
      "description": "Raw MIDI 1.0 14-bit pitch-bend value; center is 8192."
    }
  },
  "required": [
    "id",
    "start",
    "type",
    "value14"
  ],
  "additionalProperties": false
}
```

<a id="def-channelpressureevent"></a>
## channelPressureEvent

MIDI 1.0 Channel Pressure (channel aftertouch).

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `id` | `#/$defs/id` | Yes |  |
| `start` | `#/$defs/signed` | Yes |  |
| `order` | `#/$defs/signed` | No/conditional | Same-tick ordering key. Omitted means 1. Note Off has implicit order 0 and Note On implicit order 2; ties are resolved by the normative orderi... |
| `channel` | `#/$defs/midiChannel` | No/conditional |  |
| `type` | `const "channelPressure"` | Yes |  |
| `targetNoteId` | `#/$defs/id` | No/conditional | Optional semantic association with an existing concrete note. It does not replace channel/pitch wire semantics. |
| `value` | `integer` | Yes |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "description": "MIDI 1.0 Channel Pressure (channel aftertouch).",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "start": {
      "$ref": "#/$defs/signed"
    },
    "order": {
      "$ref": "#/$defs/signed",
      "default": 1,
      "description": "Same-tick ordering key. Omitted means 1. Note Off has implicit order 0 and Note On implicit order 2; ties are resolved by the normative ordering rules."
    },
    "channel": {
      "$ref": "#/$defs/midiChannel"
    },
    "type": {
      "const": "channelPressure"
    },
    "targetNoteId": {
      "$ref": "#/$defs/id",
      "description": "Optional semantic association with an existing concrete note. It does not replace channel/pitch wire semantics."
    },
    "value": {
      "type": "integer",
      "minimum": 0,
      "maximum": 127
    }
  },
  "required": [
    "id",
    "start",
    "type",
    "value"
  ],
  "additionalProperties": false
}
```

<a id="def-polypressureevent"></a>
## polyPressureEvent

MIDI 1.0 Polyphonic Key Pressure (poly aftertouch).

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `id` | `#/$defs/id` | Yes |  |
| `start` | `#/$defs/signed` | Yes |  |
| `order` | `#/$defs/signed` | No/conditional | Same-tick ordering key. Omitted means 1. Note Off has implicit order 0 and Note On implicit order 2; ties are resolved by the normative orderi... |
| `channel` | `#/$defs/midiChannel` | No/conditional |  |
| `type` | `const "polyPressure"` | Yes |  |
| `targetNoteId` | `#/$defs/id` | No/conditional | Optional semantic association with an existing concrete note. It does not replace channel/pitch wire semantics. |
| `pitch` | `#/$defs/pitch` | Yes |  |
| `value` | `integer` | Yes |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "description": "MIDI 1.0 Polyphonic Key Pressure (poly aftertouch).",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "start": {
      "$ref": "#/$defs/signed"
    },
    "order": {
      "$ref": "#/$defs/signed",
      "default": 1,
      "description": "Same-tick ordering key. Omitted means 1. Note Off has implicit order 0 and Note On implicit order 2; ties are resolved by the normative ordering rules."
    },
    "channel": {
      "$ref": "#/$defs/midiChannel"
    },
    "type": {
      "const": "polyPressure"
    },
    "targetNoteId": {
      "$ref": "#/$defs/id",
      "description": "Optional semantic association with an existing concrete note. It does not replace channel/pitch wire semantics."
    },
    "pitch": {
      "$ref": "#/$defs/pitch"
    },
    "value": {
      "type": "integer",
      "minimum": 0,
      "maximum": 127
    }
  },
  "required": [
    "id",
    "start",
    "type",
    "pitch",
    "value"
  ],
  "additionalProperties": false
}
```

<a id="def-midievent"></a>
## midiEvent

No direct `properties` table (object may be an enum, scalar, array or a composition).

### Exact JSON Schema object

```json
{
  "oneOf": [
    {
      "$ref": "#/$defs/controlChangeEvent"
    },
    {
      "$ref": "#/$defs/channelModeEvent"
    },
    {
      "$ref": "#/$defs/programChangeEvent"
    },
    {
      "$ref": "#/$defs/pitchBendEvent"
    },
    {
      "$ref": "#/$defs/channelPressureEvent"
    },
    {
      "$ref": "#/$defs/polyPressureEvent"
    }
  ]
}
```

<a id="def-lyricvoice"></a>
## lyricVoice

Explicit relationship between a vocal/melody track and a lyric document. Several voices may reference the same lyric document without duplicating text.

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `id` | `#/$defs/id` | Yes |  |
| `name` | `string` | No/conditional |  |
| `role` | `string` | No/conditional | Open authored role. Recommended values include lead, harmony, backing, unison, double, counter, adlib, response. |
| `trackId` | `#/$defs/id` | Yes |  |
| `documentId` | `#/$defs/id` | Yes |  |
| `vocalProfile` | `#/$defs/vocalProfile` | No/conditional | Optional engine-neutral vocal defaults; absence does not mean an instrument voice. |

### Exact JSON Schema object

```json
{
  "type": "object",
  "description": "Explicit relationship between a vocal/melody track and a lyric document. Several voices may reference the same lyric document without duplicating text.",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "name": {
      "type": "string"
    },
    "role": {
      "type": "string",
      "minLength": 1,
      "description": "Open authored role. Recommended values include lead, harmony, backing, unison, double, counter, adlib, response."
    },
    "trackId": {
      "$ref": "#/$defs/id"
    },
    "documentId": {
      "$ref": "#/$defs/id"
    },
    "vocalProfile": {
      "$ref": "#/$defs/vocalProfile",
      "description": "Optional engine-neutral vocal defaults; absence does not mean an instrument voice."
    }
  },
  "required": [
    "id",
    "trackId",
    "documentId"
  ],
  "additionalProperties": false
}
```

<a id="def-playablepitchrange"></a>
## playablePitchRange

Authored playable pitch capability in the same 0..127 pitch-number domain as melodic notes. Semantic rule: lowPitch <= highPitch.

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `lowPitch` | `#/$defs/pitch` | Yes |  |
| `highPitch` | `#/$defs/pitch` | Yes |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "lowPitch": {
      "$ref": "#/$defs/pitch"
    },
    "highPitch": {
      "$ref": "#/$defs/pitch"
    }
  },
  "required": [
    "lowPitch",
    "highPitch"
  ],
  "additionalProperties": false,
  "description": "Authored playable pitch capability in the same 0..127 pitch-number domain as melodic notes. Semantic rule: lowPitch <= highPitch."
}
```

<a id="def-directionpitchcollection"></a>
## directionPitchCollection

Direction-local pitch-class collection relative to tonic. It is not a harmonic scale-context object and has no independent timeline identity.

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `tonic` | `#/$defs/spelledPitchClass` | Yes |  |
| `intervals` | `array<integer>` | Yes |  |
| `label` | `string` | No/conditional |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "tonic": {
      "$ref": "#/$defs/spelledPitchClass"
    },
    "intervals": {
      "type": "array",
      "items": {
        "type": "integer",
        "minimum": 0,
        "maximum": 11
      },
      "minItems": 1,
      "maxItems": 12,
      "uniqueItems": true,
      "contains": {
        "const": 0
      }
    },
    "label": {
      "type": "string"
    }
  },
  "required": [
    "tonic",
    "intervals"
  ],
  "additionalProperties": false,
  "description": "Direction-local pitch-class collection relative to tonic. It is not a harmonic scale-context object and has no independent timeline identity."
}
```

<a id="def-directionpitchsource"></a>
## directionPitchSource

Source of pitch vocabulary for an improvisation Direction.

No direct `properties` table (object may be an enum, scalar, array or a composition).

### Exact JSON Schema object

```json
{
  "oneOf": [
    {
      "type": "object",
      "properties": {
        "type": {
          "const": "effectiveKeyScale"
        }
      },
      "required": [
        "type"
      ],
      "additionalProperties": false
    },
    {
      "type": "object",
      "properties": {
        "type": {
          "const": "songScale"
        }
      },
      "required": [
        "type"
      ],
      "additionalProperties": false
    },
    {
      "type": "object",
      "properties": {
        "type": {
          "const": "harmonyScales"
        },
        "scaleIds": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/id"
          },
          "minItems": 1,
          "uniqueItems": true
        }
      },
      "required": [
        "type",
        "scaleIds"
      ],
      "additionalProperties": false
    },
    {
      "type": "object",
      "properties": {
        "type": {
          "const": "explicitScale"
        },
        "scale": {
          "$ref": "#/$defs/directionPitchCollection"
        }
      },
      "required": [
        "type",
        "scale"
      ],
      "additionalProperties": false
    }
  ],
  "description": "Source of pitch vocabulary for an improvisation Direction."
}
```

<a id="def-improvisationdirectionparameters"></a>
## improvisationDirectionParameters

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `pitchSource` | `#/$defs/directionPitchSource` | Yes |  |
| `adherence` | `enum ["strict", "preferred"]` | Yes |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "pitchSource": {
      "$ref": "#/$defs/directionPitchSource"
    },
    "adherence": {
      "enum": [
        "strict",
        "preferred"
      ]
    }
  },
  "required": [
    "pitchSource",
    "adherence"
  ],
  "additionalProperties": false
}
```

<a id="def-playingroledirectionparameters"></a>
## playingRoleDirectionParameters

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `role` | `string` | Yes |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "role": {
      "type": "string",
      "minLength": 1
    }
  },
  "required": [
    "role"
  ],
  "additionalProperties": false
}
```

<a id="def-pitchrangedirectionparameters"></a>
## pitchRangeDirectionParameters

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `lowPitch` | `#/$defs/pitch` | Yes |  |
| `highPitch` | `#/$defs/pitch` | Yes |  |
| `constraint` | `enum ["strict", "preferred"]` | Yes |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "lowPitch": {
      "$ref": "#/$defs/pitch"
    },
    "highPitch": {
      "$ref": "#/$defs/pitch"
    },
    "constraint": {
      "enum": [
        "strict",
        "preferred"
      ]
    }
  },
  "required": [
    "lowPitch",
    "highPitch",
    "constraint"
  ],
  "additionalProperties": false
}
```

<a id="def-vendordirectionparameters"></a>
## vendorDirectionParameters

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `namespace` | `string` | Yes |  |
| `name` | `string` | Yes |  |
| `version` | `string` | No/conditional |  |
| `data` | `object` | Yes |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "namespace": {
      "type": "string",
      "minLength": 3,
      "pattern": "^[a-z][a-z0-9-]*(?:\\.[a-z][a-z0-9-]*){2,}$",
      "not": {
        "pattern": "^org\\.ostf(?:\\.|$)"
      }
    },
    "name": {
      "type": "string",
      "minLength": 1
    },
    "version": {
      "type": "string",
      "minLength": 1
    },
    "data": {
      "type": "object"
    }
  },
  "required": [
    "namespace",
    "name",
    "data"
  ],
  "additionalProperties": false
}
```

<a id="def-improvisationdirection"></a>
## improvisationDirection

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `id` | `#/$defs/id` | Yes |  |
| `start` | `#/$defs/nonnegative` | Yes |  |
| `duration` | `#/$defs/positive` | Yes |  |
| `label` | `string` | No/conditional |  |
| `instruction` | `string` | No/conditional | Supplemental human/AI-readable semantic instruction. Structured Core parameters remain authoritative. |
| `type` | `const "improvisation"` | Yes |  |
| `parameters` | `#/$defs/improvisationDirectionParameters` | Yes |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "start": {
      "$ref": "#/$defs/nonnegative"
    },
    "duration": {
      "$ref": "#/$defs/positive"
    },
    "label": {
      "type": "string"
    },
    "instruction": {
      "type": "string",
      "description": "Supplemental human/AI-readable semantic instruction. Structured Core parameters remain authoritative."
    },
    "type": {
      "const": "improvisation"
    },
    "parameters": {
      "$ref": "#/$defs/improvisationDirectionParameters"
    }
  },
  "required": [
    "id",
    "start",
    "duration",
    "type",
    "parameters"
  ],
  "additionalProperties": false
}
```

<a id="def-playingroledirection"></a>
## playingRoleDirection

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `id` | `#/$defs/id` | Yes |  |
| `start` | `#/$defs/nonnegative` | Yes |  |
| `duration` | `#/$defs/positive` | Yes |  |
| `label` | `string` | No/conditional |  |
| `instruction` | `string` | No/conditional | Supplemental human/AI-readable semantic instruction. Structured Core parameters remain authoritative. |
| `type` | `const "playingRole"` | Yes |  |
| `parameters` | `#/$defs/playingRoleDirectionParameters` | Yes |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "start": {
      "$ref": "#/$defs/nonnegative"
    },
    "duration": {
      "$ref": "#/$defs/positive"
    },
    "label": {
      "type": "string"
    },
    "instruction": {
      "type": "string",
      "description": "Supplemental human/AI-readable semantic instruction. Structured Core parameters remain authoritative."
    },
    "type": {
      "const": "playingRole"
    },
    "parameters": {
      "$ref": "#/$defs/playingRoleDirectionParameters"
    }
  },
  "required": [
    "id",
    "start",
    "duration",
    "type",
    "parameters"
  ],
  "additionalProperties": false
}
```

<a id="def-pitchrangedirection"></a>
## pitchRangeDirection

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `id` | `#/$defs/id` | Yes |  |
| `start` | `#/$defs/nonnegative` | Yes |  |
| `duration` | `#/$defs/positive` | Yes |  |
| `label` | `string` | No/conditional |  |
| `instruction` | `string` | No/conditional | Supplemental human/AI-readable semantic instruction. Structured Core parameters remain authoritative. |
| `type` | `const "pitchRange"` | Yes |  |
| `parameters` | `#/$defs/pitchRangeDirectionParameters` | Yes |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "start": {
      "$ref": "#/$defs/nonnegative"
    },
    "duration": {
      "$ref": "#/$defs/positive"
    },
    "label": {
      "type": "string"
    },
    "instruction": {
      "type": "string",
      "description": "Supplemental human/AI-readable semantic instruction. Structured Core parameters remain authoritative."
    },
    "type": {
      "const": "pitchRange"
    },
    "parameters": {
      "$ref": "#/$defs/pitchRangeDirectionParameters"
    }
  },
  "required": [
    "id",
    "start",
    "duration",
    "type",
    "parameters"
  ],
  "additionalProperties": false
}
```

<a id="def-vendorrangedirection"></a>
## vendorRangeDirection

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `id` | `#/$defs/id` | Yes |  |
| `start` | `#/$defs/nonnegative` | Yes |  |
| `duration` | `#/$defs/positive` | Yes |  |
| `label` | `string` | No/conditional |  |
| `instruction` | `string` | No/conditional | Supplemental human/AI-readable semantic instruction. Structured Core parameters remain authoritative. |
| `type` | `const "vendor"` | Yes |  |
| `parameters` | `#/$defs/vendorDirectionParameters` | Yes |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "start": {
      "$ref": "#/$defs/nonnegative"
    },
    "duration": {
      "$ref": "#/$defs/positive"
    },
    "label": {
      "type": "string"
    },
    "instruction": {
      "type": "string",
      "description": "Supplemental human/AI-readable semantic instruction. Structured Core parameters remain authoritative."
    },
    "type": {
      "const": "vendor"
    },
    "parameters": {
      "$ref": "#/$defs/vendorDirectionParameters"
    }
  },
  "required": [
    "id",
    "start",
    "duration",
    "type",
    "parameters"
  ],
  "additionalProperties": false
}
```

<a id="def-vendorpointdirection"></a>
## vendorPointDirection

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `id` | `#/$defs/id` | Yes |  |
| `at` | `#/$defs/nonnegative` | Yes |  |
| `type` | `const "vendor"` | Yes |  |
| `parameters` | `#/$defs/vendorDirectionParameters` | Yes |  |
| `label` | `string` | No/conditional |  |
| `instruction` | `string` | No/conditional | Supplemental human/AI-readable semantic instruction. Structured/vendor parameters remain authoritative. |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "at": {
      "$ref": "#/$defs/nonnegative"
    },
    "type": {
      "const": "vendor"
    },
    "parameters": {
      "$ref": "#/$defs/vendorDirectionParameters"
    },
    "label": {
      "type": "string"
    },
    "instruction": {
      "type": "string",
      "description": "Supplemental human/AI-readable semantic instruction. Structured/vendor parameters remain authoritative."
    }
  },
  "required": [
    "id",
    "at",
    "type",
    "parameters"
  ],
  "additionalProperties": false
}
```

<a id="def-trackdirection"></a>
## trackDirection

Typed semantic instruction owned by a track and positioned on the OSTF global timebase.

No direct `properties` table (object may be an enum, scalar, array or a composition).

### Exact JSON Schema object

```json
{
  "oneOf": [
    {
      "$ref": "#/$defs/improvisationDirection"
    },
    {
      "$ref": "#/$defs/playingRoleDirection"
    },
    {
      "$ref": "#/$defs/pitchRangeDirection"
    },
    {
      "$ref": "#/$defs/vendorRangeDirection"
    },
    {
      "$ref": "#/$defs/vendorPointDirection"
    },
    {
      "$ref": "#/$defs/phrasingDirection"
    },
    {
      "$ref": "#/$defs/vocalFreedomDirection"
    }
  ],
  "description": "Typed semantic instruction owned by a track and positioned on the OSTF global timebase."
}
```

<a id="def-vocalphonetics"></a>
## vocalPhonetics

Ordered phoneme symbols for a lyric unit, not an absolute pronunciation engine command.

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `alphabet` | `enum ["ipa", "xsampa", "arpabet", "other"]` | Yes |  |
| `language` | `string` | No/conditional |  |
| `symbols` | `array<string>` | Yes |  |
| `namespace` | `string` | No/conditional |  |
| `preferred` | `boolean` | No/conditional | Optional preference only within the same (alphabet, language) set for this lyricUnit. At most one preferred variant per key; absent does not i... |

### Exact JSON Schema object

```json
{
  "type": "object",
  "description": "Ordered phoneme symbols for a lyric unit, not an absolute pronunciation engine command.",
  "properties": {
    "alphabet": {
      "enum": [
        "ipa",
        "xsampa",
        "arpabet",
        "other"
      ]
    },
    "language": {
      "type": "string",
      "minLength": 1
    },
    "symbols": {
      "type": "array",
      "minItems": 1,
      "items": {
        "type": "string",
        "minLength": 1
      }
    },
    "namespace": {
      "type": "string",
      "minLength": 1
    },
    "preferred": {
      "type": "boolean",
      "description": "Optional preference only within the same (alphabet, language) set for this lyricUnit. At most one preferred variant per key; absent does not imply false or a guaranteed conversion."
    }
  },
  "required": [
    "alphabet",
    "symbols"
  ],
  "additionalProperties": false,
  "allOf": [
    {
      "if": {
        "properties": {
          "alphabet": {
            "const": "other"
          }
        },
        "required": [
          "alphabet"
        ]
      },
      "then": {
        "required": [
          "namespace"
        ]
      }
    }
  ]
}
```

<a id="def-vocalprofile"></a>
## vocalProfile

Voice default independent of commercial singer preset or license.

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `language` | `string` | No/conditional |  |
| `deliveryMode` | `enum ["sing", "rap", "speak", "hum"]` | No/conditional |  |
| `voiceDescription` | `string` | No/conditional |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "description": "Voice default independent of commercial singer preset or license.",
  "properties": {
    "language": {
      "type": "string",
      "minLength": 1
    },
    "deliveryMode": {
      "enum": [
        "sing",
        "rap",
        "speak",
        "hum"
      ]
    },
    "voiceDescription": {
      "type": "string",
      "minLength": 1
    }
  },
  "additionalProperties": false
}
```

<a id="def-vocalperformance"></a>
## vocalPerformance

Performance belonging to exactly one lyric voice within a containing clip.

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `id` | `#/$defs/id` | Yes |  |
| `voiceId` | `#/$defs/id` | Yes |  |
| `phonemeEvents` | `array<#/$defs/vocalPhonemeEvent>` | No/conditional |  |
| `pitchCurves` | `array<#/$defs/vocalPitchCurve>` | No/conditional |  |
| `expressionCurves` | `array<#/$defs/vocalExpressionCurve>` | No/conditional |  |
| `techniques` | `array<#/$defs/vocalTechnique>` | No/conditional |  |
| `breathEvents` | `array<#/$defs/vocalBreathEvent>` | No/conditional |  |
| `noteIds` | `array<#/$defs/id>` | No/conditional | Optional exact list of existing note IDs performed by this voice in the containing clip. No duplicate note objects. When present it includes a... |

### Exact JSON Schema object

```json
{
  "type": "object",
  "description": "Performance belonging to exactly one lyric voice within a containing clip.",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "voiceId": {
      "$ref": "#/$defs/id"
    },
    "phonemeEvents": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/vocalPhonemeEvent"
      }
    },
    "pitchCurves": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/vocalPitchCurve"
      }
    },
    "expressionCurves": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/vocalExpressionCurve"
      }
    },
    "techniques": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/vocalTechnique"
      }
    },
    "breathEvents": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/vocalBreathEvent"
      }
    },
    "noteIds": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/id"
      },
      "minItems": 1,
      "uniqueItems": true,
      "description": "Optional exact list of existing note IDs performed by this voice in the containing clip. No duplicate note objects. When present it includes all locally aligned note IDs for that voice. When absent, derive ownership only from voice-specific alignments. Never infer from song.melodyTrackIds."
    }
  },
  "required": [
    "id",
    "voiceId"
  ],
  "additionalProperties": false
}
```

<a id="def-vocalphonemeevent"></a>
## vocalPhonemeEvent

Explicit phoneme timing, expressed in clip-relative ppq ticks, negative allowed with nonnegative absolute song time.

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `id` | `#/$defs/id` | Yes |  |
| `unitId` | `#/$defs/id` | Yes |  |
| `noteId` | `#/$defs/id` | No/conditional |  |
| `alphabet` | `enum ["ipa", "xsampa", "arpabet", "other"]` | Yes |  |
| `namespace` | `string` | No/conditional |  |
| `symbol` | `string` | Yes |  |
| `start` | `#/$defs/signed` | Yes |  |
| `duration` | `#/$defs/positive` | Yes |  |
| `order` | `integer` | No/conditional | Optional deterministic ordering when multiple phonemeEvents for one voice share the same start tick; distinct within a (voiceId, start) tie gr... |

### Exact JSON Schema object

```json
{
  "type": "object",
  "description": "Explicit phoneme timing, expressed in clip-relative ppq ticks, negative allowed with nonnegative absolute song time.",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "unitId": {
      "$ref": "#/$defs/id"
    },
    "noteId": {
      "$ref": "#/$defs/id"
    },
    "alphabet": {
      "enum": [
        "ipa",
        "xsampa",
        "arpabet",
        "other"
      ]
    },
    "namespace": {
      "type": "string",
      "minLength": 1
    },
    "symbol": {
      "type": "string",
      "minLength": 1
    },
    "start": {
      "$ref": "#/$defs/signed"
    },
    "duration": {
      "$ref": "#/$defs/positive"
    },
    "order": {
      "type": "integer",
      "description": "Optional deterministic ordering when multiple phonemeEvents for one voice share the same start tick; distinct within a (voiceId, start) tie group. Not an audio rendering priority."
    }
  },
  "required": [
    "id",
    "unitId",
    "alphabet",
    "symbol",
    "start",
    "duration"
  ],
  "additionalProperties": false,
  "allOf": [
    {
      "if": {
        "properties": {
          "alphabet": {
            "const": "other"
          }
        },
        "required": [
          "alphabet"
        ]
      },
      "then": {
        "required": [
          "namespace"
        ]
      }
    }
  ]
}
```

<a id="def-vocalcurvepointpitch"></a>
## vocalCurvePointPitch

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `at` | `#/$defs/signed` | Yes |  |
| `value` | `number` | Yes | Semitone offset from the targeted MIDI note, in cents (signed). |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "at": {
      "$ref": "#/$defs/signed"
    },
    "value": {
      "type": "number",
      "description": "Semitone offset from the targeted MIDI note, in cents (signed)."
    }
  },
  "required": [
    "at",
    "value"
  ],
  "additionalProperties": false
}
```

<a id="def-vocalcurvepointnormalized"></a>
## vocalCurvePointNormalized

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `at` | `#/$defs/signed` | Yes |  |
| `value` | `number` | Yes |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "at": {
      "$ref": "#/$defs/signed"
    },
    "value": {
      "type": "number",
      "minimum": 0,
      "maximum": 1
    }
  },
  "required": [
    "at",
    "value"
  ],
  "additionalProperties": false
}
```

<a id="def-vocalpitchcurve"></a>
## vocalPitchCurve

Specific vocal pitch offset for a single concrete Note, in cents; sample points use clip-relative ppq ticks.

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `id` | `#/$defs/id` | Yes |  |
| `targetNoteId` | `#/$defs/id` | Yes |  |
| `unit` | `const "cents"` | Yes |  |
| `interpolation` | `enum ["step", "linear"]` | Yes |  |
| `points` | `array<#/$defs/vocalCurvePointPitch>` | Yes |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "description": "Specific vocal pitch offset for a single concrete Note, in cents; sample points use clip-relative ppq ticks.",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "targetNoteId": {
      "$ref": "#/$defs/id"
    },
    "unit": {
      "const": "cents"
    },
    "interpolation": {
      "enum": [
        "step",
        "linear"
      ]
    },
    "points": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/$defs/vocalCurvePointPitch"
      }
    }
  },
  "required": [
    "id",
    "targetNoteId",
    "unit",
    "interpolation",
    "points"
  ],
  "additionalProperties": false
}
```

<a id="def-vocalexpressioncurve"></a>
## vocalExpressionCurve

Portable vocal parameters, each normalized 0..1, with no promise of perceptually identical output across engines.

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `id` | `#/$defs/id` | Yes |  |
| `parameter` | `enum ["dynamics", "breathiness", "tension", "brightness", "voicing"]` | Yes |  |
| `interpolation` | `enum ["step", "linear"]` | Yes |  |
| `points` | `array<#/$defs/vocalCurvePointNormalized>` | Yes |  |
| `targetNoteId` | `#/$defs/id` | No/conditional | Optional note-specific replacement of a clip-scoped curve of the same parameter while the note is active. Points still use clip-relative ticks... |

### Exact JSON Schema object

```json
{
  "type": "object",
  "description": "Portable vocal parameters, each normalized 0..1, with no promise of perceptually identical output across engines.",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "parameter": {
      "enum": [
        "dynamics",
        "breathiness",
        "tension",
        "brightness",
        "voicing"
      ]
    },
    "interpolation": {
      "enum": [
        "step",
        "linear"
      ]
    },
    "points": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/$defs/vocalCurvePointNormalized"
      }
    },
    "targetNoteId": {
      "$ref": "#/$defs/id",
      "description": "Optional note-specific replacement of a clip-scoped curve of the same parameter while the note is active. Points still use clip-relative ticks. Do not sum both curves."
    }
  },
  "required": [
    "id",
    "parameter",
    "interpolation",
    "points"
  ],
  "additionalProperties": false
}
```

<a id="def-vocaltechnique"></a>
## vocalTechnique

Semantic artistic intention, not deterministic rendering or an extra pitch source.

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `id` | `#/$defs/id` | Yes |  |
| `start` | `#/$defs/signed` | Yes |  |
| `duration` | `#/$defs/positive` | Yes |  |
| `kind` | `enum ["scoop", "fall", "vibrato", "portamento", "legato", "staccato", "accent", "whisper", "growl", "falsetto", "humming", "rap", "melisma"]` | Yes |  |
| `intensity` | `number` | No/conditional |  |
| `targetNoteId` | `#/$defs/id` | No/conditional |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "description": "Semantic artistic intention, not deterministic rendering or an extra pitch source.",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "start": {
      "$ref": "#/$defs/signed"
    },
    "duration": {
      "$ref": "#/$defs/positive"
    },
    "kind": {
      "enum": [
        "scoop",
        "fall",
        "vibrato",
        "portamento",
        "legato",
        "staccato",
        "accent",
        "whisper",
        "growl",
        "falsetto",
        "humming",
        "rap",
        "melisma"
      ]
    },
    "intensity": {
      "type": "number",
      "minimum": 0,
      "maximum": 1
    },
    "targetNoteId": {
      "$ref": "#/$defs/id"
    }
  },
  "required": [
    "id",
    "start",
    "duration",
    "kind"
  ],
  "additionalProperties": false
}
```

<a id="def-vocalbreathevent"></a>
## vocalBreathEvent

Optional breath marker. The renderer decides whether to synthesize audible breath.

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `id` | `#/$defs/id` | Yes |  |
| `start` | `#/$defs/signed` | Yes |  |
| `duration` | `#/$defs/positive` | Yes |  |
| `kind` | `enum ["inhale", "exhale"]` | Yes |  |
| `intensity` | `number` | No/conditional |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "description": "Optional breath marker. The renderer decides whether to synthesize audible breath.",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "start": {
      "$ref": "#/$defs/signed"
    },
    "duration": {
      "$ref": "#/$defs/positive"
    },
    "kind": {
      "enum": [
        "inhale",
        "exhale"
      ]
    },
    "intensity": {
      "type": "number",
      "minimum": 0,
      "maximum": 1
    }
  },
  "required": [
    "id",
    "start",
    "duration",
    "kind"
  ],
  "additionalProperties": false
}
```

<a id="def-positiveintrange"></a>
## positiveIntRange

Inclusive tick bounds; semantic check min <= max.

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `min` | `#/$defs/positive` | Yes |  |
| `max` | `#/$defs/positive` | Yes |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "min": {
      "$ref": "#/$defs/positive"
    },
    "max": {
      "$ref": "#/$defs/positive"
    }
  },
  "required": [
    "min",
    "max"
  ],
  "additionalProperties": false,
  "description": "Inclusive tick bounds; semantic check min <= max."
}
```

<a id="def-nonnegativenumberrange"></a>
## nonnegativeNumberRange

Inclusive range; semantic check min <= max. Count distinct note-on groups at equal onset ticks as one onset.

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `min` | `number` | Yes |  |
| `max` | `number` | Yes |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "min": {
      "type": "number",
      "minimum": 0,
      "maximum": 128
    },
    "max": {
      "type": "number",
      "minimum": 0,
      "maximum": 128
    }
  },
  "required": [
    "min",
    "max"
  ],
  "additionalProperties": false,
  "description": "Inclusive range; semantic check min <= max. Count distinct note-on groups at equal onset ticks as one onset."
}
```

<a id="def-phrasingdirectionparameters"></a>
## phrasingDirectionParameters

At least one musical property beyond adherence must be authored; motifRef resolves to phraseLibrary.templates[].id.

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `phraseLengthTicks` | `#/$defs/positiveIntRange` | No/conditional |  |
| `onsetGroupsPerQuarter` | `#/$defs/nonnegativeNumberRange` | No/conditional |  |
| `development` | `enum ["repetition", "motivicVariation", "sequence", "contrast", "free"]` | No/conditional |  |
| `contour` | `enum ["ascending", "descending", "arch", "valley", "stable", "free"]` | No/conditional |  |
| `energyShape` | `enum ["rising", "falling", "arch", "valley", "stable", "free"]` | No/conditional | Abstract musical-energy direction; not equivalent to output velocity or volume. |
| `motifRef` | `#/$defs/id` | No/conditional |  |
| `adherence` | `enum ["strict", "preferred"]` | Yes |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "phraseLengthTicks": {
      "$ref": "#/$defs/positiveIntRange"
    },
    "onsetGroupsPerQuarter": {
      "$ref": "#/$defs/nonnegativeNumberRange"
    },
    "development": {
      "enum": [
        "repetition",
        "motivicVariation",
        "sequence",
        "contrast",
        "free"
      ]
    },
    "contour": {
      "enum": [
        "ascending",
        "descending",
        "arch",
        "valley",
        "stable",
        "free"
      ]
    },
    "energyShape": {
      "enum": [
        "rising",
        "falling",
        "arch",
        "valley",
        "stable",
        "free"
      ],
      "description": "Abstract musical-energy direction; not equivalent to output velocity or volume."
    },
    "motifRef": {
      "$ref": "#/$defs/id"
    },
    "adherence": {
      "enum": [
        "strict",
        "preferred"
      ]
    }
  },
  "required": [
    "adherence"
  ],
  "additionalProperties": false,
  "description": "At least one musical property beyond adherence must be authored; motifRef resolves to phraseLibrary.templates[].id.",
  "minProperties": 2
}
```

<a id="def-phrasingdirection"></a>
## phrasingDirection

4.3 optional phrasing Track Direction, using global source-timeline ticks.

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `id` | `#/$defs/id` | Yes |  |
| `type` | `const "phrasing"` | Yes |  |
| `start` | `#/$defs/nonnegative` | Yes |  |
| `duration` | `#/$defs/positive` | Yes |  |
| `label` | `string` | No/conditional |  |
| `instruction` | `string` | No/conditional | Non-executable music-text context, subordinate to structured fields. |
| `parameters` | `#/$defs/phrasingDirectionParameters` | Yes |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "type": {
      "const": "phrasing"
    },
    "start": {
      "$ref": "#/$defs/nonnegative"
    },
    "duration": {
      "$ref": "#/$defs/positive"
    },
    "label": {
      "type": "string"
    },
    "instruction": {
      "type": "string",
      "description": "Non-executable music-text context, subordinate to structured fields."
    },
    "parameters": {
      "$ref": "#/$defs/phrasingDirectionParameters"
    }
  },
  "required": [
    "id",
    "type",
    "start",
    "duration",
    "parameters"
  ],
  "additionalProperties": false,
  "description": "4.3 optional phrasing Track Direction, using global source-timeline ticks."
}
```

<a id="def-lyriccandidateset"></a>
## lyricCandidateSet

One ordered candidate sequence of authored Lyric Phrase IDs. No implicit note alignment.

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `phraseIds` | `array<#/$defs/id>` | Yes |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "phraseIds": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/id"
      },
      "minItems": 1,
      "uniqueItems": true
    }
  },
  "required": [
    "phraseIds"
  ],
  "additionalProperties": false,
  "description": "One ordered candidate sequence of authored Lyric Phrase IDs. No implicit note alignment."
}
```

<a id="def-vocalfreedomdirectionparameters"></a>
## vocalFreedomDirectionParameters

Voice-specific freedom policy. Fixed text does not automatically imply fixed melody or vice versa.

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `voiceId` | `#/$defs/id` | Yes |  |
| `textPolicy` | `enum ["fixed", "alternatives", "open"]` | Yes |  |
| `melodyPolicy` | `enum ["fixed", "ornamentable", "open"]` | Yes |  |
| `vocalizationKind` | `enum ["lexical", "scat", "humming", "nonLexical"]` | No/conditional |  |
| `candidatePhraseSets` | `array<#/$defs/lyricCandidateSet>` | No/conditional |  |
| `adherence` | `enum ["strict", "preferred"]` | Yes |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "voiceId": {
      "$ref": "#/$defs/id"
    },
    "textPolicy": {
      "enum": [
        "fixed",
        "alternatives",
        "open"
      ]
    },
    "melodyPolicy": {
      "enum": [
        "fixed",
        "ornamentable",
        "open"
      ]
    },
    "vocalizationKind": {
      "enum": [
        "lexical",
        "scat",
        "humming",
        "nonLexical"
      ]
    },
    "candidatePhraseSets": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/lyricCandidateSet"
      },
      "minItems": 2
    },
    "adherence": {
      "enum": [
        "strict",
        "preferred"
      ]
    }
  },
  "required": [
    "voiceId",
    "textPolicy",
    "melodyPolicy",
    "adherence"
  ],
  "additionalProperties": false,
  "description": "Voice-specific freedom policy. Fixed text does not automatically imply fixed melody or vice versa.",
  "if": {
    "properties": {
      "textPolicy": {
        "const": "alternatives"
      }
    },
    "required": [
      "textPolicy"
    ]
  },
  "then": {
    "required": [
      "candidatePhraseSets"
    ]
  },
  "else": {
    "not": {
      "required": [
        "candidatePhraseSets"
      ]
    }
  }
}
```

<a id="def-vocalfreedomdirection"></a>
## vocalFreedomDirection

4.3 optional vocalFreedom Track Direction, using global source-timeline ticks.

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `id` | `#/$defs/id` | Yes |  |
| `type` | `const "vocalFreedom"` | Yes |  |
| `start` | `#/$defs/nonnegative` | Yes |  |
| `duration` | `#/$defs/positive` | Yes |  |
| `label` | `string` | No/conditional |  |
| `instruction` | `string` | No/conditional | Non-executable music-text context, subordinate to structured fields. |
| `parameters` | `#/$defs/vocalFreedomDirectionParameters` | Yes |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "type": {
      "const": "vocalFreedom"
    },
    "start": {
      "$ref": "#/$defs/nonnegative"
    },
    "duration": {
      "$ref": "#/$defs/positive"
    },
    "label": {
      "type": "string"
    },
    "instruction": {
      "type": "string",
      "description": "Non-executable music-text context, subordinate to structured fields."
    },
    "parameters": {
      "$ref": "#/$defs/vocalFreedomDirectionParameters"
    }
  },
  "required": [
    "id",
    "type",
    "start",
    "duration",
    "parameters"
  ],
  "additionalProperties": false,
  "description": "4.3 optional vocalFreedom Track Direction, using global source-timeline ticks."
}
```

<a id="def-performancerequirements"></a>
## performanceRequirements

Minimum/peak musical capabilities required to realize this authored part, not an assertion about the performer. No robot mechanics or safety commands.

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `requiredPolyphony` | `integer` | No/conditional |  |
| `requiredPitchRange` | `#/$defs/playablePitchRange` | No/conditional |  |
| `requiredArticulations` | `array<string>` | No/conditional |  |
| `peakOnsetGroupsPerQuarter` | `number` | No/conditional |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "requiredPolyphony": {
      "type": "integer",
      "minimum": 1,
      "maximum": 128
    },
    "requiredPitchRange": {
      "$ref": "#/$defs/playablePitchRange"
    },
    "requiredArticulations": {
      "type": "array",
      "items": {
        "type": "string",
        "minLength": 1
      },
      "minItems": 1,
      "uniqueItems": true
    },
    "peakOnsetGroupsPerQuarter": {
      "type": "number",
      "exclusiveMinimum": 0,
      "maximum": 128
    }
  },
  "required": [],
  "additionalProperties": false,
  "description": "Minimum/peak musical capabilities required to realize this authored part, not an assertion about the performer. No robot mechanics or safety commands.",
  "minProperties": 1
}
```

<a id="def-performancescope"></a>
## performanceScope

Bind to exactly one finite visit within a specific plan.

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `performancePlanId` | `#/$defs/id` | Yes |  |
| `visitId` | `#/$defs/id` | Yes |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "performancePlanId": {
      "$ref": "#/$defs/id"
    },
    "visitId": {
      "$ref": "#/$defs/id"
    }
  },
  "required": [
    "performancePlanId",
    "visitId"
  ],
  "additionalProperties": false,
  "description": "Bind to exactly one finite visit within a specific plan."
}
```

<a id="def-ensembleinteraction"></a>
## ensembleInteraction

Directed actor/partner relationship: different Tracks, or the same Track only with both explicit and different Lyric Voice IDs whose trackId equals the shared Track. Use source tick range, visit scope, or both. No audio, real-time event, or motor control is implied. Same Track without two distinct owned Voices is a semantic error (JSON Schema cannot compare sibling ID values).

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `id` | `#/$defs/id` | Yes |  |
| `actorTrackId` | `#/$defs/id` | Yes |  |
| `partnerTrackId` | `#/$defs/id` | Yes |  |
| `actorVoiceId` | `#/$defs/id` | No/conditional |  |
| `partnerVoiceId` | `#/$defs/id` | No/conditional |  |
| `relation` | `enum ["respondTo", "followRhythm", "alternateWith", "leaveSpaceFor", "reinforce"]` | Yes |  |
| `start` | `#/$defs/nonnegative` | No/conditional |  |
| `duration` | `#/$defs/positive` | No/conditional |  |
| `scope` | `#/$defs/performanceScope` | No/conditional |  |
| `responseWindowTicks` | `#/$defs/positive` | No/conditional |  |
| `adherence` | `enum ["strict", "preferred"]` | Yes |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "actorTrackId": {
      "$ref": "#/$defs/id"
    },
    "partnerTrackId": {
      "$ref": "#/$defs/id"
    },
    "actorVoiceId": {
      "$ref": "#/$defs/id"
    },
    "partnerVoiceId": {
      "$ref": "#/$defs/id"
    },
    "relation": {
      "enum": [
        "respondTo",
        "followRhythm",
        "alternateWith",
        "leaveSpaceFor",
        "reinforce"
      ]
    },
    "start": {
      "$ref": "#/$defs/nonnegative"
    },
    "duration": {
      "$ref": "#/$defs/positive"
    },
    "scope": {
      "$ref": "#/$defs/performanceScope"
    },
    "responseWindowTicks": {
      "$ref": "#/$defs/positive"
    },
    "adherence": {
      "enum": [
        "strict",
        "preferred"
      ]
    }
  },
  "required": [
    "id",
    "actorTrackId",
    "partnerTrackId",
    "relation",
    "adherence"
  ],
  "additionalProperties": false,
  "description": "Directed actor/partner relationship: different Tracks, or the same Track only with both explicit and different Lyric Voice IDs whose trackId equals the shared Track. Use source tick range, visit scope, or both. No audio, real-time event, or motor control is implied. Same Track without two distinct owned Voices is a semantic error (JSON Schema cannot compare sibling ID values).",
  "anyOf": [
    {
      "required": [
        "start",
        "duration"
      ]
    },
    {
      "required": [
        "scope"
      ]
    }
  ],
  "dependentRequired": {
    "start": [
      "duration"
    ],
    "duration": [
      "start"
    ]
  }
}
```

<a id="def-visitpart"></a>
## visitPart

A part rule within one performance visit, not a mutation of the source Track.

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `trackId` | `#/$defs/id` | Yes |  |
| `role` | `string` | No/conditional | Visit-scoped role override of Track default; timed playingRole conflict requires explicitly listed replacement. |
| `realization` | `enum ["fixed", "open", "silent"]` | Yes |  |
| `replacesDirectionIds` | `array<#/$defs/id>` | No/conditional | Only explicit source-track playingRole Direction IDs may be replaced by the visit role. |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "trackId": {
      "$ref": "#/$defs/id"
    },
    "role": {
      "type": "string",
      "minLength": 1,
      "description": "Visit-scoped role override of Track default; timed playingRole conflict requires explicitly listed replacement."
    },
    "realization": {
      "enum": [
        "fixed",
        "open",
        "silent"
      ]
    },
    "replacesDirectionIds": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/id"
      },
      "uniqueItems": true,
      "description": "Only explicit source-track playingRole Direction IDs may be replaced by the visit role."
    }
  },
  "required": [
    "trackId",
    "realization"
  ],
  "additionalProperties": false,
  "description": "A part rule within one performance visit, not a mutation of the source Track."
}
```

<a id="def-performancevisit"></a>
## performanceVisit

Finite visit; exactly one source selector. Ordinals must be 0..N-1 in unique sequence within one plan.

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `id` | `#/$defs/id` | Yes |  |
| `ordinal` | `#/$defs/nonnegative` | Yes |  |
| `label` | `string` | No/conditional |  |
| `sourceSectionIds` | `array<#/$defs/id>` | No/conditional |  |
| `sourceRange` | `#/$defs/range` | No/conditional |  |
| `parts` | `array<#/$defs/visitPart>` | Yes |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "ordinal": {
      "$ref": "#/$defs/nonnegative"
    },
    "label": {
      "type": "string"
    },
    "sourceSectionIds": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/id"
      },
      "minItems": 1
    },
    "sourceRange": {
      "$ref": "#/$defs/range"
    },
    "parts": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/visitPart"
      }
    }
  },
  "required": [
    "id",
    "ordinal",
    "parts"
  ],
  "additionalProperties": false,
  "description": "Finite visit; exactly one source selector. Ordinals must be 0..N-1 in unique sequence within one plan.",
  "oneOf": [
    {
      "required": [
        "sourceSectionIds"
      ]
    },
    {
      "required": [
        "sourceRange"
      ]
    }
  ],
  "not": {
    "required": [
      "sourceSectionIds",
      "sourceRange"
    ]
  }
}
```

<a id="def-performanceplan"></a>
## performancePlan

Opt-in finite expanded playthrough. Source Section/Tick remains authoritative. No implicit cues, indefinite loops, or network session state.

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `id` | `#/$defs/id` | Yes |  |
| `name` | `string` | No/conditional |  |
| `mode` | `const "orderedFinite"` | Yes |  |
| `defaultRealization` | `enum ["fixed", "silent", "unspecified"]` | Yes | Explicit policy for unlisted tracks per visit; unspecified cannot claim deterministic replay. |
| `visits` | `array<#/$defs/performanceVisit>` | Yes |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "name": {
      "type": "string"
    },
    "mode": {
      "const": "orderedFinite"
    },
    "defaultRealization": {
      "enum": [
        "fixed",
        "silent",
        "unspecified"
      ],
      "description": "Explicit policy for unlisted tracks per visit; unspecified cannot claim deterministic replay."
    },
    "visits": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/performanceVisit"
      },
      "minItems": 1
    }
  },
  "required": [
    "id",
    "mode",
    "defaultRealization",
    "visits"
  ],
  "additionalProperties": false,
  "description": "Opt-in finite expanded playthrough. Source Section/Tick remains authoritative. No implicit cues, indefinite loops, or network session state."
}
```

## Draft 0.13 — Companion production profile parameter scope

This file remains the **full, unchanged OSTF 4.3 musical Core parameter reference** (127 `$defs`). The newly proposed **independently versioned** Production Session Profile 0.1.0 has its own 12 `$defs` and complete 61-property inventory in `PRODUCTION_PARAMETER_REFERENCE.md`. Mixer, device, asset, automation and host-extension fields MUST NOT be presented as additional root OSTF Core properties. The earlier Distributed Session Profile 0.2 continues to have its separate `SESSION_PARAMETER_REFERENCE.md`.


</details>


<details>
<summary>Inherited complete Production field reference</summary>

> **Current document edition: Draft 0.69 (unratified).** Older Draft headings and snapshot notes are retained as history. D01–D05 remain pending.

> **Historical editorial snapshot: Draft 0.59 (unratified).** Existing headings referring to earlier Drafts describe cumulative editorial proposals, not competing active document versions. The exact versioned Schemas remain unchanged; the single current release gate is RELEASE_READINESS.md (historical reference: `RELEASE_READINESS.md`). Publisher acceptance D01–D05 is still pending; runtime/independent tests are excluded, not passed.

# OSTF Production Session Profile 0.2.0 — Complete parameter reference (Draft 0.53 editorial edition; Schema unchanged)

Full schema-derived reference for Production Profile 0.2.0 including inherited 0.1 parameters and new Automation target branches. Schema authority: `schema/ostf-production-session-0.2.schema.json`; semantic authority: `docs/PRODUCTION_SESSION_PROFILE.md` §§1–30 (including later source/Visit, asset, version and cross-profile rules). This is a proposed non-ratified specification.

The Schema examples below are **exact source JSON definitions**. Structural validation alone cannot resolve Core Track/Score IDs, plugin ports or cross-object audio/automation references.

## Root

Optional studio companion profile; audio regions, sidechains and targeted Send/Region/Device-control automation. Descriptive data, not plug-in execution or DAW interoperability certification.

| Field | Required | Type | Constraints |
|---|---|---|---|
| `profile` | Yes | const OSTF-Production-Session |  |
| `profileVersion` | Yes | const 0.2.0 |  |
| `score` | Yes | ref score |  |
| `channels` | Yes | array | minItems=1; items:ref channel |
| `devices` | Optional / conditional | array | minItems=0; items:ref device |
| `assets` | Optional / conditional | array | minItems=0; items:ref asset |
| `automation` | Optional / conditional | array | minItems=0; items:ref automation |
| `notes` | Optional / conditional | string |  |
| `hostExtensions` | Optional / conditional | array | items:ref hostExtension |
| `audioRegions` | Optional / conditional | array | minItems=0; items:ref audioRegion; Optional authored audio-region arrangement in source-score global Tick time. Does not modify OSTF Core Clips/Notes. |
| `sidechainConnections` | Optional / conditional | array | minItems=0; items:ref sidechainConnection; Optional typed, acyclic audio detector/key inputs to effect plugin ports; not part of normal audible output routing. |

**Exact schema:**

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://yoh-nak.github.io/ostf/schema/ostf-production-session-0.2.schema.json",
  "title": "OSTF Production Session Profile 0.2.0 (Draft 0.15; not ratified)",
  "description": "Optional studio companion profile; audio regions, sidechains and targeted Send/Region/Device-control automation. Descriptive data, not plug-in execution or DAW interoperability certification.",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "profile": {
      "const": "OSTF-Production-Session"
    },
    "profileVersion": {
      "const": "0.2.0"
    },
    "score": {
      "$ref": "#/$defs/score"
    },
    "channels": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/channel"
      },
      "minItems": 1
    },
    "devices": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/device"
      },
      "minItems": 0
    },
    "assets": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/asset"
      },
      "minItems": 0
    },
    "automation": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/automation"
      },
      "minItems": 0
    },
    "notes": {
      "type": "string"
    },
    "hostExtensions": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/hostExtension"
      }
    },
    "audioRegions": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/audioRegion"
      },
      "minItems": 0,
      "description": "Optional authored audio-region arrangement in source-score global Tick time. Does not modify OSTF Core Clips/Notes."
    },
    "sidechainConnections": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/sidechainConnection"
      },
      "minItems": 0,
      "description": "Optional typed, acyclic audio detector/key inputs to effect plugin ports; not part of normal audible output routing."
    }
  },
  "required": [
    "profile",
    "profileVersion",
    "score",
    "channels"
  ],
  "$defs": {
    "id": {
      "type": "string",
      "minLength": 1,
      "pattern": "^\\S+$"
    },
    "sha256": {
      "type": "string",
      "pattern": "^[0-9a-f]{64}$"
    },
    "score": {
      "type": "object",
      "properties": {
        "formatVersion": {
          "const": "4.3.0"
        },
        "sha256": {
          "$ref": "#/$defs/sha256"
        },
        "documentId": {
          "$ref": "#/$defs/id"
        },
        "revisionId": {
          "$ref": "#/$defs/id"
        },
        "sourceUri": {
          "type": "string",
          "minLength": 1
        }
      },
      "required": [
        "formatVersion",
        "sha256"
      ],
      "additionalProperties": false
    },
    "channel": {
      "type": "object",
      "properties": {
        "id": {
          "$ref": "#/$defs/id"
        },
        "kind": {
          "enum": [
            "track",
            "audioTrack",
            "bus",
            "master"
          ],
          "description": "audioTrack is a production-only recorded-audio channel, and MUST NOT claim a Core trackId. kind track still maps an OSTF Track exactly as in 0.1."
        },
        "name": {
          "type": "string",
          "minLength": 1
        },
        "trackId": {
          "$ref": "#/$defs/id"
        },
        "audioChannels": {
          "enum": [
            1,
            2
          ]
        },
        "gainDb": {
          "type": "number",
          "minimum": -120,
          "maximum": 24
        },
        "pan": {
          "type": "number",
          "minimum": -1,
          "maximum": 1
        },
        "mute": {
          "type": "boolean"
        },
        "solo": {
          "type": "boolean"
        },
        "soloSafe": {
          "type": "boolean"
        },
        "outputChannelId": {
          "$ref": "#/$defs/id"
        },
        "deviceIds": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/id"
          },
          "minItems": 0,
          "uniqueItems": true
        },
        "sends": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/send"
          },
          "minItems": 0
        }
      },
      "required": [
        "id",
        "kind",
        "audioChannels",
        "gainDb",
        "pan",
        "mute",
        "solo",
        "soloSafe",
        "deviceIds"
      ],
      "additionalProperties": false
    },
    "send": {
      "type": "object",
      "properties": {
        "id": {
          "$ref": "#/$defs/id"
        },
        "targetChannelId": {
          "$ref": "#/$defs/id"
        },
        "gainDb": {
          "type": "number",
          "minimum": -120,
          "maximum": 24
        },
        "preFader": {
          "type": "boolean"
        },
        "enabled": {
          "type": "boolean"
        }
      },
      "required": [
        "id",
        "targetChannelId",
        "gainDb",
        "preFader",
        "enabled"
      ],
      "additionalProperties": false
    },
    "device": {
      "type": "object",
      "properties": {
        "id": {
          "$ref": "#/$defs/id"
        },
        "role": {
          "enum": [
            "instrument",
            "effect",
            "utility"
          ]
        },
        "plugin": {
          "$ref": "#/$defs/plugin"
        },
        "enabled": {
          "type": "boolean"
        },
        "bypass": {
          "type": "boolean"
        },
        "stateAssetId": {
          "$ref": "#/$defs/id"
        },
        "onUnavailable": {
          "enum": [
            "reportAndPreserve",
            "preserveAndBypass",
            "preserveAndSilence"
          ]
        }
      },
      "required": [
        "id",
        "role",
        "plugin",
        "enabled",
        "bypass"
      ],
      "additionalProperties": false
    },
    "plugin": {
      "type": "object",
      "properties": {
        "format": {
          "enum": [
            "vst2",
            "vst3",
            "clap",
            "au",
            "aax",
            "builtin",
            "hostNative",
            "other"
          ]
        },
        "pluginId": {
          "type": "string",
          "minLength": 1
        },
        "vendor": {
          "type": "string",
          "minLength": 1
        },
        "name": {
          "type": "string",
          "minLength": 1
        },
        "version": {
          "type": "string",
          "minLength": 1
        },
        "namespace": {
          "type": "string",
          "minLength": 1
        }
      },
      "required": [
        "format",
        "pluginId",
        "name"
      ],
      "additionalProperties": false
    },
    "asset": {
      "type": "object",
      "properties": {
        "id": {
          "$ref": "#/$defs/id"
        },
        "purpose": {
          "enum": [
            "pluginState",
            "renderedAudio",
            "other",
            "audioSource"
          ]
        },
        "uri": {
          "type": "string",
          "minLength": 1
        },
        "sha256": {
          "$ref": "#/$defs/sha256"
        },
        "mediaType": {
          "type": "string",
          "minLength": 1
        },
        "byteLength": {
          "type": "integer",
          "minimum": 0
        },
        "sampleRateHz": {
          "type": "integer",
          "minimum": 1,
          "maximum": 768000,
          "description": "Audio-source decoded sample frames per second; required only for purpose audioSource."
        },
        "frameCount": {
          "type": "integer",
          "minimum": 1,
          "description": "Number of decoded sample frames in the complete audio source asset; required for audioSource."
        },
        "audioChannels": {
          "type": "integer",
          "enum": [
            1,
            2
          ],
          "description": "Mono/stereo decoded source-channel count; required only for audioSource in 0.2."
        }
      },
      "required": [
        "id",
        "purpose",
        "uri",
        "sha256"
      ],
      "additionalProperties": false,
      "allOf": [
        {
          "if": {
            "properties": {
              "purpose": {
                "const": "audioSource"
              }
            },
            "required": [
              "purpose"
            ]
          },
          "then": {
            "required": [
              "sampleRateHz",
              "frameCount",
              "audioChannels",
              "mediaType"
            ]
          },
          "else": {
            "not": {
              "anyOf": [
                {
                  "required": [
                    "sampleRateHz"
                  ]
                },
                {
                  "required": [
                    "frameCount"
                  ]
                },
                {
                  "required": [
                    "audioChannels"
                  ]
                }
              ]
            }
          }
        }
      ],
      "description": "Opaque asset descriptors. audioSource requires sampling metadata for frame-accurate regions; plug-in state remains uninterpreted and never executable merely by presence in JSON."
    },
    "automation": {
      "type": "object",
      "properties": {
        "id": {
          "$ref": "#/$defs/id"
        },
        "target": {
          "$ref": "#/$defs/automationTarget"
        },
        "valueType": {
          "enum": [
            "number",
            "boolean"
          ]
        },
        "interpolation": {
          "enum": [
            "step",
            "linear"
          ]
        },
        "points": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/point"
          },
          "minItems": 1
        }
      },
      "required": [
        "id",
        "target",
        "valueType",
        "interpolation",
        "points"
      ],
      "additionalProperties": false,
      "description": "Unique source-global-Tick automation lane. Boolean controls use step interpolation. A single lane per exact target; static value acts as baseline before first point where available. Device plugin parameters are normalized 0..1, while deviceControl.enabled/bypass are explicit booleans.",
      "allOf": [
        {
          "if": {
            "properties": {
              "valueType": {
                "const": "boolean"
              }
            },
            "required": [
              "valueType"
            ]
          },
          "then": {
            "properties": {
              "interpolation": {
                "const": "step"
              }
            }
          }
        }
      ]
    },
    "automationTarget": {
      "oneOf": [
        {
          "type": "object",
          "properties": {
            "kind": {
              "const": "channel"
            },
            "channelId": {
              "$ref": "#/$defs/id"
            },
            "parameter": {
              "enum": [
                "gainDb",
                "pan",
                "mute"
              ]
            }
          },
          "required": [
            "kind",
            "channelId",
            "parameter"
          ],
          "additionalProperties": false
        },
        {
          "type": "object",
          "properties": {
            "kind": {
              "const": "device"
            },
            "deviceId": {
              "$ref": "#/$defs/id"
            },
            "parameterId": {
              "type": "string",
              "minLength": 1
            }
          },
          "required": [
            "kind",
            "deviceId",
            "parameterId"
          ],
          "additionalProperties": false
        },
        {
          "type": "object",
          "additionalProperties": false,
          "properties": {
            "kind": {
              "const": "send"
            },
            "sendId": {
              "$ref": "#/$defs/id"
            },
            "parameter": {
              "enum": [
                "gainDb",
                "enabled"
              ]
            }
          },
          "required": [
            "kind",
            "sendId",
            "parameter"
          ]
        },
        {
          "type": "object",
          "additionalProperties": false,
          "properties": {
            "kind": {
              "const": "audioRegion"
            },
            "audioRegionId": {
              "$ref": "#/$defs/id"
            },
            "parameter": {
              "enum": [
                "gainDb",
                "mute"
              ]
            }
          },
          "required": [
            "kind",
            "audioRegionId",
            "parameter"
          ]
        },
        {
          "type": "object",
          "additionalProperties": false,
          "properties": {
            "kind": {
              "const": "deviceControl"
            },
            "deviceId": {
              "$ref": "#/$defs/id"
            },
            "parameter": {
              "enum": [
                "enabled",
                "bypass"
              ]
            }
          },
          "required": [
            "kind",
            "deviceId",
            "parameter"
          ]
        }
      ],
      "description": "Channel, plugin parameter, Send, audio Region, or Device slot control automation target. Non-channel options added to the unpublished 0.2 development draft. References resolve within this Production Profile, not into MIDI CC or Core Note IDs."
    },
    "point": {
      "type": "object",
      "properties": {
        "atTick": {
          "type": "integer",
          "minimum": 0
        },
        "value": {
          "oneOf": [
            {
              "type": "number"
            },
            {
              "type": "boolean"
            }
          ]
        }
      },
      "required": [
        "atTick",
        "value"
      ],
      "additionalProperties": false
    },
    "hostExtension": {
      "type": "object",
      "properties": {
        "namespace": {
          "type": "string",
          "pattern": "^[A-Za-z0-9]+(?:\\.[A-Za-z0-9-]+)+$"
        },
        "version": {
          "type": "string",
          "minLength": 1
        },
        "data": {
          "type": "object"
        }
      },
      "required": [
        "namespace",
        "data"
      ],
      "additionalProperties": false
    },
    "audioRegion": {
      "type": "object",
      "additionalProperties": false,
      "description": "Source-score-tick audio segment on a production track or score-bound track channel, referencing a bounded range of exact audioSource PCM-decoded frames.",
      "properties": {
        "id": {
          "$ref": "#/$defs/id"
        },
        "channelId": {
          "$ref": "#/$defs/id"
        },
        "sourceAssetId": {
          "$ref": "#/$defs/id"
        },
        "startTick": {
          "type": "integer",
          "minimum": 0
        },
        "durationTicks": {
          "type": "integer",
          "minimum": 1
        },
        "sourceStartFrame": {
          "type": "integer",
          "minimum": 0
        },
        "sourceFrameCount": {
          "type": "integer",
          "minimum": 1
        },
        "playbackMode": {
          "enum": [
            "native",
            "fit"
          ],
          "description": "native maps ideal source-time seconds to sample frames at sampleRateHz; fit uniformly maps authored global Tick progress to the selected frame interval."
        },
        "pitchPolicy": {
          "enum": [
            "preserve",
            "followRate"
          ],
          "description": "Required for fit; preserve means retain source pitch as a musical goal, followRate means speed/rate-based pitch change. Both are DSP/host dependent."
        },
        "gainDb": {
          "type": "number",
          "minimum": -120,
          "maximum": 24
        },
        "mute": {
          "type": "boolean"
        },
        "fadeInTicks": {
          "type": "integer",
          "minimum": 0
        },
        "fadeOutTicks": {
          "type": "integer",
          "minimum": 0
        }
      },
      "required": [
        "id",
        "channelId",
        "sourceAssetId",
        "startTick",
        "durationTicks",
        "sourceStartFrame",
        "sourceFrameCount",
        "playbackMode",
        "gainDb",
        "mute"
      ],
      "allOf": [
        {
          "if": {
            "properties": {
              "playbackMode": {
                "const": "fit"
              }
            },
            "required": [
              "playbackMode"
            ]
          },
          "then": {
            "required": [
              "pitchPolicy"
            ]
          },
          "else": {
            "not": {
              "required": [
                "pitchPolicy"
              ]
            }
          }
        }
      ]
    },
    "sidechainConnection": {
      "type": "object",
      "additionalProperties": false,
      "description": "Directed detector/key signal from sourceChannelId to named key input port of an effect Device belonging to a different audio channel. Does not mix into its audible output path.",
      "properties": {
        "id": {
          "$ref": "#/$defs/id"
        },
        "sourceChannelId": {
          "$ref": "#/$defs/id"
        },
        "targetDeviceId": {
          "$ref": "#/$defs/id"
        },
        "targetPortId": {
          "$ref": "#/$defs/id",
          "description": "Opaque plugin-format-scoped sidechain input identifier. A host must verify the port actually exists; no port auto-matching by label."
        },
        "tapPoint": {
          "enum": [
            "preFader",
            "postFader"
          ]
        },
        "followMute": {
          "type": "boolean",
          "description": "If true, source channel mute suppresses this sidechain; if false, the detector feed can remain present even when that source channel is muted audibly."
        },
        "gainDb": {
          "type": "number",
          "minimum": -120,
          "maximum": 24
        },
        "enabled": {
          "type": "boolean"
        }
      },
      "required": [
        "id",
        "sourceChannelId",
        "targetDeviceId",
        "targetPortId",
        "tapPoint",
        "followMute",
        "gainDb",
        "enabled"
      ]
    }
  }
}
```

## $defs / id



| Field | Required | Type | Constraints |
|---|---|---|---|

**Exact schema:**

```json
{
  "type": "string",
  "minLength": 1,
  "pattern": "^\\S+$"
}
```

## $defs / sha256



| Field | Required | Type | Constraints |
|---|---|---|---|

**Exact schema:**

```json
{
  "type": "string",
  "pattern": "^[0-9a-f]{64}$"
}
```

## $defs / score



| Field | Required | Type | Constraints |
|---|---|---|---|
| `formatVersion` | Yes | const 4.3.0 |  |
| `sha256` | Yes | ref sha256 |  |
| `documentId` | Optional / conditional | ref id |  |
| `revisionId` | Optional / conditional | ref id |  |
| `sourceUri` | Optional / conditional | string | minLength=1 |

**Exact schema:**

```json
{
  "type": "object",
  "properties": {
    "formatVersion": {
      "const": "4.3.0"
    },
    "sha256": {
      "$ref": "#/$defs/sha256"
    },
    "documentId": {
      "$ref": "#/$defs/id"
    },
    "revisionId": {
      "$ref": "#/$defs/id"
    },
    "sourceUri": {
      "type": "string",
      "minLength": 1
    }
  },
  "required": [
    "formatVersion",
    "sha256"
  ],
  "additionalProperties": false
}
```

## $defs / channel



| Field | Required | Type | Constraints |
|---|---|---|---|
| `id` | Yes | ref id |  |
| `kind` | Yes | enum track, audioTrack, bus, master | audioTrack is a production-only recorded-audio channel, and MUST NOT claim a Core trackId. kind track still maps an OSTF |
| `name` | Optional / conditional | string | minLength=1 |
| `trackId` | Optional / conditional | ref id |  |
| `audioChannels` | Yes | enum 1, 2 |  |
| `gainDb` | Yes | number | minimum=-120; maximum=24 |
| `pan` | Yes | number | minimum=-1; maximum=1 |
| `mute` | Yes | boolean |  |
| `solo` | Yes | boolean |  |
| `soloSafe` | Yes | boolean |  |
| `outputChannelId` | Optional / conditional | ref id |  |
| `deviceIds` | Yes | array | minItems=0; uniqueItems=True; items:ref id |
| `sends` | Optional / conditional | array | minItems=0; items:ref send |

**Exact schema:**

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "kind": {
      "enum": [
        "track",
        "audioTrack",
        "bus",
        "master"
      ],
      "description": "audioTrack is a production-only recorded-audio channel, and MUST NOT claim a Core trackId. kind track still maps an OSTF Track exactly as in 0.1."
    },
    "name": {
      "type": "string",
      "minLength": 1
    },
    "trackId": {
      "$ref": "#/$defs/id"
    },
    "audioChannels": {
      "enum": [
        1,
        2
      ]
    },
    "gainDb": {
      "type": "number",
      "minimum": -120,
      "maximum": 24
    },
    "pan": {
      "type": "number",
      "minimum": -1,
      "maximum": 1
    },
    "mute": {
      "type": "boolean"
    },
    "solo": {
      "type": "boolean"
    },
    "soloSafe": {
      "type": "boolean"
    },
    "outputChannelId": {
      "$ref": "#/$defs/id"
    },
    "deviceIds": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/id"
      },
      "minItems": 0,
      "uniqueItems": true
    },
    "sends": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/send"
      },
      "minItems": 0
    }
  },
  "required": [
    "id",
    "kind",
    "audioChannels",
    "gainDb",
    "pan",
    "mute",
    "solo",
    "soloSafe",
    "deviceIds"
  ],
  "additionalProperties": false
}
```

## $defs / send



| Field | Required | Type | Constraints |
|---|---|---|---|
| `id` | Yes | ref id |  |
| `targetChannelId` | Yes | ref id |  |
| `gainDb` | Yes | number | minimum=-120; maximum=24 |
| `preFader` | Yes | boolean |  |
| `enabled` | Yes | boolean |  |

**Exact schema:**

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "targetChannelId": {
      "$ref": "#/$defs/id"
    },
    "gainDb": {
      "type": "number",
      "minimum": -120,
      "maximum": 24
    },
    "preFader": {
      "type": "boolean"
    },
    "enabled": {
      "type": "boolean"
    }
  },
  "required": [
    "id",
    "targetChannelId",
    "gainDb",
    "preFader",
    "enabled"
  ],
  "additionalProperties": false
}
```

## $defs / device



| Field | Required | Type | Constraints |
|---|---|---|---|
| `id` | Yes | ref id |  |
| `role` | Yes | enum instrument, effect, utility |  |
| `plugin` | Yes | ref plugin |  |
| `enabled` | Yes | boolean |  |
| `bypass` | Yes | boolean |  |
| `stateAssetId` | Optional / conditional | ref id |  |
| `onUnavailable` | Optional / conditional | enum reportAndPreserve, preserveAndBypass, preserveAndSilence |  |

**Exact schema:**

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "role": {
      "enum": [
        "instrument",
        "effect",
        "utility"
      ]
    },
    "plugin": {
      "$ref": "#/$defs/plugin"
    },
    "enabled": {
      "type": "boolean"
    },
    "bypass": {
      "type": "boolean"
    },
    "stateAssetId": {
      "$ref": "#/$defs/id"
    },
    "onUnavailable": {
      "enum": [
        "reportAndPreserve",
        "preserveAndBypass",
        "preserveAndSilence"
      ]
    }
  },
  "required": [
    "id",
    "role",
    "plugin",
    "enabled",
    "bypass"
  ],
  "additionalProperties": false
}
```

## $defs / plugin



| Field | Required | Type | Constraints |
|---|---|---|---|
| `format` | Yes | enum vst2, vst3, clap, au, aax, builtin, hostNative, other |  |
| `pluginId` | Yes | string | minLength=1 |
| `vendor` | Optional / conditional | string | minLength=1 |
| `name` | Yes | string | minLength=1 |
| `version` | Optional / conditional | string | minLength=1 |
| `namespace` | Optional / conditional | string | minLength=1 |

**Exact schema:**

```json
{
  "type": "object",
  "properties": {
    "format": {
      "enum": [
        "vst2",
        "vst3",
        "clap",
        "au",
        "aax",
        "builtin",
        "hostNative",
        "other"
      ]
    },
    "pluginId": {
      "type": "string",
      "minLength": 1
    },
    "vendor": {
      "type": "string",
      "minLength": 1
    },
    "name": {
      "type": "string",
      "minLength": 1
    },
    "version": {
      "type": "string",
      "minLength": 1
    },
    "namespace": {
      "type": "string",
      "minLength": 1
    }
  },
  "required": [
    "format",
    "pluginId",
    "name"
  ],
  "additionalProperties": false
}
```

## $defs / asset

Opaque asset descriptors. audioSource requires sampling metadata for frame-accurate regions; plug-in state remains uninterpreted and never executable merely by presence in JSON.

| Field | Required | Type | Constraints |
|---|---|---|---|
| `id` | Yes | ref id |  |
| `purpose` | Yes | enum pluginState, renderedAudio, other, audioSource |  |
| `uri` | Yes | string | minLength=1 |
| `sha256` | Yes | ref sha256 |  |
| `mediaType` | Optional / conditional | string | minLength=1 |
| `byteLength` | Optional / conditional | integer | minimum=0 |
| `sampleRateHz` | Optional / conditional | integer | minimum=1; maximum=768000; Audio-source decoded sample frames per second; required only for purpose audioSource. |
| `frameCount` | Optional / conditional | integer | minimum=1; Number of decoded sample frames in the complete audio source asset; required for audioSource. |
| `audioChannels` | Optional / conditional | enum 1, 2 | Mono/stereo decoded source-channel count; required only for audioSource in 0.2. |

**Exact schema:**

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "purpose": {
      "enum": [
        "pluginState",
        "renderedAudio",
        "other",
        "audioSource"
      ]
    },
    "uri": {
      "type": "string",
      "minLength": 1
    },
    "sha256": {
      "$ref": "#/$defs/sha256"
    },
    "mediaType": {
      "type": "string",
      "minLength": 1
    },
    "byteLength": {
      "type": "integer",
      "minimum": 0
    },
    "sampleRateHz": {
      "type": "integer",
      "minimum": 1,
      "maximum": 768000,
      "description": "Audio-source decoded sample frames per second; required only for purpose audioSource."
    },
    "frameCount": {
      "type": "integer",
      "minimum": 1,
      "description": "Number of decoded sample frames in the complete audio source asset; required for audioSource."
    },
    "audioChannels": {
      "type": "integer",
      "enum": [
        1,
        2
      ],
      "description": "Mono/stereo decoded source-channel count; required only for audioSource in 0.2."
    }
  },
  "required": [
    "id",
    "purpose",
    "uri",
    "sha256"
  ],
  "additionalProperties": false,
  "allOf": [
    {
      "if": {
        "properties": {
          "purpose": {
            "const": "audioSource"
          }
        },
        "required": [
          "purpose"
        ]
      },
      "then": {
        "required": [
          "sampleRateHz",
          "frameCount",
          "audioChannels",
          "mediaType"
        ]
      },
      "else": {
        "not": {
          "anyOf": [
            {
              "required": [
                "sampleRateHz"
              ]
            },
            {
              "required": [
                "frameCount"
              ]
            },
            {
              "required": [
                "audioChannels"
              ]
            }
          ]
        }
      }
    }
  ],
  "description": "Opaque asset descriptors. audioSource requires sampling metadata for frame-accurate regions; plug-in state remains uninterpreted and never executable merely by presence in JSON."
}
```

## $defs / automation

Unique source-global-Tick automation lane. Boolean controls use step interpolation. A single lane per exact target; static value acts as baseline before first point where available. Device plugin parameters are normalized 0..1, while deviceControl.enabled/bypass are explicit booleans.

| Field | Required | Type | Constraints |
|---|---|---|---|
| `id` | Yes | ref id |  |
| `target` | Yes | ref automationTarget |  |
| `valueType` | Yes | enum number, boolean |  |
| `interpolation` | Yes | enum step, linear |  |
| `points` | Yes | array | minItems=1; items:ref point |

**Exact schema:**

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "target": {
      "$ref": "#/$defs/automationTarget"
    },
    "valueType": {
      "enum": [
        "number",
        "boolean"
      ]
    },
    "interpolation": {
      "enum": [
        "step",
        "linear"
      ]
    },
    "points": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/point"
      },
      "minItems": 1
    }
  },
  "required": [
    "id",
    "target",
    "valueType",
    "interpolation",
    "points"
  ],
  "additionalProperties": false,
  "description": "Unique source-global-Tick automation lane. Boolean controls use step interpolation. A single lane per exact target; static value acts as baseline before first point where available. Device plugin parameters are normalized 0..1, while deviceControl.enabled/bypass are explicit booleans.",
  "allOf": [
    {
      "if": {
        "properties": {
          "valueType": {
            "const": "boolean"
          }
        },
        "required": [
          "valueType"
        ]
      },
      "then": {
        "properties": {
          "interpolation": {
            "const": "step"
          }
        }
      }
    }
  ]
}
```

## $defs / automationTarget

Channel, plugin parameter, Send, audio Region, or Device slot control automation target. Non-channel options added to the unpublished 0.2 development draft. References resolve within this Production Profile, not into MIDI CC or Core Note IDs.

| Field | Required | Type | Constraints |
|---|---|---|---|

**Exact schema:**

```json
{
  "oneOf": [
    {
      "type": "object",
      "properties": {
        "kind": {
          "const": "channel"
        },
        "channelId": {
          "$ref": "#/$defs/id"
        },
        "parameter": {
          "enum": [
            "gainDb",
            "pan",
            "mute"
          ]
        }
      },
      "required": [
        "kind",
        "channelId",
        "parameter"
      ],
      "additionalProperties": false
    },
    {
      "type": "object",
      "properties": {
        "kind": {
          "const": "device"
        },
        "deviceId": {
          "$ref": "#/$defs/id"
        },
        "parameterId": {
          "type": "string",
          "minLength": 1
        }
      },
      "required": [
        "kind",
        "deviceId",
        "parameterId"
      ],
      "additionalProperties": false
    },
    {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "kind": {
          "const": "send"
        },
        "sendId": {
          "$ref": "#/$defs/id"
        },
        "parameter": {
          "enum": [
            "gainDb",
            "enabled"
          ]
        }
      },
      "required": [
        "kind",
        "sendId",
        "parameter"
      ]
    },
    {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "kind": {
          "const": "audioRegion"
        },
        "audioRegionId": {
          "$ref": "#/$defs/id"
        },
        "parameter": {
          "enum": [
            "gainDb",
            "mute"
          ]
        }
      },
      "required": [
        "kind",
        "audioRegionId",
        "parameter"
      ]
    },
    {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "kind": {
          "const": "deviceControl"
        },
        "deviceId": {
          "$ref": "#/$defs/id"
        },
        "parameter": {
          "enum": [
            "enabled",
            "bypass"
          ]
        }
      },
      "required": [
        "kind",
        "deviceId",
        "parameter"
      ]
    }
  ],
  "description": "Channel, plugin parameter, Send, audio Region, or Device slot control automation target. Non-channel options added to the unpublished 0.2 development draft. References resolve within this Production Profile, not into MIDI CC or Core Note IDs."
}
```

## $defs / point



| Field | Required | Type | Constraints |
|---|---|---|---|
| `atTick` | Yes | integer | minimum=0 |
| `value` | Yes | oneOf (2 alternatives) |  |

**Exact schema:**

```json
{
  "type": "object",
  "properties": {
    "atTick": {
      "type": "integer",
      "minimum": 0
    },
    "value": {
      "oneOf": [
        {
          "type": "number"
        },
        {
          "type": "boolean"
        }
      ]
    }
  },
  "required": [
    "atTick",
    "value"
  ],
  "additionalProperties": false
}
```

## $defs / hostExtension



| Field | Required | Type | Constraints |
|---|---|---|---|
| `namespace` | Yes | string | pattern=^[A-Za-z0-9]+(?:\.[A-Za-z0-9-]+)+$ |
| `version` | Optional / conditional | string | minLength=1 |
| `data` | Yes | object |  |

**Exact schema:**

```json
{
  "type": "object",
  "properties": {
    "namespace": {
      "type": "string",
      "pattern": "^[A-Za-z0-9]+(?:\\.[A-Za-z0-9-]+)+$"
    },
    "version": {
      "type": "string",
      "minLength": 1
    },
    "data": {
      "type": "object"
    }
  },
  "required": [
    "namespace",
    "data"
  ],
  "additionalProperties": false
}
```

## $defs / audioRegion

Source-score-tick audio segment on a production track or score-bound track channel, referencing a bounded range of exact audioSource PCM-decoded frames.

| Field | Required | Type | Constraints |
|---|---|---|---|
| `id` | Yes | ref id |  |
| `channelId` | Yes | ref id |  |
| `sourceAssetId` | Yes | ref id |  |
| `startTick` | Yes | integer | minimum=0 |
| `durationTicks` | Yes | integer | minimum=1 |
| `sourceStartFrame` | Yes | integer | minimum=0 |
| `sourceFrameCount` | Yes | integer | minimum=1 |
| `playbackMode` | Yes | enum native, fit | native maps ideal source-time seconds to sample frames at sampleRateHz; fit uniformly maps authored global Tick progress |
| `pitchPolicy` | Optional / conditional | enum preserve, followRate | Required for fit; preserve means retain source pitch as a musical goal, followRate means speed/rate-based pitch change.  |
| `gainDb` | Yes | number | minimum=-120; maximum=24 |
| `mute` | Yes | boolean |  |
| `fadeInTicks` | Optional / conditional | integer | minimum=0 |
| `fadeOutTicks` | Optional / conditional | integer | minimum=0 |

**Exact schema:**

```json
{
  "type": "object",
  "additionalProperties": false,
  "description": "Source-score-tick audio segment on a production track or score-bound track channel, referencing a bounded range of exact audioSource PCM-decoded frames.",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "channelId": {
      "$ref": "#/$defs/id"
    },
    "sourceAssetId": {
      "$ref": "#/$defs/id"
    },
    "startTick": {
      "type": "integer",
      "minimum": 0
    },
    "durationTicks": {
      "type": "integer",
      "minimum": 1
    },
    "sourceStartFrame": {
      "type": "integer",
      "minimum": 0
    },
    "sourceFrameCount": {
      "type": "integer",
      "minimum": 1
    },
    "playbackMode": {
      "enum": [
        "native",
        "fit"
      ],
      "description": "native maps ideal source-time seconds to sample frames at sampleRateHz; fit uniformly maps authored global Tick progress to the selected frame interval."
    },
    "pitchPolicy": {
      "enum": [
        "preserve",
        "followRate"
      ],
      "description": "Required for fit; preserve means retain source pitch as a musical goal, followRate means speed/rate-based pitch change. Both are DSP/host dependent."
    },
    "gainDb": {
      "type": "number",
      "minimum": -120,
      "maximum": 24
    },
    "mute": {
      "type": "boolean"
    },
    "fadeInTicks": {
      "type": "integer",
      "minimum": 0
    },
    "fadeOutTicks": {
      "type": "integer",
      "minimum": 0
    }
  },
  "required": [
    "id",
    "channelId",
    "sourceAssetId",
    "startTick",
    "durationTicks",
    "sourceStartFrame",
    "sourceFrameCount",
    "playbackMode",
    "gainDb",
    "mute"
  ],
  "allOf": [
    {
      "if": {
        "properties": {
          "playbackMode": {
            "const": "fit"
          }
        },
        "required": [
          "playbackMode"
        ]
      },
      "then": {
        "required": [
          "pitchPolicy"
        ]
      },
      "else": {
        "not": {
          "required": [
            "pitchPolicy"
          ]
        }
      }
    }
  ]
}
```

## $defs / sidechainConnection

Directed detector/key signal from sourceChannelId to named key input port of an effect Device belonging to a different audio channel. Does not mix into its audible output path.

| Field | Required | Type | Constraints |
|---|---|---|---|
| `id` | Yes | ref id |  |
| `sourceChannelId` | Yes | ref id |  |
| `targetDeviceId` | Yes | ref id |  |
| `targetPortId` | Yes | ref id | Opaque plugin-format-scoped sidechain input identifier. A host must verify the port actually exists; no port auto-matchi |
| `tapPoint` | Yes | enum preFader, postFader |  |
| `followMute` | Yes | boolean | If true, source channel mute suppresses this sidechain; if false, the detector feed can remain present even when that so |
| `gainDb` | Yes | number | minimum=-120; maximum=24 |
| `enabled` | Yes | boolean |  |

**Exact schema:**

```json
{
  "type": "object",
  "additionalProperties": false,
  "description": "Directed detector/key signal from sourceChannelId to named key input port of an effect Device belonging to a different audio channel. Does not mix into its audible output path.",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "sourceChannelId": {
      "$ref": "#/$defs/id"
    },
    "targetDeviceId": {
      "$ref": "#/$defs/id"
    },
    "targetPortId": {
      "$ref": "#/$defs/id",
      "description": "Opaque plugin-format-scoped sidechain input identifier. A host must verify the port actually exists; no port auto-matching by label."
    },
    "tapPoint": {
      "enum": [
        "preFader",
        "postFader"
      ]
    },
    "followMute": {
      "type": "boolean",
      "description": "If true, source channel mute suppresses this sidechain; if false, the detector feed can remain present even when that source channel is muted audibly."
    },
    "gainDb": {
      "type": "number",
      "minimum": -120,
      "maximum": 24
    },
    "enabled": {
      "type": "boolean"
    }
  },
  "required": [
    "id",
    "sourceChannelId",
    "targetDeviceId",
    "targetPortId",
    "tapPoint",
    "followMute",
    "gainDb",
    "enabled"
  ]
}
```

## Automation target compatibility — Draft 0.15

| Kind | Identifier | Parameter / value type | Introduced |
|---|---|---|---|
| `channel` | `channelId` | gainDb number, pan number, mute boolean | 0.1 |
| `device` | `deviceId` | plugin parameterId normalized number | 0.1 |
| `send` | `sendId` | gainDb number, enabled boolean | 0.2 pre-release |
| `audioRegion` | `audioRegionId` | gainDb number, mute boolean | 0.2 pre-release |
| `deviceControl` | `deviceId` | enabled boolean, bypass boolean | 0.2 pre-release |

Boolean lanes MUST use step; each full typed target MUST have at most one lane; points are source-score global ticks and recur under source Visit repeats. References, scalar parameter ranges, and source lifetime behavior require semantic validation. A 0.2 → 0.1 downgrade loses all lanes with new target kinds; disclose each lane ID.

## Cross-object semantic checks

- Exactly one Master, unique Channel/Device/Asset/Send/Region/Automation IDs, and one ownership per Device chain.
- Score-bound `trackId` resolves to Core Track; `audioTrack` has none; score SHA-256 pins exact original bytes.
- Audio Region references valid audioSource and channel; frame range, channel count, and fades are bounded.
- Output/Send/Sidechain dependency graph is acyclic, and a sidechain target is an owned effect device port.
- All Automation Target references resolve; type/interpolation/value range and unique target/point-order constraints apply.
- URI strings are data; external resources or plug-ins are never automatically fetched/executed.
- Runtime DSP/audio restoration and independent DAW/plugin compatibility are NOT certified.


## Draft 0.16 — interpretation of existing Mixer flags (no new parameters)

`channels[].solo` and `channels[].soloSafe` remain required booleans in the 0.2 Schema; neither becomes a new Automation target. `solo` on source Channels selects those sources; `solo` on a Bus selects source Channels reaching the Bus through current enabled sends/outputs; source `soloSafe` keeps that source selected during Solo; Bus `soloSafe` only keeps an already-selected routed signal eligible and is not an unconditional upstream source selector. Master Solo/SoloSafe do not select sources. Channel `mute` is stronger than Solo for audible output. `track.enabled` of Core is limited to Score-derived content, independent Production audio Regions remain subject to Region and Channel mute. See `PRODUCTION_SESSION_PROFILE.md` §22 for the complete candidate algorithm and host deviation reporting. A local asset URI must resolve inside the Profile's directory after symbolic-link resolution. No Schema field, enum, requiredness or other `$defs` entry changed in Draft 0.16.

## Draft 0.17 — Interpretation of `assets[].uri` (no new properties)

The original `uri` string is the authoritative serialized value. Production Profile 0.2's additional portable rule is strictly once-decoded UTF-8 POSIX URI path segments for *relative* Asset references, bundle-root/symlink containment and rejection of decoded dot segments, encoded separators, residual percent escapes, invalid UTF-8 and platform-reserved filenames. `safe_asset_uri` in the bundled helper is an authoring aid, not an operating-system security guarantee. For examples and the precise rule see `PRODUCTION_SESSION_PROFILE.md` §23.1. No numeric field, enum, `$defs` count or Schema property is changed by Draft 0.17.

`performancePlans[].visits[].parts[].realization` is owned by Music Core, not by any production audio Region; see Production Specification §23.2. An explicitly authored Region remains independent of a Score `silent` Part.

## Draft 0.18 — Interpretation note (no changes to field declarations)

All Profile 0.2 parameter names, requiredness, value ranges and `$defs` are unchanged. `audioRegions[].startTick`, `durationTicks`, `sourceStartFrame`, `sourceFrameCount`, `playbackMode`, `fadeInTicks` and `fadeOutTicks` are interpreted against original source Score Tick even when finite Performance Plans skip or repeat ranges. `automation[].points[].atTick` is likewise source-global. Values are re-evaluated from the whole lane on each selected source Tick; before the first point an opaque `kind:"device"` numeric parameter cannot be determined from the typed Profile alone. Detailed proposed normative semantics: `PRODUCTION_SESSION_PROFILE.md` §24 / `PRODUCTION_SESSION_PROFILE.ja.md` §24. No schema changes or app runtime guarantees are implied.


</details>


<details>
<summary>Inherited complete Distributed field reference</summary>

> **Current document edition: Draft 0.69 (unratified).** Older Draft headings and snapshot notes are retained as history. D01–D05 remain pending.

> **Historical editorial snapshot: Draft 0.59 (unratified).** Existing headings referring to earlier Drafts describe cumulative editorial proposals, not competing active document versions. The exact versioned Schemas remain unchanged; the single current release gate is RELEASE_READINESS.md (historical reference: `RELEASE_READINESS.md`). Publisher acceptance D01–D05 is still pending; runtime/independent tests are excluded, not passed.

# OSTF Distributed Session Profile 0.2 — Full Parameter Reference (Draft 0.53 editorial edition; Schema unchanged)

**Unratified development specification.** These fields belong to a separate JSON profile, never in `.ostf` Core.

Structural authority: `schema/ostf-distributed-session-0.2.schema.json`.
Semantic authority: `docs/SESSION_STATE_MACHINE.md` and `docs/SESSION_PROFILE.md`.

The root is `oneOf` Snapshot or Event. Both **require** `performancePlanId` and `scoreSha256`; an optional nested Position must reference the same Plan. `scoreSha256` is a lowercase 64-digit digest of the **exact original UTF-8 OSTF source bytes**, not a semantic hash.

## All definitions (including nested payloads)

## `id`

No object properties (primitive or union).

**Complete JSON Schema definition:**

```json
{
  "type": "string",
  "minLength": 1
}
```

## `participant`

| Field | Type/schema summary | Direct required |
| --- | --- | --- |
| `participantId` | `{"$ref":"#/$defs/id"}` | Yes |
| `kind` | `{"enum":["human","softwareAgent","physicalRobot"]}` | Yes |
| `assignedTrackIds` | `{"type":"array","items":{"$ref":"#/$defs/id"},"uniqueItems":true}` | Yes |
| `supportedFeatures` | `{"type":"array","items":{"type":"string","minLength":1},"uniqueItems":true}` | No/Conditional |
| `capabilities` | `{"type":"object","description":"Untrusted advisory data, not robot actuator authorization","additionalProperties":true}` | No/Conditional |

**Complete JSON Schema definition:**

```json
{
  "type": "object",
  "properties": {
    "participantId": {
      "$ref": "#/$defs/id"
    },
    "kind": {
      "enum": [
        "human",
        "softwareAgent",
        "physicalRobot"
      ]
    },
    "assignedTrackIds": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/id"
      },
      "uniqueItems": true
    },
    "supportedFeatures": {
      "type": "array",
      "items": {
        "type": "string",
        "minLength": 1
      },
      "uniqueItems": true
    },
    "capabilities": {
      "type": "object",
      "description": "Untrusted advisory data, not robot actuator authorization",
      "additionalProperties": true
    }
  },
  "required": [
    "participantId",
    "kind",
    "assignedTrackIds"
  ],
  "additionalProperties": false
}
```

## `position`

| Field | Type/schema summary | Direct required |
| --- | --- | --- |
| `performancePlanId` | `{"$ref":"#/$defs/id"}` | Yes |
| `visitId` | `{"$ref":"#/$defs/id"}` | Yes |
| `sourceTick` | `{"type":"integer","minimum":0}` | Yes |
| `performanceTick` | `{"type":"integer","minimum":0}` | Yes |
| `clockDomainId` | `{"$ref":"#/$defs/id"}` | Yes |
| `epochUtc` | `{"type":"string","format":"date-time"}` | Yes |
| `uncertaintyMs` | `{"type":"number","minimum":0}` | Yes |
| `tempoBpm` | `{"type":"number","exclusiveMinimum":0}` | No/Conditional |

**Complete JSON Schema definition:**

```json
{
  "type": "object",
  "properties": {
    "performancePlanId": {
      "$ref": "#/$defs/id"
    },
    "visitId": {
      "$ref": "#/$defs/id"
    },
    "sourceTick": {
      "type": "integer",
      "minimum": 0
    },
    "performanceTick": {
      "type": "integer",
      "minimum": 0
    },
    "clockDomainId": {
      "$ref": "#/$defs/id"
    },
    "epochUtc": {
      "type": "string",
      "format": "date-time"
    },
    "uncertaintyMs": {
      "type": "number",
      "minimum": 0
    },
    "tempoBpm": {
      "type": "number",
      "exclusiveMinimum": 0
    }
  },
  "required": [
    "performancePlanId",
    "visitId",
    "sourceTick",
    "performanceTick",
    "clockDomainId",
    "epochUtc",
    "uncertaintyMs"
  ],
  "additionalProperties": false,
  "description": "epochUtc denotes the clock-domain estimate for the explicitly stated performanceTick (at the sourceTick). Clock synchronization algorithm is out of scope."
}
```

## `note`

| Field | Type/schema summary | Direct required |
| --- | --- | --- |
| `startTick` | `{"type":"integer","minimum":0}` | Yes |
| `durationTicks` | `{"type":"integer","minimum":1}` | Yes |
| `pitch` | `{"type":"integer","minimum":0,"maximum":127}` | Yes |
| `velocity` | `{"type":"integer","minimum":1,"maximum":127}` | Yes |

**Complete JSON Schema definition:**

```json
{
  "type": "object",
  "properties": {
    "startTick": {
      "type": "integer",
      "minimum": 0
    },
    "durationTicks": {
      "type": "integer",
      "minimum": 1
    },
    "pitch": {
      "type": "integer",
      "minimum": 0,
      "maximum": 127
    },
    "velocity": {
      "type": "integer",
      "minimum": 1,
      "maximum": 127
    }
  },
  "required": [
    "startTick",
    "durationTicks",
    "pitch",
    "velocity"
  ],
  "additionalProperties": false,
  "description": "MIDI-like note within a proposed session phrase, not a new authoritative OSTF Core Note."
}
```

## `phrase`

| Field | Type/schema summary | Direct required |
| --- | --- | --- |
| `representation` | `{"const":"midi1Notes"}` | Yes |
| `durationTicks` | `{"type":"integer","minimum":1}` | Yes |
| `notes` | `{"type":"array","items":{"$ref":"#/$defs/note"},"minItems":1}` | Yes |

**Complete JSON Schema definition:**

```json
{
  "type": "object",
  "properties": {
    "representation": {
      "const": "midi1Notes"
    },
    "durationTicks": {
      "type": "integer",
      "minimum": 1
    },
    "notes": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/note"
      },
      "minItems": 1
    }
  },
  "required": [
    "representation",
    "durationTicks",
    "notes"
  ],
  "additionalProperties": false,
  "description": "A portable minimal pitched-note session phrase. No lyrics, MPE, instrument actuation or audio realization is implied. Notes are relative to phrase start/effectivePerformanceTick."
}
```

## `committedPhrase`

| Field | Type/schema summary | Direct required |
| --- | --- | --- |
| `commitEventId` | `{"$ref":"#/$defs/id"}` | Yes |
| `proposalId` | `{"$ref":"#/$defs/id"}` | Yes |
| `targetTrackId` | `{"$ref":"#/$defs/id"}` | Yes |
| `effectivePerformanceTick` | `{"type":"integer","minimum":0}` | Yes |
| `phrase` | `{"$ref":"#/$defs/phrase"}` | Yes |

**Complete JSON Schema definition:**

```json
{
  "type": "object",
  "properties": {
    "commitEventId": {
      "$ref": "#/$defs/id"
    },
    "proposalId": {
      "$ref": "#/$defs/id"
    },
    "targetTrackId": {
      "$ref": "#/$defs/id"
    },
    "effectivePerformanceTick": {
      "type": "integer",
      "minimum": 0
    },
    "phrase": {
      "$ref": "#/$defs/phrase"
    }
  },
  "required": [
    "commitEventId",
    "proposalId",
    "targetTrackId",
    "effectivePerformanceTick",
    "phrase"
  ],
  "additionalProperties": false
}
```

## `snapshot`

| Field | Type/schema summary | Direct required |
| --- | --- | --- |
| `profile` | `{"const":"OSTF-Distributed-Session-0.2"}` | Yes |
| `recordType` | `{"const":"snapshot"}` | Yes |
| `sessionId` | `{"$ref":"#/$defs/id"}` | Yes |
| `documentId` | `{"$ref":"#/$defs/id"}` | Yes |
| `revisionId` | `{"$ref":"#/$defs/id"}` | Yes |
| `performancePlanId` | `{"$ref":"#/$defs/id","description":"Required pinned finite 4.3 Core performancePlans[].id, also in prepared or stopped Snapshots; positions must match this ID."}` | Yes |
| `scoreSha256` | `{"type":"string","pattern":"^[0-9a-f]{64}$","description":"SHA-256 lowercase hex over the exact UTF-8 OSTF source document bytes after HTTP Content-Encoding removal and before parsing; byte identity pin only, not authentication or semantic normalization."}` | Yes |
| `sessionStatus` | `{"enum":["prepared","playing","stopped"],"description":"Authoritative session lifecycle state; not participant availability or network connection status."}` | Yes |
| `stateRevision` | `{"type":"integer","minimum":0}` | Yes |
| `authorityParticipantId` | `{"$ref":"#/$defs/id"}` | Yes |
| `participants` | `{"type":"array","items":{"$ref":"#/$defs/participant"},"minItems":1}` | Yes |
| `position` | `{"$ref":"#/$defs/position"}` | No/Conditional |
| `committedPhrases` | `{"type":"array","items":{"$ref":"#/$defs/committedPhrase"},"description":"Self-contained accepted phrases for late joiners; only active/future material is required for live join, full archive required for full replay claims."}` | No/Conditional |
| `commitmentWindow` | `{"$ref":"#/$defs/commitmentWindow","description":"Optional truthful late-join phrase completeness assertion. Only allowed in playing Snapshots with position; absent means no completeness claim, not an empty session."}` | No/Conditional |

**Complete JSON Schema definition:**

```json
{
  "type": "object",
  "properties": {
    "profile": {
      "const": "OSTF-Distributed-Session-0.2"
    },
    "recordType": {
      "const": "snapshot"
    },
    "sessionId": {
      "$ref": "#/$defs/id"
    },
    "documentId": {
      "$ref": "#/$defs/id"
    },
    "revisionId": {
      "$ref": "#/$defs/id"
    },
    "performancePlanId": {
      "$ref": "#/$defs/id",
      "description": "Required pinned finite 4.3 Core performancePlans[].id, also in prepared or stopped Snapshots; positions must match this ID."
    },
    "scoreSha256": {
      "type": "string",
      "pattern": "^[0-9a-f]{64}$",
      "description": "SHA-256 lowercase hex over the exact UTF-8 OSTF source document bytes after HTTP Content-Encoding removal and before parsing; byte identity pin only, not authentication or semantic normalization."
    },
    "sessionStatus": {
      "enum": [
        "prepared",
        "playing",
        "stopped"
      ],
      "description": "Authoritative session lifecycle state; not participant availability or network connection status."
    },
    "stateRevision": {
      "type": "integer",
      "minimum": 0
    },
    "authorityParticipantId": {
      "$ref": "#/$defs/id"
    },
    "participants": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/participant"
      },
      "minItems": 1
    },
    "position": {
      "$ref": "#/$defs/position"
    },
    "committedPhrases": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/committedPhrase"
      },
      "description": "Self-contained accepted phrases for late joiners; only active/future material is required for live join, full archive required for full replay claims."
    },
    "commitmentWindow": {
      "$ref": "#/$defs/commitmentWindow",
      "description": "Optional truthful late-join phrase completeness assertion. Only allowed in playing Snapshots with position; absent means no completeness claim, not an empty session."
    }
  },
  "required": [
    "profile",
    "recordType",
    "sessionId",
    "documentId",
    "revisionId",
    "performancePlanId",
    "scoreSha256",
    "sessionStatus",
    "stateRevision",
    "authorityParticipantId",
    "participants"
  ],
  "additionalProperties": false,
  "allOf": [
    {
      "if": {
        "properties": {
          "sessionStatus": {
            "const": "playing"
          }
        },
        "required": [
          "sessionStatus"
        ]
      },
      "then": {
        "required": [
          "position"
        ]
      }
    },
    {
      "if": {
        "required": [
          "commitmentWindow"
        ]
      },
      "then": {
        "required": [
          "position",
          "committedPhrases"
        ],
        "properties": {
          "sessionStatus": {
            "const": "playing"
          }
        }
      }
    }
  ],
  "description": "A playing Session Snapshot must have a pinned Plan/Visit clock position. Prepared/stopped may omit position. Only the current authority can certify an authoritative Snapshot. Draft 0.5: commitmentWindow asserts complete accepted phrase coverage as of stateRevision; absence makes no completeness guarantee. Draft 0.9 requires a pinned Plan and exact score-byte digest on every 0.2 Snapshot/Event, including positionless prepared snapshots. Draft 0.12: a Snapshot has at least one Participant so the required authority identity can resolve."
}
```

## `phraseProposedPayload`

| Field | Type/schema summary | Direct required |
| --- | --- | --- |
| `proposalId` | `{"$ref":"#/$defs/id"}` | Yes |
| `targetTrackId` | `{"$ref":"#/$defs/id"}` | Yes |
| `phrase` | `{"$ref":"#/$defs/phrase"}` | Yes |

**Complete JSON Schema definition:**

```json
{
  "type": "object",
  "properties": {
    "proposalId": {
      "$ref": "#/$defs/id"
    },
    "targetTrackId": {
      "$ref": "#/$defs/id"
    },
    "phrase": {
      "$ref": "#/$defs/phrase"
    }
  },
  "required": [
    "proposalId",
    "targetTrackId",
    "phrase"
  ],
  "additionalProperties": false
}
```

## `phraseCommittedPayload`

| Field | Type/schema summary | Direct required |
| --- | --- | --- |
| `proposalId` | `{"$ref":"#/$defs/id"}` | Yes |
| `targetTrackId` | `{"$ref":"#/$defs/id"}` | Yes |
| `phrase` | `{"$ref":"#/$defs/phrase"}` | Yes |

**Complete JSON Schema definition:**

```json
{
  "type": "object",
  "properties": {
    "proposalId": {
      "$ref": "#/$defs/id"
    },
    "targetTrackId": {
      "$ref": "#/$defs/id"
    },
    "phrase": {
      "$ref": "#/$defs/phrase"
    }
  },
  "required": [
    "proposalId",
    "targetTrackId",
    "phrase"
  ],
  "additionalProperties": false
}
```

## `turnRequestedPayload`

| Field | Type/schema summary | Direct required |
| --- | --- | --- |
| `targetTrackId` | `{"$ref":"#/$defs/id"}` | Yes |
| `requestedRole` | `{"type":"string","minLength":1}` | Yes |
| `requestedVisitId` | `{"$ref":"#/$defs/id"}` | No/Conditional |

**Complete JSON Schema definition:**

```json
{
  "type": "object",
  "properties": {
    "targetTrackId": {
      "$ref": "#/$defs/id"
    },
    "requestedRole": {
      "type": "string",
      "minLength": 1
    },
    "requestedVisitId": {
      "$ref": "#/$defs/id"
    }
  },
  "required": [
    "targetTrackId",
    "requestedRole"
  ],
  "additionalProperties": false
}
```

## `cueIssuedPayload`

| Field | Type/schema summary | Direct required |
| --- | --- | --- |
| `cueId` | `{"$ref":"#/$defs/id"}` | Yes |
| `targetVisitId` | `{"$ref":"#/$defs/id"}` | No/Conditional |

**Complete JSON Schema definition:**

```json
{
  "type": "object",
  "properties": {
    "cueId": {
      "$ref": "#/$defs/id"
    },
    "targetVisitId": {
      "$ref": "#/$defs/id"
    }
  },
  "required": [
    "cueId"
  ],
  "additionalProperties": false
}
```

## `performanceObservedPayload`

| Field | Type/schema summary | Direct required |
| --- | --- | --- |
| `observedParticipantId` | `{"$ref":"#/$defs/id"}` | Yes |
| `sourceTrackId` | `{"$ref":"#/$defs/id"}` | Yes |
| `confidence` | `{"type":"number","minimum":0,"maximum":1}` | Yes |
| `features` | `{"type":"object","additionalProperties":true}` | No/Conditional |

**Complete JSON Schema definition:**

```json
{
  "type": "object",
  "properties": {
    "observedParticipantId": {
      "$ref": "#/$defs/id"
    },
    "sourceTrackId": {
      "$ref": "#/$defs/id"
    },
    "confidence": {
      "type": "number",
      "minimum": 0,
      "maximum": 1
    },
    "features": {
      "type": "object",
      "additionalProperties": true
    }
  },
  "required": [
    "observedParticipantId",
    "sourceTrackId",
    "confidence"
  ],
  "additionalProperties": false
}
```

## `participantStatusPayload`

| Field | Type/schema summary | Direct required |
| --- | --- | --- |
| `participantId` | `{"$ref":"#/$defs/id"}` | Yes |
| `availability` | `{"enum":["ready","busy","disconnected"]}` | Yes |
| `message` | `{"type":"string"}` | No/Conditional |

**Complete JSON Schema definition:**

```json
{
  "type": "object",
  "properties": {
    "participantId": {
      "$ref": "#/$defs/id"
    },
    "availability": {
      "enum": [
        "ready",
        "busy",
        "disconnected"
      ]
    },
    "message": {
      "type": "string"
    }
  },
  "required": [
    "participantId",
    "availability"
  ],
  "additionalProperties": false
}
```

## `sessionStateChangedPayload`

| Field | Type/schema summary | Direct required |
| --- | --- | --- |
| `changeKind` | `{"enum":["sessionStarted","visitChanged","assignmentChanged","sessionStopped"]}` | Yes |
| `targetVisitId` | `{"$ref":"#/$defs/id"}` | No/Conditional |
| `participantId` | `{"$ref":"#/$defs/id"}` | No/Conditional |
| `assignedTrackIds` | `{"type":"array","items":{"$ref":"#/$defs/id"},"uniqueItems":true}` | No/Conditional |
| `position` | `{"$ref":"#/$defs/position","description":"Authoritative anchored musical/clock position for prepared-to-playing transition; position.performanceTick MUST equal enclosing effectivePerformanceTick (semantic rule)."}` | No/Conditional |

**Complete JSON Schema definition:**

```json
{
  "type": "object",
  "properties": {
    "changeKind": {
      "enum": [
        "sessionStarted",
        "visitChanged",
        "assignmentChanged",
        "sessionStopped"
      ]
    },
    "targetVisitId": {
      "$ref": "#/$defs/id"
    },
    "participantId": {
      "$ref": "#/$defs/id"
    },
    "assignedTrackIds": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/id"
      },
      "uniqueItems": true
    },
    "position": {
      "$ref": "#/$defs/position",
      "description": "Authoritative Plan/Visit/source/performance Tick and clock-domain/UTC anchor. Required for sessionStarted and visitChanged; position.performanceTick MUST equal event effectivePerformanceTick. For visitChanged, position.visitId MUST equal targetVisitId at that Visit start."
    }
  },
  "required": [
    "changeKind"
  ],
  "additionalProperties": false,
  "allOf": [
    {
      "if": {
        "properties": {
          "changeKind": {
            "const": "sessionStarted"
          }
        },
        "required": [
          "changeKind"
        ]
      },
      "then": {
        "required": [
          "position"
        ],
        "not": {
          "anyOf": [
            {
              "required": [
                "targetVisitId"
              ]
            },
            {
              "required": [
                "participantId"
              ]
            },
            {
              "required": [
                "assignedTrackIds"
              ]
            }
          ]
        }
      }
    },
    {
      "if": {
        "properties": {
          "changeKind": {
            "const": "visitChanged"
          }
        },
        "required": [
          "changeKind"
        ]
      },
      "then": {
        "required": [
          "targetVisitId",
          "position"
        ],
        "not": {
          "anyOf": [
            {
              "required": [
                "participantId"
              ]
            },
            {
              "required": [
                "assignedTrackIds"
              ]
            }
          ]
        }
      }
    },
    {
      "if": {
        "properties": {
          "changeKind": {
            "const": "assignmentChanged"
          }
        },
        "required": [
          "changeKind"
        ]
      },
      "then": {
        "required": [
          "participantId",
          "assignedTrackIds"
        ],
        "not": {
          "anyOf": [
            {
              "required": [
                "targetVisitId"
              ]
            },
            {
              "required": [
                "position"
              ]
            }
          ]
        }
      }
    },
    {
      "if": {
        "properties": {
          "changeKind": {
            "const": "sessionStopped"
          }
        },
        "required": [
          "changeKind"
        ]
      },
      "then": {
        "not": {
          "anyOf": [
            {
              "required": [
                "targetVisitId"
              ]
            },
            {
              "required": [
                "participantId"
              ]
            },
            {
              "required": [
                "assignedTrackIds"
              ]
            },
            {
              "required": [
                "position"
              ]
            }
          ]
        }
      }
    }
  ],
  "description": "Authoritative sessionStarted and visitChanged both supply an explicit musical/UTC Position anchor. assignmentChanged changes assignments only and MUST NOT carry position or targetVisitId; sessionStopped is immediate."
}
```

## `event`

| Field | Type/schema summary | Direct required |
| --- | --- | --- |
| `profile` | `{"const":"OSTF-Distributed-Session-0.2"}` | Yes |
| `recordType` | `{"const":"event"}` | Yes |
| `eventId` | `{"$ref":"#/$defs/id"}` | Yes |
| `sessionId` | `{"$ref":"#/$defs/id"}` | Yes |
| `documentId` | `{"$ref":"#/$defs/id"}` | Yes |
| `revisionId` | `{"$ref":"#/$defs/id"}` | Yes |
| `performancePlanId` | `{"$ref":"#/$defs/id","description":"Required pinned finite 4.3 Core performancePlans[].id, also in prepared or stopped Snapshots; positions must match this ID."}` | Yes |
| `scoreSha256` | `{"type":"string","pattern":"^[0-9a-f]{64}$","description":"SHA-256 lowercase hex over the exact UTF-8 OSTF source document bytes after HTTP Content-Encoding removal and before parsing; byte identity pin only, not authentication or semantic normalization."}` | Yes |
| `baseStateRevision` | `{"type":"integer","minimum":0}` | Yes |
| `resultStateRevision` | `{"type":"integer","minimum":0}` | No/Conditional |
| `issuerParticipantId` | `{"$ref":"#/$defs/id"}` | Yes |
| `kind` | `{"enum":["phraseProposed","phraseCommitted","turnRequested","cueIssued","performanceObserved","participantStatus","sessionStateChanged"]}` | Yes |
| `effectivePerformanceTick` | `{"type":"integer","minimum":0}` | Yes |
| `payload` | `{"type":"object"}` | Yes |

**Complete JSON Schema definition:**

```json
{
  "type": "object",
  "properties": {
    "profile": {
      "const": "OSTF-Distributed-Session-0.2"
    },
    "recordType": {
      "const": "event"
    },
    "eventId": {
      "$ref": "#/$defs/id"
    },
    "sessionId": {
      "$ref": "#/$defs/id"
    },
    "documentId": {
      "$ref": "#/$defs/id"
    },
    "revisionId": {
      "$ref": "#/$defs/id"
    },
    "performancePlanId": {
      "$ref": "#/$defs/id",
      "description": "Required pinned finite 4.3 Core performancePlans[].id, also in prepared or stopped Snapshots; positions must match this ID."
    },
    "scoreSha256": {
      "type": "string",
      "pattern": "^[0-9a-f]{64}$",
      "description": "SHA-256 lowercase hex over the exact UTF-8 OSTF source document bytes after HTTP Content-Encoding removal and before parsing; byte identity pin only, not authentication or semantic normalization."
    },
    "baseStateRevision": {
      "type": "integer",
      "minimum": 0
    },
    "resultStateRevision": {
      "type": "integer",
      "minimum": 0
    },
    "issuerParticipantId": {
      "$ref": "#/$defs/id"
    },
    "kind": {
      "enum": [
        "phraseProposed",
        "phraseCommitted",
        "turnRequested",
        "cueIssued",
        "performanceObserved",
        "participantStatus",
        "sessionStateChanged"
      ]
    },
    "effectivePerformanceTick": {
      "type": "integer",
      "minimum": 0
    },
    "payload": {
      "type": "object"
    }
  },
  "required": [
    "profile",
    "recordType",
    "eventId",
    "sessionId",
    "documentId",
    "revisionId",
    "performancePlanId",
    "scoreSha256",
    "baseStateRevision",
    "issuerParticipantId",
    "kind",
    "effectivePerformanceTick",
    "payload"
  ],
  "additionalProperties": false,
  "oneOf": [
    {
      "properties": {
        "kind": {
          "const": "phraseProposed"
        },
        "payload": {
          "$ref": "#/$defs/phraseProposedPayload"
        }
      },
      "required": [
        "kind",
        "payload"
      ],
      "not": {
        "required": [
          "resultStateRevision"
        ]
      }
    },
    {
      "properties": {
        "kind": {
          "const": "phraseCommitted"
        },
        "payload": {
          "$ref": "#/$defs/phraseCommittedPayload"
        }
      },
      "required": [
        "kind",
        "payload",
        "resultStateRevision"
      ]
    },
    {
      "properties": {
        "kind": {
          "const": "turnRequested"
        },
        "payload": {
          "$ref": "#/$defs/turnRequestedPayload"
        }
      },
      "required": [
        "kind",
        "payload"
      ],
      "not": {
        "required": [
          "resultStateRevision"
        ]
      }
    },
    {
      "properties": {
        "kind": {
          "const": "cueIssued"
        },
        "payload": {
          "$ref": "#/$defs/cueIssuedPayload"
        }
      },
      "required": [
        "kind",
        "payload"
      ],
      "not": {
        "required": [
          "resultStateRevision"
        ]
      }
    },
    {
      "properties": {
        "kind": {
          "const": "performanceObserved"
        },
        "payload": {
          "$ref": "#/$defs/performanceObservedPayload"
        }
      },
      "required": [
        "kind",
        "payload"
      ],
      "not": {
        "required": [
          "resultStateRevision"
        ]
      }
    },
    {
      "properties": {
        "kind": {
          "const": "participantStatus"
        },
        "payload": {
          "$ref": "#/$defs/participantStatusPayload"
        }
      },
      "required": [
        "kind",
        "payload"
      ],
      "not": {
        "required": [
          "resultStateRevision"
        ]
      }
    },
    {
      "properties": {
        "kind": {
          "const": "sessionStateChanged"
        },
        "payload": {
          "$ref": "#/$defs/sessionStateChangedPayload"
        }
      },
      "required": [
        "kind",
        "payload",
        "resultStateRevision"
      ]
    }
  ],
  "description": "Authorized state changes must increment base revision by exactly 1. Proposals and observations never increment revision. See SESSION_STATE_MACHINE.md. Draft 0.9 requires a pinned Plan and exact score-byte digest on every 0.2 Snapshot/Event, including positionless prepared snapshots."
}
```

## `commitmentWindow`

| Field | Type/schema summary | Direct required |
| --- | --- | --- |
| `startPerformanceTick` | `{"type":"integer","minimum":0}` | Yes |
| `endPerformanceTick` | `{"type":"integer","minimum":1}` | Yes |

**Complete JSON Schema definition:**

```json
{
  "type": "object",
  "properties": {
    "startPerformanceTick": {
      "type": "integer",
      "minimum": 0
    },
    "endPerformanceTick": {
      "type": "integer",
      "minimum": 1
    }
  },
  "required": [
    "startPerformanceTick",
    "endPerformanceTick"
  ],
  "additionalProperties": false,
  "description": "Optional assertion that all accepted committed phrases intersecting half-open [startPerformanceTick, endPerformanceTick) are listed in committedPhrases for the Snapshot stateRevision. Semantic validator MUST check start < end and intersection/completeness against authority log."
}
```

## Draft 0.9 cross-document invariants (not representable by this Schema)

1. The root `performancePlanId` MUST resolve to an exact, finite OSTF 4.3 `performancePlans[].id` on the pinned document; it is mandatory even for `prepared` Snapshots without `position`.
2. When `position` exists (including inside `sessionStarted`), its `performancePlanId` MUST equal the record root `performancePlanId`. Source/performance Tick mapping and Visit references MUST resolve under that Plan.
3. Root `scoreSha256` MUST equal the SHA-256 of the *actual pinned OSTF source bytes*; changed byte content is a conflict even when `documentId`/`revisionId` are unchanged. The field does not confer trust/authorization or canonicalize JSON.
4. A `phraseCommitted` or retained `committedPhrase` MUST fit one explicitly `open` Part of the same pinned finite Plan and must not overlap accepted Track phrases; other Session 0.2 constraints remain in `SESSION_STATE_MACHINE.md`.
5. Earlier unpublished 0.2 Draft examples without both root fields must be explicitly re-authored. The already distinct Profile 0.1 is not silently upgraded.

No independently implemented parser, WAN, robot or DAW claims follow from this editorial reference.

## Draft 0.10 Visit re-anchoring requirement (not expressible by JSON Schema alone)

- On `changeKind:"visitChanged"`, both `targetVisitId` and `position` are mandatory; `assignmentChanged` must still not include either. No new `$defs` or Core 4.3 property is introduced.
- `position.visitId == targetVisitId`, `position.performanceTick == event.effectivePerformanceTick == pinned target Visit.startPerformanceTick`; `position.sourceTick` maps to the first source Tick of that Visit, and the inner Plan ID equals the pinned envelope Plan.
- `position.epochUtc` estimates the UTC clock-domain time associated with the asserted Performance Tick, not time of receipt. The new anchor must be usable to interpret the authorized jump without extrapolating a prior Visit's tempo/clock mapping across a skipped interval.
- Check Session authority, frozen Score tuple and forward-only transition before adopting the anchor. Clock-domain synchronization, command dispatch, safe robot timing and actually sounded notes remain external.
- Unpublished Draft 0.9 Profile 0.2 `visitChanged` Events with no `position` must be explicitly updated; Profile 0.1 is not silently migrated.

## Draft 0.11 — Cross-document semantic constraints on existing fields

- `position.clockDomainId`: on an accepted `sessionStarted`, establishes the authoritative musical clock domain for that playing Session; every later playing Snapshot and `visitChanged` Position MUST match. Cannot authenticate the real clock or certify accuracy.
- `position.tempoBpm`: optional, **descriptive**; if supplied, MUST numerically equal the effective `timeline.tempoChanges[].bpm` at its mapped source Tick. A missing source tempo cannot be filled by a Session hint.
- `event.effectivePerformanceTick`: a phrase start or a musical context depending on Event kind. For `sessionStopped`, audit/context only—NOT a future stop and NOT a claim that a physical robot stopped.

All requiredness and numeric bounds in the published Draft 0.10 Profile 0.2 Schema are unchanged in Draft 0.11. The detailed proposed rules are in `SESSION_STATE_MACHINE.md`. This appendix does not impose a new parameter name.


</details>
