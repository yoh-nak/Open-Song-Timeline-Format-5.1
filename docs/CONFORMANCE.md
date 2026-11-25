# OSTF 5.1.0 — Independent capability declarations

Capabilities are independent, not a mandatory level hierarchy. Every declaration includes document family, exact version and operation such as read/write/edit.

| Capability | Scope |
|---|---|
| `score-read/write` | Exact Score version, Core semantics and unknown-data retention |
| `take-preserve` | Consistent preservation of candidates, maps, outputs, selections and metadata |
| `midi-comp-edit` | MIDI candidate/selection/output editing with note and MIDI-state materialization |
| `audio-comp-edit` | Audio candidates, frames, phase, transitions, output and asset retention |
| `visit-selection` | Finite Plan/Visit range and selection overlay |
| `live-selection` | Launch-time policies and unsupported-feature disclosure |
| `production-read/write` | Version, Score pin and declared Channel/Device/Audio/Automation scope |
| `distributed-read/authority` | Session pin, state, events and independently established authority |
| `project-read/write` | OSTFP version, inventory, raw SHA, size, paths and bindings |
| `plugin-context-consume` | Treat Context as a partial view, never a complete Score |
| `plugin-edit-propose/apply` | Atomic proposals, ACK after persistence and external authorization |
| `loss-report` | Actual supplied scope and preserved/lost information |

A 5.1 reader without Comp editing may play saved ordinary outputs, but must not claim to reproduce Visit/live dynamic selection. A 5.0-only reader requires an explicit 5.0 export. MIDI support does not imply audio support; retention does not imply interpretation; Schema conformance does not imply audio/DSP equivalence.

Normative responsibility for reference/range/musical consistency is separate from actual runtime testing status. This release is an approved written specification; no hardware, DAW or independent-implementation runtime test was performed.
