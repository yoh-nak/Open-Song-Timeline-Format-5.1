> **現行採択候補：Draft 0.77（未承認）。** 冒頭の参照解決判定表を現行提案とし、下位の旧Draft番号を持つ節は履歴であって並列の現行規範ではありません。今回の変更は編集上の特定であり、Schemaやシリアライズ形式は変更しません。

# Draft 0.73 — 現行の参照解決判定表（未採択の規範案）

**承認対象：D02。** 以下が現行の採択候補であり、後続のDraft 0.62〜0.72の記述は改訂履歴として保持する。古い判定例を並立する現行規則として扱わない。発行者の採択前に規範として確定したわけではない。Schema・シリアライズ形式は変更しない。

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

**採択対象：D02／Distributed Session 0.2。** 正式採択の対象は、承認記録で特定する本文と既存Schemaに限る。過去Draft 0.62〜0.70の参照判定例は改訂履歴として残し、並立する定義として扱わない。矛盾する参照診断については**現行候補内で**Draft 0.71の「許可された候補集合の列挙・取得が完了してから判定」する規則を優先し、未完了ならJSONに新項目を追加せず外部診断`NOT_EVALUATED`とする。

第三者実装は、(a)未知データの読込・保持、(b)ラウンドトリップ保存、(c)編集、(d)意味解釈、(e)実行を区別する。いずれか一つの対応を他の操作まで拡大して表明しない。ハッシュ一致は分散演奏実施、ミキサーの音響再現、ロボット動作の保証にならない。これらの規範案は**D02が発行者により正式採択された場合のみ**規範効力を持つ。

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

# OSTF Distributed Session Profile 0.2 — 日本語規範仕様案（Draft 0.55）

> **現行編集版：Draft 0.59（未採択）。** 下記の古いDraft見出しは、累積した策定経緯を示し、現在のJSON版識別子を変更しません。6件の版別Schemaは不変です。公開判定の正本は [RELEASE_READINESS.md](RELEASE_READINESS.md) とし、D01〜D05はすべて承認待ちです。動作・独立実装検証は判定から除外していますが、完了とは扱いません。

## Draft 0.33 — Sessionイベント受理とScore保存の分離（未採択）

権限・Revision・楽曲同一性を確認してSessionイベントを確定しても、更新対象は**Session状態のみ**です。ScoreのNote、ProductionのMixer/Automation、音響DSPやロボットの物理動作を自動変更しません。拒否・古いRevision・競合を成功した状態変更と報告しないでください。`CONFORMANCE.md`の操作境界表を参照。Schema・通信方式の追加はありません。

---

## Draft 0.32 — Score原本ハッシュと再保存（未採択）

Distributed 0.2の`scoreSha256`は実際に受け取ったScore原本バイトを固定するもので、JSONの意味やURLだけを識別しません。再保存でScoreのバイト列が変われば新しいSHA-256と、既存のRevision規則に従った**明示的な新Session ID**が必要です。既存Session内で確定したイベントの対象を勝手に差し替えてはいけません。`CONFORMANCE.md` Draft 0.32を参照。新しいフィールド・時計プロトコルは追加しません。

---

## Draft 0.29 — 分散セッションのエラー報告と正本の分離（編集案）

`docs/CONFORMANCE.md`のDraft 0.29診断分類を参照。新しいEvent IDを持つ古いbase Revisionの状態変更イベントは拒否し、認証と固定Score/Plan照合を済ませた既承認同一イベントの再送のみ冪等処理できる。承認イベントはSession履歴を変更するがScore Notes/Productionを自動更新しない。各種チェックの結果をロボット実行・安全性の保証に転用しない。この追補は新しいJSONフィールドを追加しない。

---

## OSTF Distributed Session Profile 0.2 — 分散セッション仕様案

**OSTF 4.3 Coreとは別の任意JSONプロファイルです。** 楽曲ファイル `.ostf` にはセッション参加者、リアルタイム位置、通信イベントを入れません。通信手段（HTTP、WebSocket、WebRTC等）や時計同期方式、AIモデル、ロボットの駆動系を指定しません。

## Snapshot（共有状態）

`sessionId`、`documentId`、`revisionId`、`stateRevision`、`participants`、`authorityParticipantId` を持ちます。`position`には楽曲元の`sourceTick`、展開後の`performanceTick`、`visitId`、時計ドメインと観測UTC時刻・不確実性を保持できます。`committedPhrases`は後から参加する演奏者が今後の演奏を再現できるよう、確定した短い演奏フレーズを保持できます。全履歴を再現するには完全なログまたは完全なSnapshotが別途必要です。

参加者IDはTrack IDとは別であり、`assignedTrackIds`の割当てはロボット制御の許可ではありません。参加者の能力は自己申告情報です。実際の物理的な動作・安全性は各ロボットに実装された制御系が独立に判断します。

## Event（共有イベント）

`phraseProposed`、`turnRequested`、`cueIssued`、`performanceObserved`、`participantStatus` は提案・観測・通知にすぎず、確定状態を変更しません。`phraseCommitted`と`sessionStateChanged`だけが承認された状態変更候補です。両者には`resultStateRevision`が必要で、必ず`baseStateRevision + 1`とします。

状態を変更するイベントはSnapshotで指定された権限者の判断でなければなりません。通信の受信順や時計時刻で「最後のものを優先する」といった暗黙ルールはありません。同じ`eventId`の再送は一回だけ扱い、違う内容を同じIDで送信したら競合として報告します。

## Phrase（提案／確定フレーズ）

Profile 0.2の最低限のフレーズ形式は`midi1Notes`です。フレーズ長とノートの開始位置、長さ、音高、ベロシティを整数で表現します。音声合成・歌詞・MPE・ロボットの関節運動・外部音源状態はこの最小表現に含めません。確定したSession Phraseが元のOSTFのNoteを書き換えることはありません。明示的な編集を行って新しいOSTF Revisionへ保存する場合のみ、元の音楽文書が変わります。

## 時間と安全性

共通の音楽Tickを理解できることと、世界各地で同じ瞬間に正確に演奏できることは別です。タイムスタンプだけでは同期できません。時計の校正、通信遅延・揺らぎ、ロボットの準備時間、音の伝搬を実装側で扱います。ネットワークメッセージは運動指令ではなく、ロボットは必ず独立した安全・認証・緊急停止系を維持します。

正確な型とイベント別Payloadは`schema/ostf-distributed-session-0.2.schema.json`、英語の規範的な意味規則は`docs/SESSION_STATE_MACHINE.md`を参照してください。

## Draft 0.4 — Snapshotの状態とイベント同一性

Profile 0.2のSnapshotには`sessionStatus`（`prepared`・`playing`・`stopped`）を必須とします。`playing`のときは`position`が必要です。`prepared`・`stopped`では位置を省略できますが、省略をTick 0と解釈してはいけません。`participantStatus`は個々の参加者の状態報告であり、セッション全体の`sessionStatus`を直接変更する権限はありません。承認済み`sessionStopped`イベントを採用した後のSnapshotは必ず`stopped`となります。Profile 0.2には自動resumeを定義しません。

イベントの重複判定では、`eventId`が同じで**JSON内容が異なる場合**に競合とし、空白やオブジェクト内プロパティ順序だけの違いは競合とみなしません。重複したJSONキーはパース時に不正とします。これはデジタル署名の方式を規定するものではありません。Profile 0.2はあくまでも策定中であり、以前のDraft 0.3のProfile 0.2 Snapshotとの互換性を自動的には保証しません。

## Draft 0.5 — 演奏開始と確定フレーズの範囲

Profile 0.2に`sessionStateChanged`の新しい`changeKind:"sessionStarted"`を追加します。`prepared`から`playing`へ遷移するときは、`payload.position`に演奏Plan・Visit・Source Tick・Performance Tick・時計ドメイン・UTC基準時刻・不確実性を明記し、イベントの`effectivePerformanceTick`と位置Tickを一致させます。`playing`は演奏の時計位置が合意されている状態を意味し、実際の音響やロボット駆動が始まった証拠ではありません。自動の再開・一時停止は定義しません。`sessionStopped`は現在位置の即時の終了であり、将来位置の停止予約ではありません。

`Snapshot.commitmentWindow`は任意の完了範囲宣言です。`startPerformanceTick`から`endPerformanceTick`（半開区間）に交差する、該当State Revisionまでに**確定されたSessionフレーズを全件含む**ことを宣言します。`committedPhrases`が空であれば、その範囲に確定フレーズはないと主張します。省略されれば完全性の保証はありません。別のRevisionで後から確定される内容や、元のOSTF固定ノート、歌詞、ロボットの実行準備までは保証しません。

保存済みの提案を採用する場合は、提案ID・対象Track・フレーズ内容に加えて`effectivePerformanceTick`も一致させます。異なる位置への移動は新規の提案として扱います。詳細は`docs/SESSION_STATE_MACHINE.md`を参照してください。

## Draft 0.6 — 確定Sessionフレーズと演奏Planの整合

`phraseCommitted`で承認できるのは、固定されたOSTFのPerformance Planにおいて対象Trackの`realization`が**明示的に`open`であるVisit**の内部だけです。`fixed`の元ノートに黙って重ねたり、`silent`に音を出したり、`unspecified`を`open`と推測したりしてはいけません。確定フレーズの半開区間全体が一つのVisit内に収まる必要があります。Visitを跨ぐ場合は分割して新規提案します。

**Draft 0.9追補を優先します。** 演奏Planが不明なセッションではフレーズを承認できませんが、現行の未公開Profile 0.2では全Snapshot/Eventにルート`performancePlanId`と`scoreSha256`が必須です。そのため、`prepared`が`position`を省略してもPlanは既に固定されています。`playing`のPositionと`sessionStarted`のPositionはこのルートPlanと一致しなければなりません。Session Phraseは承認後に暗黙の上書き・撤回を行いません。承認済みフレーズの同一Track上での時間重複や、`commitEventId`重複は不正です。実際の権限・時計同期・安全制御は引き続き実装側の責任です。

これらは4.3 Coreに新しいフィールドを加えるものではなく、別冊Session Profile 0.2の**提案中の意味規則**です。`docs/SESSION_STATE_MACHINE.md`のDraft 0.6節を参照してください。

## Draft 0.7 — 楽曲Revision・確定履歴・演奏実績の分離

1つのSessionは同一の楽曲`documentId`・`revisionId`・`performancePlanId`を参照し続けます。Web API側で新しい曲に更新されても、元の確定済みフレーズは自動的に新曲へ移動できません。内容の異なる文書を同じRevisionとして受け取った場合は整合性エラーです。

`phraseCommitted`は**承認されたフレーズの履歴**であり、遠隔ロボットが実際に発音したという証拠ではありません。将来のVisitを飛ばした場合やSessionを停止した場合には、後続の未演奏フレーズを演奏済みとみなさず、承認履歴だけ保持します。演奏中のVisit切替はPerformance Tickが前へ進む場合に限定し、同一Sessionの巻戻し・再開・別Revisionへの切替はProfile 0.2では定義しません。

同一`eventId`かつ内容が同一の再送は、状態Revisionが進んだ後でも二重採用しません。異なる内容の同一IDは競合として拒否します。`assignmentChanged`でも確定済みTrackフレーズを改変・消去しません。将来の確定フレーズを担当する参加者がゼロになる割当変更は、この保守的な策定案では拒否します。各参加者への実際の発音割り当て、認証、機械的安全性はSessionを使う実装側が管理します。

詳しくは英語の`SESSION_STATE_MACHINE.md` Draft 0.7 節を参照してください。JSON Schemaは変更していません。

## Draft 0.8 — 割当変更・イベント再送・フレーズ範囲の規則修正

**未承認の規範案。** Profile 0.2の`sessionStateChanged.payload.changeKind:"assignmentChanged"`は`participantId`と`assignedTrackIds`のみを担当する変更とし、`targetVisitId`または`position`を含めてはいけません。従来のJSON Schema条件式は`position`単独を誤って許していたため、両項目を独立に禁止する`not.anyOf`へ修正しました。新フィールド・新定義は追加していません。**これはDraft 0.8時点の挙動であり、Draft 0.10で置き換えます。** 現在の未公開Draft 0.10では`sessionStarted`と`visitChanged`の両方が`position`を必須とします。`assignmentChanged`では引き続き禁止です。

認証されていない同一イベントIDの受信者へ、過去のイベントが受理されたかを開示してはいけません。**認証・権限・楽曲Revisionの照合が先、同一イベントIDの再送照合が次、未受理イベントに限って状態Revisionの新旧比較**を行います。受理済みと等しい再送はno-op、異なる内容で同じIDは競合です。JSONのオブジェクト内プロパティ順や空白は差異とせず、配列の順番と文字列の実際の文字は区別します。数値は十進数として正確に比較し、`1`と`1.0`は等価ですが真偽値とは異なります。値の精度が保証できない場合は勝手に再送と判定せず不確定として拒否します。

どのSnapshotでも、保存された各`committedPhrases[].phrase.notes[]`の`startTick + durationTicks`は親Phraseの`durationTicks`以下でなければなりません。`commitmentWindow`の有無はこのノート範囲の妥当性に影響しません。停止後やVisitスキップ後に残した過去の確定履歴は、現在の演奏者割当を要求しません。一方、未演奏の未来フレーズの担当者がゼロになる割当変更は、従来の保守的な意味規則どおり拒否します。確定履歴を実際の発音の証拠と解釈してはいけません。

## Draft 0.9 — 演奏PlanとOSTF原本バイト列の固定（未承認の規範案）

これまでのProfile 0.2では`prepared`のSnapshotが`position`を省略すると、どの`performancePlans[].id`を使うか確定できませんでした。また`documentId`と`revisionId`だけでは、同名Revisionで異なるJSONが配信された場合の不一致を確認できません。そこで、**別冊の未公開Distributed Session Profile 0.2に限り**、全Snapshot・Eventでルート直下の`performancePlanId`と`scoreSha256`を必須とします。OSTF 4.3 Core自体のSchemaは変えません。

- `performancePlanId`：参照する4.3楽曲中の有限なPerformance Plan ID。`prepared`/`stopped`の位置情報がないSnapshotでも省略不可です。
- `scoreSha256`：実際に共有するOSTFファイルの**正確なUTF-8バイト列**に対するSHA-256（小文字16進64桁）。HTTPならContent-Encodingを復号した後、JSONパースや書き直しの前の原本バイト列を計算対象にします。原本にBOMが含まれる場合もそのバイトを含めます。JSONの空白だけが違っても別ダイジェストになります。これはJSONの音楽的な同値性ではなく、特定のファイル実体を固定するための値です。
- `position`または`sessionStarted.payload.position`が存在するとき、内側の`performancePlanId`はルートのIDと**必ず一致**します。Visit ID、Source Tick、Performance TickはそのPlanで解決します。位置を省略したことをPlanの省略とみなしてはいけません。
- セッションの固定識別は`sessionId`、`documentId`、`revisionId`、`performancePlanId`、`scoreSha256`の組で行い、イベント再送を受理したかの問い合わせより前に、認証とこの組の照合を行います。同じRevision名でもファイル内容が異なれば拒否します。
- SHA-256はファイルバイト列の照合情報であって、発行者の本人性、署名、所有権、ロボット駆動の安全性を証明しません。これらは引き続きサービスや実機制御側で扱います。
- 旧Draft 0.8のProfile 0.2データには新しい必須フィールドがないため、そのままでは新案に適合しません。使用するPlanと原本バイト列を明示的に再確認して更新します。別バージョンのProfile 0.1を自動で0.2に読み替えません。

**想定診断:** `E-SESSION-PLAN-UNPINNED`、`E-SESSION-POSITION-PLAN-MISMATCH`、`E-SESSION-SCORE-DIGEST`。構造的な整合確認は通信遅延や実機演奏の検証ではありません。

## Draft 0.10 — Visit切替時の時計基準位置を明示する規範案

Profile 0.2の`sessionStateChanged.payload.changeKind:"visitChanged"`では`targetVisitId`に加えて`position`を**必須**とします。`position.visitId`は対象Visitと同一、`performanceTick`はEventの`effectivePerformanceTick`および対象Visitの展開後開始Tickと一致し、`sourceTick`はそのVisitの最初の参照区間の開始Tickを表します。`epochUtc`は受信時刻ではなく、指定された演奏Tickに対応する共有時計の推定時刻です。演奏者側はこの基準位置を使って新しいVisitに移れますが、通信遅延・ロボット動作・同期精度は保証しません。

以前の未公開Draft 0.9のように`visitChanged`がVisit IDだけを持つレコードはDraft 0.10案に適合しません。信用できる時計情報から作者が明示的に更新し、時刻を推測で埋めないものとします。Core 4.3は変更しません。実装・実機検証済みという意味ではありません。

## Draft 0.11 — 時計ドメインの継続性・テンポの正本・停止イベント（未承認の規範案）

- `sessionStarted.payload.position.clockDomainId`で演奏中セッションの音楽時計ドメインIDを確定します。同一Sessionの以後の`playing` Snapshotの`position`と`visitChanged.payload.position`は**同じIDが必須**です。違うIDへの暗黙の変更は不正であり、必要なら新しいSessionを作成します。`prepared`の任意Positionは演奏時計ドメインを確定しません。IDが同じことは通信遅延や時計の精度・本人性を保証しません。
- `position.tempoBpm`は任意の説明情報であり、元のOSTFの`timeline.tempoChanges`から`sourceTick`時点で有効なBPMと**数値的に一致**しなければなりません。source Tickで採用されるのは、その時点以前で最後に明示された段階型Tempoです。Sourceの区間を飛び越したときも元のTempoを再取得します。`tempoBpm`が異なれば`E-SESSION-TEMPO-CONFLICT`として拒否し、省略時には元のOSTFから解釈します。Tempoがソース側にまだ存在しなければ、勝手にテンポを作らず未解決とします。
- `sessionStopped`の`effectivePerformanceTick`は記録上の音楽位置・参考情報であり、将来の停止予約ではありません。承認された停止はただちにSessionを`stopped`にしますが、実際の音やロボット駆動が停止した証拠にはなりません。`prepared`から停止した場合など、再生位置の未確定なケースでTick 0を記録しても物理的な停止時刻を意味しません。

追加フィールドはありません。Core 4.3 Schemaと正式4.2継承部分は変更しません。詳細規則の英語正本案は`SESSION_STATE_MACHINE.md` Draft 0.11であり、実際のWAN・実機・独立パーサー検証は利用者指定のリリース判定条件から除外され、完了とも主張しません。

## Draft 0.12：演奏中の時計基準には元楽曲のテンポが必要（未承認）

`playing`状態のSnapshot、および`sessionStarted`・`visitChanged`の`position`は、音楽時刻とUTC推定時刻を対応させる有効な演奏上の基準位置を主張します。そのため、`sourceTick`において、固定されたOSTF楽曲の`timeline.tempoChanges[]`から有効なBPMを一意に解決できなければなりません。任意の`position.tempoBpm`を省略しても、元楽曲にテンポがなければ`E-SESSION-TEMPO-UNRESOLVED`としてこの時計基準を拒否します。`tempoBpm`が存在する場合は元楽曲の値と一致しなければなりません。

通常のOSTF楽曲に必ずTempoを記載することを要求するものではありません。`prepared` / `stopped` Snapshotの任意のPositionは演奏中の時計基準を宣言しないため、テンポ未解決であっても演奏同期が成立したとは扱いません。演奏開始前に必要なテンポを明示するには、新しいOSTF Revisionを作成して楽曲側に記述します。Profileだけでテンポを捏造・上書きしてはいけません。

1区間の理想的な音楽経過秒数は `60 × Tick数 ÷ (PPQ × BPM)` です。実演奏上の同一Visit内で時計基準から将来Tickを求める場合、元の楽曲のテンポ変更点と参照Section境界で区間を分割し、それぞれのBPMで積算します。省略された元曲の区間は経過時間に加えず、境界をまたいで直前のテンポを流用しません。テンポ未解決区間ではUTC演奏期限を算出できると主張してはいけません。これは楽曲上の理想時刻の数理規則であり、WAN同期精度やロボット駆動時刻を保証しません。

さらにProfile 0.2のSnapshotは少なくとも1名の`participants[]`を持つ必要があります。`authorityParticipantId`がその中の唯一のIDへ解決されるという既存の意味規則を、Schemaの`minItems:1`でも補強しました。これらは正式採択前の編集案です。

## Draft 0.19 — Studio Production Profileとの任意の関連付け

Distributed Session 0.2の`scoreSha256`とProduction Session 0.1/0.2の`score.sha256`を元OSTFの実体バイト列のSHA-256と一致させ、文書ID/RevisionおよびDistributedが指定する有限Plan IDを原本で解決できる場合に限り、同じ曲の二つのProfileとして関連付けられる。ProductionにはルートのPlan IDを勝手に追加しない。Track IDの一致はプラグイン、音声出力、ロボットを自動接続する指示ではない。遠隔の`phraseCommitted`はStudioの録音・Automation・Plugin状態を編集しない。詳しくは`PRODUCTION_SESSION_PROFILE.ja.md`第25節。

## Draft 0.23 — 原本ハッシュと別冊の責任分離（未採用の整理案）

Core Score 4.3そのものに必須のハッシュ値はない。一方、Distributed Session Profile 0.2のルート`scoreSha256`は必須であり、`documentId`、`revisionId`、`performancePlanId`と共に**元ScoreのUTF-8原本バイト列**に固定する。これはJSONの再整形後に計算する標準化ハッシュではない。元Scoreが未入手で両Profileのハッシュが一致しても、元のTrack ID・Plan IDが有効とは確認できない。古いWeb説明の「共通のcanonical JSONハッシュはない」を、別冊0.2の必須`scoreSha256`を無効にするものとして解釈しない。

DistributedのEventが確定しても、ProductionのChannel/Plugin/AudioRegionやCoreのNoteへ無断転記しない。Studio ChannelとSession参加者が同じTrack IDを参照しても、プラグイン起動やロボット駆動の許可は生じない。新JSONパラメーターや通信APIは追加しない。


## Draft 0.24 — データ識別子と旧Revisionイベントの区別（未採択案）

Distributed Profile 0.2のSnapshot/Eventは、ルートに`profile:"OSTF-Distributed-Session-0.2"`および`recordType:"snapshot"`または`"event"`を持ちます。**Production Profileの`profileVersion`フィールドを持ちません。** 旧Distributed 0.1は`profile:"OSTF-Distributed-Session-0.1"`であり、0.2と互換レコードとして自動解釈しません。Production 0.1.0/0.2.0とは`profile`もSchemaも異なります。

すでに承認されているイベントの再送は、セッション/原本/Plan/発信者の認証・照合後に、同一`eventId`と完全に等しいパース済みイベント内容であれば何も再適用しません。同一IDで内容が違う場合は不整合です。**新しい状態変更イベント**が古い`baseStateRevision`を指定していたら拒否します。勝手に`phraseProposed`へ変更したり、最新Revisionとして再承認したりしません。提案・観測・状態報告は確定Revisionを増やしません。根拠となる詳細な英文規範案は`SESSION_STATE_MACHINE.md`です。これらは新規JSONフィールドを定義せず、動作・WAN・ロボットの検証を意味しません。


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
