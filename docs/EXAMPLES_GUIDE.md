# OSTF 5.1.0 — Complete example catalog

36 files: 22 standalone `.ostf`, 6 `.ostfp`, 2 Production, 3 Distributed and 3 Plugin JSON records. These examples cover feature themes; they are not an exhaustive test of every legal value or input combination. The 25 original 5.0 Score themes are retained directly, consolidated, or carried inside a package as mapped below.

| File | Focus | Inherited source |
|---|---|---|
| [01-prepared.json](../examples/distributed/01-prepared.json) | Prepared snapshot for the AABA Score in 04-combined-production-distributed.ostfp | 01-prepared.json, 22-pinned-session-aaba.ostf |
| [02-phrase-proposed.json](../examples/distributed/02-phrase-proposed.json) | Illustrative proposed phrase during open piano chorus; data alone does not change Score Takes | 04-phrase-proposed.json, 22-pinned-session-aaba.ostf |
| [03-playing-committed.json](../examples/distributed/03-playing-committed.json) | Playing snapshot with committed phrase and finite Plan/source/performance coordinates | 06-playing-committed.json, 22-pinned-session-aaba.ostf |
| [01-score-only.ostfp](../examples/ostfp/01-score-only.ostfp) | Minimal self-contained 5.1 Score-only archive | 01-score-only.ostfp |
| [02-legacy-4.3-compatible.ostfp](../examples/ostfp/02-legacy-4.3-compatible.ostfp) | Manifest 1.1 carrying unchanged legacy 4.3 Score bytes | 06-legacy-4.3-compatible.ostfp |
| [03-inert-plugin-state.ostfp](../examples/ostfp/03-inert-plugin-state.ostfp) | Actual authored post-proposal Score bytes; Production pin; preserved fictional plugin identity/state and source-audio binding | 04-inert-plugin-state.ostfp |
| [04-combined-production-distributed.ostfp](../examples/ostfp/04-combined-production-distributed.ostfp) | AABA Score document/revision pin, Production and Distributed 0.4 together, exact raw-byte SHA and supplied audio bytes | 11-combined-production-distributed.ostfp, 22-pinned-session-aaba.ostf |
| [05-audio-linear-comp.ostfp](../examples/ostfp/05-audio-linear-comp.ostfp) | Original two Take WAVs; non-destructive source handles; explicit linear region crossfade; inactive hard-cut Comp; no duplicate source playback | 5.1 new |
| [06-audio-rendered-comp.ostfp](../examples/ostfp/06-audio-rendered-comp.ostfp) | Original source assets plus a new equal-power rendered audioSource; outputMode=rendered; no second application of fades | 5.1 new |
| [01-context.json](../examples/plugin/01-context.json) | Read-only partial take/clip projection pinned to 26-midi-comp | 5.1 new |
| [02-edit-proposal.json](../examples/plugin/02-edit-proposal.json) | Atomic whole-Group and two whole-output replacements using one immutable base snapshot | 5.1 new |
| [03-applied-with-new-score.json](../examples/plugin/03-applied-with-new-score.json) | Illustrative applied acknowledgement whose effective SHA identifies the authored Score inside 03-inert-plugin-state.ostfp | 5.1 new |
| [01-production-04.json](../examples/production/01-production-04.json) | Production 0.4 audio source and independent mixer authority | 01-production-03.json |
| [02-typed-automation-04.json](../examples/production/02-typed-automation-04.json) | Typed Boolean/numeric channel, send, ordinary audio-region and device automation | 03-boolean-and-device-automation-03.json |
| [01-minimal.ostf](../examples/score/01-minimal.ostf) | Minimal required Score | 01-minimal.ostf |
| [02-guitar-solo.ostf](../examples/score/02-guitar-solo.ostf) | Guitar performed notes | 02-guitar-solo.ostf |
| [03-jazz-comping.ostf](../examples/score/03-jazz-comping.ostf) | Jazz harmony and ensemble comping | 03-jazz-comping.ostf |
| [04-aaba-performance-plan.ostf](../examples/score/04-aaba-performance-plan.ostf) | Finite AABA form and repeated Visits | 04-aaba-performance-plan.ostf |
| [06-scat.ostf](../examples/score/06-scat.ostf) | Scat and non-lexical vocal intent | 06-scat.ostf |
| [07-vocal-alternatives.ostf](../examples/score/07-vocal-alternatives.ostf) | Lyric alternatives plus a separate R&B open-vocal part | 07-vocal-alternatives.ostf, 05-rnb-vocal-open.ostf |
| [09-techno-variation.ostf](../examples/score/09-techno-variation.ostf) | Techno variation intent | 09-techno-variation.ostf |
| [10-physical-robot-requirements.ostf](../examples/score/10-physical-robot-requirements.ostf) | Physical performance requirements as inert data | 10-physical-robot-requirements.ostf |
| [11-harmony-plus-phrasing.ostf](../examples/score/11-harmony-plus-phrasing.ostf) | Harmony, key and phrasing | 11-harmony-plus-phrasing.ostf |
| [13-fixed-notes-and-directions.ostf](../examples/score/13-fixed-notes-and-directions.ostf) | Fixed notes with optional directions | 13-fixed-notes-and-directions.ostf |
| [14-tempo-map-reentry.ostf](../examples/score/14-tempo-map-reentry.ostf) | Tempo reentry and an explicit sourceRange Visit with a label | 14-tempo-map-reentry.ostf, 23-range-visit-and-label.ostf |
| [15-vocal-response-phrasing.ostf](../examples/score/15-vocal-response-phrasing.ostf) | Gospel response, vocal phonemes, curves and fixed-Plan boundaries | 15-vocal-response-phrasing.ostf, 08-gospel-response.ostf |
| [16-inherited-comprehensive-core.ostf](../examples/score/16-inherited-comprehensive-core.ostf) | Broad inherited Core: MIDI, resources, voices, provenance, clipChoices, localization and generation | 16-inherited-comprehensive-core.ostf |
| [17-fixed-note-source-cut.ostf](../examples/score/17-fixed-note-source-cut.ostf) | Source cuts, contiguous joins, repeated note occurrences and probability metadata | 17-fixed-note-source-cut.ostf, 25-source-note-repeated-visits.ostf |
| [18-visit-role-override.ostf](../examples/score/18-visit-role-override.ostf) | Visit realization and playing-role overrides | 18-visit-role-override.ostf |
| [20-phrasing-with-motif-reference.ostf](../examples/score/20-phrasing-with-motif-reference.ostf) | Motif reference and phrasing | 20-phrasing-with-motif-reference.ostf |
| [21-visit-and-range-intersection.ostf](../examples/score/21-visit-and-range-intersection.ostf) | Both Visit-only and Visit/range intersection response scopes | 21-visit-and-range-intersection.ostf, 12-visit-scoped-response.ostf |
| [24-intra-track-voices-response.ostf](../examples/score/24-intra-track-voices-response.ostf) | Concurrent voices and intra-track call/response | 24-intra-track-voices-response.ostf, 19-concurrent-voice-directions.ostf |
| [26-midi-comp.ostf](../examples/score/26-midi-comp.ostf) | Partial second Take; bar/chord-aligned Comp; lineage, ratings, note links, finite Visit override, weighted live selection and history | delta/examples/01-midi-comp.ostf |
| [27-silence-and-null.ostf](../examples/score/27-silence-and-null.ostf) | All-silence Comp, null active selection, partial silence, retained candidates and historical deleted IDs | 5.1 new |
| [28-midi-boundaries.ostf](../examples/score/28-midi-boundaries.ostf) | Sub-bar cut; truncate/retrigger/authored outputs; held note clipping, sustain/timbre chase and explicit sustain-off; cycle selection | 5.1 new |
| [29-live-selection-policies.ostf](../examples/score/29-live-selection-policies.ostf) | Fixed/manual/cycle/random/weighted live selection; explicit zero weight; independent track ownership; stored active fallback | 5.1 new |


## Bindings

Standalone Production/Distributed records pin the exact Score bytes inside `04-combined-production-distributed.ostfp`. The Plugin proposal base is `26-midi-comp.ostf`; the ACK new SHA identifies `score/song.ostf` inside `03-inert-plugin-state.ostfp`. This is authored illustration, not evidence of a plugin execution. Distributed examples illustrate independent states/events, not a complete replayable event log.

Audio05/06 use short original synthetic 16-bit PCM assets created for these examples, not an external artist recording. Original candidates and selected results are both retained. No audio playback or runtime test was conducted.

## Migration of the 25 original Score themes

| 5.0 source | 5.1 destination |
|---|---|
| `01-minimal.ostf` | [01-minimal.ostf](../examples/score/01-minimal.ostf) |
| `02-guitar-solo.ostf` | [02-guitar-solo.ostf](../examples/score/02-guitar-solo.ostf) |
| `03-jazz-comping.ostf` | [03-jazz-comping.ostf](../examples/score/03-jazz-comping.ostf) |
| `04-aaba-performance-plan.ostf` | [04-aaba-performance-plan.ostf](../examples/score/04-aaba-performance-plan.ostf) |
| `05-rnb-vocal-open.ostf` | [07-vocal-alternatives.ostf](../examples/score/07-vocal-alternatives.ostf) |
| `06-scat.ostf` | [06-scat.ostf](../examples/score/06-scat.ostf) |
| `07-vocal-alternatives.ostf` | [07-vocal-alternatives.ostf](../examples/score/07-vocal-alternatives.ostf) |
| `08-gospel-response.ostf` | [15-vocal-response-phrasing.ostf](../examples/score/15-vocal-response-phrasing.ostf) |
| `09-techno-variation.ostf` | [09-techno-variation.ostf](../examples/score/09-techno-variation.ostf) |
| `10-physical-robot-requirements.ostf` | [10-physical-robot-requirements.ostf](../examples/score/10-physical-robot-requirements.ostf) |
| `11-harmony-plus-phrasing.ostf` | [11-harmony-plus-phrasing.ostf](../examples/score/11-harmony-plus-phrasing.ostf) |
| `12-visit-scoped-response.ostf` | [21-visit-and-range-intersection.ostf](../examples/score/21-visit-and-range-intersection.ostf) |
| `13-fixed-notes-and-directions.ostf` | [13-fixed-notes-and-directions.ostf](../examples/score/13-fixed-notes-and-directions.ostf) |
| `14-tempo-map-reentry.ostf` | [14-tempo-map-reentry.ostf](../examples/score/14-tempo-map-reentry.ostf) |
| `15-vocal-response-phrasing.ostf` | [15-vocal-response-phrasing.ostf](../examples/score/15-vocal-response-phrasing.ostf) |
| `16-inherited-comprehensive-core.ostf` | [16-inherited-comprehensive-core.ostf](../examples/score/16-inherited-comprehensive-core.ostf) |
| `17-fixed-note-source-cut.ostf` | [17-fixed-note-source-cut.ostf](../examples/score/17-fixed-note-source-cut.ostf) |
| `18-visit-role-override.ostf` | [18-visit-role-override.ostf](../examples/score/18-visit-role-override.ostf) |
| `19-concurrent-voice-directions.ostf` | [24-intra-track-voices-response.ostf](../examples/score/24-intra-track-voices-response.ostf) |
| `20-phrasing-with-motif-reference.ostf` | [20-phrasing-with-motif-reference.ostf](../examples/score/20-phrasing-with-motif-reference.ostf) |
| `21-visit-and-range-intersection.ostf` | [21-visit-and-range-intersection.ostf](../examples/score/21-visit-and-range-intersection.ostf) |
| `22-pinned-session-aaba.ostf` | [01-prepared.json](../examples/distributed/01-prepared.json) |
| `22-pinned-session-aaba.ostf` | [02-phrase-proposed.json](../examples/distributed/02-phrase-proposed.json) |
| `22-pinned-session-aaba.ostf` | [03-playing-committed.json](../examples/distributed/03-playing-committed.json) |
| `22-pinned-session-aaba.ostf` | [04-combined-production-distributed.ostfp](../examples/ostfp/04-combined-production-distributed.ostfp) |
| `23-range-visit-and-label.ostf` | [14-tempo-map-reentry.ostf](../examples/score/14-tempo-map-reentry.ostf) |
| `24-intra-track-voices-response.ostf` | [24-intra-track-voices-response.ostf](../examples/score/24-intra-track-voices-response.ostf) |
| `25-source-note-repeated-visits.ostf` | [17-fixed-note-source-cut.ostf](../examples/score/17-fixed-note-source-cut.ostf) |

## Retention mode and concrete field coverage

A version migration of a complete musical tree is distinguished from consolidating its feature theme into another example. The field evidence and changes below record the actual handling; no byte-identical migration is claimed.

| Source | Destination/member | Retention | Field evidence / deliberate changes |
|---|---|---|---|
| `01-minimal.ostf` | [01-minimal.ostf](../examples/score/01-minimal.ostf)  | complete_score_migrated | Whole inherited musical tree retained; see changes for deliberate additions. Root version and demonstration title updated. |
| `02-guitar-solo.ostf` | [02-guitar-solo.ostf](../examples/score/02-guitar-solo.ostf)  | complete_score_migrated | Whole inherited musical tree retained; see changes for deliberate additions. Only root version changes from 5.0.0 to 5.1.0. |
| `03-jazz-comping.ostf` | [03-jazz-comping.ostf](../examples/score/03-jazz-comping.ostf)  | complete_score_migrated | Whole inherited musical tree retained; see changes for deliberate additions. Only root version changes from 5.0.0 to 5.1.0. |
| `04-aaba-performance-plan.ostf` | [04-aaba-performance-plan.ostf](../examples/score/04-aaba-performance-plan.ostf)  | complete_score_migrated | Whole inherited musical tree retained; see changes for deliberate additions. Only root version changes from 5.0.0 to 5.1.0. |
| `05-rnb-vocal-open.ostf` | [07-vocal-alternatives.ostf](../examples/score/07-vocal-alternatives.ostf)  | entities_merged | /tracks/1/id = lead; /tracks/1/directions/0/id = open-vocal-direction; /tracks/1/directions/0/parameters: voiceId=voice-lead, textPolicy=open, melodyPolicy=open, vocalizationKind=lexical; /lyrics/documents/1/id = doc-lead; /lyrics/voices/1: id=voice-lead, trackId=lead, documentId=doc-lead Original lead Track, its open lexical vocalFreedom, lyric document and voice are appended. Direction ID is renamed to open-vocal-direction to avoid an ID collision. The old separate song title is not retained as a second Score. |
| `06-scat.ostf` | [06-scat.ostf](../examples/score/06-scat.ostf)  | complete_score_migrated | Whole inherited musical tree retained; see changes for deliberate additions. Only root version changes from 5.0.0 to 5.1.0. |
| `07-vocal-alternatives.ostf` | [07-vocal-alternatives.ostf](../examples/score/07-vocal-alternatives.ostf)  | complete_score_migrated | Whole inherited musical tree retained; see changes for deliberate additions. Root version/title updated; old example 05 open-vocal entities are appended. |
| `08-gospel-response.ostf` | [15-vocal-response-phrasing.ostf](../examples/score/15-vocal-response-phrasing.ostf)  | theme_equivalent | /tracks/0/id = lead; /tracks/1/id = choir; /lyrics/voices: vlead->lead/lead-words with role=lead; vchoir->choir/choir-words with role=response; /ensembleInteractions/0: actorTrackId=choir, partnerTrackId=lead, actorVoiceId=vchoir, partnerVoiceId=vlead, relation=respondTo, start=0, duration=15360 The separate minimal empty-track Score is not copied. Its lead/choir voice relationship and respondTo interaction are demonstrated by the richer existing vocal example. The interaction duration is that richer example's 15360 ticks, not old 08's 30720 ticks. |
| `09-techno-variation.ostf` | [09-techno-variation.ostf](../examples/score/09-techno-variation.ostf)  | complete_score_migrated | Whole inherited musical tree retained; see changes for deliberate additions. Only root version changes from 5.0.0 to 5.1.0. |
| `10-physical-robot-requirements.ostf` | [10-physical-robot-requirements.ostf](../examples/score/10-physical-robot-requirements.ostf)  | complete_score_migrated | Whole inherited musical tree retained; see changes for deliberate additions. Only root version changes from 5.0.0 to 5.1.0. |
| `11-harmony-plus-phrasing.ostf` | [11-harmony-plus-phrasing.ostf](../examples/score/11-harmony-plus-phrasing.ostf)  | complete_score_migrated | Whole inherited musical tree retained; see changes for deliberate additions. Only root version changes from 5.0.0 to 5.1.0. |
| `12-visit-scoped-response.ostf` | [21-visit-and-range-intersection.ostf](../examples/score/21-visit-and-range-intersection.ostf)  | interaction_merged | /ensembleInteractions/1/id = whole-visit-response; /ensembleInteractions/1: actorTrackId=piano, partnerTrackId=sax, relation=respondTo; /ensembleInteractions/1/scope: performancePlanId=plan1, visitId=visit-head; start/duration are absent; /ensembleInteractions/0 keeps visit-solo plus start=30720 and duration=30720 for comparison The Visit-only response object is added as whole-visit-response and assigned to visit-head, so it does not duplicate the existing visit-solo/range interaction. The shared Plan, two Visits and piano/sax Tracks already exist in 21. This is an equivalent scope example, not an unchanged copy of the old solo-Visit decision. |
| `13-fixed-notes-and-directions.ostf` | [13-fixed-notes-and-directions.ostf](../examples/score/13-fixed-notes-and-directions.ostf)  | complete_score_migrated | Whole inherited musical tree retained; see changes for deliberate additions. Only root version changes from 5.0.0 to 5.1.0. |
| `14-tempo-map-reentry.ostf` | [14-tempo-map-reentry.ostf](../examples/score/14-tempo-map-reentry.ostf)  | complete_score_migrated | Whole inherited musical tree retained; see changes for deliberate additions. Root version updated; old example 23 sourceRange Visit is appended. |
| `15-vocal-response-phrasing.ostf` | [15-vocal-response-phrasing.ostf](../examples/score/15-vocal-response-phrasing.ostf)  | complete_score_migrated | Whole inherited musical tree retained; see changes for deliberate additions. Only root version changes from 5.0.0 to 5.1.0. |
| `16-inherited-comprehensive-core.ostf` | [16-inherited-comprehensive-core.ostf](../examples/score/16-inherited-comprehensive-core.ostf)  | complete_score_migrated | Whole inherited musical tree retained; see changes for deliberate additions. Only root version changes from 5.0.0 to 5.1.0. |
| `17-fixed-note-source-cut.ostf` | [17-fixed-note-source-cut.ostf](../examples/score/17-fixed-note-source-cut.ostf)  | complete_score_migrated | Whole inherited musical tree retained; see changes for deliberate additions. Root version updated; a source Note with old example 25 probability/deviation is added. |
| `18-visit-role-override.ostf` | [18-visit-role-override.ostf](../examples/score/18-visit-role-override.ostf)  | complete_score_migrated | Whole inherited musical tree retained; see changes for deliberate additions. Only root version changes from 5.0.0 to 5.1.0. |
| `19-concurrent-voice-directions.ostf` | [24-intra-track-voices-response.ostf](../examples/score/24-intra-track-voices-response.ostf)  | theme_equivalent_with_text_transfer | /tracks/0/id = vocal-group; /tracks/0/directions/0 and /tracks/0/directions/1 both start=0 and duration=3840, with voiceId=vlead and vchoir respectively; /tracks/0/directions/0/label = Lead vocal flexibility; /tracks/0/directions/0/instruction = Sing with gentle ornaments; text remains fixed.; /lyrics/voices/0/trackId and /lyrics/voices/1/trackId = vocal-group One Track with two simultaneous voice-specific directions is demonstrated by 24. The old first-direction label/instruction is transferred. Old 19's two fixed/ornamentable voice policies are not retained as a separate rendition: 24 deliberately uses fixed/ornamentable lead and open/nonLexical response. |
| `20-phrasing-with-motif-reference.ostf` | [20-phrasing-with-motif-reference.ostf](../examples/score/20-phrasing-with-motif-reference.ostf)  | complete_score_migrated | Whole inherited musical tree retained; see changes for deliberate additions. Only root version changes from 5.0.0 to 5.1.0. |
| `21-visit-and-range-intersection.ostf` | [21-visit-and-range-intersection.ostf](../examples/score/21-visit-and-range-intersection.ostf)  | complete_score_migrated | Whole inherited musical tree retained; see changes for deliberate additions. Root version updated; a Visit-only response derived from old example 12 is added for the head Visit. |
| `22-pinned-session-aaba.ostf` | [04-combined-production-distributed.ostfp](../examples/ostfp/04-combined-production-distributed.ostfp) score/song.ostf | complete_score_inside_package_migrated | /timeline/sections: A1,A2,B,A3 each duration=30720; /tracks: sax,piano,bass,drums; /performancePlans/0: id=form, visits=head/piano-chorus/sax-chorus/head-out; /document/id = doc-remote-aaba-43; /document/revisionId = r2-51; manifest.score.sha256 and sessions/production.json score.sha256 and sessions/distributed.json scoreSha256 identify the same uncompressed Score bytes The full AABA musical tree is enclosed as the one authoritative Score. Version becomes 5.1.0, title identifies the new 0.4 example, and revision becomes r2-51. A new Distributed session and Production companion are pinned to its exact new bytes; historical session records are not repinned in place. |
| `23-range-visit-and-label.ostf` | [14-tempo-map-reentry.ostf](../examples/score/14-tempo-map-reentry.ostf)  | visit_merged | /performancePlans/0/visits/2/id = range-selected; /performancePlans/0/visits/2/ordinal = 2; /performancePlans/0/visits/2/label = Only the second authored Section; /performancePlans/0/visits/2/sourceRange: start=7680, duration=3840; sourceSectionIds absent The sourceRange Visit and its label are copied into the existing tempo-reentry Plan as ordinal 2. The old one-Visit Plan title and separate Score title are not duplicated. |
| `24-intra-track-voices-response.ostf` | [24-intra-track-voices-response.ostf](../examples/score/24-intra-track-voices-response.ostf)  | complete_score_migrated | Whole inherited musical tree retained; see changes for deliberate additions. Root version updated; old example 19 label/instruction is copied to the first concurrent voice direction. |
| `25-source-note-repeated-visits.ostf` | [17-fixed-note-source-cut.ostf](../examples/score/17-fixed-note-source-cut.ostf)  | note_semantics_merged | /tracks/0/clips/0/notes/6/id = probabilistic-repeated-source; /tracks/0/clips/0/notes/6: start=960, duration=1440, pitch=64, velocity=90, probability=0.5, velocityDeviation=-8; /performancePlans/0/defaultRealization = fixed; /performancePlans/0/visits/0 and /performancePlans/0/visits/1 both include section-one The note values are reproduced under a fresh source Note ID on the existing long-source clip. Both existing Visits select section-one, so the same stored source Note can have two performance occurrences. Old Track/Clip/Plan names and the old silent default are not copied; the retained Plan explicitly uses fixed realization. |
