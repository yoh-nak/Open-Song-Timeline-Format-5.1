> **Current adoption candidate: Draft 0.77 (UNRATIFIED).** The first reference-binding decision table is the active proposal. Older dated clauses in this document are historical and must not be interpreted as simultaneous alternative normative rules. This edition changes editorial identification only; it does not alter serialization or Schema.

# Draft 0.77 — Active reference-binding decision table (PROPOSED / NOT RATIFIED)

**Review gate D02.** This active candidate is the controlling *proposal* for reference-binding interpretation. Earlier Draft 0.62–0.72 sections below are historical change records, **not alternative active requirements**. This front section has no authority until publisher adoption. Schema structures and serialization are unchanged.

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

**Adoption target: D02 / Distributed Session 0.2.** Only the text explicitly identified in the release ballot and its existing schema is eligible for adoption. Previous Draft 0.62–0.70 binding examples are retained as change history, not simultaneous alternative definitions. For conflicting reference outcomes, Draft 0.71's fully enumerated/fully fetched authorized candidate-set rule prevails **within this candidate**. A partial collection is externally `NOT_EVALUATED`; no JSON property is introduced.

An implementation MUST distinguish: (a) reading/retaining unknown data, (b) round-trip preservation, (c) editing, (d) interpretation, and (e) actual execution. A claim covering one operation MUST NOT imply all others. A valid matching digest is not evidence of Session execution, mixer audio parity or robot actuation. These proposed MUST statements become normative **only after D02 publisher adoption**.

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

# OSTF Distributed Session Profile 0.2 — Proposed Semantics (Draft 0.55)

> **Historical editorial snapshot: Draft 0.59 (unratified).** Existing headings referring to earlier Drafts describe cumulative editorial proposals, not competing active document versions. The exact versioned Schemas remain unchanged; the single current release gate is [RELEASE_READINESS.md](RELEASE_READINESS.md). Publisher acceptance D01–D05 is still pending; runtime/independent tests are excluded, not passed.

## Draft 0.33 — Event-acceptance operation boundary (unratified)

Acceptance of a version-pinned and authorized Distributed Session Event mutates **Session state**, never Source Score bytes, Production Mixer/Automation, plug-in execution, or physical robot actuators. Refusal/stale/conflict must not be misreported as a successful state change. See `CONFORMANCE.md` for separate operation outcomes. No new Session Schema field or transport protocol.

---

## Draft 0.32 — Byte-pinned Score and reserialization boundary (pending)

Distributed 0.2 `scoreSha256` pins the *actually supplied original Score bytes*, not JSON meaning or a server URI. Any reserialization producing different bytes requires a new digest and an **explicit new Session identity** under the existing revision rules; it MUST NOT retarget accepted events in place. See `CONFORMANCE.md` Draft 0.32 for the distinct identity/preservation claims. No field, Schema or clock protocol is changed.

---

## Draft 0.29 — Distributed diagnostic boundary (editorial proposal)

Refer to the `docs/CONFORMANCE.md` reporting taxonomy. A new stale-revision event is a semantic rejection rather than a deferred proposal; an authenticated identical accepted replay can remain idempotent under the pinned-Score Session rules. Session acceptance never certifies acoustic delivery, robot safety, nor mutation of Score Notes or Production state. No JSON Schema change is introduced.

---

## OSTF Distributed Session Profile 0.2 — Draft 0.26 editorial edition (schema unchanged)

This is **an optional separate JSON format**, not a 4.3 song field, Web service, time-sync protocol or robot-control system.

- Canonical candidate schema: `schema/ostf-distributed-session-0.2.schema.json`.
- Legacy development profile: `schema/ostf-distributed-session-0.1.schema.json` (informational; NOT wire-compatible without explicit conversion).
- Typed event contracts, proposal/commit semantics, authority, late-join state and temporal mapping: `docs/SESSION_STATE_MACHINE.md`.
- Musical fixed-note and source-cut semantics: `docs/NOTE_AND_MIDI_CUT_SEMANTICS.md`.
- Web API guidance (non-normative): `docs/WEB_INTERCHANGE_PROFILE.md`.

Session Snapshot identifies a pinned OSTF document + revision, participants and their Track assignments, a session authority and monotonic state revision, optional source/expanded musical position and clock-domain observation, and optionally concrete committed phrase data for late joiners. No Snapshot supplies authorization, synchronized clock guarantees or safe robot motion merely by being syntactically valid.

Event records distinguish proposals, observations, cues, statuses, requests, authorized phrase commitments and authorized state transitions. Only the latter two kinds advance the authoritative session revision, and each accepted transition advances it by exactly one. This is a **single-authority editorial model** for predictable interoperability, not a distributed consensus protocol.

The first 0.2 phrase representation intentionally handles only finite pitched MIDI1 notes. Singing syllables, audio transfer, MIDI2/MPE, physical-actuation trajectory and algorithm-specific improvisation state are out of Profile 0.2 scope and are not silently fabricated. Session phrases are realizations separate from original song Notes, unless explicitly materialized into a new OSTF document revision.

Read `examples/session/03-snapshot-02.json` through `07-session-state-change-02.json` in the package for the typed event envelope and committed-note snapshots.

## Draft 0.4 snapshot lifecycle note

A Profile 0.2 Snapshot MUST include `sessionStatus` (`prepared`, `playing`, `stopped`); a `playing` Snapshot MUST also include `position`. This is a deliberate normative amendment to an unpublished draft, not a new `.ostf` Core field. `participantStatus` alone never changes session lifecycle. Duplicate `eventId` with identical parsed JSON content is idempotent even if whitespace or object key order differs; different content is an integrity conflict. See `SESSION_PROFILE.md`.

## Draft 0.6: Musical placement authority

Committed session phrases are permitted **only inside an explicitly `open` Part of the pinned finite Core Performance Plan**. The entire phrase interval must fit one Visit; no automatic overdub on `fixed`, sound on `silent`, or conversion of `unspecified` to open is allowed. Accepted phrases on the same Track do not overlap. A prepared Session without a pinned Plan cannot accept a phrase commit. See the added normative section of `docs/SESSION_STATE_MACHINE.md`.

## Draft 0.7 editorial resolution — Frozen score and historical commitments

Profile 0.2 maintains the same pinned source Score/Revision/finite Plan throughout a Session. New Web API source contents cannot implicitly rebase accepted events. `stateRevision` tracks authoritative Session decisions, not changes to OSTF source data. Exact duplicate Event-ID replay is idempotent even if the original base revision is now old; new events with stale base revisions must be rejected. During `playing`, `visitChanged` is forward-only in expanded Performance Tick; a backwards jump is outside this Profile. Accepted Session phrases are immutable records, not claims of actual acoustic performance. A forward skip or terminal stop prevents claims that bypassed/future phrases sounded, without deleting the ledger. Track reassignment does not transfer instrument authorization. These are candidate normative rules, not proof of WAN/robot operation. See `SESSION_STATE_MACHINE.md` Draft 0.7.

## Draft 0.8 — Tightened subtype and replay safety

The Profile 0.2 `assignmentChanged` payload must never contain `position`; its Schema condition has been corrected from a logically ineffective nested `required`/`anyOf` to two independently forbidden properties. A Session authority must authenticate and match the pinned Score before confirming an event-id replay; a known ID alone grants no access to the event ledger. Whole parsed-event value equality is precise, not lossy JS-number coercion. Every retained Session Phrase must have Note end positions inside its own duration regardless of `commitmentWindow`. A stopped or skipped historical commitment is not an assertion of a currently assigned performer or actual sounding performance. See `SESSION_STATE_MACHINE.md` Draft 0.8.

## Draft 0.9 source/Plan pinning

The separate Profile 0.2 now requires `performancePlanId` and `scoreSha256` at the root of *every* Snapshot and Event, including positionless prepared snapshots. The root Plan ID names a finite Plan in the actual pinned OSTF 4.3 score. `position.performancePlanId`, when present, must match. `scoreSha256` is computed over the exact UTF-8 original OSTF bytes (after HTTP content decoding, before JSON parsing/reserialization), not a semantic JSON hash. Same document/revision names with different bytes are not interchangeable. No host is authorized by these data fields. See `SESSION_STATE_MACHINE.md` Draft 0.9 and updated complete Session reference.

## Draft 0.10 — A Visit change now carries an anchored Position

Profile 0.2 `visitChanged` Events now require both a `targetVisitId` and a `position` with Plan, Visit, source Tick, expanded Tick, UTC clock-domain epoch and uncertainty. That Position must identify the first Tick of the new Visit, and the Event effective Tick must match. Without a new anchor, a forward skip could not be interpreted precisely by a distant participant. This adds no Core field; refer to `SESSION_STATE_MACHINE.md` Draft 0.10 for formal meaning. This is an unratified proposal and does not certify WAN/robot execution.

## Draft 0.11 — Clock-domain and source-tempo interpretation

Within one playing Profile 0.2 Session, the `clockDomainId` established by `sessionStarted` MUST remain the same on later `visitChanged` positions and playing Snapshots. A new clock domain requires a new Session. Optional `position.tempoBpm` is explanatory only; when present it MUST equal the pinned OSTF's step-tempo value at `sourceTick`, not a host-created alternate tempo. `sessionStopped.effectivePerformanceTick` is observational context, never a delayed stop or an emergency-stop mechanism. Full candidate semantics: `SESSION_STATE_MACHINE.md` Draft 0.11.

## Draft 0.12 — Timed anchors and minimum participant constraint

A `playing` Snapshot or `sessionStarted` / `visitChanged` timed Position requires a resolvable effective Tempo from the pinned OSTF score at `sourceTick`, even when `tempoBpm` is omitted. An unpositioned prepared Snapshot does not need a tempo event yet, but cannot begin authoritative timed playback until one is authored in the pinned score. Within a Visit, ideal musical time is the sum of piecewise step-Tempo durations in source segments, re-reading source Tempo after cuts. This is a data-level time mapping, not clock synchronization. Every 0.2 Snapshot now has at least one participant in its Schema, consistent with authority resolution. See `SESSION_STATE_MACHINE.md` Draft 0.12. These changes are still unratified and do not modify OSTF 4.3 Core.

## Draft 0.19 — Optional Studio Production companion record

A Distributed Session Profile 0.2 record may be associated with an independent Production Session Profile 0.1.0/0.2.0 only when both pin identical **original OSTF Score bytes** (`scoreSha256` vs `score.sha256`), with matching explicit document/revision identities and an existing finite `performancePlanId` in the pinned Score. Production Profile carries no root Plan selection; its `channels[].trackId` is a Core Track ID, not a remote host-output/robot assignment. `phraseCommitted` does not edit Studio plug-in state, Audio Regions or Production automation, and a studio Audio Region does not become a Session Participant. This does not modify any Distributed Schema or authorize asset downloads, plug-in launch, network behavior or actuation. See `PRODUCTION_SESSION_PROFILE.md` §25.

## Draft 0.23 — Exact-Score identity is companion-specific (editorial clarification)

Unlike Core Score 4.3, **Profile 0.2** has mandatory original-byte `scoreSha256`, alongside `documentId`, `revisionId` and `performancePlanId`. It is not a generic canonical-JSON digest. Matching digests on two companions with no original Score bytes cannot establish that their Plan/Track IDs resolve. Older Web guidance describing "no canonical content digest" only means that OSTF Core did not introduce a canonical JSON hashing scheme; it does not supersede the exact-byte Profile 0.2 field. Session Events do not update the separate Production Profile or materialize a new Score revision, even when a Studio Channel and remote Participant both refer to the same Core Track ID. No transport, authorization or robot action is inferred.


## Draft 0.24 — Exact profile discriminator and stale-event distinction (unratified)

A Distributed Session 0.2 Snapshot/Event uses root `profile:"OSTF-Distributed-Session-0.2"` and `recordType:"snapshot"` or `"event"`. **It does not have a `profileVersion` property.** Archived Distributed 0.1 instead declares `profile:"OSTF-Distributed-Session-0.1"`; it is not a 0.2 payload alias. In contrast, Production 0.1.0/0.2.0 has `profile:"OSTF-Production-Session"` plus required `profileVersion`. These discriminators are exactly those in the bundled existing Schemas; do not guess a family from a filename or API URL.

After authentication and immutable Session/Score/Plan identity checks, an identical already-accepted Event ID and full parsed Event value is an idempotent no-op. An altered same-ID record is an integrity conflict. A **new** state-changing Event with stale `baseStateRevision` is rejected rather than being relabeled a proposal or retroactively accepted. Proposals, observations and participant status reports do not alter the authoritative session revision. See `SESSION_STATE_MACHINE.md` for admission ordering. This amendment does not add JSON fields or certify real-time/robot operation.


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
