# OSTF 5.1.0 — Source provenance

Integrated release date: **2026-11-25**. Source retrieved from the publisher's existing release artifacts, not reconstructed from search snippets.

| Input | SHA-256 |
|---|---|
| OSTF_5.0.0_GitHub_Release.zip | `e3c9cfc85cd9ff2ebcb93b2a6f0255307066e12c8bfd452a29cbcdf8c709ca55` |
| OSTF_5.1.0_Take_Comp_Specification_Delta.zip | `6334c3907f44d9bb5a909ac8308ed74a62c730d1b24c7f6edf7d4d60c6880574` |

The baseline identifies its public repository as https://github.com/yoh-nak/Open-Song-Timeline-Format-5.0 . The release archive above, rather than an inferred Git commit, is the exact byte source for this integration. No commit SHA or new remote tag is asserted.

The five original 5.0-family Schemas and thirteen adopted 4.3 files are unchanged. Current documents integrate 5.0 semantics and the completed 5.1 take rules. New file names carry their actual version; legacy files are not overwritten or relabeled.

## Current precedence

The current 5.1 SPECIFICATION, current family specifications and exact current Schemas govern this edition. Explicit 5.1 additions override earlier exclusions of comping. Unchanged 5.0 musical meanings inherit publisher-adopted 4.3 semantics. Historical Draft/approval text in source appendices records history, not an outstanding 5.1 release approval. The publisher has approved specification decisions and waived runtime validation for this release.

This integration refines the preliminary delta by defining saved-output selection overlays, preserving Production Audio independence from Core part realization, specifying source phase/envelope handling, and allowing narrowly scoped Plugin1.1 Core take edits. It also makes structural conditions explicit in the complete Schemas. These are approved specification decisions, not claims of software behavior.

Historical relative links inside unchanged adopted-4.3 sources may refer to documents or examples from that historical release which are not repeated here. Current manuals rebase available links and label omitted historical references; use the current documentation index for this edition.

## Preserved original files

| File | SHA-256 |
|---|---|
| `adopted-4.3/docs/COMPLETE_MANUAL.md` | `25f4a52316861e9cb588a1374cc2eaa972d6f93bc362e9e66223dc3eaf15acfe` |
| `adopted-4.3/docs/PARAMETER_REFERENCE.md` | `d0d83af99a98701061713f52aaf7347fd2afb17068a68c7db3519298dc67dedf` |
| `adopted-4.3/docs/PRODUCTION_PARAMETER_REFERENCE.md` | `24cf4a3c53f3beffbe10bd934c24d809b9cc53ea867e7ef2652b9d68d749b8e2` |
| `adopted-4.3/docs/PRODUCTION_SESSION_PROFILE.ja.md` | `132ae206526eb92f4c042ce234bc702a95d7553ea51d4d603de8f6501594f023` |
| `adopted-4.3/docs/PRODUCTION_SESSION_PROFILE.md` | `42f12628afbcbdce72787b94675f5ba1e292ae7ccccae079cf1bc3c8174ba61b` |
| `adopted-4.3/docs/SESSION_PARAMETER_REFERENCE.md` | `700e8f0731a18ab8b1e8b0d1ec91ab77f682799ce45f44e39fa3796930917915` |
| `adopted-4.3/docs/SESSION_PROFILE.ja.md` | `4b8e8f3f94eff07d24b3dc54dedca57051a365de3ce2020ea66d256b5405aa65` |
| `adopted-4.3/docs/SESSION_PROFILE.md` | `18196c82e9eeac97b79b639245637b89c43233671ddde834c6407a76d8b07dd2` |
| `adopted-4.3/docs/SPECIFICATION.ja.md` | `bc5b06e6edd413f1c11fd6bc513e73954005fead0aa82b9bd2f9cd96311f9989` |
| `adopted-4.3/docs/SPECIFICATION.md` | `075a51db61239fa75cc27d8e402f67759bc852cbe0b8e196dcd9539fc2c8a145` |
| `adopted-4.3/schema/ostf-4.3.0.schema.json` | `72bf44666b42a760c883fbfa87e1da891467768032ee8e96fbee9fb47f673fc7` |
| `adopted-4.3/schema/ostf-distributed-session-0.2.schema.json` | `f79832adea0e48d6042c820a7d7a51e7a7288944bde833e255ce96c22b5ed0e7` |
| `adopted-4.3/schema/ostf-production-session-0.2.schema.json` | `1ac57129bfc1def9d5e1529b32d3905495c86e0d0b1f7530199a4dce72037e29` |
| `schema/ostf-5.0.0.schema.json` | `616f003c90c54bcfa8a2334d38027c4a96ea608456a48a53cccafd0d82741bc8` |
| `schema/ostf-distributed-session-0.3.schema.json` | `391149b9cffda1e5f79deada00c1f0da3bd17c372b08dab777bcd8f14b2134f8` |
| `schema/ostf-package-manifest-1.0.schema.json` | `e07002207f845387e73bd569ed7911a58dc59b47973785f5a64aefa40e4b4056` |
| `schema/ostf-plugin-context-1.0.schema.json` | `a7902770e108c601a0bc144a23d5c85e91677689675e1f1fe0805d73edccc598` |
| `schema/ostf-production-session-0.3.schema.json` | `5bc4e273f264becde46d940892eb58e17b145c1522d192500c305730f59b6047` |
