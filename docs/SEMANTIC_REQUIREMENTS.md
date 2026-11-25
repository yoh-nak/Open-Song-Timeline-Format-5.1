# OSTF 5.1.0 — Semantic requirement index / 意味規則索引

This index summarizes required data consistency; it is not a record of executed tests. 本表は実装者向けの意味規則索引であり、動作検証の実施記録ではありません。詳細と例外は現行SPECIFICATIONおよび各family仕様を優先します。

| ID | 日本語 | English |
|---|---|---|
| TC01 | 各参照が正しい所有者・ID名前空間内で一意に解決 | Resolve every reference uniquely in its owner and ID namespace |
| TC02 | 元Score Tick/PPQ、半開区間、安全整数の和、正の長さ | Source-score Tick/PPQ, half-open intervals, safe endpoint sums and positive duration |
| TC03 | 同一ドメイン・所有者のGroupは非重複 | Groups are disjoint per domain and owner |
| TC04 | 候補は元Clip/Regionに参照、別Comp出力と共有しない | Candidates reference original Clips/Regions and never share output identity |
| TC05 | 同一Take内は非重複、部分Takeの不足は暗黙補完しない | Disjoint source intervals within each Take; no implicit partial-take filling |
| TC06 | Comp mapは全Groupの隙間なし非重複分割、無音を明記 | Comp map completely partitions Group without gaps/overlap; silence is explicit |
| TC07 | source区間がTakeに属し元素材の範囲内 | Source selection belongs to the Take and lies within source bounds |
| TC08 | activeCompは存在するIDまたはnull、comp空ならnull | Active Comp resolves or is null; empty Comps require null |
| TC09 | 候補は常時無効/mute、保存時にactive出力だけ有効 | Candidates always disabled/muted; saved active outputs alone selected |
| TC10 | 全silence Compは出力/リンク/遷移なし、sourceありは出力あり | All-silence Comp has no outputs/links/transitions; source-bearing Comp has outputs |
| TC11 | 各Comp出力を一意に所有、旧clipChoicesと排他 | Output identity is owned once and is disjoint from legacy clipChoices |
| TC12 | map・独立出力・flags・関連参照を原子的に保存 | Atomically save maps, independent outputs, flags and related references |
| TC13 | MIDI境界、状態追跡、ノートID/歌詞/音素参照を出力で整合 | Materialize MIDI boundaries/state and output note/lyric/phoneme references consistently |
| TC14 | noteLinksが各Compのsource/outputへ解決、組重複なし | Resolve noteLinks within corresponding source/output; no duplicate pair |
| TC15 | Audioフレーム範囲・Tempo位相・fit比・fadeを保持 | Preserve Audio frame bounds, tempo phase, fit ratio and fades |
| TC16 | 遷移窓はsource/source境界を内包し実ハンドルを持つ | Transition windows contain source/source junctions and actual source handles |
| TC17 | 遷移窓非重複、regionsはlinear、その他rendered | Disjoint transition windows; regions uses linear, others use rendered output |
| TC18 | 管理Audio RegionへのRegion単位Automationなし | No Region-targeted automation for managed Audio Regions |
| TC19 | Visit参照・重複組・交差範囲を確認、overlayは保存flag限定 | Resolve Visit, unique pair and intersection; overlay overrides only selection flags |
| TC20 | Core silent/open規則をMIDIへ適用、Production独立性を維持 | Apply Core silent/open to MIDI while preserving Production independence |
| TC21 | live候補IDの一意性、weighted全weightと正の合計 | Unique live candidate IDs; all weighted values supplied, positive total |
| TC22 | parentTakeは同Group内非循環、履歴sequence厳密昇順 | Acyclic same-Group lineage; strictly increasing history sequence |
| TC23 | 元ScoreバイトSHAと全Profile/Manifest pinの一致 | Exact raw Score SHA agrees with all companion/manifest pins |
| TC24 | 版matrixとmanifest目録・全Asset SHA/size/binding | Version matrix, manifest inventory and every asset SHA/size/binding |
| TC25 | Plugin1.1 Take編集はScore5.1のみ、全変更共通Snapshot | Plugin1.1 take edits only for Score5.1; all edits share one source Snapshot |
| TC26 | 未対応情報を保持または無損失保存拒否、旧版Export損失報告 | Preserve unsupported information or decline lossless save; disclose downgrade loss |
