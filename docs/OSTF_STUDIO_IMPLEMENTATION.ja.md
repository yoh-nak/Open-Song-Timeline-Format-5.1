# OSTF Studio — 5.1実装ガイド

本書はアプリ実装上の推奨設計です。標準の時間・保存・採用規則は`SPECIFICATION.ja.md`が正本です。OSTF Studioの実装完了や動作確認を示すものではありません。

## 構成×トラックのセッション画面

行をSection、列をTrackとする構成単位のクリップ表示を維持できます。セルは既存の素材とTake Group/Compへのビューであり、規格にUIセルやAbleton固有オブジェクトを追加しません。通常はSectionと同じ範囲のGroupを1つ作り、必要なら小節・コード・フレーズ・任意Tick範囲のGroupを扱います。

Section内の相対表示位置は`sourceTick - section.start`です。保存上はsource-global Tickを維持します。同じSectionの再訪は素材を複製せず、有限Performance PlanのVisitやホスト内の起動Instanceで区別します。SectionをまたぐGroupは一つのIDを保ったまま、UIで範囲を投影します。

## 推奨する基本操作

| ユーザー操作 | 保存する内容 |
|---|---|
| 録音/AI生成 | 新しい候補Clip/RegionとTake。候補は無効/mute |
| テイク全体を採用 | そのTakeの範囲＋明示無音からなるCompと別出力 |
| 小節やコード単位の採用 | UIで区切ったsource-global Tick区間をcompRegionsへ |
| コンピング | 完全な非重複区間mapと実体化済み出力を同時更新 |
| Compの切替 | activeCompIdと旧/新出力の選択用flagsを一括保存 |
| ライブ中だけ変更 | 再生時の選択overlay。保存activeCompは維持 |
| 曲として確定 | 有限Plan/visitSelectionsと対応Comp出力を保存 |
| 旧形式へ書出し | 保存active出力を通常素材として投影、損失報告 |

## ライブ起動

ホストは起動量子化、ループ長、複数トラックの同時切替、停止、試聴、UI状態を扱います。標準liveSelectionのcycleは最初の起動を先頭候補から始め、randomは一様、weightedは明示した正の総重みに比例します。固定再現が必要な演奏は最終選択を有限Visitに記録します。無限ループを無限Visit列で保存しません。

Visitまたはliveで選ばれたCompは、保存上の選択用enabled/muteと独立した再生overlayで鳴らします。候補素材を通常再生に混ぜません。Core MIDIのsilent/openと独立したProduction Audioの扱いは維持し、両方を止める操作ではチャンネル制御等を明示します。

## 境界と編集

MIDIのtruncate/retrigger/authoredはComp出力作成時の選択であり、Visitの途中再入に勝手なNote Onを付加する指示ではありません。サステイン・CC・MPE・歌詞/音素の対応を出力側で整えます。オーディオは元素材の位相とframe区間を維持し、表せない複合fadeやequalPowerはチャンネル処理前にレンダーします。

クリップの色、レーンの高さ、波形表示、キーバインド、構成ボタン、画面上の並びは各実装が決めます。表示用に別の必須時間体系を作らず、ホスト拡張を使う場合も標準の意味を変更しません。
