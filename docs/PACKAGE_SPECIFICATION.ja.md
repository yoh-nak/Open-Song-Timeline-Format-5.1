# OSTF Project Package 1.1 — OSTF 5.1用正式規範仕様（5.1.0）

## 1. 目的とファイル表現

OSTF TEXT（`.ostf`）は従来どおり独立したUTF-8 JSONの楽曲Scoreです。OSTF PROJECT（`.ostfp`）は、正本Scoreを**必ず1件**、制作／分散Session JSONや実体Assetを任意で同梱する**ZIP輸送形式**です。Scoreと制作情報の正本を混合しません。Project Directoryは同じ論理構造を持つ**展開・編集中のフォルダ表現**であり、第3の交換用拡張子ではありません。単なるPack/Unpackで元のScore等のバイト列を書き換えてはいけません。

## 2. ZIP構造と識別子

1. ZIP最初のメンバーは`mimetype`、圧縮方式`Stored`、内容はASCIIの`application/vnd.ostf-project+zip`**完全一致**（BOM・改行・空白なし）を必須とします。このメディアタイプは**提案上の未登録値**であり、IANA登録済みとは表記しません。
2. 2番目は暗号化されていないUTF-8 JSONの`manifest.json`です。構造は`schema/ostf-package-manifest-1.1.schema.json`に従います。
3. 残りはManifestで宣言したScore1件、任意のJSONとBinaryです。ZIPの`Stored`/`Deflate`およびZIP64を認めます。空ディレクトリエントリを必須とはせず、実体素材には数えません。暗号化されたZIPや実行可能ファイルのインストールを規格化しません。
4. 各パスはNFC正規化済みPOSIX相対パスです。絶対／ドライブパス、バックスラッシュ、`.`/`..`、制御文字、ルート脱出、予約名との衝突を禁止します。大文字小文字同一視による衝突も拒否します。Symlinkなどを使った展開先の迂回は拒否します。

受信アプリはZIPを信頼できない入力として扱い、重複名、Zip Slip、圧縮爆弾、巨大展開、パス衝突、Symlink経由の脱出や不完全保存を防ぎます。同梱`tools/ostfp.py`は独自上限を持つ参考試作であり、セキュリティ認証済み実装や共通上限値ではありません。

## 3. Manifestと原本SHA

必須キーは`packageFormat:"OSTFP"`、`packageVersion:"1.1.0"`、`projectId`、`title`、`score`、`documents[]`、`assets[]`、`bindings[]`です。

- `score`：`path`, `format:"OSTF"`, `version:"4.3.0"|"5.0.0"|"5.1.0"`, `sha256`。正本は必ず1件です。
- `documents[]`：`id/role/path/family/version/sha256`、任意`required`。各JSONは独立した正確な版で識別します。
- `assets[]`：`id/path/purpose/sha256/mediaType/sizeBytes`、任意の権利表示。`sizeBytes`は実体のバイト数です。
- `externalAssets[]`、`metadata`、`extensions`：任意・非権威の補助データです。

ハッシュはZIP圧縮後のバイトや整形JSONではなく、**各ファイルの非圧縮・元バイトSHA-256**です。Manifest自身は自己ハッシュしません。`mimetype`と`manifest.json`以外の全実体をScore、documents、assetsのいずれか**ちょうど一つ**に記載します。未記載・二重宣言・実体欠損は不正です。補助JSONを第2の正本Scoreにしてはいけません。

## 4. ScoreとProfileの組合せ

| Score | Production | Distributed | Manifest内のfamily/version |
|---|---|---|---|
| OSTF 4.3.0 | Production 0.2.0（任意） | Distributed 0.2（任意） | Production `OSTF-Production-Session` / `0.2.0`、Distributed `OSTF-Distributed-Session-0.2` / `0.2` |
| OSTF 5.0.0 | Production 0.3.0（任意） | Distributed 0.3（任意） | Production `OSTF-Production-Session` / `0.3.0`、Distributed `OSTF-Distributed-Session-0.3` / `0.3` |
| OSTF 5.1.0 | Production 0.4.0 | Distributed 0.4 | `OSTF-Production-Session` / `0.4.0`; `OSTF-Distributed-Session-0.4` / `0.4` |

Productionの本文は`profile`、`profileVersion`、`score.formatVersion`、`score.sha256`を実際のScoreと一致させます。任意の`score.documentId/revisionId`もScoreのDocument識別子と一致させます。Distributedの本文では`profile`、`recordType:"snapshot"|"event"`と、正しいScore/Plan参照を確認します。**Distributed 0.3/0.4にはネストした`score`オブジェクトも`profileVersion`も存在せず、ルートの`scoreSha256`、`documentId`、`revisionId`、`performancePlanId`を照合します。** これらは正本の実バイトSHA、Document、Revision、有限のPerformance Planに対応します。旧Distributed 0.2も採択された旧規範に従って照合します。旧SessionのVersionだけ置き換えて再利用してはいけません。

`documents[].role:"supplement"|"metadata"`はCore／Profileの正本権限を生みません。Plugin Contextメッセージを補助資料として保存しても編集実行権限にはなりません。

## 5. AssetのBinding

`bindings[]`は`(documentPath,resourceKind,resourceId)`から同梱された1件の`assets[].id`への対応です。`coreResource`は**正本Score**の`resources[].id`、`productionAsset`は**指定Production文書**の`assets[].id`（Plugin Stateを含む）に解決します。パスは参照文書の場所ではなく**Project Root基準**です。曖昧な重複Binding、存在しないID、実体SHAの矛盾、用途／MIMEの不一致を拒否します。**同梱のために元JSONのURIやScoreを変更しません。** Bindingの正本は本節です。

`externalAssets[]`は非同梱参照であり、HTTPSの自動取得・ファイル読取権限を与えません。参照があっても音声素材、プラグイン本体、ライセンス、実音再現が確保されたとは主張できません。

## 6. Project Directory・保存・部分Export

Project Directoryは`mimetype`と`manifest.json`、Manifestで宣言した実体を、`.ostfp`と同じルート相対パスで保持します。Pack/Unpackは元のScore/Profile/Assetバイトを保持します。ZIPメタデータ・圧縮結果のSHAまで同一にする必要はありません。保存では一時領域で全実体とManifestを構築して一貫した世代を公開することを推奨しますが、複数ファイルのOSレベル原子的保存は保証しません。Scoreを変更したら別ProfileのSHAを暗黙更新せず、明示的な再関連付け／新Sessionが必要です。Scoreだけの`.ostfp`は合法ですが、制作情報・音声実体を受領したのに省略した場合は「プロジェクト全体が無損失」と表現せずLossを報告します。`MIGRATION_MATRIX.ja.md`を参照してください。

## 7. 保証しない事項

構造Schema合格、参照意味の成立、元バイトの一致、ZIPの安全処理、DAW・プラグイン実機互換性は別の機能です。`.ostfp`は実行ファイル／音源インストーラー、認証済み遠隔Session、著作権許諾、音響レンダリング保証ではありません。実装は`CONFORMANCE.ja.md`で機能別の対応範囲を宣言します。

## テイク素材の保持

Manifest 1.1は4.3/5.0/5.1をそれぞれ正確な版のまま収納します。旧Manifest 1.0は5.1を受理しません。Production 0.4はネストした`score.sha256`と任意の`score.documentId/revisionId`、Distributed 0.4はルートの`scoreSha256`・`documentId`・`revisionId`・`performancePlanId`を使用します。無損失のOSTFP出力では未採用テイクの音声実体と、各Compの実体化済み出力も保持します。Comp対応を理由に素材を勝手に間引きません。採用結果のみのExportは明示的な部分Exportです。
