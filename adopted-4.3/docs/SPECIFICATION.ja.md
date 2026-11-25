> **現行採択候補：Draft 0.77（未承認）。** 冒頭の参照解決判定表を現行提案とし、下位の旧Draft番号を持つ節は履歴であって並列の現行規範ではありません。今回の変更は編集上の特定であり、Schemaやシリアライズ形式は変更しません。

# Draft 0.73 — 現行の参照解決判定表（未採択の規範案）

**承認対象：D01。** 以下が現行の採択候補であり、後続のDraft 0.62〜0.72の記述は改訂履歴として保持する。古い判定例を並立する現行規則として扱わない。発行者の採択前に規範として確定したわけではない。Schema・シリアライズ形式は変更しない。

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

**採択対象：D01／Core Score 4.3。** 正式採択の対象は、承認記録で特定する本文と既存Schemaに限る。過去Draft 0.62〜0.70の参照判定例は改訂履歴として残し、並立する定義として扱わない。矛盾する参照診断については**現行候補内で**Draft 0.71の「許可された候補集合の列挙・取得が完了してから判定」する規則を優先し、未完了ならJSONに新項目を追加せず外部診断`NOT_EVALUATED`とする。

第三者実装は、(a)未知データの読込・保持、(b)ラウンドトリップ保存、(c)編集、(d)意味解釈、(e)実行を区別する。いずれか一つの対応を他の操作まで拡大して表明しない。ハッシュ一致は分散演奏実施、ミキサーの音響再現、ロボット動作の保証にならない。これらの規範案は**D01が発行者により正式採択された場合のみ**規範効力を持つ。

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

# OSTF 4.3.0 — 楽曲Coreの規範仕様案（Draft 0.55）

> **現行編集版：Draft 0.59（未採択）。** 下記の古いDraft見出しは、累積した策定経緯を示し、現在のJSON版識別子を変更しません。6件の版別Schemaは不変です。公開判定の正本は [RELEASE_READINESS.md](RELEASE_READINESS.md) とし、D01〜D05はすべて承認待ちです。動作・独立実装検証は判定から除外していますが、完了とは扱いません。

## Draft 0.44 — 意味規則IDの重複解消（D01/D04未承認）

従来の`SEMANTIC_RULES.md`ではS13とS14が2つずつ存在し、遠隔Sessionと
Core音楽側の規則を同じ番号で参照していました。本Draftでは先に定義された
**S13=Sessionの状態Revision**、**S14=Session開始・確定範囲**を維持し、
後から追加した**連続fixed区間とhard cutをS22**、**歌詞・歌唱選択をS23**に分離します。
S21は既存のSession音楽テンポ参照として保持します。番号は仕様書の参照IDであり、
優先順位やJSONパラメーターを意味しません。既存4.2の正本・Schemaは変更しません。
英日文書の最終承認D04と意味規則の正式採用D01はまだ完了していません。

## Draft 0.43 — 有限Performance Planでの歌詞・歌唱表現の選択（未採択）

既存4.2のLyric Voice・Unit・Alignment・VocalPerformanceが元Scoreの正本です。`fixed`のVisitごとに選択された**Noteの発音開始出現**と生存ゲートを先に解決し、そのうえでVoice所属と元の歌詞Alignmentの対応を評価します。複数Noteへ結び付くAlignmentの一部だけが選択された場合は**部分選択**であり、元のAlignmentの不正や歌詞全体の再現成功を意味しません。元Noteが連続するSectionをまたぐ場合は一つの出現として扱い、音素や歌唱曲線を結合境界で再トリガーしません。ジャンプによるhard cutでNoteが短縮された場合、元のphonemeEvents・pitchCurves・expressionCurvesの残りを勝手に演奏済みと宣言したり、別Noteへ付け替えたりしません。固定歌唱データに実体化する際は新しいNote IDと整合するVoice/Unit/Alignment/Performance参照を明示的に生成し、不明・近似・欠落を開示します。詳細は`NOTE_AND_MIDI_CUT_SEMANTICS.md`のDraft 0.43節と`examples/15-vocal-response-phrasing.ostf`です。Schema変更・歌唱合成機能・D01/D04承認は伴いません。


## Draft 0.33 — 第三者製ソフトの操作境界（未採択）

同じOSTFのデータを使用しても、**読込、編集プレビュー、Score保存、Production再関連付け、Distributed Sessionのイベント確定、部分Export、規格の正式公開**は異なる操作です。ある操作の成功を別の操作の許可や成功として扱ってはいけません。

| 要求された操作 | 扱う正本 | 無断で実行してはいけないこと |
| --- | --- | --- |
| Scoreを読む・表示する | Scoreのみ | Note生成・Profile変更・プラグイン実行・Assetの自動取得・ロボット制御 |
| 編集内容をプレビュー | 影響を受ける安定IDとsource Tick | 原データやSession履歴の自動更新 |
| Scoreを保存 | 変更対象のScoreと明示したRevision | 元バイトが変更されたのに旧Production/Distributedのハッシュを流用すること |
| Productionを保存・再関連付け | Score原本のSHA-256と制作Profile | 未提供Asset実体の捏造・音源ロード・Score本体の無断変更 |
| Session Eventを確定 | 承認されたSession状態Revision | Score Note・制作Automation・ロボット運動の自動更新 |
| 部分Export | 明示した出力範囲 | 提供済みProfile/Assetを省略して「制作データ一式を無損失保存」と表示 |
| 公開版として出す | 実際に承認された完成アーカイブ | Draft作成やライセンステンプレートを著作者許諾と扱うこと |

**失敗時：** ある保存やイベントの受理が拒否された場合、承認済み状態への部分的変更が起きたかのように報告してはいけません。複数ファイルの保存が部分成功した場合は、ファイル単位で成功・失敗・未実施と情報損失を開示します。すべてのソフトに共通のトランザクション実装方式やレポート用JSONを追加するものではありません。`sourceTick`と展開後の`performanceTick`、Score NoteとSession Phrase、MIDIイベントとProduction Automationの正本は混同しません。

本節はD01〜D04の著作者承認待ちの意味規則案で、JSON Schemaの追加、動作確認、公開承認を意味しません。

---

## Draft 0.32 — 原本バイトの同一性と情報の無損失保持の区別（未採択の編集案）

次の3種類を混同してはなりません。

| 主張 | 必要な根拠 | 保証しないこと |
| --- | --- | --- |
| **Score原本のバイト同一性** | 実際に供給された`.ostf` UTF-8原本バイトのSHA-256照合 | JSONの意味一致、再生、外部取得権限 |
| **Scoreの音楽的情報を保持した保存** | 版に適合する構造・ID・参照・元の音楽情報と、未知情報の保持／損失報告 | JSONの文字列・空白・キー順序まで同一であること |
| **制作データ一式・Asset実体のバイト保持** | 指定された保存範囲について、実際に受領したScore／Profileと不透明なAsset実体バイトを列挙し保持した証拠 | プラグイン実行、同一音色、ロボット動作、未提供Asset実体の保存 |

**関連付け規則案：** JSONを読み取って再保存すると、音楽的な値が同じでも原本のバイト列が変わる場合があります。その場合、以前の`scoreSha256`／`score.sha256`は新しいScore原本を証明しません。旧ハッシュを黙って再利用してはいけません。原本のバイトを不変で保持するか、新しいバイトのSHA-256を計算して当該Profileを**明示的な改訂・再関連付け規則に従って**更新するか、処理を拒否／損失を明示した部分出力とする必要があります。ハッシュ一致のためだけに旧Revisionや稼働中Sessionを書き換えてはいけません。Core 4.3はJSONの正規化ハッシュ方式を定義しません。

HTTPの圧縮やヘッダーはScore原本バイトに含まれません。元のデータを取得できない場合、URLやETag、他Profileのハッシュ申告だけでは原本の同一性を検証できません。**この追補はD01〜D04の未採択候補であり、新しいJSONフィールド・自動公開承認・動作検証の完了を意味しません。**

---

## Draft 0.29 — 第三者製ソフトの診断分類と情報損失の報告（未採択の編集案）

この追補は新しい`.ostf`のフィールド、診断結果を保存する必須JSON形式、APIエンドポイントを定義するものではありません。JSONとして読めること、参照できること、意味を理解できること、無損失に保存できること、実際に音を鳴らせることを**別の能力**として扱います。

| 診断カテゴリー（提案） | 内容 | 原則的な扱い |
| --- | --- | --- |
| `invalid_document` | JSON/Schemaまたはfamily/version識別が不正 | 無断で古いバージョンとみなさず拒否 |
| `unresolved_reference` | Track・Voice・Visit・Assetなどの参照が解決できない | Stable ID・JSON Pointer等を明示して報告 |
| `semantic_conflict` | 同種指示の競合・セッションRevision衝突等 | 配列の最後を優先せず、該当操作を拒否 |
| `unsupported_semantics` | 読めるが意味機能を実装していない | 無損失保存では原データを保持し、未対応を表示 |
| `missing_asset_bytes` | URI/ハッシュのみでプラグイン/音声の実体なし | 記述子の保持とAsset実体の保持を区別 |
| `explicit_loss` | 提供されたProfile/Region/Note/Asset等を省略 | 省略対象IDと範囲を明示した部分・損失ありExport |
| `stale_binding` | 別RevisionやSHAのScoreに付属Profileが残る | 明示的な再関連付けまたは新Sessionを要求 |
| `execution_unverified` | DAW/プラグイン/ロボットの実行結果は未確認 | データの妥当性を可聴再現・安全性の証明としない |

保存・書き出し操作では、**文書ファミリーと正確な版、操作、採否、カテゴリー、影響する安定ID/JSON Pointer、実際に提供された入力データとAsset実体、保持/省略/近似/未解決の範囲**を識別できる報告を推奨します。カテゴリー名は相互運用の説明用語彙であり、新しいSchema列挙値や標準診断ファイルの導入ではありません。

例えば4.3 Scoreを解釈できない旧Readerでも、未知のDirectionを完全に保持できるなら、その保存能力と意味解釈能力は別に報告できます。供給されたProduction ProfileをScoreだけのExportで省略した場合はScoreが完全でも集合全体としては部分Exportです。遠隔イベントが承認されてもCore NotesやStudio情報を書き換えません。各規範文書に矛盾を発見した場合は曖昧な優先順位で解決せず著作者の採用・修正判断へ戻します。

**本追補はDraft 0.29の未承認提案で、実機・独立パーサー検証やライセンス承認の証拠ではありません。** D01〜D05の最終採用が必要です。

---

## Draft 0.28 — 第三者製ソフトの保存・書き出しトランザクション（未承認の規範候補）

この追補は**新しいJSONフィールド、制作プロジェクト用ZIP規格、音声処理・ロボット制御機能を導入しません**。一回の保存・Exportの対象と、実際に入力として提供されたScore・Profile・Asset実体を区別するための編集案です。

| 事例 | 入力として提供されたデータ | 出力 | 正確に表明できる範囲 |
| --- | --- | --- | --- |
| A：Scoreのみの編集 | Scoreのみ。Profileは元から渡されていない | 改訂Score | Score内のすべてを保持できれば「Scoreのみ無損失」。未提供Profileは損失ではない |
| B：制作環境からScoreだけExport | Score、Production Profile、実体の音声・プラグイン状態Asset | Scoreのみ | Scoreが完全でも、**提供済み制作データの一部を省略した部分Export**。省略したProfile、ID、Asset実体を明示 |
| C：状態Assetの記述子だけ受領 | Scoreと、状態ファイルのURI/ハッシュを持つProduction Profile。実体バイトは未提供 | ScoreとProfile | 「記述子の保持」は可。「状態バイトの保持」や「プラグイン再現成功」は不可 |
| D：提供データ全体を保持 | Score、実際に渡された両Profile、実体Asset | 全入力を保持する集合 | バイトと意味の保持が実際に成立する範囲で全提供データの保持と表明可。音声・ロボット動作は別 |
| E：遠隔でフレーズが確定 | Scoreと承認済みDistributedイベント | Core Scoreを保存 | Core Notesは**自動変更されない**。分散イベントは対応Profileを保持した場合だけ継承 |

推奨判断手順：（1）実際に受領した文書のfamily/versionを特定、（2）保存・Exportの対象範囲を明示、（3）Assetの参照記述子と実体バイトを別に棚卸し、（4）提供された各情報について保存・欠落・近似・未解決を判定、（5）Stable IDとパスで影響を説明、（6）無損失で保存できない場合は拒否するか、利用者が理解して選択した別名の部分／損失ありExportとする。

ProfileのScore SHA-256は元のOSTF JSONのUTF-8**原本バイト**に対するものです。Score改訂時にハッシュだけを書き換えて再関連付けを完了したことにしたり、古いセッションの権限・イベント・ロボット制御を暗黙に引き継いだりしません。本提案はD01〜D05の正式採択待ちであり、実機や相互運用検証の結果ではありません。

---

## Draft 0.27 公開者確認（編集用）

正式採用前に`PUBLISHER_RELEASE_DECISIONS.md`のD01〜D05を著作者が個別に判断し、`CONFORMANCE.md`の文書ファミリー・版・対応操作別の表明と、提供済みAssetバイトと参照だけの違いを確認します。これは新しいJSON項目や外部機器を実行する許可ではありません。新規の規範意味規則は未承認のままです。

---

## OSTF 4.3.0 — 規範仕様案（Draft 0.29、未承認）

**策定中・未公開確定。** 4.3はDAW・AI・ジャンル・楽器・通信方式に依存しないUTF-8 JSONの音楽情報交換規格です。音源、演奏エンジン、ネットワークサービス、フィジカルAI制御器ではありません。4.2の全Coreを継承し、作曲・即興・アンサンブルに共通する音楽的意味情報を任意追加します。

## Draft 0.26 — 第三者実装における形式識別と適合範囲（未採択案）

外部ソフトは、JSONのフィールドが似ているという理由で別バージョンを推測してはならない。Scoreは`format`と`version`、Distributed Session 0.2はバージョンを含む`profile`文字列と`recordType`（`profileVersion`は使用しない）、Production Session 0.1.0／0.2.0は`profile`と必須の`profileVersion`で、対象のSchemaを厳密に選択する。未対応のバージョンは無損失に保持するか、破壊的保存を拒否する。JSON読込と、Score/Profile原本照合、外部Asset実体の保持、DSP・WAN同期・ロボット実行は別の対応機能である。詳細な対応表は`CONFORMANCE.md` Draft 0.26を参照する。4.2継承仕様と既存JSONフィールドは変更せず、日英校了と著作者の正式採用は未了である。

本書は4.3で新たに定義する意味規則です。4.2から継承する項目は本パッケージ内の`schema/ostf-4.2.0.schema.json`と公式4.2仕様（`docs/SOURCE_RECONCILIATION.md`参照）に従います。構造の正本は`schema/ostf-4.3.0.schema.json`、詳細な英文規範意味規則は`docs/SPECIFICATION.md`、全項目の正本は`docs/PARAMETER_REFERENCE.md`です。

## 1. 正本の維持

Timelineは構成・テンポ・拍子、Harmonyは和声、Tracks/Clips/Notes/MIDI Eventsは具体的な演奏、LyricsとAlignmentは歌詞・ノートの対応、VocalPerformanceは歌唱表現、Track Directionは生成・解釈に利用する演奏意図、Generation/Provenanceは履歴です。新4.3項目はこれらの正本を置換しません。読込時の自動生成、URL自動取得、AIへの外部送信、物理アクチュエータの自動駆動を行うよう指示するものではありません。

全ての時間付き新Core要素は既存PPQ/Tickに従います。絶対区間は`[start,start+duration)`の半開区間です。Track Directionは別時計を作りません。IDは表示名ではなく安定した文書内識別子です。既存Coreがもつ正本、重複禁止、未知データ保持の原則を継承します。

## 2. phrasing Direction

`tracks[].directions[]`に`type:"phrasing"`を追加します。既存Directionの封筒（`id`, `type`, `start`, `duration`, `parameters`）をそのまま使います。`parameters.adherence`（strict / preferred）は必須です。ほかに少なくとも1つの音楽パラメーターを指定します。

- `phraseLengthTicks`: `{min,max}`、それぞれ正の整数、`min<=max`。フレーズ分割の意図を表すものでClipを自動分割しません。
- `onsetGroupsPerQuarter`: `{min,max}`、0～128、`min<=max`。同一Track内の同Tick同時発音は1つの発音開始グループとし、フレーズ中の異なる発音開始数×PPQ÷フレーズ長Tickを密度とします。複数の同時和声音は1群です。
- `development`: repetition / motivicVariation / sequence / contrast / free。
- `contour`: ascending / descending / arch / valley / stable / free。全体的な音高輪郭であり、局所的な逆方向移動をすべて禁じる意味ではありません。
- `energyShape`: rising / falling / arch / valley / stable / free。抽象的な盛り上がりであり、Velocityや音量カーブの正本ではありません。
- `motifRef`: 既存`phraseLibrary.templates[]`に存在するIDを参照します。

音階は既存`improvisation`、音域は`pitchRange`、役割は`playingRole`が担当します。`phrasing`自体は実際のノートを変更しません。既存の具体的フレーズ境界が明示されない場合、strictなフレーズ長・発音開始密度の充足は機械的に確定できません。実装は任意の独自分割を規格唯一の正解と主張してはいけません。

## 3. vocalFreedom Direction

既存Direction封筒を用い、`parameters.voiceId`、`textPolicy`、`melodyPolicy`、`adherence`を必須とします。Voiceは同じTrackに属する既存`lyrics.voices[]`のIDに解決しなければなりません。歌詞とメロディの自由度はそれぞれ独立です。

- `textPolicy`: fixed（既存テキストを固定）、alternatives（明示した候補Phrase列から選択）、open（未確定）。
- `melodyPolicy`: fixed（既存旋律を固定）、ornamentable（装飾可）、open（未確定）。
- `vocalizationKind`: lexical / scat / humming / nonLexical（任意）。
- `candidatePhraseSets`: alternativesの場合に限り2個以上必須。各候補の`phraseIds[]`は対象VoiceのLyric Documentに属する既存Phrase ID列を参照し、完全に同じ候補を繰り返してはいけません。

候補選択・テキスト生成・旋律生成では、具体的なLyrics/Notes/Alignmentを書き換える前に明示的な編集操作を必要とします。生成されていない歌詞やノートを偽のプレースホルダーとして正本へ追加しません。発声表現は既存4.2のVocalPerformanceを使います。`melodic` Trackだからという理由だけでボーカルと推測しません。

## 4. ensembleInteractions

ルート任意配列`ensembleInteractions[]`はTrack/Voice間の方向付き関係です。`actorTrackId`は行動する側、`partnerTrackId`は対象です。異なる実在Trackの組合せを通常としますが、**同一Track内の異なる2つのLyric Voice**であれば同一Track IDの組合せも許します。この場合は`actorVoiceId`と`partnerVoiceId`がともに必須で、異なる実在Voiceを参照し、両方の`trackId`がそのTrackと一致しなければなりません。同じVoiceが自分自身を相手にする関係は不正です。異なるTrack間の関係ではVoice IDは任意ですが、指定する場合は所有Trackと一致する必要があります。

Relationは`respondTo`、`followRhythm`、`alternateWith`、`leaveSpaceFor`、`reinforce`の5種です。`adherence`は必須です。適用条件としてsourceの`start+duration`または`scope:{performancePlanId,visitId}`の少なくとも片方が必要です。双方がある場合は、そのVisitのsource区間との交差する部分だけに適用し、交差がなければ不正です。方向付きなので逆向き関係を自動追加しません。`responseWindowTicks`は音楽時間であり、ネットワーク遅延を表しません。

## 5. performancePlans

ルート任意配列`performancePlans[]`は`mode:"orderedFinite"`の有限の演奏順序です。各Planの`visits[]`は0から連続する一意の`ordinal`を持ちます。各Visitは参照するSection ID列またはSource Rangeのどちらか1つを必須とします。同一Visit内でSection区間が重複してはいけません。別Visitで同じSectionを再訪することは可能です。

訪問された元区間`[S,S+L)`が展開先Tick `P`から始まる場合、範囲内Tick `t`の演奏上位置は`P+(t-S)`です。Source Tickは元曲の正本であり、Performance TickはVisit展開から導かれる二次座標です。元のNote/Chord/SectionのIDを複製したことにはなりません。切替位置でSourceのTempo/Meter/Key/Harmonyを必ず再評価します。元の小節を無関係な前のVisitのテンポで演奏してはいけません。

`parts[].realization`はfixed（確定sourceノートを使用）、open（このVisitでは既存ノートも再生せず未確定の演奏として扱う）、silent（無音）の3つです。未記載TrackはPlanの`defaultRealization`（fixed/silent/unspecified）に従います。unspecifiedを勝手にfixedとみなして完全再生できるとは主張できません。

Visit固有の`parts[].role`は元Trackのデフォルト役割を当該Visitで一時的に置き換えます。同じsource区間に矛盾する`playingRole` Directionがあれば、`replacesDirectionIds`に該当IDを明示して衝突解決します。元Directionの削除・変更はしません。

### Source区間の境界での確定ノート／MIDI

`fixed`ではSource Noteの開始Tickが選択半開区間`[S,E)`内にある攻撃（Note On）のみを選択します。開始前から持続するNoteに境界SでNote Onを作りません。ただし**同一Visit内で前区間の終了Source Tickと次区間の開始Source Tickが一致し、同じTrackが双方で`fixed`のままなら連続結合**です。この場合、前区間内で開始したNoteのゲートを連続する次区間へ持続させ、境界で人工的なNote Off/Onを挿入しません。Source Tickのジャンプ・ギャップ、Visit変更、`open`/`silent`への切替ではハードカットし、残るゲートをその位置で終えます。元Noteの長さ・IDは変更しません。新区間の開始Tickで始まる別Noteはその新しい半開区間に一度だけ属します。連続結合では既に選択したMIDI制御状態を通常の時間順に保持できますが、不連続カットでは過去のCC/Program Change/Pitch Bendを暗黙に再生成・複製してはいけません。再生に必要な状態が不足すれば、その状態不足を報告します。詳しくは`docs/NOTE_AND_MIDI_CUT_SEMANTICS.md`を参照してください。

### Draft 0.40 追補 — `fixed`と演奏結果の決定性（未承認案）

`fixed`は各Visitで**既存のsource Note/MIDIイベントを選ぶ方式**を確定しますが、すべてのNoteが必ず発音し、常に同じVelocityになることは保証しません。OSTF 4.2の`track.enabled`、`clip.enabled`、`note.enabled`による再生可否を尊重し、無効な要素があっても元データを消さないでください。

- `note.probability`は0〜1、未指定は1。0は発音しません。0より大きく1より小さい場合、実際に選ばれる発音結果は未確定です。OSTFは乱数列・シード・Visitごとの抽選方法を標準化しません。同じsource Noteが2回出現しても同じ発音結果を強制しません。
- `note.velocityDeviation`は既存の相対的なVelocity変動終点で、未指定は0です。非ゼロ値だけでは具体的なVelocityの抽選結果は一意に決まりません。`velocity`自体が未指定の場合も、勝手に既定値を保存してはいけません。`releaseVelocity`と`pitchRole`などの4.2の意味は変更しません。
- 完全に決定的なNote/MIDI出力を主張する場合は、確定した発音の採否とVelocityを明示したノートへ具体化する必要があります。元Scoreを無断変更せず、必要に応じて新RevisionのScoreに異なるVisit出現ごとに固有Note IDを割り当てます。未確定のMIDI CC/Program状態についても別途報告します。
- `fixed`に含まれる不発音/確率的Noteと、`open`（元の固定演奏を使用しない）や`silent`（演奏させない）は異なります。どちらもファイル読込だけでAIに作曲や即興を実行させる指示ではありません。

この追補は4.2のNote状態の**意味の整理**であり、4.3 Schema/JSONフィールドや乱数方式の新設ではありません。例は`examples/25-source-note-repeated-visits.ostf`を参照してください。正式採用D01と文書・例の承認D04は保留中です。

## 6. performanceRequirements

`tracks[].performanceRequirements`は演奏者の能力の申告ではなく、**その楽曲パートの実現に必要な音楽上の能力**です。任意に`requiredPolyphony`、`requiredPitchRange`、`requiredArticulations`、`peakOnsetGroupsPerQuarter`を持ちます。既存`instrument.playablePitchRange`と矛盾する音域を定義してはいけません。演奏者の実力、ロボットの速度、関節、モーター、安全停止、レイテンシーはこのCoreの対象外です。

## 7. ID・重複・互換性

新Core要素IDは既存ID空間に属し、文書全体で一意とします。同Trackの`phrasing`同士は重複禁止。同Trackかつ同Voiceの`vocalFreedom`同士も時間重複禁止ですが、異なるVoice同士は重複できます。異なるDirection種類は独立であり、配列順や「後勝ち」は優先順位になりません。

4.2に存在しない任意情報を新規に推測せず、4.2有効文書を4.3へ移行できるようにします。4.3から4.2へ情報損失を伴って書き戻す場合は、失われるJSON Pointerを明示し、元の4.3文書を保持します。不明な情報を理解できないEditorは非破壊保存または保存拒否を行い、黙って破棄しません。

## 8. Distributed Session Profileとの境界

遠隔人間・AI・フィジカルAIは、楽曲Coreとは別のSession Profileで参加者・役割割当て・音楽演奏位置・時計観測・提案・承認イベントを共有します。Draft 0.6では`OSTF-Distributed-Session-0.2`を別冊として提案します。個別の通信プロトコルを規格の必須条件にせず、イベント受信だけでロボットを駆動しません。セッション提案や演奏状態は元の`.ostf`文書を自動変更しません。詳細は`docs/SESSION_PROFILE.ja.md`および`docs/SESSION_STATE_MACHINE.md`を参照します。

## 9. 機能適合と公開判定

OSTF Core Reader/Writer、Direction-aware、Ensemble-aware、Plan-aware、Vocal-aware、Requirement-aware、Session-profile-awareは独立した対応段階です。フォーマットに対応したというだけではAI生成能力・音質・ネットワーク遅延・ロボット動作を保証しません。今回の策定では動作・実機・独立パーサー検証をリリース判定条件から除外していますが、それらを検証済みとみなすものではありません。公開権利確認と編集上の仕様確定は引き続き必要です。

## 10. Draft 0.4 補足 — 同一Trackの複数VoiceとPlan展開後のNote識別

同一Track内で合いの手を行う複数のLyric Voiceは、`ensembleInteractions`で両方のVoice IDを明示し、異なるVoice IDである場合に限り相互関係を記述できます。Voiceは4.2のLyric Voiceが正本であり、同じTrackだからといってVoiceを統合したり音声チャンネルを自動追加したりしません。

同じSource Noteを複数のVisitで参照して演奏する場合、**元Note IDは同一**ですが、演奏上の各出現は`performancePlanId + visitId + sourceSegmentOrdinal + sourceNoteId`で識別できるものとします。この組はPlan解釈時の内部識別子であって、新しいCore NoteのIDではありません。Clip内相対Tickはまず元のSong Tickへ変換してからSource区間の半開境界を判定します。Source Noteを繰り返しても元のNotesを複製・変更しません。

Planの演奏結果を固定した新しいOSTF文書に保存する場合は、各出現のNoteに新しい一意のCore IDを付け、新文書Revisionと由来を記録します。読込やPlan参照だけではこの書き込みを行いません。

## 11. Draft 0.5 補足 — 固定Visitの歌詞・歌唱表現

同じ元Noteが複数Visitで演奏されても、元の`lyrics.units`や`lyrics.alignments`のIDは複製しません。各Visitでの演奏は異なる**出現**ですが、元の歌詞・ノート・VocalPerformanceの正本は変わりません。Source区間境界でNoteのゲートが切られた際、音素タイミングや歌唱表現の曲線が境界を越えている場合、それらを無条件に切り詰めて完全再現と宣言してはいけません。複数Noteに関連付く歌詞Unitの一部だけが選択される場合も、欠落・曖昧さを明示したうえで新しい文書への明示的な具体化を行います。`docs/SPECIFICATION.md`を参照してください。

## 12. Draft 0.5 補足 — 分散セッションの演奏開始

別冊Profile 0.2に`sessionStarted`を追加し、`prepared`から`playing`への遷移を明示します。演奏位置の時計アンカーはCore OSTFではなくSnapshot/Eventで管理します。任意の`commitmentWindow`によって確定済みSessionフレーズの完了範囲を主張できますが、未記載なら完全性の保証はありません。通信やロボットの安全性・実行能力は依然としてCoreの対象外です。

## 13. Draft 0.6 — 遠隔Sessionフレーズの確定条件

今回のCore Schema自体は変更しません。別冊Profile 0.2で承認されたフレーズは、固定されたPerformance Planの**明示的に`open`と指定された対象Track Part**の範囲にのみ割り当てられます。`fixed`に重ねる、`silent`を鳴らす、`unspecified`を未承認のまま`open`と解釈する操作は、規格上許されません。フレーズ全体が同一Visitに収まらない場合は分割・再提案します。`prepared`の段階でもPlanが固定されていなければ確定できません。詳しい意味規則は`docs/SESSION_STATE_MACHINE.md`です。4.3 Coreの正本や元のNoteは変えません。

## 14. Draft 0.7 — 楽曲Revisionの固定と遠隔演奏の履歴の分離

OSTF Coreの楽曲構造・演奏・歌詞の正本は、セッションの受信イベントでは変更されません。別冊Profile 0.2の1つのSessionは、同じ`documentId`・`revisionId`・有限の`performancePlanId`を参照し続けます。Web APIで新しい楽曲Revisionを取得しても、現在のSessionの楽曲を自動で入れ替えてはいけません。同じ文書ID・Revision IDで異なる内容を受け取った場合は、同一の演奏位置を共有できると見なさず、整合性の問題を報告します。

承認済み`phraseCommitted`はセッション内の**確定履歴**であり、音が鳴った証拠ではありません。`visitChanged`で後のVisitへジャンプして以前に確定したフレーズを飛ばした場合、または`sessionStopped`で将来の演奏が停止した場合、元の確定レコードは保持しますが、飛ばした/停止後のフレーズを演奏済みと表示してはいけません。Profile 0.2の演奏Tickは原則として前方へ進み、同一Sessionでの巻き戻しや新しい楽曲Revisionへの切替は扱いません。これらが必要な場合は、新しいSessionまたは将来の拡張仕様が必要です。

イベントの再送は`eventId`と内容の一致を**先に**調べ、既に承認済みの同一イベントなら、Revisionが進んでいても二重採用しません。同じIDの内容違いは不正であり、別IDで古い`baseStateRevision`のイベントも採用しません。演奏トラックの担当参加者を変更しても、確定済みフレーズを他のロボットへ自動実行させる意味にはなりません。必要な残作業と判定条件は別冊`docs/SESSION_STATE_MACHINE.md`に詳述します。

これは**4.3 Coreではなく別冊Session Profileに対する意味規則**です。Schemaは変更せず、公開者による採用判断が必要な策定案です。

## 15. Draft 0.8 — 別冊Distributed Session Profileのデータ整合性

OSTF 4.3 Coreを変更せず、未公開の別冊Session Profile 0.2の`assignmentChanged`では`position`と`targetVisitId`をそれぞれ禁止します。以前のSchema条件式は`position`の単独混入を拒否できなかったため、今回は構造的に修正しました。担当者の変更は演奏の時計アンカーを変更できません。時計アンカーを持つ遷移は`sessionStarted`のみです。保持されたすべての`committedPhrase`のNoteは、`commitmentWindow`の有無にかかわらず親Phraseの半開区間内に収まらなければなりません。停止やスキップによって歴史的な承認済みPhraseが残っていても、現在の担当者や実発音の存在を証明しません。再送された同一IDを確認する際は認証・固定楽曲Revisionの照合を先に行い、その後にID内容の一致を確認し、新規イベントだけに状態Revisionの新旧照合を適用します。数値の比較は十進数の正確な値で行い、損失のある型変換で同一と推測しません。詳細は`SESSION_STATE_MACHINE.md` Draft 0.8節を参照してください。これらは公開者の承認前の案です。

## Draft 0.9 — 別冊分散セッションのPlan固定とバイト列照合

OSTF 4.3 CoreのSchemaおよび4.2から継承した音楽上の正本は変更しません。**別冊の未公開Distributed Session Profile 0.2のみ**、全SnapshotとEventにルート直下の`performancePlanId`と`scoreSha256`を必須としました。`prepared`でPositionがなくても参照する有限Performance Planを確定できるようになります。`scoreSha256`は取得した元OSTFの正確なUTF-8バイト列のSHA-256であり、文書名・Revisionだけが一致する異なるJSONを無断で同じ演奏に使わないための照合値です。Position内のPlan IDはルートと一致させます。SHA-256は認証・所有権・実機駆動の許諾ではありません。詳細と規範的な判定順序は`SESSION_STATE_MACHINE.md` Draft 0.9節に定義します。

## Draft 0.10 — 遠隔Visit切替の時計基準

**別冊の未承認Distributed Session Profile 0.2のみ**を改訂します。従来`visitChanged`は移動先Visit IDだけを記述していましたが、遠隔演奏の切替時刻を再特定する必要があるため、`position`を必須とします。`position.visitId == targetVisitId`、`position.performanceTick == Event.effectivePerformanceTick == 対象Visitの開始演奏Tick`とし、`sourceTick`はVisitが最初に参照するソース区間の開始Tickとします。UTC時刻`epochUtc`はそのTickを示す推定時計基準で、受信時刻ではありません。これは演奏位置の意味情報であり、通信・ロボット制御の安全性や音声出力を保証しません。OSTF 4.3 Core、4.2正本、既存NoteやLyricsは変更しません。

## Draft 0.11 — 分散セッションの時計ドメインとテンポの整合（未承認）

別冊Profile 0.2では、`sessionStarted`で設定した音楽時計の`clockDomainId`を、演奏中のSnapshotと`visitChanged`の新しい時計基準位置でも維持しなければならない。演奏途中の時計ドメイン変更はProfile 0.2では表現できず、新しいSessionを必要とする。`position.tempoBpm`は説明情報で、元OSTFの`timeline.tempoChanges`の`sourceTick`で有効な値と一致しなければならない。Session側のテンポで元の楽曲を書き換えない。`sessionStopped.effectivePerformanceTick`は記録上の位置であり、将来停止予約またはロボットの緊急停止命令ではない。詳細は`SESSION_STATE_MACHINE.md` Draft 0.11および`SESSION_PROFILE.ja.md`を参照する。これらはCore 4.3への新パラメーター追加ではなく、公開者の最終採用待ちの意味規則である。

## Draft 0.12追補：遠隔セッションの有効テンポと時計基準（未承認）

別冊Distributed Session Profile 0.2の`playing` Snapshot、`sessionStarted`および`visitChanged`が提示する`position`は、固定されたOSTF原曲の`sourceTick`において有効なTempoを解決できなければなりません。`position.tempoBpm`の省略をデフォルトテンポの存在と解釈してはいけません。テンポ未解決の演奏中時計位置は`E-SESSION-TEMPO-UNRESOLVED`として拒否します。元の曲の選択区間とテンポ変更点ごとに `60 × Tick差 / (PPQ × BPM)` を積算し、省略区間の時間やテンポを暗黙に継承してはいけません。これは理想的な音楽時刻の定義で、遠隔地での実時計精度や物理動作の保証ではありません。さらに別冊ProfileのSnapshotの`participants[]`は1名以上必要です。いずれも4.3 Coreの楽曲フィールドを変更しない編集案です。

## Draft 0.13 — 別冊Production Session Profile 0.1.0

第三者製の独立した音楽制作アプリのために、Mixer（Mute/Solo/音量/Pan）、音声Bus/Send、エフェクト・音源の順序付きDevice Chain、Plug-in IDと不透明State参照、Automation、Host固有データを表す任意の別冊JSON Profile案を追加します。**OSTF 4.3 CoreとDistributed Session Profile 0.2のSchemaは変更しません。** Core `track.enabled`とAudio Mixer Mute、MIDI CCと音声Mixerは異なる正本として維持します。定義案は`PRODUCTION_SESSION_PROFILE.ja.md`、型と値域は`PRODUCTION_PARAMETER_REFERENCE.md`を参照してください。著作者による採用承認は未了です。

## Draft 0.20：別冊ProfileとScore改訂時の責任分離

本改訂ではOSTF 4.3 Coreのフィールド・定義を変更しない。Scoreが新しい実体バイト列・Revisionになった場合、別冊Production Profileは旧版を保持したまま、Track参照と元source Tickの録音/Automationを著者がレビューして新しいコピーへ明示的に再関連付けできる。一方、Distributed Sessionは旧Score/Plan/Clock/Event履歴をそのまま維持し、**新しいSession IDが必要**である。`score.sha256`だけの書換えで安全な無損失変換とみなしたり、Web APIの自動取得・プラグイン実行・ロボット動作の権限を認めたりしてはならない。未採用の規範候補の詳細はProduction Profile日英第26節。

## Draft 0.21 — 無損失保存とProfileの対象範囲

新しいCoreフィールドは追加しない。OSTF ScoreとProduction/Distributed Session Profileは独立した正本・版番号を持つ。Coreのみを読み込むソフトは別冊Profileを無視してよいが、受領した制作プロジェクト全体の「無損失保存」を主張しながら、別冊Profileや不透明Asset本体を黙って破棄してはならない。未対応の新しい意味情報を保存できないWriterは、無損失上書きを拒否するか、利用者に損失を明示した別のExportとする。Score原本のバイト列が変われば旧Profileのハッシュ固定は無効で、Productionの再関連付けは著者が新しいコピーとして明示的に行う。Distributedの既存Sessionには付け替えず、新しいSession IDを用いる。具体的な未採用規範案は`CONFORMANCE.md`とProduction Profile第27節。ソフトウェアの実装・プラグイン実行・フィジカルAIの動作を定義するものではない。

## Draft 0.22 — Coreと別冊Profileの正本の分離（未採用）

OSTF 4.3はバージョン付きの**楽曲Score JSON**である。Production Session ProfileとDistributed Session Profileは**別々の版を持つ任意のJSON文書**であり、隠れたOSTF Coreフィールドではない。各Schemaは宣言された文書の構造にのみ適用し、CoreのNote、Track、Harmony、Lyrics、MIDIの正本を変更しない。開発ZIP、`PACKAGE_MANIFEST.json`、`SHA256SUMS.txt`は規格配布用であり、制作プロジェクトの標準コンテナーやHTTP APIを定義するものではない。

規格の適合では、各Schemaの構造、独立した規範案、例示、外部Assetの**実体の有無**、DAW/ロボット等の実行を区別する。旧Draftと現行規範案に解釈の矛盾があれば、文書の更新順や配列順から暗黙の優先順位を作らず、公開者の編集上の決定として解消する。`CONFORMANCE.md`とProduction Profile第28節を参照。新しいCoreパラメーターは追加しない。

## Draft 0.23 — Score・別冊Profileの解釈順序（未採用の編集案）

過去Draftの記述を残しているため、実装者は以下を現行案の基準とする。フィールドの型・必須性は**文書ごとの版に一致するJSON Schema**、4.2から継承する音楽的な意味は正式4.2仕様、4.3の新しい意味は本書の現行4.3規範案、Distributed/Productionの意味は**各別冊Profileの版別規範案**で解釈する。以前の編集履歴を、現在の原本ハッシュ固定や元Score Tickの扱いを上書きする代替規則として使ってはならない。現行規範案同士が矛盾する場合は公開者が決定する未解決事項であり、配列順や「新しい記述優先」をアプリが推測してはならない。

`scoreSha256`と`score.sha256`はそれぞれ**別冊Profile**のフィールドであり、Core 4.3の新しいルート項目ではない。元ScoreのUTF-8**実バイト列**を照合する。セッション内の`phraseCommitted`はDistributed Sessionの履歴であり、Scoreの`notes[]`、Productionの`audioRegions[]`、プラグイン設定を自動変更しない。複数文書の関連付けは、外部リソースの取得・ソフトのインストール・ロボット駆動の許可にはならない。**新しいJSON項目は追加しない。**

## Draft 0.24 — 3領域の版選択と状態変更の責任分界（未採択案）

OSTF楽曲本体はルート`format:"OSTF"`と`version:"4.3.0"`で識別します。分散セッションSnapshot/Eventは`profile:"OSTF-Distributed-Session-0.2"`と`recordType`で識別し、**`profileVersion`を持ちません**。Production Profileは`profile:"OSTF-Production-Session"`と`profileVersion:"0.1.0"`または`"0.2.0"`で識別します。構造上、これらを1つのJSONへ暗黙統合する仕様ではありません。

分散セッションの新規状態変更イベントは、現在のRevisionと`baseStateRevision`が一致しなければ確定してはいけません。一方、元から承認済みで全データが等しい同一`eventId`再送は、認証・楽曲固定情報の照合後、冪等な無操作とします。異なる内容への再利用は禁止です。詳細は`SESSION_STATE_MACHINE.md`に委ね、CoreのNote/MIDI/歌詞は変更しません。著作者の正式採用と公開権利承認は引き続き未完了です。

## Draft 0.25 — 第三者実装と正本の分離（未採択案）

OSTF 4.3の確定済みノート・MIDI、音楽的演奏指示、遠隔セッションの承認イベント、制作環境のミキサー/音声リージョン/プラグイン状態は、それぞれ別の正本を持つ。JSONを読み込めても、全データの無損失保存、音声処理、ロボット制御まで対応したとは主張できない。**元のAssetバイトが未入手なら、参照記述子の保存は「音源実体の保持」と同義ではない。** 分散セッションの承認フレーズはScoreのノートを自動追加しない。Scoreの新Revisionに従属Production/Distributedを暗黙に移行しない。

詳しい第三者実装の対応表・失われる情報の分類・規範資料の参照先は`CONFORMANCE.md`のDraft 0.25を参照する。4.2継承の正本と6 Schemaは変更せず、日英校了・著作者による新規規範採用・公開権利承認を要する。



## Draft 0.35 — Schema選択・サンプル対応表（規範案・未承認）

データの読み込み時には、楽曲Coreの `format` と `version`、Distributed Sessionの `profile` と `recordType`、Production Sessionの `profile` と `profileVersion` を識別し、厳密に対応するSchemaを選択する。未知の版を既知の版に無断で置き換えない。

同梱45件のJSONサンプルは、Core楽曲25件、Distributed Session 17件（0.1の2件と0.2の15件）、Production Session 3件（0.1の2件と0.2の1件）である。ファイルごとの対応は `docs/EXAMPLES_GUIDE.md` に示す。これは同梱例の索引であり、機能の網羅性や独立実装の相互運用性を保証するものではない。

対応を表明するソフトウェアは、構造的読込、参照の整合、受領した情報の無損失保持、意味の解釈、音響・ロボット実行をそれぞれ区別しなければならない。Schemaへの適合だけでプラグイン起動・遠隔イベント受理・ロボット制御を許可しない。これらの文面はD01〜D04で正式採択待ちである。

### Draft 0.41 — 連続するSource区間の結合と不連続カット（未採択）

A `[0,3840)`→B `[7680,11520)`は元の時間軸が飛ぶため、Aの終端3840で持続中のNoteを切ります。一方B `[7680,11520)`→C `[11520,15360)`が同一Visitで、該当Trackの`fixed`を維持するなら連続結合です。Bで11280から720 Tick持続するNoteはCの先頭をまたぎ、元Source Tick12000まで持続できます。C開始11520に別NoteがあればC側のNote Onとして一度だけ扱います。次のVisitへ移る場合は、Source Tickが偶然連続していてもハードカットとします。新しいフィールドではなく、Performance Planの再生対象となるSource Note/MIDIの選択・ゲートの意味規則案です。`probability`や`velocityDeviation`の実際の決定、楽器音源の音声Tailや録音リージョンのFade、音素・ロボット動作の連続性を保証するものではありません。D01（音楽的意味規則）とD04（翻訳/例の校了）の明示的承認が必要です。


## Draft 0.42 — 有限Performance Planにおけるノート指定MIDIイベント（D01/D04未承認）

4.2から継承するCC、Pitch Bend、Channel Pressure、Poly Pressureの`targetNoteId`は、**保存済みの元Noteとの意味上の関連**です。MIDI Channel/Pitchの伝送上の意味や実際のMPEルーティングを置き換えるものではありません。以下は`fixed`の演奏区間を展開する際の規範候補であり、元の4.2データの改変を要求しません。

1. MIDI Eventの元楽曲位置は`clip.start + midiEvent.start`とし、各Visitの`fixed` Partが選んだ半開区間に入るイベントだけを、その元IDで一度選択します。区間の終端Tickは次の区間に属します。省略された小節のイベントからProgram/CC等の初期状態を捏造しません。
2. `targetNoteId`のないイベントは元のChannel/Busのイベントです。省略区間のコントローラー状態は補完されず、ハードカット直後には状態が不明な場合があります。
3. `targetNoteId`のあるイベントの**演奏上の対象Note**を確定できるのは、そのNoteの発音開始が選択され、当該Tickまで同一Visit内の連続した`fixed`区間でゲートが有効なときだけです。選択外の小節で発音したNoteは、その後のCC等の時刻が選択区間に入っても自動的には選択されません。連続Sectionで持続中のNoteは、元の攻撃位置に対応する一つの出現のままです。
4. 対象Noteが選択されない、無効化されている、または発音確率により実出力が未確定の場合、当該イベントを**別のNoteやtargetなしのChannelイベントに無断で読み替えてはいけません**。元のEventのバイト/参照は保持します。確定MIDI出力には明示的な省略・保持・近似の方針と損失報告、または出力拒否が必要です。MPE/マルチティンバーでは特に重要です。元Scoreの構造不正とは限りません。
5. 展開した診断上のNote出現は`(performancePlanId, visitId, sourceAttackSegmentOrdinal, sourceNoteId)`、イベント出現は`(performancePlanId, visitId, eventSegmentOrdinal, midiEventId)`で識別できます。連続SectionをまたいでNoteが持続すると、両者のSegmentOrdinalは異なっても構いません。これらは保存用の新しいCore IDではありません。新しいScoreに確定保存する場合にのみ、新規Core IDと妥当な`targetNoteId`参照を生成します。
6. 4.2の`order`は同TickのMIDI Event順序に従来どおり適用しますが、MIDI EventとNote Onとのすべての順序を新規に定義しません。決まらない実行順序を勝手に確定したと扱いません。

**サンプル17：** `target-prior-note-selected`は選択されたNoteを参照します。`ctrl-omitted-gap`は選択外です。`target-prior-note-not-selected`の元Noteの攻撃Tickは7400で、次のSectionに含まれないため対象を確定できません。一方`target-across-contiguous-join`は、連続するTwo→Threeの境界を越えて持続しているNoteを参照できます。これは静的な規格例であり、DAW/MIDI音声処理・ロボット実機検証を意味しません。

## Draft 0.45 — Voice／Clip全体の歌唱表現の投影（S24、未承認）

4.2の`VocalPerformance`では、`noteId`を持たない`phonemeEvents`、
`targetNoteId`を持たない`techniques`や`expressionCurves`、独立した
`breathEvents`を記録できます。これらを、歌詞Alignmentが存在するだけで
特定Noteに結び付けてはいけません。4.3の有限`fixed` Planでは、個々の
時間付きイベントの開始位置を`clip.start + item.start`でSource Tickに
変換し、選択した半開区間に開始位置がある場合にだけ派生出現を認めます。
選択外の開始位置を区間先頭に移動しません。同一Visitの連続fixed区間を
またぐイベントは一回の出現として継続し、ジャンプやVisit変更による
hard cutでは残りを切断します。`noteId`を持たない音素の`unitId`を、
根拠なくNoteのAlignmentへ変換しません。

`targetNoteId`を持たない表現カーブはVoice／Clip全体の情報です。
複数点の場合は元Source Tickでの指定点間のみ既存4.2の補間が定義され、
範囲外は未指定です。一点だけのカーブは元Clip／Voiceの適用範囲で
定数です。区間ジャンプ後に前Visitの値を持ち越さず、未指定値を
`0.5`などで補完せず、原本への境界点の自動追加もしません。
既存のNote単位のカーブとの置換関係は4.2の規則を継承し、二重加算しません。
ブレスなどの非Note対象イベントは、休符中に存在してもNoteの実発音を
証明しません。確定歌唱として書き出す場合は新RevisionとID再対応、
切断・近似・未解決音素の情報損失を明示します。具体例は
`examples/15-vocal-response-phrasing.ostf`、詳細は英語規範案のS24です。
これらはD01/D04の採用待ちで、Schemaの新フィールドではありません。


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
