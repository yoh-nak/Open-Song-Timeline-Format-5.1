# OSTF 5.1.0 — Take & Comp

**Release date: 2026-11-25 · Tag: v5.1.0 · Official written specification**

## Highlights

This complete release adds non-destructive Take/Comp interchange to OSTF while retaining the musical Core and optional project families of 5.0. Candidates remain stored and disabled/muted. Comp maps choose arbitrary source-score Tick intervals; independent ordinary Clip/Audio Region outputs carry the selected result.

New capabilities include partial Takes, multiple Comps, explicit silence, MIDI boundary handling, Audio region/rendered output and explicit transitions, finite Visit choices, free-session launch policies, provenance/rating/lineage/history and scoped Plugin take-edit proposals. A Section-by-Track Studio grid is supported as an application view without constraining other hosts.

## Versions

| Family | Current version | Previous version |
|---|---|---|
| OSTF Core / Score | **5.1.0** | 5.0.0 |
| Production Session | **0.4.0** | 0.3.0 |
| Distributed Session | **0.4** | 0.3 |
| OSTFP Manifest | **1.1.0** | 1.0.0 |
| Plugin Context | **1.1.0** | 1.0.0 |

## Completed integration

- Full 5.0 inheritance plus complete current Schemas, not a delta requiring an external merge.
- Five unchanged 5.0-family Schemas and thirteen unchanged adopted 4.3 source files retained.
- English/Japanese specification, manual, reference and family documents.
- 2,341 explicit current Schema declarations, 36 sample files and source-theme coverage mapping.
- 100 repository files, license/provenance records and SHA256SUMS.

## Clarifications since the preliminary 5.1 delta

- A finite Visit or live launch uses a playback selection overlay; it does not rewrite saved activeComp or activate source candidates.
- Production Audio retains its inherited independence from Core part realized:silent/open.
- MIDI Comp boundary processing is separate from subsequent Visit hard-cut rules.
- Audio crop phase, source envelope preservation and transition handles are explicit. Nonlinear or unrepresentable output uses a pre-channel rendered asset.
- Plugin1.1 permits takeGroups descendants only with Score5.1. The host initializes a missing array and reissues context; group/output edits are atomic.
- Schemas enforce empty/all-silence Comp conditions, weighted-selection constraints, exact companion-version matrices and appropriate safe-integer time bounds.

## Migration

5.1 does not require takeGroups for ordinary scores. Original 5.0 documents retain their version and may be explicitly migrated. Downgrade to 5.0 preserves the saved active ordinary outputs but loses Comp maps and selection metadata; it is an explicit projection with loss disclosure, not automatic legacy reader compatibility.

## Release policy and verification scope

All specification decisions for this edition are approved. Runtime validation is not a release prerequisite and was not performed. Document, Schema and package-content consistency work is distinct from DAW/audio/plugin/network testing. Included reference utilities were updated but not executed. This release does not certify a software implementation.

The archive is ready for publisher upload and tag creation. No GitHub upload, remote commit or tag was performed by preparing it.

---

## 日本語

OSTF 5.1.0の正式仕様パッケージです。5.0本体との統合を完了し、テイク・コンピング・MIDI/Audio境界・ライブ選択・Plugin連携・移行ルールを確定しました。構成単位のStudioクリップ設計を維持しながら、規格上は任意Tick範囲で採用区間を表現します。

日英の全仕様、全網羅マニュアル、全項目リファレンス、36サンプル、5.0/4.3の継承原本、ライセンスとハッシュを100ファイルにまとめています。仕様策定は承認済み、動作検証は不要という指定に基づき、**仕様として正式リリース可能**です。DAW・音声・Plugin・ネットワークの動作検証は実施しておらず、GitHubへの実公開もこのZIPの作成とは別です。
