# OSTF 5.1.0 — Import safety, content boundaries and implementation security

This specification serializes inert, untrusted **data**, not authorized instructions or executable behavior. Neither a URI nor a `pluginId`, schema `$id`, `asset.path`, MIDI note, physical-action hint or collaboration event grants software installation, file-system access, network access, I/O, device actuation or copyright permission.

## ZIP and directory handling

- Use the exact first uncompressed `mimetype` ZIP member and second `manifest.json` member, as specified in `PACKAGE_SPECIFICATION.md`.
- Reject absolute, drive-prefixed, parent `..`, dot `.` and empty path segments; reject backslashes, control chars, non-NFC paths, case-fold collisions, symlink or redirected extraction, unexpected/unlisted members and duplicate JSON keys.
- Enforce implementation-defined decompression, nesting, recursion, JSON and total-size limits before allocating memory; avoid ZIP bombs, path traversal and replacement of existing files.
- Extract to a staging directory; verify each uncompressed payload digest and size; only then perform a host-authorized, atomic final rename or equivalent safe save action.
- A relative resource URI in a Profile is never silently rewritten or used as an automatic remote-fetch instruction. Package binding is descriptive, not network consent.

## Score and plugin editing

Plugin Context `editProposal` is untrusted. Every `expected` value, stable ID, pointer and change must refer to one immutable source snapshot; reject overlapping edits or stale SHAs/revisions. Host permission is **outside** JSON; an `applied` Ack requires a successful real save and new digest. Do not let a parser import an inert plugin-state blob and execute it, or treat unknown plugin IDs as installed equivalents. Never confuse Score MIDI CC automation with Production mixer/send automation.

## Distributed sessions

The Versioned Distributed Session `snapshot`/`event` contract does not authenticate a participant or authorize events. SessionId, eventId, scoreSha256 and stateRevision provide data-level consistency; external identity, authorization, networking, scheduling and physical safety remain host responsibilities. Unverified fields and unavailable dependencies should be preserved as data or reported, not silently fabricated.

## Publication and interoperability limitations

`application/vnd.ostf-project+zip` is a proposed unregistered MIME identifier. JSON Schema `$id` identifiers are not evidence that the listed URLs serve content. A valid archive or passing structural Schema is not a security review, DAW interoperability certification or license clearance of third-party WAV, plugin state, samples, presets or voice assets. The included `tools/` scripts are static reference utilities, not hardened production parsers.


## Take handling

Candidate and unselected outputs remain disabled on import; importing does not automatically audition them. A writer without Comp support preserves candidates, outputs and additional information, or declines lossless save and reports loss. Unresolved references, contradictory selection and conflicting managed-Region automation are not repaired by guessing.
