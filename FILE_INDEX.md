# OSTF 5.1.0 — File Index / 全ファイル目録

**100 files in the repository distribution / 配布物は全100ファイル。**

## Reading order / 読む順番

| Purpose / 目的 | 日本語 | English |
|---|---|---|
| Learn the complete format / 全体を理解する | [全網羅マニュアル](docs/COMPLETE_MANUAL.ja.md) | [Complete manual](docs/COMPLETE_MANUAL.md) |
| Look up every parameter / 全項目を調べる | [全パラメーターリファレンス](docs/PARAMETER_REFERENCE.ja.md) | [Parameter reference](docs/PARAMETER_REFERENCE.md) |
| Use the examples / サンプルを使う | [全サンプルガイド](docs/EXAMPLES_GUIDE.ja.md) | [Example catalog](docs/EXAMPLES_GUIDE.md) |
| Resolve normative details / 正式な意味規則を確認する | [正式仕様](docs/SPECIFICATION.ja.md) | [Specification](docs/SPECIFICATION.md) |
| Implement the Studio session view / 構成別クリップを実装する | [Studioガイド](docs/OSTF_STUDIO_IMPLEMENTATION.ja.md) | [Studio guide](docs/OSTF_STUDIO_IMPLEMENTATION.md) |

The reference enumerates **2,341 explicit structural declarations** in the five current Schemas, including conditional branches. This is not a count of independent musical parameters. The sample catalog covers feature themes and maps all 25 earlier Score-example themes; it is not an exhaustive execution test of every legal combination.

リファレンスは現行5 Schemaの**2,341構造宣言**を条件分岐も含めて列挙します。独立した音楽パラメーターが2,341個という意味ではありません。サンプルは機能別に整理し、旧25 Scoreテーマの対応先を示しています。

## File count / ファイル数

| Location / 配置 | Files / 件数 |
|---|---:|
| Repository root / ルート | 10 |
| docs/ | 29 |
| schema/ | 10 |
| examples/ | 36 |
| adopted-4.3/ | 13 |
| tools/ | 2 |
| **Total / 合計** | **100** |

Examples comprise **22 .ostf + 6 .ostfp + 8 companion JSON files**. Each .ostfp is one repository file; its packaged Score/audio/companion members remain inside that file. Directories and the outer distribution ZIP are not counted as repository files. SHA256SUMS lists the other 99 files and excludes itself.

サンプル内訳は**.ostf 22件、.ostfp 6件、関連JSON 8件**です。.ostfp内の音声等はパッケージの内部メンバーです。100ファイルはGitHubに配置する実ファイル数で、フォルダと配布ZIP自身は含めません。

## Current and historical documents / 現行版と継承資料

Use **docs/** and the current exact-version Schemas for 5.1. **adopted-4.3/** preserves original historical bytes; old Draft/approval labels there do not reopen the already approved 5.1 specification. The current manual and reference integrate the inherited material under explicit current precedence. The original 5.0-family Schema files in schema/ are also preserved unchanged.

現在の5.1規定は**docs/**と現行Schemaが入口です。**adopted-4.3/**の旧Draft・承認表記は履歴として原本を維持したもので、5.1の追加承認条件ではありません。旧版と現行版のSchemaを混同しないでください。

## Complete inventory / 全100ファイル


### Repository root / 公開トップ (10)

| No. | File | Purpose / 用途 |
|---:|---|---|
| 1 | [CHANGELOG.md](CHANGELOG.md) | Version history / 変更履歴 |
| 2 | [FILE_INDEX.md](FILE_INDEX.md) | All 100 files and reading order / 全100ファイルの用途・読む順番 |
| 3 | [LICENSE](LICENSE) | CC0 text for specification/data / 規格・自作データのライセンス |
| 4 | [LICENSE-CODE](LICENSE-CODE) | MIT text for reference code / 参考コードのライセンス |
| 5 | [LICENSE-POLICY.md](LICENSE-POLICY.md) | License scope / ライセンス適用範囲 |
| 6 | [NOTICE.md](NOTICE.md) | Edition status and notices / 版の状態と注意書き |
| 7 | [README.ja.md](README.ja.md) | Japanese entry point / 日本語の公開トップページ |
| 8 | [README.md](README.md) | English entry point / 英語の公開トップページ |
| 9 | [RELEASE_NOTES.md](RELEASE_NOTES.md) | Release text for v5.1.0 / 公開時のリリース本文 |
| 10 | [SHA256SUMS.txt](SHA256SUMS.txt) | Digests of the other 99 files / 自身を除く99ファイルのハッシュ |

### Current documentation / 現行ドキュメント (29)

| No. | File | Purpose / 用途 |
|---:|---|---|
| 11 | [docs/COMPLETE_MANUAL.ja.md](docs/COMPLETE_MANUAL.ja.md) | Complete integrated manual / 全網羅マニュアル — 日本語 |
| 12 | [docs/COMPLETE_MANUAL.md](docs/COMPLETE_MANUAL.md) | Complete integrated manual / 全網羅マニュアル — English |
| 13 | [docs/CONFORMANCE.ja.md](docs/CONFORMANCE.ja.md) | Independent capability declarations / 機能別適合宣言 — 日本語 |
| 14 | [docs/CONFORMANCE.md](docs/CONFORMANCE.md) | Independent capability declarations / 機能別適合宣言 — English |
| 15 | [docs/DISTRIBUTED_SESSION_0_4_SPECIFICATION.ja.md](docs/DISTRIBUTED_SESSION_0_4_SPECIFICATION.ja.md) | Distributed Session 0.4 / 分散セッション — 日本語 |
| 16 | [docs/DISTRIBUTED_SESSION_0_4_SPECIFICATION.md](docs/DISTRIBUTED_SESSION_0_4_SPECIFICATION.md) | Distributed Session 0.4 / 分散セッション — English |
| 17 | [docs/EXAMPLES_GUIDE.ja.md](docs/EXAMPLES_GUIDE.ja.md) | All 36 examples and original-theme coverage / 全36例と旧版テーマの対応表 — 日本語 |
| 18 | [docs/EXAMPLES_GUIDE.md](docs/EXAMPLES_GUIDE.md) | All 36 examples and original-theme coverage / 全36例と旧版テーマの対応表 — English |
| 19 | [docs/FORMAT_REGISTRY.ja.md](docs/FORMAT_REGISTRY.ja.md) | Exact version and family matrix / 形式・版の対応表 — 日本語 |
| 20 | [docs/FORMAT_REGISTRY.md](docs/FORMAT_REGISTRY.md) | Exact version and family matrix / 形式・版の対応表 — English |
| 21 | [docs/MIGRATION_MATRIX.ja.md](docs/MIGRATION_MATRIX.ja.md) | Upgrade, downgrade and loss / 移行・旧版出力・情報損失 — 日本語 |
| 22 | [docs/MIGRATION_MATRIX.md](docs/MIGRATION_MATRIX.md) | Upgrade, downgrade and loss / 移行・旧版出力・情報損失 — English |
| 23 | [docs/OSTF_STUDIO_IMPLEMENTATION.ja.md](docs/OSTF_STUDIO_IMPLEMENTATION.ja.md) | Section/Track session UI guidance / 構成別クリップの実装ガイド — 日本語 |
| 24 | [docs/OSTF_STUDIO_IMPLEMENTATION.md](docs/OSTF_STUDIO_IMPLEMENTATION.md) | Section/Track session UI guidance / 構成別クリップの実装ガイド — English |
| 25 | [docs/PACKAGE_SPECIFICATION.ja.md](docs/PACKAGE_SPECIFICATION.ja.md) | OSTFP 1.1 container / プロジェクトZIP・素材の対応 — 日本語 |
| 26 | [docs/PACKAGE_SPECIFICATION.md](docs/PACKAGE_SPECIFICATION.md) | OSTFP 1.1 container / プロジェクトZIP・素材の対応 — English |
| 27 | [docs/PARAMETER_REFERENCE.ja.md](docs/PARAMETER_REFERENCE.ja.md) | Every current Schema declaration and inherited field explanations / 全パラメーター・構造制約と継承項目の説明 — 日本語 |
| 28 | [docs/PARAMETER_REFERENCE.md](docs/PARAMETER_REFERENCE.md) | Every current Schema declaration and inherited field explanations / 全パラメーター・構造制約と継承項目の説明 — English |
| 29 | [docs/PLUGIN_EXCHANGE_PROTOCOL.ja.md](docs/PLUGIN_EXCHANGE_PROTOCOL.ja.md) | Plugin Context 1.1 / 部分読取り・原子的編集提案 — 日本語 |
| 30 | [docs/PLUGIN_EXCHANGE_PROTOCOL.md](docs/PLUGIN_EXCHANGE_PROTOCOL.md) | Plugin Context 1.1 / 部分読取り・原子的編集提案 — English |
| 31 | [docs/PRODUCTION_SESSION_0_4.ja.md](docs/PRODUCTION_SESSION_0_4.ja.md) | Production Session 0.4 / 制作・音声・ミキサー — 日本語 |
| 32 | [docs/PRODUCTION_SESSION_0_4.md](docs/PRODUCTION_SESSION_0_4.md) | Production Session 0.4 / 制作・音声・ミキサー — English |
| 33 | [docs/PROVENANCE.md](docs/PROVENANCE.md) | Exact source archives and retained-original hashes / 出典・原本ハッシュ |
| 34 | [docs/RELEASE_CHECKLIST.md](docs/RELEASE_CHECKLIST.md) | Written release status and scope / リリース状態・確認範囲 |
| 35 | [docs/SECURITY.ja.md](docs/SECURITY.ja.md) | Import and editing boundaries / 取込み・編集の扱い — 日本語 |
| 36 | [docs/SECURITY.md](docs/SECURITY.md) | Import and editing boundaries / 取込み・編集の扱い — English |
| 37 | [docs/SEMANTIC_REQUIREMENTS.md](docs/SEMANTIC_REQUIREMENTS.md) | Cross-reference and time/output requirements / 参照・時間・出力の意味規則索引 |
| 38 | [docs/SPECIFICATION.ja.md](docs/SPECIFICATION.ja.md) | Current normative specification / 5.1の正式規範仕様 — 日本語 |
| 39 | [docs/SPECIFICATION.md](docs/SPECIFICATION.md) | Current normative specification / 5.1の正式規範仕様 — English |

### Current and 5.0 Schemas / 現行・5.0 Schema (10)

| No. | File | Purpose / 用途 |
|---:|---|---|
| 40 | [schema/ostf-5.0.0.schema.json](schema/ostf-5.0.0.schema.json) | Original 5.0-family Schema, unchanged / 5.0系の継承原本 |
| 41 | [schema/ostf-5.1.0.schema.json](schema/ostf-5.1.0.schema.json) | Current complete Schema / 現行の完全Schema |
| 42 | [schema/ostf-distributed-session-0.3.schema.json](schema/ostf-distributed-session-0.3.schema.json) | Original 5.0-family Schema, unchanged / 5.0系の継承原本 |
| 43 | [schema/ostf-distributed-session-0.4.schema.json](schema/ostf-distributed-session-0.4.schema.json) | Current complete Schema / 現行の完全Schema |
| 44 | [schema/ostf-package-manifest-1.0.schema.json](schema/ostf-package-manifest-1.0.schema.json) | Original 5.0-family Schema, unchanged / 5.0系の継承原本 |
| 45 | [schema/ostf-package-manifest-1.1.schema.json](schema/ostf-package-manifest-1.1.schema.json) | Current complete Schema / 現行の完全Schema |
| 46 | [schema/ostf-plugin-context-1.0.schema.json](schema/ostf-plugin-context-1.0.schema.json) | Original 5.0-family Schema, unchanged / 5.0系の継承原本 |
| 47 | [schema/ostf-plugin-context-1.1.schema.json](schema/ostf-plugin-context-1.1.schema.json) | Current complete Schema / 現行の完全Schema |
| 48 | [schema/ostf-production-session-0.3.schema.json](schema/ostf-production-session-0.3.schema.json) | Original 5.0-family Schema, unchanged / 5.0系の継承原本 |
| 49 | [schema/ostf-production-session-0.4.schema.json](schema/ostf-production-session-0.4.schema.json) | Current complete Schema / 現行の完全Schema |

### Samples / サンプル (36)

| No. | File | Purpose / 用途 |
|---:|---|---|
| 50 | [examples/distributed/01-prepared.json](examples/distributed/01-prepared.json) | Prepared snapshot for the AABA Score in 04-combined-production-distributed.ostfp |
| 51 | [examples/distributed/02-phrase-proposed.json](examples/distributed/02-phrase-proposed.json) | Illustrative proposed phrase during open piano chorus; data alone does not change Score Takes |
| 52 | [examples/distributed/03-playing-committed.json](examples/distributed/03-playing-committed.json) | Playing snapshot with committed phrase and finite Plan/source/performance coordinates |
| 53 | [examples/ostfp/01-score-only.ostfp](examples/ostfp/01-score-only.ostfp) | Minimal self-contained 5.1 Score-only archive |
| 54 | [examples/ostfp/02-legacy-4.3-compatible.ostfp](examples/ostfp/02-legacy-4.3-compatible.ostfp) | Manifest 1.1 carrying unchanged legacy 4.3 Score bytes |
| 55 | [examples/ostfp/03-inert-plugin-state.ostfp](examples/ostfp/03-inert-plugin-state.ostfp) | Actual authored post-proposal Score bytes; Production pin; preserved fictional plugin identity/state and source-audio binding |
| 56 | [examples/ostfp/04-combined-production-distributed.ostfp](examples/ostfp/04-combined-production-distributed.ostfp) | AABA Score document/revision pin, Production and Distributed 0.4 together, exact raw-byte SHA and supplied audio bytes |
| 57 | [examples/ostfp/05-audio-linear-comp.ostfp](examples/ostfp/05-audio-linear-comp.ostfp) | Original two Take WAVs; non-destructive source handles; explicit linear region crossfade; inactive hard-cut Comp; no duplicate source playback |
| 58 | [examples/ostfp/06-audio-rendered-comp.ostfp](examples/ostfp/06-audio-rendered-comp.ostfp) | Original source assets plus a new equal-power rendered audioSource; outputMode=rendered; no second application of fades |
| 59 | [examples/plugin/01-context.json](examples/plugin/01-context.json) | Read-only partial take/clip projection pinned to 26-midi-comp |
| 60 | [examples/plugin/02-edit-proposal.json](examples/plugin/02-edit-proposal.json) | Atomic whole-Group and two whole-output replacements using one immutable base snapshot |
| 61 | [examples/plugin/03-applied-with-new-score.json](examples/plugin/03-applied-with-new-score.json) | Illustrative applied acknowledgement whose effective SHA identifies the authored Score inside 03-inert-plugin-state.ostfp |
| 62 | [examples/production/01-production-04.json](examples/production/01-production-04.json) | Production 0.4 audio source and independent mixer authority |
| 63 | [examples/production/02-typed-automation-04.json](examples/production/02-typed-automation-04.json) | Typed Boolean/numeric channel, send, ordinary audio-region and device automation |
| 64 | [examples/score/01-minimal.ostf](examples/score/01-minimal.ostf) | Minimal required Score |
| 65 | [examples/score/02-guitar-solo.ostf](examples/score/02-guitar-solo.ostf) | Guitar performed notes |
| 66 | [examples/score/03-jazz-comping.ostf](examples/score/03-jazz-comping.ostf) | Jazz harmony and ensemble comping |
| 67 | [examples/score/04-aaba-performance-plan.ostf](examples/score/04-aaba-performance-plan.ostf) | Finite AABA form and repeated Visits |
| 68 | [examples/score/06-scat.ostf](examples/score/06-scat.ostf) | Scat and non-lexical vocal intent |
| 69 | [examples/score/07-vocal-alternatives.ostf](examples/score/07-vocal-alternatives.ostf) | Lyric alternatives plus a separate R&B open-vocal part |
| 70 | [examples/score/09-techno-variation.ostf](examples/score/09-techno-variation.ostf) | Techno variation intent |
| 71 | [examples/score/10-physical-robot-requirements.ostf](examples/score/10-physical-robot-requirements.ostf) | Physical performance requirements as inert data |
| 72 | [examples/score/11-harmony-plus-phrasing.ostf](examples/score/11-harmony-plus-phrasing.ostf) | Harmony, key and phrasing |
| 73 | [examples/score/13-fixed-notes-and-directions.ostf](examples/score/13-fixed-notes-and-directions.ostf) | Fixed notes with optional directions |
| 74 | [examples/score/14-tempo-map-reentry.ostf](examples/score/14-tempo-map-reentry.ostf) | Tempo reentry and an explicit sourceRange Visit with a label |
| 75 | [examples/score/15-vocal-response-phrasing.ostf](examples/score/15-vocal-response-phrasing.ostf) | Gospel response, vocal phonemes, curves and fixed-Plan boundaries |
| 76 | [examples/score/16-inherited-comprehensive-core.ostf](examples/score/16-inherited-comprehensive-core.ostf) | Broad inherited Core: MIDI, resources, voices, provenance, clipChoices, localization and generation |
| 77 | [examples/score/17-fixed-note-source-cut.ostf](examples/score/17-fixed-note-source-cut.ostf) | Source cuts, contiguous joins, repeated note occurrences and probability metadata |
| 78 | [examples/score/18-visit-role-override.ostf](examples/score/18-visit-role-override.ostf) | Visit realization and playing-role overrides |
| 79 | [examples/score/20-phrasing-with-motif-reference.ostf](examples/score/20-phrasing-with-motif-reference.ostf) | Motif reference and phrasing |
| 80 | [examples/score/21-visit-and-range-intersection.ostf](examples/score/21-visit-and-range-intersection.ostf) | Both Visit-only and Visit/range intersection response scopes |
| 81 | [examples/score/24-intra-track-voices-response.ostf](examples/score/24-intra-track-voices-response.ostf) | Concurrent voices and intra-track call/response |
| 82 | [examples/score/26-midi-comp.ostf](examples/score/26-midi-comp.ostf) | Partial second Take; bar/chord-aligned Comp; lineage, ratings, note links, finite Visit override, weighted live selection and history |
| 83 | [examples/score/27-silence-and-null.ostf](examples/score/27-silence-and-null.ostf) | All-silence Comp, null active selection, partial silence, retained candidates and historical deleted IDs |
| 84 | [examples/score/28-midi-boundaries.ostf](examples/score/28-midi-boundaries.ostf) | Sub-bar cut; truncate/retrigger/authored outputs; held note clipping, sustain/timbre chase and explicit sustain-off; cycle selection |
| 85 | [examples/score/29-live-selection-policies.ostf](examples/score/29-live-selection-policies.ostf) | Fixed/manual/cycle/random/weighted live selection; explicit zero weight; independent track ownership; stored active fallback |

### Adopted 4.3 originals / 4.3継承原本 (13)

| No. | File | Purpose / 用途 |
|---:|---|---|
| 86 | [adopted-4.3/docs/COMPLETE_MANUAL.md](adopted-4.3/docs/COMPLETE_MANUAL.md) | Adopted 4.3 historical source, unchanged / 採択済み4.3の原本（現行規定はdocsを参照） |
| 87 | [adopted-4.3/docs/PARAMETER_REFERENCE.md](adopted-4.3/docs/PARAMETER_REFERENCE.md) | Adopted 4.3 historical source, unchanged / 採択済み4.3の原本（現行規定はdocsを参照） |
| 88 | [adopted-4.3/docs/PRODUCTION_PARAMETER_REFERENCE.md](adopted-4.3/docs/PRODUCTION_PARAMETER_REFERENCE.md) | Adopted 4.3 historical source, unchanged / 採択済み4.3の原本（現行規定はdocsを参照） |
| 89 | [adopted-4.3/docs/PRODUCTION_SESSION_PROFILE.ja.md](adopted-4.3/docs/PRODUCTION_SESSION_PROFILE.ja.md) | Adopted 4.3 historical source, unchanged / 採択済み4.3の原本（現行規定はdocsを参照） |
| 90 | [adopted-4.3/docs/PRODUCTION_SESSION_PROFILE.md](adopted-4.3/docs/PRODUCTION_SESSION_PROFILE.md) | Adopted 4.3 historical source, unchanged / 採択済み4.3の原本（現行規定はdocsを参照） |
| 91 | [adopted-4.3/docs/SESSION_PARAMETER_REFERENCE.md](adopted-4.3/docs/SESSION_PARAMETER_REFERENCE.md) | Adopted 4.3 historical source, unchanged / 採択済み4.3の原本（現行規定はdocsを参照） |
| 92 | [adopted-4.3/docs/SESSION_PROFILE.ja.md](adopted-4.3/docs/SESSION_PROFILE.ja.md) | Adopted 4.3 historical source, unchanged / 採択済み4.3の原本（現行規定はdocsを参照） |
| 93 | [adopted-4.3/docs/SESSION_PROFILE.md](adopted-4.3/docs/SESSION_PROFILE.md) | Adopted 4.3 historical source, unchanged / 採択済み4.3の原本（現行規定はdocsを参照） |
| 94 | [adopted-4.3/docs/SPECIFICATION.ja.md](adopted-4.3/docs/SPECIFICATION.ja.md) | Adopted 4.3 historical source, unchanged / 採択済み4.3の原本（現行規定はdocsを参照） |
| 95 | [adopted-4.3/docs/SPECIFICATION.md](adopted-4.3/docs/SPECIFICATION.md) | Adopted 4.3 historical source, unchanged / 採択済み4.3の原本（現行規定はdocsを参照） |
| 96 | [adopted-4.3/schema/ostf-4.3.0.schema.json](adopted-4.3/schema/ostf-4.3.0.schema.json) | Adopted 4.3 historical source, unchanged / 採択済み4.3の原本（現行規定はdocsを参照） |
| 97 | [adopted-4.3/schema/ostf-distributed-session-0.2.schema.json](adopted-4.3/schema/ostf-distributed-session-0.2.schema.json) | Adopted 4.3 historical source, unchanged / 採択済み4.3の原本（現行規定はdocsを参照） |
| 98 | [adopted-4.3/schema/ostf-production-session-0.2.schema.json](adopted-4.3/schema/ostf-production-session-0.2.schema.json) | Adopted 4.3 historical source, unchanged / 採択済み4.3の原本（現行規定はdocsを参照） |

### Reference utilities / 参考ツール (2)

| No. | File | Purpose / 用途 |
|---:|---|---|
| 99 | [tools/ostfp.py](tools/ostfp.py) | Optional static package utility / パッケージの参考ユーティリティ |
| 100 | [tools/validate_examples.py](tools/validate_examples.py) | Optional partial static checker / サンプルの参考静的チェッカー |


## Publication / 公開

The ZIP is rootless: extract its contents directly into the intended repository root. README.md is the English entry point and README.ja.md the Japanese entry point. Use RELEASE_NOTES.md for v5.1.0. This package organization does not itself perform a GitHub upload or create a tag.

ZIPを展開した中身をリポジトリのルートに配置できます。公開本文にはRELEASE_NOTES.mdを使えます。動作検証は指定どおり実施していません。今回の整理は文書の導線、全ファイル目録、件数、配布バイトの整合に関する作業です。
