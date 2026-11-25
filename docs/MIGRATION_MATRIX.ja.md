# OSTF 5.1.0 — 移行・互換性・情報損失

| Score | Production | Distributed | Manifest | Plugin Context |
|---|---|---|---|---|
| 4.3.0 | 0.2.0 | 0.2 | 1.0.0 / 1.1.0 | 1.0.0 / 1.1.0 |
| 5.0.0 | 0.3.0 | 0.3 | 1.0.0 / 1.1.0 | 1.0.0 / 1.1.0 |
| 5.1.0 | 0.4.0 | 0.4 | 1.1.0 | 1.1.0 |

## 1. 版を変えずに扱う

5.0を読み込むときは5.0のSchemaと意味規則で扱います。5.1のテイクを追加しない保存では原版の保持が可能です。OSTFPへ収納するだけでScoreを再整形・改版しません。5.1の直接読込みを5.0専用Readerに期待しません。

## 2. 5.0 → 5.1

1. 正確な5.0文書の元バイト、Document ID/Revision、素材と関連Profileを保持します。
2. 新版への保存を明示し、Scoreのversionを5.1.0にします。takeGroupsは不要なら省略可能。構成・コード・MIDI・歌詞・演奏意図は保持します。
3. テイクを導入する場合、元Clip/Regionを候補にし、独立した出力ID・Comp map・採用状態を同じ保存で作成します。候補のenabled/muteのみ変更する操作を「テイク切替」としません。
4. 新しいScoreの実バイトSHAを計算し、Productionを0.4へ明示的に再関連付けします。参照先・時間・Frameの安全整数範囲を確認します。旧Profileのpinを書き換えるだけの操作は行いません。
5. Distributedは旧履歴を保持し、5.1用の新Sessionを別のsessionId、実際の権限・時計・Planで作成します。過去Eventを新Scoreへ書き換えません。
6. Manifest 1.1を、実際の新Score・Profile・AssetバイトとSHA/size/bindingから再構築します。

4.3からは採択版の意味規則を維持して同様に明示移行できます。Production 0.2のAutomationは0.3以降の型・値域制約を満たす必要があります。

## 3. 5.1 → 5.0の採用結果Export

保存されたactiveCompの通常Clip/Audio Regionを残し、Core takeGroupsとProduction audioTakeGroupsを取り除きます。nullは当該範囲の無音を維持します。候補を残す場合は無効/muteのまま、削除する場合は関連するノート・歌詞・素材等の参照を全て修復します。未採用Comp出力の扱いも明示します。

Scoreは5.0.0、Productionは0.3.0へ新規出力し、全pin・manifestを新バイトに合わせます。動的選択、別Comp、評価、出自、選択履歴、visitSelectionsは失われるため元5.1を保存し、損失範囲を報告します。Visitごとの選択も残すには演奏タイムラインへの別の実体化が必要で、単純なversion変更では再現しません。音声レンダーを残す場合も使用素材と明示的なbindingsを維持します。

## 4. 損失の表示

| 入力と操作 | 言えること |
|---|---|
| Scoreだけを受領しScoreを保存 | 受領したScore範囲の保持 |
| Score+Production+音声を受領しScoreだけ出力 | プロジェクトの部分Export |
| URI/SHA記述子のみ受領 | 記述子の保持。音声実体の保持とは別 |
| 音声/Plugin Stateバイトあり、実装なし | 元バイトの保持。音色再現は未確認 |
| take mapを理解しないWriter | 元構造・候補・出力を保持、または無損失保存を拒否 |
| 不整合・古いpin | 対象IDと原因を報告。推測で更新しない |

Loss Reportには操作、実際に受け取った文書/実体、出力版、対象ID/Pointer、omitted/approximated/unavailable/unsupported/unresolved/stale_binding、保存結果を示します。これは推奨語彙であり、新規の必須ファイル形式ではありません。
