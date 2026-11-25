> **Current adoption candidate: Draft 0.77 (UNRATIFIED).** The first reference-binding decision table is the active proposal. Older dated clauses in this document are historical and must not be interpreted as simultaneous alternative normative rules. This edition changes editorial identification only; it does not alter serialization or Schema.

# Draft 0.77 — Active reference-binding decision table (PROPOSED / NOT RATIFIED)

**Review gate D01.** This active candidate is the controlling *proposal* for reference-binding interpretation. Earlier Draft 0.62–0.72 sections below are historical change records, **not alternative active requirements**. This front section has no authority until publisher adoption. Schema structures and serialization are unchanged.

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

**Adoption target: D01 / Core Score 4.3.** Only the text explicitly identified in the release ballot and its existing schema is eligible for adoption. Previous Draft 0.62–0.70 binding examples are retained as change history, not simultaneous alternative definitions. For conflicting reference outcomes, Draft 0.71's fully enumerated/fully fetched authorized candidate-set rule prevails **within this candidate**. A partial collection is externally `NOT_EVALUATED`; no JSON property is introduced.

An implementation MUST distinguish: (a) reading/retaining unknown data, (b) round-trip preservation, (c) editing, (d) interpretation, and (e) actual execution. A claim covering one operation MUST NOT imply all others. A valid matching digest is not evidence of Session execution, mixer audio parity or robot actuation. These proposed MUST statements become normative **only after D01 publisher adoption**.

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

# Open Song Timeline Format 4.3.0 — Proposed Normative Score Specification (Draft 0.55)

> **Historical editorial snapshot: Draft 0.59 (unratified).** Existing headings referring to earlier Drafts describe cumulative editorial proposals, not competing active document versions. The exact versioned Schemas remain unchanged; the single current release gate is [RELEASE_READINESS.md](RELEASE_READINESS.md). Publisher acceptance D01–D05 is still pending; runtime/independent tests are excluded, not passed.

## Draft 0.44 — Rule ID disambiguation (D01/D04 PENDING)

`SEMANTIC_RULES.md` previously used the identifiers S13 and S14 twice, once
for Distributed Session semantics and again for later Core music semantics.
To prevent incompatible implementations, the earlier S13 and S14 remain
**Session-only**, and the later fixed continuous-join and fixed vocal/lyric
rules are uniquely identified as **S22** and **S23**. S21 remains the
source-tempo Session rule. Rule numbers are documentary cross-references,
not JSON fields or a priority order. See the canonical ID table and the
published corrections in `PUBLISHER_RELEASE_DECISIONS.md`.
Publisher adoption and English/Japanese editorial review are still required;
no Schema, 4.2 inherited field, runtime claim or license changes are made.

## Draft 0.43 — Lyric/Voice/VocalPerformance selection in finite Performance Plans (unratified)

`performancePlans` do **not** promote authored `lyrics.units[]`, `lyrics.alignments[]` or Clip `vocalPerformances[]` into duplicated source objects on Visit replay. First resolve the inherited 4.2 voice and alignment ownership, then select the concrete Note **attack** occurrences and surviving gates of each `fixed` Visit. A many-to-many or melismatic source Alignment may be partially selected even while the original source data remains valid. A selected Note crossing contiguous source Sections retains its associated source vocal metadata without a duplicate phoneme or onset; a hard cut that shortens its gate does **not** assert that the unplayed portion of an authored phoneme event, pitch/expression curve or technique was reproduced. An explicit deterministic vocal export must remap new Note occurrences to valid lyric/performance references and disclose loss or unresolved timing. The fully worked source witness is `examples/15-vocal-response-phrasing.ostf`; precise non-executing rules are in `NOTE_AND_MIDI_CUT_SEMANTICS.md` Draft 0.43. This is a proposed D01/D04 interpretation, not a new field or singing-synth implementation.


## Draft 0.33 — Operation-scoped authority (publisher review pending)

A reader, previewer, Score writer, Production rebinder, Distributed event acceptor, partial exporter, and publisher perform **separate operations**. Successful parsing does not authorize generation, companion mutation, remote fetching, plug-in/DSP processing or physical robot actuation. Each operation retains its own canonical data authority and reports partial success / loss where material. See `CONFORMANCE.md` Draft 0.33 for the operation table and failure-isolation rule. This is a semantic editorial proposal only; Core JSON shape is unchanged.

---

## Draft 0.32 — Original-byte identity versus information preservation (unratified editorial decision)

**Three separate assertions must not be conflated:**

| Assertion | Required evidence | What it does not guarantee |
| --- | --- | --- |
| **Original-byte Score identity** | SHA-256 of the exact supplied UTF-8 `.ostf` document bytes, bound to the referenced Score and checked before any parse/rewrite | JSON semantic equality, audio playback or external-source authorization |
| **Score meaning-preserving export** | Correct versioned structure, identities, references and original authored musical content, with unsupported optional information retained or losses disclosed | The resulting byte sequence is unchanged (formatting, key order and escaping may differ) |
| **Collection/Asset byte-complete preservation** | Inventory and exact retention of all *actually supplied* Score/Profile documents and supplied opaque Asset byte streams, according to explicitly requested collection scope | Playable plug-ins, same rendered audio, robotic execution or retention of never-supplied Asset bodies |

**Critical binding rule:** JSON parse-and-serialize may preserve the same musical values while changing raw Score bytes. If Score bytes change, the old `scoreSha256` / `score.sha256` is not valid for the newly serialized Score, even when semantic content is judged unchanged. A Writer MUST NOT silently reuse an old companion digest. It must either (a) preserve the original Score bytes unchanged; (b) explicitly create/rebind appropriate companion records with the newly computed digest under the applicable revision and session rules; or (c) decline the operation / issue a clearly labelled partial or lossy output with scope disclosure. A revision or distributed Session must never be silently rewritten merely to make a hash check pass. There is no portable canonical-JSON hashing algorithm in Score Core 4.3.

**External delivery:** HTTP compression and transport headers are not part of the hashed Score bytes. If decoded resource bytes are unavailable, a URI, ETag, digest declaration or visually equal JSON is not proof of Score-byte identity. The implementation must report `not_evaluated` / unresolved binding instead of manufacturing certainty.

This is a **proposed D01–D04 editorial clarification**, not a Schema change, automatic publication approval, required serialized reporting field or completed interoperability validation.

---

## Draft 0.29 — Portable diagnostics and operation capability (editorial proposal)

The accompanying `docs/CONFORMANCE.md` Draft 0.29 section defines optional **reporting categories** distinguishing invalid data, unresolved references, conflicting meanings, unsupported but preservable semantics, missing asset bytes, intentional loss, stale binding and unverified execution. These categories are explanatory terms **outside the serialized OSTF 4.3 Core**. No new Core/Session/Production fields are adopted. Interpretability and non-lossy preservation remain distinct; the author must explicitly approve the convention before final publication.

---

## Draft 0.27 publisher-review guidance (editorial only)

Before treating this material as a published interchange standard, consult `PUBLISHER_RELEASE_DECISIONS.md` decisions D01–D05 and `CONFORMANCE.md` Draft 0.27 for accurate third-party capability claims and input-byte retention expectations. This note creates no JSON parameter or authority to execute devices. All new 4.3 normative proposals remain subject to explicit adoption.

---

## Open Song Timeline Format 4.3.0 — Proposed Normative Specification

**Historical status note (Draft 0.26; not the current edition):** Editorial edition dated 2026-11-14 (not adopted). This document proposes interoperable semantics for the added 4.3 fields. It is not yet an adopted release. Throughout this document, MUST/SHOULD/MAY apply to implementations *claiming the corresponding feature*, not all software.

## Draft 0.26 — Cross-family implementer navigation (editorial candidate)

For a third-party importer or exporter, **the record's exact version discriminator selects its Schema before semantic processing**. Score 4.3 uses `format`/`version`; Distributed Session 0.2 uses a versioned `profile` token (no `profileVersion`); Production Session 0.1.0/0.2.0 uses both `profile` and `profileVersion`. The precise decision matrix and loss/uncertainty reporting states are in `CONFORMANCE.md` Draft 0.26. A successful parse does not certify a coherent multi-record binding, available Asset bytes, plug-in DSP, WAN timing or robot actuation. This note adds no JSON parameter and does not amend the official inherited 4.2 semantics. Publisher ratification and bilingual editorial sign-off remain pending.

## 1. Purpose and scope

OSTF 4.3 is an additive extension to the 4.2 musical document: composition, human/AI improvisation, ensemble interaction, expressive vocals and finite performance-form interpretation can share the same source score and performance-intent data. It does not mandate an AI algorithm, DAW, runtime, HTTP API, robot controller, robot safety envelope, audio renderer or network clock.

## 2. Inherited 4.2 authority

The 4.2 root contains `format`, `version`, `ppq`, `song`, `timeline`, `harmony`, `tracks`, `soundSlots`, `lyrics`, `resources`, with additional inherited optional fields. 4.3 has the same required root fields, but the root version is `4.3.0`. The inherited 4.2 Schema was byte-verified against the published final checksum; see `SOURCE_RECONCILIATION.md`. All prior fields retain their prior meaning, except for the explicit addition of new optional types, properties and reference vocabulary. Schema Draft 2020-12 is the structural authority; this specification is the semantic authority for new fields.

- Harmony describes harmonic context; a Track Direction cannot overwrite Harmony.
- Clips/Notes/MIDI Events contain concrete source performance; Directions do not constitute a second stream of notes.
- Lyrics Documents/Phrases/Units and Alignments are authoritative for text and note alignment. VocalPerformances do not copy lyrics into a competing authority.
- Generation and Provenance record process and history, never automatically invoke an engine.
- Phrase Library templates are not independently sounding notes; concrete Notes remain authoritative.
- Source Timeline and all source-scoped Directions are in integer global document PPQ ticks. Event-relative ticks in Clips retain their inherited meaning. Half-open source ranges are `[start, start+duration)`.

## 3. New `phrasing` Direction

A Track MAY contain a `type:"phrasing"` Direction in `tracks[].directions[]`, following the inherited `id`, `start`, `duration`, `type`, `parameters` shape. Parameters MUST include `adherence` (`strict` or `preferred`) and at least one musical parameter. The optional parameters are:

- `phraseLengthTicks`: `{min,max}` inclusive positive tick bounds; `min <= max`. Describes an approximate phrase segmentation, not a mandatory clip partition.
- `onsetGroupsPerQuarter`: `{min,max}` inclusive numbers in 0–128; `min <= max`. One onset group counts all note attacks at the same tick **within the Track** as one group (chord polyphony does not multiply onset group count). Count per quarter-note over the **authored phrase interval**, not per-second, based on the song PPQ (onset density = distinct onset timestamps × PPQ / interval duration ticks). For an explicitly empty source phrase the density is zero. If a phrase segmentation is not authored, the density is intent for future realization rather than a measurable claim about existing notes.
- `development`: `repetition`, `motivicVariation`, `sequence`, `contrast`, `free`.
- `contour`: `ascending`, `descending`, `arch`, `valley`, `stable`, `free`. Describes a dominant pitched contour, not a prohibition on every local contrary motion.
- `energyShape`: `rising`, `falling`, `arch`, `valley`, `stable`, `free`. Abstract musical energy; MUST NOT be interpreted as a fixed velocity/volume curve.
- `motifRef`: stable ID of `phraseLibrary.templates[]` in the same document. The template MUST exist when referenced.
- `adherence`: `strict` is an explicitly authored constraint; `preferred` is a soft preference. This affects intent-aware realization only. It never invalidates already authored concrete Notes.

`phrasing` does not replace inherited `improvisation` (pitch vocabulary), `pitchRange` (register), `playingRole` (role), or Generation/Groove Intent (process history). No implicit regeneration is permitted upon read.

## 4. New `vocalFreedom` Direction

`type:"vocalFreedom"` MUST use the inherited Track Direction envelope and include a `parameters` object with `voiceId`, `textPolicy`, `melodyPolicy`, `adherence`. Optional `vocalizationKind` and `candidatePhraseSets` apply.

- `voiceId` MUST resolve to exactly one `lyrics.voices[]` whose `trackId` matches the enclosing Track.
- `textPolicy`: `fixed` (authored text is retained), `alternatives` (one of authored phrase sequences MAY be selected), or `open` (text may be realized later; no placeholder Unit is required).
- `melodyPolicy`: `fixed` (authored pitched Notes remain the intention), `ornamentable` (keep phrase identity with expressive pitch/rhythm ornaments), or `open` (melody may be realized later).
- `vocalizationKind`: `lexical`, `scat`, `humming`, `nonLexical`.
- If `textPolicy:"alternatives"`, `candidatePhraseSets` MUST have at least two distinct alternatives. Each set's ordered `phraseIds` MUST resolve to authored Lyric Phrases, all belonging to the target Voice's Lyric Document. The alternative lists MUST NOT be identical. Otherwise `candidatePhraseSets` MUST be absent.

Selection of an alternative MUST NOT silently change `lyrics.alignments`. Any new concrete text, notes, phonetics, and alignment must be materialized by an explicit editing/realization action. A Vocal Freedom Direction by itself never creates an audible voice and does not imply that an instrumental melodic Track is vocal.

## 5. New `ensembleInteractions[]`

Every Interaction is directed (`actorTrackId` acts relative to `partnerTrackId`). Both Track IDs MUST resolve to existing Tracks. **Distinct Tracks** are the ordinary case. **The same Track is permitted only if BOTH `actorVoiceId` and `partnerVoiceId` are supplied, they resolve to different existing Lyric Voices, and both Voices belong to that shared Track.** An Interaction MUST NOT direct a Voice to itself; `actorVoiceId == partnerVoiceId` is invalid regardless of Track IDs. When distinct Tracks are used, Voice IDs are optional but MUST still resolve to their respective Track owners if supplied. This permits two vocal parts carried within one Track to exchange a musical relationship without inventing a second Track or changing lyric ownership. The `relation` value is one of:

- `respondTo`: actor provides a musically responsive part after/during partner material;
- `followRhythm`: actor uses partner attacks/groove as a reference;
- `alternateWith`: actor/partner take turns, not necessarily in a fixed 4-bar pattern;
- `leaveSpaceFor`: actor is directed to avoid masking partner material;
- `reinforce`: actor emphasizes partner rhythm or accents.

An Interaction MUST have a global `(start,duration)` source range, a `scope:{performancePlanId,visitId}`, or both. `scope` references one Plan and one of its Visits. Without `(start,duration)`, scope means the whole Visit. With both, the Interaction applies only to the exact source-tick intersection with the selected Visit segments; non-intersection is a semantic error. A `(start,duration)` range MUST lie inside the source song time domain even when scope is present. Within a Visit that concatenates multiple Sections, interaction timing is mapped per intersecting source segment, not as one unbroken source clock. `responseWindowTicks` is an optional positive source musical-tick interval, not a network latency limit.

Every Interaction MUST include authored `adherence`. Interactions convey neither real-time event messages nor a specific rendering algorithm; multiple relations MAY overlap where not explicitly contradictory. Identical duplicate interactions SHOULD be diagnosed. A directed relation does not imply its reverse. Track role changes and voice ownership are independent of Interaction identities.

## 6. New `performancePlans[]`

A Plan MUST have `id`, `mode:"orderedFinite"`, `defaultRealization`, and a nonempty `visits[]`. `defaultRealization` is explicitly one of `fixed`, `silent`, `unspecified` and applies to Tracks not named in a Visit's `parts`. A Plan is opt-in; an ordinary OSTF reader which ignores it MUST continue to read and preserve original Notes/Timeline.

Each Visit MUST declare a stable `id`, a unique zero-based `ordinal` in the contiguous range `0..N-1` within its Plan, a `parts` array, and EXACTLY ONE source selector:
- `sourceSectionIds`: one or more authored Section IDs in explicit playback sequence (IDs resolve without using name matching); or
- `sourceRange`: a valid nonempty source Timeline range.

Section spans in `sourceSectionIds` are concatenated **without inserting unrepresented source gaps**. The same source Section MAY be revisited in separate Visits, but no overlapping/duplicate source Section spans are allowed within one Visit in this draft. All referenced source ranges must be inside the declared source song duration. Visits are concatenated by `ordinal` to derive *performance* time. For any segment with source start `S` and visit-performance segment start `P`, mapping is `performanceTick = P + (sourceTick - S)`. Every selected source segment MUST lie within the source Timeline, and source pieces MUST be well-defined and non-overlapping inside a Visit. At the beginning of **each concatenated segment**, the effective source Tempo, Meter, Key and Harmony context MUST be re-evaluated from the source maps at the segment start; it MUST NOT inherit a stale context from a preceding Visit. No musical ramp/interpolation is inferred across the cut. A single `performanceTick` can have only one active source position per Visit and one mapped musical context. A source Section MAY reoccur in another Visit. `performanceTick` is a derived coordinate, NOT a second source authority or a new source Note timestamp.

Per-Visit parts identify `trackId` and `realization`: 
- `fixed`: selected source Notes/MIDI remain the **authored source events** for that Part and Visit (possibly empty); the source-event selection is determinate, but actual Note-On/velocity outcomes may still be conditional under inherited 4.2 Note-state fields; see §13 and §Draft 0.40 below;
- `open`: this Visit contains no fixed realization for that part, even if a source Clip contains Notes used in other Visits; this is a *view-specific intentional omission* and MUST NOT mutate original Notes or auto-generate replacements;
- `silent`: the part is silent in that Visit, without deleting source Notes.

A `fixed` part with no Notes still has silence. An unlisted Track uses `defaultRealization`; `unspecified` MUST NOT be silently treated as either playback or omission when making deterministic export claims. To produce reproducible complete music, a generator must explicitly materialize `open` material or provide a disclosed external recording. Runtime realization is an application concern.

`parts[].role` is a visit-local override of the Track default role. If an inherited timed `playingRole` Direction also covers selected source positions and conflicts with that role, the Visit Part MUST explicitly list all affected Direction IDs in `replacesDirectionIds`, otherwise the Plan is semantically ambiguous. Other Direction types continue to apply by their scoped source timing unless otherwise specified in a future revision. An explicitly replaced `playingRole` Direction is suppressed **only for the current Visit and Track**, not deleted or changed in source. All replacement IDs MUST intersect that Visit source interval and belong to its Track; replacement with no applicable time interval is an invalid stale override. A Visit-local role that matches an existing timed role does not require replacement. `replacesDirectionIds` MUST reference only playingRole Directions owned by the same Track.

No infinite loops, conditional cue branching, automatic network renegotiation, or robot actuation are defined by Plan 0.1. Dynamic cues belong to a separately negotiated session-profile extension.

## 7. New `tracks[].performanceRequirements`

An optional Track object describes the *minimum musical requirements of the part*, not what an actual performer can do. Fields: `requiredPolyphony` (1..128), `requiredPitchRange` (`lowPitch <= highPitch`), `requiredArticulations` (open, unique strings), `peakOnsetGroupsPerQuarter` (>0..128). If an authored `instrument.playablePitchRange` is present, the required range MUST be a subset of that range; a contradiction is a semantic error. These parameters describe only a track’s requested musical capability; no one may infer that a specific robot is capable of it. Real robot speed, motor limits, safety interlocks, device mapping, preparation latency, and actuator permissions are OUTSIDE OSTF Core.

## 8. Identity, overlap and preservation

New ID-bearing Core objects (`ensembleInteraction`, `performancePlan`, `performanceVisit` and new Track Directions) join the existing document-local ID uniqueness domain. New reference vocabulary names may be used where `ref.type` accepts them. References MUST resolve by type and ID. A 4.3 Writer MUST preserve unsupported optional data or refuse a purportedly non-lossy overwrite.

Inherited same-Type Direction overlap restrictions apply. For `phrasing`, two authored ranges on the same Track MUST NOT overlap. For `vocalFreedom`, two ranges for the **same voiceId** on the same Track MUST NOT overlap; different Voices on that Track MAY have concurrent Vocal Freedom. Different Direction types MAY overlap because they describe distinct facets, without implicit precedence or order-based 'last wins'.

## 9. Compatibility and migration

A structurally/semantically valid 4.2.0 source may migrate by replacing `version` with `4.3.0` without creating a Phrasing/Plan/etc.; a 4.3 implementation MUST still check the actual final 4.2 schema baseline, not guess migration from shape alone. A pure 4.2 reader is NOT a 4.3 reader. Dropping 4.3 fields on downgrade requires explicit loss reporting. Unknown future versions must not be edited destructively under silent fallback.

## 10. Distributed Session Profile — independent binding

The JSON Schema `ostf-distributed-session-0.1.schema.json` defines *session snapshots and events*, not song fields. Snapshot stores session ID, OSTF document/revision, monotonic state revision, participating entities, and optionally a musical position associated with an identified clock domain/UTC epoch and uncertainty. Events store event ID, issuing participant, base state revision, musical effective position, type and non-executable payload. Neither data shape specifies an HTTP path, WebSocket protocol, a clock-sync algorithm, actuator movement nor an authorization mechanism. Implementers MUST implement authorization, synchronization, jitter buffering, deduplication and safe scheduling independently before claiming remote physical execution.

## 11. Security and conformance

Natural-language `instruction`, prompts, URIs, session event payloads and Vendor data are untrusted data, NOT executable instructions or permissions. A conformant serialization reader MUST NOT auto-fetch arbitrary URLs, run commands, regenerate notes or actuate a robot upon load. Conformance levels are Core Reader/Writer, Direction-aware, Ensemble-aware, Plan-aware, Vocal-aware, Requirement-aware, and Session-profile-aware; feature claims are independent and must not imply unimplemented runtime behavior.

## 12. Release status

The inherited 4.2 Schema is now byte-verified against the published official 4.2.0 SHA256. Release approval is **NO-GO** pending final 4.3 editorial and publication review. The inherited final-4.2 Schema is now authenticated and structurally preserved. Independent tool, DAW, singing-software, network, and robot validation have been intentionally excluded from *this* readiness assessment at the user's request; this exclusion is NOT a claim they passed.

## 13. Draft 0.3 normative clarification — Fixed performance at source cuts

The following resolves ambiguity left open in Draft 0.3 without changing any 4.2 Core Note or MIDI structure. It applies ONLY when a consumer intentionally expands a `performancePlans[]` Visit whose Part resolves to `fixed`.

1. Each selected source segment is half-open `[S,E)`. For each source Clip/Note or timed MIDI Event, compute the **absolute source attack/start Tick** using the inherited Clip-relative coordinate semantics. Only an attack/start Tick `t` with `S <= t < E` is selected. A Note already sounding before `S` does NOT acquire an invented new Note On at `S` merely because its gate overlaps the segment.
2. Distinguish a **continuous source join** from a **cut**. Two adjacent source segments within the **same Visit** form a continuous join for a Track whose resolved Part is `fixed` when the first ends at source Tick `E`, the second begins at the **same** source Tick `E`, and their expanded Performance intervals are adjacent. In that case a Note attacked in the first segment MUST retain its authored gate into the next contiguous segment (if that selected attack is actually realized), bounded by the end of the maximal continuous fixed run; it is not retriggered. At a discontinuity, a Visit boundary, or a change of Part realization away from `fixed`, the Note MUST release at that boundary. A source Note `[t,t+d)` maps to `[mapped(t),mapped(min(t+d,R)))`, where `R` is the end of its maximal continuous fixed run. Original Note duration/IDs MUST NOT change. No new Note On is synthesized when an earlier attack was not selected.
3. MIDI Events (Control Change, Program Change, Pitch Bend, Pressure, etc.) with source start outside the selected segment are not synthesized at entry. At a **continuous join** inside one Visit, previously selected MIDI control state MAY continue in ordinary time order; the join does not itself reset it or duplicate an event. At a discontinuous cut or new Visit, no portable MIDI or plug-in-state checkpoint is implied. The inherited Notes/MIDI Events do not encode a full controller-state snapshot, and a deterministic exporter MUST report unresolved state when the result depends on missing initialization. Merely jumping to a later source section is not permission to replay all earlier source events.
4. At each source cut, Harmony, Key, Meter, and Tempo derive from the **source** at `S` as in Draft 0.3. The expanded performance tick positions are unambiguous, but real-time wall-clock timing is still the host's responsibility. A source map change at exactly `S` is effective at `S`.
5. A Part marked `open` or `silent` does not replay any selected source Notes/MIDI Events for that Part within that Visit. A missing Part with Plan `defaultRealization:"unspecified"` prevents claims of fully determined expanded playback.
6. The rule above applies to score-level MIDI/Note state only. Release tails, reverb, sample audio, voice synthesis, MPE instrument state and physical robot trajectory continuity are NOT standardized by OSTF Performance Plans. An application MUST disclose approximation rather than asserting faithful audio equivalence.

### Example: source cuts and note gates

Source sections A `[0,3840)`, B `[7680,11520)`, and C `[11520,15360)` occur in **one Visit**. A→B is discontinuous: a Note at source 3600 with duration 960 is cut at 3840, so its expanded duration is 240; a Note starting at 7400 that only sustains into B is not retriggered. **B→C is continuous**: a Note attacked at source 11280 with duration 720 is allowed to sound through source 12000 with no duplicate Note On at 11520. A newly attacked Note at 11520 belongs to C only. A later Visit returning to A is a new cut, even if its expanded Performance Tick is adjacent. This scenario is included in `examples/17-fixed-note-source-cut.ostf`.

### Draft 0.40 clarification — Fixed Part is not necessarily deterministic playback (UNRATIFIED)

A `fixed` Part deterministically *selects source Note/Event records* at the chosen source intervals; it **does not** guarantee that every eligible Note produces an audible Note-On or that a complete fixed MIDI output can be derived from the authored JSON alone. Inherited OSTF 4.2 Note state remains authoritative and is not rewritten by Performance Plan expansion:

1. The original `track.enabled`, `clip.enabled`, and `note.enabled` values retain their 4.2 enable/scheduling meaning. When an applicable element is explicitly disabled, its contained events are not scheduled. Do not delete or alter those original objects merely because they do not sound in a Visit.
2. `note.probability` is 0..1 (omitted = 1). At 0, the Note does not sound; at values strictly between 0 and 1 its inclusion in a realized performance is unresolved. OSTF defines **no shared random sequence or draw-per-Visit algorithm**. Equal source Note IDs revisited in two Visits do not imply the same stochastic outcome or two independently authored source Notes.
3. `note.velocityDeviation` is an optional 4.2 variation endpoint relative to authored `velocity` (omitted = 0); a nonzero value does not specify a portable sampling law or a uniquely determined outgoing velocity. Omitted `velocity` remains **unspecified** rather than an implied value. Neither value may be silently normalized during Plan projection. `releaseVelocity`, `pitchRole` and other inherited Note fields keep their existing meanings.
4. An application claiming *fully deterministic Note/MIDI export* MUST either use already resolved concrete Note/velocity outcomes or explicitly materialize the realization into a separately authored Score revision with fully specified Note states. The materialized Notes receive distinct IDs for distinct Visit occurrences, while the original source and provenance are retained as appropriate. Do not call an unresolved probability, velocity deviation, unspecified velocity, or earlier MIDI controller/program state a deterministic output.
5. `open` and `silent` remain distinct from a `fixed` Part containing disabled/probabilistic Notes. An `open` Part supplies no source fixed playback for the Visit; a `fixed` Part continues to reference its authored sources even when their inherited enabled/probability values result in silence. Do not reinterpret the former as a command to improvise, or the latter as an automatic generator.

This is an **editorial clarification of inherited 4.2 fields**, not a new 4.3 JSON field, PRNG standard, or mandatory renderer. See `NOTE_AND_MIDI_CUT_SEMANTICS.md` for the proposed source-cut event table and `examples/25-source-note-repeated-visits.ostf` for an illustrative repeated source Note with stochastic state. D01 (musical semantics) and D04 (editorial/example approval) remain unsigned.

## Draft 0.42 — Note-targeted MIDI event association across finite Plan cuts (D01/D04 PENDING)

The inherited 4.2 `targetNoteId` on Control Change, Pitch Bend, Channel Pressure, and Poly Pressure is a **semantic association with an authored source Note**, not a substitute for MIDI channel/pitch wire semantics. It is NOT a new source Note or guaranteed per-note actuator routing. This proposal applies to a **derived fixed-Plan selection view**, not to validating or rewriting original 4.2 events.

1. Compute each MIDI event's source position using `clip.start + midiEvent.start`; select its original record exactly once if that source Tick lies in an eligible half-open source segment of the current `fixed` Part and Visit. An event exactly at an adjacent source boundary belongs to the next segment. Events in skipped source gaps are not synthesized or copied as a state checkpoint.
2. An **untargeted** event remains a channel/bus-scoped authored source event, selected solely by its own source Tick. Its prior MIDI Program/CC/Bend state at a hard-cut entry can still be unknown; do not invent a snapshot.
3. A **targeted** event only has a resolvable *Visit-local Note association* when the referenced source Note has an eligible selected attack occurrence whose gate is still within the same continuous fixed run at that event's Tick. A Note attacked in the skipped region is **not** selected merely because its later targeted event lies inside a selected segment. The continuous-join rule may carry a selected target Note into the following contiguous Section without creating a duplicate Note occurrence.
4. When the referenced Note has no eligible active occurrence, is disabled, or has a potentially suppressed Note-On due to probabilistic realization, the event is **not automatically reinterpreted as an untargeted channel event, assigned to a different Note, or claimed to be a deterministically rendered per-note gesture**. The source event bytes remain intact. A deterministic expanded-MIDI writer must make and disclose an explicit omit/preserve/approximation policy or decline the conversion. This caveat is especially important for MPE member channels and multi-timbral routing. A derived source-selection preview may label such an event `unresolved_target` without declaring the original Score structurally invalid.
5. A selected targeted event carries the original `targetNoteId` in source documents. For expanded *diagnostic* views, associate it with the selected **derived Note occurrence** `(performancePlanId, visitId, sourceAttackSegmentOrdinal, sourceNoteId)`; its own MIDI-event occurrence may use `(performancePlanId, visitId, eventSegmentOrdinal, midiEventId)`. These are computed addresses, never new Core IDs. Event and Note ordinals may differ for a sustained Note across a continuous join. Explicit materialization into a new Score needs fresh Core IDs and rewritten valid target references; none is created by merely reading a Plan.
6. The existing 4.2 MIDI `order` resolves ordering among same-Tick MIDI Events only under its inherited rules. This amendment does NOT invent a universal Note-On versus controller ordering at an identical Tick or mandate a plug-in/MPE playback policy. Report unresolved ordering instead of inventing a deterministic MIDI wire sequence.

**Worked static witness — `examples/17-fixed-note-source-cut.ostf`:** In the first Visit, `target-prior-note-selected` at source 3750 is associated with source Note `cut-shortened` in Section One. `ctrl-omitted-gap` at 4000 is not selected. On the source jump to Section Two, `program-on-source-entry` at 7680 is included once, while `target-prior-note-not-selected` at 7800 references the unselected `cut-pre-sustain` attack at 7400 and therefore has no selected target occurrence. At the continuous Two→Three source join, `controller-on-contiguous-join` at 11520 is selected once and `target-across-contiguous-join` at 11760 remains associated with the already-selected `carry-across-contiguous-join` Note attacked in Two. The later One Visit supplies separate derived occurrences for One; it does not reuse the first Visit's MIDI state. These cases are a **non-executing data interpretation example**, not a DAW/robot test or new serialized requirement.

## 14. Draft 0.3 normative clarification — Phrasing interpretation

- `phraseLengthTicks` and `onsetGroupsPerQuarter` express constraints on *future realized phrasing*; they do not imply that a source Clip, Section, a bar, a lyric Phrase or a Note is a uniquely determined phrase boundary.
- For an authored explicit phrase, count distinct Note onset timestamps **in the relevant Track and bounded phrase interval**. Simultaneous polyphonic attacks count as one onset group. The average density is `(onset group count * document ppq) / phrase duration ticks`.
- Without explicit realized phrase segmentation, one cannot assert that a stored passage has passed strict phrase-length/density constraints. A feature-aware reader may preserve the Direction and report `not-assessable`, but MUST NOT silently infer its own phrase boundaries as the only standard interpretation.
- `adherence:"strict"` constrains a subsequent realization **if that feature is supported**; it does not retroactively invalidate existing fixed Notes. Contradictory strict Phrasing and Pitch/Role guidance must be reported as unsatisfiable when identified; no last-wins array semantics.

## 15. Draft 0.3 normative clarification — Scope and authority

- Track-level Directions use the authored **source** absolute Tick range. Repeated sections duplicate the effective *meaning* in each Visit, but do not duplicate source IDs.
- An Interaction scoped by Plan/Visit is evaluated independently for each source segment in that Visit. It applies only to the intersecting source ticks and to the named actor/partner Track/Voice objects; it MUST NOT reach other Visits simply because their source positions are the same.
- A Visit-local `parts[].role` replaces the *Track default role* for the whole Visit, subject to explicit `replacesDirectionIds` when an inherited timed `playingRole` conflicts on selected source material. The replaced Direction remains untouched in the OSTF Core and remains active in other Visits.
- Unknown `relation`, `development`, `vocalizationKind` or policies must not be guessed into known meanings. A consumer lacking the corresponding feature may preserve it without realizing it.

## 16. Draft 0.3 normative clarification — Lyric alternatives

`vocalFreedom` means an **authoring/realization permission**, not an automatic rewrite of existing Lyrics. For `textPolicy:"fixed"`, the authored Lyric Unit sequence and text are not rewritten; for `alternatives`, only listed Phrase ID sequences are eligible; for `open`, concrete words need not exist yet. Any chosen or newly authored concrete phrase requires distinct normal Core phrase/unit identities and valid Alignments to any realized Notes before a fixed vocal export can claim reproducibility. `melodyPolicy:"ornamentable"` does not itself materialize MIDI or vocal curves; existing 4.2 VocalPerformance remains authoritative for authored voice expression.

## 17. Compatibility and editorial priority

Rules in §§13–16 are part of the proposed 4.3 semantic authority. They do not add mandatory fields. The 4.2 source data model, including absolute-vs-local Clip timing, remains unchanged. The companion Distributed Session Profile is independently versioned; Draft 0.3 proposes Profile 0.2 with typed event payloads alongside archived Profile 0.1, neither of which is a required Core implementation.

## 18. Draft 0.4 clarification — Occurrence identity during finite Plan expansion

An OSTF source Note ID identifies the **source** Note, not every sounding event after Plan expansion. A Plan-aware renderer MAY derive a private occurrence key as `(performancePlanId, visitId, sourceSegmentOrdinal, sourceNoteId)`; this key is **not a new Core object identity** and MUST NOT be stored as a duplicate source Note ID. The `sourceSegmentOrdinal` is the zero-based order within one Visit's chosen source Section sequence (or zero for a single `sourceRange`). A repeated source Note thus has different *performance occurrences* in different Visits while retaining the same authored source Note ID. For each fixed occurrence, event onset is mapped using the chosen segment's source-to-performance Tick mapping; the sounding Note gate is cut at the selected source segment end as specified in §13.

A renderer with only a *source* Note ID MUST NOT mistake a repeated later Visit for the first appearance. At a cut, any Clip-local Note start is first converted to the document source Tick using the inherited Clip start; a negative Clip-local start is not itself a license to synthesize a new Note-On at a later segment entry. Source Note identity is unchanged when selected multiple times.

**Materialization is a separate authoring action:** converting expanded Visit occurrences to a new fixed `.ostf` song MUST mint distinct new source Note IDs for each occurrence, create an explicit resulting document revision, and preserve provenance of the original source, Plan, Visit and segment where supported. Merely reading or rendering the Plan MUST NOT write such new Notes. Collision-free identity generation and materialization are the exporter/editor's responsibility; there is no normative implicit canonical Note-ID algorithm in this format.

## 19. Draft 0.4 clarification — Explicit event identity and absence of execution authority

New Core `ensembleInteractions` between two Lyric Voices on the same Track are valid only under §5's explicit distinct-Voice conditions; Voice ID ownership remains bound to the inherited 4.2 `lyrics.voices[]` authority. OSTF does not infer multiple audio voices merely from storing two Voice IDs. A Plan scoped interaction applies by its Visit identity; a duplicated source Section in another Visit does not inherit that scope. No event proposal, Web API URI, or Note materialization example conveys authorization to actuate a robot, call a model, or transmit external data.

## 20. Draft 0.5 clarification — Lyrics and VocalPerformance on fixed Plan cuts

Plan expansion does not create new authoritative `lyrics.*` IDs, nor does replaying the same source Note create new source lyric content. A fixed, repeated source Note is a distinct **performance occurrence** using the same authored Note ID, with the source Lyric Voice, Units and Alignments unchanged. At finite source cuts, MIDI Note gates can be clipped under §13, but phoneme events and expression curves must not be silently adjusted or invented to make truncated vocal delivery appear lossless. Source Units aligned to multiple Notes require an explicit re-assessment when only some aligned Notes are selected. A reader must report unresolved or lossy fixed-vocal materialization and must not silently manufacture a replacement 4.2 Alignment. The detailed editorial rule is `docs/SPECIFICATION.md`; the 4.2 VocalPerformance schema remains unchanged.

## 21. Draft 0.5 companion Profile 0.2 lifecycle note

`sessionStarted` and `commitmentWindow` are **not 4.3 Core parameters**. They amend only the proposed, separately versioned Distributed Session Profile 0.2; see `docs/SESSION_STATE_MACHINE.md`. Core Reader compliance must not be mistaken for remote orchestration capability.

## 22. Draft 0.6 companion Profile interoperability boundary

No change to Core 4.3 field definitions is made in Draft 0.6. A session phrase cannot silently convert source `fixed` material into a generated part, or perform on `silent` material. The separately versioned Profile 0.2 permits `phraseCommitted` only in an explicitly `open` pinned Performance Plan Part, completely within one Visit. The normative proposed algorithm and its late-join constraints are in `docs/SESSION_STATE_MACHINE.md`. This is a cross-document rule, not an alteration of OSTF's source musical authority.

## 23. Draft 0.7 companion-only clarifications — Frozen source and accepted-phrase history

The OSTF 4.3 **Core** remains a portable musical score/intent document. Its source document/revision, authored Track/Note/Lyrics authority and finite Performance Plan are **not mutable by Session events**. A Profile 0.2 Session may pin one source `(documentId, revisionId, performancePlanId)` and must treat changed source bytes/semantics under the same revision as an integrity conflict rather than a transparent refresh.

The separate Profile 0.2 candidate now explicitly distinguishes (a) event *acceptance* in an append-only authoritative revision log, (b) selected Visit traversal along a monotonic expanded Performance Tick axis, and (c) actual audio/robot performance, which the JSON cannot certify. An authorized stop or forward Visit skip does not delete historical accepted phrases or imply that skipped/unplayed future phrases sounded. Event-ID replay is resolved before stale-base-revision rejection; a new stale Event remains invalid. An assignment change does not transfer execution authority for accepted phrases or rewrite Core Tracks. The complete companion semantics and proposed diagnostics are in `docs/SESSION_STATE_MACHINE.md` (Draft 0.7 section). None of these refinements adds new Core or Session JSON fields, new actuator commands or automatic rendering behavior.

## 24. Draft 0.8 companion profile integrity amendment

The separate **unreleased** Distributed Session Profile 0.2 now rejects a `position` object in an `assignmentChanged` payload. A corrected JSON Schema conditional enforces the existing musical separation between Track assignment and musical-clock anchoring. At Draft 0.8, `sessionStarted` alone carried the clock position; Draft 0.10 supersedes that limitation by requiring an anchored `position` also on `visitChanged`. All retained Session phrases, with or without a `commitmentWindow`, have Note gates bounded by their own phrase duration. A historical commitment retained after stopping or a forward Visit skip need not imply a currently assigned performer or physical playback. Incoming matching Event IDs still require authentication and immutable Session/Score identity verification before any replay acknowledgment; only the stale state-Revision comparison may be bypassed for an accepted identical retry. Parsed-event comparison is independent of object property order, and numeric equality must be exact. The unchanged OSTF 4.3 Core Schema carries no live participant/clock state. Detailed rules: `SESSION_STATE_MACHINE.md` § Draft 0.8.

## Draft 0.9 companion Profile source-binding amendment

OSTF 4.3 Core fields, root requirements and inherited 4.2 musical authority are **unchanged**. The separately versioned, still-unpublished Distributed Session Profile 0.2 now requires root `performancePlanId` and exact-byte `scoreSha256` in Snapshots and Events. This resolves ambiguity when a `prepared` Snapshot has no Position and provides an explicit content-integrity check beyond document/revision name matching. A nested Position's Plan must match the record's root; changed source bytes must not be silently rebound in an active Session. SHA-256 pinning is neither authentication nor a physical robot permission. The candidate normative source of truth is `SESSION_STATE_MACHINE.md` § Draft 0.9.

## Draft 0.10 — Companion remote Visit anchoring

Only the separate unratified Distributed Session Profile 0.2 changes in this revision. A `visitChanged` event now requires a new authoritative `position` mapping the target Visit beginning from source musical Tick to expanded Performance Tick and clock-domain UTC. It must match `targetVisitId`, the pinned Plan, and the enclosing `effectivePerformanceTick`. Previous `sessionStarted` anchoring remains. Profile 0.1 remains version-distinct. This is a remote session event-format requirement, not a new OSTF 4.3 Core field or a promise of physical synchronization. See `SESSION_STATE_MACHINE.md` Draft 0.10.

## 4.3 Draft 0.11 candidate — Session clock continuity without Core changes

The **separate**, unpublished Distributed Session Profile 0.2 now specifies continuity of the `clockDomainId` established by `sessionStarted` through subsequent `playing` Snapshots and `visitChanged` records. Source `timeline.tempoChanges` remains the sole musical tempo authority at every mapped source Tick: optional `position.tempoBpm` is redundant and MUST agree exactly, and cannot fill in missing source tempo. `sessionStopped.effectivePerformanceTick` is audit context, not a scheduled future stop. These are **proposed semantic requirements**, with no added Core fields or 4.2 change. `SESSION_STATE_MACHINE.md` Draft 0.11 is the detailed reference.

## Draft 0.12 companion-session clarification — authoritative Tempo at a clock anchor

For a separate Distributed Session Profile 0.2 running clock Position (`playing` Snapshot or `sessionStarted` / `visitChanged` Event), the active source score Tempo MUST resolve at `sourceTick`, even if optional `position.tempoBpm` is omitted. If absent, the Session record has no valid running clock anchor and MUST NOT claim synchronized performance. Source segments and Tempo changes are integrated piecewise when deriving ideal musical elapsed time from an anchor; a cut does not inherit the skipped interval's BPM. The companion Snapshot's required `participants[]` now has `minItems:1` to support authority resolution. These new constraints do not change any 4.3 `.ostf` Core musical field. See `SESSION_STATE_MACHINE.md` for detailed semantics. Publisher adoption remains pending.

## Draft 0.13 — Separate Production Session Profile (non-Core)

A third-party app MAY store stereo/mono mixer Mute/Solo/Gain/Pan, audio Buses and Sends, ordered plug-in/effect chains, plug-in identities, opaque state asset references, parameter automation and host extensions in the **independent** `OSTF-Production-Session` Profile `0.1.0`. None of these are new OSTF 4.3 Core fields. `tracks[].enabled` and MIDI CC events retain musical/source authority; production Mute/Solo and audio Gain/Pan are separate authorities. This Profile also does not encode participants or clocks from **OSTF Distributed Session Profile 0.2**. Readers that understand only Core MAY ignore the external Profile. See `PRODUCTION_SESSION_PROFILE.md` for the proposed Profile's normative fields, conflict and preservation rules. Public adoption remains pending.

## Draft 0.20 companion-boundary note — score revisions

The Core 4.3 JSON musical semantics and `document` lineage are not extended by this editorial update. An independently versioned Production Profile may be re-associated with a changed Score only through an explicitly authored new copy and a deliberate source-Tick/Track review; a new score digest on an old Production profile is not proof of mapping equivalence. A live Distributed Session cannot silently rebind to a newer score revision; it requires a new Session ID and fresh event/clock state. See the candidate Production Profile §26. This boundary is non-executable and does not grant automatic Web API fetch or physical actuation rights.

## Draft 0.21 — Portable interchange and non-lossy claims

This change **adds no Core fields**. OSTF 4.3 musical authority remains Score/Timeline/Harmony/Notes/MIDI/Lyrics/Directions, independent of non-executable Production and Distributed companion JSON documents. An application that reads only Score 4.3 MAY ignore companions, but MUST NOT claim it preserved a bundled Production/Distributed project non-lossily if it discarded those documents or referenced Asset bytes. A claimed non-lossy Writer must preserve unsupported optional Core fields or explicitly refuse/label a lossy export. An exact-byte Score change invalidates old companion source hashes until explicitly re-bound; it does not authorize reusing a live remote Session. The proposed feature-level preservation/reporting contract is described in `CONFORMANCE.md` and Production Profile §27. It is not an executed transport, renderer, plug-in host or robot-control specification.

## Draft 0.22 — Explicit authority of the separate companion documents

OSTF 4.3 is a versioned **Score JSON model**. A Production Session Profile or Distributed Session Profile is **another independently versioned JSON document**, not a hidden OSTF Score field. Each explicit Profile schema governs only its own JSON record and does not change Core Note, Track, Harmony, Lyrics or MIDI authority. The packaged `PACKAGE_MANIFEST.json` and release ZIP are publisher development artifacts, not OSTF music-production interchange structures. This release does **not** standardize a multi-file Production archive container or HTTP API.

For an implementation's data claim, distinguish Schema structure, feature-specific proposed normative semantics, example illustrations, opaque referenced Asset bytes and real application/robot execution. Do not infer permission to fetch assets or execute JSON as instructions. Unknown/conflicting semantics must be surfaced for publisher resolution rather than silently chosen from the latest historical Draft paragraph. See `CONFORMANCE.md` and Production Profile §28. All these statements are unratified Draft editorial guidance, not new Core fields.

## Draft 0.23 — Current interpretive priority across Score and companions (editorial proposal)

For implementers reading the cumulative Draft history: structural field/requiredness authority comes from the **exact version-matched Schema**; 4.2 musical semantics come from the inherited official 4.2 specification; proposed 4.3 semantics come from the *current* Core sections here. Companion Distributed/Production semantics are governed by their **own version-matched** Profile specification and Schema. Earlier historical companion paragraphs are retained for editorial traceability, not alternative rules that can override the current exact-byte pin and source-Tick boundary requirements. A conflict between current candidate normative texts is a **publication defect requiring a publisher decision**, not permission for a tool to choose last-wins or infer behavior.

`scoreSha256` and `score.sha256` are defined only by their respective companion Profile versions, over the original Score bytes, **not** as new Core 4.3 root fields. A `phraseCommitted` belongs to a live Distributed Session's record, not to Core `notes[]`, Production `audioRegions[]` or plug-in parameter values. An application's binding of those sources remains informational, not authority to install plug-ins, transmit audio, write a new Score or actuate a remote robot. This clarifies existing proposals and adds no Core field or automatically executable instruction.

## Draft 0.24 — Exact companion-family selection and event authority (editorial candidate)

The OSTF music Score is selected using `format:"OSTF"` and `version:"4.3.0"`. Distributed 0.2 Snapshots/Events are selected using `profile:"OSTF-Distributed-Session-0.2"` and `recordType` and have **no `profileVersion`**. Production 0.1/0.2 is selected using `profile:"OSTF-Production-Session"` and mandatory `profileVersion:"0.1.0"` / `"0.2.0"`. These documents are not secretly embedded in the Score, and neither a filename nor API endpoint substitutes for their exact discriminators. The tabular authority and conformance rules are in `CONFORMANCE.md`.

A novel accepted state-changing Distributed Event requires the current `baseStateRevision` at admission. After independent authentication/Source pin verification, an identical previously accepted eventId/full parsed event is a **no-op** even if its historic base revision is old; altered same-ID content is an integrity conflict. A newly submitted stale command is rejected, not reclassified as an authoritative proposal. No Event grants Score editing or physical actuation rights. All existing 4.2 Core semantics and six existing Schema structures remain unchanged, subject to publisher ratification and publication rights approval.

## Draft 0.25 — Separate data authorities and software support claims (editorial candidate)

Fixed OSTF Note/MIDI values, musical performance Directions, accepted remote Session Events and Studio Mixer/AudioRegion/plug-in descriptors each have a **distinct authority**. JSON parsing alone does not imply full non-lossy preservation, sound generation or robot control. An accepted remote phrase is not an automatic edit to Score Notes. Persisted Asset *descriptors* are not preserved Asset *bytes* if the referenced source material was not supplied. Revising a Score does not implicitly rebind its pinned Production/Distributed companions.

See the current decision matrix, capability wording and failure classifications in `CONFORMANCE.md` Draft 0.25. The six shipped Schemas and inherited 4.2 authority remain unchanged. These additions are unratified pending final bilingual editor and rights-holder approval.

### Draft 0.41 — Continuous-source join versus hard cut (UNRATIFIED)

For each Track and ordered source segment pair in a finite Visit, a continuous join exists **only** when `previous.endSourceTick == next.startSourceTick`, both occupy adjacent expanded intervals, and that Track's resolved realization is `fixed` on both sides. A new Visit is a hard cut even if source intervals happen to be numerically adjacent: Visit roles, source occurrences and session transition semantics are separately scoped. Any source gap, backwards jump, overlap-invalid pair or change to `open`/`silent` terminates the fixed voice. A same-Tick Note attack at the join belongs to the following half-open segment and is emitted once. In a continuous run, a selected earlier attack's gate is mapped through the join **only until the end of the maximal run or its authored Note end, whichever is earlier**; do not insert a duplicate Note On or artificial release/retrigger. Per-Note probability and velocity-deviation remain unresolved exactly as in Draft 0.40; extending a selected gate is not a probability draw. This rule concerns source Note/MIDI timing, not continuous acoustic output, synth release tails, plug-in tails, audio-region fades, vocal phoneme rendering, or robot actuator trajectories. Underlying `notes[]` and MIDI Events remain authoritative and unmodified. See `NOTE_AND_MIDI_CUT_SEMANTICS.md`, the updated `examples/17-fixed-note-source-cut.ostf`, and D01/D04 approval gates.

## Draft 0.45 — Voice/Clip-wide vocal data under finite fixed Plans (S24, UNRATIFIED)

The inherited 4.2 VocalPerformance model also permits **non-note-targeted**
`breathEvents`, `techniques` without `targetNoteId`, `phonemeEvents` without
`noteId`, and `expressionCurves` without `targetNoteId`. These do not become
Note-scoped simply because the same Voice has a Lyric Alignment. For each
finite `fixed` Plan Visit, select a discrete item's original onset from the
Clip-relative time converted to absolute Score Tick; a skipped onset stays
unselected, a contiguous fixed join keeps one ongoing occurrence, and a hard
cut ends any selected ongoing item. An unbound phoneme retains its Unit and
Voice attribution but cannot be claimed as a fully specified Note/phoneme
association. Voice/Clip-wide curves are projected from their *source-time*
interpolation on selected segments, never by extrapolating missing values,
carrying a prior Visit's value, or rewriting 4.2 source points. A single-point
curve is constant over the applicable Clip/Voice scope; multi-point curves are
unspecified outside their authored point span. Existing note-targeted curves
replace overlapping Voice/Clip values where 4.2 defines such replacement;
they are not summed. Neither an audible rendering nor the automatic creation
of new Units/Alignments/Notes is specified. See `SEMANTIC_RULES.md` S24 and
the updated `examples/15-vocal-response-phrasing.ostf`. This is an editorial
D01/D04 proposal only.


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
