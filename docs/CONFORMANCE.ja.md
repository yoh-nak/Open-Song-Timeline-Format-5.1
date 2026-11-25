# OSTF 5.1.0 — 機能別適合宣言

機能は独立して宣言します。レベル1〜5のような必須階層は設けません。各能力に文書ファミリー・正確な版・read/write/edit等の操作を添えます。

| Capability | 範囲 |
|---|---|
| `score-read/write` | 正確なScore版・Core意味・未知情報の保持 |
| `take-preserve` | 候補・Comp map・出力・選択・付属データの一貫保持 |
| `midi-comp-edit` | MIDI候補/採用区間/独立出力と境界・MIDI状態の実体化 |
| `audio-comp-edit` | Audio候補・Frame・位相・transition/出力/素材保持 |
| `visit-selection` | 有限Plan/Visitの範囲と再生overlay |
| `live-selection` | 起動時のfixed/manual/cycle/random/weightedと未対応報告 |
| `production-read/write` | 対応版・Score pin・Channel/Device/Audio/Automationの宣言範囲 |
| `distributed-read/authority` | 別Sessionのpin・状態・Eventと外部権限 |
| `project-read/write` | OSTFP版・目録・元SHA・size・path・binding |
| `plugin-context-consume` | 部分ビューを完全Scoreと誤認しない |
| `plugin-edit-propose/apply` | 原子的提案と永続保存後ACK、外部認可 |
| `loss-report` | 受領範囲と実際の保持/損失の明示 |

テイク編集に未対応の5.1 Readerは保存済み通常出力を再生できますが、Visit/liveの動的選択を再現したとは表示しません。5.0専用Readerでは明示的な5.0 Exportが必要です。MIDI対応はAudio対応を、データ保持は意味理解を、Schema適合は音響/DSP互換性を意味しません。

規定上の参照・区間・音楽的対応を検査する責任と、実際の動作試験の実施状態は別です。本リリースは承認済み書面仕様であり、実機・DAW・独立実装の動作検証は行っていません。
