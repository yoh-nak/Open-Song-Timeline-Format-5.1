# Open Song Timeline Format (OSTF) 5.1.0 — Take & Comp

**正式な書面仕様リリース／2026年11月25日／リリースタグ `v5.1.0`**

OSTF 5.0の全規定を継承し、テイク・コンピング・採用済み出力・ライブ／Visit選択を統合した完全版です。5.0の別途ダウンロードやSchema差分の合成作業は必要ありません。

## GitHub公開用の構成

マニュアル、全パラメーターリファレンス、サンプル、Schema、ライセンス、参考ツールを含めて**全100ファイル**です。[FILE_INDEX.md（全ファイル目録）](FILE_INDEX.md)に用途と読む順番をまとめています。ZIPには余分な親フォルダを設けていないため、展開した中身をリポジトリのルートへ配置できます。

読む入口は[全網羅マニュアル](docs/COMPLETE_MANUAL.ja.md)、項目を調べる入口は[全パラメーターリファレンス](docs/PARAMETER_REFERENCE.ja.md)、具体例の入口は[全サンプルガイド](docs/EXAMPLES_GUIDE.ja.md)です。旧版の継承資料は目録で区別しています。`v5.1.0`のリリース本文には[RELEASE_NOTES.md](RELEASE_NOTES.md)を使えます。


## 5.1の基本設計

すべてのテイク候補を元のタイムライン上に保持し、どの区間を採用するかをCompとして別に記録します。元候補を破壊せず、通常再生用のClip／Audio Regionを独立したIDで作成して保存します。

- 規格上の単位は任意のsource-global Tick範囲。構成・小節・コード・フレーズを共通の仕組みで扱います。
- MIDIとAudioの複数Take、部分Take、複数Comp、明示的な無音、null選択を定義します。
- MIDIの境界処理・サステイン・CC・歌詞／音素参照と、Audioの切出し・クロスフェード・事前レンダーを規定します。
- 保存された採用Compと、ライブ起動や有限Visitごとの選択を分離します。候補素材を二重に再生しません。
- fixed/manual/cycle/random/weightedの選択と、出自・評価・派生・履歴を保持できます。
- Plugin Context 1.1では、Score 5.1のtakeGroupsと関連出力を一括編集する提案を扱えます。
- 5.0への書き出しは保存済み採用結果を維持し、失われるテイク情報を報告します。

**OSTF Studioの構成×トラックのクリップ表示は維持できます。** レーン、色、起動UIなどは各アプリが自由に実装でき、規格は特定DAWの画面構成を要求しません。

## ファイル形式

`.ostf`（OSTF TEXT）はBOMなしUTF-8 JSONの独立した楽曲Scoreです。`.ostfp`（OSTF PROJECT）は1つのScoreと任意の制作・分散JSON、音声・状態素材をまとめるZIPです。制作・分散・Plugin対応は任意であり、Coreだけのツールも実装できます。

## ドキュメント

| Document | English | 日本語 |
|---|---|---|
| Integrated specification | [Specification](docs/SPECIFICATION.md) | [正式仕様](docs/SPECIFICATION.ja.md) |
| Complete manual | [Manual](docs/COMPLETE_MANUAL.md) | [全網羅マニュアル](docs/COMPLETE_MANUAL.ja.md) |
| All fields and constraints | [Reference](docs/PARAMETER_REFERENCE.md) | [全網羅リファレンス](docs/PARAMETER_REFERENCE.ja.md) |
| All example files | [Catalog](docs/EXAMPLES_GUIDE.md) | [サンプル一覧](docs/EXAMPLES_GUIDE.ja.md) |
| OSTF Studio session view | [Implementation guide](docs/OSTF_STUDIO_IMPLEMENTATION.md) | [Studio実装ガイド](docs/OSTF_STUDIO_IMPLEMENTATION.ja.md) |
| Production / audio | [Production0.4](docs/PRODUCTION_SESSION_0_4.md) | [制作0.4](docs/PRODUCTION_SESSION_0_4.ja.md) |
| Distributed / AI | [Distributed0.4](docs/DISTRIBUTED_SESSION_0_4_SPECIFICATION.md) | [分散0.4](docs/DISTRIBUTED_SESSION_0_4_SPECIFICATION.ja.md) |
| Project container | [Package1.1](docs/PACKAGE_SPECIFICATION.md) | [パッケージ1.1](docs/PACKAGE_SPECIFICATION.ja.md) |
| Plugin / host editing | [Plugin1.1](docs/PLUGIN_EXCHANGE_PROTOCOL.md) | [プラグイン1.1](docs/PLUGIN_EXCHANGE_PROTOCOL.ja.md) |
| Migration and loss | [Migration](docs/MIGRATION_MATRIX.md) | [移行・情報損失](docs/MIGRATION_MATRIX.ja.md) |
| Feature declarations | [Conformance](docs/CONFORMANCE.md) | [機能別適合](docs/CONFORMANCE.ja.md) |
| Import boundaries | [Security](docs/SECURITY.md) | [取込み規則](docs/SECURITY.ja.md) |
| Exact formats and versions | [Format registry](docs/FORMAT_REGISTRY.md) | [形式・版の対応表](docs/FORMAT_REGISTRY.ja.md) |
| Cross-object requirements | [Semantic requirements](docs/SEMANTIC_REQUIREMENTS.md) | [意味規則索引](docs/SEMANTIC_REQUIREMENTS.md) |

## バージョン

| Family | Current version | Previous version |
|---|---|---|
| OSTF Core / Score | **5.1.0** | 5.0.0 |
| Production Session | **0.4.0** | 0.3.0 |
| Distributed Session | **0.4** | 0.3 |
| OSTFP Manifest | **1.1.0** | 1.0.0 |
| Plugin Context | **1.1.0** | 1.0.0 |

5.0専用Readerが5.1をそのまま読めるという意味ではありません。旧形式向けには明示的にExportします。5.0の5 Schemaと4.3の採択資料13ファイルを原本のまま同梱しています。

## 収録内容

- 現行Schema 5本、5.0互換用Schema 5本、4.3のSchema 3本。
- 日英の全網羅マニュアル・リファレンス。現行5 Schemaの**2,341構造宣言**を全件列挙。
- **36サンプル**：`.ostf` 22件、`.ostfp` 6件、Production 2件、Distributed 3件、Plugin 3件。
- 元5.0の25 Scoreテーマの収録先・保持方式・変更点をサンプルガイドに記載。
- オーディオ例には独自に作成した短いPCM素材と元テイク・採用出力を同梱。
- ライセンス、出典、リリースノート、全ファイルのSHA一覧。
- **配布物は100ファイル**。各`.ostfp`は内部の素材を含む1つのリポジトリファイルとして数えます。

## 参考ツールと確認範囲

```sh
python -m pip install jsonschema
python tools/validate_examples.py
python tools/ostfp.py validate examples/ostfp/05-audio-linear-comp.ostfp
```

参考ツールは開発者向けに同梱しており、今回のリリースでは実行していません。部分的な静的確認用であり、Compの全意味規則やDAW動作を証明しません。パッケージ作成時には文書・Schema・目録等の静的整合を確認しましたが、**DAW・音声再生・Plugin実行・独立実装・ネットワークの動作検証は行っていません。**

## リリース状態

**仕様として正式リリース可能です。** 策定上の判断は承認済み、動作検証はリリース条件外です。[リリース状態](docs/RELEASE_CHECKLIST.md)を参照してください。この成果物の作成はGitHubへのアップロードやタグ作成を意味しません。

規格文章・Schema・自作サンプルは[CC0](LICENSE)、参考コードは[MIT](LICENSE-CODE)です。[ライセンス範囲](LICENSE-POLICY.md)、[NOTICE](NOTICE.md)、[出典](docs/PROVENANCE.md)を参照してください。
