# OSTF 5.1.0 — Distributed Session 0.4 正式規範仕様

**この版は2026-11-16正式採択4.3 Distributed Session0.2（SHA照合済）を元にした5.1版。** 規範Schema: `schema/ostf-distributed-session-0.4.schema.json`。Core/Production/Plugin Contextとは別のJSON文書。通信・WAN同期・音源・ロボットの実行権限を与えない。

## 文書識別・原本へのピン

`profile:"OSTF-Distributed-Session-0.4"`と`recordType:"snapshot"|"event"`を両文書で使用する。`profileVersion`やネストした`score`は**使用しない**。`sessionId`、`documentId`、`revisionId`、`performancePlanId`、`scoreSha256`（元Score5のraw UTF-8バイトSHA-256、64桁小文字）は共通必須。PlanはScore5の既存かつ有限な`performancePlans[]`を参照する。参照の同一性は外部に現物Scoreが存在してはじめて確認できる。

## Snapshot

`sessionStatus: prepared|playing|stopped`、`stateRevision`非負整数、`authorityParticipantId`、1件以上の`participants[]`が必須。各Participantは`participantId`, `kind:human|softwareAgent|physicalRobot`, `assignedTrackIds[]`を必須とする。`playing`には`position`必須、`prepared/stopped`では任意。`committedPhrases[]`、`commitmentWindow`は任意であり、既存の意味を継承。

`commitmentWindow`は`startPerformanceTick`と`endPerformanceTick`の半開区間で、`start<end`。窓を与える場合はplayingで`position`と`committedPhrases`が必須であり、**窓と交差する確定フレーズが全て含まれるという宣言**になる。不完全な窓に暗黙の`coverage:partial`を付けることは認めない。窓を省略して部分抜粋を保持できる。

## Event

`eventId`, `issuerParticipantId`, `baseStateRevision`, `effectivePerformanceTick`, `kind`, `payload`が必須。7種類：`phraseProposed`, `phraseCommitted`, `turnRequested`, `cueIssued`, `performanceObserved`, `participantStatus`, `sessionStateChanged`。`phraseCommitted`と`sessionStateChanged`では`resultStateRevision`が必須であり、受理時に必ず`base+1`。それ以外はこのフィールド禁止。イベント重複の冪等性、StateRevision競合・順序・権限は採択版0.2の意味を継承。

`phrase`は`representation:"midi1Notes"`, `durationTicks>0`, `notes[]`（pitch 0..127, velocity 1..127）の構造。確定フレーズは`commitEventId`で識別し、CoreのNotesへの自動編集や実DSP/ロボット制御ではない。

`sessionStateChanged.payload.changeKind`は`sessionStarted`, `visitChanged`, `assignmentChanged`, `sessionStopped`の4種類。時計Anchor (`position`: performancePlanId/visitId/sourceTick/performanceTick/clockDomainId/epochUtc/uncertaintyMs) は開始・Visit移動で必須。Assignment変更ではTrack集合のみ。Stopped後の同一Session再開は定義せず、別Sessionが必要。

## Score 5と旧0.2の分離

同名の意味を持つフィールドでも、正式0.2はScore 4.3専用、0.3はScore 5.0専用、0.4はScore 5.1専用。Scoreを改訂した時は新Sessionを明示的に作る。単に`profile`だけ差し替えたり、過去Eventの権限・参加者・clockを自動引き継いだりしない。Schema構造の妥当性は実ネットワーク・機材動作の証明ではない。

**過去の未公開草案からの修正履歴**：旧ネスト`score`、`participant.id`、`phrase.encoding`、`committedPhrase.eventId`、`commitmentWindow.coverage`を正式0.2由来のwireフィールドへ修正。旧草案例は新Schemaに対応した新しいExampleへ書き直した。


## 5.1のテイクとの接続

0.3はScore 5.0、0.4はScore 5.1に固定します。既存の7イベント種別とSnapshot/Event構造を継承し、新しいネットワーク操作は追加しません。phraseCommittedの受理だけではScore、takeGroups、activeCompIdは変わりません。ホストが許可した取込み操作で候補素材を作り、originにsessionId/proposalId/commitEventIdを記録できます。これらは出自情報であり権限ではありません。新Scoreへ履歴Eventを自動的に付け替えません。
