# OSTF 5.1.0 — Release status / リリース状態

**Decision: READY for the official written specification release `v5.1.0`.**  
**判定：仕様として正式リリース可能。**  
Date: 2026-11-25 (Japan)

## Completed deliverables / 完了した成果物

| Item | Status |
|---|---|
| 5.0 baseline integrated | Complete; exact source archive identified |
| Take/Comp semantics | Approved current specification, Japanese and English |
| Current complete Schemas | 5 files, no external merge required |
| Legacy source retained | 5 original 5.0 Schemas + 13 original adopted 4.3 files |
| Full manuals and references | Japanese/English; all 2,341 current structural declarations |
| Samples | 36 files: 22 .ostf, 6 .ostfp, 8 companion JSON |
| Release notes / licenses / provenance | Included |
| File inventory | 100 repository files, within the requested 100-file limit |
| Individual specification approval | Already granted by publisher instruction |
| Runtime validation | Excluded from release criteria; not performed |
| GitHub upload / remote tag | Not performed by this artifact preparation |

## Editorial assembly record

The following records document/byte consistency, not software runtime behavior. The source examples were statically compared with their Schemas during authoring; the included reference tools were not run. Full musical rendering/DAW/plugin/network interoperability is not certified.

- repository_files_including_checksum: 100
- current_schemas: 5
- retained_original_files: 18
- plain_json_documents_parsed: 43
- example_files: 36
- standalone_ostf: 22
- ostfp_archives: 6
- companion_json: 8
- package_payload_hashes_matched: 19
- packaged_audio_asset_descriptors: 7
- current_local_links_resolved: 679
- original_score_themes_mapped: 25
- runtime_tests_performed: False
- delivered_reference_tools_executed: False

## Publication package

Extract `OSTF_5.1.0_GitHub_Release.zip` at the intended repository root. Keep the versioned legacy Schema files and `adopted-4.3` intact. Use `RELEASE_NOTES.md` for the `v5.1.0` release description and include the archive as the release asset. SHA256SUMS records every repository file except itself; the archive digest is recorded in the delivery receipt.

This is a completed written-specification package. It is not a pending draft, a request for further approval, or an implemented/tested OSTF Studio release.
