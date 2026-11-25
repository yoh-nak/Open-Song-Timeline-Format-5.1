# OSTF 5.1.0 — Migration, compatibility and information loss

| Score | Production | Distributed | Manifest | Plugin Context |
|---|---|---|---|---|
| 4.3.0 | 0.2.0 | 0.2 | 1.0.0 / 1.1.0 | 1.0.0 / 1.1.0 |
| 5.0.0 | 0.3.0 | 0.3 | 1.0.0 / 1.1.0 | 1.0.0 / 1.1.0 |
| 5.1.0 | 0.4.0 | 0.4 | 1.1.0 | 1.1.0 |

## 1. Retain exact versions

Read legacy Score 5.0 under its own Schema and semantics. A save without 5.1 takes may retain that version. Packaging alone must not reformat or revise a Score. A 5.0-only reader is not assumed to accept 5.1 directly.

## 2. Upgrade 5.0 to 5.1

1. Retain original bytes, Document ID/Revision, source material and companion records.
2. Explicitly save a new Score at version 5.1.0. takeGroups may be omitted. Preserve structure, harmony, MIDI, lyrics and performance intent.
3. When introducing takes, create source candidates, separate output IDs, Comp maps and flags in the same save. Merely enabling a candidate is not a take-selection operation.
4. Compute the new raw Score digest. Explicitly migrate/rebind Production 0.4 after checking references and safe-integer time/frame bounds. Do not simply swap an old pin.
5. Preserve Distributed history. Create a separate 5.1 Session with a new sessionId and actual authority, clock and Plan identity; never rewrite historical Events onto the new Score.
6. Build Manifest 1.1 from actual new Score/Profile/Asset bytes, SHA, size and bindings.

An explicit 4.3 migration retains adopted semantics. Production 0.2 automation must additionally meet the numeric type/domain rules introduced in 0.3.

## 3. Export the active result to 5.0

Retain the saved active Comp's ordinary Clips/Audio Regions and remove Core takeGroups and Production audioTakeGroups. Null selection retains silence. Retained source candidates stay disabled/muted; deleting them requires repair of every affected note, lyric, resource and other reference. Disposition of unselected Comp outputs is explicit.

Write a new Score 5.0.0 and Production 0.3.0 with matching raw pins and manifest. Alternative Comps, dynamic selection, ratings, origin, history and visitSelections are lost, so preserve the original 5.1 and disclose that loss. Preserving visit-specific choices requires a separate bake to a performance timeline; changing version alone cannot reproduce it. Retain rendered audio and its explicit bindings when used.

## 4. Loss disclosure

| Supplied input and operation | Supported assertion |
|---|---|
| Score-only received and saved | Preservation of that Score scope |
| Score+Production+audio received, only Score exported | Partial project export |
| Only URI/SHA descriptors received | Descriptor preservation, not actual audio preservation |
| Asset/state bytes present, runtime absent | Byte retention, not verified sound reproduction |
| Writer does not understand Comp maps | Preserve the original structure/material/output or decline lossless save |
| Contradiction or stale pin | Report affected IDs and cause; do not repair by guessing |

A loss report names the operation, actual supplied documents/bytes, target version, affected ID/Pointer, omitted/approximated/unavailable/unsupported/unresolved/stale_binding classification, and save outcome. This vocabulary is advisory, not a new mandatory file family.
