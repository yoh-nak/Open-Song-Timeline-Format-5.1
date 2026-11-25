# Open Song Timeline Format 5.1.0 — 正式仕様

**リリース：v5.1.0 · 2026年11月25日 · Take & Comp**

本書はOSTF 5.1.0の統合済み書面仕様である。正式版5.0の楽曲・プロジェクトモデルを継承し、任意の非破壊MIDI／Audio Take Group、Comp採用写像、保存済み出力、有限Visitごとの選択、ライブ起動時の選択方針を追加する。英語版は`SPECIFICATION.md`であり、両言語版は同じ現行要件を規定する。「必須」「禁止」「推奨」「任意」はそれぞれMUST、MUST NOT、SHOULD、MAYを意味する。

## 1. 提供形式・対象範囲・規範の優先順位

ファイル形式は引き続き**OSTF TEXT**（`.ostf`、BOMなしUTF-8のJSON Score）と**OSTF PROJECT**（`.ostfp`、ZIPコンテナー）の2種類とする。Production SessionとDistributed Sessionは独立した版を持つ任意のJSON文書ファミリーである。Plugin Context ExchangeはHostとPlugin間の論理メッセージ契約であり、第三の必須拡張子やリアルタイムプラグインAPIを新設しない。

策定者が正式採択した4.3.0の楽曲文法、5.0のファミリー別意味規則、明示的に変更していない必須項目を継承する。Score 5.1は正確な版識別子を変更して任意の`takeGroups`を追加し、Production 0.4は任意の`audioTakeGroups`とScore 5.1への結合を追加する。テイクを使わない文書に、これらのフィールドを要求しない。型、必須性、構造分岐、列挙値、数値境界は版別Schemaが規定し、参照・時間・所有者・動作上の意味条件は本書と現行ファミリー別仕様が規定する。現行の明示的な変更は、名指ししたファミリー・版・事項に限って継承規則に優先する。例題は規範を変更しない。

採択済み4.3の原本は`../adopted-4.3/`に元のバイト列のまま保持する。これらの履歴資料に残るDraft表記、過去の承認条件、旧ナビゲーションは出典履歴であり、5.1のリリース状態や条件ではない。全網羅マニュアルとパラメーターリファレンスは継承項目と現行追加項目を扱う。未知の意味を推測せず、未対応データはlossless保存で保持するか保存を拒否する。文書内の参照だけで外部データの取得・実行は許可されない。

### 現行文書の正確な識別値

| ファミリー | 正確な識別 | 構造の正本 | 現行の意味規則 |
|---|---|---|---|
| Score | `format:"OSTF"`、`version:"5.1.0"` | [Core Schema](../schema/ostf-5.1.0.schema.json) | 本書、[全網羅マニュアル](COMPLETE_MANUAL.ja.md)、採択済み4.3 Score規則 |
| Production | `profile:"OSTF-Production-Session"`、`profileVersion:"0.4.0"`、`score.formatVersion:"5.1.0"` | [Production Schema](../schema/ostf-production-session-0.4.schema.json) | [Production Session 0.4](PRODUCTION_SESSION_0_4.ja.md)、採択済みProduction 0.2と継承した5.0増補 |
| Distributed | `profile:"OSTF-Distributed-Session-0.4"`、`recordType:"snapshot"`または`"event"` | [Distributed Schema](../schema/ostf-distributed-session-0.4.schema.json) | [Distributed Session 0.4](DISTRIBUTED_SESSION_0_4_SPECIFICATION.ja.md) |
| Project manifest | `packageFormat:"OSTFP"`、`packageVersion:"1.1.0"` | [Manifest Schema](../schema/ostf-package-manifest-1.1.schema.json) | [Package仕様](PACKAGE_SPECIFICATION.ja.md) |
| Plugin Context | `protocol:"OSTF-Plugin-Context"`、`protocolVersion:"1.1.0"` | [Plugin Schema](../schema/ostf-plugin-context-1.1.schema.json) | [Plugin交換プロトコル](PLUGIN_EXCHANGE_PROTOCOL.ja.md) |

旧Scoreと関連文書は、それぞれの正確な元バージョンで有効である。5.1対応を理由に4.3や5.0文書の版を付け替えない。5.0対応も5.1識別子の受理を意味しない。

## 2. 継承する正本と不変原則

1. ScoreのSHA-256は、再シリアライズや正規化したJSONではなく、**元のUTF-8バイト列そのもの**から計算する。空白だけの変更でも旧ハッシュは失効する。パッケージ作成時にScore、Production／Distributed文書、Assetの内容バイトを書き換えてはならない。結合は既存のパッケージルート基準パスと正確な識別情報に従う。
2. CoreのHarmony、Lyrics、Notes、Directions、Voice、Resource、音楽的意図は既存の権威を保つ。構成名、レーン順、色は識別や再生内容を決めない。
3. CoreのMIDI CCによるVolume／Expression／Effect制御と、ProductionミキサーのGain／Pan／Sendは別の正本である。Productionの非循環チャンネル・Send・Sidechainグラフ、型付きAutomation、非実行のプラグイン状態モデルを維持する。JSONだけでプラグインを起動したり音響的同一性を保証したりしない。
4. 有限Performance Planは明示的に選択する素材の投影である。元のNoteを書き換えず、第二の正本タイムラインを作らない。既存のfixed／open／silent、役割上書き、連続するsource接続、ハードカット、sourceテンポの規則を維持する。
5. Distributed Sessionは協調状態と演奏句の提案・確定を自身の領域に記録する。`phraseCommitted`だけでScore、Take選択、録音素材は変わらず、実際に音が出た証明にもならない。ルート`scoreSha256`が元のScoreバイト列を固定する。
6. Plugin Contextは読み取り用の部分ビュー、または未信頼の編集提案である。Hostのみが原Snapshot・安定ID・権限に基づき全変更を一括適用し、完全な新状態の保存成功後に`applied`を返す。部分Contextを完全なScoreとして保存してはならない。
7. 実装は対応する正確なファミリー・版・能力を宣言する。「OSTF対応」という総称だけで全任意機能への対応を表してはならない。

## 3. 時間・範囲・包含関係

Take Group、Comp Region、Audio transitionは、既存ScoreのPPQと**source-global Tick**座標を使う。Groupは`startTick >= 0`、`durationTicks > 0`を持ち、範囲は半開区間`[startTick, startTick + durationTicks)`である。これらの構造で使うTickの保存値と、終端・オフセット・加算等の結果は、`0..9007199254740991`内の正確な整数でなければならない。正の長さをゼロに潰さず、オーバーフローを丸めたり折り返したりせず診断する。

Core Clipは従来の`start`と`duration`、NoteとMIDI EventはClip内の相対開始値を維持する。Comp範囲と比較する前に実際のClip開始位置を加算する。Production Audio Assetの座標はデコード後フレームである。source Tick、展開後Performance Tick、Session Clock、Audio Frame、画面上の小節番号を混同しない。

任意の`sectionId`は、Groupと範囲が重なる実在Sectionへの編集上の関連付けである。同一境界を強制せず、Section内相対時間を新たな保存座標にしない。全曲・構成・フレーズ・小節・コード・拍より細かい範囲を同じ区間表現で扱う。あるHostはSectionをセッションクリップとして表示し、別のHostはアレンジメントとして表示できる。クリップ格子、レーン配置、起動UIは固定しない。

Section名、テンポ、拍子、小節番号の変更で保存Tickを暗黙に移動しない。明示的な移動、PPQ変換、タイムライン編集では、関連素材・範囲・出力・参照を一括更新する。テンポ変更は`native` Audioの時間関係を変えるため、出力と再結合への影響を判断する。構成名が一致するだけでは古い出力の整合性を証明しない。Tickから秒への変換は、有限Planの再進入時を含め、適用されるsourceテンポ区間をすべて積分する。

## 4. Take Groupと保持する候補素材

Coreの`takeGroups[]`は一つの実在`trackId`に属する。Productionの`audioTakeGroups[]`は一つの実在`channelId`に属し、Channel種別は`track`または`audioTrack`に限る。Bus／Masterには属せない。同一ファミリー・同一所有者のGroup範囲は重複不可。MIDIとProduction Audioは独立領域であり、同時に演奏する既存の記述は引き続き可能である。

Groupは一つ以上の`takes[]`を持つ。MIDI Takeの`clipIds`は所有Track上の既存Clipを一つ以上参照する。Audio Takeの`audioRegionIds`は所有Channel上の既存Audio Regionを一つ以上参照する。各候補の区間はGroup内に収まる。候補ごとに開始位置や長さが異なってよく、部分的な差し替えTakeがGroup全体を覆う必要はない。同一Take内の候補区間は重複不可で、MIDIの複音はClip内に記述する。異なるTake間の区間は重複できる。

候補Clip／Audio Regionは一つのTakeにのみ所属し、別Groupの素材やComp出力を兼ねてはならない。同じTakeを複数Compから選ぶ場合、元候補データを複製する必要はない。Audio Regionは既存Asset規則に従い同じ音声Assetを参照できる。Coreの`clipChoices`は維持するが、Take Groupが管理する候補・出力Clipを同時に対象にしてはならない。既存のID名前空間・参照の一意性は維持する。

候補MIDI Clipは必ず`enabled:false`、候補Audio Regionは必ず`mute:true`を保存する。これは通常再生の抑制であり、削除ではない。元のNote、Note単位のenabled、MIDI Event、歌唱データ、フレーム選択、gain、fadeを保持する。Takeを選ぶことで候補そのものを通常出力に変えない。明示的なHostの試聴は別系統で可能だが、通常再生の選択を矛盾した状態で保存してはならない。

Groupの再生範囲に、同一所有者・同一領域の無関係なClip／Audio Regionを重ねてはならない。Groupへ組み入れる前に、Writerが分割または明示的な整理を行う。Group外素材のイベントがGroup内へ意図せず漏れないようにする。音源の残響・リリース等DSPテイルの挙動を、これらの音楽的区間規則で新たに定義するものではない。

### 候補のメタデータ

`kind`は、同じ意図に対する別演奏の`take`、同じ範囲の内容変奏の`variation`、別の演奏候補の`alternative`とする。選択の仕組みは共通である。これらの分類はHarmony、歌詞本文、曲構成の書換えを許可しない。その変更には既存の該当構造や別Revisionを用いる。同時に鳴らすダブル／Layerは独立したパートとして扱い、競合Takeの選択とは区別する。

`origin`は人間、AI、外部取り込み、派生、不明等の任意の出自を記録する。Prompt、モデル名、URI、遠隔Participant／ProposalのIDは非実行のメタデータである。`parentTakeId`は同一Group内の別Takeに解決し、親参照は循環不可。`ratings`は`[0,1]`の情報的評価であり、自動採用命令ではない。`laneOrder`は表示順のヒントに限る。メタデータから認証、実行、ネットワーク、Assetアクセスの権限は生じない。

## 5. Compと完全な採用写像

`comps[]`の各項目は、一つの完成した保存済み採用結果である。`compRegions[]`は`startTick`の昇順とし、Group全体を隙間・重複なく分割する。各区間の長さは正。隣接境界のTickは半開区間規則により後続区間に属する。

| 区間種別 | 必須の意味 | 禁止する推測 |
|---|---|---|
| `source` | `takeId`と`clipId`または`audioRegionId`がそのTakeの候補に解決し、採用区間全体が候補内にある | 暗黙の移動、ループ、伸縮、素材置換、別Takeからの補完 |
| `silence` | 明示的な無音であり、Take／候補の参照を持たない | 素材欠落を無音指定と同一視すること |

候補と採用区間のsource Tickは一致する。採用は保持した元素材への参照であり、破壊的な切断ではない。部分Takeがない範囲を暗黙に埋めず、Compが別Takeまたは無音を明示する。

`activeCompId`は必須で、Group内CompのIDまたは`null`である。nullは通常の保存状態でGroupを無音にする。`comps`が空の場合は`activeCompId:null`とし、Visit選択も存在するならすべてnull、liveSelectionはfixed／manualのみとする。一つのTakeをそのまま採用する場合もCompで表現し、競合する`activeTakeId`は設けない。Group IDはファミリー内で一意、Take ID・Comp ID・Comp Region IDはそれぞれGroup内の名前空間で一意とする。§12の歴史的IDを除き、現行の参照はすべて解決しなければならない。

## 6. 実体化出力・保存フラグ・原子性

Comp写像を**編集上の正本**とする。`outputClipIds`／`outputAudioRegionIds`が参照する独立IDの通常Clip／Audio Regionを**再生上の正本**とする。非採用Compを含むすべてのCompは、現在の写像に対応した実体化済み出力を持つ。Readerが毎回リアルタイムにNoteや音声を生成する必要はない。出力は同じ所有者に属し、Group内に収まる。候補IDと出力IDは別であり、異なるCompや`clipChoices`で出力IDを共有しない。

完全無音Compの出力配列は空とし、`noteLinks`／`transitions`も非空にしない。source区間が一つでもあるCompは一つ以上の出力を持つ。採用したMIDI sourceに音符がない場合は、出力欠落ではなく`notes:[]`の出力Clipで表現する。同一MIDI Comp内の出力Clip区間は重複不可。出力Clipの区間自体は無音区間をまたげるが、音符のゲートと採用素材は無音指定を守る。必要なリリース／状態イベントで無音への移行を実現できる。Audio出力の重複は§8の遷移窓に限る。候補と非採用出力は保持する。

通常再生用の保存状態は次のとおり固定する。

| 管理対象 | MIDIの`enabled` | Audioの`mute` |
|---|---|---|
| 候補素材 | `false` | `true` |
| `activeCompId`の出力 | `true` | `false` |
| その他のComp出力、またはactiveがnullの場合の全出力 | `false` | `true` |

これらのフラグは**保存済み既定選択**を表す。選択上の標準例外は§9の明示的な有限Visit／ライブ選択であり、保存フラグを書き換えずに選択Comp出力の再生対象判定だけを差し替える。候補素材を有効化する例外ではない。Core Track／Noteのenabled、Production Channel／Automationのmute、ルーティング、既存のPart実現規則は別の権威として維持する。

5.1では、管理対象である候補または出力Audio Regionに対するRegion単位Automationを禁止する。Channel Automationを使うか、Comp出力へ明示的に編集・レンダーする。特に、保存候補や非採用出力をAutomationでunmuteしてはならない。Group管理外のAudio Regionは従来のAutomation能力を保つ。

Writerは、写像、候補編集、影響する全実体化出力、ID、参照、保存フラグを一つの整合したトランザクションとして保存する。写像や素材を編集した後、古い出力を黙って受理してはならない。出力欠落、所有者違い、参照不明、フラグ矛盾、内容不整合は診断し、その編集／保存を拒否する。明示的なHostの修復は新たな整合Revisionを作れるが、Readerが無断で推測修復しない。写像と出力の音楽的対応はSchema形状だけでは証明できず、DSPのbit単位同一性も主張しない。

## 7. MIDIと歌唱の境界

MIDI Compでは`noteBoundary`を必須とする。

| 値 | 出力の実体化規則 |
|---|---|
| `truncate` | 採用source区間内に絶対開始位置を持つ元Noteのみ採用し、ゲートをその区間末で切る。区間より前に開始したNoteの残りから新しい発音を作らない。 |
| `retrigger` | 区間開始時に持続している元Noteも採用し、区間開始で新たに発音させ、ゲートを区間との共通部分に限定する。 |
| `authored` | 明示的に調整された実体化出力の境界／フレージングを実際の演奏とする。採用元の由来と明示的無音は維持する。 |

同じ候補を参照する連続した採用区間は、この処理前に論理的に結合する。単なる区間細分化で発音回数を増やさない。元の開始はClip内相対値から換算し、Note単位の無効状態を維持する。出力Noteには独立IDを与える。任意の`noteLinks`で元Noteと出力NoteのIDを対応付け、対象候補／出力集合内に解決する。一対多・多対一は可能だが、同一組の重複は禁止する。

これは**Compを作成するときの規則**であり、有限Planによる切断規則を置き換えない。固定Visitは、その後で実体化出力に既存のsource開始位置／ハードカット規則を適用する。作成時に`retrigger`を使用したという理由だけで、Visit進入時に新たな発音を合成してはならない。進入位置での発音が必要なら、そのsource位置に明示的な出力Noteがあるか、別の実体化済みPerformance renditionに記述する必要がある。

WriterはCC、サステイン、Program Change、Pitch Bend、MPE／Channel状態、Note参照データ、音素タイミング、歌唱曲線、歌詞alignmentを出力内で整合させる。非採用素材の制御ストリームを通常再生へ漏らしてはならない。必要な初期化／リリースは既存の対応構造で実体化し、表現できなければ制約を報告し、表現可能な結果が得られるまで編集を受理しない。共有MIDIバス上の無関係なパートを変える一括resetを行わない。外部音源の未規定な初期状態は、Take選択だけでは移植可能にならない。

候補Clip内の歌唱データを保持し、出力の参照は新しい出力IDへ更新する。選択で歌詞本文の正本を書き換えず、一部Noteしか残らないalignmentを完全な歌詞発声とみなさない。境界を作成できない実装も、保存出力の再生と追加データの保持はできるが、Comp編集能力を宣言しない。

## 8. Audioの実体化・切出位置・遷移

Audio Compは`outputMode:"regions"`または`"rendered"`を必須とする。`regions`は通常の出力Region記述で採用素材を表す。`rendered`は別の事前レンダー済み`audioSource` Assetを出力Regionから参照する。レンダーはChannelのDevice／Mixer処理前とし、焼き込んだChannel処理を二重適用しない。元Assetは保持する。

従来のFrame条件は必須である。`sourceStartFrame >= 0`、`sourceFrameCount > 0`、両者の和がデコード後Asset `frameCount`を超えず、`fadeInTicks + fadeOutTicks <= durationTicks`とする。切出しでは元候補のsource位置を保持する。

- source Tick `R`で始まるnative候補のTick `t`における理想Frame位置は、`sourceStartFrame + sampleRateHz × T(R,t)`である。`T`はsourceテンポ区間をすべて積分した秒数。選択Frameを使い切った後は無音であり、Comp区間やVisitの先頭でループ／巻戻ししない。
- source長`L`のfit候補の理想Frame位置は、`sourceStartFrame + sourceFrameCount × (t-R)/L`である。短く切った出力でも、`pitchPolicy`を含む元の選択位置・速度関係を保持する。短い区間に元の全Frame窓をそのまま割り当てると誤った伸縮になる。
- 採用範囲で元候補のgainと元Region内fadeの意味を保持する。切断で旧fadeを自動的に最初からやり直さない。必要な包絡、切出し、遷移を既存Region項目で表せない場合、Writerはrendered出力を使うか、その編集能力に対応しないことを明示する。端数Frameの丸め、再標本化／伸縮アルゴリズムはHost依存であり、交換結果に影響する近似は報告する。

任意の`transitions[]`は、明示的に作成したクロスフェードを記述する。`atTick`は異なる候補を採る隣接source区間の境界である。半開区間の窓`[startTick,startTick+durationTicks)`はその境界を**厳密に内包**し、Group内に収まり、窓全体について両候補に実際の素材ハンドルが存在しなければならない。遷移窓は互いに重複せず、別のsource／silence境界をまたがない。明示的無音を跨いで遷移させない。

`curve`は`linear`、`equalPower`、`customRendered`とする。`regions`は線形振幅遷移だけに対応し、出力Regionの一致した重複窓と既存のfadeIn／fadeOut値を明示する。既存包絡との組合せを表現できない場合はrenderedを使う。重複窓内の正規化位置を`u`とすると、追加するlinear重みは`1-u`と`u`である。equalPowerは`cos(pi*u/2)`と`sin(pi*u/2)`を意図する追加重みとしてrenderedを必須とする。customRenderedもrenderedを必須とし、保存音声Assetが再生の正本である。gain、素材相関、DSP、Frame丸めによって結果の音は影響を受ける。

遷移メタデータは編集内容を記録するものであり、実体化済みfadeやレンダー済み音声に再適用してはならない。遷移指定のない境界はハードカットで、自動スムージングを暗黙に足さない。muteされた二つの元Takeの保持だけでは、レンダー済みクロスフェードを提供したことにならない。

## 9. 有限Visitと自由なライブセッション起動

### 9.1 明示的な有限Visit選択

`visitSelections[]`はGroup内で`(performancePlanId, visitId)`の組をComp IDまたはnullへ対応付ける。組は一意で、実在する有限Plan／Visitに解決し、そのVisitが実際に選ぶsource区間の集合とGroupが交差する必要がある。不連続Visitを最小開始から最大終端まで埋まった一つの範囲とみなさない。nullは明示的な無音であり、上書き指定の省略とは異なる。

通常の選択解決は次の順序とする。

1. 有限Visitでは完全に一致する`visitSelections`があればそれを採用し、なければ保存済み`activeCompId`を使う。自由なliveSelectionで有限Planの決定を置き換えない。
2. Groupとの交差範囲では他Compの出力を抑制し、選択Compの実体化出力だけを再生対象にする。上書きするのは保存済み既定選択を表す管理対象出力の`enabled`／`mute`だけである。候補は引き続き無効で、保存フラグを書き換えない。
3. Core MIDIにはTrack／Noteのenabledと既存Visit Partの実現方式を適用する。Compを選んでも`silent`、`open`、`unspecified`は固定再生にならず、`fixed`だけが保存された音楽出力を再生する。openパートは別途明示的に対応した仕組みで実現できる。
4. 実際の各source区間との交差部分だけに素材を投影する。選択後に既存の連続source接続／ハードカット、source状態、Automation、Tempoの規則を適用する。Visit境界で元Audio Frameやfade位置を最初からやり直さない。

**Productionの独立性を維持する。** Production Audio Regionは、ChannelがCore Trackを参照していても、Core固定Noteの実現方式とは独立する。従ってAudio Compの選択と通常Audio出力は、そのCore Trackの`enabled`や`realization:"silent"`／`"open"`だけでは自動抑制されない。Production Channel／Regionの適格性、mute、routingに従う。上記の選択上書きは管理対象Audio出力の選択集合を差し替え、Visitのsource区間に投影する。特定VisitでAudio Take Groupを無音にするにはnull／完全無音Compを明示的に選ぶか、適切なProduction muteを使用する。これは旧5.1差分にあったAudio候補とCore Part実現方式の曖昧な連動説明を解消する規定である。

保存済み5.1再生に対応していてもVisit選択に未対応のHostは、機能未対応を明示した上で保存既定結果を保持・再生できる。異なる選択を含むPlanを同等に再現したと主張してはならない。

### 9.2 自由なライブ起動

任意の`liveSelection`は、解決済み有限Plan Visitとは別の、Hostの自由なセッションモード起動時の方針である。

| mode | 選択 |
|---|---|
| `fixed` | 保存済み`activeCompId` |
| `manual` | Host／利用者が明示的に選んだGroup内Compまたは無音。未決定なら保存済み選択 |
| `cycle` | 初回は候補一覧の先頭、以後は記載順に循環 |
| `random` | 候補を等確率で選択 |
| `weighted` | 非負のweightに比例して選択。総weightは正 |

cycle／random／weightedでは、実在する異なるComp IDの非空候補一覧を必須とする。weightedでは全候補のweightが必須で、他modeではweightを禁止する。fixed／manualには候補一覧を付けない。動的候補内の無音は名前を持つ完全無音Compで表現できる。候補やメタデータが自動起動を命令するものではない。

確定した起動は§9.1と同じ出力選択上書きを使い、`activeCompId`を書き換えない。未確定または未対応の場合は保存済みactive Compへ戻し、Hostは動的機能未対応を報告する。選択は起動時に確定する。量子化、クリップ途中の切替、無期限ループ、セッションTransport、複数TrackのScene同時制御、乱数seed永続化はHostの方針であり、新しい標準フィールドにはしない。繰返し起動のために元Clipを複製したり無限Visit配列を保存したりしない。

有限の演奏結果を交換する場合は、有限Planと`visitSelections`に明示的な決定を記録する。未記録のランダム／手動選択の再現性は保証しない。Hostは複数Trackの選択を一つのトランザクションで確定できるが、ラベルや同じTake番号だけから規格共通のSceneやTrack間対応を推測しない。

## 10. 分散・AI・Plugin連携

Distributed Session 0.4は従来のSnapshot／Event文法、Clockモデル、権限規則を維持し、Score 5.1の正確な元バイト列・文書／Revision・有限Planに結合する。採用した遠隔演奏句をTakeへ取り込む処理は、候補と整合した出力を作るHostの明示的Score編集である。遠隔CommitだけではCompを選択・変更しない。新Score Revisionで、既存の変更不可な確定EventやScore pinを遡って置き換えない。新たなネットワーク実行器、自動Comp同期、ロボット駆動権限は追加しない。

Plugin Context 1.1はScore 5.1の識別を追加する。この組合せに限り、認可された編集pathにGroup自体の`/takeGroups/{index}`、その子孫の`/takeGroups/{index}/...`、Group追加用の`/takeGroups/-`を加える。旧Scoreへの結合は従来の編集可能rootを維持する。`/takeGroups`配列全体の置換／作成は、このプロトコルの編集対象ではない。配列がない場合はHostが先に明示的なRevisionとして初期化・保存し、新Score SHAに対するContextを発行し直す。

root配列への追加では、`containerId`をpinされたScoreの実際の`document.id`に解決し、Envelopeに一致する`score.documentId`を含め、`newEntityId`を追加Groupの`value.id`と一致させる。Scoreに文書IDがない場合、Hostがその編集Contextを発行する前にIDを設定する。入れ子編集は既存の安定owner／entity ID規則を維持する。提案はTake Group、影響するTrack Clip、全Comp出力、保存選択フラグを原子的に整合させる。写像やactive IDだけを変えて出力フラグを矛盾させる提案は不正。参照不明、古いSnapshot、未認可pathは拒否し、プロトコル版だけでアクセス権は得られない。

Core Plugin Contextの権限はProduction Audio Comp編集を許可しない。Hostは別途認可されたProduction編集経路を実装できるが、Productionの結合とトランザクション条件を維持する。出自Prompt、評価、モデル名、遠隔IDは情報であり、実行命令ではない。

## 11. Package・移行・保持

OSTFP 1.1は5.0のZIP配置、mimetype、安全なpath、manifest、正確なバイトSHA、Asset／Binding規則を維持する。許可する対応版を次のとおり固定する。

| 同梱Score | Production | Distributed |
|---|---|---|
| 4.3.0 | 0.2.0 | `OSTF-Distributed-Session-0.2` |
| 5.0.0 | 0.3.0 | `OSTF-Distributed-Session-0.3` |
| 5.1.0 | 0.4.0 | `OSTF-Distributed-Session-0.4` |

任意ファミリーは省略できるが、同梱する場合はScoreの行に一致させる。Package 1.0は元の受理バージョンを維持する。Package 1.1によって旧Scoreの識別を消去・再解釈しない。Audio Takeの素材は既存の`productionAsset` bindingを使う。lossless Packageには、可聴出力だけでなく、管理対象の元候補・非採用素材と必要な全Assetを含める。解決不能な外部素材は明示し、無断ダウンロードや代替置換をしない。

5.0から5.1への移行は、明示的なRevision／変換操作である。テイクなしScoreは音楽データを保持できるが、版のバイトが変わるため新SHAと明示的な関連文書／Package再結合が必要になる。該当する文書／Revision ID、Productionのsource Tick意味、新しいPlugin Contextを整合させる。過去のDistributed Eventを無断でrepinせず、継承したSession移行規則に従う。

5.1から5.0への移行は、**保存済みactive出力を取り出す明示的な変換**である。採用された通常出力と音楽データを維持し、新しいTake Group構造を取り除き、規定の移行に従って関連文書／Package／Protocolの識別を変換する。別の採用写像、メタデータ、履歴、Visit／live決定の損失を報告する。元候補や非採用出力を残す場合はdisabled／mutedのままとする。削除する場合は残る参照、歌詞alignment、Asset bindingを修復する。非破壊編集を残すには元5.1プロジェクトを保持する。

単純なdowngradeではVisitごとに異なる選択は保持できない。確定した有限演奏を保持するには、適切な別出力ID、Tempo／状態規則、損失報告を持つ新しいArrangement／RenditionへHostが明示的に実体化する。元Scoreを無断でflatten／版変更しない。5.0のみ対応のReaderが5.1 Scoreを直接受理する義務はない。

## 12. 情報的な選択履歴

任意の`takeSelectionHistory[]`は保存された選択履歴である。`sequence`はGroup内で厳密に増加する非負の安全整数、`compId`はその時点の採用IDまたはnullとする。`actorId`、`recordedAt`、`reason`は任意。削除済みCompの歴史的IDを残してよいが、現行再生の参照解決に使ってはならない。履歴は`activeCompId`、`visitSelections`、明示的ライブ起動を上書きせず、完全なイベントログも必須としない。再現可能な有限演奏は有限Plan選択で記録し、不完全な履歴から推測しない。

## 13. 能力宣言とリリース範囲

能力は段階的な必須レベルではなく、独立に宣言する。`score-5.1-read`、`score-5.1-write`、`take-preserve`、`midi-comp-edit`、`audio-comp-edit`、`visit-selection`、`live-selection`、`distributed-0.4`、`plugin-context-1.1`、`package-1.1`を用いる。アプリはTakeレーン表示やComp編集を備えなくても保存済み再生とデータ保持に対応できる。lossless Writerは、管理する未対応標準データ／Assetを保持するか、破壊的上書きを拒否して損失を説明する。

意味上の適合には所有者と範囲の包含、参照解決、Group／Compの一意性、全域分割、候補と出力の有効状態、境界状態、版の正確な結合、原子的更新を含む。JSON Schemaだけではこれらの義務、同一レンダリング、プラグイン利用可能性、ネットワーク時間精度を証明できない。ユーザーインターフェースは各実装が決める。

**本書面仕様は策定者の一括承認に基づく正式リリース仕様である。動作検証、独立パーサー、DAW、DSP、プラグイン、実機、WANでの実行試験はリリース条件に含めず、実施済みとも主張しない。** 仕様リリースは、リポジトリ／Tagの公開作業や実装アプリの認証とは別である。保存された旧Draftの文言から追加の個別承認・実機試験条件を導入しない。

完全な項目宣言と作成手順は、[パラメーターリファレンス](PARAMETER_REFERENCE.ja.md)、[全網羅マニュアル](COMPLETE_MANUAL.ja.md)、[移行表](MIGRATION_MATRIX.ja.md)、[適合性](CONFORMANCE.ja.md)、[セキュリティ](SECURITY.ja.md)、現行ファミリー別仕様、採択済み原本を併せて参照する。
