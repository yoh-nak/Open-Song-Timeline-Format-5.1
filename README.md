# Open Song Timeline Format (OSTF) 5.1.0 — Take & Comp

**Official written specification release · 2026-11-25 · Release tag: `v5.1.0`**

OSTF is an open, DAW-independent format for song structure, harmony, MIDI, lyrics, musical intent and optional production/project data. This complete 5.1 edition integrates the publisher's 5.0 release with non-destructive **Takes, Comp maps, materialized results and launch/Visit selection**. No separate 5.0 download or schema-merge step is required to read this distribution.

## GitHub publication layout

The complete distribution contains **100 files**, including documentation, Schemas, samples, licenses and reference utilities. [FILE_INDEX.md](FILE_INDEX.md) lists every file by purpose and gives the recommended reading order. The ZIP has no enclosing wrapper folder; place its extracted contents at the repository root.

Start with [the complete manual](docs/COMPLETE_MANUAL.md), use [the full parameter reference](docs/PARAMETER_REFERENCE.md) for fields and constraints, and open [the sample catalog](docs/EXAMPLES_GUIDE.md) for `.ostf` and `.ostfp` cases. Historical sources are labeled separately in the index. Use [RELEASE_NOTES.md](RELEASE_NOTES.md) for the `v5.1.0` release text.


## Two file forms

- **OSTF TEXT — `.ostf`:** standalone BOM-free UTF-8 JSON Score.
- **OSTF PROJECT — `.ostfp`:** optional ZIP carrying one Score and its companion JSON/audio/state bytes, with exact hashes and bindings.

Production, Distributed and Plugin support remain optional. OSTF is a data specification; it does not implement a DAW or establish a native VST3/AU/CLAP transport API.

## What 5.1 defines

- Takes on arbitrary source-score Tick ranges: Sections, bars, chords and phrases use the same coordinate model.
- Preserved disabled/muted source candidates, separate Comp interval maps and distinct ordinary playback outputs.
- Multiple Comps, explicit silence and null selection; no competing activeTake flag.
- MIDI truncate/retrigger/authored boundaries, note lineage, controller/vocal consistency obligations.
- Audio region or rendered output, source-phase preservation and explicit linear/equal-power/custom transitions.
- Finite Visit selection and fixed/manual/cycle/random/weighted launch policies. Saved selection is separate from playback overlays.
- Score5.1-scoped atomic Plugin1.1 take editing; independent Production and Distributed authority.
- Explicit 5.0 projection preserving the saved active result and reporting lost take/selection information.

OSTF Studio may present Section-by-Track clips; the open format does not require that interface or a particular DAW's lane layout.

## Documentation

| Document | English | 日本語 |
|---|---|---|
| Integrated specification | [Specification](docs/SPECIFICATION.md) | [正式仕様](docs/SPECIFICATION.ja.md) |
| Complete manual | [Manual](docs/COMPLETE_MANUAL.md) | [全網羅マニュアル](docs/COMPLETE_MANUAL.ja.md) |
| All fields and constraints | [Reference](docs/PARAMETER_REFERENCE.md) | [全網羅リファレンス](docs/PARAMETER_REFERENCE.ja.md) |
| All example files | [Catalog](docs/EXAMPLES_GUIDE.md) | [サンプル一覧](docs/EXAMPLES_GUIDE.ja.md) |
| OSTF Studio session view | [Implementation guide](docs/OSTF_STUDIO_IMPLEMENTATION.md) | [Studio実装ガイド](docs/OSTF_STUDIO_IMPLEMENTATION.ja.md) |
| Production / audio | [Production0.4](docs/PRODUCTION_SESSION_0_4.md) | [制作0.4](docs/PRODUCTION_SESSION_0_4.ja.md) |
| Distributed / AI | [Distributed0.4](docs/DISTRIBUTED_SESSION_0_4_SPECIFICATION.md) | [分散0.4](docs/DISTRIBUTED_SESSION_0_4_SPECIFICATION.ja.md) |
| Project container | [Package1.1](docs/PACKAGE_SPECIFICATION.md) | [パッケージ1.1](docs/PACKAGE_SPECIFICATION.ja.md) |
| Plugin / host editing | [Plugin1.1](docs/PLUGIN_EXCHANGE_PROTOCOL.md) | [プラグイン1.1](docs/PLUGIN_EXCHANGE_PROTOCOL.ja.md) |
| Migration and loss | [Migration](docs/MIGRATION_MATRIX.md) | [移行・情報損失](docs/MIGRATION_MATRIX.ja.md) |
| Feature declarations | [Conformance](docs/CONFORMANCE.md) | [機能別適合](docs/CONFORMANCE.ja.md) |
| Import boundaries | [Security](docs/SECURITY.md) | [取込み規則](docs/SECURITY.ja.md) |
| Exact formats and versions | [Format registry](docs/FORMAT_REGISTRY.md) | [形式・版の対応表](docs/FORMAT_REGISTRY.ja.md) |
| Cross-object requirements | [Semantic requirements](docs/SEMANTIC_REQUIREMENTS.md) | [意味規則索引](docs/SEMANTIC_REQUIREMENTS.md) |

## Version families

| Family | Current version | Previous version |
|---|---|---|
| OSTF Core / Score | **5.1.0** | 5.0.0 |
| Production Session | **0.4.0** | 0.3.0 |
| Distributed Session | **0.4** | 0.3 |
| OSTFP Manifest | **1.1.0** | 1.0.0 |
| Plugin Context | **1.1.0** | 1.0.0 |

Exact legacy/current combinations are in [Format Registry](docs/FORMAT_REGISTRY.md). A 5.0-only reader is not assumed to accept 5.1 directly; use explicit downgrade/export. Original 5.0 Schemas are retained unchanged, as are the thirteen adopted 4.3 files.

## Distribution contents

- **5 complete current Schemas**, **5 preserved 5.0-family Schemas**, and **3 adopted 4.3 Schemas**.
- Complete Japanese/English manuals and references covering **2,341 explicit current Schema declarations**.
- **36 example files:** 22 `.ostf`, 6 `.ostfp`, 2 Production, 3 Distributed and 3 Plugin JSON files. The catalog maps all 25 original 5.0 Score themes to retained or consolidated examples.
- Original synthetic PCM audio, retained source Takes and authored Comp outputs inside Audio packages.
- CC0 specification/data license, MIT reference-code license, provenance, release notes and `SHA256SUMS.txt`.
- **100 repository files**; each `.ostfp` is one repository file containing its own declared members.

## Optional static reference utilities

```sh
python -m pip install jsonschema
python tools/validate_examples.py
python tools/ostfp.py validate examples/ostfp/05-audio-linear-comp.ostfp
```

These utilities are supplied for developers and were not executed for this 5.1 release. They perform partial static checks and do not prove full Comp semantics, DAW behavior or interoperability. Release assembly included document/Schema/inventory consistency work; no DAW, audio playback, plugin, independent implementation or network runtime validation was performed.

## Release and license

**The specification is ready for release as `v5.1.0`.** Specification decisions are approved; runtime validation is excluded from the publisher's release criteria. [Release status](docs/RELEASE_CHECKLIST.md) distinguishes the completed artifact from remote publication. This ZIP does not itself upload a repository or create a GitHub tag.

Author-controlled specification, Schemas and original example data use [CC0](LICENSE); original reference tools use [MIT](LICENSE-CODE). See [license policy](LICENSE-POLICY.md), [notice](NOTICE.md) and [provenance](docs/PROVENANCE.md). The package MIME is proposed/unregistered and Schema `$id` identifiers do not imply hosted endpoints.
