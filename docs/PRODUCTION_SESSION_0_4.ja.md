# OSTF 5 Production Session 0.4 — 相互運用意味規則（5.1.0）

> **0.4の継承関係：** 5.0のProduction 0.3の全規則を継承し、Score 5.1への固定、任意の`audioTakeGroups`、安全整数の時間・Frame制約を追加します。元の0.3 Schemaは別ファイルのまま保持します。音声コンピングの規定は本書末尾および`SPECIFICATION.ja.md`が優先します。

**Production 0.4はバイト照合済の採択4.3 Production 0.2を継承する5.1用規範です。正式な継承原文は `adopted-4.3/docs/PRODUCTION_SESSION_PROFILE.ja.md` に収録しています。** 構造の正本は`schema/ostf-production-session-0.4.schema.json`、宣言可能なProfileは`profile:"OSTF-Production-Session"`、`profileVersion:"0.4.0"`です。`score.formatVersion`は`5.1.0`固定。各実装はCore Score原文のUTF-8バイト列のSHA-256を照合する必要があります。未知のScore版、旧Profileとの不一致を自動変換してはなりません。

## 1. チャンネル・音源・接続の参照

* `channels[].id`、`devices[].id`、`assets[].id`、`audioRegions[].id`、`automation[].id`、全チャンネルを横断した`channels[].sends[].id`、`sidechainConnections[].id`はそれぞれの名前空間で一意。IDは表示名で代用しません。
* `master` Channelはちょうど1件。`track` Channelだけが実在Core Trackに対応し`trackId`を持つ。`audioTrack`はCore Trackを増やさず、`bus/master`はTrack参照を持ちません。Core Trackが複数Channelから参照される場合、意図的な重複出力として誤って扱わず、実装が必要な多重マッピング規則を提供しない限り拒否します。
* それぞれの`deviceIds[]`は同一Profileに存在するDeviceを処理順に列挙します。1 Deviceを2 Channelで所有させない。`instrument`はCore Track Channelの最初のSlotに最大1個、Bus/MasterはInstrumentを含まない。未知のPlugin識別子・状態は参照として保持します。
* 非Master Channelの`outputChannelId`は他Channelに解決しなければなりません。`send.targetChannelId`はBusに、`sidechain.targetDeviceId`は別Channelに属するEffectに解決しなければなりません。`sourceChannelId`はMasterにできません。Sidechain `(targetDeviceId,targetPortId)`は同じProfileで二重に定義しない。
* Output、Send、Sidechainで作られたChannel依存の有向グラフは循環禁止。Source→Destinationを辺とし、SidechainではTarget Deviceの所有ChannelをDestinationとします。存在しない参照や循環を無音で補正せず、明確に拒否・診断します。

## 2. 素材・Audio Regionの一致

* `stateAssetId`は`purpose:"pluginState"`のAssetだけを参照する。`audioRegions[].sourceAssetId`は`purpose:"audioSource"`のAssetだけを参照する。用途違いは拒否します。URIは自動ダウンロードやインストール権限ではありません。
* `sourceStartFrame >= 0`、`sourceFrameCount > 0`、`sourceStartFrame + sourceFrameCount <= asset.frameCount`。`fadeInTicks + fadeOutTicks <= durationTicks`。`startTick`はScore元のグローバルTickです。
* `native`は指定された音声Frameを元のTempo Mapの実時間で再生し、勝手にループ・伸縮しない。`fit`はRegion時間と指定Frame区間の等比例関係を意図し、音高の扱いを`pitchPolicy:preserve|followRate`に明示する。アルゴリズムの違いは音響一致を保証しません。
* 音声Regionは`track`または`audioTrack` Channelに置く。Bus/Master上のAudio Regionは不正。重なりは加算であり、自動Crossfade、正規化、補完サンプルの挿入を行わない。

## 3. Automationの正本・値域・競合

* 全`automation[].points`は非負の**元Score Tick**の厳密昇順で、同Tick重複禁止。複数Visitが同じ元区間を通る場合、元座標の自動化をそれぞれ再適用します。
* 同じ`(target.kind,参照ID,parameter/parameterId)`へ複数Laneを宣言しない。サポートされないLaneを他のパラメータへ暗黙変換しません。
* Boolean対象は`channel.mute`、`send.enabled`、`audioRegion.mute`、`deviceControl.enabled/bypass`のみ。`valueType:boolean`と`interpolation:step`を必須にし、`points[].value`はBooleanです。**Boolean Pointは`atTick`と`value`の両方が必須です。**
* `channel.gainDb/send.gainDb/audioRegion.gainDb`は数値dB、`channel.pan`は-1..1、`device.parameterId`は原則0..1の正規化数値。`deviceControl`は内部VSTパラメータではありません。値域外や異なる型を暗黙に丸めず、診断します。
* 同じ時刻の異種Laneの効果とMIDI CC間の処理順は明示された責務だけに限る。MIDI CC7/10/11/91/93をMixer Gain/Pan/Sendと同じ正本として合成・上書きしません。
* 初回Point前はChannel/Device静的値、最終Point後は最後のPoint値を保持。`step`は直前値、`linear`は対象の数値領域で線形補間します。1つの対象について異なるLaneが競合したら曖昧なlast-writer-winsを採用しません。

## 4. 情報損失と受け渡し

* Score編集で元バイトSHAが変わった場合、Productionの旧`score.sha256`をそのまま引用しません。ユーザーが明示的にProductionを新Scoreへ再関連付けするか、旧Profileを歴史資料として保持します。Plugin Contextの`ack`だけで制作環境のSHAを更新しません。
* `.ostfp`内に素材が存在しても、Pluginプログラム・License・Voicebankが利用可能だと保証しません。未対応Hostは識別子・順序・State記述子と実際に受領したBytesを可能な限り保持するか、損失範囲を示して破壊的保存を拒否します。
* 本規格はDAW/プラグインの演奏・DSPアルゴリズム、複雑なWarp、Surround、並列Rack、物理I/Oの同一性を標準化しません。

**公開版の規範範囲**：上記はProduction 0.4の正式な意味規則です。参照整合、音楽時間、循環禁止等はJSON Schema単独で検証できないため、実装が別途評価します。実装・DSP・DAWでの可聴互換性はこの文書の保証対象ではありません。

## Automation Target の型と値域（規範）

Production Session 0.4は、0.3で導入済みの数値AutomationにBooleanを許さない型・値域制約を継承します。既存5.0・4.3のSchemaは変更しません。

| `target.kind` | `parameter` | `valueType` | `points[].value` | 補足 |
|---|---|---|---|---|
| `channel` | `gainDb` | `number` | -120～+24 dB | チャンネルの音声Gain。MIDI CC7と独立 |
| `channel` | `pan` | `number` | -1～+1 | 音声Pan。MIDI CC10と独立 |
| `channel` | `mute` | `boolean` | `true` / `false` | `interpolation:step`のみ |
| `send` | `gainDb` | `number` | -120～+24 dB | 対象Sendの音声Gain |
| `send` | `enabled` | `boolean` | `true` / `false` | `interpolation:step`のみ |
| `audioRegion` | `gainDb` | `number` | -120～+24 dB | Region段階の音声Gain |
| `audioRegion` | `mute` | `boolean` | `true` / `false` | `interpolation:step`のみ |
| `deviceControl` | `enabled`、`bypass` | `boolean` | `true` / `false` | Plugin内部Parameterではない |
| `device` | `parameterId` | `number` | 0～1 | 正規化された不透明Parameter値、実パラメータの尺度はホスト依存 |

**必須意味規則：** 各Laneは`points[]`を1件以上持ち、`atTick`を元ScoreのGlobal Tickで**厳密昇順・重複なし**に並べる。Scopeは元ScoreのTickであり、Performance PlanのVisitが再訪する場合も元位置のAutomationを再適用する。複数の同じ`target.kind`+ID+Parameterがある場合、配列後勝ちにせず不正とする。数値には`step`と`linear`を許し、Booleanには`step`のみ。最初のPoint以前は各静的Channel/Send/Device/Region値、最後のPoint以降は最後のPoint値とする。未存在ID、未対応Parameter、型・値域外を黙って補正せず、保存拒否またはLoss報告を行う。

**構造上の保証範囲：** 0.4 Schemaではターゲットごとの型・値域まで確認できる。ただし参照先IDの存在・重複Lane・時刻の昇順・音声グラフの循環禁止をJSON Schema 2020-12の単一文書構造ルールのみで完結させたとは主張しない。実機の音質・再生・プラグイン相互運用は動作検証は実施していません。

**サンプル：** `EXAMPLES_GUIDE.ja.md` のProduction例を参照してください。数値対象にBooleanを与える値は不正です。


### 正式4.3原本継承の注意

正式採択4.3 Production0.2 Schemaの14 `$defs`全てを再採用した。`channel.name`、`plugin.name`（必須）、`plugin.namespace`、`asset.purpose=renderedAudio`、`asset.byteLength`、`hostExtension.namespace`のパターン等は正式0.2の原義のまま保持する。以前の未公開案にあった`assets[].sizeBytes`という便宜項目は**ProductionではなくPackage Manifest内のsizeBytes**としてのみ使用する。0.3で導入されたAutomation型制約を継承し、0.4ではScore 5.1へのpinとaudioTakeGroupsを追加。詳細は`PROVENANCE.md`参照。


## Audio Take / Comp — 0.4

`audioTakeGroups[]` は同一track/audioTrackチャンネルの元Score Tick範囲を管理します。候補Audio Regionは常に`mute:true`。Compは完全な区間分割と、独立した`outputAudioRegionIds`を持ち、保存時はactiveCompだけを非muteにします。管理対象RegionへのRegion単位Automationは禁止し、チャンネルAutomationを使用します。複数グループは同一チャンネル内で重複できません。

`regions`出力は元素材の位相・gain・fadeを保持します。native切出しは元のTempo Map全区間からフレーム位置を求め、fitは元Regionの比率を維持します。線形クロスフェードは宣言した遷移窓と実体化したRegion/fadeに対応させます。非線形遷移、複合fade等をRegionで正確に表せない場合は`rendered`出力を用い、別audioSourceを同梱します。DSP同一性は規定しません。チャンネル処理はレンダー後に一度だけ適用します。

Visit選択は保存中のactiveCompを変更しない再生時選択です。選択Compの出力に付いた選択用muteだけを上書きし、候補素材は鳴らしません。チャンネルmute等は維持します。従来どおりProduction AudioはCoreの`realized:silent/open`と独立し、Core partのsilentはAudioを暗黙に停止しません。同期停止が必要ならProductionチャンネルの明示的なmute等を使います。Visitによる範囲切断はCompの実体化後に適用します。

全ての参照、区間、選択と出力の整合を一回の制作編集として保存します。全体のテイク規則、クロスフェード条件、移行は`SPECIFICATION.ja.md`を参照してください。
