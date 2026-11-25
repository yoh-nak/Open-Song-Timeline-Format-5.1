> **現行採択候補：Draft 0.77（未承認）。** 冒頭の参照解決判定表を現行提案とし、下位の旧Draft番号を持つ節は履歴であって並列の現行規範ではありません。今回の変更は編集上の特定であり、Schemaやシリアライズ形式は変更しません。

# Draft 0.73 — 現行の参照解決判定表（未採択の規範案）

**承認対象：D03。** 以下が現行の採択候補であり、後続のDraft 0.62〜0.72の記述は改訂履歴として保持する。古い判定例を並立する現行規則として扱わない。発行者の採択前に規範として確定したわけではない。Schema・シリアライズ形式は変更しない。

| 優先順 | 条件 | 実装側の診断 |
|---|---|---|
| 1 | ProfileのJSON・必須pin・形式が不正 | `INVALID`（4状態の対象外） |
| 2 | Profileの形式・版が未対応 | `UNSUPPORTED`（4状態の対象外） |
| 3 | 許可範囲が未定義、候補列挙未完了、必要なScore実体を取得不可 | `NOT_EVALUATED`（暫定情報は別途報告、確定4状態を返さない） |
| 4 | 明示的に許可された完全な候補集合にScore実体が0件 | `MISSING`（評価範囲内に限る） |
| 5 | Scoreの実体はあるが、元バイト列のSHA-256がpinと一致しない | `MISMATCH`（評価範囲内に限る） |
| 6 | ハッシュ一致したScoreが構造的に不正または解析不可 | Score形式エラー（`RESOLVED`ではない） |
| 7 | 一致する正常なScore内のTrack/Plan/Visit/range等の必須参照が欠落・重複・不正 | `AMBIGUOUS`＋具体的な診断（`missing_referent`、`nonunique_referent`等） |
| 8 | 元バイト列とハッシュが一致し、必要な参照がすべて一意に解決 | `RESOLVED`（評価範囲内に限る） |

**同一性と権限の境界：** 宣言されたハッシュ対象の元Scoreファイルのバイト列を使用する。Unicode正規化、改行変換、BOM除去、JSONの再シリアライズ、ZIP全体のハッシュによる代替は禁止する。同じバイト列のコピーは同一のバイト同一性を持つ。ファイル名、URI、キャッシュしたハッシュ、音楽上の等価性だけでは同一としない。探索に失敗した候補を黙って除外せず、範囲を狭める場合は新しい評価として明示する。診断名はJSON Schemaに追加するフィールドではない。ハッシュ一致は著作権、信頼性、アクセス権、音響再現、遠隔実行、ロボット安全性を保証しない。編集後の付け替えには明示的承認と新しいpinが必要。

**公開管理：** D01〜D05はすべて未承認。独立パーサー、DAW／プラグイン／DSP、歌唱、WAN／分散実行、フィジカルAI／ロボットの動作検証は公開GO条件から除外し、実施済みとも主張しない。

---

# Draft 0.72 — 編集上の優先順位と採択範囲（未承認）

**採択対象：D03／Production Session 0.2。** 正式採択の対象は、承認記録で特定する本文と既存Schemaに限る。過去Draft 0.62〜0.70の参照判定例は改訂履歴として残し、並立する定義として扱わない。矛盾する参照診断については**現行候補内で**Draft 0.71の「許可された候補集合の列挙・取得が完了してから判定」する規則を優先し、未完了ならJSONに新項目を追加せず外部診断`NOT_EVALUATED`とする。

第三者実装は、(a)未知データの読込・保持、(b)ラウンドトリップ保存、(c)編集、(d)意味解釈、(e)実行を区別する。いずれか一つの対応を他の操作まで拡大して表明しない。ハッシュ一致は分散演奏実施、ミキサーの音響再現、ロボット動作の保証にならない。これらの規範案は**D03が発行者により正式採択された場合のみ**規範効力を持つ。

> **Current proposed editorial precedence: Draft 0.71.** This first section supersedes the Draft 0.70 incomplete-enumeration RESOLVED exception; historical sections below are retained as version history. No publisher adoption is implied.

## Draft 0.71 — 参照判定の探索完了条件（未採択の規範案）

Draft 0.70の「探索が未完了でも追加候補で結果が変わらないと予測できればRESOLVEDにできる」という例外を撤回する。未確認候補に関する予測を検証済みの根拠として扱ってはならない。

1. Profileの構造と対応バージョンを先に確認する。不正・未対応なら参照判定とは別の`INVALID`／`UNSUPPORTED`を報告する。URIやハッシュの存在はScore実体へのアクセス許可にならない。
2. **明示された有限かつアクセスが許可された候補集合**を定義し、その範囲、列挙完了、各候補の実バイト取得とSHA-256計算の有無を記録する。判定は宣言された範囲に限定し、世界中に存在しないと断定しない。
3. 候補列挙が未完了、または必要な候補の元バイトが取得できない場合は、外部診断`NOT_EVALUATED`と取得済みの根拠を示す。ハッシュ一致候補が1つ見つかっても4つの確定状態を報告しない。より狭い集合を明示的に定義し直して再評価してもよいが、除外した候補と探索範囲変更を必ず開示する。
4. 列挙と取得が完了した集合について、候補が0件なら`MISSING`、候補があるが生バイト列のSHA-256一致が0件なら`MISMATCH`、一致したScoreの必須参照が欠落・重複・無効なら`AMBIGUOUS`、一致と全必須参照の一意解決が揃った場合のみ`RESOLVED`とする。
5. 同じScoreバイト列の複数コピーは同一データとして扱う。名称、URL、音楽内容、申告ハッシュだけで一致としない。改訂Scoreへの付け替えには明示的な許可と新ハッシュの指定が必要。参照判定だけで実行・通信・音響・プラグイン・ロボット制御を許可しない。

`NOT_EVALUATED`／`INVALID`／`UNSUPPORTED`／診断補足は報告用で、JSONフィールドやSchema enumの追加ではない。4つの判定名称も新しいシリアライズ項目ではない。この規則はD01・D02・D03の正式採択前の提案で、動作・相互運用検証は未実施である。

---

# Draft 0.69 — Score候補の探索範囲と判定の確実性（未採択）

**R04/R11/R13/R14の提案規範。** 4種類の参照診断は、対象操作について**明示的に提供・許可された候補集合内**で判定する。無関係なローカルフォルダーや遠隔URL、リポジトリを勝手に探索して`MISSING`を`RESOLVED`へ変更してはならない。利用者またはホストが追加の元バイト列を許可した場合は**新たな評価**として再判定する。

- **許可された元バイト列候補が0件：** `MISSING`。あくまで評価対象内で未発見であり、Scoreの世界全体における消失を断定しない。
- **候補が1件以上あるがピンのハッシュと一致しない：** `MISMATCH`。候補がすべて新しいリビジョンでも同じ。旧Scoreが全世界から消えたとは断定しない。
- **ハッシュ一致・Score構造不正：** `RESOLVED`ではなくScore形式エラー。
- **ハッシュ一致・必須参照先が0件または複数件：** `AMBIGUOUS`に詳細`missing_referent`または`nonunique_referent`を付す（JSONに追加するフィールドではない）。
- **必要な参照がすべて一意に確定：** 評価対象内で`RESOLVED`。同じバイト列の複製は単一の同一性として扱う。

キャッシュされたハッシュ、ファイル名、URL、署名付きリンク、索引の一致だけでは、実際のScoreの元バイト列による照合を代替できない。候補の元バイト列を取得できず評価自体が行えなかった場合、操作側で`not_evaluated`/`unknown`等を報告してよいが、これはOSTFの第5の参照状態ではない。確認済みの`MISSING`や`MISMATCH`と偽ってはならない。参照診断はデータの真正性、発音、プラグイン復元、ロボットの実行許可を保証しない。**D01～D03、D05、D04は未承認。**

---

# Draft 0.68 — 参照診断の判定順序と過去の事例表の整合（未採択）

**現行の提案（R04/R11/R13/R14）:** 明示的に許可されたScore候補だけを用い、次の順序で判定する。過去のDraftの表が異なる場合、この節を現行の編集提案とし、過去の記録は履歴として残す。

1. Companionの形式・バージョン・必須ハッシュが不正／未対応なら`INVALID / UNSUPPORTED`。4種類の参照診断には含めない。
2. Scoreの元バイト列の候補が1件もなければ`MISSING`。ファイル名やメタデータの一致は候補とみなさない。
3. 候補が存在するが元バイト列のSHA-256が1件も一致しなければ`MISMATCH`。**新版Scoreだけが存在する場合も同様**。Draft 0.62の旧事例でこの場合を`MISSING`とした記述は現行提案では採用しない。
4. 一致したScoreが解析不能または必須構造違反なら、参照成功とせずScore形式エラーとして報告する。
5. 一致して正常なScoreの必須参照を全件調べる。参照先0件は`AMBIGUOUS`と詳細`missing_referent`、複数件は`AMBIGUOUS`と`nonunique_referent`、矛盾・範囲違反は`AMBIGUOUS`とその詳細を示す。複数の問題があればそれぞれ報告する。
6. 必須参照がすべて一意に解決した場合のみ`RESOLVED`。同じバイト列を持つ複数のパスは1つのScore同一性として数える。

この状態名・詳細は**実装側の診断指針**であり、新しいJSONフィールドやSchema列挙値ではない。認証、演奏実行、無断ネットワーク取得、権利許諾、自動的な再関連付けを許可しない。日本語版と英語版の意味が異なる場合は採択を保留する。D01〜D05は未承認。実機・独立パーサー等の検証は条件外かつ未実施。

---

# Draft 0.67 — 参照診断の意味規則の確定候補（未採択）

**公開前の要判断事項（R04/R11/R13/R14）:** Draft 0.64では、必須のTrack/Plan参照先が「存在しない」ケースを`AMBIGUOUS`と呼んでいます。一方、通常の意味では`AMBIGUOUS`は「候補が複数で一意に定まらない」ことを表します。これは提案文書の解釈上の曖昧さであり、Schemaの欠陥や検証結果ではありません。

**採択推奨:** 新しいJSONフィールドや状態の列挙値は導入せず、既存の4つの人間向け診断分類を維持します。対応するProfileを構造的に確認し、許可された元Scoreの**生バイト列**のSHA-256一致を先に要求します。その後、必須Track/Plan/Visit参照先の件数が**0件**ならサマリーは`AMBIGUOUS`とし、診断詳細で`missing_referent`を示します。**2件以上**なら同じサマリーでも詳細は`nonunique_referent`とします。各必須参照が1件に確定した場合のみ`RESOLVED`です。詳細ラベルは推奨診断名であり、OSTFの新規フィールド・enum値・保存必須データではありません。`MISSING`は元Scoreの正確なバイト列がない場合に限り使用し、Score内部の参照欠落には流用しません。

**参照元の信頼境界:** 呼出元が明示的に提供・許可したScore候補のみ参照できます。ファイル名、URL、タイトル、意味的に等しい再シリアライズ結果は生バイト一致の証拠になりません。外部ネットワークからの無断取得、暗黙の付け替え、根拠のない可逆保存の表明は禁止する方針を採択候補とします。

**審査状況:** D01〜D03による採択・修正・却下が必要です。D04/D05も未承認です。動作・独立パーサー・DAW・WAN・ロボットの検証は対象外で未実施です。

---

# Draft 0.66 — 現行審査基準（未採択）

この節は**現行Draft 0.66の審査基準**です。本文に残る旧Draft番号の追記は経緯を示す資料であり、独立した現行版の規範ではありません。Schema・サンプル・ツールは変更していません。

- **Core 4.3:** `schema/ostf-4.3.0.schema.json`と現行Core仕様書・意味規則。4.3で変更を明記していない部分は4.2を継承します。
- **Distributed Session 0.2:** Versionに対応するSchemaと日英Session仕様書。セッションのイベントや同期状態は、ネットワークサービスの保証やロボット実行の許可ではありません。
- **Production Session 0.2:** Versionに対応するSchemaと日英Production仕様書。ミキサー設定・プラグイン記述・アセット参照は、実際のDSP実行や音声再現を保証しません。
- **権限の優先順位（採択案）:** 構造制約は該当バージョンのSchema、意味制約は該当バージョンの規範仕様を参照します。例示、旧版追記、チェックリストはこれらを上書きできません。Schemaと規範仕様が矛盾した場合は、任意解釈を認めず公開阻害要因として修正します。
- **Score参照:** 先にProfileの形式・Versionを検査し、元Scoreのバイト列のSHA-256一致を確認後、必要な参照を解決します。RESOLVED／MISSING／MISMATCH／AMBIGUOUSは診断用の名称でJSONフィールドではありません。不正形式・未対応版は4状態に含めません。参照先不足の具体的な原因を記録し、暗黙の再関連付けを禁止します。
- **対応表明:** Score／Distributed／Production、Version、読込／編集／保存／保持／実行を区別し、未対応や欠落を表示します。

R01〜R14の一括採択は提案段階です。D01〜D03の発行者承認、D05の権利承認、D04の最終ZIP承認は引き続き未完了です。動作・独立実装・実機検証は公開判定から除外し、実施済みとは表記しません。

---

## Draft 0.64 — 形式検証と参照解決の境界（未採択の規範案）

Draft 0.63の4状態は、**形式上有効かつ認識可能な関連Profile**について、元Scoreの参照が解決するかを表す診断である。JSONフィールドや通信上の状態コード、動作認証ではない。判定順序は次のとおり。

1. **関連Profileを先に形式検証する。** Profile種別と版、規定の位置にある必須SHA-256参照の書式を確認する。未対応版や必須参照の不正は**INVALID / UNSUPPORTED**であり、`MISSING`や`AMBIGUOUS`としない。
2. **利用を許可されたScore候補の元バイト列を列挙する。** 候補がなければ`MISSING`。候補はあるが元バイト列のSHA-256が一致しなければ`MISMATCH`。ファイル名、タイトル、音楽内容が同じJSON再出力によって代用しない。
3. **ハッシュ一致後に必要な参照を解決する。** Profileが要求する識別子・Track・Plan・Visit・範囲・改訂などを確認し、すべて矛盾なく一意に解決した場合のみ`RESOLVED`。一致するハッシュがあっても必須参照が欠落・矛盾・非一意なら、人間向け参照診断として`AMBIGUOUS`とし、根本のエラーを併記する。
4. **暗黙の修復は禁止する。** これらの状態はハッシュ書換え、Score付替え、未知データ削除、保存・演奏成功の認定を許可しない。再関連付けは別の明示的に権限を得た編集であり、確定するまで元のScoreとProfileを保持する。

ハッシュ一致のScoreが解析不能、または必須Core制約に違反する場合は**Score形式検証エラー**を明示し、参照が整合していると装ったり、同名の別Scoreへ自動で変更したりしない。4状態によって前提となる形式エラーを隠さない。この案は真正性・権限・機器安全・分散合意を保証しない。**R04/R11/R13/R14およびD01〜D03は未承認。**

---

> **Historical editorial snapshot: Draft 0.64 (unratified); D01–D05 pending.**


## Draft 0.63 — 関連ProfileとScoreの参照解決を行う判定手順（未採択の規範明確化案）

この手順は、与えられた関連Profileを入手済みのScoreバイト列に対して解釈できるかを判断するものである。JSON Schemaを変更せず、ネットワーク取得や実行をホストへ義務付けない。

1. Profileの版に応じて**必須の参照ハッシュおよび識別子**を読む。Distributed 0.2はルートの`scoreSha256`、Production 0.2は`score.sha256`を使用する。必須ハッシュが欠落・不正、または未対応の版である場合は`MISSING`ではなく、**不正な／未対応のProfile**として4状態の対象外とする。
2. 対象の参照に対し、**明示的に渡された、またはローカルでアクセスが許可されたScoreの元バイト列**のみを候補にする。ファイル名、タイトル、パス、Track名、最新版による推測でハッシュを代替しない。ネットワークから暗黙に取得しない。
3. JSONの再シリアライズ前に、**元のバイト列**のSHA-256を計算する。同じバイト列の複数ファイルは1つのバイト同一性として扱う。ハッシュ一致はこの判定におけるバイト同一性の根拠であり、著作者・真正性の証明ではない。
4. 次の優先順位で判定する。
   - 元Scoreの候補バイト列が全くない：**MISSING**。
   - 一致するバイト同一性が1つあり、Scoreの識別子・改訂、参照Track、および必要なPlan／Visit／範囲が規範Profileに従って解決する：**RESOLVED**。
   - ハッシュ一致の候補はあるが、必須の参照先が欠落・矛盾・一意に特定できない：意味上の参照は**AMBIGUOUS**。ハッシュ一致だけでRESOLVEDとはしない。
   - 候補は存在するが一致するハッシュが1つもない：**MISMATCH**。不一致候補が複数あっても、それだけでAMBIGUOUSにしない。
   - 検査後も相異なるハッシュ一致バイト同一性や矛盾する参照解決が残る：**AMBIGUOUS**。恣意的に1件を選ばない。通常のSHA-256同一性の前提では前者は例外的であり、観測済みと主張しない。
5. 関連Profileの参照が整合していると表明できるのは**RESOLVED**のみである。それ以外ではハッシュや識別子を暗黙に書き換えない。明示的な再関連付けは別の権限付き編集であり、必須参照を見直し、Profileが要求する場合は新しい改訂として保存する。未確定または失敗した場合、旧Profileと旧Scoreを維持する。

この優先順位により、通常のファイル探索における`MISMATCH`と`AMBIGUOUS`の混同を防ぐ。4状態は**人間向けの仕様解釈ラベル**であり、必須のJSON列挙値、標準エラーコード、一般的な信頼モデル、動作検証の結果を意味しない。R04/R11/R13/R14およびD01〜D03の採択待ちである。

---

> **Historical editorial snapshot: Draft 0.62 (unratified).** Companion binding resolution states clarified; D01–D05 pending. Runtime tests excluded, not passed.


## Draft 0.62 — Scoreと関連Profileの参照解決状態（未採択の規範案）

Distributed／Productionの関連Profileを開く際、参照元Scoreのハッシュに対して、**RESOLVED**（元Scoreの正確なバイト列が存在しダイジェスト一致）、**MISSING**（元Scoreの実体が存在しない）、**MISMATCH**（候補は存在するがダイジェスト不一致）、**AMBIGUOUS**（候補または同一性が複数あり意図した参照を特定できない）を区別することを推奨する。表示名・ファイルパス・音楽的に等価な書き出しだけではRESOLVEDと判定しない。同一バイト列の複数コピーは同一のバイト同一性であり、曖昧さには該当しない。

RESOLVED以外の状態で最新Scoreやトラック名から参照を**暗黙に付け替えてはならない**。参照未解決のProfileを読み取り専用表示することはできるが、再関連付けはTrack／Plan／Visit／範囲の参照確認を伴う明示的な操作とする。必要な参照が解決していないセットを完全な無損失保存と主張してはならない。これはR04/R11/R13/R14およびD01–D03向けの**未採択案**であり、新しいJSONフィールド、診断メッセージの標準書式、ネットワーク取得許可、実装の動作検証結果を追加するものではない。

---

## Draft 0.61 — 旧Scoreの保持と障害復旧の境界（提案・未承認）

**依存先の保持：** 旧Scoreの正確なバイト列のハッシュを参照するProfileが整合性を維持できるのは、対応する旧Scoreのバイト列も引き続き取得できる場合に限る。Profileだけの保持では十分ではない。新Scoreと旧Scoreを参照する未変更Profileの組を「新バージョンの整合した一式」と表示してはならない。安全な結果は、(i)旧Scoreと旧Profileを対応付けて保持する、(ii)参照先を確認したうえで選択したProfileを明示的に再関連付けする、(iii)参照未解決・分離状態を報告して無損失の一式と主張しない、のいずれかとする。

**部分的な保存失敗：** 一時ファイルへの出力は、それだけではアトミックなトランザクションではない。クラッシュ、リネーム失敗、権限不足、通信中断などでは、実際に確定したScore/Profileのバイト列と未確定・参照未解決のものを区別し、状態が不明なら成功とみなさない。旧Scoreを黙って破棄せず、未確認のハッシュ更新も行わない。ManifestやUIの表示はアトミックな保存の証明ではない。

**新しいJSONプロパティの追加ではない：** 保存場所、確定処理、バックアップ・復旧画面の詳細は実装責任とする。本節はファイルシステムAPIを定義せず、相互運用上の結果を提案する。DistributedとProduction双方に適用する。R04/R11/R13/R14およびD01〜D03の採択は保留中である。

---

## Draft 0.60 — 楽曲編集後の関連Profileのトランザクション的な再関連付け（未採択案）

楽曲の意味が同じでも、書き出したScoreの**元バイト列**が変われば参照先の同一性は変わります。以下は編集ツール向けの提案手順であり、OSTFの新しいJSON命令やファイルシステムの原子的更新を要求するものではありません。

1. 元Scoreのバイト列とハッシュ、参照元のDistributed／Production Profileを、明示的な新Scoreの書き出しが確定するまで変更せず保持する。参照不明のProfileも個別に記録する。
2. 新Scoreの実際の書き出しバイト列からハッシュを算出する。パース後のオブジェクト、空白の正規化、音楽的同等性、Manifestの値で代用しない。
3. 各Profileを「元Scoreを引き続き参照」「新Scoreへ明示的に再関連付け」「不明・未解決」に分類し、利用者が選んでいないものを暗黙に再関連付けしない。トラック名の一致だけで判断しない。
4. 再関連付けするProfileについて、元の参照ハッシュを確認し、新Score上で参照ID・範囲が解決できることを確認する。解決不能ならProfileを変更せず、具体的な不整合を報告する。イベント、オートメーション、歌唱情報を黙って削除しない。
5. 変更対象は確定まで別の出力先へ書き出す。全ファイル一括成功を約束する実装だけが一括ロールバック責任を負う。OSTF自体はファイル／ZIP／ネットワークの原子的トランザクションを提供しない。
6. 新Scoreのハッシュ、Profileごとの判断、未知データの保持、欠落、Asset不足を報告する。一括処理できない場合は元Profileを元Scoreに紐付けたままScoreだけ出力するか、出力を中止する。未解決の組を無損失・整合済みと表明しない。

Sessionでのイベント確定はScoreの変更承認ではなく、Productionのミキサー設定もScoreのMIDI CCを上書きしません。未知データの保持はその内容の解釈を意味しません。再関連付けはプラグイン／ネットワーク／ロボット実行権限を付与しません。R04/R11/R13/R14およびD01〜D03の**未採択**規範候補であり、JSONフィールドの追加はありません。

---

## Draft 0.56 — 操作別の保持責任と明示的な再関連付け（未採択案）

**読込解析・データ保持・編集・実行・音響再現**は異なる能力です。以下の「しなければならない」はD01〜D03での正式採択を前提とした**規範案**であり、版別JSON Schemaには新しい必須項目を追加しません。

- Scoreの読取専用インポートはSessionイベントを確定せず、Production状態を書き換えません。編集可能範囲だけを「対応」と表明できますが、書出しで未対応情報を削除・変換した場合は欠落を開示します。
- Scoreのバイト単位のハッシュが変化した場合、音楽的に同一でもProfileの関連付けを自動移行しません。明示的な確認と再関連付けが必要です。旧Scoreへの参照を保持する選択もできます。
- Sessionのイベント受理・確定は発音、ロボット動作、オーディオ生成の証拠ではありません。同様にProductionのプラグイン記述子は実行可能なプラグインが存在する証拠ではありません。
- URI・ハッシュ・メタデータが残っていても、実際の外部Assetのバイト列がない場合は欠落として申告します。Mixer/Automationを再現するためにScoreのノート・MIDIイベントを暗黙に改変してはいけません。
- 情報欠落の報告には対象のファミリーとバージョン、操作、影響範囲・外部参照、保持／変換／省略／利用不可の区別を含めることを推奨します。これは**OSTF本体外の報告方式**であり、新規の直列化項目ではありません。

必要なデータを保持も欠落申告もできない場合は「完全互換」を主張せず、対応操作の範囲を限定します。詳細は`CONFORMANCE.md`と`PUBLISHER_RELEASE_DECISIONS.md`のR14を参照してください。

# OSTF Production Session Profile 0.1 / 0.2 — 日本語規範仕様案（Draft 0.55）

> **現行編集版：Draft 0.59（未採択）。** 下記の古いDraft見出しは、累積した策定経緯を示し、現在のJSON版識別子を変更しません。6件の版別Schemaは不変です。公開判定の正本は [RELEASE_READINESS.md](RELEASE_READINESS.md) とし、D01〜D05はすべて承認待ちです。動作・独立実装検証は判定から除外していますが、完了とは扱いません。

## Draft 0.33 — Production保存・再関連付けの操作境界（未採択）

Productionの保存や新Scoreへの再関連付けは、Scoreの作曲編集やDistributed Sessionイベントの確定と独立した操作です。参照情報があるだけでプラグイン状態・外部Asset実体の完全保存を主張してはいけません。Profileの参照解決によってScore Note、Session状態、実際の音声素材を書き換えてはいけません。複数文書を扱う場合、変更／未保存／損失を文書ごとに開示します。詳細は`CONFORMANCE.md`。Schema変更はありません。

---

## Draft 0.32 — Score再保存後のProduction関連付け（未採択）

`score.sha256`はJSONの意味ではなく、**実際のScore原本バイト**に対応します。音楽情報に変更がなくてもJSONの再保存によりハッシュが変わる場合があります。その場合、既存Profileのハッシュだけを無断で書き換えることはできません。新しいScoreに対して明示的なProduction Profileの複製・再関連付けと、必要なTrack／Tick／Planの影響確認を行うか、集合全体の無損失保存の主張を取り下げて損失の範囲を報告します。URLや記述子だけではScore原本やAsset実体バイトが実際に供給された証拠になりません。`CONFORMANCE.md` Draft 0.32を参照。Schema変更はありません。

---

## Draft 0.29 — 制作ソフトの診断と保存能力の区別（未採択）

`docs/CONFORMANCE.md`と`docs/SPECIFICATION.ja.md`のDraft 0.29診断カテゴリー案を参照。プラグイン状態のURI/ハッシュのみを保持することと実体バイトの保持、未対応Sidechainの意味解釈と情報の無損失保持、Score単独Exportと制作環境全体の保持、旧Revisionへの参照と明示的再関連付けを分けて報告する。これは新しいProduction JSON項目ではなく、著作者採択待ちの説明規則。

---

## Draft 0.28 公開候補 — 保存対象と実体バイトの範囲

一回の書き出しで「Scoreのみ」「Scoreと実際に提供されたProduction Profile」「Profileに列挙されたが提供されていないAsset記述子」「実体バイトも含む全提供データ」を区別します。`docs/SPECIFICATION.ja.md`のDraft 0.28事例A〜Eと`docs/CONFORMANCE.md`を参照してください。**Profileが元から無い場合は損失と判定しませんが、入力として渡されたProfile/Asset実体を省略した書き出しは無損失の制作環境Exportとは表明できません。** スコア改訂時の再関連付けには明示的な確認が必要です。これらは採択待ちの編集案です。

---

## OSTF Production Session Profile 0.1.0 / 0.2.0 — 日本語仕様案

**策定状況：OSTF 4.3 Draft 0.29付属の未承認実験仕様。正式採用・公開権利は未確定。** 1〜11節は旧Profile 0.1の規範案、12節以降は0.2の追加案である。`profileVersion`ごとに別Schemaを用いる。

## 1. 目的と責任分界

本Profileは、OSTF 4.3の音楽的Coreとは独立して、第三者の音楽制作ソフトが使用する**ミキサー・Solo/Mute・音量・Pan・音源/エフェクトの順序・プラグイン識別子・状態参照・音声Bus/Send・Automation**を交換するための別冊JSON仕様である。

「Production Session」は**保存された制作環境**を意味する。遠隔AI/ロボットの参加者・演奏同期イベントを表す別冊「Distributed Session Profile 0.2」とは別物である。OSTF Coreも本Profileもソフトウェアではなく、プラグインを実行する機能は含まない。

規範的な構造は `schema/ostf-production-session-0.1.schema.json`、意味規則の詳述は英語版 `docs/PRODUCTION_SESSION_PROFILE.md` に置く。日本語版は意味を一致させることを目標とする出版候補であり、最終編集承認は未実施。

## 2. ファイル構造とScoreの固定

必須ルート項目：`profile:"OSTF-Production-Session"`、`profileVersion:"0.1.0"`、`score`、1件以上の`channels[]`。`devices[]`、`assets[]`、`automation[]`、`hostExtensions[]`は任意。

`score.formatVersion`は`4.3.0`。`score.sha256`は参照元`.ostf`の**UTF-8の元バイト列**に対する小文字64桁SHA-256である。JSONを整形・保存し直すとハッシュは変わる。`documentId`と`revisionId`を記す場合は元のCoreのDocument情報と一致しなければならない。`score.sourceUri`は情報上の参照であり、自動ダウンロード命令ではない。ハッシュ一致は著作者認証・実行権限を意味しない。

## 3. TrackとMixerの分離

`channels[].kind`は`track`、`bus`、`master`。`track`の場合だけCoreの`tracks[].id`を`trackId`で参照する。Coreの`track.enabled`、`clip.enabled`、`note.enabled`などは**音楽情報側の再生対象**であり、Production Profileの`mute`、`solo`とは別の正本である。`track.enabled=false`の曲を、Mixerの`mute=false`によって勝手に有効化してはならない。

各Channelは`id`、`kind`、`audioChannels`（1または2）、`gainDb`（-120〜+24、0がユニティ）、`pan`（-1左〜+1右）、`mute`、`solo`、`soloSafe`、順序付き`deviceIds[]`を持つ。未指定のGain/Mute等に隠れたデフォルト値を補完しない。`master`は全Profile中1つで、出力先は持たない。その他のChannelはBusまたはMasterへの`outputChannelId`を指定する。出力＋Sendの音声グラフは循環禁止、Sendの宛先はBusに限定する。

`mute=true`は原則としてそのChannelの音声出力とSendを抑止する意図を示す。`solo`はミキサー上のオーディション選択、`soloSafe`はSolo選択中に保持する意図を示す。特にBus Solo、Pre-fader Send、Sidechainの厳密な発音動作はホスト差があるため、音の完全な同一性は保証しない。対応できない場合は警告とデータ保持を行う。

CoreのMIDI CC7（Volume）、CC10（Pan）、CC11（Expression）、CC91/93（Effect Send）は**MIDI演奏/音源制御**であり、本Profileの音声ミキサーGain/Pan/Sendへ置き換えない。両者を同一の正本にしない。

## 4. 音源・エフェクトチェーン

Channelの`deviceIds[]`は並び順が処理順である。Device IDは全Profile内で独立・一意で、1つのDeviceは1つのChannelにのみ属する。`instrument`はTrack Channelの先頭に最大1件、`effect`と`utility`は後続の列として利用できる。Bus/MasterにはEffect/Utilityを置けるが、Instrumentは置かない。複数段のRack、並列FX、マルチインストゥルメントは0.1では未定義。

`devices[]`は`id`、`role`、`plugin`、`enabled`、`bypass`を必須とし、任意の`stateAssetId`と`onUnavailable`を持つ。`plugin.format`は`vst2/vst3/clap/au/aax/builtin/hostNative/other`、`plugin.pluginId`はその形式の識別名前空間内でのみ意味を持つ不透明な文字列である。表示名やVendor文字列だけで別のプラグインと同定しない。プラグインのファイルパス、ライセンス、実行可能コードをここで標準化しない。

`enabled=false`（Deviceスロットを不使用）と`bypass=true`（スロットの処理をバイパス）は区別する。これらはCore Trackのenabledと同一ではない。

## 5. プラグイン状態・代替処理

プラグイン独自のStateバイナリはJSONに直接埋めず、`assets[]`の`purpose:"pluginState"`と`stateAssetId`で参照する。Assetには`uri`、元バイト列SHA-256、任意のサイズ・MIMEを保持する。パスはZIPなどのパッケージ内でのPOSIX形式相対参照、または明示的な権限で利用するHTTPSを想定する。`file://`、親フォルダへの遡り、任意の自動外部アクセスを拒否する。OSTFはプラグインバイナリ仕様の互換性を保証しない。

未インストールのプラグインについて、`onUnavailable`に`reportAndPreserve`、`preserveAndBypass`、`preserveAndSilence`を指定できる。どれも*音色の完全復元*を保証しない。未知の状態参照と識別子を保ち、読み込み不能・バイパス・無音などの損失を通知する。同名別製品への自動置換は禁止。

## 6. Audio Bus / Send

Coreの`midi.buses[]`は論理MIDI出力先であり、Production ProfileのAudio Busとは別概念である。`channels[].outputChannelId`は音声出力先、`sends[]`は`id`、`targetChannelId`、`gainDb`、`preFader`、`enabled`で構成する。物理オーディオI/O、Sidechain、Feedback、Surround、並列Rackは0.1の対象外であり、欠落なく再現できない場合は警告する。

## 7. Automation

`automation[]`は対象Channel（Gain/Pan/Mute）またはDeviceパラメーターの時間系列を記述する。`points[]`は各`{atTick,value}`で、TickはScoreの**元のGlobal Tick**。Tickは非負の昇順・重複なし、同一ターゲットにつき1 Laneとする。繰り返しのVisitで同じ元区間が演奏される場合、元区間のAutomationを再適用し、以前のVisitの制御状態を無断継承しない。

- MuteのAutomationは`valueType:boolean`＋`interpolation:step`。
- Gainは-120〜+24 dB、Panは-1〜+1の数値。
- Device Parameterは識別子`parameterId`と0〜1の正規化数値。パラメーター名や尺度のホスト間の互換性は保証しない。
- 初回Point以前は静的なChannel/Device値、最終Point後は最後の値を保持する。数値Laneは`linear`または`step`。SoloのAutomationはv0.1では定義しない。
- AutomationはMIDI CCやopaque Plugin Stateを自動的に書き換えない。該当パラメーターの再生時値を決めるのみ。

## 8. サードパーティー独自拡張

`hostExtensions[]`は`namespace`、任意の`version`、非実行JSONの`data`からなる。独自ソフトのWindow配置、製品固有機能、ホストの設定等を記述できるが、Coreや標準Mixerフィールドの正本を密かに上書きしてはいけない。非破壊保存を宣言するソフトは未知の標準/独自フィールドを保持する。保存できなければ明示的に損失を報告する。

## 9. 携帯用の配布・公開

`score.ostf`、`production.ostfprod.json`、`assets/…`をZIPにまとめる運用は推奨例だが、OSTFの必須拡張子・公式パッケージ標準ではない。Coreだけを読み取るアプリはProfileを実装せずに利用できる。Web APIはScore JSONまたはProfile JSONを別々に提供できるが、HTTP認証/プラグイン実行権限はOSTF規格外である。

## 10. 適合性と公開判断

Profile 0.1のSchema・参照規則に対応するReader、Writer、Device Adapter等の適合宣言は機能別に行う。Schemaに合格してもプラグイン音質の一致・状態復元・DAW互換性を保証しない。演奏できないDevice、欠落Asset、出力/Sendのループ、未知Track、無効なAutomation、CoreとProfileのScore SHA不一致について、エラーと損失警告を区別する。

付属の`tools/validate_production_profile.py`は編集用の構造・部分的意味チェックであり、VST3/CLAP、DAW、フィジカルAI、WANの実行テストではない。ユーザー指定によりこれら実機/独立検証を公開判定条件から除外するが、検証済みとは記載しない。

## 11. 既存規格との関係

DAWprojectは音声Region、Automation、Mixer、デバイスStateをより深く交換する既存規格であり、実装上の重要な参考となる。本Profileの導入はDAWprojectを廃止・代替するものではない。相互変換では再現不能な項目を明示する。関連資料： https://github.com/bitwig/dawproject/blob/main/Project.xsd 。

## 12. Production Session Profile 0.2の位置付け

Profile 0.2.0は`profile:"OSTF-Production-Session"`と`profileVersion:"0.2.0"`を持つ**独立した制作環境JSON**であり、構造の正本は`schema/ostf-production-session-0.2.schema.json`である。従来の0.1は別バージョンとして保持し、そのScore固定・Mixer・プラグインチェーン・Bus/Send・Automation・非実行拡張の意味規則を継承する。0.1の値を推測して変換してはならない。変更されるのは制作Profileのみで、音楽Core 4.3、元の4.2、遠隔演奏用Distributed Session Profile 0.2は変更しない。

新規に、①Coreに存在しない録音・ミックス専用の`audioTrack`、②音声ファイルを参照する`audioRegions[]`、③別チャンネルからエフェクトのサイドチェーン入力へ送る`sidechainConnections[]`を追加する。これらの要素はすべて任意である。対象範囲はモノ/ステレオ、直列プラグインチェーン、固定素材と簡易伸縮、循環しない信号依存関係に限定する。音声録音機器、プラグインのDSPアルゴリズム、マルチポイントWarp、複数TakeのComp、並列Rack、サラウンド、PDCなどはまだ標準化しない。非対応項目はLoss報告を要する。

## 13. 録音専用トラックとScoreの関係

`channels[].kind:"audioTrack"`はProfile専用チャンネルであり、Core `tracks[]`の要素ではないため`trackId`を**持たない**。既存の`kind:"track"`のみ、対応するCore Track IDを`trackId`に必須とする。`bus`/`master`にも`trackId`を付けない。Audio Regionは`track`または`audioTrack`のみに配置し、Bus/Masterを音声Clipの所属先とみなさない。

同一`track`チャンネル上にMIDI InstrumentとAudio Regionが存在してもよい。MIDI音源の出力とRegionの音声は同じ音声チャンネルのエフェクト処理入口で合成する。これはScore NoteやClipの追加、再生成ではない。複数Regionの重なりは加算されるが、暗黙の音量正規化やCrossfadeを行わない。Core `track.enabled`とProduction Channel `mute/solo`、Region `mute`はそれぞれ別の正本である。

## 14. Audio Assetとフレーム

`assets[].purpose:"audioSource"`には、元のエンコード済みファイルのSHA-256、`uri`、`mediaType`、`sampleRateHz`、`frameCount`、`audioChannels`を必須とする。`frameCount`はファイルをデコードした音声の**時間フレーム数**であり、ステレオでも左右のサンプル数の合計ではない。`sampleRateHz`はそのフレームの秒あたりの数。0.2のポータブル範囲は1/2チャンネルに限定し、暗黙のアップミックスやダウンミックスを行わない。実際に取得したAssetバイトのSHAが違う、デコーダで読み取れない、申告したフレーム数などと違う場合には、正確な復元を主張せずエラーまたは明示的な損失を報告する。

URIは自動ダウンロード命令・ファイル操作権限・著作権許諾ではない。安全な相対パスおよび明示的な許可を得たHTTPSのみを使う。Plugin Stateのデータと音源のAssetは目的が異なる。

## 15. Audio Regionの時間・伸縮

各`audioRegions[]`は一意の`id`、`channelId`、`sourceAssetId`、元OSTF ScoreのグローバルTickによる`startTick`と正の`durationTicks`、非負の`sourceStartFrame`と正の`sourceFrameCount`、`playbackMode`、`gainDb`、`mute`を持つ。対象は半開区間`[startTick,startTick+durationTicks)`。`sourceStartFrame+sourceFrameCount`はAssetの全`frameCount`以下とする。

`playbackMode:"native"`では、開始Tickと開始Frameを対応付け、OSTFの`ppq`および有効なTempo変更を積算して求めた**経過秒数**に基づき、宣言された`sampleRateHz`で元音声を進める。指定Frameの終端またはRegionの終端で停止し、余ったRegion時間は無音になる。暗黙のループやタイムストレッチはしない。`pitchPolicy`は指定してはならない。Tempoが未定義なら推測してサンプル正確な復元を主張してはならない。

`playbackMode:"fit"`では、元OSTFのTick上の位置を指定されたSource Frame区間に等比対応させる。概念式は`sourceStartFrame + sourceFrameCount × ((currentTick-startTick)/durationTicks)`。`pitchPolicy`を必須とし、`preserve`は元の音高維持の意図、`followRate`は再生速度に従う音高変化を意味する。実際の伸縮・リサンプリングアルゴリズムや小数Frameの丸めはホスト依存であり、同一波形を保証しない。サンプル復元不能ならProfileの値を保持して警告する。

Region `gainDb`は音声リージョンの段階で適用する音量、`mute`はRegion固有の発音停止であり、Channel MuteやCore Track enabledと置き換えない。

## 16. Fadeと繰り返し・切断

`fadeInTicks`と`fadeOutTicks`は省略時0であり、和が`durationTicks`を超えてはならない。Fadeは**振幅で線形**。Fade-inの開始は振幅ゼロ、指定長で通常Gainに到達する。Fade-outはRegion末尾の指定長で開始し、終端でゼロへ向かう。複数Regionの交差部分に自動Crossfadeを生成しない。

Performance Planが元のSource範囲の一部を選ぶ場合、Regionとの交差部分だけがVisitへ投影される。切断時にRegionのID、元Source Frameとの時間対応、Fadeの相対位置をリセットせず、元座標で解釈する。同じ範囲を参照する複数Visitには同じRegionが出現しうるが、元のCore NoteやProduction Regionを勝手に書き換えない。Coreの`realization:"open"`は録音許可でもセッション確定フレーズの採用許可でもない。ProductionをScoreだけに書き出す場合は音声素材の損失を報告する。

## 17. Sidechain入力

`sidechainConnections[]`は可聴のBus/Sendと異なる**検出用入力**である。必須項目は`id`、`sourceChannelId`、`targetDeviceId`、`targetPortId`、`tapPoint`、`followMute`、`gainDb`、`enabled`。送信元はMaster以外、宛先は別Channelに所属する`effect` Device。1個のPlugin Portには1つのSourceだけを指定できる。複数入力をまとめたい場合はBusで明示的にミックスする。

`tapPoint:"preFader"`は直列Device処理後・Channel Gain/Pan前、`postFader`はGain/Pan後から検出用信号を採る。`followMute:true`では元ChannelのMuteによってSidechain信号も抑止し、falseでは可聴出力がMuteでもSidechain入力を残せる。`gainDb`はSidechainにのみ適用する。Plugin Port IDは不透明な識別子であり、実在のポートであることはHostが別途解決する。同名の入力へ自動変換しない。

Output、Send、SidechainによるChannel依存グラフ全体は**循環禁止**とする。自己Sidechain、暗黙のFeedback、PDC・Lookahead、DSPの動作や音質は標準化しない。Deviceが不在でも接続の意味情報は保持する。

## 18. バージョン移行・情報損失・適合性

正しい0.1文書を0.2へ移行する場合は、0.2 Schemaと意味規則のチェック後に`profileVersion`のみを書き換えてよい。新しいAudio RegionやSidechainを推測して生成しない。0.2から0.1への無損失変換は`audioTrack`、`audioRegions`、`sidechainConnections`、`audioSource` Assetなど0.2専用内容が一切ない場合に限り可能とする。0.2専用情報がある場合は、損失項目を明示して許容を得るか保存を拒否する。

本Profileは音声を演奏・生成するソフトではない。Schemaの正当性と実機・プラグイン・サンプル波形の同一性は別の条件である。ローカルの`validate_production_profile.py`は0.1/0.2の選択的な静的確認を補助するだけで、DAWやプラグインの独立相互運用テストではない。正式な出版には著作者による規範採択、英日文書整合、権利とライセンスの承認が必要で、いずれも現時点では未完了である。

## 19. 対象・対象外とサンプル

0.2では録音専用トラック、モノ/ステレオAudio Region、トリミング、簡易Fade、`native/fit`の伸縮意図、Sidechain入力を表現する。DAWprojectレベルのあらゆるオーディオ編集機能、複数TakeのComp、マルチポイントWarp、サラウンド、並列Rack、正確なプラグインState復元、物理録音I/Oやネットワーク演奏は対象外である。補足の違いは本文英語版第19節の役割表に従う。

`examples/production/03-audio-regions-sidechain-02.json`は元のScoreをSHA固定し、録音専用Channel、WAVテスト音源を2つのモードで参照するRegion、架空のBass CompressorへのSidechainを示す。`assets/example-audio.wav`はこのDraftのために生成した220Hzの合成音であり、商用ソフトの録音やプリセットではない。旧0.1例は変更せずに保持する。


## 21. Production Profile 0.2のAutomation対象拡張（Draft 0.15）

この追補は未公開の**Production Profile 0.2.0案だけ**を変更する。OSTF 4.3音楽Core、継承4.2、遠隔Distributed Session Profile 0.2、歴史的なProduction Profile 0.1のSchemaは変更しない。0.2はまだ正式公開されていないため、今回の追加を確定公開済みの0.2へ黙って導入したものとして扱わない。

旧来の`channel`（Mixer Gain/Pan/Mute）と`device`（プラグイン固有の0〜1正規化数値Parameter）に加え、`automation[].target`に以下の候補を追加する。

| Target kind | 参照ID | 操作対象 | 値型 |
|---|---|---|---|
| `send` | `sendId` | `gainDb`, `enabled` | 数値dB、真偽値 |
| `audioRegion` | `audioRegionId` | `gainDb`, `mute` | 数値dB、真偽値 |
| `deviceControl` | `deviceId` | `enabled`, `bypass` | 真偽値 |

Send IDはProfile全体の全Channelを通じて一意でなければならず、各参照は対象の実在を要求する。`deviceControl`の有効/Bypassはプラグイン内部のパラメータとは区別し、`kind:"device"`の`parameterId`として自動変換してはならない。単一の型付きTargetには1つのAutomation Laneだけを持てる。Laneを作成してもSend、Region、Deviceの実体を生成しない。

Automationの位置は従来どおり**元のOSTF楽曲の絶対Tick**である。Tickは非負かつ厳密昇順、同一Tickの重複は禁止。真偽値のLaneは`boolean`＋`step`が必須。数値のLaneは`number`であり、Panは-1〜+1、音量系dBは-120〜+24、プラグイン固有値は0〜1。新しいSend/Regionの音量にプラグイン固有の0〜1スケールを適用してはならない。

最初の点より前は対象オブジェクトの明示された静的値を適用し、その後は最後の有効点を保持する。数値`linear`は隣接点の区間内のみ補間する。プラグイン内部の最初の静的値が不明な場合、その区間の値は未規定であり勝手に補完しない。RegionへのAutomationが存在しても、もとのRegionの半開区間外では発音せず、Regionを延長しない。繰返しVisitで再び区間を利用するときは**元のScore Tickから状態を再解決**し、前のVisitの状態を持ち越さない。RegionのMute/GainはFade、Trimなどとは別の操作であり、元データを書き換えない。

`send.enabled:false`はSendの発音を止め、`audioRegion.mute:true`はそのRegionを消音する。Deviceの`enabled:false`は処理Slotを無効、Slot有効中の`bypass:true`は処理をバイパスする意図である。ただし実際のDSPと音源状態の等価性は保証しない。AutomationはCoreのTrack.enabled、MIDI CC、Soloの操作、プラグイン実行権限ではない。非対応Hostは全Laneの保存と不足機能の開示を行い、未対応の値を破棄して「損失なし」と呼んではならない。`send`/`audioRegion`/`deviceControl` Laneがある0.2から0.1へのダウングレードは情報損失を伴う。

`examples/production/03-audio-regions-sidechain-02.json`に6種類の新ターゲット操作を追加した。これらは構造・意味の例示であり、実際にプラグインを制御できたことの証拠ではない。英語版21節を詳細な規範候補とし、公開前に日英の最終編集承認が必要である。


## 22. ポータブルなMixer/Solo/Solo Safe・音源権威の境界（Draft 0.16候補）

この節は、未公開の**Production Profile 0.2.0候補**に対し、第三者製HostがSolo/Muteをどう解釈するかの**演奏源選択の共通基準**を提案する。旧Profile 0.1のSchemaと既存データは変更しない。これはDSP、Pan Law、遅延補正、音質まで統一する規則ではなく、いずれの素材が音声経路に参加し得るかを明示する規則である。

### 22.1 音源の種類と正本

- `channel.kind:"track"`と`"audioTrack"`を**source channel**とする。`"bus"`は受信/分配する経路、`"master"`は最終出力であり、いずれもそれ自体では新しい楽曲音源を生成しない。
- Scoreに紐付く`"track"`において、Coreの`track.enabled`、`clip.enabled`、Note/MIDIは**Core由来の演奏**だけの参加可否を決める。同じProduction Channelに置いた独立の`audioRegion`まで自動消音してはならない。Region自身の位置・MuteとStudio Mixerは別々に適用する。
- `"audioTrack"`はCoreの`trackId`を持たない。Channelの存在だけで発音は生まれない。
- Channel Mute、Send enabled、Region Mute、Device enabled/bypass、Automationは異なる制御層である。`solo`/`soloSafe`はミキサーの試聴状態であって、楽曲Noteの変更やプラグイン起動権限ではない。MasterのSolo/SoloSafeは音源選択に関与しない。新規作成時はMasterの両方をfalseとすることを推奨するが、旧ファイルにある値を勝手に書き換えてはならない。

### 22.2 Solo中に選択する演奏源（Profile 0.2の提案規則）

1. `outputChannelId`と、**その元Score Tickで有効な**Send（`send.enabled`のAutomation適用後）の矢印で、出力グラフを作る。Sidechainはこのグラフに含めない。Muteによって接続情報を削除しない。
2. Master以外で`solo:true`のChannel集合を`S`とする。`S`が空ならすべての`track`/`audioTrack`源が選択される。
3. `S`が空でなければ、演奏源Channelは①自分がSolo、②自分がSoloSafe、③有効な出力/Send経路をたどってSolo中のBusへ到達できる、のいずれかで選択される。**SoloSafeのBusだけでは、それまで非選択だった他の演奏源を復活させない。**
4. 選択された演奏源の直接出力と有効なSendは、Mute/音源状態/後段の経路に従って利用可能となる。そのためBusをSoloしたとき、上流源のDry出力も選択対象になり得る。Wetのみを試聴するHostは、その差を開示して元のSolo情報を保持する。SoloSafeのBusは選択源の信号を通してよいが、非選択源を新規に選ぶ機能ではない。
5. Send EnabledのAutomationやVisit再入で到達関係が変わった場合、元Score Tickから選択状態を再計算し、前のVisitの選択を持ち越さない。0.2ではSoloとSoloSafeそのものは**静的な値でありAutomation対象外**である。

この共通規則に従わないDAWのBus Solo/試聴動作をそのまま実行することは許されるが、元データを保全し、結果の非互換性を表示して、等価再生を保証してはならない。

### 22.3 Mute・Send・Sidechain・処理順

- Score由来の演奏とProductionのAudio Regionは独立して参加判定し、そのChannel内で合成した後、順序付きDevice Chainへ送る。Coreの`track.enabled:false`は独立したProduction Audio RegionのMuteではない。
- ポータブルな信号順序を、**演奏入力→Device Chain→Pre-fader Tap→Gain/Pan→Post-fader Tap→出力/Send→Master**とする。`send.preFader:true`はPre-fader、falseはPost-faderから取る。Pan LawやDSPのビット単位の一致は規定しない。
- Channel MuteはSolo中でも優先し、Pre/Postに関係なく**可聴出力とSendの両方**を抑制する。Mute中のBusも同様。無効なSendは接続を抑制する。Deviceの`enabled`/`bypass`はChannel Muteとは別の状態。
- Sidechainは検出用経路でありSoloの選択対象にはならない。`followMute:true`ならソースChannelのMuteで検出信号を抑制し、falseならMute中も元信号を検出へ送ることができる。ただしfalseは、Soloで非選択の音源やCore側で無効のNote入力まで復活させない。Sidechainの`enabled:false`は常に検出入力を抑制する。Host独自のSoloとKey Listening規則の差は開示する。
- Masterは選択・有効な音声を受け取り、自身のGain/Pan/Muteを適用する最終経路である。MasterをSoloしても無効な音源は発音しない。

### 22.4 アセットパスの安全な解決

Production Profileの`asset.uri`が相対パスなら、Profile文書を含むディレクトリの**内部だけ**で解決する。`..`などの字面チェックだけでなく、シンボリックリンク経由で外部ファイルへ脱出する場合も拒否する。SHA-256の一致はファイル閲覧権限を与えない。HTTPS URLは情報として保持し、無断取得しない。付属Pythonチェッカーはこの基本的な境界判定を追加したが、完全なセキュリティ監査を実施したという意味ではない。

### 22.5 選択の例

| 状態 | 選択される源Channel | 備考 |
|---|---|---|
| Soloが存在しない | 全track/audioTrack源 | 実際の発音はMuteやCore/Region状態に従う |
| サンプル03のSax Solo・Reverb Bus SoloSafe | `sax-channel` | Reverb BusのSoloSafeだけでPianoのSendは復活しない |
| Reverb Bus Solo・有効Piano Send | `piano-channel` | Dryも選択され得る（Wet限定Hostとの違いに注意） |
| Reverb Bus Solo・Piano Send無効 | 当該Bus経由の選択源なし | Send Automationで選択が変化 |
| Sax Solo・Piano Channel SoloSafe | `sax-channel`, `piano-channel` | どちらもMuteで抑制可能 |

チェッカーの`--explain-audition --at-tick N`は、元Tick時点の静的な演奏源選択を表示する説明機能である。音声レンダリング・DAW互換検証・ロボット実機検証ではない。この追補で新しいJSONフィールドは追加せず、既存の6 SchemaはDraft 0.15から変更しない。**公開前に著作者の意味規則採用が必要である。**

## 23. Asset URIの厳密な解釈とScore/Productionの権威分離（Draft 0.17候補）

### 23.1 相対Asset URIの移植性と安全性

`assets[].uri`が相対URIである場合、OSの生パスではなく**URIパス**として解釈する。0.1と0.2共通の規範候補として、文字通りの`/`で空でない成分に分け、パーセントエスケープを成分ごとに**1回だけ**厳密なUTF-8として復号する。`.`/`..`、`%2F`/`%5C`のような隠れた区切り、`%252e`のように2度目の復号で意味が変わる残存`%`、不正なUTF-8、制御文字、前後の空白・末尾のピリオド、Windowsで予約された文字・`CON`や`NUL`等のデバイス名を禁止する。生の空白は使わず`%20`で符号化する（例：`assets/My%20Take.wav`はファイル`My Take.wav`）。

復号後はProduction Profile JSONのディレクトリ以下に解決し、シンボリックリンクを含めて実際の解決先がディレクトリ外なら拒否する。URI文字列自体はJSONのデータとして保持する。アクセス権限の確認なしにファイルを読まず、外部HTTPSも自動取得しない。SHA-256は許可された取得後に元バイト列へ適用する。Unicode正規化や2度目のURI復号を行ってはならない。復元不能なら原文を保持して理由を報告する。この規則は安全監査が完了したという意味ではない。

具体例：`assets/%2e%2e/private.bin`、`assets/%252e%252e/private.bin`、`assets/%2Fetc.bin`、`assets/note%FF.wav`、`assets/CON.txt`は拒否対象。URI文字列以外のSchema項目は追加しない。

### 23.2 Performance Plan `realization` とAudio Regionの関係

Core `performancePlans[].visits[].parts[].realization`（`fixed`/`open`/`silent`）は**Core由来の演奏**を規定し、同じScore Trackに紐付いたProduction Channel上の独立`audioRegions[]`を自動変更・消音しない。例えばギターのPlan Partを`silent`にしても、該当するSource Tickに置かれた録音Regionは、独自のRegion/Channel MuteやAutomationなどが許す限り再生候補のままである。Production専用の`audioTrack`も、同名というだけでCore Plan Partにはならない。

MIDIと録音素材を含む全体を消音したい場合は、Production Profile側でRegion/ChannelのMuteなどを**明示的に**指定する。逆にMixer MuteはCore Noteや`open`/`silent`という演奏意図を書き換えない。異なる動作をするホストは差分を開示し、元データを保持する。Visitの再出現でもこの権威分離を守る。

**現在は著作者の正式採択・日英最終編集前の規範候補である。** 本記述は実行・音声DSP・OS権限・ネットワーク・ロボット実機の検証結果ではない。

## 24. Performance Plan再入時のAudio RegionとAutomationの位置・状態規則（Draft 0.18候補）

### 24.1 Source TickとPerformance Tickを混同しない

未公開の**Production Session Profile 0.2.0案**に適用する規範候補であり、第7・15・16・21〜23節を補足する。**source Tick `t`**は元のOSTF楽曲の絶対Tick、**performance Tick `P`**は有限Performance PlanのVisitを展開した位置、実機/サンプルの時計はホストの責任である。元の半開区間`[S,E)`を演奏位置`Q`へ配置すると、選択中は`P=Q+(t-S)`となる。Visitを繰り返しても、元のRegion ID、Automationポイント、Scoreハッシュ、確定MIDIイベントは変更しない。

### 24.2 Regionの一部分だけを選択したとき

Regionの元範囲`[R,R+L)`とVisitの選択区間`[S,E)`の**半開区間の共通部分**`[max(S,R), min(E,R+L))`だけが対象である。VisitがRegionの途中から始まっても、元の`sourceStartFrame`へ巻き戻してはならず、元のsource Tickから対応するフレーム位置を計算する。後のVisitで同じ元区間を再度選択した場合は、その区間に対応する元の素材位置を再び利用し、前Visitの再生カーソルを継承しない。

- `playbackMode:"native"`では、source Tick `t`の理想連続フレーム位置は`sourceStartFrame + sampleRateHz × T(R,t)`とする。`T(R,t)`はRegion開始`R`から`t`まで**元の楽曲のテンポマップ**を積分した理想秒数で、テンポ一定の小区間ごとに`60 × deltaTicks/(ppq × bpm)`を足す。途中のsource区間がPerformance Planで省略されていても、素材内の開始フレームを求める際には**元のRegion開始からの経過**を用いる。この積分は、**展開後の演奏時間に省略区間を足すことではない**。選択された`sourceFrameCount`を超えたら無音とし、素材を自動ループ・先頭再生しない。
- `playbackMode:"fit"`では`sourceStartFrame + sourceFrameCount × (t-R)/L`を利用する。Visitの途中開始・区間切断でも元のRegion-local Tickによる位置を維持する。小数フレームの丸め、タイムストレッチ、ピッチ保持のDSPはホスト依存であり、音声データの同一性を保証しない。
- `fadeInTicks`/`fadeOutTicks`は元のRegion境界を基準に評価する。Visitの切断位置で新しいFadeを暗黙に作らない。カットによって不連続・クリックが生じ得るが、ホスト独自のCrossfade/平滑化を用いた場合は等価再生とは主張せず、その近似を開示する。
- **MIDI Noteの元区間外の発音開始を作り直さない規則とは区別する**。Regionは途中位置の音声フレームを参照できるが、確定Noteは元区間にNote Onがなければ新しいNote Onを生成しない。過去のMIDI CCやProgram Changeの状態をこのProduction規則で復元するわけでもない。

### 24.3 Visit開始時のAutomationは元のsource Tickから解決する

Automation Laneの有効値は、現在の**元のsource Tick `t`**から全ポイントを用いて計算する。現在のVisitが省略した元区間にあるポイントも、状態評価に必要なら参照する（省略区間を演奏イベントとして再出力するわけではない）。ポイントと同じTickでは当該ポイント値が有効。`step`は直近ポイントを保持し、`linear`は隣接する数値ポイントのsource Tick比で補間し、最後のポイント以後は値を保持する。最初のポイント前はChannel/Send/Region/DeviceControlに明示された静的値を使う。一方、`kind:"device"`のプラグイン数値Parameterは**型付きの静的初期値がProfileにない**ため、最初のポイント前はプラグインStateを解釈できない限り**未解決**である。0、0.5、最初のポイント値、前Visitの最終値を勝手に採用しない。

元のsource Tickが切断やVisit再入で巻き戻った場合、Sendの`enabled`、Channel/RegionのMute、Deviceのenabled/bypass、Gainなど、すべて**新しいsource Tickで再評価**する。**前VisitのAutomation状態は持ち越さない**。RegionのAutomationは元のRegion範囲外に新しい音声を作らない。これは元のsource Tickに対する状態関数の評価であり、選択した区間の前にあるCore MIDI CC/Programイベントを新たに送る処理ではない。Profile 0.2にはVisitごとのMixer Automation上書きはない。同じ元Tickなら、異なるVisitでも同じAutomation値となる。

### 24.4 計算例（音声再生検証ではない）

PPQ=960、BPM=120、sampleRateHz=48000、Region開始Tick=0、開始フレーム0なら、source Tick 960は`48000 × (60/120)=24000`フレーム相当である。`[960,1920)`から始まるVisitでもフレーム0から再生しない。`fit`のRegionが`R=1920`、`L=1920`、`sourceStartFrame=0`、`sourceFrameCount=11025`なら、元Tick 2880で理想フレーム位置は5512.5である。実際の小数フレームの取り扱いはホスト依存。

付属`03-audio-regions-sidechain-02.json`では、`reverb-send-on-automation`にsource Tick 7680で`enabled:false`がある。VisitがそのTick以降の元区間に途中から入った場合でも、**当該ポイントを経過して演奏していなくても**Sendは無効と解釈する。次のVisitで元Tick 0へ戻れば`enabled:true`を再評価する。また`room-clip-native`は44100Hzで11025フレーム＝0.25秒しか素材がない。BPM=120・PPQ=960では元Tick 480で素材が尽きるため、Region自体が960 Tickでも`[480,960)`からの選択で先頭へ戻らない。

### 24.5 未解決情報・互換性・公開状態

Nativeの素材位置決定に必要な元テンポが不明、またはプラグインStateから最初のAutomationポイントより前の数値が復元できない場合は、元のデータを保持して未解決を報告し、確定した音声再現を主張してはならない。診断コード案：`E-PRODUCTION-NATIVE-TEMPO-UNRESOLVED`、`W-PRODUCTION-DEVICE-BASELINE-UNKNOWN`、`W-PRODUCTION-CUT-DISCONTINUITY`、`W-PRODUCTION-VISIT-LOCAL-MIX-UNREPRESENTABLE`。ホスト独自のVisit別Automation、Fade、演奏状態持ち越しによる差異も情報損失・近似として開示する。

**Draft 0.18ではSchemaの追加・変更、Profile版番号の変更は行わない。** これらは公開前の規範候補であり、著作者による正式採用、日英最終編集、ライセンス承認が必要。独立パーサー・DAW/DSP・WAN・ロボット実機の検証は行ったとは主張しない。

## 25. Production ProfileとDistributed Session Profileを同じOSTFへ関連付ける規則（Draft 0.19候補）

### 25.1 三つの文書を明示的に関連付ける

本節は、独立した**OSTF Production Session Profile 0.1/0.2**と**Distributed Session Profile 0.2**のSnapshot/Eventが、同じ**OSTF 4.3楽曲の実体バイト列**を参照するときだけ適用する、未公開の意味規則案である。新しいJSONフィールド・Schema・Profileバージョンは追加しない。Studio専用ソフトがDistributed Profileを必要とすることも、遠隔SessionがProduction Profileを必要とすることもない。

Productionの`score.sha256`とDistributedルートの`scoreSha256`は、**同じOSTF原本のUTF-8実体バイト列**に対するSHA-256である。三文書を同一Scoreとして関連付ける場合、両方の宣言値と原本から計算した値が**すべて一致しなければならない**。IDやRevision名だけが同じでも一致の代用にはならない。JSONの整形・再直列化、Web APIからの自動取得、原本の暗黙書換えによってハッシュを無理に一致させない。ハッシュは署名・許諾・本人確認・セッション参加権限を意味しない。Production `score.sourceUri`は参考URIであり、読み込んだだけで取得権限を与えない。Production Profileだけを編集しても、元OSTFのSHA-256は変わらない。

Productionの`score.documentId`/`score.revisionId`があるときは、Distributedの必須`documentId`/`revisionId`およびOSTF原本の`document.id`/`document.revisionId`と一致する必要がある。Productionで未指定なら推測しない。Distributedの必須`performancePlanId`は、原本Scoreの`performancePlans[]`に存在するIDを明示的に指す。原本を確認できない場合、2つのProfileが宣言するハッシュの文字列一致は**主張の整合**であり、楽曲実体・Plan・Track参照を検証できたとは表示できない。

### 25.2 Trackの一致から音声出力やロボット制御を推測しない

Productionの`channels[kind:"track"].trackId`とDistributedの`participants[].assignedTrackIds`/`targetTrackId`はいずれもCoreの`tracks[].id`を参照する。しかし同じIDでも、Remote Participantを特定のStudio Channel・Plugin・物理出力・ロボット関節へ割り当てたことには**ならない**。Production ChannelがないCore TrackはMuteや参加不可を意味しない。Production専用`kind:"audioTrack"`はCore Trackではなく、名前の類似から遠隔参加者や`open` Partへ暗黙割当しない。

分散PlanのVisit/PositionはScore由来演奏の範囲を指定する。独立したProduction Audio Region/Automationは第23～24節の元`source Tick`規則で解釈し、前VisitのMute等を持ち越さない。Core `realization:"silent"`は独立したStudio録音を自動Muteしない。遠隔`phraseCommitted`は明示された`open` Partの**セッション確定フレーズ**であり、元ScoreのNote、Production Automation/Audio Region/Device状態、プラグインの実行やロボット動作を自動変更しない。元Scoreを編集したら、新Revision/新ハッシュに基づきProfileとの関連付けを明示的にやり直す必要がある。

### 25.3 拒否条件と表示

任意の`OSTF 4.3 Cross-Profile Binding Reader`を名乗るアダプターは、Scoreハッシュの不一致、明示ID/Revisionの不一致、原本があるのに未解決のPlan/Track参照がある場合、**自動関連付けを拒否**し、両Profileの内容を変更せず保存する。独立した未関連の文書として表示することはできる。原本がなく検証できない場合、`W-CROSS-PROFILE-SCORE-UNAVAILABLE`などで未確認を明示する。関連付け成功を、音声の一致、遠隔同期、MIDI状態復元、プラグイン実行、安全なロボット制御の証拠としてはならない。

候補の診断コード：`E-CROSS-PROFILE-SCORE-HASH`、`E-CROSS-PROFILE-DOCUMENT`、`E-CROSS-PROFILE-REVISION`、`E-CROSS-PROFILE-PLAN`、`E-CROSS-PROFILE-TRACK`、`W-CROSS-PROFILE-SCORE-UNAVAILABLE`、`W-CROSS-PROFILE-ROUTING-UNDEFINED`。これはSchemaの新しいenumではない。

### 25.4 既存の3つのサンプルを用いた例

`examples/22-pinned-session-aaba.ostf`を原本とし、`examples/production/03-audio-regions-sidechain-02.json`と`examples/session/03-snapshot-02.json`を関連付けられる。いずれも原本のハッシュと文書ID/Revisionが一致し、Distributedの`performancePlanId:"form"`は元のPlanを参照する。一方、Productionの`bass-channel`と遠隔Participantの`bass`担当が同じScore Trackを参照していても、Remoteロボットの音声をそのStudio Channelに流すことは指示されていない。

**公開状態：Draft 0.19の意味規則候補。** Schema・例のJSONは変更しない。独立実装によるDAW/プラグイン/DSP/遠隔ロボット動作や公開承認の証拠ではなく、従来の著作者決定事項は未解決のままである。

## 26. Score改訂後の明示的な再関連付け（Draft 0.20・未採用の規範案）

### 26.1 制作環境の引継ぎと遠隔Sessionの引継ぎを混同しない

OSTF楽曲のJSONバイト列が変更された場合、意味が似ていても**以前とは別の固定されたScore実体**である。制作環境を記録するProduction Profile 0.1/0.2は、新しいScore改訂版に**明示的な再関連付け**を行える。一方、演奏中・停止後のDistributed Session Profile 0.2のセッションを**その場で別Scoreへ付け替えてはならない**。この候補規則は新規フィールド・Schema・通信方式を追加せず、既存の正本と権限境界を明確にするものである。Production `score.sha256`の文字列だけを書き換え、安全または無損失の引継ぎが完了したと宣言してはならない。

Note、Harmony、Tempo、Section、Track、Performance Planなどを編集した場合、新しいScoreの実体が必要になる。同じ作品の改訂と主張するなら、`document.id`を維持し、新しい`document.revisionId`を明示する。`document.id`が異なる場合は同一曲のRevisionではなく別作品への再割当である。Coreの文書メタデータは任意だが、IDまたはRevisionがないときに曲名・ハッシュだけから改訂系譜を証明してはならない。同じ `(document.id, document.revisionId)` や固定URLのまま別バイト列を公開してはならない。空白などのJSON整形だけの変更でも、原本バイトハッシュが変わるため再固定が必要である。

### 26.2 Production Profileを引き継ぐための必須確認

専用ソフトは、従来のScoreとProduction Profileを保存したまま、**新しいProduction Profileのコピー**を作成してよい。ただし以下をすべて明示的に扱うこと。旧データの削除は別途の著者指示が必要である。

1. 旧Production `score.sha256`が旧Scoreの**実体バイト列**と一致し、新Scoreのバイト列から新しいハッシュを計算できること。Productionに旧文書ID/Revisionが明示されていれば旧Scoreと一致させる。新コピーには新Scoreのハッシュを設定し、明示する場合は新文書ID/Revisionも更新する。旧IDを無条件でコピーしない。
2. 新ScoreのTrack IDをすべて解決すること。**同じTrack IDは同じ参照先の識別を意味するが、演奏内容や発音時刻まで同一とは限らない。** Trackの削除や付け替えには、著者承認の明示的な再割当、別Profileとしての保持、または情報損失を開示した変換が必要である。Channel名の一致だけから新Trackを生成したり、不正なTrack参照を含む新Profileを黙って保存してはならない。
3. **元Scoreのsource Tick**を使う`audioRegions[]`や`automation[].points[]`について、PPQ、Sections、Tempo/Meter、選択したPerformance Plansの差分を確認する。Tempoを変えれば`native`素材の元フレーム時刻に影響し、PPQや構成を変えればRegionの開始/長さ、Fade、Automationの音楽的な位置が変わりうる。Plan変更は同じsource TickでもVisitへの投影を変える。ハッシュ更新・Track名・小節ラベルだけを根拠に自動移動、伸縮、カット、直前Visitの値持越しを行ってはならない。
4. 不透明なプラグイン状態、音声Asset、独立Audio Region、Bus/Send、Device ID、`hostExtensions`は**Production側の正本**である。Scoreの更新を理由に自動上書き・実行してはならない。意図通りに再対応できない場合、著者による配置確認を求め、非破壊であれば旧Profileを保持する。損失変換なら、失う具体的なChannel/Region/Automation/Device IDと意味を報告する。

結果の状態を区別すること：**旧Scoreに固定されたまま**、**新Scoreへの再関連付け候補（要レビュー）**、**著者承認済みの新Score/新Productionコピー**。単に新ハッシュと同じTrack IDがあるだけで最後の状態を主張してはならない。プラグインの音質まで一致することは保証しない。

### 26.3 Distributed Sessionは新Scoreごとに新セッション

Distributed Profile 0.2は`documentId/revisionId/performancePlanId/scoreSha256`と受理済みイベント履歴に固定されている。Score Revisionが変わったら、**新しい`sessionId`**で遠隔セッションを開始すること。既存の`stateRevision`、`eventId`、確定`phraseCommitted`、Visit位置、共通時計位置、参加者割当を、新Scoreへ暗黙で移してはならない。旧イベント履歴は元Scoreと結び付いた記録として残る。フレーズを新セッションで再利用したい場合は、新しい識別子・明示的な著者の移行操作・必要な損失報告を伴う新規データにする。既存JSONを読み込んだことはロボット動作の認可ではない。

Web APIの`latest` URLやHTTP `ETag`が変わっても演奏中の元Scoreを切り替えない。参加者の名前、同じTrack ID、新しく表示された曲名は移行の承認とはみなさない。ハッシュは発信者認証やプラグインロード権限ではない。

### 26.4 読取専用の再関連付けプレビュー

付属`tools/validate_production_profile.py`にDraft 0.20の`--score OLD.ostf --rebind-target NEW.ostf`を追加する。旧・新原本のハッシュ/ID/Revision、Track参照、source時刻・Performance Planの変更可能性を**表示するだけ**である。結果は原則`REVIEW_REQUIRED`であり、プレビューが通っても自動変換・無損失証明・動作検証にはならない。目標Scoreが不正なら`BLOCKED`とし、既存ファイルを書き換えない。

診断名案：`E-REBIND-SCORE-INVALID`、`E-REBIND-IDENTITY`、`E-REBIND-REVISION-REUSE`、`E-REBIND-TRACK-UNRESOLVED`、`W-REBIND-SOURCE-TIME-CHANGED`、`W-REBIND-PLAN-CHANGED`、`W-REBIND-NEEDS-AUTHOR-REVIEW`、`W-DISTRIBUTED-NEW-SESSION-REQUIRED`。Schema enumを追加するものではない。

**状態：Draft 0.20の規範候補であり著作者未採用。** 4.3 Core、正式4.2継承Schema、別冊Distributed/ProductionのSchema、既存デモJSONは変更しない。著作者による意味規則の正式採用、日英仕様書とサンプルの最終承認、公開権利・ライセンス許諾が未完であり、検証を除外してもNO-GOを維持する。

## 27. データ保持・機能別対応の明示（Draft 0.21・未採用規範候補）

### 27.1 保存・解釈・実行を区別する

OSTF Score、Production Session Profile、Distributed Session Profileは**独立した文書と版番号**を持つ。JSONを失わず保持できること、音楽上の意味を解釈できること、プラグインを実際に動かして同じ音を出すこと、遠隔ロボットを制御できることは、すべて別の能力である。第三者製ソフトはこれらを混同して「完全対応」と称してはならない。Coreだけを読むViewerは別冊Profileを無視してもよいが、**受領した制作プロジェクト全体を無損失で再保存する**と明示するWriterは、別冊Profileと参照Assetを保持するか、欠落を個別に説明しなければならない。

### 27.2 参照Assetと再保存時の正本

無損失のデータ保存では、受領した文書の実体と、利用可能な不透明Assetバイト（プラグイン状態・録音音声等）を保持するか、明示的に新しい版・ID・参照を作成して整合させる。Score JSONを整形し直しただけでも、**元バイト列**に対するSHA-256は変化する。古いProduction/DistributedのScoreハッシュをそのまま新しいScoreへ結び付けてはならない。Asset ID・ファイル名・URIだけが残り、Asset本体が欠けている状態は**参照情報のみの保持**であり、完全な無損失移送ではない。未知の`hostExtensions`やプラグイン状態をそのまま保持する場合でも、音色の再現・プラグインの起動・ライセンス有効性を保証しない。

### 27.3 未対応機能・損失の報告

要求された情報を保持できない場合、無損失上書きを拒否するか、利用者が明示的に選んだ損失ありExportへ切り替える。報告には、影響するTrack・Channel・Device・Region・Asset・Automation・Voice・Plan・Event等の安定IDを可能な限り含め、**削除、近似、Asset本体の未取得、実行未対応、再現性未確認**を区別する。これは診断の区分案であり、**新しいJSONフィールドやSchemaのenum値ではない**。プラグイン状態のバイト列を保存してDSPをバイパスする場合は「データ保持・音響面の劣化」であり、状態バイトそのものを破棄すれば「データ損失」となる。Score単独のExportでは、別途保持していないMixer・録音Regionなどの情報が失われる。

### 27.4 Score改訂・遠隔Sessionの責任分離

Scoreが編集・再整形された場合、旧Scoreと既存Profileの関連付けは履歴として保持する。Productionは第26節に従い、`score.documentId`、`score.revisionId`、`score.sourceUri`、`score.sha256`の存在する項目と、元source Tickの録音/Automationを確認して、新しいProfileコピーとして明示的に再関連付けする。`sourceUri`は参照先のヒントであり、ハッシュの代替でも自動取得の命令でもない。Distributed Sessionは新しいScore Revisionを扱う場合、**新しい`sessionId`**と新しい演奏状態を必要とし、旧Event・Clock・確定フレーズを無断移植しない。ハッシュ一致は著作者認証でも機器制御の認可でもない。

### 27.5 機能別の対応表明

Core Reader/Writer、Production Profile 0.1/0.2 Reader/Writer、Opaque Asset保持、Cross-Profile Binding Reader、Plan-aware、Distributed Snapshot/Event Readerなどは**対象版と操作別**に対応を表明する。データを読み込めるだけで、DAWの音や遠隔AI・ロボットの実動作を保証したことにしてはならない。将来の未知のVersionを無断で旧Versionへ読み替えない。

**公開状態：** 本節は実行を伴わない未承認の規範候補。Schemaパラメーターは追加しない。著作者による正式採用、日英校了、ライセンス・権利の確認が必要であり、動作検証を行ったとは主張しない。

## 28. 規格の配布ZIPと制作環境データ一式の区別（Draft 0.22・未採用案）

### 28.1 標準化した制作プロジェクトのアーカイブ形式は存在しない

Production Session Profile 0.1.0/0.2.0が規定するのは**JSON、安定ID、参照・Asset URIの意味**である。独立した制作プロジェクトのZIP構造、ディレクトリ配置、共通マニフェスト形式、暗号化、署名、ネットワークAPI、プラグイン本体の梱包仕様を規定しない。`OSTF_4.3_Draft_*_Development_Package.zip`は規格文書の**配布パッケージ**であり、利用者の制作プロジェクトを交換する標準コンテナーではない。配布用の`PACKAGE_MANIFEST.json`や`SHA256SUMS.txt`を楽曲・制作Profileの規範フィールドとして扱ってはならない。

### 28.2 実際に受け取ったデータに基づいて無損失保存を表明する

ソフトウェアはScore、任意の独立Profile、参照された外部Assetの実バイト列を、独自のフォルダー/アーカイブ/許可されたサービスから受け取ってよい。受け取った**原本Score/Profile JSON**、受け取った**不透明Assetの実体**、記述子だけで**実体が未入手のAsset**を区別する。これは報告上の区別であり、新しいJSONプロパティではない。

「受領したデータ一式を無損失で保持」と表明するソフトウェアは、表明の対象である**実際に渡された**バージョン付きJSONとAsset実体を欠落・無断改変なく保存しなければならない。保持できない場合は無損失を主張せず、拒否するか対象IDを含む損失報告を提示する。実体のないAsset記述子だけでは制作環境の完全復元を主張できない。一方、**元々提供されていないProfile**を保存していないことを、ソフトウェアによるデータ削除とみなしてはいけない。主張の対象となる入力セットを明示する。

### 28.3 原本ハッシュと実行の責任分離

既存のScore SHA-256は**原本OSTFファイルの正確なバイト列**に対する値であり、外側のZIP、URL、JSON再整形後の内容のハッシュではない。Scoreを書き換えたら第26節の新Revision・再関連付け手順が必要である。プラグイン状態・音声Assetのチェックサムは、それぞれ元のAsset実体について解釈する。外部コンテナー独自の暗号化・署名・権限・圧縮機能はOSTFが保証する機能ではない。

### 28.4 適合の表記

「Core Reader」「Production 0.2 JSON Reader」「受領したAssetを含む無損失Writer」「明示したデータ一式の無損失保持」「DAW/プラグインの実音レンダリング」は互いに別の能力である。配布用ZIPの展開だけではいずれも証明されない。将来、制作プロジェクトをまとめるアーカイブ形式を標準化する場合は、独立したバージョンを持つ新提案と著作者承認が必要である。

**公開状態：** 未採用のDraft 0.22規範案。新たなSchema・JSON項目はなく、動作検証・権利承認も済んだものではない。

## 29. 3文書の関連付けと更新権限の現行解釈（Draft 0.23・未採用）

OSTFのScore、Production Session Profile、Distributed Session Profileはそれぞれ独立した版・正本を持つ。**3文書の関連付けは宣言内容の照合であって、状態変更ではない。** 過去Draftの規範候補を累積している本書について、現行案の解釈を次のように整理する。

| 入力・処理 | Score Coreへの影響 | Productionへの影響 | Distributedへの影響 |
| --- | --- | --- | --- |
| 認可されたAPIから版付きScoreを取得 | 元バイトの同一性・Schema・意味を確認 | `score.sha256`照合は別途行う | `scoreSha256`照合は別途行う |
| `phraseProposed`を受信 | Noteの追加なし | RegionやPluginを変更しない | 提案にすぎず、確定フレーズではない |
| 有効な`phraseCommitted`を受理 | **Scoreの`notes[]`を自動更新しない** | **録音Region・Automation・Pluginを自動更新しない** | 認可された`open` Visit Partの確定履歴を更新する |
| 確定演奏を新Scoreへ保存 | 著者操作で新バイト列・RevisionのScoreを作る | 元source TickとTrackを照合した**新Profileコピー**を作る場合のみ関連付けを更新 | Scoreが変われば**新Session ID**を必要とする |
| Profileと元Scoreのハッシュ不一致 | 旧Scoreを無断で書き換えない | 無断で新Scoreへ移行せず、未関連状態を表示 | 元の固定Sessionを保持 |
| 実体がないAsset記述子 | Core音声を推測生成しない | 参照メタデータのみ保持。音声・音色の復元とは区別 | ロボットへの実行権限を与えない |

元Scoreの実体バイトが未入手なら、2つのProfileに記載されたハッシュが等しいことは**宣言値の一致**にすぎず、実際の原本・Track・Planの検証にはならない。URL、HTTP ETag、ZIP名、Track表示名も同一性の代替ではない。Session権限はミキサー変更やプラグイン起動の権限ではなく、Production Writerの操作は分散Eventの確定権限ではない。従来§25〜28の詳細規則は維持する。**新しいJSON項目・通信APIは追加しない。**

## 30. Draft 0.24 — ProductionとDistributedの版識別（未採択案）

Production Profile 0.1.0/0.2.0は`profile:"OSTF-Production-Session"`および必須の`profileVersion:"0.1.0"`/`"0.2.0"`で版を選択します。Distributed Session Profile 0.2は代わりに`profile:"OSTF-Distributed-Session-0.2"`と`recordType`を持ち、**`profileVersion`を持ちません**。既存のSchemaとサンプルが正本であり、この追補で新しいJSON項目は追加しません。分散イベントの確定・再送はMixer Automationやプラグイン状態を変更しません。詳細は`CONFORMANCE.md`および`SESSION_STATE_MACHINE.md`を参照してください。著作者の正式採用と公開承認は未完了です。


## Draft 0.70 — 候補集合の探索完了と慎重な参照判定（未採択）

参照の4状態は、**実際に評価できた範囲での判定**であり、インターネット上の全候補を探索した保証ではない。実装は許可された候補の探索範囲、およびその列挙と実体バイト取得の完了・未完了を明示しなければならない。ファイル名、申告されたハッシュ、HTTPヘッダー、音楽的な一致だけでは検証済みとはしない。

1. 許可された候補集合の列挙またはバイト取得が不完全な場合は、外部診断 **NOT_EVALUATED** とする。これはOSTFの新しいJSON値ではない。
2. 候補集合の探索と取得が完了している場合、候補Scoreが0件ならその範囲において **MISSING**、Scoreが1件以上存在しても元バイト列のSHA-256一致がなければ **MISMATCH** とする。世界中に存在しないという意味ではない。
3. ハッシュ一致候補の同一バイト列は重複コピーとしてまとめ、Track／Plan／Visitなど必須参照が欠落または一意に解決できない場合は **AMBIGUOUS** とする。`missing_referent` と `nonunique_referent` はJSONに格納しない診断補足とする。
4. ハッシュと必須参照がすべて整合して初めて **RESOLVED** とする。
5. 許可された候補の列挙または実体バイト取得が一つでも未完了なら、一致候補をすでに観測していても **NOT_EVALUATED** と報告する。部分的・条件付きの **RESOLVED** は認めない。未完了の探索範囲を明示し、候補集合が未完了のままMISSING・MISMATCH・AMBIGUOUS・RESOLVEDを推定してはならない。古いProfileを改訂Scoreへ暗黙に付け替えてはならない。

INVALID／UNSUPPORTEDは形式・バージョンに関する事前エラーであり、4状態とは別扱い。SHA-256だけで著作者の認証やDAW・プラグイン・遠隔AI・ロボットへの実行権限は得られない。本規則はD01〜D03の正式採択前の仕様候補であり、実装検証済みではない。


## Draft 0.76 — 参照判定規則の文書統合（未採択）

上記Draft 0.70の第5項に残っていた部分的`RESOLVED`の例外を撤回し、Draft 0.71／0.73の現行優先規則と一致させた。INVALID／UNSUPPORTEDは参照判定前の形式エラー、許可済み候補の列挙・取得が未完了なら外部診断`NOT_EVALUATED`、探索完了後にのみMISSING／MISMATCH／AMBIGUOUS／RESOLVEDを判定できる。探索完了前に得たハッシュ一致は暫定証拠であり、**RESOLVEDではない**。新しいJSONフィールドやネットワーク探索義務は追加しない。D01〜D03の正式採択前の規範案である。
