# OSTF 5.1.0 — 形式と版の登録表

正確な文書内識別子でSchemaを選びます。拡張子や表示名から版を推定しません。5.0・4.3のSchemaは原本を保持し、現行Schemaで旧文書を勝手に再ラベルしません。

| Family | Version | Exact identity | Schema |
|---|---|---|---|
| Score | 5.1.0 | `format=OSTF; version=5.1.0` | [ostf-5.1.0.schema.json](../schema/ostf-5.1.0.schema.json) |
| Production | 0.4.0 | `profile=OSTF-Production-Session; profileVersion=0.4.0` | [ostf-production-session-0.4.schema.json](../schema/ostf-production-session-0.4.schema.json) |
| Distributed | 0.4 | `profile=OSTF-Distributed-Session-0.4; recordType=snapshot/event` | [ostf-distributed-session-0.4.schema.json](../schema/ostf-distributed-session-0.4.schema.json) |
| Manifest | 1.1.0 | `packageFormat=OSTFP; packageVersion=1.1.0` | [ostf-package-manifest-1.1.schema.json](../schema/ostf-package-manifest-1.1.schema.json) |
| Plugin Context | 1.1.0 | `protocol=OSTF-Plugin-Context; protocolVersion=1.1.0` | [ostf-plugin-context-1.1.schema.json](../schema/ostf-plugin-context-1.1.schema.json) |
| Score | 5.0.0 | `format=OSTF; version=5.0.0` | [ostf-5.0.0.schema.json](../schema/ostf-5.0.0.schema.json) |
| Production | 0.3.0 | `profile=OSTF-Production-Session; profileVersion=0.3.0` | [ostf-production-session-0.3.schema.json](../schema/ostf-production-session-0.3.schema.json) |
| Distributed | 0.3 | `profile=OSTF-Distributed-Session-0.3` | [ostf-distributed-session-0.3.schema.json](../schema/ostf-distributed-session-0.3.schema.json) |
| Manifest | 1.0.0 | `packageFormat=OSTFP; packageVersion=1.0.0` | [ostf-package-manifest-1.0.schema.json](../schema/ostf-package-manifest-1.0.schema.json) |
| Plugin Context | 1.0.0 | `protocol=OSTF-Plugin-Context; protocolVersion=1.0.0` | [ostf-plugin-context-1.0.schema.json](../schema/ostf-plugin-context-1.0.schema.json) |
| Score | 4.3.0 | `format=OSTF; version=4.3.0` | [ostf-4.3.0.schema.json](../adopted-4.3/schema/ostf-4.3.0.schema.json) |
| Production | 0.2.0 | `profile=OSTF-Production-Session; profileVersion=0.2.0` | [ostf-production-session-0.2.schema.json](../adopted-4.3/schema/ostf-production-session-0.2.schema.json) |
| Distributed | 0.2 | `profile=OSTF-Distributed-Session-0.2` | [ostf-distributed-session-0.2.schema.json](../adopted-4.3/schema/ostf-distributed-session-0.2.schema.json) |

## 組合せ

| Score | Production | Distributed | Manifest | Plugin Context |
|---|---|---|---|---|
| 4.3.0 | 0.2.0 | 0.2 | 1.0.0 / 1.1.0 | 1.0.0 / 1.1.0 |
| 5.0.0 | 0.3.0 | 0.3 | 1.0.0 / 1.1.0 | 1.0.0 / 1.1.0 |
| 5.1.0 | 0.4.0 | 0.4 | 1.1.0 | 1.1.0 |

Production/Distributed/Pluginは任意であり、Coreだけの実装に必須ではありません。Distributedの`documents[].version`は`0.2`/`0.3`/`0.4`、Productionは`0.2.0`/`0.3.0`/`0.4.0`です。DistributedにprofileVersionやネストしたscoreを足しません。

`.ostf`はBOMなしUTF-8 JSON、`.ostfp`はmimetypeを先頭Stored、manifest.jsonを2番目に置くZIPです。`application/vnd.ostf-project+zip`は未登録の提案値。Schemaの$idは識別子でありWeb配信を意味しません。Score/AssetのSHAは元バイトのSHA-256です。
