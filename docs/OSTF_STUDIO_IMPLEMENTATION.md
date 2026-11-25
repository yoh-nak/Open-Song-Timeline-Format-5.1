# OSTF Studio — 5.1 implementation guide

This is application guidance. `SPECIFICATION.md` defines normative timing, saving and selection. This guide does not assert that OSTF Studio has been implemented or tested.

## Section-by-track session view

The session grid may retain Section rows and Track columns. A cell is a view of existing material and Take Group/Comp data, not a new required UI or Ableton-specific object in the format. A group usually spans a Section, while bars, chords, phrases and arbitrary Tick ranges remain legal.

Display a local position as `sourceTick - section.start` while retaining source-global Ticks in the document. Revisited Sections reuse source material and use finite Plan Visits or host launch instances for identity. A group crossing Sections retains one ID while its range is projected into the view.

## Recommended operations

| User action | Stored representation |
|---|---|
| Record / generate | New disabled/muted source Clip/Region and Take |
| Select a whole Take | Comp covering its source plus explicit silence, with separate outputs |
| Pick a bar / chord range | UI-selected source-global Tick interval in compRegions |
| Comp | Complete nonoverlapping map and materialized output updated together |
| Switch saved Comp | activeCompId and old/new output selection flags saved atomically |
| Change during live play | Playback overlay; saved active Comp retained |
| Record a chosen performance | Finite Plan/visitSelections and matching Comp outputs |
| Export legacy | Project saved active outputs into ordinary material and report loss |

## Live launch

The host owns launch quantization, loop length, coordinated track switching, stopping, audition and UI state. Cycle starts at the first candidate on the first launch; random is uniform; weighted uses the explicit positive total. Persist actual choices as finite Visits when reproducibility is needed. Never store an infinite Visit list for indefinite looping.

A Visit/live-selected Comp is played through an overlay independent of saved selection flags. Candidates are not normal playback. Preserve Production Audio independence from Core MIDI silent/open; coordinated stopping uses explicit Channel controls.

## Boundaries and editing

MIDI truncate/retrigger/authored is applied when creating Comp output, not an instruction to invent a Note On on Visit reentry. Output MIDI state, sustain, CC, MPE, lyrics and phonemes must remain consistent. Audio retains source phase and frame ranges; composite envelopes or equalPower transitions that cannot be represented by regions use a pre-channel render.

Colors, lane heights, waveforms, key bindings, section buttons and grid layout belong to each application. Do not invent a required alternative timebase for display or let host extensions silently redefine standard meanings.
