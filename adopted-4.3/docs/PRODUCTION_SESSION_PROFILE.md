> **Current adoption candidate: Draft 0.77 (UNRATIFIED).** The first reference-binding decision table is the active proposal. Older dated clauses in this document are historical and must not be interpreted as simultaneous alternative normative rules. This edition changes editorial identification only; it does not alter serialization or Schema.

# Draft 0.77 — Active reference-binding decision table (PROPOSED / NOT RATIFIED)

**Review gate D03.** This active candidate is the controlling *proposal* for reference-binding interpretation. Earlier Draft 0.62–0.72 sections below are historical change records, **not alternative active requirements**. This front section has no authority until publisher adoption. Schema structures and serialization are unchanged.

| Evaluation order | Condition | Implementation-side report |
|---|---|---|
| 1 | Companion JSON, required pin or declared format is malformed | `INVALID` (outside four binding statuses) |
| 2 | Companion format/version unsupported | `UNSUPPORTED` (outside four binding statuses) |
| 3 | Authorization boundary undefined, authorized candidates not completely enumerated, or required Score bytes not retrievable | `NOT_EVALUATED`; disclose partial evidence, no conclusive binding status |
| 4 | Complete explicitly authorized candidate set contains no Score byte streams | `MISSING` within that scope only |
| 5 | Complete set contains bytes but no raw-byte SHA-256 match to pinned Score | `MISMATCH` within that scope only |
| 6 | Digest-matched Score is not parseable or violates its applicable Core structure | Score-format error, **not** `RESOLVED` |
| 7 | Matching valid Score has absent, duplicate, or invalid required Track/Plan/Visit/range referents | `AMBIGUOUS` plus specific diagnostic details (including `missing_referent` or `nonunique_referent`) |
| 8 | Matching valid Score and all required referents resolve uniquely | `RESOLVED` within declared scope |

**Byte identity and permissions.** Hash the original Score file bytes in the declared hash domain; do not normalize Unicode, change line endings, strip BOMs, reserialize JSON, or hash the ZIP wrapper as a substitute. A copy of identical Score bytes is one byte identity. Never infer identity from a filename, URI, cached digest, or matching musical contents. A narrower candidate set is a **new explicitly disclosed assessment**; silently dropping failed retrievals is prohibited. None of these reporting labels are JSON Schema fields, and digest equality does not establish authorship, trust, permission, audible reproduction, network execution or physical-actuator safety. Score rebind after editing requires deliberate approval and a new pin.

**Release control.** D01, D02, D03, D04 and D05 remain PENDING. Independent parser, DAW/plugin/DSP, vocal, WAN/distributed execution, and physical AI/robot runtime verification are excluded from the requested publication gate and have not been performed.

---

# Draft 0.72 — Editorial authority and adoption boundary (UNRATIFIED)

**Adoption target: D03 / Production Session 0.2.** Only the text explicitly identified in the release ballot and its existing schema is eligible for adoption. Previous Draft 0.62–0.70 binding examples are retained as change history, not simultaneous alternative definitions. For conflicting reference outcomes, Draft 0.71's fully enumerated/fully fetched authorized candidate-set rule prevails **within this candidate**. A partial collection is externally `NOT_EVALUATED`; no JSON property is introduced.

An implementation MUST distinguish: (a) reading/retaining unknown data, (b) round-trip preservation, (c) editing, (d) interpretation, and (e) actual execution. A claim covering one operation MUST NOT imply all others. A valid matching digest is not evidence of Session execution, mixer audio parity or robot actuation. These proposed MUST statements become normative **only after D03 publisher adoption**.

> **Current proposed editorial precedence: Draft 0.71.** This first section supersedes the Draft 0.70 incomplete-enumeration RESOLVED exception; historical sections below are retained as version history. No publisher adoption is implied.

## Draft 0.71 — Completion barrier for binding resolution (PROPOSED; not ratified)

This clause supersedes the Draft 0.70 exception allowing `RESOLVED` on incomplete candidate enumeration based on an implementer's prediction that additional candidates cannot change the outcome. Predictions about uninspected candidates MUST NOT be treated as verified evidence.

1. First establish that the Profile is structurally valid and its version is supported; otherwise return `INVALID` or `UNSUPPORTED` outside the binding classifications. Do not infer authorization to read Score bytes from a locator or a hash.
2. Define a **bounded, authorized candidate set** and record its identification, coverage and whether each candidate was retrieved and hashed from actual bytes. The binding diagnosis is strictly local to this declared set, never a global absence claim.
3. If the set is not completely enumerated **or** at least one required candidate's original bytes could not be retrieved, report external diagnostic `NOT_EVALUATED` with observed partial evidence. Do not issue any of the four conclusive statuses, even when one inspected candidate matches the pin. A caller MAY explicitly define a narrower *complete* authorized set and reassess, but MUST disclose the changed scope rather than silently discard failures.
4. Once authorized enumeration and required byte retrieval are complete: zero eligible Score candidates produces `MISSING`; one or more candidates but zero raw-byte SHA-256 matches produces `MISMATCH`; a matching Score whose required semantic referents are absent, nonunique or invalid for the declared target produces `AMBIGUOUS` with external details; exact digest match and all required referents uniquely resolved produces `RESOLVED`.
5. Multiple physical copies of the same exact Score bytes count as the same byte identity; distinct mismatching candidates do not become matches from identical labels, URLs, musical content, or hashes asserted without byte verification. Rebinding to a changed Score always requires explicit user/application authorization and a new digest assertion. The binding outcome grants no execution, network, audio, plugin or robot permissions.

`NOT_EVALUATED`, `INVALID`, `UNSUPPORTED` and optional diagnostic suffixes are **reporting statuses**, not new wire fields or schema enums. The four binding names are also editorial diagnostics, not newly serialized properties. These rules are proposed interpretations for publisher decision D01/D02/D03 and have not undergone implementation or interoperability testing.

---

# Draft 0.69 — Authorized Score candidate boundaries (UNRATIFIED)

**Proposed clarification for R04/R11/R13/R14.** The four reference outcomes are evaluated against the *candidate set explicitly supplied or authorized for this operation*, not against every Score that might exist elsewhere. Do not scan local unrelated directories, query remote URLs, or search a repository implicitly merely to turn `MISSING` into `RESOLVED`. The user/host may separately authorize additional bytes and then **rerun** the assessment; this is a new evaluation, not a retrospective correction of the earlier result.

- **No supplied/authorized candidate bytes:** `MISSING`, meaning *not found within the evaluated scope*, not a global assertion that the Score no longer exists.
- **At least one candidate byte stream, none matching the pin:** `MISMATCH` within that scope, even when every available candidate is a newer revision. Do not claim the old Score is globally absent.
- **Matched bytes, invalid Score structure:** Score-format error; the digest match alone cannot establish `RESOLVED`.
- **Matched valid Score, missing/non-unique required referent:** `AMBIGUOUS` with `missing_referent` / `nonunique_referent` detail respectively (diagnostics only, not serialized fields).
- **All required referents unique:** `RESOLVED` within the evaluated scope. Duplicate copies of identical bytes are one byte identity.

A cached digest, filename, URL, signed link or filename-index hit **does not replace possession of the actual Score bytes** for a fresh raw-byte check. Implementations may disclose an additional `not_evaluated`/`unknown` operation-level condition when access to the nominated candidate bytes was not actually possible; this is not a fifth OSTF binding status and must not be reported as verified `MISSING` or `MISMATCH`. No result grants authenticity, recording, playback, plug-in restoration or physical actuation authority. **Publisher adoption D01–D03 and rights/ZIP approvals D05/D04 remain pending.**

---

# Draft 0.68 — Reference outcome precedence and historical-table reconciliation (UNRATIFIED)

**Current proposed interpretation (R04/R11/R13/R14; not an adopted standard):** Apply the following decisions *in order* to an explicitly authorized Score candidate set. A historical table below that differs from this precedence is superseded as editorial guidance, not silently rewritten as if it had never existed.

1. Reject malformed or unsupported companion format/version/pin as `INVALID / UNSUPPORTED` (outside binding diagnostics).
2. If no original Score byte candidates are available, report `MISSING`. A matching filename or metadata is not a byte candidate.
3. If one or more bytes candidates exist but no raw SHA-256 digest matches, report `MISMATCH`, **including when only a newer Score revision is present**. This corrects the Draft 0.62 historical example that had called that case `MISSING`.
4. If digest-matched Score bytes cannot be parsed or violate mandatory Score structure, report a **Score format error** outside binding diagnostics.
5. For a valid matching Score, evaluate *all required* companion referents, never permitting a digest match alone to imply resolution: zero referents => `AMBIGUOUS` + `missing_referent`; more than one => `AMBIGUOUS` + `nonunique_referent`; contradictory/invalid scope => `AMBIGUOUS` + explanatory detail. If multiple required referents fail, disclose each failure and retain one summary `AMBIGUOUS`.
6. Only when every required referent resolves uniquely, report `RESOLVED`. Duplicate file paths containing identical bytes are **one** Score identity; no ambiguity merely from file copies.

All displayed statuses/details are implementation-side diagnostic guidance, **not** new serialized schema fields or enumerations. This decision does not authenticate a Score, imply execution, permit network retrieval, grant rights, or authorize automatic rebind. The EN/JA versions have equal editorial review priority; a conflicting translation blocks adoption. D01–D05 remain PENDING; runtime/DAW/DSP/network/robot/independent-parser checks remain excluded and unperformed.

---

# Draft 0.67 — Reference-diagnostic semantic closure candidate (NOT ADOPTED)

**Actual editorial inconsistency for publisher resolution (R04/R11/R13/R14):** the Draft 0.64 conformance matrix labels an *absent* required Track/Plan referent `AMBIGUOUS`, even though that word normally describes *more than one valid candidate*. The published four-outcome reference-diagnostic vocabulary does not separately serialize a `REFERENT_MISSING` state. This is an ambiguity in proposed explanatory text, **not** evidence of a Schema defect or of a tested parser.

**Recommended normative clarification:** keep the four existing human-readable binding statuses and do not change any JSON Schema. First require valid, supported Profile structure and an exact raw-byte Score digest match. Only then resolve semantic referents. When a required Track/Plan/Visit referent resolves to **zero** objects, emit `AMBIGUOUS` at the *companion binding summary* level **with an explicit detail `missing_referent`**, never describe this as multiple valid targets; when it resolves to **more than one** object, emit `AMBIGUOUS` with detail `nonunique_referent`. When it resolves to exactly one object and all other required referents likewise resolve, emit `RESOLVED`. These detail labels are **recommended diagnostic strings, not new OSTF fields, enum members, or required serialized values**. Implementations may use their own diagnostic codes provided they preserve the distinction. `MISSING` remains reserved for missing exact Score bytes, not missing objects inside a matched Score.

**Binding security/privacy boundary:** Only candidates explicitly supplied or authorized by the caller may be used to resolve a Score pin. A matching path, filename, URL, metadata title or semantically equivalent reserialization does not prove a raw-byte identity; implementations MUST NOT silently pull unrelated network objects, automatically rebind, replace a source, or claim lossless round trips without backing bytes. This is proposed normative wording pending publisher adoption.

**Decision:** D01/D02/D03 must explicitly adopt, revise, or reject this clarification; any future accepted normative text must be reflected in the EN/JA pairs and conformance examples. D04/D05 still pending. Tests of runtime, independent parsers, DAWs, WAN and robots remain out of scope and unexecuted.

---

# Draft 0.66 — Current review baseline and normative authority (UNRATIFIED)

**This is the active Draft 0.66 review baseline; earlier Draft-numbered addenda in this file are historical design rationale, not separately applicable alternative versions.** This section does not alter the six JSON Schemas, Score data, Profiles, or reference tools. It also does not record publisher acceptance.

- **Core 4.3:** `schema/ostf-4.3.0.schema.json` together with the *current consolidated* `docs/SPECIFICATION.md`, `docs/SPECIFICATION.ja.md`, `docs/SEMANTIC_RULES.md` and `docs/PERFORMANCE_TIMELINE.md`. Inherited Core 4.2 semantics remain in force where 4.3 does not explicitly amend them.
- **Distributed Session 0.2:** `schema/ostf-distributed-session-0.2.schema.json`, `docs/SESSION_PROFILE.md`, `docs/SESSION_PROFILE.ja.md`, `docs/SESSION_STATE_MACHINE.md`. This records synchronization/session state, **not** network service or physical-actuation permissions.
- **Production Session 0.2:** `schema/ostf-production-session-0.2.schema.json`, `docs/PRODUCTION_SESSION_PROFILE.md`, `docs/PRODUCTION_SESSION_PROFILE.ja.md`, `docs/PRODUCTION_COMPATIBILITY.md`. Host mixer state and plug-in/asset descriptions do **not** imply DSP or plug-in execution.
- **Interpretation hierarchy proposed for adoption:** for structural constraints, version-matched Schema is authoritative; for semantic constraints, the applicable version-matched normative specification is authoritative; explicit Core 4.2 inheritance continues where 4.3 is silent. Editorial examples, diagnostics, implementation guides, old change notes and checklists cannot override either. If Schema and normative prose disagree, it is an **unresolved release-blocking inconsistency**, not permission to pick whichever is convenient.
- **Companion binding:** validate the specific companion format/version first; digest-match against authorized **original Score bytes**, then resolve required referents. `RESOLVED`, `MISSING`, `MISMATCH` and `AMBIGUOUS` are proposed human-readable binding diagnoses, not wire-format fields. Invalid/unsupported inputs are errors outside these four diagnoses. Missing referents must be named precisely even when grouped under `AMBIGUOUS`; they are not proof that several equally valid targets exist. Never silently rebind or claim atomic cross-file saving.
- **Conformance:** claims must identify family, version, and operations (read, edit, write/export, preserve, execute) separately. Retaining a URI does not retain the asset; storing plugin state does not guarantee reconstruction; an acknowledged remote event is not proof of performance. Explicitly report unsupported or lost data.

**Freeze proposal:** R01–R14 below are recommended for ACCEPT as a single non-breaking editorial closure set, subject to the publisher reviewing the exact normative documents. Any contradictory interpretation found during that review returns the affected D01–D03 gate to AMEND. D04 and D05 must not be approved by inference; the final exact ZIP and rights evidence remain required. Excluded runtime/integration tests are neither performed nor certified.

---

## Draft 0.64 — Reference resolution versus validation: decision boundary (candidate, unratified)

The four diagnostic labels in Draft 0.63 describe **reference resolution** of an otherwise recognized, well-formed companion. They are not JSON fields, wire-level status codes, or runtime certification. The precedence is:

1. **VALIDATE THE COMPANION FIRST.** Determine the declared family/version and check required pin syntax, including the documented location of its SHA-256 pin. Unsupported versions and malformed required pins are **INVALID / UNSUPPORTED**, not `MISSING` or `AMBIGUOUS`.
2. **IDENTIFY THE AUTHORIZED SCORE CANDIDATE SET.** An empty set of original Score bytes is `MISSING`; an existing set with no matching raw-byte SHA-256 is `MISMATCH`. Do not substitute filenames, document titles or a semantically equivalent reserialization.
3. **RESOLVE REFERENCES ONLY AFTER A DIGEST MATCH.** Check the identity, Track, Plan, Visit, range and revision referents actually required by the specific companion Profile. Only a complete, uncontradicted resolution is `RESOLVED`. A matching digest with unresolved, conflicting or non-unique required referents is `AMBIGUOUS` as a human-readable reference diagnosis; retain the specific underlying error.
4. **NO IMPLICIT REPAIR.** None of the four labels authorizes digest rewriting, Score relinking, deleting unsupported payloads or a claim that a saved or executed performance succeeded. An explicit rebind is an independently authorized edit and must preserve the previous Score/Profile until the edit is committed.

If a score file's bytes match the pin but the Score itself is unparsable or violates a required Core constraint, report a **Score-format validation failure** explicitly rather than pretending reference coherence or selecting a different Score by name. The four labels must not conceal a prerequisite structural error. The above is not a cryptographic authenticity, authorization, device-safety or distributed-consensus guarantee. **R04/R11/R13/R14 and D01–D03 are still pending.**

---

> **Historical editorial snapshot: Draft 0.64 (unratified); D01–D05 pending.**


## Draft 0.63 — Deterministic companion Score binding decision procedure (candidate normative clarification)

This procedure determines whether a *given companion record* can be interpreted against available Score bytes; it neither changes any JSON Schema nor makes the host fetch or execute content.

1. Read the companion's **required pin and identity fields** from its declared Profile version. For Distributed 0.2 the pin is root `scoreSha256`; for Production 0.2 the pin is `score.sha256`. Do not treat an absent, invalid or unsupported-version required pin as `MISSING`: this is a **malformed/unsupported companion**, outside the four binding outcomes.
2. Form a finite candidate set from Score **bytes already explicitly supplied or locally authorized** for this binding. Do not use matching filenames, titles, paths, Track names or the most recent revision as a substitute for the digest. Do not retrieve network assets implicitly.
3. Hash each candidate's **original byte sequence** using SHA-256, before parsing/reserializing. Distinct paths containing identical bytes count as one byte identity. A cryptographic digest match is evidence of byte identity for this purpose, not proof of content provenance or authenticity.
4. Apply this decision precedence:
   - If no Score bytes are available: **MISSING**.
   - If exactly one distinct matching byte identity is available and its Score identity, revision, referenced Track(s), and (when applicable) Plan/Visit/ranges are resolvable according to the companion's normative Profile: **RESOLVED**.
   - If one matching byte identity is available but any required referent is absent, contradictory or non-unique: **AMBIGUOUS** at the *semantic binding* layer; do not claim RESOLVED merely from the digest.
   - If no candidate bytes match the expected digest, despite candidates being present: **MISMATCH**. Multiple different mismatching candidates do not turn a known digest mismatch into ambiguity.
   - If distinct matching byte identities or incompatible referent resolutions remain after the prescribed checks: **AMBIGUOUS**; record the conflicting identities without choosing arbitrarily. Under ordinary SHA-256 byte-identity assumptions distinct matching bytes would be exceptional; do not infer they have been encountered.
5. Only **RESOLVED** can support a claim that the companion's *binding* is currently coherent. The other outcomes must not trigger an implicit edit of the companion's digest/identity fields. An explicit rebind is a separately authorized edit that must review and update all required references and produce a newly identified companion revision where the Profile requires it. Preserve the original companion and Score if a rebind fails or is uncommitted.

The order above makes `MISMATCH` and `AMBIGUOUS` disjoint in routine file-search cases and clarifies that the four labels are **human-facing editorial outcomes**, not required wire enums, standardized error codes, a universal trust model, or validated runtime behavior. An implementation may provide a more detailed diagnostics vocabulary, but must not silently assert RESOLVED for a failed reference check. This proposal is pending R04/R11/R13/R14 and D01–D03 adoption.

---

> **Historical editorial snapshot: Draft 0.62 (unratified).** Companion binding resolution states clarified; D01–D05 pending. Runtime tests excluded, not passed.


## Draft 0.62 — Companion binding resolution states (candidate; not adopted)

When an implementation opens a Distributed or Production companion bound to a Score digest, it SHOULD distinguish **RESOLVED** (the exact original Score bytes have the expected digest), **MISSING** (no original Score bytes available), **MISMATCH** (bytes are available but digest differs), and **AMBIGUOUS** (multiple candidates/identities are present and the intended binding cannot be established). A matching display title, file path, or musically equivalent re-export is not sufficient to change a MISSING/MISMATCH/AMBIGUOUS case into RESOLVED. Multiple identical-byte copies are one byte identity, not an ambiguity.

A non-RESOLVED binding MUST NOT be silently repaired by selecting the latest local Score or guessing from Track names. Implementations MAY display the unresolved companion read-only, but any reassociation is an explicit user/author operation subject to referenced Track, Plan, Visit and range checks. Do not claim a lossless coherent bundle while a required companion binding is unresolved. This is an **editorial proposal** for R04/R11/R13/R14 and D01–D03, not an additional JSON property, mandatory diagnostic wire format, network-retrieval permission, or tested implementation.

---

## Draft 0.61 — Old-Score retention and crash-recovery boundary (PROPOSED; unsigned)

**Dependency preservation:** A companion Profile left pinned to the old exact Score digest remains usable *as a coherent old-version bundle* only if the corresponding old Score bytes remain available. Retaining the Profile alone is insufficient. A save/export UI MUST NOT describe the new Score plus an unmodified old-pinned Profile as a consistent new-version bundle. The safe outcomes are: (i) preserve and identify the old Score with its old companion, (ii) explicitly rebind a selected companion after verifying all references, or (iii) report a detached/unresolved companion and avoid a lossless-bundle claim.

**Partial failures:** Writing files to temporary destinations does not itself create an atomic transaction. If a crash, failed rename, permission error or interrupted network transfer occurs, the implementation must report which exact Score/Profile bytes were durably committed, which are pending, and which references are unresolved before it claims a coherent export. If status cannot be established, treat it as *unknown*, not success. Never fabricate an updated pin or silently discard the old Score. A manifest or UI status is evidence of a claim, not proof of an atomic filesystem or network operation.

**Not a newly required serialized property:** The exact storage location, durable-commit mechanism, backup policy and recovery UI are implementation concerns; this paragraph proposes an observable interoperability outcome, not an OSTF filesystem protocol. This applies equally to Distributed and Production companions. R04/R11/R13/R14 and D01–D03 adoption pending; no publisher approval is implied.

---

## Draft 0.60 — Transactional companion Profile rebinding after a Score edit (PROPOSED, unsigned)

A Score edit that changes its exact serialized bytes changes its pinned identity even when the music sounds equivalent. **Proposed authoring operation** (not a new OSTF JSON command or mandatory API):

1. Preserve the original Score bytes, its digest, and every referring Profile **unchanged** until an explicit new Score export is accepted. List the companion Distributed and Production documents separately, including any unavailable or opaque reference targets.
2. Produce a new Score artifact and compute the digest from the **exact exported byte sequence**. Do not substitute a parsed-object comparison, whitespace-normalized JSON, decoded audio, or a manifest entry for the referenced Score bytes.
3. Before any companion update, classify each reference as: (a) still targeting the unchanged original Score; (b) selected for explicit rebind to the new Score; or (c) unresolved/unknown. Never silently convert (a) or (c) to (b). A musical-performance plan or Track ID matching by name is not sufficient evidence for rebinding.
4. For each selected companion, verify the old pinned digest corresponds to the expected original Score bytes and verify that its referenced IDs/ranges still resolve under the new Score. If a reference no longer resolves, leave that companion unchanged and report the specific incompatibility. Do not silently drop events, automation or non-note vocal information to make rebind appear successful.
5. Write each new or updated artifact to a **separate destination** until all chosen edits are ready. An implementation promising an all-or-nothing multi-file export must complete or roll back the *entire chosen set*; the OSTF format itself does not provide an atomic filesystem, archive or network transaction. Do not overwrite the original Score/Profiles before the chosen consistency boundary is satisfied.
6. Report the output Score digest, companion-by-companion binding decision, retained unknown data, omitted information and missing assets. Where a local tool cannot complete steps 4–5, export the new Score only with old Profiles still explicitly pinned to the original, or decline the combined export; never call an unresolved bundle lossless or coherently rebound.

**Cross-family safety boundary:** Session commitment is not approval of Score mutation; Production mixer state is not a substitute for Score MIDI CC. An unknown optional payload can be retained as opaque data without claiming it was interpreted. Rebinding metadata cannot grant plug-in, network, filesystem or robot execution authority. This is candidate guidance for R04, R11, R13 and R14 under D01–D03; it has no authority until adopted by the publisher and creates no new JSON properties.

---

## Draft 0.56 — operation-scoped preservation and explicit binding (candidate, not ratified)

An importer/exporter MUST NOT conflate **parsing**, **preserving**, **editing**, **executing**, and **rendering**. In the following decision examples, MUST is **proposed normative language** subject to publisher adoption under D01–D03; it does not revise the versioned JSON Schema:

- A read-only Score import does not commit Session events or change Production state. An editor may report Score-only support while retaining opaque optional fields, but must disclose any deleted or rewritten unsupported data when it exports.
- A byte-pinned Score association cannot be silently transferred to a different serialized Score. Even if musical content is equivalent, a changed hash requires explicit review/rebinding; old associations may remain attached to the old Score.
- A Profile's descriptive state and a real-world action are independent. An accepted Session phrase is not proof of played sound, a robot action or an audio render. Likewise, a Production plug-in descriptor is not proof of executable plug-in availability.
- Missing external Asset bytes must be reported as missing, even where the URI, digest or descriptor is preserved. A Studio importer must not silently rewrite musical source notes, velocities or MIDI events to realize mixer or automation data.
- Reporting loss should identify affected family/version, operation, affected paths or external resources, and whether information was retained, transformed, omitted or unavailable; this reporting convention is **out-of-band**, with no newly required serialized OSTF property.

If the application cannot safely preserve or disclose information necessary for its advertised operation, it must narrow the claim instead of representing the result as full-fidelity interchange. See `CONFORMANCE.md` and R14 in `PUBLISHER_RELEASE_DECISIONS.md`.

# OSTF Production Session Profiles 0.1.0 / 0.2.0 — Proposed Semantics (Draft 0.55)

> **Historical editorial snapshot: Draft 0.59 (unratified).** Existing headings referring to earlier Drafts describe cumulative editorial proposals, not competing active document versions. The exact versioned Schemas remain unchanged; the single current release gate is [RELEASE_READINESS.md](RELEASE_READINESS.md). Publisher acceptance D01–D05 is still pending; runtime/independent tests are excluded, not passed.

## Draft 0.33 — Production save/rebind operation boundary (pending adoption)

Production save or Score-rebind is separate from Score authoring and Distributed event acceptance. A host MUST NOT claim plug-in/Asset-byte preservation based solely on a descriptor, and MUST NOT modify Score Notes, Session state or opaque Asset bytes merely because a Production reference resolves. A cross-document operation must report each modified or omitted component and refuse the non-lossy claim on incomplete scope. See `CONFORMANCE.md` for operation-by-operation distinction. No new Studio schema or serialized report field.

---

## Draft 0.32 — Production binding after Score reserialization (pending)

The `score.sha256` value pins **exact Score resource bytes**, not a JSON-semantic equivalence class. Reserializing Score without changing its music may still invalidate the old digest. Use an explicit Production Profile copy/rebinding workflow (and review affected source-Tick/Track/Plan meanings), retain the old binding for the old Score, or decline the claimed non-lossy *combined* export. A URI or descriptor alone is not proof that original Score or opaque Asset bytes were supplied. See `CONFORMANCE.md` Draft 0.32. No Schema/JSON-field change.

---

## Draft 0.29 — Implementation diagnostics and preservation claims (unratified)

See the new proposed reporting taxonomy in `docs/CONFORMANCE.md`: a Profile descriptor retained without referenced audio/plug-in bytes is not complete asset preservation; unsupported semantics need not mean invalid serialized input; an intentionally partial export must identify supplied components omitted; stale Score digest/revision needs explicit rebind. This adds no Production JSON fields or mandatory report format. Publisher review is pending.

---

## Draft 0.28 editorial cross-reference — preservation scope

The explicit five-case preservation/export matrix in `docs/CONFORMANCE.md` (Draft 0.28) distinguishes Score-only non-lossy operations, partial studio export, descriptor-only asset retention, preservation of genuinely supplied asset bytes and accepted remote-phrase history. This is a cross-reference to a proposed conformance convention, **not** a new JSON field or standard project archive. All wording remains subject to publisher adoption and rights clearance.

---

## OSTF Production Session Profiles 0.1.0 / 0.2.0 — Proposed normative specification

**Status: Draft 0.29 editorial edition, experimental, not publisher-ratified.** Section 1–11 records legacy Profile 0.1 rules; Section 12 onward is the proposed Profile 0.2 addition. A `profileVersion` explicitly selects the exact schema; do not reinterpret a 0.1 document as 0.2 merely by ignoring unknown keys. In 0.2 the `audioTrack` type and additional audio/sidechain rules extend the channel semantics below without altering any 0.1 payload.

## 1. Purpose and position

The optional **OSTF Production Session Profile** describes portable production-session settings for an application that uses an OSTF 4.3 score: track mixer settings, audio channel destinations, ordered instrument/effect devices, opaque plug-in state references, buses, sends, and time-based automation. It enables an independent commercial or open-source third-party host to **record the intended session configuration**, not to execute plug-ins by virtue of parsing JSON. The word *Session* here means a persistent studio project configuration, **NOT** the mutable live **OSTF Distributed Session Profile 0.2** used for remote performance. Implementations MUST distinguish these profile names and version numbers.

The OSTF score (`.ostf`) is immutable relative to this profile. A production profile is a separate UTF-8 JSON document, normally stored as `song.ostfprod.json`; this filename is a convention and not a new registered file type. Its required root tokens are `profile:"OSTF-Production-Session"`, `profileVersion:"0.1.0"`, `score`, and nonempty `channels[]`. The structural authority is `schema/ostf-production-session-0.1.schema.json`. This document is the proposed cross-reference/semantic authority. More advanced audio editing, sampler libraries, render engines, plug-in UI layouts and native host projects are **not** fully represented in 0.1. Companion profiles may coexist without one implicitly altering the other.

## 2. Score binding

`score.formatVersion` MUST be `4.3.0`. `score.sha256` is the lowercase hexadecimal SHA-256 over the **exact UTF-8 original byte sequence** of the referenced `.ostf` score. JSON reformatting alters this value. Optional `score.documentId`, `score.revisionId` must match declared OSTF Core `document.id` and `document.revisionId` when included. Optional `score.sourceUri` is an informational locator; it MUST NOT be implicitly fetched. A consumer with both documents MUST reject a digest mismatch rather than silently attaching the production settings to a different score revision. Hashing alone does not authenticate the publisher or grant plug-in execution permission.

Track channels reference existing **Core** `tracks[].id` using `trackId`. Names are never identifiers. A 0.1 profile maps at most one production channel to any one OSTF track. A production channel may be absent for a Core track; this omission does not mean mute. Track `enabled` and `clip.enabled` describe **musical/source participation**; channel `mute` describes the audio mixer's runtime signal state; `solo` describes the mixer's audition-selection state. **These three are not interchangeable.**

## 3. Channels, Mute/Solo, Gain and Pan

`channels[]` defines track channels, bus channels and exactly one `kind:"master"` channel. `id` is the profile-local identifier, not a Core Track ID. Every track channel MUST carry a valid `trackId`; non-track channels MUST NOT. Master MUST omit `outputChannelId`; every other channel MUST route to an existing bus or master. The combined output/send routing graph MUST be acyclic, and sends MUST target a bus. These are 0.1 portability constraints, not claims about what a specific DAW can route.

Each channel declares `audioChannels` (1 or 2), `gainDb` (-120…+24 dB, with 0 dB as unity), `pan` (-1 left, 0 center, +1 right, stereo balance/mono pan intent), and three explicit booleans `mute`, `solo`, `soloSafe`. **No omitted-value mixer defaults are inferred**. A `mute:true` channel is intended not to contribute audible output, including through its sends. `solo` denotes user-authored audition intent and `soloSafe` marks channels meant to remain auditionable during an external solo. Exact host-specific bus-solo, pre-fader mute and sidechain behavior can vary; applications MUST disclose any incompatible rendering behavior and preserve the authored settings. The Profile does not certify identical signal output in different hosts.

A Core Track's `midiEvents` CC7 (volume), CC10 (pan), CC11 (expression), CC91/93 (effects sends) remain part of the **instrument/MIDI stream** and MUST NOT be rewritten as production `gainDb`, `pan` or `sends`. Conversely, a mix control does not replace MIDI events. No implicit double-application, CC emission or DAW internal routing is prescribed by the data format.

## 4. Ordered device chains and plug-in identity

Every channel's `deviceIds[]` is an **ordered** list of unique references to `devices[]`. Every declared device MUST belong to exactly one channel chain in Profile 0.1. This is the portable processing order. Only track channels may include an `instrument` device; if present it MUST be first and there MUST NOT be more than one on that channel. Effect and utility devices may follow in order, and bus/master channels may contain effect/utility devices. Plug-ins in parallel racks, nested containers or instrument layers are future candidates, not silently mapped to a serial chain.

A device has `role` (`instrument`/`effect`/`utility`), `enabled`, `bypass`, `plugin`, optional `stateAssetId`, and optional `onUnavailable`. `plugin.format` is one of `vst2`, `vst3`, `clap`, `au`, `aax`, `builtin`, `hostNative`, `other`; `plugin.pluginId` is a **format-scoped opaque identifier**, **not** a universal name or filesystem path. A plugin name or vendor label is descriptive only. `plugin.version` is descriptive, not sufficient to establish state compatibility. `builtin` and `hostNative` require a stable vendor/host namespace by agreement, not universal interoperability. AU and AAX are retained as descriptors; their actual host support depends on the platform and licensing.

`enabled:false` means a device is not participating in the authored chain. `bypass:true` denotes an active slot whose processing is bypassed. They MUST NOT be conflated, and neither is the Core Track `enabled`. A reader MUST NOT instantiate or execute a plug-in solely because its record is present. Plug-in discovery, legal licensing, sandboxing and permission are host responsibilities.

## 5. Plug-in state and assets

The Profile does **not** standardize a plug-in vendor's private binary state format. Instead, `stateAssetId` references a typed `assets[]` entry of `purpose:"pluginState"`, whose `uri` points to a blob stored in a containing project bundle or at an explicitly authorized HTTPS location. `sha256` covers its exact bytes; `byteLength` is optional. Assets may also reference rendered audio or other supplemental media, but 0.1 does not define an audio clip/region timeline. Local asset paths use bundle-relative POSIX separators, and MUST reject path traversal, absolute filesystem paths or `file:`/`javascript:` URIs. HTTP(S) fetch, file reads and plugin-state loading are always subject to host permission and trust policies. This JSON alone is not an instruction to fetch or execute code.

The `onUnavailable` preference can be `reportAndPreserve`, `preserveAndBypass`, or `preserveAndSilence`. It describes a preferred *degraded import representation*, **never** a promise of equivalent sound. A host that cannot load a plug-in SHOULD retain its identifier, bypass/enabled flags and opaque state asset reference without altering them, and MUST report that the original DSP is unavailable. It MAY render silence or bypass an effect if consistent with the explicit authored preference and disclosed to the user. It MUST NOT silently use an unrelated installed plug-in with a similar name. A data-only reader can keep every unknown state byte and device descriptor without being a plug-in host.

For VST3, the component and controller state streams have distinct persistence roles; a host-side adapter decides how to store/replay the vendor-defined stream(s). For CLAP, the state extension likewise serializes implementation-defined state. OSTF does NOT impose a common binary representation across VST3, CLAP, AU or AAX. See https://steinbergmedia.github.io/vst3_dev_portal/pages/FAQ/Persistence.html and https://github.com/free-audio/clap/blob/main/include/clap/ext/state.h for reference.

## 6. Output buses and sends

`outputChannelId` expresses the channel's normal downstream audio destination. The master channel is the terminal logical destination; connection to the computer's physical audio output is outside the Profile. `sends[]` entries contain `id`, a bus `targetChannelId`, send `gainDb`, `preFader`, and `enabled`. Sends reference a bus (not an arbitrary plug-in or the Core logical MIDI bus). No graph cycle is permitted across **either** the output links or sends. 0.1 does not represent explicit feedback routing, sidechain key-input mappings, surround speaker assignments, instrument sidechains or parallel wet/dry graphs. A host unable to represent a route MUST report the loss and preserve the record.

A `midi.buses[]` Core logical MIDI Bus is **not** an audio bus in this Profile. No physical port or OS device is serialized here.

## 7. Automation

`automation[]` contains unique automation IDs, a target, `valueType` (`number`/`boolean`), `interpolation` (`step`/`linear`), and nonempty `points[]` of `{atTick,value}`. A target is either a `channel` `gainDb`/`pan`/`mute` control, or a `device` identifier plus its implementation-defined `parameterId`. Each target may have at most one automation lane in Profile 0.1. Points MUST be strictly ordered by unique, nonnegative **Core global source ticks**. They are source-time musical instructions, and reoccur when a finite Performance Plan repeats a source range. No other clock domain is invented. When applying a Plan source cut, initial automation state MUST be resolved from the effective source value at the segment start; previous Visit state MUST NOT leak across the cut.

- Channel `mute` automation MUST be `boolean` and `step`.
- Channel `gainDb` and `pan` automation MUST be numeric and within channel bounds.
- Device automation MUST be numeric with values normalized to `[0,1]` and mapped to the plug-in's parameter space only by a capable adapter. Stable vendor parameter IDs are **not standardized** by OSTF. A host unable to map a parameter MUST preserve it and report that automation was not applied.
- For a numeric lane, linear interpolation occurs between points; values before the first point retain the static parameter if defined, and values after the last point hold the final point. A boolean step lane holds its last known point; before its first point the static value applies. At the same Tick, an authored automation point takes precedence for **that controlled mixer/parameter value**, but does not rewrite an opaque plug-in state blob or Core MIDI Events.

Automation `solo` is intentionally **not** defined in 0.1: Solo is an audition flag and host implementations differ in real-time routing behavior. Do not silently repurpose a mute automation as solo automation.

## 8. Host extensions and lossless preservation

`hostExtensions[]` is optional and carries `{namespace, version?, data}`. `namespace` is an independently controlled reverse-domain identifier (e.g. `com.example.myhost`) and `data` is inert, non-executable JSON. Host extensions must never override the standard Core, `channels`, `devices`, `assets`, or `automation` authority without explicit import logic and a documented conflict policy. Applications claiming lossless round-trip MUST preserve unsupported standard fields and unknown extension objects (and external assets they manage), or decline destructive overwrite. Host extensions do not create a new musical timeline or authorize external actions.

## 9. Bundling and file interchange

For a portable deliverable, a producer MAY distribute a ZIP containing `score.ostf`, `production.ostfprod.json`, and `assets/*`. This is an **illustrative bundle convention**, not a new registered OSTF file extension or guaranteed DAWproject-equivalent package. Each file remains independently identified and integrity-checked; packaging MUST NOT rewrite the pinned score bytes without updating `score.sha256`. Source URI, relative profile paths, and asset URLs are data only. Cross-host load and licensing must be explicitly handled by the recipient. It is acceptable to ship a score without this Profile; consumers which only understand Core 4.3 MUST be able to ignore the companion document.

## 10. Compatibility, errors, security and conformance

This optional Profile does not alter `schema/ostf-4.3.0.schema.json`, original OSTF 4.2 inherited definitions, or the independently versioned Distributed Session Profile 0.2. An implementation MAY support score-only, production-data reading, production-data writing, or plug-in host restoration independently; capabilities MUST be described accurately. Example diagnostics include `E-PRODUCTION-SCORE-MISMATCH`, `E-PRODUCTION-TRACK-UNKNOWN`, `E-PRODUCTION-DEVICE-DUPLICATE`, `E-PRODUCTION-STATE-MISSING`, `E-PRODUCTION-ROUTE-CYCLE`, `W-PRODUCTION-PLUGIN-UNAVAILABLE`, `W-PRODUCTION-LOSSY-AUTOMATION`.

The supplied Python `tools/validate_production_profile.py` checks structural and selected reference/routing constraints only. It does **not** open a plug-in host, emulate a DSP engine, authorize a third-party resource fetch, validate vendor state, certify a compatible DAW, or prove remote robot/WAN behavior. Runtime verification remains explicitly outside the user's requested release gate; no such verification is claimed.

## 11. Relationship to other industry formats

DAWproject has concrete project/mixer/device models including inserts, sends, mute, pan and plug-in state. The OSTF Profile does not copy its XML/XSD or promise identical exchange; a third-party adapter MAY convert compatible fields and MUST explicitly report data that cannot be represented. DAWproject is especially relevant where detailed audio clip/DAW-project transfer is required. Its authoritative public implementation reference is https://github.com/bitwig/dawproject/blob/main/Project.xsd.

## 12. Production Session Profile 0.2 — extension and scope (Draft 0.15)

Profile 0.2 is a **separate, explicitly versioned** optional JSON studio-session document: `profile:"OSTF-Production-Session"`, `profileVersion:"0.2.0"`, and `score` pinned exactly as in 0.1. Structural authority: `schema/ostf-production-session-0.2.schema.json`. Profile 0.1.0 remains separately readable and its exact schema is retained. All old 0.1 semantics for Score, explicit Mixer state, serial Device chains, assets, bus output, sends, automation and inert vendor extensions continue to apply except where this 0.2 section explicitly extends them.

0.2 adds three independent capabilities: (i) a **production-only** `audioTrack` Channel without an OSTF Core Track; (ii) `audioRegions[]` referring to byte-pinned, decoded-frame-addressable `audioSource` assets; and (iii) `sidechainConnections[]` targeting an effect's explicitly named input port. Neither new array is required. An application can author a complete 0.2 document without audio Regions, sidechains or any known plug-ins. Existing Core 4.3 (127 `$defs`), Distributed Session Profile 0.2 (16 `$defs`) and the inherited 4.2 score remain unaffected.

The 0.2 portability subset is deliberately mono/stereo, fixed-channel, source-tick-based, serial effect chains and acyclic signal dependencies. *Not* standardized here: multi-point warp maps, external timecode or sample-accurate synchronized recording, looping audio source material, comp takes, surround/ambisonics, parallel plug-in racks, hardware mixer control, oscillator/DSP internals, latency-compensation values, automated sample-rate conversion algorithms, and guaranteed identical audio output. Applications MAY maintain those in non-executable `hostExtensions`, but MUST report loss when translating to a profile that cannot represent them.

## 13. Production-only audio tracks and score-bound tracks

In 0.2, `channels[].kind` additionally permits `audioTrack`. It is a studio recording/mixing channel with its **own production Channel ID**, intentionally not an OSTF Core Track. Such a channel MUST omit `trackId`; `kind:"track"` still MUST resolve `trackId` to an existing Score Track. `bus` and `master` also have no Core `trackId`. Production audio-only channels are not implicitly added as a Core music Track or given a `playingRole`, chord, melody, lyric, or generated Note.

`audioRegions[].channelId` MUST refer to `track` or `audioTrack`; placing an audio Region on a Bus or Master is not standardized in this subset. The former allows audio on a source-bound Score Track; the latter allows recording-only studio material without corrupting the Core. A Core MIDI instrument and a Production audio Region on the same `kind:"track"` Channel may coexist; their *audio outputs* are summed at the input of the subsequent serial effects on that Channel, while MIDI control routing is unchanged. Source audio does not become MIDI Notes or a separate Core Clip. The order of input summation is not an additional signal-processing effect.

Production Channel `mute` and Solo audition state remain distinct from the Score's `tracks[].enabled` and from Region-level `mute`. A muted Region contributes no output; it does not mutate Score Notes. Multiple Regions on one track MAY overlap; their decoded audio is summed and each Region keeps its own envelope.

## 14. Audio asset identity, exact bytes, and decoded frame metadata

For `purpose:"audioSource"`, an `assets[]` object MUST contain all of `uri`, SHA-256 of exact *original encoded bytes*, `mediaType`, `sampleRateHz` (>0), `frameCount` (>0), and `audioChannels` (1 or 2). `byteLength` remains optional. `frameCount` is the number of **decoded sample frames** in the entire source asset (one frame per time instant including all audio channels; not the number of individual channel samples). `sampleRateHz` describes decoded frames per second, not a rendering device's output clock. Per-Region trim offsets are measured in integer decoded source frames.

A consuming host MUST check SHA-256 against bytes it actually obtains through an authorized, non-traversing path, and MUST report a mismatch between declared frame format/count and the decoder result. WAV is used for the synthetic example; the schema does not force a particular audio codec, and no universal set of codecs is guaranteed. A file can pass JSON structure checks yet be unavailable, undecodable or unacceptable to a host. A host MUST NOT fetch external URIs merely because they occur in a JSON file, and MUST NOT execute plug-in state or binaries merely because they are referenced. Mono/stereo mismatch between Region source and Channel has no implicit upmix/downmix in 0.2: it requires an explicit host-specific lossy decision or rejection.

No asset in 0.2 defines copyright authorization, model weights, plug-in license ownership or the right to redistribute a recording. Any of these concerns remain publisher/host responsibilities.

## 15. Audio Regions: timeline, trims, playback modes

`audioRegions[]` contains uniquely identified objects with `channelId`, `sourceAssetId`, `startTick` >= 0 and `durationTicks` > 0 on the **original OSTF source-score global Tick timebase**. An item additionally declares `sourceStartFrame` >= 0 and `sourceFrameCount` > 0; their sum MUST NOT exceed its Audio Asset's `frameCount`. No negative score-absolute start positions are standardized for 0.2 Regions. A Region covers the half-open `[startTick,startTick+durationTicks)` interval. The source file itself is *not* embedded in the `.ostf` Core.

`playbackMode:"native"`: first frame is the selected `sourceStartFrame` at `startTick`. Frame position progresses at the declared **native sample rate**, using the time elapsed in seconds computed by integrating the effective source OSTF `timeline.tempoChanges` and Score `ppq`. Playback stops when the selected source frame window ends **or** when the Region ends, whichever comes first; any remaining Region tail is silent. Native mode never silently loops/stretches and MUST NOT carry `pitchPolicy`. A tempo map that cannot resolve elapsed source time is not a basis for guaranteed sample-accurate audio playback; report this rather than inventing an unstated BPM.

`playbackMode:"fit"`: maps musical source Tick progress *linearly* across the Region's selected frame interval: selected frame position = `sourceStartFrame + sourceFrameCount × ((tick-startTick)/durationTicks)`. Exact implementation rounding of fractional frame positions is renderer-dependent; do not claim acoustic or sample-bit identity. Fit MUST declare `pitchPolicy`: `preserve` (keep original perceived pitch while adjusting duration, if an available algorithm can achieve it) or `followRate` (pitch changes with effective playback-speed adjustment). This is semantic intent; it is NOT a normative DSP stretch/resampler algorithm. Applications unable to reproduce this intent MUST preserve the instructions and describe an approximation or omission. Tempo changes can alter speed in wall-clock time but never alter authored source Tick positions.

For both modes, region `gainDb` -120..+24 dB is a per-Region amplitude multiplier before the channel effects and mixer fader, and `mute` is an independent Region boolean. Absence of a Region does NOT imply a muted Track, and an asset may be reused by many Regions without duplicating bytes.

## 16. Fades, selected Performance Plan ranges and authority

Optional `fadeInTicks` / `fadeOutTicks` default to **zero** when absent. A fade is linear in amplitude relative to its *original Region-local Tick* start/end boundary; the maximum of `fadeInTicks + fadeOutTicks` MUST NOT exceed `durationTicks`. With fade-in of positive duration, amplitude starts at zero and reaches full Region gain at `startTick + fadeInTicks`; fade-out starts at `endTick - fadeOutTicks` and approaches zero at the excluded Region end. No nonlinear crossfade law or automatic overlap crossfade is specified. When Regions overlap, summing them is permitted without implied normalization.

A Performance Plan Visit that selects only part of a source interval projects the **intersection** of the Region range with the selected source range into that Visit. The Region's original source-frame mapping, original fade position and ID remain authoritative; do not restart the Region or its fades at every Visit cut. A Region is re-encountered in each Visit selecting that source range. The Studio Profile projection is *not* remote Distributed Session `phraseCommitted` activity, and Core `realization:"open"` does not grant permission to record a new Session phrase or silently delete a separately authored production Region. Audio arrangement revisions are explicit Production Profile edits; they never modify immutable Score Notes.

If a source cut requires audio sample reconstruction or tempo information that the target host cannot resolve, the importer MUST warn, preserve the authored Region, and decline claiming a lossless rendered result. A Production Profile export to Score-only is lossy whenever it contains Regions even if the Score hash remains unchanged.

## 17. Sidechain signal inputs and no-feedback routing

`sidechainConnections[]` is a separate optional directed signal-dependency set, **not** another audible output Channel or a MIDI Bus. Each Connection requires unique `id`, `sourceChannelId`, `targetDeviceId`, opaque `targetPortId`, `tapPoint` (`preFader`/`postFader`), `followMute`, `gainDb`, `enabled`. The source MUST be a non-master channel; the target MUST be an `effect` Device that belongs to exactly one Channel chain. The target's owning Channel MUST be different from the source. At most one source may address a given `(targetDeviceId,targetPortId)` in the 0.2 portability subset; to combine multiple sources, route them through an explicit Bus and use one Connection.

`tapPoint:"preFader"` obtains post-serial-Device audio **before** Channel fader/pan; `postFader` obtains it after Channel gain/pan. `followMute:true` applies source Channel `mute` to the key signal; false allows a muted-audible source to retain detector signal. `gainDb` applies to the sidechain key only and does not affect audible Channel output. Core `MIDI CC` and `Track.enabled` remain independent; disabled music-source tracks do not generate audio by virtue of a Connection. Sidechain inputs to missing plug-in ports are unresolved, not auto-mapped to a similarly named input.

The dependency graph formed by all audio `outputChannelId`, `sends[].targetChannelId`, and sidechain links from source Channel to the Channel containing the target Device MUST be **acyclic**. Self-sidechain, feedback paths and implicit DSP delay loops are outside this portable Profile. Target Device bypass/unavailable state may prevent actual key processing; the Connection is still retained as authored metadata. No guaranteed sidechain timing, PDC, lookahead or detector response is implied.

## 18. Migration, preservation, conformance and errors

A valid 0.1 document may upgrade to 0.2 by changing only `profileVersion`, **after** checking 0.2 Schema and semantics; new optional arrays, audio-only Channels and assets are NOT invented. The original 0.1 document remains valid as 0.1. A 0.2 document can downgrade to 0.1 *without information loss* only if it has **no** `audioTrack` Channels, `audioRegions`, `sidechainConnections`, `audioSource` assets or other 0.2-only fields. In that case, omit empty 0.2 arrays, relabel version and revalidate. Otherwise, a consumer MUST report the exact discarded features or refuse the downgrade; it MUST NOT lie about a lossless 0.1 round-trip. Both Profiles remain separately versioned and no hidden auto-migration takes place on JSON parse.

Example messages: `E-PRODUCTION-AUDIO-ASSET-UNKNOWN`, `E-PRODUCTION-AUDIO-FRAME-RANGE`, `E-PRODUCTION-AUDIO-CHANNEL-MISMATCH`, `E-PRODUCTION-REGION-FADE`, `E-PRODUCTION-SIDECHAIN-PORT-DUPLICATE`, `E-PRODUCTION-DSP-CYCLE`, `W-PRODUCTION-STRETCH-UNSUPPORTED`, `W-PRODUCTION-PORT-UNAVAILABLE`, `W-PRODUCTION-DOWNGRADE-LOSS`. Structural validation and cross-reference/semantic validation are separate; only the latter has access to a pinned Score and external asset bytes. 0.2 compatibility means accurate interpretation and loss reporting, **not** bit-identical audio or successful plug-in hosting.

The `tools/validate_production_profile.py` helper accepts Profile 0.1.0 or 0.2.0 by explicit version and implements selected static checks. It does not inspect every audio decoder/DAW/plugin DSP implementation; a successful result must never be described as a third-party renderer/interoperability or live robot/WAN test. All such tests remain excluded from the user's publication decision. The new 0.2 meanings remain **not ratified** pending explicit author approval, bilingual editorial sign-off and verified publication rights/licensing.

## 19. 0.2 feature ownership matrix (not a host conformance claim)

| Task | Score 4.3 Core | Production Profile 0.1 | Production Profile 0.2 | Host-native / external |
|---|---|---|---|---|
| Chords, sections, MIDI, lyrics | **Authoritative** | Pin Score only | Pin Score only | Rendering |
| Mixer Solo/Mute, gain, pan, Bus/Send | No | Authored data | Inherited unchanged | Audition / signal flow |
| Instrument and FX chain/state | No | Ordered chain, opaque hashes | Inherited unchanged | Plug-in discovery, DSP, vendor license |
| Audio-only studio track | No | Not represented | **`audioTrack`** | Recording device/monitor |
| Audio clips / trims / fades | Core Resources only | Not represented | **`audioRegions`** | Decoder and sample rendering |
| Fixed-rate vs time-fit / pitch intent | No | Not represented | **`native` / `fit`** | Resampling/stretch algorithm |
| Sidechain input/key port | No | Not represented | **`sidechainConnections`** | Actual plug-in key port/DSP |
| Remote AI/physical robot session | Planned musical intent | Not represented | Not represented | **Distributed Profile 0.2** + Transport/Safety |

## 20. 0.2 sample inventory (illustrative, invented)

- `examples/production/01-track-mixer-plugin-chain.json`: 0.1 Mixer/plug-in chain, synthetic nonfunctional state bytes.
- `examples/production/02-unavailable-plugin.json`: 0.1 missing plug-in preservation policy.
- `examples/production/03-audio-regions-sidechain-02.json`: 0.2 `audioTrack`, native and fit audio Regions, original WAV test tone, sidechain detector routing to a fictitious plugin port.
- `examples/production/assets/example-audio.wav`: small original synthetic waveform; *not* a commercially licensed recording or an example of verified time-stretch output.
- `tests/invalid/07-production-invalid-bus.json`: intentionally invalid 0.1 channel routing fixture.

A 0.2 Writer MUST NOT invent a valid sidechain plugin port merely from a readable `plugin.name`. The sample `org.example.demo.sidechain-compressor` and its `key` port are fictional identifiers used to demonstrate serialization only.


## 21. Production Profile 0.2 automation targets — Draft 0.15 normative proposal

This pre-release update expands **only** `schema/ostf-production-session-0.2.schema.json`; the published-score Core, separate Distributed Session Profile 0.2 and historical Production Profile 0.1 remain byte-identical to Draft 0.14. Because 0.2.0 is not yet ratified or publicly released, these proposed new 0.2 automation targets are a revision of the candidate, **not** a post-release silent compatibility change. Importers MUST select an exact version and SHOULD report unsupported targets; no automation may be inferred by silently dropping an unfamiliar target.

In addition to existing `kind:"channel"` (channel `gainDb`, `pan`, `mute`) and `kind:"device"` (normalized opaque plug-in parameter), 0.2 adds the following mutually exclusive typed `automation[].target` choices:

| Target | Required identity | `parameter` choices | Value type / baseline |
|---|---|---|---|
| `kind:"send"` | `sendId` | `gainDb`, `enabled` | dB number (-120..+24) or boolean; `channels[].sends[]` static value |
| `kind:"audioRegion"` | `audioRegionId` | `gainDb`, `mute` | dB number (-120..+24) or boolean; `audioRegions[]` static value |
| `kind:"deviceControl"` | `deviceId` | `enabled`, `bypass` | boolean; `devices[]` static value |

Every identity MUST resolve to the actual owning object in this **Production Profile**; a `sendId` is unique across all Channels. `deviceControl` flags are portable slot/processing intent rather than a vendor-defined plug-in parameter; they MUST NOT be misinterpreted as `kind:"device"` `parameterId` values. No second Automation lane for the same exact typed target is valid. An Automation lane does not create or remove a Send, Region, or Device. The Studio Profile remains the only source for Mixer/FX targets; OSTF music Core notes, MIDI CC, Lyric and Score provenance are unaffected.

All Automation points remain at **global original Score source Ticks** and MUST have strictly increasing, unique Tick positions. Boolean targets MUST use `valueType:"boolean"` and `interpolation:"step"`; numeric targets MUST use `valueType:"number"`. Channel Pan is [-1,1], gain values in dB are [-120,+24], and a plug-in `kind:"device" numeric parameter stays normalized [0,1]; no implicit plug-in normalization for Send/Region/Device-control targets.

Before the first point, the target's explicitly stored static value is effective (a device plug-in parameter with no known static value remains unspecified). A point at Tick T takes effect **at** T. `step` holds the most recent authored value until the next point; numeric `linear` interpolates only inside adjacent point intervals; after the last point, hold the final point. Any `audioRegion` lane is audible only within the owning Region's half-open lifetime; points outside that lifetime remain portable data and MUST NOT create audio or extend the Region. Source cuts and Performance Plan Visit repeats re-evaluate the value from **source time**; previous Visit's live value MUST NOT leak through a cut. A region-level gain/mute automation is resolved together with original Region-local fade/trim but never rewrites it.

`send.enabled:false` suppresses that Send regardless of gain automation; `audioRegion.mute:true` suppresses that Region even if its gain is automated. Device `enabled:false` makes its slot inactive; when active and `bypass:true`, the slot bypasses processing. Both author-set flags are retained even if a host cannot realize the requested processing. Automation does not override Core musical `track.enabled`, does not imply a Solo change and does not authorize plug-in state execution. A Reader lacking any new target MUST preserve the entire lane in non-lossy save and disclose the missing behavior. The down-conversion to Profile 0.1 is **lossy whenever any `send`, `audioRegion` or `deviceControl` Automation target is present**, even if it contains no Regions or sidechains. 0.1 instruments MUST NOT be silently re-labelled 0.2 data.

Illustrative Profile 0.2 example: `examples/production/03-audio-regions-sidechain-02.json` now contains valid Send gain/on, Region gain/mute and Device enabled/bypass Automation targets. Structural and selected cross-reference checks are authoring aids only, not runtime host/DAW or plug-in tests.


## 22. Portable mixer, Solo/Solo Safe and production-source authority — Draft 0.16 candidate

This section **proposes** an explicit, deterministic *audition-source selection baseline* for the still-unpublished **Production Profile 0.2.0**. Earlier 0.1 files and their Schema remain unchanged; interpreting 0.1 with this newly proposed 0.2 rule is **not** a conforming automatic upgrade. The actual plug-in DSP sound, pan law, bus-latency compensation and sampling are host responsibilities; the following selection rules only define which musical or audio sources may contribute in principle.

### 22.1 Source types and independent authority

- A **source channel** is a `channel.kind:"track"` or `"audioTrack"` record. `"bus"` routes/mixes existing signals; `"master"` is the terminal output and is not a source.
- For a score-bound `"track"` channel, the OSTF score's `track.enabled`, each `clip.enabled`, concrete Notes and MIDI Events determine participation of the **score-derived** input only. The Production Profile MUST NOT override or rewrite them. An independently authored Production `audioRegion` on that same channel remains eligible as an audio source even if the score Track is disabled: only its own source interval, `mute` and profile channel processing affect it.
- An `"audioTrack"` has no Core `trackId` and contributes only Production audio regions or intentionally host-native content. The mere existence of a channel does not create audible content.
- Channel `mute`, Send `enabled`, Region `mute`, Device `enabled`/`bypass` and time-varying Automation control distinct layers. `solo` and `soloSafe` are *authored audition flags*, not source note editing, generator instructions, MIDI CC messages or authority to load a plug-in. Master `solo`/`soloSafe` flags do not select musical sources and SHOULD be `false`; for preservation, a Reader MUST NOT silently change an authored historical value.

### 22.2 Selected source channels under Solo (portable 0.2 rule)

1. Form the directed **audible routing graph** from `outputChannelId` edges plus Sends whose `enabled` is true at the queried **source Score Tick** (resolve `send.enabled` Automation first using Section 21). This graph excludes sidechain key paths and is acyclic per Section 17. Channel `mute` does not erase graph identity; muting is applied afterward.
2. Define the set `S` of channels with `solo:true` and `kind != "master"`. If `S` is empty, all source channels are *selected*, regardless of `soloSafe`.
3. If `S` is nonempty, a source channel `c` is selected if **(a)** it has `solo:true`, **(b)** it has `soloSafe:true`, or **(c)** it can reach at least one `solo:true` **bus** through the directed audible graph. A solo-safe bus does *not* by itself select unrelated upstream sources. An isolated soloed bus with no enabled upstream path does not invent audio.
4. All outputs and enabled Sends of a selected source remain eligible for audible routing, subject to actual source availability, channel/Region mute and downstream routing. Thus a soloed Bus may select an upstream source whose direct dry output is also eligible; a host with wet-only bus Solo MUST disclose its deviation and preserve the authored state rather than claiming equivalent rendering. Transit buses, including solo-safe effect returns, MAY carry only the signals of selected, unsuppressed sources. `soloSafe` on a bus means preserving that bus/return against native-host solo gating; it MUST NOT restore audio from an unselected source.
5. Source eligibility is recalculated when an automated Send `enabled` change alters reachability or a Performance Plan Visit re-enters a source interval. A previously selected state MUST NOT silently persist after a source cut or a different Visit. In 0.2, `solo` and `soloSafe` themselves are **static, non-automatable fields**.

This rule describes an explicitly portable **selection** subset. If a host implements different bus-Solo, solo-safe, pre-fader audition, or multi-output policies, it MUST preserve all authored values and report the incompatible audition behavior. Two hosts complying with the JSON format alone are not guaranteed sample-identical or perceptually identical output.

### 22.3 Mute, Sends, key inputs and signal-flow boundaries

- Resolve an active source's Production Region gain/mute/fade and its score material independently; sum participating sources at that channel's input before its serial Device chain. Score Track `enabled:false` excludes score-derived input, **not** separately authored Production Regions on the same channel.
- Within the portable 0.2 subset the signal order is: **source inputs → serial Devices → pre-fader tap → gain/pan → post-fader tap → audible output/Sends and terminal Master**. Sends with `preFader:true` take the pre-fader signal; `preFader:false` uses the post-fader signal. Neither reinterprets MIDI CC7/CC10/CC11 as mixer controls. The exact stereo panning law and device DSP are host-specific and MUST NOT be claimed interchangeable.
- Effective `channel.mute:true` suppresses all **audible** output and Sends from that channel, regardless of pre/post-fader placement, even when `solo:true`. A muted Bus similarly cannot restore audible output downstream; Solo never overrides Mute. Disabling a Send suppresses that edge, even with gain Automation. An inactive Device and a bypassed Device remain distinct from channel Mute.
- Sidechains are detector/key paths, never audible output paths and never a means of selecting source channels. `followMute:true` suppresses the key when its source Channel's effective Mute is true. `followMute:false` allows key input from the still-available upstream signal despite that channel's Mute; this flag does **not** restore an unselected source or score input disabled by the Score. Source Solo eligibility is respected for sidechain feed in this portable subset; a host with a different key-listening policy MUST disclose it. `sidechainConnection.enabled:false` always suppresses that detector path.
- The Master receives the routed eligible signals, applies its gain/pan where supported and `mute`, and is the only audible terminal. A master `solo:true` cannot force disabled/unselected inputs to sound. These are interchange selection semantics, not a universal signal-processing implementation.

### 22.4 Original file paths and safe asset boundaries

A relative `asset.uri` is resolved only below the directory of the Production Profile document after path normalization and symbolic-link resolution. An importer MUST reject relative asset paths that escape the package root, **including** paths that appear safe lexically but traverse a symbolic link to an outside file. Relative path checking and SHA-256 do not authorize access to an external filesystem. External HTTPS URIs remain data and MUST NOT be auto-fetched. The included Python authoring aid now checks resolved relative-path containment as a basic safety guard; no claim of complete security auditing is made.

### 22.5 Worked source-selection cases (source eligibility only)

| Authored mix state | Selected source channel IDs | Limitation |
|---|---|---|
| No `solo:true` channels | All `track` and `audioTrack` source channels | Mute/region/score source gating still applies |
| Sample `03-audio-regions-sidechain-02.json` (`sax-channel.solo:true`, `reverb.soloSafe:true`) | `sax-channel` | Solo-safe Bus does not independently restore piano send |
| `reverb.solo:true` with piano's Send enabled, no other solo and no source soloSafe | `piano-channel` | Portable baseline also allows piano's dry path; wet-only host must report difference |
| `reverb.solo:true` but piano Send disabled at a source Tick | None via that Bus | Reachability changes with Send Automation |
| `sax-channel.solo:true`, `piano-channel.soloSafe:true` | `sax-channel`, `piano-channel` | Channel mute can still suppress either |

The helper's optional `--explain-audition --at-tick N` displays this *static/source-tick* selection model and is not a DAW renderer, signal analyzer or runtime conformance test. This addendum introduces no new JSON fields and leaves all six existing Schemas byte-identical to Draft 0.15. **Publisher ratification is still required.**

## 23. Safe Asset URI decoding and Score Plan / Production-source boundary — Draft 0.17 candidate

### 23.1 Cross-platform relative `asset.uri` interpretation

A bundle-relative Asset URI is a **URI path**, not a raw operating-system path. For both Profile 0.1 and 0.2, the normative portability candidate is: (1) reject a URI that declares an unexpected scheme, authority, query or fragment; only explicitly authorized external HTTPS may remain external; (2) split the relative URI using **literal `/`** into nonempty components; (3) reject malformed `%` escapes and decode each component **exactly once** as strict UTF-8; (4) reject the resulting `.` and `..` components, encoded `/` or `\\`, residual `%` (including `%252e` double-decode ambiguity), controls, leading/trailing spaces, trailing dots, colon and other Windows-reserved filename characters, and device names such as `CON`/`NUL`; (5) join the decoded components below the directory containing the Production Profile, resolve symbolic links and reject any resolved path outside that root; (6) check original-byte hashes only after a separately authorized file read. Do not Unicode-normalize, percent-decode twice, map a filesystem drive, or fetch an external URL on JSON import. An implementation unable to represent the filename safely MUST retain the original URI as data and report that it cannot resolve the Asset. Percent-encoded internal spaces are permitted (`assets/My%20Take.wav` → a file named `My Take.wav`); raw spaces are not.

| Illustrative relative URI | Interpretation |
|---|---|
| `assets/take.wav` | Allowed; bundle-relative file |
| `assets/My%20Take.wav` | Allowed; decode exactly once to `assets/My Take.wav` |
| `assets/%2e%2e/private.bin` | Reject: decoded parent segment |
| `assets/%252e%252e/private.bin` | Reject: nested percent-decoding ambiguity |
| `assets/%2Fetc.bin` or `assets/%5cprivate.bin` | Reject: disguised separator |
| `assets/note%FF.wav` | Reject: invalid UTF-8 |
| `assets/CON.txt` | Reject: Windows-reserved filename |
| `assets/link/escape.wav` | Reject if link resolves outside the bundle root |

This does **not** grant authorization to read any bytes, prove ownership or eliminate every platform-specific filesystem risk. The Schema continues to store the original URI string; parsing into a local path is a consent-gated host operation. No new JSON field, Score representation or Profile version token is introduced by Draft 0.17.

### 23.2 Performance Plan `realization` vs. Production audio

The Core `performancePlans[].visits[].parts[].realization` (`fixed` / `open` / `silent`) governs the **Core Score-derived performance** of the referenced Track. It does **not** implicitly rewrite or mute a separately authored `audioRegions[]` Region placed on a Production Channel, even when that Channel is bound to the same Core Track. For example, a Visit declaring a guitar Track `silent` prohibits Score-derived Notes for that Visit but does not by itself suppress an independent studio recording on the guitar Channel. That Region is eligible if its source Tick intersects the Visit and its own Region/Channel/Automation/Mixer conditions permit it. A `kind:"audioTrack"` Production-only Channel never becomes a Core Plan Part merely because it has a similar name.

A Host needing the entire composite audio output silent MUST apply an explicit Production Region or Channel Mute (or an authored Automation lane) in the Production Profile; a Score `silent` assertion is not a hidden Mixer Mute. Conversely, Production Mute does not change Score Notes or turn `open` into `silent`. A consumer that instead suppresses all studio audio on a Score-silent Part MUST report the resulting playback difference and preserve the source data unchanged. These rules preserve one authority for each kind of data and make Plan Visit repetition and studio overdubs unambiguous.

**Editorial and release status:** both clauses are proposed semantics for the unpublished Profile candidate, subject to publisher adoption and bilingual editing. Nothing in this section certifies plugin, DSP, filesystem security, network or robot execution.

## 24. Performance Plan re-entry: Source-Tick automation and Audio Region phase (Draft 0.18 candidate)

### 24.1 Three distinct coordinates and no implicit transport state

This clause applies to the **unreleased Production Session Profile 0.2.0** and clarifies Sections 7, 15, 16, 21–23 without adding JSON fields. **Source Tick** (`t`) is the absolute OSTF score Tick used to author a Production Region or Automation point; **performance Tick** (`P`) is the finite Performance Plan Visit expansion coordinate; actual device/sample clocks are host-managed. For selected source interval `[S,E)` placed at performance interval `[Q,Q+(E-S))`, the relation is `P=Q+(t-S)`. The Profile never stores a new authoritative copy of the source Timeline, and a Visit never edits a Region ID, Automation point, source MIDI stream or Score hash.

### 24.2 Source-range intersection and audio-frame position

A Region with authored source span `[R,R+L)` contributes only over the **half-open intersection** `[max(S,R), min(E,R+L))` when this interval is nonempty. At the projected entry, its source-frame position is evaluated at the **original source Tick** `t=max(S,R)`, *not* reset to `sourceStartFrame` merely because a Visit or a source segment begins. Repeating a Visit that selects the same source span repeats its original Region content from the corresponding source position, not from the previous Visit's runtime cursor.

- For `playbackMode:"native"`, the ideal continuous decoded-frame coordinate at source Tick `t>=R` is `sourceStartFrame + sampleRateHz × T(R,t)`, where `T(R,t)` is elapsed **source-score** ideal seconds, integrating the score's effective tempo over `[R,t)` in original source order: `Σ 60 × deltaTicks/(ppq × bpm)` for each constant-tempo subinterval. `sourceFrameCount` bounds the selected window; at or beyond `sourceStartFrame+sourceFrameCount` the Region yields **no source samples** rather than wrapping or restarting. At a Visit cut, the asset-frame offset is computed using original source time since `R` even if the Plan omitted earlier source ranges; this does **not** add skipped durations to the *expanded performance* clock.
- For `playbackMode:"fit"`, the ideal continuous decoded-frame coordinate is `sourceStartFrame + sourceFrameCount × (t-R)/L`. It too uses original Region-local source position at re-entry or truncation. Actual fractional-frame rounding, resampling/stretching and output are host-dependent; Profile compliance does not certify identical audio.
- The existing `fadeInTicks`/`fadeOutTicks` envelope is evaluated at original Region-local Tick `t-R`. A cut MUST NOT implicitly start a new fade-in or fade-out. A hard cut may be discontinuous; invented smoothing, crossfade or tail playback is a host approximation that MUST be disclosed if claimed as equivalent. Region/Channel `mute` and gain are separately applied as specified in Sections 21–23.
- A Region beginning before a selected source span is **not analogous to a MIDI Note whose attack preceded the cut**: Region samples may be read at the correct later source-frame offset, whereas Core fixed-Note selection does not synthesize a preceding Note On. Likewise, prior MIDI CC/Program state is not auto-restored by this Production rule.

### 24.3 Stateless Source-Tick Automation value at each Visit entry

For every Production Automation lane, determine its effective value as a **function of the queried original source Tick `t`**. This evaluation uses the *entire authored lane*, including points located in source ranges omitted by the current finite Plan; it does not emit those skipped points as new performance events. If a point is at `t`, that point is effective at `t`. Between adjacent numeric points, `linear` uses their source-Tick fraction; `step` holds the most recent point. After the last point hold its value. Before the first point use the target's explicit static property (`channel`, `send`, `audioRegion`, `deviceControl`) when available. For `kind:"device"` numeric plug-in parameters, the portable Profile has **no typed static numeric baseline**; before the first point the value is **unresolved** unless a capable host can interpret the opaque plug-in state. Never infer 0, 0.5, the first point or a previous Visit's value.

At every source cut, Visit restart or backward source jump, re-resolve each controlled parameter using the new source Tick. **No Automation latch survives from a prior Visit**, even when a transition's expanded `performanceTick` is increasing. This includes `send.enabled`, `channel.mute`, `audioRegion.mute`, Device enabled/bypass and gains. For a Region target, applying the value does not create audio outside the Region's own source span. Production Automation is a **continuous/state-value query**, unlike the Core fixed-MIDI event selection (which does not synthesize earlier Program/CC events). Source-tick values are the same in all finite Visits visiting the same source Tick, absent a new explicit Profile revision; Visit-local mixer overrides are not represented by Profile 0.2.

### 24.4 Deterministic editorial examples, not playback evidence

Assume score `ppq=960`, source tempo `120 BPM`, `sampleRateHz=48000`, and a native Region starting at source Tick `0` and source frame `0`. At source Tick `960`, the ideal native frame offset is `48000 × (60/120)=24000`. A Visit selecting only `[960,1920)` does **not** replay frame 0; the frame window may already be exhausted. Likewise a `fit` Region `R=1920`, `L=1920`, `sourceStartFrame=0`, `sourceFrameCount=11025` has ideal frame position `5512.5` at source Tick `2880`, not frame 0 after a cut. Source-frame sample rounding remains implementation-specific.

In the bundled Profile example `03-audio-regions-sidechain-02.json`, `reverb-send-on-automation` sets `enabled:false` at source Tick `7680`. Any Visit re-entering source Tick `7680` or later (until another point changes it) observes the disabled Send, **even if its transition jumped over the point at 7680**. A subsequent Visit returning to source Tick `0` observes the earlier `enabled:true`; there is no previous-Visit latch. The same example's `room-clip-native` has only 11025 decoded source frames at 44100 Hz, i.e. 0.25 s: at 120 BPM and 960 PPQ the media window is exhausted at source Tick `480` despite the Region's authored duration of 960 Ticks. A source selection of `[480,960)` does not restart this recording.

### 24.5 Error disclosure, compatibility and release status

If source tempo required for native frame indexing is undefined, or an opaque plug-in parameter's pre-first-point value cannot be resolved, a consumer MUST preserve the original data and report the ambiguity; it MUST NOT claim fully determined sample rendering. Suggested (informational) diagnostics: `E-PRODUCTION-NATIVE-TEMPO-UNRESOLVED`, `W-PRODUCTION-DEVICE-BASELINE-UNKNOWN`, `W-PRODUCTION-CUT-DISCONTINUITY`, `W-PRODUCTION-VISIT-LOCAL-MIX-UNREPRESENTABLE`. The same caveat applies when a host implements Visit-local Automation, automatic fades or note/mixer-state carryover as a host-specific extension. These 0.18 clauses change **no field names, no Schema byte hashes, no Production Profile version** and do not imply independent parser, DAW/DSP or robot/WAN verification. **Publisher adoption and bilingual editorial approval remain pending.**

## 25. Co-binding a Production Profile with a Distributed Session (Draft 0.19 candidate)

### 25.1 Explicit three-document association — no implicit host session

This clause concerns an optional **OSTF Production Session Profile 0.1.0 or 0.2.0** combined with a separate **OSTF Distributed Session Profile 0.2** Snapshot or Event, both referring to one **exact OSTF 4.3 Score**. It does **not** define a new JSON field, change any Schema, merge the two Profile identities, or require that every production client support remote sessions. A studio-only tool may read the Production Profile without any Distributed record. A remote performance client may read the Distributed record without production data.

The canonical source is the **original byte sequence** of the externally supplied Score `.ostf`. The Production `score.sha256` and Distributed root `scoreSha256` are both mandatory *original-score byte digests*, and when paired MUST equal each other and the SHA-256 of the exact pinned Score bytes. Hashes describe byte identity, **not** rights, authority, approval, shared Session participation or cryptographic identity. No implicit JSON reserialization, score download or silent score migration is permitted to make the hashes match. Production `score.sourceUri` is only a hint; it is not consent to fetch an asset. The external Production Profile JSON may be independently edited without changing the Score's SHA-256; the Profile's own changes are never transmitted as part of a Distributed Event unless a separate authorized mechanism explicitly defines that exchange.

When Production `score.documentId` or `score.revisionId` is present, it MUST agree with both the corresponding Distributed root fields and the Score's actual `document.id` / `document.revisionId`. Their omission in Production is **unspecified**, not a license to fabricate IDs. The Distributed Profile 0.2 root requires its `documentId`, `revisionId`, `performancePlanId` and `scoreSha256`; it MUST resolve its Plan ID against that pinned Score's `performancePlans[]`, rather than interpreting the first Plan or name. If the Score bytes are unavailable, equality between two Profile digest declarations is at most **claim consistency**; the original Score identity, effective source Track IDs and Plan validity remain **unverified** and MUST NOT be reported as checked.

### 25.2 Source binding is not hardware routing

Production `channels[kind:"track"].trackId` names a Core `tracks[].id`. The Distributed `participants[].assignedTrackIds` and phrase Event `targetTrackId` also refer to Core Track IDs. Matching these two references does **NOT** bind a remote Participant to a Production Channel or plug-in slot, authorize plug-in state loading, set physical output ports, assign a robotic actuator or grant Session authority. A Core Track may intentionally have no Production Channel; absence cannot be inferred as mute or Session ineligibility. Production-only `kind:"audioTrack"` Channels have no Core Track ID and MUST NOT become remote Participant assignments or open-Plan Parts by a similar name.

The Distributed finite Plan's active `visitId`, `sourceTick` and `performanceTick` determine which source material is eligible for Score-derived musical performance. Production automation and recorded Audio Regions, when independently authored, remain governed by Production §23–24: evaluate against **original source Tick** for each Visit; do not carry prior Visit mixer-state latches; independent Audio Regions are not automatically silenced by Core `realization:"silent"`. A Distributed `phraseCommitted` adds an accepted, separately identified musical phrase to an explicit `open` Part; it does **not** change the original Score bytes, materialize the Core Note array, rewrite Production automation, replace a studio recording or trigger an effect/plugin/robot. To save an edited Score, publish a **new byte-pinned Score revision** with its own profiles or perform an explicitly authorized migration; existing pinned remote sessions do not silently switch.

### 25.3 Cross-profile consumer behavior and diagnostics

An adapter making the optional claim **`OSTF 4.3 Cross-Profile Binding Reader`** MUST reject automatic co-binding when the Score digests disagree; MUST reject conflicting explicit document/revision IDs or absent/unresolvable Plan/Track IDs when it has the pinned Score; and MUST preserve all source Profile records without mutating them on rejection. It MAY show two independent records separately, labeled *not bound*. It MUST NOT infer remote host permissions, latency correction, deterministic audio mix, MIDI restoration or robot safety from successful association. A `Production Profile Reader` and a `Distributed Session Profile Reader` remain independent conformance claims.

Suggested diagnostics: `E-CROSS-PROFILE-SCORE-HASH`, `E-CROSS-PROFILE-DOCUMENT`, `E-CROSS-PROFILE-REVISION`, `E-CROSS-PROFILE-PLAN`, `E-CROSS-PROFILE-TRACK`, `W-CROSS-PROFILE-SCORE-UNAVAILABLE`, `W-CROSS-PROFILE-ROUTING-UNDEFINED`. These are descriptive proposed reporting codes, not a new required Schema enum. A URI locator without permission to fetch is never treated as equivalent to a locally verified Score.

### 25.4 Worked bundled case — exact-score association

The included `examples/production/03-audio-regions-sidechain-02.json`, `examples/session/03-snapshot-02.json`, and `examples/22-pinned-session-aaba.ostf` deliberately refer to the same pinned Score digest and identities. The Production channel `trackId:"bass"` and Distributed Participant assignment `"bass"` denote the **same musical Track**, but do not assert that the remote robot should output sound through the Production `bass-channel`, nor that this host has a compatible bass plug-in installed. The distributed Session's `performancePlanId:"form"` is a Core Plan ID, absent from Production root; the two Profiles retain distinct version tokens and unrelated local IDs. Studio Audio Regions, Sends, Sidechains and Device state remain host/local representations unless explicitly exported via a separate authorized workflow.

**Status:** Draft 0.19 semantic candidate only. Successful structural/source-binding inspection cannot prove remote synchronization, plug-in execution, audio rendering, robotics, copyright rights or formal publisher adoption. All prior author-owned non-test release decisions remain open.

## 26. Explicit Score revision re-binding for separate Production and Distributed Profiles (Draft 0.20 proposal)

### 26.1 Two separate operations, not automatic migration

A new OSTF Score byte sequence is a different **pinned source** even if musical contents appear identical after JSON reformatting. A Production Profile 0.1/0.2 may be **explicitly re-associated** with a new Score revision; a Distributed Session Profile 0.2 live Session is **not** re-associated in place. This clause is a candidate *non-executable data-authoring rule* for third-party tools. It adds no JSON fields, does not rewrite the Core, and does not make a Studio Profile into a live Session document. Updating a `score.sha256` alone MUST NOT be advertised as a safe or lossless migration.

A source Score edit, such as changing Notes, Harmony, Tempo, Sections, Track IDs or the finite `performancePlans`, MUST create an intentionally chosen new Score resource. For a claimed revision of the same work, preserve `document.id` and assign a **new** `document.revisionId`; if a different `document.id` is supplied, this is cross-song reassignment rather than a same-song revision. OSTF Core permits optional document metadata, but without explicit document/revision identities the application cannot claim revision lineage from a matching title or a content hash. Publishing replacement bytes under an unchanged `(document.id, document.revisionId)` or unchanged immutable URL is **not** a legitimate revision operation for companions relying on that identity. A format-only byte change still requires an explicit re-pin; the claim of music equivalence is separate from source-byte integrity.

### 26.2 Re-binding a Production Profile without silent music edits

A Studio application MAY prepare a **new copy** of a Production Profile referencing the new Score. It MUST retain the original Profile and previous Score unchanged unless the author separately requests deletion. A purported non-lossy re-binding is acceptable only after all these independently reviewable facts are established:

1. The *old* Production `score.sha256` matches the original OSTF Score's exact bytes, and the proposed new score bytes are available with a freshly calculated SHA-256. Optional old Production document/revision fields, when authored, MUST agree with the old Score; a new Profile copy MUST use the new Score digest and any newly authored document/revision identity, not copy stale identity claims.
2. All Production `channels[kind:"track"].trackId` map to valid Tracks in the new Score. An unchanged Track ID establishes **identity only**, not unchanged music, channel sound, routing or source timing. A removed/renamed Track requires an explicit author-approved re-map, separation as a different Profile, or a declared **lossy** export. The Schema requires valid Track references; a tool MUST NOT fabricate a matching Track by channel name or knowingly emit a broken Profile copy.
3. Score PPQ, Sections, Tempo/Meter maps and any selected Performance Plans must be compared for effects on **original source Ticks**. A changed tempo map changes the mathematical `native` Audio Region source-frame offset/time relationship; a changed PPQ or source timeline may change the intended positions of `audioRegions[].startTick`, `durationTicks`, fades and `automation[].points[].atTick`. A changed Performance Plan can alter source-to-Visit projection even when source ticks are the same. The importer MUST NOT shift, stretch, quantize, trim or latch such information solely from a new score digest, matching Track ID or section label.
4. Retained plug-in state Assets, independent Production Audio Regions, Send/Bus routing, opaque Device IDs and host extensions remain **Production-owned**, not Score-owned. Changing a Score must not automatically overwrite or execute them. Any unresolvable source-time intent or unsupported re-map requires author review; a target host unable to preserve the data must retain the original Profile or issue an itemized loss report before a separate lossy export.

Thus three states must be distinguished: **pinned to original** (old Production is still valid against old Score); **re-bind candidate requiring review** (new Score is a plausible revision but all ported meanings are not yet accepted); **author-approved new binding** (new Production copy and new Score digest/identities are authored and verified as a pair). A structurally valid changed hash is never, by itself, evidence of the third state. Retaining unknown assets or plugin IDs without activation is permitted, but there is no automatic acoustic-fidelity claim.

### 26.3 Distributed Session immutability across Score edits

A playing or stopped **Distributed Session Profile 0.2** is bound to its original `(documentId, revisionId, performancePlanId, scoreSha256)` and its accepted event history. A new Score revision MUST use a **new Session identity** for new collaboration; existing `stateRevision`, `eventId`, accepted `phraseCommitted` records, `visitId`, `performanceTick`, source-Tempo clock anchor, committed-phrase window and participant assignments MUST NOT be transparently migrated by changing the Score digest. Historical records remain attached to the original pinned Score. Any desire to reuse some musical material in a new Session is a **new explicit conversion/authoring action** with separately assigned identities and any necessary loss reports, not event replay or a hidden authorized robot command.

A third-party host receiving an API response with changed Score bytes SHOULD retain the old pin while preparing an explicit new revision/new Session workflow. It MUST NOT treat `latest` URL changes, HTTP `ETag` changes, a UI save, a consistent new title or identical Track IDs as consent to mutate an active remote Session. Hash pinning does not authenticate a publisher or authorize plug-in loading or physical actions.

### 26.4 Optional read-only revision assessment

The bundled `tools/validate_production_profile.py` has a Draft 0.20 optional `--score OLD.ostf --rebind-target NEW.ostf` **preview**. It reports hash/identity/Track correspondence and whether source timing and Performance Plan declarations differ. It NEVER saves a modified Profile, edits OSTF Notes, auto-retimes audio, starts a Session or certifies losslessness. Its `REVIEW_REQUIRED` status is deliberate, including for format-only changes. An unresolved or malformed target must be reported as `BLOCKED` or an input error without changing existing records. This is a local authoring aid, not an independent interoperability test or publisher approval.

Suggested diagnostics (not new Schema enum values): `E-REBIND-SCORE-INVALID`, `E-REBIND-IDENTITY`, `E-REBIND-REVISION-REUSE`, `E-REBIND-TRACK-UNRESOLVED`, `W-REBIND-SOURCE-TIME-CHANGED`, `W-REBIND-PLAN-CHANGED`, `W-REBIND-NEEDS-AUTHOR-REVIEW`, `W-DISTRIBUTED-NEW-SESSION-REQUIRED`.

**Publication status:** This §26 is an **unratified Draft 0.20 normative candidate**. Core 4.3, inherited Core 4.2, Distributed Profile 0.2, Production 0.1/0.2 Schemas and all bundled song/profile JSON examples remain byte-for-byte unchanged. The rights holder's explicit adoption, bilingual editorial approval and licensing decisions remain pending, irrespective of the user-excluded runtime/independent validation.

## 27. Portable preservation and feature-level disclosure (Draft 0.21; unratified)

### 27.1 Independent artifacts and three different kinds of claims

An OSTF Score, a **Production Session Profile**, and a **Distributed Session Profile** have independent file/Schema versions and separate authorities. Preserving their JSON documents is not the same claim as interpreting their musical meaning; interpreting them is not the same claim as reproducing their audio or acting on physical devices. A third-party application MUST distinguish these claims when exporting or advertising support. A Core-only Reader MAY ignore the **separate** Profile documents, but an application claiming to save the **complete source bundle non-lossily** MUST preserve or explicitly account for each companion and each referenced asset it received. It MUST NOT silently drop an unsupported Profile while advertising complete-project round-trip capability.

### 27.2 Minimum source preservation at a transfer boundary

For an explicitly **non-lossy data-preservation** operation, a writer MUST either (a) retain the exact source documents and bytes of available referenced opaque assets, including plug-in state, or (b) produce a new explicitly authored valid document version with stable referential meaning and all dependent Profile pins re-established. Rewriting the Score changes its raw-byte `sha256` even if the parsed JSON appears equivalent; it MUST NOT leave a stale Production/Distributed Score pin. Production `assets[].sha256` pins source material bytes, not an asset's display name, plugin identity or URI alone. A metadata-only import with missing asset bytes is **descriptor preservation**, not a complete non-lossy transfer of that asset. Unknown inert `hostExtensions` and plugin-state bytes MAY remain uninterpreted; preserved does not mean installed, decoded, licensed, executable or sonically equivalent.

### 27.3 Unsupported features and explicit loss disclosure

An importer/exporter that cannot preserve some requested feature MUST refuse an advertised non-lossy overwrite or provide an explicit, opt-in **lossy export**. The disclosed affected elements SHOULD identify stable source IDs (Track/Channel/Device/Region/Asset/Automation/Event/Voice/Plan where applicable), describe why the target cannot represent them, and distinguish **omitted**, **approximated**, **unavailable bytes**, **unsupported execution** and **unverified equivalence**. These are editorial report categories, **not new mandatory JSON fields or Schema enum values**. Keeping a plugin descriptor and its binary state bytes but bypassing DSP is *data-preserving but acoustically degraded*; dropping the state bytes is *data-lossy*. A Score-only export is explicitly lossy with respect to any companion production mix or recorded Regions not also preserved as separate files.

### 27.4 Score revision and remote session boundary

If a Score is edited or reserialized, the old Score and existing Profile pins remain historical. Follow §26 to author-review any Production Profile re-binding, including all present `score.documentId`, `score.revisionId`, `score.sourceUri` and `score.sha256` fields and the source-Tick media/automation meaning. A `sourceUri` is **only a locator**, not a replacement for the exact-byte digest or an instruction to fetch. A new Score revision requires a new **Distributed `sessionId`**, not a rewrite of accepted Event IDs, authoritative `stateRevision`, clock anchors or committed phrases. A new JSON hash proves byte equality of available content, **not** publisher authenticity or any audio, plug-in, network or robot execution permission.

### 27.5 Capability matrix for honest claims

An implementation MAY independently claim: `Core 4.3 Data Reader`, `Core 4.3 Data Writer`, `Production Profile 0.1 Data Reader/Writer`, `Production Profile 0.2 Data Reader/Writer`, `Opaque Asset-Preserving`, `Cross-Profile Binding Reader`, `Plan-Aware`, `Distributed Profile 0.2 Snapshot/Event Reader`, or separately qualified host DSP/remote actuation support. A claim must name the supported exact versions and operations. None of these is an automatically conferred certificate, and a local format helper never proves cross-vendor sound or robotic performance. Unknown future versions cannot be silently relabeled as 4.3 or 0.2.

**Status:** This section is a non-executable, unratified normative candidate. It adds zero Schema fields, does not require new servers or APIs, and leaves the Core musical authority unchanged. Author adoption, bilingual proofing and complete-package licensing remain required before publication; runtime tests are excluded by the user, not marked passed.

## 28. Distribution package versus a defined Production interchange set (Draft 0.22 candidate)

### 28.1 No standardized project archive in OSTF 4.3

The optional Production Session Profile 0.1.0/0.2.0 specifies **JSON records**, stable references and Asset URI semantics; it does **not** specify a portable `.zip`, directory layout, manifest encoding, central index, streaming framing, file extension for a multi-file project, encryption, signatures, plug-in binary package, or HTTP API. The `OSTF_4.3_Draft_*_Development_Package.zip` used to distribute this specification is a **publisher release artifact**, **not** a production-session interchange container. An application MUST NOT interpret the development ZIP layout, the publisher `PACKAGE_MANIFEST.json`, or the publisher's `SHA256SUMS.txt` as additional normative fields of a user-authored Score or Production Profile.

### 28.2 Define a preservation claim by the supplied document/Asset set

A third-party implementation MAY receive a Score and zero or more independent versioned Profiles, plus zero or more referenced Asset byte streams through an application-specific folder, archive or user-authorized service. The existence of an Asset descriptor or checksum does **not** prove that the Asset bytes were supplied. For an interchange claim, distinguish **(a) original Score bytes and declared Profile JSON**, **(b) received exact opaque Asset bytes**, and **(c) missing/unauthorized/unresolvable Asset bytes**. This is an import/export **reporting distinction**, not three new Profile fields or a requirement to disclose a host filesystem layout.

A tool claiming **non-lossy preservation of the supplied collection** MUST retain each **actually supplied** versioned document and each **actually supplied** referenced Asset byte sequence it includes in the claim, together with their identity references, without silent modification. It MUST refuse that claim or supply an explicit loss report if such data is dropped or altered. A descriptor-only import with unavailable Asset bytes MUST NOT be represented as complete studio project restoration; conversely, absence of a Profile that was **never supplied** MUST NOT be described as that tool deleting the Profile. The producing/receiving application MUST clearly define the scope and presence of data on which its claim is based.

### 28.3 Exact byte pinning and archive/container responsibilities

The existing Score hash fields continue to cover the exact **original Score file bytes**, not the bytes of an outer archive, a URL, a normalized JSON reserialization or a newly exported Score. Byte-identical source retention preserves a compatible Profile pin; a genuine Score rewrite requires explicit revision/rebinding as defined in §26. The checksums of Production binary Assets apply to the referenced Asset bytes as authored, not to an outer host container. A container application MAY add independent access controls, encryption, signatures, compression or a user interface, but MUST NOT mistake such host capabilities for OSTF Profile features or remote actuation authority.

### 28.4 Compatibility and conformance wording

Use **"Score 4.3 Reader"**, **"Production Profile 0.2 JSON Reader"**, **"Production Profile 0.2 Data/Asset-Preserving Writer"**, **"Full Supplied Collection Preservation"** (with an explicit collection inventory), and **"DAW/plug-in rendering"** as different, version-scoped claims. Merely opening a ZIP or reading `LICENSE`/`PACKAGE_MANIFEST.json` does not provide any of these capabilities. An implementation can preserve data while declining to interpret or execute it. The project packaging question is **out of scope for OSTF 4.3 Core and this Profile**; if standardized in the future it needs a separately versioned proposal and explicit publisher ratification.

**Status:** unratified Draft 0.22 semantic guidance; no JSON Schema changes, no new interop archive standard, no run-time/independent implementation testing or license approval claimed.

## 29. Current cross-document interpretation matrix (Draft 0.23 editorial reconciliation; unratified)

A single original Score can be referenced by optional separate Production and Distributed Profile JSON documents. **Co-binding is a read-time association of declarations, not a state mutation.** The following table is the current candidate interpretation where earlier chronological Draft sections might otherwise look conflicting:

| Observed record or operation | Score Core 4.3 effect | Production Profile effect | Distributed Session effect |
| --- | --- | --- | --- |
| Retrieve a versioned Score over an authorized API | Read exact bytes, verify `format`/`version` and supported meaning | Nothing automatically; confirm `score.sha256` if provided | Nothing automatically; confirm pinned `scoreSha256` if supplied |
| Receive a `phraseProposed` Event | No new Core Notes | No region/device/automation change | Proposal/observation only; not an accepted phrase |
| Accept a valid `phraseCommitted` Event | **No mutation** of Core `notes[]` | **No implicit** mute, render, plug-in state change or Region replacement | Accepted phrase is in the Session's ledger for its authorized `open` Visit Part |
| Save that accepted music into a revised Score | Requires explicit new authored Score and new byte/revision identity | Re-bind a **new Profile copy** only after source-Tick and Track reconciliation | New Score pin requires **new Session identity**, not replay of the old event log |
| Score differs but one Profile still refers to old digest | Do not silently relabel version or edit source bytes | Keep Profile independently, mark it **not co-bound** with new Score | Keep original Session pinned; never reinterpret as a new one |
| Metadata-only Asset with no actual bytes available | No invented Core audio | Descriptor preservation **only**, not complete audio/state restoration | No remote Asset or robot execution implied |

Where exact original Score bytes are unavailable, matching declared SHA-256 values are insufficient to claim source verification, valid Plan/Track references or complete production transfer. A Source URI, ETag, ZIP filename or matching Track name is not a substitute. Session authority has no implied rights to change Production channels, and a Studio Writer has no implied rights to commit a Distributed Event. Existing §§25–28 continue to specify the detailed identity, re-binding, preservation and archive boundaries. This section **adds no fields or transport API** and has no runtime/DAW/robot validation claim.

## 30. Draft 0.24 — Record-version interoperability discriminator (editorial)

A Production 0.1.0 or 0.2.0 file MUST declare `profile:"OSTF-Production-Session"` and, respectively, `profileVersion:"0.1.0"` or `"0.2.0"`. Both are mandatory exact discriminator fields and select the corresponding packaged JSON Schema. Unlike Production, Distributed Session 0.2 instead declares `profile:"OSTF-Distributed-Session-0.2"` and `recordType`; it has no `profileVersion`. This corrects an obsolete sentence in `PRODUCTION_COMPATIBILITY.md`, not an existing Schema or example. A host MUST NOT silently convert Distributed Event state into audio Mixer automation or the inverse, and an authenticated session replay must not rewrite the Studio data. See `CONFORMANCE.md` and `SESSION_STATE_MACHINE.md`. This is a candidate interpretation, not publisher adoption, a new field or a tested plugin/runtime feature.


## Draft 0.70 — Candidate-set closure and conservative binding result (unratified)

The four reference-binding outcomes are **evaluated conclusions**, not proof that every possible remote location has been searched. A reader MUST first declare its authorized candidate scope and whether enumeration and byte retrieval within that scope are complete. A candidate is verified only after its original Score bytes have actually been read and hashed; a filename, declared hash, network response header, or matching musical content is not verification.

For a supported structurally valid Profile with a valid declared digest, the candidate resolution procedure is:

1. Record the authorized, bounded candidate scope and whether the scope has been fully enumerated. Treat a failed download, revoked access or incomplete enumeration as **NOT_EVALUATED**, an external diagnostic, not one of the four resolved binding states.
2. If all eligible candidate Score bytes are retrieved and the scope is complete, zero candidate Scores gives **MISSING** within that scope; one or more Score candidates with no matching raw-byte SHA-256 gives **MISMATCH**. This does not assert global absence.
3. If matching Score byte identities exist, collapse duplicate copies of the **same bytes** before resolving Track/Plan/Visit and other required referents. Required referents absent or not uniquely identifiable yield **AMBIGUOUS**, with `missing_referent` / `nonunique_referent` as non-serialized diagnostic details.
4. Only a matching Score with all required referents uniquely resolved yields **RESOLVED**. Multiple distinct byte sequences matching a SHA-256 digest are outside the normal identity model and must not be silently treated as identical.
5. If any authorized candidate remains unenumerated or its bytes cannot be retrieved, report **NOT_EVALUATED** regardless of any already observed hash match. No partial or conditional **RESOLVED** is allowed. The diagnostic MUST identify the incomplete authorized scope; an implementation MUST NOT infer MISSING, MISMATCH, AMBIGUOUS, or RESOLVED from a partial candidate set. No writer may silently rebind an old Profile to a revised Score.

**NOT_EVALUATED** is an implementation/report status, not an OSTF JSON enum or new Schema field. INVALID and UNSUPPORTED remain separate pre-binding format/version errors. Hash integrity alone does not authenticate authors or grant access, playback, recording, plug-in installation, network requests or robotic actuation. This candidate rule requires D01–D03 publisher approval; it is not a verified implementation.


## Draft 0.76 — Binding rule editorial consolidation (unratified)

Draft 0.70 step 5 is corrected above in place to eliminate its obsolete partial-`RESOLVED` exception. The active Draft 0.71/0.73 precedence remains: INVALID and UNSUPPORTED are pre-binding errors; incomplete authorized enumeration or byte retrieval yields external `NOT_EVALUATED`; only complete authorized candidate evidence permits MISSING, MISMATCH, AMBIGUOUS or RESOLVED. A SHA-256 match observed before enumeration closure is provisional evidence, **not** RESOLVED. This is documentary clarification only: no Schema field or mandatory network discovery is introduced. This text remains subject to D01–D03 publisher adoption.
