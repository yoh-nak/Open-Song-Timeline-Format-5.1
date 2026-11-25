# OSTF Project Package 1.1 — Normative specification for OSTF 5.1 (5.1.0)

## 1. Purpose and representation

OSTF TEXT (`.ostf`) remains a standalone UTF-8 JSON Score. OSTF PROJECT (`.ostfp`) is an **optional ZIP carriage** for exactly one authoritative Score (4.3.0, 5.0.0 or 5.1.0), independent Production/Distributed JSON records and optional actual asset bytes. It does not merge the musical and production authorities or turn text into a binary-only format. A Project Directory is the **unpacked working representation** of the same logical content, not a third interoperable file extension. Source document bytes MUST NOT be changed solely by packaging or unpackaging.

## 2. Archive members, path and media identifier

1. Member 0 **MUST** be `mimetype`, stored without ZIP compression and with exactly the ASCII bytes `application/vnd.ostf-project+zip` (no BOM, whitespace or line break). This is a **proposed, unregistered** media type; no IANA registration or server availability is asserted.
2. Member 1 **MUST** be `manifest.json`, an unencrypted UTF-8 JSON object conforming to `schema/ostf-package-manifest-1.1.schema.json`.
3. Remaining members are the one authoritative Score and exactly those companion JSON documents and binary assets declared by the manifest. Directory placeholders are optional; receivers MUST NOT treat them as content assets. Only ZIP `Stored` and `Deflate` compression are supported; ZIP64 is allowed. Encryption, executable-package semantics and code installation are not standardized.
4. Paths are case-fold-unique, NFC-normalized POSIX relative paths: no absolute paths, drives, backslashes, dot/parent segments, control characters, `mimetype` or `manifest.json` collisions, or names that escape the project root. Reject symlinks and other filesystem redirects on extraction.

A reader MUST treat any ZIP/archive input as untrusted. It MUST use bounded resource budgets, reject duplicate/normalized/case-fold collisions and unexpected members, and prevent Zip Slip, decompression bombs, directory symlink traversal, or premature filesystem changes. The provided `tools/ostfp.py` is an illustrative prototype with its own resource budgets, **not** a security certification or universal limit prescription.

## 3. Manifest identity and byte inventory

Required fields: `packageFormat:"OSTFP"`, `packageVersion:"1.1.0"`, `projectId`, `title`, `score`, `documents[]`, `assets[]`, `bindings[]`. There is exactly **one** authoritative `score` descriptor (`path`, `format:"OSTF"`, `version:"4.3.0"|"5.0.0"|"5.1.0"`, `sha256`). `documents[]` has `id/role/path/family/version/sha256` and optional `required`; `assets[]` has `id/path/purpose/sha256/mediaType/sizeBytes` and optional rights notices. `metadata`, `externalAssets[]` and `extensions` are optional non-authoritative data. For all descriptors, hashes are SHA-256 of **uncompressed exact file bytes**, not ZIP container bytes or JSON-canonicalized objects. An asset's `sizeBytes` is its actual byte length. The manifest itself does not self-hash.

Every content member other than `mimetype` and `manifest.json` MUST be listed **once and only once** among Score, documents and assets; no undeclared or missing payload is permitted. Descriptor paths and IDs are subject to namespace-appropriate uniqueness. A metadata descriptor does not make a second Score authoritative. Array order does not select a new musical authority.

## 4. Version and Score-identity matrix

| Score payload | Production companion | Distributed companion | Manifest family/version values |
|---|---|---|---|
| OSTF 4.3.0 | Production Session 0.2.0, if present | Distributed Session 0.2, if present | Production: family `OSTF-Production-Session`, version `0.2.0`; Distributed: family `OSTF-Distributed-Session-0.2`, version `0.2` |
| OSTF 5.0.0 | Production Session 0.3.0, if present | Distributed Session 0.3, if present | Production: family `OSTF-Production-Session`, version `0.3.0`; Distributed: family `OSTF-Distributed-Session-0.3`, version `0.3` |
| OSTF 5.1.0 | Production 0.4.0 | Distributed 0.4 | `OSTF-Production-Session` / `0.4.0`; `OSTF-Distributed-Session-0.4` / `0.4` |

For Production, payload `profile` and `profileVersion` MUST match the descriptor and `score.formatVersion` and `score.sha256` MUST match the manifest Score version and exact original bytes. If supplied, `score.documentId` and `score.revisionId` MUST identify the Score document. For Distributed, payload `profile` MUST match `documents[].family`, and `recordType` MUST be the corresponding `snapshot` or `event`. **Distributed 0.3/0.4 has no nested `score` object and no `profileVersion`; it uses root `scoreSha256`, `documentId`, `revisionId` and `performancePlanId`.** Those fields MUST match the Score's raw digest, document identity and a real finite Performance Plan. The analogous original root binding of Distributed 0.2 is evaluated under the adopted 0.2 normative source. Do not relabel existing 0.2 sessions, accept stale pins, or convert authority by changing a discriminator.

`documents[].role:"supplement"|"metadata"` does not create Profile or Score authority. Their `family`/`version` identify the actual supplied bytes; unknown such documents may be retained without their semantics being interpreted. A Plugin Context message is **not** a Project document that authorizes a Score edit; archive copies of such messages, if explicitly retained as supplements, are inert data.

## 5. Asset bindings and unresolved resources

`bindings[]` maps one `(documentPath,resourceKind,resourceId)` to one `assets[].id`. `resourceKind` is `coreResource` (Score `resources[].id` only, using `score.path`) or `productionAsset` (the named Production document's `assets[].id`, including `pluginState`). Binding member paths are resolved from **project root**, not relative to the JSON document's folder. Each binding MUST resolve to exactly one real resource and one packaged asset; duplicate tuples, conflicting SHA, mismatching purpose/mediaType where asserted, and unknown document paths are invalid. Package binding **never edits** source JSON `uri`, `sha256`, Score Revision or other data. The rules in this section are the binding authority.

`externalAssets[]` describes references not included as bytes. Retain an unresolved descriptor without claiming the audio or state bytes were supplied, and never automatically fetch an HTTPS reference. The actual media rights, plug-in state compatibility, plug-in installation and audible/DSP equivalence are outside the package guarantee.

## 6. Working directory, transaction, and portability assertions

A Project Directory contains the same `mimetype`, `manifest.json` and exactly declared content paths as an OSTFP archive. Packing or unpacking must retain each declared Score/Profile/Asset payload byte sequence. It need not preserve ZIP member metadata, compression stream or archive SHA. Exporters SHOULD prepare complete content and a matching manifest in a staging area, then publish a consistent generation; OS-level atomicity across multiple directory files is not promised. Do not silently rebind a Production/Distributed Score pin after a Score edit. A Score-only archive is valid; it is *not* a lossless **project** export if the operation's supplied input included Production, Session or asset bytes that were omitted. Missing assets and lossy scope MUST be reported as in `MIGRATION_MATRIX.md`.

## 7. Interoperability and scope of promises

Schema structure, semantic cross-references, source byte identity, package inventory and safety checks are distinct responsibilities. A valid archive is not a VST3/AU/CLAP plug-in, a DAW project executor, a studio reconstruction certificate, a copyright license, an audio rendering guarantee or a real-time distributed session. Implementations advertise feature-by-feature conformance as in `CONFORMANCE.md`; none is automatically granted by this document.

## Preserving take material

Manifest 1.1 carries 4.3/5.0/5.1 at their exact original identities. Legacy Manifest 1.0 does not accept Score 5.1. Production 0.4 uses nested `score.sha256` and optional `score.documentId/revisionId`; Distributed 0.4 uses root `scoreSha256`, `documentId`, `revisionId` and `performancePlanId`. Lossless OSTFP export retains unselected take audio and every materialized Comp output. Supporting comping does not authorize pruning source assets. An active-result-only export is an explicitly partial export.
