> **Current document edition: Draft 0.69 (unratified).** Older Draft headings and snapshot notes are retained as history. D01–D05 remain pending.

> **Historical editorial snapshot: Draft 0.59 (unratified).** Existing headings referring to earlier Drafts describe cumulative editorial proposals, not competing active document versions. The exact versioned Schemas remain unchanged; the single current release gate is [RELEASE_READINESS.md](RELEASE_READINESS.md). Publisher acceptance D01–D05 is still pending; runtime/independent tests are excluded, not passed.

# OSTF 4.3.0 — Complete Parameter Reference (Draft 0.53 editorial edition; Core Schema unchanged)

Full root and all `$defs`, generated from the actual `schema/ostf-4.3.0.schema.json` of this package. Contains the exact inherited **official** 4.2.0 schema plus 4.3 additions. All object-level constraints are reproduced in JSON blocks. Structural validity does not imply semantic validity or software interoperability.

**Source:** `docs/SOURCE_RECONCILIATION.md` documents the byte-perfect official 4.2 SHA256 match.

Schema definitions: **127**. Root fields: **24**.

## Index

- [Root](#root)
- [id](#def-id)
- [nonnegative](#def-nonnegative)
- [positive](#def-positive)
- [signed](#def-signed)
- [pitch](#def-pitch)
- [ref](#def-ref)
- [range](#def-range)
- [spelledPitchClass](#def-spelledpitchclass)
- [song](#def-song)
- [section](#def-section)
- [tempo](#def-tempo)
- [meter](#def-meter)
- [timeline](#def-timeline)
- [chord](#def-chord)
- [scale](#def-scale)
- [harmony](#def-harmony)
- [instrument](#def-instrument)
- [note](#def-note)
- [clip](#def-clip)
- [track](#def-track)
- [soundSlot](#def-soundslot)
- [lyricDocument](#def-lyricdocument)
- [lyricPhrase](#def-lyricphrase)
- [lyricUnit](#def-lyricunit)
- [lyricAlignment](#def-lyricalignment)
- [lyrics](#def-lyrics)
- [sha256](#def-sha256)
- [resource](#def-resource)
- [dependencies](#def-dependencies)
- [relativeAssignment](#def-relativeassignment)
- [generator](#def-generator)
- [generationInput](#def-generationinput)
- [generationProcess](#def-generationprocess)
- [color](#def-color)
- [roleDefinition](#def-roledefinition)
- [roleColorMap](#def-rolecolormap)
- [customRoleColorMap](#def-customrolecolormap)
- [objectColor](#def-objectcolor)
- [phraseTemplate](#def-phrasetemplate)
- [phraseNoteMapping](#def-phrasenotemapping)
- [phraseInstance](#def-phraseinstance)
- [clipCandidate](#def-clipcandidate)
- [clipChoiceGroup](#def-clipchoicegroup)
- [midiMapping](#def-midimapping)
- [soundSource](#def-soundsource)
- [localizedNames](#def-localizednames)
- [drumKit](#def-drumkit)
- [voicing](#def-voicing)
- [contributor](#def-contributor)
- [credit](#def-credit)
- [alternateTitle](#def-alternatetitle)
- [languageMap32](#def-languagemap32)
- [localizationTarget](#def-localizationtarget)
- [localizationEntry](#def-localizationentry)
- [genre](#def-genre)
- [legacy33](#def-legacy33)
- [opaqueDocumentId](#def-opaquedocumentid)
- [revisionRef](#def-revisionref)
- [software](#def-software)
- [documentInfo](#def-documentinfo)
- [key](#def-key)
- [keyChange](#def-keychange)
- [scaleDefinition](#def-scaledefinition)
- [scaleTarget](#def-scaletarget)
- [mood](#def-mood)
- [rightsStatement](#def-rightsstatement)
- [grooveIntent](#def-grooveintent)
- [generationIntent](#def-generationintent)
- [relativePhrases](#def-relativephrases)
- [generation](#def-generation)
- [presentation](#def-presentation)
- [phraseLibrary](#def-phraselibrary)
- [clipChoices](#def-clipchoices)
- [localization](#def-localization)
- [corePhraseSourceNote](#def-corephrasesourcenote)
- [provenanceSource](#def-provenancesource)
- [provenanceRecord](#def-provenancerecord)
- [provenance](#def-provenance)
- [midiChannel](#def-midichannel)
- [midiBus](#def-midibus)
- [midi](#def-midi)
- [mpeSettings](#def-mpesettings)
- [trackMidi](#def-trackmidi)
- [controlChangeEvent](#def-controlchangeevent)
- [channelModeEvent](#def-channelmodeevent)
- [programChangeEvent](#def-programchangeevent)
- [pitchBendEvent](#def-pitchbendevent)
- [channelPressureEvent](#def-channelpressureevent)
- [polyPressureEvent](#def-polypressureevent)
- [midiEvent](#def-midievent)
- [lyricVoice](#def-lyricvoice)
- [playablePitchRange](#def-playablepitchrange)
- [directionPitchCollection](#def-directionpitchcollection)
- [directionPitchSource](#def-directionpitchsource)
- [improvisationDirectionParameters](#def-improvisationdirectionparameters)
- [playingRoleDirectionParameters](#def-playingroledirectionparameters)
- [pitchRangeDirectionParameters](#def-pitchrangedirectionparameters)
- [vendorDirectionParameters](#def-vendordirectionparameters)
- [improvisationDirection](#def-improvisationdirection)
- [playingRoleDirection](#def-playingroledirection)
- [pitchRangeDirection](#def-pitchrangedirection)
- [vendorRangeDirection](#def-vendorrangedirection)
- [vendorPointDirection](#def-vendorpointdirection)
- [trackDirection](#def-trackdirection)
- [vocalPhonetics](#def-vocalphonetics)
- [vocalProfile](#def-vocalprofile)
- [vocalPerformance](#def-vocalperformance)
- [vocalPhonemeEvent](#def-vocalphonemeevent)
- [vocalCurvePointPitch](#def-vocalcurvepointpitch)
- [vocalCurvePointNormalized](#def-vocalcurvepointnormalized)
- [vocalPitchCurve](#def-vocalpitchcurve)
- [vocalExpressionCurve](#def-vocalexpressioncurve)
- [vocalTechnique](#def-vocaltechnique)
- [vocalBreathEvent](#def-vocalbreathevent)
- [positiveIntRange](#def-positiveintrange)
- [nonnegativeNumberRange](#def-nonnegativenumberrange)
- [phrasingDirectionParameters](#def-phrasingdirectionparameters)
- [phrasingDirection](#def-phrasingdirection)
- [lyricCandidateSet](#def-lyriccandidateset)
- [vocalFreedomDirectionParameters](#def-vocalfreedomdirectionparameters)
- [vocalFreedomDirection](#def-vocalfreedomdirection)
- [performanceRequirements](#def-performancerequirements)
- [performanceScope](#def-performancescope)
- [ensembleInteraction](#def-ensembleinteraction)
- [visitPart](#def-visitpart)
- [performanceVisit](#def-performancevisit)
- [performancePlan](#def-performanceplan)

<a id="root"></a>
## Root

Additive OSTF 4.3 development draft, based on the byte-verified public OSTF 4.2.0 schema. Optional Phrasing, Vocal Freedom, Ensemble Interactions, finite Performance Plans, and musical performance requirements.

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `format` | `const "OSTF"` | Yes |  |
| `version` | `const "4.3.0"` | Yes |  |
| `ppq` | `integer` | Yes |  |
| `song` | `#/$defs/song` | Yes |  |
| `timeline` | `#/$defs/timeline` | Yes |  |
| `harmony` | `#/$defs/harmony` | Yes |  |
| `tracks` | `array<#/$defs/track>` | Yes |  |
| `soundSlots` | `array<#/$defs/soundSlot>` | Yes |  |
| `lyrics` | `#/$defs/lyrics` | Yes |  |
| `resources` | `array<#/$defs/resource>` | Yes |  |
| `extensions` | `#/$defs/legacy33/$defs/extensions` | No/conditional | Optional third-party or verbatim legacy compatibility payloads. Standard Core always remains authoritative. New first-party common information... |
| `drumKits` | `array<#/$defs/drumKit>` | No/conditional | Optional multiple percussion-kit definitions; absent = no declared kits (3.0 compatible). |
| `contributors` | `array<#/$defs/contributor>` | No/conditional | Optional unordered identity records referenced by song.credits. No contributor limit is imposed by this format. |
| `document` | `#/$defs/documentInfo` | No/conditional |  |
| `relativePhrases` | `#/$defs/relativePhrases` | No/conditional |  |
| `generation` | `#/$defs/generation` | No/conditional |  |
| `presentation` | `#/$defs/presentation` | No/conditional |  |
| `phraseLibrary` | `#/$defs/phraseLibrary` | No/conditional |  |
| `clipChoices` | `#/$defs/clipChoices` | No/conditional |  |
| `localization` | `#/$defs/localization` | No/conditional |  |
| `provenance` | `#/$defs/provenance` | No/conditional |  |
| `midi` | `#/$defs/midi` | No/conditional | Optional document-level logical MIDI bus declarations. No physical device or DAW port assignment is encoded. |
| `ensembleInteractions` | `array<#/$defs/ensembleInteraction>` | No/conditional | Optional directed music relationships; these neither materialize notes nor initiate network messages. |
| `performancePlans` | `array<#/$defs/performancePlan>` | No/conditional | Optional finite source-timeline playthroughs; do not modify source timeline or concrete notes. |

### Exact JSON Schema object

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://yoh-nak.github.io/ostf/schema/ostf-4.3.0.schema.json",
  "title": "Open Song Timeline Format (OSTF) 4.3.0 — Draft 0.4",
  "description": "Additive OSTF 4.3 development draft, based on the byte-verified public OSTF 4.2.0 schema. Optional Phrasing, Vocal Freedom, Ensemble Interactions, finite Performance Plans, and musical performance requirements.",
  "$comment": "Unreleased Draft 0.4. The inherited 4.2.0 baseline has published SHA256 6933e2b52332e8b58b9c34b53ca7e101c3f0b689fd5f50f593809480b35e0fa2. See docs/SPECIFICATION.md for normative proposals, and SOURCE_RECONCILIATION.md for source evidence. Not an interoperability certification.",
  "type": "object",
  "properties": {
    "format": {
      "const": "OSTF"
    },
    "version": {
      "const": "4.3.0"
    },
    "ppq": {
      "type": "integer",
      "minimum": 1,
      "maximum": 960000
    },
    "song": {
      "$ref": "#/$defs/song"
    },
    "timeline": {
      "$ref": "#/$defs/timeline"
    },
    "harmony": {
      "$ref": "#/$defs/harmony"
    },
    "tracks": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/track"
      }
    },
    "soundSlots": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/soundSlot"
      }
    },
    "lyrics": {
      "$ref": "#/$defs/lyrics"
    },
    "resources": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/resource"
      }
    },
    "extensions": {
      "$ref": "#/$defs/legacy33/$defs/extensions",
      "description": "Optional third-party or verbatim legacy compatibility payloads. Standard Core always remains authoritative. New first-party common information must not be stored only here."
    },
    "drumKits": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/drumKit"
      },
      "description": "Optional multiple percussion-kit definitions; absent = no declared kits (3.0 compatible)."
    },
    "contributors": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/contributor"
      },
      "description": "Optional unordered identity records referenced by song.credits. No contributor limit is imposed by this format."
    },
    "document": {
      "$ref": "#/$defs/documentInfo"
    },
    "relativePhrases": {
      "$ref": "#/$defs/relativePhrases"
    },
    "generation": {
      "$ref": "#/$defs/generation"
    },
    "presentation": {
      "$ref": "#/$defs/presentation"
    },
    "phraseLibrary": {
      "$ref": "#/$defs/phraseLibrary"
    },
    "clipChoices": {
      "$ref": "#/$defs/clipChoices"
    },
    "localization": {
      "$ref": "#/$defs/localization"
    },
    "provenance": {
      "$ref": "#/$defs/provenance"
    },
    "midi": {
      "$ref": "#/$defs/midi",
      "description": "Optional document-level logical MIDI bus declarations. No physical device or DAW port assignment is encoded."
    },
    "ensembleInteractions": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/ensembleInteraction"
      },
      "description": "Optional directed music relationships; these neither materialize notes nor initiate network messages."
    },
    "performancePlans": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/performancePlan"
      },
      "description": "Optional finite source-timeline playthroughs; do not modify source timeline or concrete notes."
    }
  },
  "required": [
    "format",
    "version",
    "ppq",
    "song",
    "timeline",
    "harmony",
    "tracks",
    "soundSlots",
    "lyrics",
    "resources"
  ],
  "additionalProperties": false,
  "$defs": {
    "id": {
      "type": "string",
      "pattern": "^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$",
      "not": {
        "pattern": "[\\r\\n\\u2028\\u2029]"
      }
    },
    "nonnegative": {
      "type": "integer",
      "minimum": 0,
      "maximum": 9007199254740991
    },
    "positive": {
      "type": "integer",
      "minimum": 1,
      "maximum": 9007199254740991
    },
    "signed": {
      "type": "integer",
      "minimum": -9007199254740991,
      "maximum": 9007199254740991
    },
    "pitch": {
      "type": "integer",
      "minimum": 0,
      "maximum": 127
    },
    "ref": {
      "type": "object",
      "properties": {
        "type": {
          "enum": [
            "section",
            "track",
            "clip",
            "note",
            "chord",
            "scale",
            "soundSlot",
            "drumKit",
            "lyricDocument",
            "lyricPhrase",
            "lyricUnit",
            "lyricAlignment",
            "resource",
            "genre",
            "contributor",
            "credit",
            "alternateTitle",
            "mood",
            "keyChange",
            "phraseTemplate",
            "phraseInstance",
            "clipChoiceGroup",
            "clipCandidate",
            "roleDefinition",
            "generationProcess",
            "provenanceRecord",
            "midiBus",
            "midiEvent",
            "lyricVoice",
            "trackDirection",
            "ensembleInteraction",
            "performancePlan",
            "performanceVisit"
          ]
        },
        "id": {
          "$ref": "#/$defs/id"
        }
      },
      "required": [
        "type",
        "id"
      ],
      "additionalProperties": false
    },
    "range": {
      "type": "object",
      "properties": {
        "start": {
          "$ref": "#/$defs/nonnegative"
        },
        "duration": {
          "$ref": "#/$defs/positive"
        }
      },
      "required": [
        "start",
        "duration"
      ],
      "additionalProperties": false
    },
    "spelledPitchClass": {
      "type": "object",
      "properties": {
        "step": {
          "enum": [
            "A",
            "B",
            "C",
            "D",
            "E",
            "F",
            "G"
          ]
        },
        "alter": {
          "type": "integer",
          "minimum": -2,
          "maximum": 2
        }
      },
      "required": [
        "step",
        "alter"
      ],
      "additionalProperties": false
    },
    "song": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string"
        },
        "primaryMelodyTrackId": {
          "$ref": "#/$defs/id"
        },
        "localizedTitles": {
          "$ref": "#/$defs/localizedNames",
          "description": "Optional localized song-title alternatives. song.title is the stable fallback."
        },
        "subtitle": {
          "type": "string",
          "description": "Optional original-language subtitle."
        },
        "description": {
          "type": "string",
          "description": "Optional original-language description, including Unicode and line breaks."
        },
        "alternateTitles": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/alternateTitle"
          },
          "description": "Additional stable-ID source-language titles."
        },
        "credits": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/credit"
          },
          "description": "Ordered credit assignments to contributors. Multiple roles and duplicate contributors permitted."
        },
        "genres": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/genre"
          },
          "description": "Optional open-ended ordered genre tags; zero or more allowed. Order is authored display preference, first item is primary if a primary label is desired, not a generator weight. Absent means unspecified."
        },
        "key": {
          "$ref": "#/$defs/key"
        },
        "scale": {
          "$ref": "#/$defs/scaleDefinition"
        },
        "languages": {
          "type": "array",
          "items": {
            "type": "string",
            "minLength": 1,
            "description": "Authored language tag, preferably BCP 47. Unknown spelling is retained; case-insensitive duplicate tags forbidden."
          },
          "uniqueItems": true
        },
        "primaryLyricDocumentId": {
          "$ref": "#/$defs/id"
        },
        "moods": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/mood"
          }
        },
        "rights": {
          "$ref": "#/$defs/rightsStatement"
        },
        "melodyTrackIds": {
          "type": "array",
          "uniqueItems": true,
          "items": {
            "$ref": "#/$defs/id"
          },
          "description": "Optional ordered set of tracks explicitly authored as melody-bearing tracks. If present with primaryMelodyTrackId, the primary track must be a member."
        }
      },
      "required": [
        "title"
      ],
      "additionalProperties": false
    },
    "section": {
      "type": "object",
      "properties": {
        "id": {
          "$ref": "#/$defs/id"
        },
        "name": {
          "type": "string",
          "minLength": 1
        },
        "start": {
          "$ref": "#/$defs/nonnegative"
        },
        "duration": {
          "$ref": "#/$defs/positive"
        },
        "role": {
          "type": "string"
        },
        "localizedNames": {
          "$ref": "#/$defs/localizedNames",
          "description": "Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity."
        }
      },
      "required": [
        "id",
        "name",
        "start",
        "duration"
      ],
      "additionalProperties": false
    },
    "tempo": {
      "type": "object",
      "properties": {
        "at": {
          "$ref": "#/$defs/nonnegative"
        },
        "bpm": {
          "type": "number",
          "exclusiveMinimum": 0,
          "maximum": 1000
        }
      },
      "required": [
        "at",
        "bpm"
      ],
      "additionalProperties": false
    },
    "meter": {
      "type": "object",
      "properties": {
        "at": {
          "$ref": "#/$defs/nonnegative"
        },
        "numerator": {
          "type": "integer",
          "minimum": 1,
          "maximum": 64
        },
        "denominator": {
          "enum": [
            1,
            2,
            4,
            8,
            16,
            32,
            64
          ],
          "type": "integer"
        },
        "beatGroups": {
          "type": "array",
          "items": {
            "type": "integer",
            "minimum": 1,
            "maximum": 64
          },
          "minItems": 1,
          "maxItems": 64,
          "description": "Optional additive grouping in denominator units. Values must sum to numerator. Descriptive only; does not change note timestamps."
        }
      },
      "required": [
        "at",
        "numerator",
        "denominator"
      ],
      "additionalProperties": false
    },
    "timeline": {
      "type": "object",
      "properties": {
        "sections": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/section"
          }
        },
        "tempoChanges": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/tempo"
          },
          "minItems": 1
        },
        "meterChanges": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/meter"
          },
          "minItems": 1
        },
        "keyChanges": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/keyChange"
          }
        },
        "duration": {
          "$ref": "#/$defs/nonnegative"
        },
        "barOrigin": {
          "$ref": "#/$defs/nonnegative"
        }
      },
      "required": [
        "sections",
        "tempoChanges",
        "meterChanges"
      ],
      "additionalProperties": false
    },
    "chord": {
      "type": "object",
      "properties": {
        "id": {
          "$ref": "#/$defs/id"
        },
        "start": {
          "$ref": "#/$defs/nonnegative"
        },
        "duration": {
          "$ref": "#/$defs/positive"
        },
        "label": {
          "type": "string",
          "minLength": 1
        },
        "root": {
          "$ref": "#/$defs/spelledPitchClass"
        },
        "intervals": {
          "type": "array",
          "items": {
            "type": "integer",
            "minimum": 0,
            "maximum": 35
          },
          "minItems": 1,
          "maxItems": 36,
          "uniqueItems": true,
          "contains": {
            "const": 0
          }
        },
        "bass": {
          "$ref": "#/$defs/spelledPitchClass"
        },
        "voicing": {
          "$ref": "#/$defs/voicing",
          "description": "Optional pitch snapshot (not an arrangement note sequence). No automatic playback."
        }
      },
      "required": [
        "id",
        "start",
        "duration",
        "label"
      ],
      "additionalProperties": false,
      "dependentRequired": {
        "root": [
          "intervals"
        ],
        "intervals": [
          "root"
        ]
      }
    },
    "scale": {
      "type": "object",
      "properties": {
        "id": {
          "$ref": "#/$defs/id"
        },
        "start": {
          "$ref": "#/$defs/nonnegative"
        },
        "duration": {
          "$ref": "#/$defs/positive"
        },
        "label": {
          "type": "string"
        },
        "tonic": {
          "$ref": "#/$defs/spelledPitchClass"
        },
        "intervals": {
          "type": "array",
          "items": {
            "type": "integer",
            "minimum": 0,
            "maximum": 11
          },
          "minItems": 1,
          "maxItems": 12,
          "uniqueItems": true,
          "contains": {
            "const": 0
          }
        },
        "targets": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/scaleTarget"
          },
          "minItems": 1,
          "uniqueItems": true,
          "description": "Optional explicit scope. Absence means general timed context, not a global key. Overlapping contexts are not resolved by array order."
        }
      },
      "required": [
        "id",
        "start",
        "duration",
        "tonic",
        "intervals"
      ],
      "additionalProperties": false
    },
    "harmony": {
      "type": "object",
      "properties": {
        "chords": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/chord"
          }
        },
        "scales": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/scale"
          }
        }
      },
      "required": [
        "chords",
        "scales"
      ],
      "additionalProperties": false
    },
    "instrument": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "family": {
          "type": "string"
        },
        "localizedNames": {
          "$ref": "#/$defs/localizedNames",
          "description": "Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity."
        },
        "playablePitchRange": {
          "$ref": "#/$defs/playablePitchRange"
        }
      },
      "required": [
        "name"
      ],
      "additionalProperties": false
    },
    "note": {
      "type": "object",
      "properties": {
        "id": {
          "$ref": "#/$defs/id"
        },
        "start": {
          "$ref": "#/$defs/signed"
        },
        "duration": {
          "$ref": "#/$defs/positive",
          "description": "Positive note gate in ticks, not the guaranteed audible duration of a one-shot percussion sample."
        },
        "pitch": {
          "$ref": "#/$defs/pitch"
        },
        "soundSlotId": {
          "$ref": "#/$defs/id",
          "description": "Document-local Sound Slot ID. Distinct events and IDs stay distinct even if several slots share a MIDI key; a renderer decides the acoustic timbre."
        },
        "velocity": {
          "type": "integer",
          "minimum": 1,
          "maximum": 127,
          "description": "Optional authored note-on velocity for performed Core notes, 1–127; omit to mean unspecified. It is not a note-off velocity, controller stream, chord tone, or a sound-rendering guarantee. Never insert an inferred default when saving."
        },
        "enabled": {
          "type": "boolean",
          "default": true,
          "description": "Optional note-local enable state. Omitted means enabled. False preserves the note but suppresses scheduling/playback; it is distinct from probability=0."
        },
        "releaseVelocity": {
          "type": "integer",
          "minimum": 0,
          "maximum": 127,
          "description": "Optional MIDI Note Off/release velocity, 0-127. Omit when unspecified; readers must not invent and write back a default."
        },
        "probability": {
          "type": "number",
          "minimum": 0,
          "maximum": 1,
          "default": 1,
          "description": "Optional note-playback probability from 0.0 to 1.0. Omitted means 1.0. Random sequence identity is not standardized; materialize notes for deterministic interchange."
        },
        "velocityDeviation": {
          "type": "integer",
          "minimum": -126,
          "maximum": 126,
          "default": 0,
          "description": "Optional note-local velocity variation endpoint relative to velocity. Requires velocity. Semantic rule: velocity + velocityDeviation must remain within 1..127. Omitted means 0."
        },
        "pitchRole": {
          "enum": [
            "musical",
            "fixedTrigger"
          ],
          "default": "musical",
          "description": "Meaning of a pitch note. musical participates in pitch/harmony/transpose operations; fixedTrigger is an exact MIDI key trigger (for example a keyswitch) and is never transposed or used as musical-pitch evidence. Allowed only on pitch notes."
        },
        "channel": {
          "$ref": "#/$defs/midiChannel",
          "description": "Optional concrete MIDI channel for this performed note. In singleChannel mode it may be omitted and inherited from the track; in multiChannel/MPE mode semantic rules require explicit channel where channel identity matters."
        }
      },
      "required": [
        "id",
        "start",
        "duration"
      ],
      "additionalProperties": false,
      "oneOf": [
        {
          "required": [
            "pitch"
          ],
          "not": {
            "required": [
              "soundSlotId"
            ]
          }
        },
        {
          "required": [
            "soundSlotId"
          ],
          "not": {
            "required": [
              "pitch"
            ]
          }
        }
      ],
      "description": "Concrete Core DAW-note event. The event target is pitch or soundSlotId. Optional 3.5 note-local properties preserve mute, release velocity, probability and velocity variation. pitchRole=fixedTrigger marks a literal MIDI key trigger that must not be musically transposed or analyzed.",
      "dependentRequired": {
        "velocityDeviation": [
          "velocity"
        ]
      },
      "allOf": [
        {
          "if": {
            "required": [
              "soundSlotId"
            ]
          },
          "then": {
            "not": {
              "required": [
                "pitchRole"
              ]
            }
          }
        }
      ]
    },
    "clip": {
      "type": "object",
      "properties": {
        "id": {
          "$ref": "#/$defs/id"
        },
        "name": {
          "type": "string"
        },
        "start": {
          "$ref": "#/$defs/nonnegative"
        },
        "duration": {
          "$ref": "#/$defs/positive"
        },
        "enabled": {
          "type": "boolean",
          "default": true
        },
        "notes": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/note"
          }
        },
        "localizedNames": {
          "$ref": "#/$defs/localizedNames",
          "description": "Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity."
        },
        "midiEvents": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/midiEvent"
          },
          "description": "Optional clip-local MIDI performance/control events. start is local to the clip and may be negative if absolute time remains nonnegative. Notes remain authoritative in notes[]."
        },
        "vocalPerformances": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/vocalPerformance"
          },
          "minItems": 1,
          "description": "Optional voice-specific phoneme and singing-performance data; references lyrics.voices. Notes/MIDI remain authoritative for MIDI playback."
        }
      },
      "required": [
        "id",
        "start",
        "duration",
        "notes"
      ],
      "additionalProperties": false
    },
    "track": {
      "type": "object",
      "properties": {
        "id": {
          "$ref": "#/$defs/id"
        },
        "name": {
          "type": "string"
        },
        "role": {
          "type": "string"
        },
        "instrument": {
          "$ref": "#/$defs/instrument"
        },
        "enabled": {
          "type": "boolean",
          "default": true
        },
        "clips": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/clip"
          }
        },
        "trackType": {
          "enum": [
            "melodic",
            "drum",
            "mixed"
          ],
          "description": "Semantic event-target category; optional; missing/empty-note tracks may be unknown. It is not a DAW track class."
        },
        "preferredView": {
          "enum": [
            "auto",
            "pianoRoll",
            "drumGrid"
          ],
          "default": "auto",
          "description": "Non-binding presentation preference. Does not change note meaning."
        },
        "soundSource": {
          "$ref": "#/$defs/soundSource",
          "description": "Optional sound-source selection hint, not a plug-in state, preset blob, or sound guarantee."
        },
        "localizedNames": {
          "$ref": "#/$defs/localizedNames",
          "description": "Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity."
        },
        "drumKitId": {
          "$ref": "#/$defs/id",
          "description": "Optional reference to a declared drumKit; only for a drum/mixed or empty inferred track. All stored slot events in the track must belong to the referenced kit."
        },
        "midi": {
          "$ref": "#/$defs/trackMidi"
        },
        "directions": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/trackDirection"
          },
          "description": "Optional typed semantic instructions for performance, interpretation, or generation. Uses the global OSTF timebase; it is not a second timeline."
        },
        "performanceRequirements": {
          "$ref": "#/$defs/performanceRequirements",
          "description": "Portable requirements for realizing this track, not a robot/device capability report."
        }
      },
      "required": [
        "id",
        "name",
        "clips"
      ],
      "additionalProperties": false,
      "allOf": [
        {
          "if": {
            "properties": {
              "trackType": {
                "const": "melodic"
              }
            },
            "required": [
              "trackType"
            ]
          },
          "then": {
            "not": {
              "required": [
                "drumKitId"
              ]
            }
          }
        }
      ]
    },
    "soundSlot": {
      "type": "object",
      "properties": {
        "id": {
          "$ref": "#/$defs/id"
        },
        "name": {
          "type": "string"
        },
        "role": {
          "type": "string",
          "description": "Optional free-text musical role; not a standardized GM instrument code or an acoustic sample identifier."
        },
        "midiNote": {
          "$ref": "#/$defs/pitch",
          "description": "Legacy 3.0 MIDI note hint only; not a GM1 declaration or preview timbre identity."
        },
        "midiMapping": {
          "$ref": "#/$defs/midiMapping",
          "description": "Explicit external MIDI1 output mapping; standard=gm1 is separate from custom even for an equal note number. Not a unique slot or audio identity."
        },
        "localizedNames": {
          "$ref": "#/$defs/localizedNames",
          "description": "Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity."
        }
      },
      "required": [
        "id",
        "name"
      ],
      "additionalProperties": false,
      "description": "Document-local stable logical percussion target. Equal roles, names or MIDI note mappings never merge distinct slot IDs. No sample/audio identity is encoded."
    },
    "lyricDocument": {
      "type": "object",
      "properties": {
        "id": {
          "$ref": "#/$defs/id"
        },
        "title": {
          "type": "string"
        },
        "language": {
          "type": "string"
        }
      },
      "required": [
        "id"
      ],
      "additionalProperties": false
    },
    "lyricPhrase": {
      "type": "object",
      "properties": {
        "id": {
          "$ref": "#/$defs/id"
        },
        "documentId": {
          "$ref": "#/$defs/id"
        },
        "text": {
          "type": "string"
        },
        "pronunciation": {
          "type": "string"
        },
        "start": {
          "$ref": "#/$defs/nonnegative"
        },
        "duration": {
          "$ref": "#/$defs/positive"
        }
      },
      "required": [
        "id",
        "documentId",
        "text"
      ],
      "additionalProperties": false,
      "dependentRequired": {
        "start": [
          "duration"
        ],
        "duration": [
          "start"
        ]
      }
    },
    "lyricUnit": {
      "type": "object",
      "properties": {
        "id": {
          "$ref": "#/$defs/id"
        },
        "phraseId": {
          "$ref": "#/$defs/id"
        },
        "text": {
          "type": "string"
        },
        "pronunciation": {
          "type": "string"
        },
        "start": {
          "$ref": "#/$defs/nonnegative"
        },
        "duration": {
          "$ref": "#/$defs/positive"
        },
        "phonetics": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/vocalPhonetics"
          },
          "minItems": 1,
          "description": "Optional alternate phoneme token sequences. Do not alter text/pronunciation. Multiple alphabets are permitted."
        }
      },
      "required": [
        "id",
        "phraseId",
        "text"
      ],
      "additionalProperties": false,
      "dependentRequired": {
        "start": [
          "duration"
        ],
        "duration": [
          "start"
        ]
      }
    },
    "lyricAlignment": {
      "type": "object",
      "properties": {
        "id": {
          "$ref": "#/$defs/id"
        },
        "unitIds": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/id"
          },
          "uniqueItems": true,
          "minItems": 1
        },
        "noteIds": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/id"
          },
          "uniqueItems": true,
          "minItems": 1
        },
        "voiceId": {
          "$ref": "#/$defs/id",
          "description": "Optional lyricVoice association. When present, aligned units must belong to that voice document and aligned notes must belong to that voice track."
        }
      },
      "required": [
        "id",
        "unitIds",
        "noteIds"
      ],
      "additionalProperties": false
    },
    "lyrics": {
      "type": "object",
      "properties": {
        "documents": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/lyricDocument"
          }
        },
        "phrases": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/lyricPhrase"
          }
        },
        "units": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/lyricUnit"
          }
        },
        "alignments": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/lyricAlignment"
          }
        },
        "voices": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/lyricVoice"
          },
          "description": "Optional explicit vocal-part relationships for multi-voice, harmony and chorus lyrics."
        }
      },
      "required": [
        "documents",
        "phrases",
        "units",
        "alignments"
      ],
      "additionalProperties": false
    },
    "sha256": {
      "type": "string",
      "pattern": "^[0-9a-f]{64}$",
      "not": {
        "pattern": "[\\r\\n\\u2028\\u2029]"
      }
    },
    "resource": {
      "type": "object",
      "properties": {
        "id": {
          "$ref": "#/$defs/id"
        },
        "kind": {
          "enum": [
            "audio",
            "midi",
            "text",
            "other"
          ]
        },
        "uri": {
          "type": "string",
          "minLength": 1
        },
        "name": {
          "type": "string"
        },
        "sha256": {
          "$ref": "#/$defs/sha256"
        }
      },
      "required": [
        "id",
        "kind",
        "uri"
      ],
      "additionalProperties": false
    },
    "dependencies": {
      "oneOf": [
        {
          "type": "object",
          "properties": {
            "scope": {
              "enum": [
                "document",
                "none"
              ]
            }
          },
          "required": [
            "scope"
          ],
          "additionalProperties": false
        },
        {
          "type": "object",
          "properties": {
            "scope": {
              "const": "objects"
            },
            "refs": {
              "type": "array",
              "items": {
                "$ref": "#/$defs/ref"
              },
              "minItems": 1,
              "uniqueItems": true
            }
          },
          "required": [
            "scope",
            "refs"
          ],
          "additionalProperties": false
        }
      ]
    },
    "relativeAssignment": {
      "type": "object",
      "properties": {
        "noteId": {
          "$ref": "#/$defs/id"
        },
        "basis": {
          "enum": [
            "chordTone",
            "scaleDegree"
          ]
        },
        "contextId": {
          "$ref": "#/$defs/id"
        },
        "anchorPitch": {
          "$ref": "#/$defs/pitch"
        },
        "index": {
          "type": "integer",
          "minimum": 1,
          "maximum": 36
        },
        "chromaticOffset": {
          "type": "integer",
          "minimum": -24,
          "maximum": 24
        }
      },
      "required": [
        "noteId",
        "basis",
        "contextId",
        "anchorPitch",
        "index",
        "chromaticOffset"
      ],
      "additionalProperties": false,
      "allOf": [
        {
          "if": {
            "properties": {
              "basis": {
                "const": "scaleDegree"
              }
            },
            "required": [
              "basis"
            ]
          },
          "then": {
            "properties": {
              "index": {
                "maximum": 12
              }
            }
          }
        }
      ]
    },
    "generator": {
      "type": "object",
      "properties": {
        "id": {
          "type": "string",
          "minLength": 1
        },
        "version": {
          "type": "string",
          "minLength": 1
        }
      },
      "required": [
        "id",
        "version"
      ],
      "additionalProperties": false
    },
    "generationInput": {
      "type": "object",
      "properties": {
        "role": {
          "type": "string",
          "minLength": 1
        },
        "ref": {
          "$ref": "#/$defs/ref"
        },
        "readRange": {
          "$ref": "#/$defs/range"
        }
      },
      "required": [
        "role",
        "ref"
      ],
      "additionalProperties": false
    },
    "generationProcess": {
      "type": "object",
      "properties": {
        "id": {
          "$ref": "#/$defs/id"
        },
        "generator": {
          "$ref": "#/$defs/generator"
        },
        "inputs": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/generationInput"
          }
        },
        "outputs": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/ref"
          },
          "minItems": 1
        },
        "targetRange": {
          "$ref": "#/$defs/range"
        },
        "protectedNoteIds": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/id"
          },
          "uniqueItems": true
        },
        "intent": {
          "$ref": "#/$defs/generationIntent"
        }
      },
      "required": [
        "id",
        "generator",
        "inputs",
        "outputs",
        "protectedNoteIds"
      ],
      "additionalProperties": false
    },
    "color": {
      "type": "string",
      "pattern": "^#[0-9A-Fa-f]{6}$",
      "not": {
        "pattern": "[\\r\\n\\u2028\\u2029]"
      }
    },
    "roleDefinition": {
      "type": "object",
      "properties": {
        "id": {
          "$ref": "#/$defs/id"
        },
        "name": {
          "type": "string",
          "minLength": 1
        },
        "baseRole": {
          "type": "string"
        }
      },
      "required": [
        "id",
        "name"
      ],
      "additionalProperties": false
    },
    "roleColorMap": {
      "type": "object",
      "additionalProperties": {
        "$ref": "#/$defs/color"
      }
    },
    "customRoleColorMap": {
      "type": "object",
      "propertyNames": {
        "$ref": "#/$defs/id"
      },
      "additionalProperties": {
        "$ref": "#/$defs/color"
      }
    },
    "objectColor": {
      "type": "object",
      "properties": {
        "target": {
          "$ref": "#/$defs/ref"
        },
        "color": {
          "$ref": "#/$defs/color"
        }
      },
      "required": [
        "target",
        "color"
      ],
      "additionalProperties": false
    },
    "phraseTemplate": {
      "type": "object",
      "properties": {
        "id": {
          "$ref": "#/$defs/id"
        },
        "duration": {
          "$ref": "#/$defs/positive"
        },
        "notes": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/corePhraseSourceNote"
          }
        },
        "name": {
          "type": "string"
        }
      },
      "required": [
        "id",
        "duration",
        "notes"
      ],
      "additionalProperties": false
    },
    "phraseNoteMapping": {
      "type": "object",
      "properties": {
        "templateNoteId": {
          "$ref": "#/$defs/id"
        },
        "repeatIndex": {
          "$ref": "#/$defs/nonnegative"
        },
        "noteId": {
          "$ref": "#/$defs/id"
        }
      },
      "required": [
        "templateNoteId",
        "repeatIndex",
        "noteId"
      ],
      "additionalProperties": false
    },
    "phraseInstance": {
      "type": "object",
      "properties": {
        "id": {
          "$ref": "#/$defs/id"
        },
        "templateId": {
          "$ref": "#/$defs/id"
        },
        "clipId": {
          "$ref": "#/$defs/id"
        },
        "repeatCount": {
          "$ref": "#/$defs/positive"
        },
        "transpose": {
          "type": "integer",
          "minimum": -127,
          "maximum": 127
        },
        "noteMap": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/phraseNoteMapping"
          }
        },
        "velocityMode": {
          "enum": [
            "independent",
            "linked"
          ],
          "default": "independent",
          "description": "independent preserves concrete velocities on refresh; linked requires exact presence/value equality with the template. This field does not trigger refresh on load."
        },
        "noteStateMode": {
          "enum": [
            "independent",
            "linked"
          ],
          "default": "independent",
          "description": "Controls enabled/releaseVelocity/probability/velocityDeviation after materialization. independent preserves concrete note-state values on refresh; linked requires exact presence/value equality with the template. pitchRole is structural and must always remain semantically equal between a source pitch note and its mapped concrete note."
        }
      },
      "required": [
        "id",
        "templateId",
        "clipId",
        "repeatCount",
        "transpose",
        "noteMap"
      ],
      "additionalProperties": false
    },
    "clipCandidate": {
      "type": "object",
      "properties": {
        "id": {
          "$ref": "#/$defs/id"
        },
        "clipIds": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/id"
          },
          "uniqueItems": true
        },
        "name": {
          "type": "string"
        }
      },
      "required": [
        "id",
        "clipIds"
      ],
      "additionalProperties": false
    },
    "clipChoiceGroup": {
      "type": "object",
      "properties": {
        "id": {
          "$ref": "#/$defs/id"
        },
        "candidates": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/clipCandidate"
          },
          "minItems": 1
        },
        "selectedCandidateId": {
          "anyOf": [
            {
              "$ref": "#/$defs/id"
            },
            {
              "type": "null"
            }
          ]
        },
        "name": {
          "type": "string"
        }
      },
      "required": [
        "id",
        "candidates",
        "selectedCandidateId"
      ],
      "additionalProperties": false
    },
    "midiMapping": {
      "type": "object",
      "properties": {
        "standard": {
          "enum": [
            "gm1",
            "custom"
          ],
          "description": "gm1=GM Level 1 percussion key 35..81; custom=explicit arbitrary MIDI1 note number."
        },
        "note": {
          "$ref": "#/$defs/pitch",
          "description": "MIDI1 note number in 0..127; for gm1 restrict to 35..81."
        }
      },
      "required": [
        "standard",
        "note"
      ],
      "additionalProperties": false,
      "allOf": [
        {
          "if": {
            "properties": {
              "standard": {
                "const": "gm1"
              }
            },
            "required": [
              "standard"
            ]
          },
          "then": {
            "properties": {
              "note": {
                "type": "integer",
                "minimum": 35,
                "maximum": 81
              }
            }
          }
        }
      ]
    },
    "soundSource": {
      "type": "object",
      "description": "Optional informational rendering class or opaque destination hint. In OSTF 4.0, track.midi.busId is the Core logical MIDI routing reference; soundSource does not bind a physical device, plugin state or preset.",
      "properties": {
        "kind": {
          "enum": [
            "unassigned",
            "gm1",
            "externalMidi",
            "plugin",
            "hostManaged"
          ]
        },
        "identifier": {
          "type": "string",
          "minLength": 1,
          "description": "Opaque informational target identifier (for example a URI or plug-in identifier), not a physical MIDI-port binding or loading command."
        }
      },
      "required": [
        "kind"
      ],
      "additionalProperties": false,
      "allOf": [
        {
          "if": {
            "properties": {
              "kind": {
                "enum": [
                  "gm1",
                  "unassigned"
                ]
              }
            },
            "required": [
              "kind"
            ]
          },
          "then": {
            "not": {
              "required": [
                "identifier"
              ]
            }
          }
        }
      ]
    },
    "localizedNames": {
      "type": "object",
      "minProperties": 1,
      "propertyNames": {
        "type": "string",
        "pattern": "^(?:[A-Za-z]{2,3}|[A-Za-z]{5,8})(?:-[A-Za-z0-9]{2,8})*$"
      },
      "additionalProperties": {
        "type": "string",
        "minLength": 1
      },
      "description": "Optional translations indexed by a conservative BCP 47 language-tag subset. The original name/title remains authoritative and is never rewritten by locale changes. Case-insensitive duplicate tags are forbidden semantically."
    },
    "drumKit": {
      "type": "object",
      "description": "Optional named ordered membership of global Sound Slot IDs. Does not define plugin preset, sample loading, choke or a kit-local MIDI remapping.",
      "properties": {
        "id": {
          "$ref": "#/$defs/id"
        },
        "name": {
          "type": "string"
        },
        "localizedNames": {
          "$ref": "#/$defs/localizedNames"
        },
        "soundSlotIds": {
          "type": "array",
          "uniqueItems": true,
          "items": {
            "$ref": "#/$defs/id"
          },
          "description": "Ordered, unique references to global soundSlots; may be empty."
        }
      },
      "required": [
        "id",
        "name",
        "soundSlotIds"
      ],
      "additionalProperties": false
    },
    "voicing": {
      "type": "object",
      "additionalProperties": false,
      "description": "Optional informational chord voicing snapshot, not a played Core note collection. Repeated pitches and original array order have meaning for lossless preservation. Per-entry velocity is an optional voicing-preview hint.",
      "properties": {
        "pitches": {
          "type": "array",
          "minItems": 1,
          "items": {
            "$ref": "#/$defs/pitch"
          },
          "description": "Ordered multiset of concrete absolute pitches, 0-127. Duplicates allowed."
        },
        "velocities": {
          "type": "array",
          "minItems": 1,
          "items": {
            "anyOf": [
              {
                "type": "integer",
                "minimum": 1,
                "maximum": 127
              },
              {
                "type": "null"
              }
            ]
          },
          "description": "Optional positional velocities aligned one-to-one to pitches. Null means unspecified at this index, not 0. Exact equal-length rule is semantic."
        }
      },
      "required": [
        "pitches"
      ]
    },
    "contributor": {
      "type": "object",
      "additionalProperties": false,
      "description": "One song-local identity; same contributor can receive multiple credit roles. Unicode source name is authoritative.",
      "properties": {
        "id": {
          "$ref": "#/$defs/id"
        },
        "name": {
          "type": "string",
          "minLength": 1
        },
        "kind": {
          "enum": [
            "person",
            "organization",
            "other"
          ]
        },
        "localizedNames": {
          "$ref": "#/$defs/localizedNames"
        }
      },
      "required": [
        "id",
        "name"
      ]
    },
    "credit": {
      "type": "object",
      "additionalProperties": false,
      "description": "Ordered credit assignment referencing one contributor; role is an open semantic token, not a translated label.",
      "properties": {
        "id": {
          "$ref": "#/$defs/id"
        },
        "contributorId": {
          "$ref": "#/$defs/id"
        },
        "role": {
          "type": "string",
          "pattern": "^[a-z][a-z0-9.-]*$"
        },
        "label": {
          "type": "string"
        }
      },
      "required": [
        "id",
        "contributorId",
        "role"
      ]
    },
    "alternateTitle": {
      "type": "object",
      "additionalProperties": false,
      "description": "Stable-ID song title alternative; array position and title text do not identify it.",
      "properties": {
        "id": {
          "$ref": "#/$defs/id"
        },
        "title": {
          "type": "string",
          "minLength": 1
        }
      },
      "required": [
        "id",
        "title"
      ]
    },
    "languageMap32": {
      "type": "object",
      "minProperties": 1,
      "propertyNames": {
        "type": "string",
        "pattern": "^[A-Za-z]{1,8}(?:-[A-Za-z0-9]{1,8})*$"
      },
      "additionalProperties": {
        "type": "string"
      },
      "description": "Open BCP 47 language-tag dictionary. Schema checks loose subtag structure; full BCP 47 well-formedness and case-insensitive uniqueness are semantic requirements. String may be empty if intentionally blank."
    },
    "localizationTarget": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "kind": {
          "enum": [
            "song",
            "alternateTitle",
            "contributor",
            "credit",
            "section",
            "track",
            "clip",
            "soundSlot",
            "drumKit",
            "lyricDocument",
            "resource",
            "phraseTemplate",
            "clipCandidate",
            "clipChoiceGroup",
            "roleDefinition",
            "genre",
            "mood",
            "keyChange",
            "scale",
            "midiBus",
            "lyricVoice"
          ]
        },
        "id": {
          "$ref": "#/$defs/id"
        }
      },
      "required": [
        "kind"
      ],
      "allOf": [
        {
          "if": {
            "properties": {
              "kind": {
                "const": "song"
              }
            },
            "required": [
              "kind"
            ]
          },
          "then": {
            "not": {
              "required": [
                "id"
              ]
            }
          },
          "else": {
            "required": [
              "id"
            ]
          }
        }
      ],
      "description": "Core target; song is ID-less, all others use global Core ID. No namespace/profile selector."
    },
    "localizationEntry": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "target": {
          "$ref": "#/$defs/localizationTarget"
        },
        "field": {
          "type": "string",
          "minLength": 1,
          "description": "Exact allowed source text field for this target kind (see normative matrix). No arbitrary path or musical value fields."
        },
        "values": {
          "$ref": "#/$defs/languageMap32"
        }
      },
      "required": [
        "target",
        "field",
        "values"
      ],
      "description": "Independent translations for one stable source field. Original source text remains authoritative as fallback."
    },
    "genre": {
      "type": "object",
      "description": "One song-local open genre tag. The label is authored Unicode text and not a predefined controlled taxonomy; ID is stable for metadata merges and localization.",
      "properties": {
        "id": {
          "$ref": "#/$defs/id",
          "description": "Stable song-local ID unique among all Core objects."
        },
        "name": {
          "type": "string",
          "minLength": 1,
          "description": "Original Unicode genre label, never normalized or rewritten during import."
        },
        "externalUri": {
          "type": "string",
          "minLength": 1,
          "format": "uri",
          "description": "Optional external taxonomy URI hint; never authoritative for a local genre label, and never auto-dereferenced."
        }
      },
      "required": [
        "id",
        "name"
      ],
      "additionalProperties": false
    },
    "legacy33": {
      "$defs": {
        "id": {
          "type": "string",
          "pattern": "^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$",
          "not": {
            "pattern": "[\\r\\n\\u2028\\u2029]"
          }
        },
        "nonnegative": {
          "type": "integer",
          "minimum": 0,
          "maximum": 9007199254740991
        },
        "positive": {
          "type": "integer",
          "minimum": 1,
          "maximum": 9007199254740991
        },
        "signed": {
          "type": "integer",
          "minimum": -9007199254740991,
          "maximum": 9007199254740991
        },
        "pitch": {
          "type": "integer",
          "minimum": 0,
          "maximum": 127
        },
        "ref": {
          "type": "object",
          "properties": {
            "type": {
              "enum": [
                "section",
                "track",
                "clip",
                "note",
                "chord",
                "scale",
                "soundSlot",
                "drumKit",
                "lyricDocument",
                "lyricPhrase",
                "lyricUnit",
                "lyricAlignment",
                "resource",
                "genre"
              ]
            },
            "id": {
              "$ref": "#/$defs/legacy33/$defs/id"
            }
          },
          "required": [
            "type",
            "id"
          ],
          "additionalProperties": false
        },
        "range": {
          "type": "object",
          "properties": {
            "start": {
              "$ref": "#/$defs/legacy33/$defs/nonnegative"
            },
            "duration": {
              "$ref": "#/$defs/legacy33/$defs/positive"
            }
          },
          "required": [
            "start",
            "duration"
          ],
          "additionalProperties": false
        },
        "spelledPitchClass": {
          "type": "object",
          "properties": {
            "step": {
              "enum": [
                "A",
                "B",
                "C",
                "D",
                "E",
                "F",
                "G"
              ]
            },
            "alter": {
              "type": "integer",
              "minimum": -2,
              "maximum": 2
            }
          },
          "required": [
            "step",
            "alter"
          ],
          "additionalProperties": false
        },
        "song": {
          "type": "object",
          "properties": {
            "title": {
              "type": "string"
            },
            "primaryMelodyTrackId": {
              "$ref": "#/$defs/legacy33/$defs/id"
            },
            "localizedTitles": {
              "$ref": "#/$defs/legacy33/$defs/localizedNames",
              "description": "Optional localized song-title alternatives. song.title is the stable fallback."
            },
            "subtitle": {
              "type": "string",
              "description": "Optional original-language subtitle."
            },
            "description": {
              "type": "string",
              "description": "Optional original-language description, including Unicode and line breaks."
            },
            "alternateTitles": {
              "type": "array",
              "items": {
                "$ref": "#/$defs/legacy33/$defs/alternateTitle"
              },
              "description": "Additional stable-ID source-language titles."
            },
            "credits": {
              "type": "array",
              "items": {
                "$ref": "#/$defs/legacy33/$defs/credit"
              },
              "description": "Ordered credit assignments to contributors. Multiple roles and duplicate contributors permitted."
            },
            "genres": {
              "type": "array",
              "items": {
                "$ref": "#/$defs/legacy33/$defs/genre"
              },
              "description": "Optional open-ended ordered genre tags; zero or more allowed. Order is authored display preference, first item is primary if a primary label is desired, not a generator weight. Absent means unspecified."
            }
          },
          "required": [
            "title"
          ],
          "additionalProperties": false
        },
        "section": {
          "type": "object",
          "properties": {
            "id": {
              "$ref": "#/$defs/legacy33/$defs/id"
            },
            "name": {
              "type": "string",
              "minLength": 1
            },
            "start": {
              "$ref": "#/$defs/legacy33/$defs/nonnegative"
            },
            "duration": {
              "$ref": "#/$defs/legacy33/$defs/positive"
            },
            "role": {
              "type": "string"
            },
            "localizedNames": {
              "$ref": "#/$defs/legacy33/$defs/localizedNames",
              "description": "Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity."
            }
          },
          "required": [
            "id",
            "name",
            "start",
            "duration"
          ],
          "additionalProperties": false
        },
        "tempo": {
          "type": "object",
          "properties": {
            "at": {
              "$ref": "#/$defs/legacy33/$defs/nonnegative"
            },
            "bpm": {
              "type": "number",
              "exclusiveMinimum": 0,
              "maximum": 1000
            }
          },
          "required": [
            "at",
            "bpm"
          ],
          "additionalProperties": false
        },
        "meter": {
          "type": "object",
          "properties": {
            "at": {
              "$ref": "#/$defs/legacy33/$defs/nonnegative"
            },
            "numerator": {
              "type": "integer",
              "minimum": 1,
              "maximum": 64
            },
            "denominator": {
              "enum": [
                1,
                2,
                4,
                8,
                16,
                32,
                64
              ],
              "type": "integer"
            }
          },
          "required": [
            "at",
            "numerator",
            "denominator"
          ],
          "additionalProperties": false
        },
        "timeline": {
          "type": "object",
          "properties": {
            "sections": {
              "type": "array",
              "items": {
                "$ref": "#/$defs/legacy33/$defs/section"
              }
            },
            "tempoChanges": {
              "type": "array",
              "items": {
                "$ref": "#/$defs/legacy33/$defs/tempo"
              },
              "minItems": 1
            },
            "meterChanges": {
              "type": "array",
              "items": {
                "$ref": "#/$defs/legacy33/$defs/meter"
              },
              "minItems": 1
            }
          },
          "required": [
            "sections",
            "tempoChanges",
            "meterChanges"
          ],
          "additionalProperties": false
        },
        "chord": {
          "type": "object",
          "properties": {
            "id": {
              "$ref": "#/$defs/legacy33/$defs/id"
            },
            "start": {
              "$ref": "#/$defs/legacy33/$defs/nonnegative"
            },
            "duration": {
              "$ref": "#/$defs/legacy33/$defs/positive"
            },
            "label": {
              "type": "string",
              "minLength": 1
            },
            "root": {
              "$ref": "#/$defs/legacy33/$defs/spelledPitchClass"
            },
            "intervals": {
              "type": "array",
              "items": {
                "type": "integer",
                "minimum": 0,
                "maximum": 35
              },
              "minItems": 1,
              "maxItems": 36,
              "uniqueItems": true,
              "contains": {
                "const": 0
              }
            },
            "bass": {
              "$ref": "#/$defs/legacy33/$defs/spelledPitchClass"
            },
            "voicing": {
              "$ref": "#/$defs/legacy33/$defs/voicing",
              "description": "Optional pitch snapshot (not an arrangement note sequence). No automatic playback."
            }
          },
          "required": [
            "id",
            "start",
            "duration",
            "label"
          ],
          "additionalProperties": false,
          "dependentRequired": {
            "root": [
              "intervals"
            ],
            "intervals": [
              "root"
            ]
          }
        },
        "scale": {
          "type": "object",
          "properties": {
            "id": {
              "$ref": "#/$defs/legacy33/$defs/id"
            },
            "start": {
              "$ref": "#/$defs/legacy33/$defs/nonnegative"
            },
            "duration": {
              "$ref": "#/$defs/legacy33/$defs/positive"
            },
            "label": {
              "type": "string"
            },
            "tonic": {
              "$ref": "#/$defs/legacy33/$defs/spelledPitchClass"
            },
            "intervals": {
              "type": "array",
              "items": {
                "type": "integer",
                "minimum": 0,
                "maximum": 11
              },
              "minItems": 1,
              "maxItems": 12,
              "uniqueItems": true,
              "contains": {
                "const": 0
              }
            }
          },
          "required": [
            "id",
            "start",
            "duration",
            "tonic",
            "intervals"
          ],
          "additionalProperties": false
        },
        "harmony": {
          "type": "object",
          "properties": {
            "chords": {
              "type": "array",
              "items": {
                "$ref": "#/$defs/legacy33/$defs/chord"
              }
            },
            "scales": {
              "type": "array",
              "items": {
                "$ref": "#/$defs/legacy33/$defs/scale"
              }
            }
          },
          "required": [
            "chords",
            "scales"
          ],
          "additionalProperties": false
        },
        "instrument": {
          "type": "object",
          "properties": {
            "name": {
              "type": "string"
            },
            "family": {
              "type": "string"
            },
            "localizedNames": {
              "$ref": "#/$defs/legacy33/$defs/localizedNames",
              "description": "Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity."
            }
          },
          "required": [
            "name"
          ],
          "additionalProperties": false
        },
        "note": {
          "type": "object",
          "properties": {
            "id": {
              "$ref": "#/$defs/legacy33/$defs/id"
            },
            "start": {
              "$ref": "#/$defs/legacy33/$defs/signed"
            },
            "duration": {
              "$ref": "#/$defs/legacy33/$defs/positive",
              "description": "Positive note gate in ticks, not the guaranteed audible duration of a one-shot percussion sample."
            },
            "pitch": {
              "$ref": "#/$defs/legacy33/$defs/pitch"
            },
            "soundSlotId": {
              "$ref": "#/$defs/legacy33/$defs/id",
              "description": "Document-local Sound Slot ID. Distinct events and IDs stay distinct even if several slots share a MIDI key; a renderer decides the acoustic timbre."
            },
            "velocity": {
              "type": "integer",
              "minimum": 1,
              "maximum": 127,
              "description": "Optional authored note-on velocity for performed Core notes, 1–127; omit to mean unspecified. It is not a note-off velocity, controller stream, chord tone, or a sound-rendering guarantee. Never insert an inferred default when saving."
            }
          },
          "required": [
            "id",
            "start",
            "duration"
          ],
          "additionalProperties": false,
          "oneOf": [
            {
              "required": [
                "pitch"
              ],
              "not": {
                "required": [
                  "soundSlotId"
                ]
              }
            },
            {
              "required": [
                "soundSlotId"
              ],
              "not": {
                "required": [
                  "pitch"
                ]
              }
            }
          ],
          "description": "Concrete Core note; optional velocity is a note-on attribute. Phrase templates use a separate version-frozen sourceNote shape."
        },
        "clip": {
          "type": "object",
          "properties": {
            "id": {
              "$ref": "#/$defs/legacy33/$defs/id"
            },
            "name": {
              "type": "string"
            },
            "start": {
              "$ref": "#/$defs/legacy33/$defs/nonnegative"
            },
            "duration": {
              "$ref": "#/$defs/legacy33/$defs/positive"
            },
            "enabled": {
              "type": "boolean",
              "default": true
            },
            "notes": {
              "type": "array",
              "items": {
                "$ref": "#/$defs/legacy33/$defs/note"
              }
            },
            "localizedNames": {
              "$ref": "#/$defs/legacy33/$defs/localizedNames",
              "description": "Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity."
            }
          },
          "required": [
            "id",
            "start",
            "duration",
            "notes"
          ],
          "additionalProperties": false
        },
        "track": {
          "type": "object",
          "properties": {
            "id": {
              "$ref": "#/$defs/legacy33/$defs/id"
            },
            "name": {
              "type": "string"
            },
            "role": {
              "type": "string"
            },
            "instrument": {
              "$ref": "#/$defs/legacy33/$defs/instrument"
            },
            "enabled": {
              "type": "boolean",
              "default": true
            },
            "clips": {
              "type": "array",
              "items": {
                "$ref": "#/$defs/legacy33/$defs/clip"
              }
            },
            "trackType": {
              "enum": [
                "melodic",
                "drum",
                "mixed"
              ],
              "description": "Semantic event-target category; optional; missing/empty-note tracks may be unknown. It is not a DAW track class."
            },
            "preferredView": {
              "enum": [
                "auto",
                "pianoRoll",
                "drumGrid"
              ],
              "default": "auto",
              "description": "Non-binding presentation preference. Does not change note meaning."
            },
            "soundSource": {
              "$ref": "#/$defs/legacy33/$defs/soundSource",
              "description": "Optional sound-source selection hint, not a plug-in state, preset blob, or sound guarantee."
            },
            "localizedNames": {
              "$ref": "#/$defs/legacy33/$defs/localizedNames",
              "description": "Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity."
            },
            "drumKitId": {
              "$ref": "#/$defs/legacy33/$defs/id",
              "description": "Optional reference to a declared drumKit; only for a drum/mixed or empty inferred track. All stored slot events in the track must belong to the referenced kit."
            }
          },
          "required": [
            "id",
            "name",
            "clips"
          ],
          "additionalProperties": false,
          "allOf": [
            {
              "if": {
                "properties": {
                  "trackType": {
                    "const": "melodic"
                  }
                },
                "required": [
                  "trackType"
                ]
              },
              "then": {
                "not": {
                  "required": [
                    "drumKitId"
                  ]
                }
              }
            }
          ]
        },
        "soundSlot": {
          "type": "object",
          "properties": {
            "id": {
              "$ref": "#/$defs/legacy33/$defs/id"
            },
            "name": {
              "type": "string"
            },
            "role": {
              "type": "string",
              "description": "Optional free-text musical role; not a standardized GM instrument code or an acoustic sample identifier."
            },
            "midiNote": {
              "$ref": "#/$defs/legacy33/$defs/pitch",
              "description": "Legacy 3.0 MIDI note hint only; not a GM1 declaration or preview timbre identity."
            },
            "midiMapping": {
              "$ref": "#/$defs/legacy33/$defs/midiMapping",
              "description": "Explicit external MIDI1 output mapping; standard=gm1 is separate from custom even for an equal note number. Not a unique slot or audio identity."
            },
            "localizedNames": {
              "$ref": "#/$defs/legacy33/$defs/localizedNames",
              "description": "Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity."
            }
          },
          "required": [
            "id",
            "name"
          ],
          "additionalProperties": false,
          "description": "Document-local stable logical percussion target. Equal roles, names or MIDI note mappings never merge distinct slot IDs. No sample/audio identity is encoded."
        },
        "lyricDocument": {
          "type": "object",
          "properties": {
            "id": {
              "$ref": "#/$defs/legacy33/$defs/id"
            },
            "title": {
              "type": "string"
            },
            "language": {
              "type": "string"
            }
          },
          "required": [
            "id"
          ],
          "additionalProperties": false
        },
        "lyricPhrase": {
          "type": "object",
          "properties": {
            "id": {
              "$ref": "#/$defs/legacy33/$defs/id"
            },
            "documentId": {
              "$ref": "#/$defs/legacy33/$defs/id"
            },
            "text": {
              "type": "string"
            },
            "pronunciation": {
              "type": "string"
            },
            "start": {
              "$ref": "#/$defs/legacy33/$defs/nonnegative"
            },
            "duration": {
              "$ref": "#/$defs/legacy33/$defs/positive"
            }
          },
          "required": [
            "id",
            "documentId",
            "text"
          ],
          "additionalProperties": false,
          "dependentRequired": {
            "start": [
              "duration"
            ],
            "duration": [
              "start"
            ]
          }
        },
        "lyricUnit": {
          "type": "object",
          "properties": {
            "id": {
              "$ref": "#/$defs/legacy33/$defs/id"
            },
            "phraseId": {
              "$ref": "#/$defs/legacy33/$defs/id"
            },
            "text": {
              "type": "string"
            },
            "pronunciation": {
              "type": "string"
            },
            "start": {
              "$ref": "#/$defs/legacy33/$defs/nonnegative"
            },
            "duration": {
              "$ref": "#/$defs/legacy33/$defs/positive"
            }
          },
          "required": [
            "id",
            "phraseId",
            "text"
          ],
          "additionalProperties": false,
          "dependentRequired": {
            "start": [
              "duration"
            ],
            "duration": [
              "start"
            ]
          }
        },
        "lyricAlignment": {
          "type": "object",
          "properties": {
            "id": {
              "$ref": "#/$defs/legacy33/$defs/id"
            },
            "unitIds": {
              "type": "array",
              "items": {
                "$ref": "#/$defs/legacy33/$defs/id"
              },
              "uniqueItems": true,
              "minItems": 1
            },
            "noteIds": {
              "type": "array",
              "items": {
                "$ref": "#/$defs/legacy33/$defs/id"
              },
              "uniqueItems": true,
              "minItems": 1
            }
          },
          "required": [
            "id",
            "unitIds",
            "noteIds"
          ],
          "additionalProperties": false
        },
        "lyrics": {
          "type": "object",
          "properties": {
            "documents": {
              "type": "array",
              "items": {
                "$ref": "#/$defs/legacy33/$defs/lyricDocument"
              }
            },
            "phrases": {
              "type": "array",
              "items": {
                "$ref": "#/$defs/legacy33/$defs/lyricPhrase"
              }
            },
            "units": {
              "type": "array",
              "items": {
                "$ref": "#/$defs/legacy33/$defs/lyricUnit"
              }
            },
            "alignments": {
              "type": "array",
              "items": {
                "$ref": "#/$defs/legacy33/$defs/lyricAlignment"
              }
            }
          },
          "required": [
            "documents",
            "phrases",
            "units",
            "alignments"
          ],
          "additionalProperties": false
        },
        "sha256": {
          "type": "string",
          "pattern": "^[0-9a-f]{64}$",
          "not": {
            "pattern": "[\\r\\n\\u2028\\u2029]"
          }
        },
        "resource": {
          "type": "object",
          "properties": {
            "id": {
              "$ref": "#/$defs/legacy33/$defs/id"
            },
            "kind": {
              "enum": [
                "audio",
                "midi",
                "text",
                "other"
              ]
            },
            "uri": {
              "type": "string",
              "minLength": 1
            },
            "name": {
              "type": "string"
            },
            "sha256": {
              "$ref": "#/$defs/legacy33/$defs/sha256"
            }
          },
          "required": [
            "id",
            "kind",
            "uri"
          ],
          "additionalProperties": false
        },
        "dependencies": {
          "oneOf": [
            {
              "type": "object",
              "properties": {
                "scope": {
                  "enum": [
                    "document",
                    "none"
                  ]
                }
              },
              "required": [
                "scope"
              ],
              "additionalProperties": false
            },
            {
              "type": "object",
              "properties": {
                "scope": {
                  "const": "objects"
                },
                "refs": {
                  "type": "array",
                  "items": {
                    "$ref": "#/$defs/legacy33/$defs/ref"
                  },
                  "minItems": 1,
                  "uniqueItems": true
                }
              },
              "required": [
                "scope",
                "refs"
              ],
              "additionalProperties": false
            }
          ]
        },
        "extension": {
          "type": "object",
          "properties": {
            "version": {
              "type": "string",
              "minLength": 1
            },
            "status": {
              "enum": [
                "current",
                "stale",
                "unverified"
              ]
            },
            "dependencies": {
              "$ref": "#/$defs/legacy33/$defs/dependencies"
            },
            "data": {}
          },
          "required": [
            "version",
            "status",
            "dependencies",
            "data"
          ],
          "additionalProperties": false
        },
        "relativeAssignment": {
          "type": "object",
          "properties": {
            "noteId": {
              "$ref": "#/$defs/legacy33/$defs/id"
            },
            "basis": {
              "enum": [
                "chordTone",
                "scaleDegree"
              ]
            },
            "contextId": {
              "$ref": "#/$defs/legacy33/$defs/id"
            },
            "anchorPitch": {
              "$ref": "#/$defs/legacy33/$defs/pitch"
            },
            "index": {
              "type": "integer",
              "minimum": 1,
              "maximum": 36
            },
            "chromaticOffset": {
              "type": "integer",
              "minimum": -24,
              "maximum": 24
            }
          },
          "required": [
            "noteId",
            "basis",
            "contextId",
            "anchorPitch",
            "index",
            "chromaticOffset"
          ],
          "additionalProperties": false,
          "allOf": [
            {
              "if": {
                "properties": {
                  "basis": {
                    "const": "scaleDegree"
                  }
                },
                "required": [
                  "basis"
                ]
              },
              "then": {
                "properties": {
                  "index": {
                    "maximum": 12
                  }
                }
              }
            }
          ]
        },
        "relativeData": {
          "type": "object",
          "properties": {
            "assignments": {
              "type": "array",
              "items": {
                "$ref": "#/$defs/legacy33/$defs/relativeAssignment"
              }
            }
          },
          "required": [
            "assignments"
          ],
          "additionalProperties": false
        },
        "generator": {
          "type": "object",
          "properties": {
            "id": {
              "type": "string",
              "minLength": 1
            },
            "version": {
              "type": "string",
              "minLength": 1
            }
          },
          "required": [
            "id",
            "version"
          ],
          "additionalProperties": false
        },
        "generationInput": {
          "type": "object",
          "properties": {
            "role": {
              "type": "string",
              "minLength": 1
            },
            "ref": {
              "$ref": "#/$defs/legacy33/$defs/ref"
            },
            "readRange": {
              "$ref": "#/$defs/legacy33/$defs/range"
            }
          },
          "required": [
            "role",
            "ref"
          ],
          "additionalProperties": false
        },
        "generationProcess": {
          "type": "object",
          "properties": {
            "id": {
              "$ref": "#/$defs/legacy33/$defs/id"
            },
            "generator": {
              "$ref": "#/$defs/legacy33/$defs/generator"
            },
            "inputs": {
              "type": "array",
              "items": {
                "$ref": "#/$defs/legacy33/$defs/generationInput"
              }
            },
            "outputs": {
              "type": "array",
              "items": {
                "$ref": "#/$defs/legacy33/$defs/ref"
              },
              "minItems": 1
            },
            "targetRange": {
              "$ref": "#/$defs/legacy33/$defs/range"
            },
            "protectedNoteIds": {
              "type": "array",
              "items": {
                "$ref": "#/$defs/legacy33/$defs/id"
              },
              "uniqueItems": true
            },
            "vendorExtension": {
              "type": "string",
              "minLength": 1
            }
          },
          "required": [
            "id",
            "generator",
            "inputs",
            "outputs",
            "protectedNoteIds"
          ],
          "additionalProperties": false
        },
        "generationData": {
          "type": "object",
          "properties": {
            "processes": {
              "type": "array",
              "items": {
                "$ref": "#/$defs/legacy33/$defs/generationProcess"
              }
            }
          },
          "required": [
            "processes"
          ],
          "additionalProperties": false
        },
        "color": {
          "type": "string",
          "pattern": "^#[0-9A-Fa-f]{6}$",
          "not": {
            "pattern": "[\\r\\n\\u2028\\u2029]"
          }
        },
        "roleDefinition": {
          "type": "object",
          "properties": {
            "id": {
              "$ref": "#/$defs/legacy33/$defs/id"
            },
            "name": {
              "type": "string",
              "minLength": 1
            },
            "baseRole": {
              "type": "string"
            }
          },
          "required": [
            "id",
            "name"
          ],
          "additionalProperties": false
        },
        "roleColorMap": {
          "type": "object",
          "additionalProperties": {
            "$ref": "#/$defs/legacy33/$defs/color"
          }
        },
        "customRoleColorMap": {
          "type": "object",
          "propertyNames": {
            "$ref": "#/$defs/legacy33/$defs/id"
          },
          "additionalProperties": {
            "$ref": "#/$defs/legacy33/$defs/color"
          }
        },
        "objectColor": {
          "type": "object",
          "properties": {
            "target": {
              "$ref": "#/$defs/legacy33/$defs/ref"
            },
            "color": {
              "$ref": "#/$defs/legacy33/$defs/color"
            }
          },
          "required": [
            "target",
            "color"
          ],
          "additionalProperties": false
        },
        "appearanceData": {
          "type": "object",
          "properties": {
            "roleDefinitions": {
              "type": "array",
              "items": {
                "$ref": "#/$defs/legacy33/$defs/roleDefinition"
              }
            },
            "sectionRoleAssignments": {
              "type": "object",
              "propertyNames": {
                "$ref": "#/$defs/legacy33/$defs/id"
              },
              "additionalProperties": {
                "$ref": "#/$defs/legacy33/$defs/id"
              }
            },
            "appearance": {
              "type": "object",
              "properties": {
                "roleColors": {
                  "$ref": "#/$defs/legacy33/$defs/roleColorMap"
                },
                "customRoleColors": {
                  "$ref": "#/$defs/legacy33/$defs/customRoleColorMap"
                },
                "objectColors": {
                  "type": "array",
                  "items": {
                    "$ref": "#/$defs/legacy33/$defs/objectColor"
                  }
                }
              },
              "required": [
                "roleColors",
                "customRoleColors",
                "objectColors"
              ],
              "additionalProperties": false
            }
          },
          "required": [
            "roleDefinitions",
            "sectionRoleAssignments",
            "appearance"
          ],
          "additionalProperties": false
        },
        "legacyData": {
          "type": "object",
          "properties": {
            "sourceVersion": {
              "const": "2.3.0"
            },
            "sourceSha256": {
              "$ref": "#/$defs/legacy33/$defs/sha256"
            },
            "sourceText": {
              "type": "string",
              "minLength": 1
            },
            "conversionReport": {
              "type": "object"
            }
          },
          "required": [
            "sourceVersion",
            "sourceSha256",
            "sourceText",
            "conversionReport"
          ],
          "additionalProperties": false
        },
        "extensions": {
          "type": "object",
          "propertyNames": {
            "pattern": "^[a-z][a-z0-9-]*(?:\\.[a-z][a-z0-9-]*){2,}$",
            "not": {
              "pattern": "[\\r\\n\\u2028\\u2029]"
            }
          },
          "properties": {
            "org.ostf.relative-phrase.v1": {
              "allOf": [
                {
                  "$ref": "#/$defs/legacy33/$defs/extension"
                },
                {
                  "if": {
                    "properties": {
                      "version": {
                        "const": "1.0.0-draft.1"
                      }
                    },
                    "required": [
                      "version"
                    ]
                  },
                  "then": {
                    "properties": {
                      "data": {
                        "$ref": "#/$defs/legacy33/$defs/relativeData"
                      }
                    }
                  }
                }
              ]
            },
            "org.ostf.generation-context.v1": {
              "allOf": [
                {
                  "$ref": "#/$defs/legacy33/$defs/extension"
                },
                {
                  "if": {
                    "properties": {
                      "version": {
                        "const": "1.0.0-draft.1"
                      }
                    },
                    "required": [
                      "version"
                    ]
                  },
                  "then": {
                    "properties": {
                      "data": {
                        "$ref": "#/$defs/legacy33/$defs/generationData"
                      }
                    }
                  }
                }
              ]
            },
            "org.ostf.appearance.v1": {
              "allOf": [
                {
                  "$ref": "#/$defs/legacy33/$defs/extension"
                },
                {
                  "if": {
                    "properties": {
                      "version": {
                        "const": "1.0.0-draft.1"
                      }
                    },
                    "required": [
                      "version"
                    ]
                  },
                  "then": {
                    "properties": {
                      "data": {
                        "$ref": "#/$defs/legacy33/$defs/appearanceData"
                      }
                    }
                  }
                }
              ]
            },
            "org.ostf.legacy-import.v1": {
              "allOf": [
                {
                  "$ref": "#/$defs/legacy33/$defs/extension"
                },
                {
                  "if": {
                    "properties": {
                      "version": {
                        "const": "1.0.0-draft.1"
                      }
                    },
                    "required": [
                      "version"
                    ]
                  },
                  "then": {
                    "properties": {
                      "data": {
                        "$ref": "#/$defs/legacy33/$defs/legacyData"
                      }
                    }
                  }
                }
              ]
            },
            "org.ostf.phrase-library.v1": {
              "allOf": [
                {
                  "$ref": "#/$defs/legacy33/$defs/extension"
                },
                {
                  "if": {
                    "properties": {
                      "version": {
                        "const": "1.0.0-draft.1"
                      }
                    },
                    "required": [
                      "version"
                    ]
                  },
                  "then": {
                    "properties": {
                      "data": {
                        "$ref": "#/$defs/legacy33/$defs/phraseLibraryData"
                      }
                    }
                  }
                }
              ]
            },
            "org.ostf.clip-choices.v1": {
              "allOf": [
                {
                  "$ref": "#/$defs/legacy33/$defs/extension"
                },
                {
                  "if": {
                    "properties": {
                      "version": {
                        "const": "1.0.0-draft.1"
                      }
                    },
                    "required": [
                      "version"
                    ]
                  },
                  "then": {
                    "properties": {
                      "data": {
                        "$ref": "#/$defs/legacy33/$defs/clipChoicesData"
                      }
                    }
                  }
                }
              ]
            },
            "org.ostf.localization.v1": {
              "allOf": [
                {
                  "$ref": "#/$defs/legacy33/$defs/extension"
                },
                {
                  "if": {
                    "properties": {
                      "version": {
                        "const": "1.0.0"
                      }
                    },
                    "required": [
                      "version"
                    ]
                  },
                  "then": {
                    "properties": {
                      "data": {
                        "$ref": "#/$defs/legacy33/$defs/localizationData"
                      }
                    }
                  }
                }
              ]
            }
          },
          "additionalProperties": {
            "$ref": "#/$defs/legacy33/$defs/extension"
          }
        },
        "phraseTemplate": {
          "type": "object",
          "properties": {
            "id": {
              "$ref": "#/$defs/legacy33/$defs/id"
            },
            "duration": {
              "$ref": "#/$defs/legacy33/$defs/positive"
            },
            "notes": {
              "type": "array",
              "items": {
                "$ref": "#/$defs/legacy33/$defs/phraseSourceNote"
              }
            },
            "name": {
              "type": "string"
            }
          },
          "required": [
            "id",
            "duration",
            "notes"
          ],
          "additionalProperties": false
        },
        "phraseNoteMapping": {
          "type": "object",
          "properties": {
            "templateNoteId": {
              "$ref": "#/$defs/legacy33/$defs/id"
            },
            "repeatIndex": {
              "$ref": "#/$defs/legacy33/$defs/nonnegative"
            },
            "noteId": {
              "$ref": "#/$defs/legacy33/$defs/id"
            }
          },
          "required": [
            "templateNoteId",
            "repeatIndex",
            "noteId"
          ],
          "additionalProperties": false
        },
        "phraseInstance": {
          "type": "object",
          "properties": {
            "id": {
              "$ref": "#/$defs/legacy33/$defs/id"
            },
            "templateId": {
              "$ref": "#/$defs/legacy33/$defs/id"
            },
            "clipId": {
              "$ref": "#/$defs/legacy33/$defs/id"
            },
            "repeatCount": {
              "$ref": "#/$defs/legacy33/$defs/positive"
            },
            "transpose": {
              "type": "integer",
              "minimum": -127,
              "maximum": 127
            },
            "noteMap": {
              "type": "array",
              "items": {
                "$ref": "#/$defs/legacy33/$defs/phraseNoteMapping"
              }
            }
          },
          "required": [
            "id",
            "templateId",
            "clipId",
            "repeatCount",
            "transpose",
            "noteMap"
          ],
          "additionalProperties": false
        },
        "phraseLibraryData": {
          "type": "object",
          "properties": {
            "templates": {
              "type": "array",
              "items": {
                "$ref": "#/$defs/legacy33/$defs/phraseTemplate"
              }
            },
            "instances": {
              "type": "array",
              "items": {
                "$ref": "#/$defs/legacy33/$defs/phraseInstance"
              }
            }
          },
          "required": [
            "templates",
            "instances"
          ],
          "additionalProperties": false
        },
        "clipCandidate": {
          "type": "object",
          "properties": {
            "id": {
              "$ref": "#/$defs/legacy33/$defs/id"
            },
            "clipIds": {
              "type": "array",
              "items": {
                "$ref": "#/$defs/legacy33/$defs/id"
              },
              "uniqueItems": true
            },
            "name": {
              "type": "string"
            }
          },
          "required": [
            "id",
            "clipIds"
          ],
          "additionalProperties": false
        },
        "clipChoiceGroup": {
          "type": "object",
          "properties": {
            "id": {
              "$ref": "#/$defs/legacy33/$defs/id"
            },
            "candidates": {
              "type": "array",
              "items": {
                "$ref": "#/$defs/legacy33/$defs/clipCandidate"
              },
              "minItems": 1
            },
            "selectedCandidateId": {
              "anyOf": [
                {
                  "$ref": "#/$defs/legacy33/$defs/id"
                },
                {
                  "type": "null"
                }
              ]
            },
            "name": {
              "type": "string"
            }
          },
          "required": [
            "id",
            "candidates",
            "selectedCandidateId"
          ],
          "additionalProperties": false
        },
        "clipChoicesData": {
          "type": "object",
          "properties": {
            "groups": {
              "type": "array",
              "items": {
                "$ref": "#/$defs/legacy33/$defs/clipChoiceGroup"
              }
            }
          },
          "required": [
            "groups"
          ],
          "additionalProperties": false
        },
        "midiMapping": {
          "type": "object",
          "properties": {
            "standard": {
              "enum": [
                "gm1",
                "custom"
              ],
              "description": "gm1=GM Level 1 percussion key 35..81; custom=explicit arbitrary MIDI1 note number."
            },
            "note": {
              "$ref": "#/$defs/legacy33/$defs/pitch",
              "description": "MIDI1 note number in 0..127; for gm1 restrict to 35..81."
            }
          },
          "required": [
            "standard",
            "note"
          ],
          "additionalProperties": false,
          "allOf": [
            {
              "if": {
                "properties": {
                  "standard": {
                    "const": "gm1"
                  }
                },
                "required": [
                  "standard"
                ]
              },
              "then": {
                "properties": {
                  "note": {
                    "type": "integer",
                    "minimum": 35,
                    "maximum": 81
                  }
                }
              }
            }
          ]
        },
        "soundSource": {
          "type": "object",
          "description": "Optional informational rendering class or opaque destination hint. Program Change, Bank Select and plugin presets are not standardized by Core.",
          "properties": {
            "kind": {
              "enum": [
                "unassigned",
                "gm1",
                "externalMidi",
                "plugin",
                "hostManaged"
              ]
            },
            "identifier": {
              "type": "string",
              "minLength": 1,
              "description": "Opaque target identifier, e.g. URI, plug-in identifier or port alias, not a loading command."
            }
          },
          "required": [
            "kind"
          ],
          "additionalProperties": false,
          "allOf": [
            {
              "if": {
                "properties": {
                  "kind": {
                    "enum": [
                      "gm1",
                      "unassigned"
                    ]
                  }
                },
                "required": [
                  "kind"
                ]
              },
              "then": {
                "not": {
                  "required": [
                    "identifier"
                  ]
                }
              }
            }
          ]
        },
        "localizedNames": {
          "type": "object",
          "minProperties": 1,
          "propertyNames": {
            "type": "string",
            "pattern": "^(?:[A-Za-z]{2,3}|[A-Za-z]{5,8})(?:-[A-Za-z0-9]{2,8})*$"
          },
          "additionalProperties": {
            "type": "string",
            "minLength": 1
          },
          "description": "Optional translations indexed by a conservative BCP 47 language-tag subset. The original name/title remains authoritative and is never rewritten by locale changes. Case-insensitive duplicate tags are forbidden semantically."
        },
        "drumKit": {
          "type": "object",
          "description": "Optional named ordered membership of global Sound Slot IDs. Does not define plugin preset, sample loading, choke or a kit-local MIDI remapping.",
          "properties": {
            "id": {
              "$ref": "#/$defs/legacy33/$defs/id"
            },
            "name": {
              "type": "string"
            },
            "localizedNames": {
              "$ref": "#/$defs/legacy33/$defs/localizedNames"
            },
            "soundSlotIds": {
              "type": "array",
              "uniqueItems": true,
              "items": {
                "$ref": "#/$defs/legacy33/$defs/id"
              },
              "description": "Ordered, unique references to global soundSlots; may be empty."
            }
          },
          "required": [
            "id",
            "name",
            "soundSlotIds"
          ],
          "additionalProperties": false
        },
        "phraseSourceNote": {
          "type": "object",
          "properties": {
            "id": {
              "$ref": "#/$defs/legacy33/$defs/id"
            },
            "start": {
              "$ref": "#/$defs/legacy33/$defs/signed"
            },
            "duration": {
              "$ref": "#/$defs/legacy33/$defs/positive"
            },
            "pitch": {
              "$ref": "#/$defs/legacy33/$defs/pitch"
            },
            "soundSlotId": {
              "$ref": "#/$defs/legacy33/$defs/id"
            }
          },
          "required": [
            "id",
            "start",
            "duration"
          ],
          "additionalProperties": false,
          "oneOf": [
            {
              "required": [
                "pitch"
              ],
              "not": {
                "required": [
                  "soundSlotId"
                ]
              }
            },
            {
              "required": [
                "soundSlotId"
              ],
              "not": {
                "required": [
                  "pitch"
                ]
              }
            }
          ],
          "description": "Version-frozen 1.0.0-draft.1 phrase source note. Does NOT admit velocity; a linked Core instance may independently set velocity."
        },
        "voicing": {
          "type": "object",
          "additionalProperties": false,
          "description": "Optional informational chord voicing snapshot, not a played Core note collection. Repeated pitches and original array order have meaning for lossless preservation. Per-entry velocity is an optional voicing-preview hint.",
          "properties": {
            "pitches": {
              "type": "array",
              "minItems": 1,
              "items": {
                "$ref": "#/$defs/legacy33/$defs/pitch"
              },
              "description": "Ordered multiset of concrete absolute pitches, 0-127. Duplicates allowed."
            },
            "velocities": {
              "type": "array",
              "minItems": 1,
              "items": {
                "anyOf": [
                  {
                    "type": "integer",
                    "minimum": 1,
                    "maximum": 127
                  },
                  {
                    "type": "null"
                  }
                ]
              },
              "description": "Optional positional velocities aligned one-to-one to pitches. Null means unspecified at this index, not 0. Exact equal-length rule is semantic."
            }
          },
          "required": [
            "pitches"
          ]
        },
        "contributor": {
          "type": "object",
          "additionalProperties": false,
          "description": "One song-local identity; same contributor can receive multiple credit roles. Unicode source name is authoritative.",
          "properties": {
            "id": {
              "$ref": "#/$defs/legacy33/$defs/id"
            },
            "name": {
              "type": "string",
              "minLength": 1
            },
            "kind": {
              "enum": [
                "person",
                "organization",
                "other"
              ]
            },
            "localizedNames": {
              "$ref": "#/$defs/legacy33/$defs/localizedNames"
            }
          },
          "required": [
            "id",
            "name"
          ]
        },
        "credit": {
          "type": "object",
          "additionalProperties": false,
          "description": "Ordered credit assignment referencing one contributor; role is an open semantic token, not a translated label.",
          "properties": {
            "id": {
              "$ref": "#/$defs/legacy33/$defs/id"
            },
            "contributorId": {
              "$ref": "#/$defs/legacy33/$defs/id"
            },
            "role": {
              "type": "string",
              "pattern": "^[a-z][a-z0-9.-]*$"
            },
            "label": {
              "type": "string"
            }
          },
          "required": [
            "id",
            "contributorId",
            "role"
          ]
        },
        "alternateTitle": {
          "type": "object",
          "additionalProperties": false,
          "description": "Stable-ID song title alternative; array position and title text do not identify it.",
          "properties": {
            "id": {
              "$ref": "#/$defs/legacy33/$defs/id"
            },
            "title": {
              "type": "string",
              "minLength": 1
            }
          },
          "required": [
            "id",
            "title"
          ]
        },
        "languageMap32": {
          "type": "object",
          "minProperties": 1,
          "propertyNames": {
            "type": "string",
            "pattern": "^[A-Za-z]{1,8}(?:-[A-Za-z0-9]{1,8})*$"
          },
          "additionalProperties": {
            "type": "string"
          },
          "description": "Open BCP 47 language-tag dictionary. Schema checks loose subtag structure; full BCP 47 well-formedness and case-insensitive uniqueness are semantic requirements. String may be empty if intentionally blank."
        },
        "localizationTarget": {
          "type": "object",
          "additionalProperties": false,
          "properties": {
            "kind": {
              "enum": [
                "song",
                "alternateTitle",
                "contributor",
                "credit",
                "section",
                "track",
                "clip",
                "soundSlot",
                "drumKit",
                "lyricDocument",
                "resource",
                "phraseTemplate",
                "clipCandidate",
                "clipChoiceGroup",
                "roleDefinition",
                "genre"
              ]
            },
            "id": {
              "$ref": "#/$defs/legacy33/$defs/id"
            },
            "profile": {
              "type": "string",
              "enum": [
                "org.ostf.phrase-library.v1",
                "org.ostf.clip-choices.v1",
                "org.ostf.appearance.v1"
              ]
            }
          },
          "required": [
            "kind"
          ],
          "allOf": [
            {
              "if": {
                "properties": {
                  "kind": {
                    "const": "song"
                  }
                },
                "required": [
                  "kind"
                ]
              },
              "then": {
                "not": {
                  "anyOf": [
                    {
                      "required": [
                        "id"
                      ]
                    },
                    {
                      "required": [
                        "profile"
                      ]
                    }
                  ]
                }
              },
              "else": {
                "required": [
                  "id"
                ]
              }
            },
            {
              "if": {
                "properties": {
                  "kind": {
                    "enum": [
                      "phraseTemplate",
                      "clipCandidate",
                      "clipChoiceGroup",
                      "roleDefinition"
                    ]
                  }
                },
                "required": [
                  "kind"
                ]
              },
              "then": {
                "required": [
                  "profile"
                ]
              },
              "else": {
                "not": {
                  "required": [
                    "profile"
                  ]
                }
              }
            }
          ],
          "description": "Stable target by Core ID or profile-local scoped ID; song is the only ID-less target. No array indexes or mutable names as locators."
        },
        "localizationEntry": {
          "type": "object",
          "additionalProperties": false,
          "properties": {
            "target": {
              "$ref": "#/$defs/legacy33/$defs/localizationTarget"
            },
            "field": {
              "type": "string",
              "minLength": 1,
              "description": "Exact allowed source text field for this target kind (see normative matrix). No arbitrary path or musical value fields."
            },
            "values": {
              "$ref": "#/$defs/legacy33/$defs/languageMap32"
            }
          },
          "required": [
            "target",
            "field",
            "values"
          ],
          "description": "Independent translations for one stable source field. Original source text remains authoritative as fallback."
        },
        "localizationData": {
          "type": "object",
          "additionalProperties": false,
          "properties": {
            "entries": {
              "type": "array",
              "items": {
                "$ref": "#/$defs/legacy33/$defs/localizationEntry"
              }
            }
          },
          "required": [
            "entries"
          ],
          "description": "Language-map translations indexed by stable kind/id/field, never by names or array positions."
        },
        "genre": {
          "type": "object",
          "description": "One song-local open genre tag. The label is authored Unicode text and not a predefined controlled taxonomy; ID is stable for metadata merges and localization.",
          "properties": {
            "id": {
              "$ref": "#/$defs/legacy33/$defs/id",
              "description": "Stable song-local ID unique among all Core objects."
            },
            "name": {
              "type": "string",
              "minLength": 1,
              "description": "Original Unicode genre label, never normalized or rewritten during import."
            },
            "externalUri": {
              "type": "string",
              "minLength": 1,
              "format": "uri",
              "description": "Optional external taxonomy URI hint; never authoritative for a local genre label, and never auto-dereferenced."
            }
          },
          "required": [
            "id",
            "name"
          ],
          "additionalProperties": false
        }
      }
    },
    "opaqueDocumentId": {
      "type": "string",
      "minLength": 1,
      "description": "Stable URI or UUID-style identifier for a document lineage. Compared as exact Unicode text; never fetched."
    },
    "revisionRef": {
      "type": "object",
      "properties": {
        "documentId": {
          "$ref": "#/$defs/opaqueDocumentId"
        },
        "revisionId": {
          "$ref": "#/$defs/opaqueDocumentId"
        },
        "sha256": {
          "$ref": "#/$defs/sha256"
        }
      },
      "required": [
        "documentId",
        "revisionId"
      ],
      "additionalProperties": false
    },
    "software": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "minLength": 1
        },
        "version": {
          "type": "string",
          "minLength": 1
        }
      },
      "required": [
        "name"
      ],
      "additionalProperties": false
    },
    "documentInfo": {
      "type": "object",
      "properties": {
        "id": {
          "$ref": "#/$defs/opaqueDocumentId"
        },
        "revisionId": {
          "$ref": "#/$defs/opaqueDocumentId"
        },
        "parents": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/revisionRef"
          },
          "uniqueItems": true
        },
        "createdBy": {
          "$ref": "#/$defs/software"
        },
        "modifiedBy": {
          "$ref": "#/$defs/software"
        }
      },
      "required": [
        "id",
        "revisionId"
      ],
      "additionalProperties": false
    },
    "key": {
      "type": "object",
      "properties": {
        "state": {
          "enum": [
            "tonal",
            "atonal",
            "unspecified"
          ]
        },
        "tonic": {
          "$ref": "#/$defs/spelledPitchClass"
        },
        "mode": {
          "type": "string",
          "minLength": 1,
          "description": "Authored mode identifier. Canonical recognized values include major, minor, dorian, phrygian, lydian, mixolydian, locrian. Unknown values are preserved, never converted to major/minor."
        },
        "label": {
          "type": "string"
        }
      },
      "required": [
        "state"
      ],
      "additionalProperties": false,
      "allOf": [
        {
          "if": {
            "properties": {
              "state": {
                "const": "tonal"
              }
            },
            "required": [
              "state"
            ]
          },
          "then": {
            "required": [
              "tonic",
              "mode"
            ]
          },
          "else": {
            "not": {
              "anyOf": [
                {
                  "required": [
                    "tonic"
                  ]
                },
                {
                  "required": [
                    "mode"
                  ]
                }
              ]
            }
          }
        }
      ]
    },
    "keyChange": {
      "type": "object",
      "properties": {
        "id": {
          "$ref": "#/$defs/id"
        },
        "at": {
          "$ref": "#/$defs/positive"
        },
        "key": {
          "$ref": "#/$defs/key"
        },
        "label": {
          "type": "string"
        }
      },
      "required": [
        "id",
        "at",
        "key"
      ],
      "additionalProperties": false,
      "description": "A change after tick zero; initial key is stored only at song.key. Change at tick 0 is forbidden to prevent dual authority."
    },
    "scaleDefinition": {
      "type": "object",
      "properties": {
        "id": {
          "$ref": "#/$defs/id"
        },
        "tonic": {
          "$ref": "#/$defs/spelledPitchClass"
        },
        "intervals": {
          "type": "array",
          "items": {
            "type": "integer",
            "minimum": 0,
            "maximum": 11
          },
          "minItems": 1,
          "maxItems": 12,
          "uniqueItems": true,
          "contains": {
            "const": 0
          }
        },
        "label": {
          "type": "string"
        }
      },
      "required": [
        "id",
        "tonic",
        "intervals"
      ],
      "additionalProperties": false
    },
    "scaleTarget": {
      "type": "object",
      "properties": {
        "type": {
          "enum": [
            "section",
            "track",
            "clip",
            "chord",
            "note"
          ]
        },
        "id": {
          "$ref": "#/$defs/id"
        }
      },
      "required": [
        "type",
        "id"
      ],
      "additionalProperties": false
    },
    "mood": {
      "type": "object",
      "description": "Authored descriptive mood tag; not a generator preset or a probability.",
      "properties": {
        "id": {
          "$ref": "#/$defs/id",
          "description": "Stable song-local ID unique among all Core objects."
        },
        "name": {
          "type": "string",
          "minLength": 1,
          "description": "Original Unicode genre label, never normalized or rewritten during import."
        },
        "externalUri": {
          "type": "string",
          "minLength": 1,
          "format": "uri",
          "description": "Optional external vocabulary URI hint; never authoritative for the authored mood name and never auto-dereferenced."
        }
      },
      "required": [
        "id",
        "name"
      ],
      "additionalProperties": false
    },
    "rightsStatement": {
      "type": "object",
      "properties": {
        "notice": {
          "type": "string"
        },
        "licenseUri": {
          "type": "string",
          "minLength": 1
        },
        "rightsHolderIds": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/id"
          },
          "uniqueItems": true
        }
      },
      "required": [],
      "additionalProperties": false,
      "description": "Authored rights statement only; no rights or permissions are inferred or granted by the format.",
      "minProperties": 1
    },
    "grooveIntent": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "unitTicks": {
          "$ref": "#/$defs/positive"
        },
        "longWeight": {
          "type": "integer",
          "minimum": 1,
          "maximum": 1000000
        },
        "shortWeight": {
          "type": "integer",
          "minimum": 1,
          "maximum": 1000000
        }
      },
      "required": [],
      "additionalProperties": false,
      "description": "Descriptive generation intent only. Never re-apply to already stored notes. unitTicks is one unswung subdivision; two subdivisions form a pair.",
      "minProperties": 1,
      "dependentRequired": {
        "unitTicks": [
          "longWeight",
          "shortWeight"
        ],
        "longWeight": [
          "unitTicks",
          "shortWeight"
        ],
        "shortWeight": [
          "unitTicks",
          "longWeight"
        ]
      }
    },
    "generationIntent": {
      "type": "object",
      "properties": {
        "genreNames": {
          "type": "array",
          "items": {
            "type": "string",
            "minLength": 1
          }
        },
        "moodNames": {
          "type": "array",
          "items": {
            "type": "string",
            "minLength": 1
          }
        },
        "groove": {
          "$ref": "#/$defs/grooveIntent"
        },
        "prompt": {
          "type": "string"
        },
        "seed": {
          "type": "string"
        }
      },
      "required": [],
      "additionalProperties": false,
      "description": "Portable description of intent, not a promise to reproduce an algorithm. Does not change song.genres or song.moods."
    },
    "relativePhrases": {
      "type": "object",
      "properties": {
        "status": {
          "enum": [
            "current",
            "stale",
            "unverified"
          ]
        },
        "dependencies": {
          "$ref": "#/$defs/dependencies"
        },
        "assignments": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/relativeAssignment"
          }
        }
      },
      "required": [
        "status",
        "dependencies",
        "assignments"
      ],
      "additionalProperties": false,
      "description": "Standard optional Core object under root version 4.0.0, not an extension. Current relationships must be consistent with saved Core; loading never performs editing or generation."
    },
    "generation": {
      "type": "object",
      "properties": {
        "status": {
          "enum": [
            "current",
            "stale",
            "unverified"
          ]
        },
        "dependencies": {
          "$ref": "#/$defs/dependencies"
        },
        "processes": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/generationProcess"
          }
        }
      },
      "required": [
        "status",
        "dependencies",
        "processes"
      ],
      "additionalProperties": false,
      "description": "Standard optional Core object under root version 4.0.0, not an extension. Current relationships must be consistent with saved Core; loading never performs editing or generation."
    },
    "presentation": {
      "type": "object",
      "properties": {
        "status": {
          "enum": [
            "current",
            "stale",
            "unverified"
          ]
        },
        "dependencies": {
          "$ref": "#/$defs/dependencies"
        },
        "roleDefinitions": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/roleDefinition"
          }
        },
        "sectionRoleAssignments": {
          "type": "object",
          "propertyNames": {
            "$ref": "#/$defs/id"
          },
          "additionalProperties": {
            "$ref": "#/$defs/id"
          }
        },
        "appearance": {
          "type": "object",
          "properties": {
            "roleColors": {
              "$ref": "#/$defs/roleColorMap"
            },
            "customRoleColors": {
              "$ref": "#/$defs/customRoleColorMap"
            },
            "objectColors": {
              "type": "array",
              "items": {
                "$ref": "#/$defs/objectColor"
              }
            }
          },
          "required": [
            "roleColors",
            "customRoleColors",
            "objectColors"
          ],
          "additionalProperties": false
        }
      },
      "required": [
        "status",
        "dependencies",
        "roleDefinitions",
        "sectionRoleAssignments",
        "appearance"
      ],
      "additionalProperties": false,
      "description": "Standard optional Core object under root version 4.0.0, not an extension. Current relationships must be consistent with saved Core; loading never performs editing or generation."
    },
    "phraseLibrary": {
      "type": "object",
      "properties": {
        "status": {
          "enum": [
            "current",
            "stale",
            "unverified"
          ]
        },
        "dependencies": {
          "$ref": "#/$defs/dependencies"
        },
        "templates": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/phraseTemplate"
          }
        },
        "instances": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/phraseInstance"
          }
        }
      },
      "required": [
        "status",
        "dependencies",
        "templates",
        "instances"
      ],
      "additionalProperties": false,
      "description": "Standard optional Core object under root version 4.0.0, not an extension. Current relationships must be consistent with saved Core; loading never performs editing or generation."
    },
    "clipChoices": {
      "type": "object",
      "properties": {
        "status": {
          "enum": [
            "current",
            "stale",
            "unverified"
          ]
        },
        "dependencies": {
          "$ref": "#/$defs/dependencies"
        },
        "groups": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/clipChoiceGroup"
          }
        }
      },
      "required": [
        "status",
        "dependencies",
        "groups"
      ],
      "additionalProperties": false,
      "description": "Standard optional Core object under root version 4.0.0, not an extension. Current relationships must be consistent with saved Core; loading never performs editing or generation."
    },
    "localization": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "status": {
          "enum": [
            "current",
            "stale",
            "unverified"
          ]
        },
        "dependencies": {
          "$ref": "#/$defs/dependencies"
        },
        "entries": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/localizationEntry"
          }
        }
      },
      "required": [
        "status",
        "dependencies",
        "entries"
      ],
      "description": "Standard optional Core object under root version 4.0.0, not an extension. Current relationships must be consistent with saved Core; loading never performs editing or generation."
    },
    "corePhraseSourceNote": {
      "type": "object",
      "properties": {
        "id": {
          "$ref": "#/$defs/id"
        },
        "start": {
          "$ref": "#/$defs/signed"
        },
        "duration": {
          "$ref": "#/$defs/positive",
          "description": "Positive note gate in ticks, not the guaranteed audible duration of a one-shot percussion sample."
        },
        "pitch": {
          "$ref": "#/$defs/pitch"
        },
        "soundSlotId": {
          "$ref": "#/$defs/id",
          "description": "Document-local Sound Slot ID. Distinct events and IDs stay distinct even if several slots share a MIDI key; a renderer decides the acoustic timbre."
        },
        "velocity": {
          "type": "integer",
          "minimum": 1,
          "maximum": 127,
          "description": "Optional template note-on velocity, 1–127. Applied only by an explicit materialization/update according to instance.velocityMode; never a performed event by itself."
        },
        "enabled": {
          "type": "boolean",
          "default": true,
          "description": "Optional note-local enable state. Omitted means enabled. False preserves the note but suppresses scheduling/playback; it is distinct from probability=0."
        },
        "releaseVelocity": {
          "type": "integer",
          "minimum": 0,
          "maximum": 127,
          "description": "Optional MIDI Note Off/release velocity, 0-127. Omit when unspecified; readers must not invent and write back a default."
        },
        "probability": {
          "type": "number",
          "minimum": 0,
          "maximum": 1,
          "default": 1,
          "description": "Optional note-playback probability from 0.0 to 1.0. Omitted means 1.0. Random sequence identity is not standardized; materialize notes for deterministic interchange."
        },
        "velocityDeviation": {
          "type": "integer",
          "minimum": -126,
          "maximum": 126,
          "default": 0,
          "description": "Optional note-local velocity variation endpoint relative to velocity. Requires velocity. Semantic rule: velocity + velocityDeviation must remain within 1..127. Omitted means 0."
        },
        "pitchRole": {
          "enum": [
            "musical",
            "fixedTrigger"
          ],
          "default": "musical",
          "description": "Meaning of a pitch note. musical participates in pitch/harmony/transpose operations; fixedTrigger is an exact MIDI key trigger (for example a keyswitch) and is never transposed or used as musical-pitch evidence. Allowed only on pitch notes."
        }
      },
      "required": [
        "id",
        "start",
        "duration"
      ],
      "additionalProperties": false,
      "oneOf": [
        {
          "required": [
            "pitch"
          ],
          "not": {
            "required": [
              "soundSlotId"
            ]
          }
        },
        {
          "required": [
            "soundSlotId"
          ],
          "not": {
            "required": [
              "pitch"
            ]
          }
        }
      ],
      "description": "Template-local source note for phrase materialization. It carries the same note-local 3.5 properties as concrete notes. It is not performed by itself; concrete track notes remain the saved playback events.",
      "dependentRequired": {
        "velocityDeviation": [
          "velocity"
        ]
      },
      "allOf": [
        {
          "if": {
            "required": [
              "soundSlotId"
            ]
          },
          "then": {
            "not": {
              "required": [
                "pitchRole"
              ]
            }
          }
        }
      ]
    },
    "provenanceSource": {
      "type": "object",
      "properties": {
        "format": {
          "type": "string",
          "minLength": 1
        },
        "version": {
          "type": "string",
          "minLength": 1
        },
        "sha256": {
          "$ref": "#/$defs/sha256"
        },
        "uri": {
          "type": "string",
          "minLength": 1
        },
        "documentId": {
          "$ref": "#/$defs/opaqueDocumentId"
        },
        "revisionId": {
          "$ref": "#/$defs/opaqueDocumentId"
        },
        "resourceId": {
          "$ref": "#/$defs/id"
        }
      },
      "required": [],
      "additionalProperties": false,
      "description": "Historical source; hashes refer to exact source bytes, not the current document. No automatic retrieval.",
      "minProperties": 1,
      "dependentRequired": {
        "revisionId": [
          "documentId"
        ]
      }
    },
    "provenanceRecord": {
      "type": "object",
      "properties": {
        "id": {
          "$ref": "#/$defs/id"
        },
        "action": {
          "enum": [
            "create",
            "import",
            "conversion",
            "edit",
            "transpose",
            "merge",
            "generation",
            "other"
          ]
        },
        "description": {
          "type": "string"
        },
        "tool": {
          "$ref": "#/$defs/software"
        },
        "sources": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/provenanceSource"
          }
        },
        "semitones": {
          "type": "integer",
          "minimum": -127,
          "maximum": 127
        },
        "beforeKey": {
          "$ref": "#/$defs/key"
        },
        "afterKey": {
          "$ref": "#/$defs/key"
        }
      },
      "required": [
        "id",
        "action"
      ],
      "additionalProperties": false,
      "allOf": [
        {
          "if": {
            "not": {
              "properties": {
                "action": {
                  "const": "transpose"
                }
              },
              "required": [
                "action"
              ]
            }
          },
          "then": {
            "not": {
              "required": [
                "semitones"
              ]
            }
          }
        }
      ]
    },
    "provenance": {
      "type": "object",
      "properties": {
        "records": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/provenanceRecord"
          }
        }
      },
      "required": [
        "records"
      ],
      "additionalProperties": false,
      "description": "Non-executable historical assertions; not composer credits and not a substitute for current metadata. Does not prove authorship or operation correctness."
    },
    "midiChannel": {
      "type": "integer",
      "minimum": 1,
      "maximum": 16,
      "description": "Human-readable MIDI 1.0 channel number 1..16. Wire status-nibble channel = value - 1."
    },
    "midiBus": {
      "type": "object",
      "description": "Document-local logical MIDI destination. Each bus has its own MIDI channel namespace. It is not a physical OS/USB/DAW port binding.",
      "properties": {
        "id": {
          "$ref": "#/$defs/id"
        },
        "name": {
          "type": "string"
        }
      },
      "required": [
        "id",
        "name"
      ],
      "additionalProperties": false
    },
    "midi": {
      "type": "object",
      "properties": {
        "buses": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/midiBus"
          }
        }
      },
      "required": [
        "buses"
      ],
      "additionalProperties": false
    },
    "mpeSettings": {
      "type": "object",
      "description": "Semantic MPE zone declaration. Lower-zone master is channel 1 and upper-zone master is channel 16; member channels are derived contiguously from memberChannelCount.",
      "properties": {
        "zone": {
          "enum": [
            "lower",
            "upper"
          ]
        },
        "memberChannelCount": {
          "type": "integer",
          "minimum": 1,
          "maximum": 15
        }
      },
      "required": [
        "zone",
        "memberChannelCount"
      ],
      "additionalProperties": false
    },
    "trackMidi": {
      "type": "object",
      "description": "Optional MIDI channel/routing interpretation for a track. busId is a logical OSTF bus, never a physical MIDI port.",
      "properties": {
        "busId": {
          "$ref": "#/$defs/id"
        },
        "mode": {
          "enum": [
            "singleChannel",
            "multiChannel",
            "mpe"
          ]
        },
        "channel": {
          "$ref": "#/$defs/midiChannel"
        },
        "mpe": {
          "$ref": "#/$defs/mpeSettings"
        }
      },
      "required": [
        "mode"
      ],
      "additionalProperties": false,
      "allOf": [
        {
          "if": {
            "properties": {
              "mode": {
                "const": "singleChannel"
              }
            },
            "required": [
              "mode"
            ]
          },
          "then": {
            "required": [
              "channel"
            ],
            "not": {
              "required": [
                "mpe"
              ]
            }
          }
        },
        {
          "if": {
            "properties": {
              "mode": {
                "const": "multiChannel"
              }
            },
            "required": [
              "mode"
            ]
          },
          "then": {
            "not": {
              "anyOf": [
                {
                  "required": [
                    "channel"
                  ]
                },
                {
                  "required": [
                    "mpe"
                  ]
                }
              ]
            }
          }
        },
        {
          "if": {
            "properties": {
              "mode": {
                "const": "mpe"
              }
            },
            "required": [
              "mode"
            ]
          },
          "then": {
            "required": [
              "mpe"
            ],
            "not": {
              "required": [
                "channel"
              ]
            }
          }
        }
      ]
    },
    "controlChangeEvent": {
      "type": "object",
      "description": "MIDI 1.0 Control Change. Controllers 120..127 use channelMode instead.",
      "properties": {
        "id": {
          "$ref": "#/$defs/id"
        },
        "start": {
          "$ref": "#/$defs/signed"
        },
        "order": {
          "$ref": "#/$defs/signed",
          "default": 1,
          "description": "Same-tick ordering key. Omitted means 1. Note Off has implicit order 0 and Note On implicit order 2; ties are resolved by the normative ordering rules."
        },
        "channel": {
          "$ref": "#/$defs/midiChannel"
        },
        "type": {
          "const": "controlChange"
        },
        "targetNoteId": {
          "$ref": "#/$defs/id",
          "description": "Optional semantic association with an existing concrete note. It does not replace channel/pitch wire semantics."
        },
        "controller": {
          "type": "integer",
          "minimum": 0,
          "maximum": 119
        },
        "value": {
          "type": "integer",
          "minimum": 0,
          "maximum": 127
        }
      },
      "required": [
        "id",
        "start",
        "type",
        "controller",
        "value"
      ],
      "additionalProperties": false
    },
    "channelModeEvent": {
      "type": "object",
      "description": "MIDI 1.0 Channel Mode message represented separately from ordinary Control Change.",
      "properties": {
        "id": {
          "$ref": "#/$defs/id"
        },
        "start": {
          "$ref": "#/$defs/signed"
        },
        "order": {
          "$ref": "#/$defs/signed",
          "default": 1,
          "description": "Same-tick ordering key. Omitted means 1. Note Off has implicit order 0 and Note On implicit order 2; ties are resolved by the normative ordering rules."
        },
        "channel": {
          "$ref": "#/$defs/midiChannel"
        },
        "type": {
          "const": "channelMode"
        },
        "controller": {
          "type": "integer",
          "minimum": 120,
          "maximum": 127
        },
        "value": {
          "type": "integer",
          "minimum": 0,
          "maximum": 127
        }
      },
      "required": [
        "id",
        "start",
        "type",
        "controller",
        "value"
      ],
      "additionalProperties": false
    },
    "programChangeEvent": {
      "type": "object",
      "description": "MIDI 1.0 Program Change using the wire data value 0..127. UI may display 1..128.",
      "properties": {
        "id": {
          "$ref": "#/$defs/id"
        },
        "start": {
          "$ref": "#/$defs/signed"
        },
        "order": {
          "$ref": "#/$defs/signed",
          "default": 1,
          "description": "Same-tick ordering key. Omitted means 1. Note Off has implicit order 0 and Note On implicit order 2; ties are resolved by the normative ordering rules."
        },
        "channel": {
          "$ref": "#/$defs/midiChannel"
        },
        "type": {
          "const": "programChange"
        },
        "program": {
          "type": "integer",
          "minimum": 0,
          "maximum": 127
        }
      },
      "required": [
        "id",
        "start",
        "type",
        "program"
      ],
      "additionalProperties": false
    },
    "pitchBendEvent": {
      "type": "object",
      "description": "MIDI 1.0 14-bit Pitch Bend Change. Bend range is receiver state/RPN data, not encoded in value14.",
      "properties": {
        "id": {
          "$ref": "#/$defs/id"
        },
        "start": {
          "$ref": "#/$defs/signed"
        },
        "order": {
          "$ref": "#/$defs/signed",
          "default": 1,
          "description": "Same-tick ordering key. Omitted means 1. Note Off has implicit order 0 and Note On implicit order 2; ties are resolved by the normative ordering rules."
        },
        "channel": {
          "$ref": "#/$defs/midiChannel"
        },
        "type": {
          "const": "pitchBend"
        },
        "targetNoteId": {
          "$ref": "#/$defs/id",
          "description": "Optional semantic association with an existing concrete note. It does not replace channel/pitch wire semantics."
        },
        "value14": {
          "type": "integer",
          "minimum": 0,
          "maximum": 16383,
          "description": "Raw MIDI 1.0 14-bit pitch-bend value; center is 8192."
        }
      },
      "required": [
        "id",
        "start",
        "type",
        "value14"
      ],
      "additionalProperties": false
    },
    "channelPressureEvent": {
      "type": "object",
      "description": "MIDI 1.0 Channel Pressure (channel aftertouch).",
      "properties": {
        "id": {
          "$ref": "#/$defs/id"
        },
        "start": {
          "$ref": "#/$defs/signed"
        },
        "order": {
          "$ref": "#/$defs/signed",
          "default": 1,
          "description": "Same-tick ordering key. Omitted means 1. Note Off has implicit order 0 and Note On implicit order 2; ties are resolved by the normative ordering rules."
        },
        "channel": {
          "$ref": "#/$defs/midiChannel"
        },
        "type": {
          "const": "channelPressure"
        },
        "targetNoteId": {
          "$ref": "#/$defs/id",
          "description": "Optional semantic association with an existing concrete note. It does not replace channel/pitch wire semantics."
        },
        "value": {
          "type": "integer",
          "minimum": 0,
          "maximum": 127
        }
      },
      "required": [
        "id",
        "start",
        "type",
        "value"
      ],
      "additionalProperties": false
    },
    "polyPressureEvent": {
      "type": "object",
      "description": "MIDI 1.0 Polyphonic Key Pressure (poly aftertouch).",
      "properties": {
        "id": {
          "$ref": "#/$defs/id"
        },
        "start": {
          "$ref": "#/$defs/signed"
        },
        "order": {
          "$ref": "#/$defs/signed",
          "default": 1,
          "description": "Same-tick ordering key. Omitted means 1. Note Off has implicit order 0 and Note On implicit order 2; ties are resolved by the normative ordering rules."
        },
        "channel": {
          "$ref": "#/$defs/midiChannel"
        },
        "type": {
          "const": "polyPressure"
        },
        "targetNoteId": {
          "$ref": "#/$defs/id",
          "description": "Optional semantic association with an existing concrete note. It does not replace channel/pitch wire semantics."
        },
        "pitch": {
          "$ref": "#/$defs/pitch"
        },
        "value": {
          "type": "integer",
          "minimum": 0,
          "maximum": 127
        }
      },
      "required": [
        "id",
        "start",
        "type",
        "pitch",
        "value"
      ],
      "additionalProperties": false
    },
    "midiEvent": {
      "oneOf": [
        {
          "$ref": "#/$defs/controlChangeEvent"
        },
        {
          "$ref": "#/$defs/channelModeEvent"
        },
        {
          "$ref": "#/$defs/programChangeEvent"
        },
        {
          "$ref": "#/$defs/pitchBendEvent"
        },
        {
          "$ref": "#/$defs/channelPressureEvent"
        },
        {
          "$ref": "#/$defs/polyPressureEvent"
        }
      ]
    },
    "lyricVoice": {
      "type": "object",
      "description": "Explicit relationship between a vocal/melody track and a lyric document. Several voices may reference the same lyric document without duplicating text.",
      "properties": {
        "id": {
          "$ref": "#/$defs/id"
        },
        "name": {
          "type": "string"
        },
        "role": {
          "type": "string",
          "minLength": 1,
          "description": "Open authored role. Recommended values include lead, harmony, backing, unison, double, counter, adlib, response."
        },
        "trackId": {
          "$ref": "#/$defs/id"
        },
        "documentId": {
          "$ref": "#/$defs/id"
        },
        "vocalProfile": {
          "$ref": "#/$defs/vocalProfile",
          "description": "Optional engine-neutral vocal defaults; absence does not mean an instrument voice."
        }
      },
      "required": [
        "id",
        "trackId",
        "documentId"
      ],
      "additionalProperties": false
    },
    "playablePitchRange": {
      "type": "object",
      "properties": {
        "lowPitch": {
          "$ref": "#/$defs/pitch"
        },
        "highPitch": {
          "$ref": "#/$defs/pitch"
        }
      },
      "required": [
        "lowPitch",
        "highPitch"
      ],
      "additionalProperties": false,
      "description": "Authored playable pitch capability in the same 0..127 pitch-number domain as melodic notes. Semantic rule: lowPitch <= highPitch."
    },
    "directionPitchCollection": {
      "type": "object",
      "properties": {
        "tonic": {
          "$ref": "#/$defs/spelledPitchClass"
        },
        "intervals": {
          "type": "array",
          "items": {
            "type": "integer",
            "minimum": 0,
            "maximum": 11
          },
          "minItems": 1,
          "maxItems": 12,
          "uniqueItems": true,
          "contains": {
            "const": 0
          }
        },
        "label": {
          "type": "string"
        }
      },
      "required": [
        "tonic",
        "intervals"
      ],
      "additionalProperties": false,
      "description": "Direction-local pitch-class collection relative to tonic. It is not a harmonic scale-context object and has no independent timeline identity."
    },
    "directionPitchSource": {
      "oneOf": [
        {
          "type": "object",
          "properties": {
            "type": {
              "const": "effectiveKeyScale"
            }
          },
          "required": [
            "type"
          ],
          "additionalProperties": false
        },
        {
          "type": "object",
          "properties": {
            "type": {
              "const": "songScale"
            }
          },
          "required": [
            "type"
          ],
          "additionalProperties": false
        },
        {
          "type": "object",
          "properties": {
            "type": {
              "const": "harmonyScales"
            },
            "scaleIds": {
              "type": "array",
              "items": {
                "$ref": "#/$defs/id"
              },
              "minItems": 1,
              "uniqueItems": true
            }
          },
          "required": [
            "type",
            "scaleIds"
          ],
          "additionalProperties": false
        },
        {
          "type": "object",
          "properties": {
            "type": {
              "const": "explicitScale"
            },
            "scale": {
              "$ref": "#/$defs/directionPitchCollection"
            }
          },
          "required": [
            "type",
            "scale"
          ],
          "additionalProperties": false
        }
      ],
      "description": "Source of pitch vocabulary for an improvisation Direction."
    },
    "improvisationDirectionParameters": {
      "type": "object",
      "properties": {
        "pitchSource": {
          "$ref": "#/$defs/directionPitchSource"
        },
        "adherence": {
          "enum": [
            "strict",
            "preferred"
          ]
        }
      },
      "required": [
        "pitchSource",
        "adherence"
      ],
      "additionalProperties": false
    },
    "playingRoleDirectionParameters": {
      "type": "object",
      "properties": {
        "role": {
          "type": "string",
          "minLength": 1
        }
      },
      "required": [
        "role"
      ],
      "additionalProperties": false
    },
    "pitchRangeDirectionParameters": {
      "type": "object",
      "properties": {
        "lowPitch": {
          "$ref": "#/$defs/pitch"
        },
        "highPitch": {
          "$ref": "#/$defs/pitch"
        },
        "constraint": {
          "enum": [
            "strict",
            "preferred"
          ]
        }
      },
      "required": [
        "lowPitch",
        "highPitch",
        "constraint"
      ],
      "additionalProperties": false
    },
    "vendorDirectionParameters": {
      "type": "object",
      "properties": {
        "namespace": {
          "type": "string",
          "minLength": 3,
          "pattern": "^[a-z][a-z0-9-]*(?:\\.[a-z][a-z0-9-]*){2,}$",
          "not": {
            "pattern": "^org\\.ostf(?:\\.|$)"
          }
        },
        "name": {
          "type": "string",
          "minLength": 1
        },
        "version": {
          "type": "string",
          "minLength": 1
        },
        "data": {
          "type": "object"
        }
      },
      "required": [
        "namespace",
        "name",
        "data"
      ],
      "additionalProperties": false
    },
    "improvisationDirection": {
      "type": "object",
      "properties": {
        "id": {
          "$ref": "#/$defs/id"
        },
        "start": {
          "$ref": "#/$defs/nonnegative"
        },
        "duration": {
          "$ref": "#/$defs/positive"
        },
        "label": {
          "type": "string"
        },
        "instruction": {
          "type": "string",
          "description": "Supplemental human/AI-readable semantic instruction. Structured Core parameters remain authoritative."
        },
        "type": {
          "const": "improvisation"
        },
        "parameters": {
          "$ref": "#/$defs/improvisationDirectionParameters"
        }
      },
      "required": [
        "id",
        "start",
        "duration",
        "type",
        "parameters"
      ],
      "additionalProperties": false
    },
    "playingRoleDirection": {
      "type": "object",
      "properties": {
        "id": {
          "$ref": "#/$defs/id"
        },
        "start": {
          "$ref": "#/$defs/nonnegative"
        },
        "duration": {
          "$ref": "#/$defs/positive"
        },
        "label": {
          "type": "string"
        },
        "instruction": {
          "type": "string",
          "description": "Supplemental human/AI-readable semantic instruction. Structured Core parameters remain authoritative."
        },
        "type": {
          "const": "playingRole"
        },
        "parameters": {
          "$ref": "#/$defs/playingRoleDirectionParameters"
        }
      },
      "required": [
        "id",
        "start",
        "duration",
        "type",
        "parameters"
      ],
      "additionalProperties": false
    },
    "pitchRangeDirection": {
      "type": "object",
      "properties": {
        "id": {
          "$ref": "#/$defs/id"
        },
        "start": {
          "$ref": "#/$defs/nonnegative"
        },
        "duration": {
          "$ref": "#/$defs/positive"
        },
        "label": {
          "type": "string"
        },
        "instruction": {
          "type": "string",
          "description": "Supplemental human/AI-readable semantic instruction. Structured Core parameters remain authoritative."
        },
        "type": {
          "const": "pitchRange"
        },
        "parameters": {
          "$ref": "#/$defs/pitchRangeDirectionParameters"
        }
      },
      "required": [
        "id",
        "start",
        "duration",
        "type",
        "parameters"
      ],
      "additionalProperties": false
    },
    "vendorRangeDirection": {
      "type": "object",
      "properties": {
        "id": {
          "$ref": "#/$defs/id"
        },
        "start": {
          "$ref": "#/$defs/nonnegative"
        },
        "duration": {
          "$ref": "#/$defs/positive"
        },
        "label": {
          "type": "string"
        },
        "instruction": {
          "type": "string",
          "description": "Supplemental human/AI-readable semantic instruction. Structured Core parameters remain authoritative."
        },
        "type": {
          "const": "vendor"
        },
        "parameters": {
          "$ref": "#/$defs/vendorDirectionParameters"
        }
      },
      "required": [
        "id",
        "start",
        "duration",
        "type",
        "parameters"
      ],
      "additionalProperties": false
    },
    "vendorPointDirection": {
      "type": "object",
      "properties": {
        "id": {
          "$ref": "#/$defs/id"
        },
        "at": {
          "$ref": "#/$defs/nonnegative"
        },
        "type": {
          "const": "vendor"
        },
        "parameters": {
          "$ref": "#/$defs/vendorDirectionParameters"
        },
        "label": {
          "type": "string"
        },
        "instruction": {
          "type": "string",
          "description": "Supplemental human/AI-readable semantic instruction. Structured/vendor parameters remain authoritative."
        }
      },
      "required": [
        "id",
        "at",
        "type",
        "parameters"
      ],
      "additionalProperties": false
    },
    "trackDirection": {
      "oneOf": [
        {
          "$ref": "#/$defs/improvisationDirection"
        },
        {
          "$ref": "#/$defs/playingRoleDirection"
        },
        {
          "$ref": "#/$defs/pitchRangeDirection"
        },
        {
          "$ref": "#/$defs/vendorRangeDirection"
        },
        {
          "$ref": "#/$defs/vendorPointDirection"
        },
        {
          "$ref": "#/$defs/phrasingDirection"
        },
        {
          "$ref": "#/$defs/vocalFreedomDirection"
        }
      ],
      "description": "Typed semantic instruction owned by a track and positioned on the OSTF global timebase."
    },
    "vocalPhonetics": {
      "type": "object",
      "description": "Ordered phoneme symbols for a lyric unit, not an absolute pronunciation engine command.",
      "properties": {
        "alphabet": {
          "enum": [
            "ipa",
            "xsampa",
            "arpabet",
            "other"
          ]
        },
        "language": {
          "type": "string",
          "minLength": 1
        },
        "symbols": {
          "type": "array",
          "minItems": 1,
          "items": {
            "type": "string",
            "minLength": 1
          }
        },
        "namespace": {
          "type": "string",
          "minLength": 1
        },
        "preferred": {
          "type": "boolean",
          "description": "Optional preference only within the same (alphabet, language) set for this lyricUnit. At most one preferred variant per key; absent does not imply false or a guaranteed conversion."
        }
      },
      "required": [
        "alphabet",
        "symbols"
      ],
      "additionalProperties": false,
      "allOf": [
        {
          "if": {
            "properties": {
              "alphabet": {
                "const": "other"
              }
            },
            "required": [
              "alphabet"
            ]
          },
          "then": {
            "required": [
              "namespace"
            ]
          }
        }
      ]
    },
    "vocalProfile": {
      "type": "object",
      "description": "Voice default independent of commercial singer preset or license.",
      "properties": {
        "language": {
          "type": "string",
          "minLength": 1
        },
        "deliveryMode": {
          "enum": [
            "sing",
            "rap",
            "speak",
            "hum"
          ]
        },
        "voiceDescription": {
          "type": "string",
          "minLength": 1
        }
      },
      "additionalProperties": false
    },
    "vocalPerformance": {
      "type": "object",
      "description": "Performance belonging to exactly one lyric voice within a containing clip.",
      "properties": {
        "id": {
          "$ref": "#/$defs/id"
        },
        "voiceId": {
          "$ref": "#/$defs/id"
        },
        "phonemeEvents": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/vocalPhonemeEvent"
          }
        },
        "pitchCurves": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/vocalPitchCurve"
          }
        },
        "expressionCurves": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/vocalExpressionCurve"
          }
        },
        "techniques": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/vocalTechnique"
          }
        },
        "breathEvents": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/vocalBreathEvent"
          }
        },
        "noteIds": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/id"
          },
          "minItems": 1,
          "uniqueItems": true,
          "description": "Optional exact list of existing note IDs performed by this voice in the containing clip. No duplicate note objects. When present it includes all locally aligned note IDs for that voice. When absent, derive ownership only from voice-specific alignments. Never infer from song.melodyTrackIds."
        }
      },
      "required": [
        "id",
        "voiceId"
      ],
      "additionalProperties": false
    },
    "vocalPhonemeEvent": {
      "type": "object",
      "description": "Explicit phoneme timing, expressed in clip-relative ppq ticks, negative allowed with nonnegative absolute song time.",
      "properties": {
        "id": {
          "$ref": "#/$defs/id"
        },
        "unitId": {
          "$ref": "#/$defs/id"
        },
        "noteId": {
          "$ref": "#/$defs/id"
        },
        "alphabet": {
          "enum": [
            "ipa",
            "xsampa",
            "arpabet",
            "other"
          ]
        },
        "namespace": {
          "type": "string",
          "minLength": 1
        },
        "symbol": {
          "type": "string",
          "minLength": 1
        },
        "start": {
          "$ref": "#/$defs/signed"
        },
        "duration": {
          "$ref": "#/$defs/positive"
        },
        "order": {
          "type": "integer",
          "description": "Optional deterministic ordering when multiple phonemeEvents for one voice share the same start tick; distinct within a (voiceId, start) tie group. Not an audio rendering priority."
        }
      },
      "required": [
        "id",
        "unitId",
        "alphabet",
        "symbol",
        "start",
        "duration"
      ],
      "additionalProperties": false,
      "allOf": [
        {
          "if": {
            "properties": {
              "alphabet": {
                "const": "other"
              }
            },
            "required": [
              "alphabet"
            ]
          },
          "then": {
            "required": [
              "namespace"
            ]
          }
        }
      ]
    },
    "vocalCurvePointPitch": {
      "type": "object",
      "properties": {
        "at": {
          "$ref": "#/$defs/signed"
        },
        "value": {
          "type": "number",
          "description": "Semitone offset from the targeted MIDI note, in cents (signed)."
        }
      },
      "required": [
        "at",
        "value"
      ],
      "additionalProperties": false
    },
    "vocalCurvePointNormalized": {
      "type": "object",
      "properties": {
        "at": {
          "$ref": "#/$defs/signed"
        },
        "value": {
          "type": "number",
          "minimum": 0,
          "maximum": 1
        }
      },
      "required": [
        "at",
        "value"
      ],
      "additionalProperties": false
    },
    "vocalPitchCurve": {
      "type": "object",
      "description": "Specific vocal pitch offset for a single concrete Note, in cents; sample points use clip-relative ppq ticks.",
      "properties": {
        "id": {
          "$ref": "#/$defs/id"
        },
        "targetNoteId": {
          "$ref": "#/$defs/id"
        },
        "unit": {
          "const": "cents"
        },
        "interpolation": {
          "enum": [
            "step",
            "linear"
          ]
        },
        "points": {
          "type": "array",
          "minItems": 1,
          "items": {
            "$ref": "#/$defs/vocalCurvePointPitch"
          }
        }
      },
      "required": [
        "id",
        "targetNoteId",
        "unit",
        "interpolation",
        "points"
      ],
      "additionalProperties": false
    },
    "vocalExpressionCurve": {
      "type": "object",
      "description": "Portable vocal parameters, each normalized 0..1, with no promise of perceptually identical output across engines.",
      "properties": {
        "id": {
          "$ref": "#/$defs/id"
        },
        "parameter": {
          "enum": [
            "dynamics",
            "breathiness",
            "tension",
            "brightness",
            "voicing"
          ]
        },
        "interpolation": {
          "enum": [
            "step",
            "linear"
          ]
        },
        "points": {
          "type": "array",
          "minItems": 1,
          "items": {
            "$ref": "#/$defs/vocalCurvePointNormalized"
          }
        },
        "targetNoteId": {
          "$ref": "#/$defs/id",
          "description": "Optional note-specific replacement of a clip-scoped curve of the same parameter while the note is active. Points still use clip-relative ticks. Do not sum both curves."
        }
      },
      "required": [
        "id",
        "parameter",
        "interpolation",
        "points"
      ],
      "additionalProperties": false
    },
    "vocalTechnique": {
      "type": "object",
      "description": "Semantic artistic intention, not deterministic rendering or an extra pitch source.",
      "properties": {
        "id": {
          "$ref": "#/$defs/id"
        },
        "start": {
          "$ref": "#/$defs/signed"
        },
        "duration": {
          "$ref": "#/$defs/positive"
        },
        "kind": {
          "enum": [
            "scoop",
            "fall",
            "vibrato",
            "portamento",
            "legato",
            "staccato",
            "accent",
            "whisper",
            "growl",
            "falsetto",
            "humming",
            "rap",
            "melisma"
          ]
        },
        "intensity": {
          "type": "number",
          "minimum": 0,
          "maximum": 1
        },
        "targetNoteId": {
          "$ref": "#/$defs/id"
        }
      },
      "required": [
        "id",
        "start",
        "duration",
        "kind"
      ],
      "additionalProperties": false
    },
    "vocalBreathEvent": {
      "type": "object",
      "description": "Optional breath marker. The renderer decides whether to synthesize audible breath.",
      "properties": {
        "id": {
          "$ref": "#/$defs/id"
        },
        "start": {
          "$ref": "#/$defs/signed"
        },
        "duration": {
          "$ref": "#/$defs/positive"
        },
        "kind": {
          "enum": [
            "inhale",
            "exhale"
          ]
        },
        "intensity": {
          "type": "number",
          "minimum": 0,
          "maximum": 1
        }
      },
      "required": [
        "id",
        "start",
        "duration",
        "kind"
      ],
      "additionalProperties": false
    },
    "positiveIntRange": {
      "type": "object",
      "properties": {
        "min": {
          "$ref": "#/$defs/positive"
        },
        "max": {
          "$ref": "#/$defs/positive"
        }
      },
      "required": [
        "min",
        "max"
      ],
      "additionalProperties": false,
      "description": "Inclusive tick bounds; semantic check min <= max."
    },
    "nonnegativeNumberRange": {
      "type": "object",
      "properties": {
        "min": {
          "type": "number",
          "minimum": 0,
          "maximum": 128
        },
        "max": {
          "type": "number",
          "minimum": 0,
          "maximum": 128
        }
      },
      "required": [
        "min",
        "max"
      ],
      "additionalProperties": false,
      "description": "Inclusive range; semantic check min <= max. Count distinct note-on groups at equal onset ticks as one onset."
    },
    "phrasingDirectionParameters": {
      "type": "object",
      "properties": {
        "phraseLengthTicks": {
          "$ref": "#/$defs/positiveIntRange"
        },
        "onsetGroupsPerQuarter": {
          "$ref": "#/$defs/nonnegativeNumberRange"
        },
        "development": {
          "enum": [
            "repetition",
            "motivicVariation",
            "sequence",
            "contrast",
            "free"
          ]
        },
        "contour": {
          "enum": [
            "ascending",
            "descending",
            "arch",
            "valley",
            "stable",
            "free"
          ]
        },
        "energyShape": {
          "enum": [
            "rising",
            "falling",
            "arch",
            "valley",
            "stable",
            "free"
          ],
          "description": "Abstract musical-energy direction; not equivalent to output velocity or volume."
        },
        "motifRef": {
          "$ref": "#/$defs/id"
        },
        "adherence": {
          "enum": [
            "strict",
            "preferred"
          ]
        }
      },
      "required": [
        "adherence"
      ],
      "additionalProperties": false,
      "description": "At least one musical property beyond adherence must be authored; motifRef resolves to phraseLibrary.templates[].id.",
      "minProperties": 2
    },
    "phrasingDirection": {
      "type": "object",
      "properties": {
        "id": {
          "$ref": "#/$defs/id"
        },
        "type": {
          "const": "phrasing"
        },
        "start": {
          "$ref": "#/$defs/nonnegative"
        },
        "duration": {
          "$ref": "#/$defs/positive"
        },
        "label": {
          "type": "string"
        },
        "instruction": {
          "type": "string",
          "description": "Non-executable music-text context, subordinate to structured fields."
        },
        "parameters": {
          "$ref": "#/$defs/phrasingDirectionParameters"
        }
      },
      "required": [
        "id",
        "type",
        "start",
        "duration",
        "parameters"
      ],
      "additionalProperties": false,
      "description": "4.3 optional phrasing Track Direction, using global source-timeline ticks."
    },
    "lyricCandidateSet": {
      "type": "object",
      "properties": {
        "phraseIds": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/id"
          },
          "minItems": 1,
          "uniqueItems": true
        }
      },
      "required": [
        "phraseIds"
      ],
      "additionalProperties": false,
      "description": "One ordered candidate sequence of authored Lyric Phrase IDs. No implicit note alignment."
    },
    "vocalFreedomDirectionParameters": {
      "type": "object",
      "properties": {
        "voiceId": {
          "$ref": "#/$defs/id"
        },
        "textPolicy": {
          "enum": [
            "fixed",
            "alternatives",
            "open"
          ]
        },
        "melodyPolicy": {
          "enum": [
            "fixed",
            "ornamentable",
            "open"
          ]
        },
        "vocalizationKind": {
          "enum": [
            "lexical",
            "scat",
            "humming",
            "nonLexical"
          ]
        },
        "candidatePhraseSets": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/lyricCandidateSet"
          },
          "minItems": 2
        },
        "adherence": {
          "enum": [
            "strict",
            "preferred"
          ]
        }
      },
      "required": [
        "voiceId",
        "textPolicy",
        "melodyPolicy",
        "adherence"
      ],
      "additionalProperties": false,
      "description": "Voice-specific freedom policy. Fixed text does not automatically imply fixed melody or vice versa.",
      "if": {
        "properties": {
          "textPolicy": {
            "const": "alternatives"
          }
        },
        "required": [
          "textPolicy"
        ]
      },
      "then": {
        "required": [
          "candidatePhraseSets"
        ]
      },
      "else": {
        "not": {
          "required": [
            "candidatePhraseSets"
          ]
        }
      }
    },
    "vocalFreedomDirection": {
      "type": "object",
      "properties": {
        "id": {
          "$ref": "#/$defs/id"
        },
        "type": {
          "const": "vocalFreedom"
        },
        "start": {
          "$ref": "#/$defs/nonnegative"
        },
        "duration": {
          "$ref": "#/$defs/positive"
        },
        "label": {
          "type": "string"
        },
        "instruction": {
          "type": "string",
          "description": "Non-executable music-text context, subordinate to structured fields."
        },
        "parameters": {
          "$ref": "#/$defs/vocalFreedomDirectionParameters"
        }
      },
      "required": [
        "id",
        "type",
        "start",
        "duration",
        "parameters"
      ],
      "additionalProperties": false,
      "description": "4.3 optional vocalFreedom Track Direction, using global source-timeline ticks."
    },
    "performanceRequirements": {
      "type": "object",
      "properties": {
        "requiredPolyphony": {
          "type": "integer",
          "minimum": 1,
          "maximum": 128
        },
        "requiredPitchRange": {
          "$ref": "#/$defs/playablePitchRange"
        },
        "requiredArticulations": {
          "type": "array",
          "items": {
            "type": "string",
            "minLength": 1
          },
          "minItems": 1,
          "uniqueItems": true
        },
        "peakOnsetGroupsPerQuarter": {
          "type": "number",
          "exclusiveMinimum": 0,
          "maximum": 128
        }
      },
      "required": [],
      "additionalProperties": false,
      "description": "Minimum/peak musical capabilities required to realize this authored part, not an assertion about the performer. No robot mechanics or safety commands.",
      "minProperties": 1
    },
    "performanceScope": {
      "type": "object",
      "properties": {
        "performancePlanId": {
          "$ref": "#/$defs/id"
        },
        "visitId": {
          "$ref": "#/$defs/id"
        }
      },
      "required": [
        "performancePlanId",
        "visitId"
      ],
      "additionalProperties": false,
      "description": "Bind to exactly one finite visit within a specific plan."
    },
    "ensembleInteraction": {
      "type": "object",
      "properties": {
        "id": {
          "$ref": "#/$defs/id"
        },
        "actorTrackId": {
          "$ref": "#/$defs/id"
        },
        "partnerTrackId": {
          "$ref": "#/$defs/id"
        },
        "actorVoiceId": {
          "$ref": "#/$defs/id"
        },
        "partnerVoiceId": {
          "$ref": "#/$defs/id"
        },
        "relation": {
          "enum": [
            "respondTo",
            "followRhythm",
            "alternateWith",
            "leaveSpaceFor",
            "reinforce"
          ]
        },
        "start": {
          "$ref": "#/$defs/nonnegative"
        },
        "duration": {
          "$ref": "#/$defs/positive"
        },
        "scope": {
          "$ref": "#/$defs/performanceScope"
        },
        "responseWindowTicks": {
          "$ref": "#/$defs/positive"
        },
        "adherence": {
          "enum": [
            "strict",
            "preferred"
          ]
        }
      },
      "required": [
        "id",
        "actorTrackId",
        "partnerTrackId",
        "relation",
        "adherence"
      ],
      "additionalProperties": false,
      "description": "Directed actor/partner relationship: different Tracks, or the same Track only with both explicit and different Lyric Voice IDs whose trackId equals the shared Track. Use source tick range, visit scope, or both. No audio, real-time event, or motor control is implied. Same Track without two distinct owned Voices is a semantic error (JSON Schema cannot compare sibling ID values).",
      "anyOf": [
        {
          "required": [
            "start",
            "duration"
          ]
        },
        {
          "required": [
            "scope"
          ]
        }
      ],
      "dependentRequired": {
        "start": [
          "duration"
        ],
        "duration": [
          "start"
        ]
      }
    },
    "visitPart": {
      "type": "object",
      "properties": {
        "trackId": {
          "$ref": "#/$defs/id"
        },
        "role": {
          "type": "string",
          "minLength": 1,
          "description": "Visit-scoped role override of Track default; timed playingRole conflict requires explicitly listed replacement."
        },
        "realization": {
          "enum": [
            "fixed",
            "open",
            "silent"
          ]
        },
        "replacesDirectionIds": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/id"
          },
          "uniqueItems": true,
          "description": "Only explicit source-track playingRole Direction IDs may be replaced by the visit role."
        }
      },
      "required": [
        "trackId",
        "realization"
      ],
      "additionalProperties": false,
      "description": "A part rule within one performance visit, not a mutation of the source Track."
    },
    "performanceVisit": {
      "type": "object",
      "properties": {
        "id": {
          "$ref": "#/$defs/id"
        },
        "ordinal": {
          "$ref": "#/$defs/nonnegative"
        },
        "label": {
          "type": "string"
        },
        "sourceSectionIds": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/id"
          },
          "minItems": 1
        },
        "sourceRange": {
          "$ref": "#/$defs/range"
        },
        "parts": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/visitPart"
          }
        }
      },
      "required": [
        "id",
        "ordinal",
        "parts"
      ],
      "additionalProperties": false,
      "description": "Finite visit; exactly one source selector. Ordinals must be 0..N-1 in unique sequence within one plan.",
      "oneOf": [
        {
          "required": [
            "sourceSectionIds"
          ]
        },
        {
          "required": [
            "sourceRange"
          ]
        }
      ],
      "not": {
        "required": [
          "sourceSectionIds",
          "sourceRange"
        ]
      }
    },
    "performancePlan": {
      "type": "object",
      "properties": {
        "id": {
          "$ref": "#/$defs/id"
        },
        "name": {
          "type": "string"
        },
        "mode": {
          "const": "orderedFinite"
        },
        "defaultRealization": {
          "enum": [
            "fixed",
            "silent",
            "unspecified"
          ],
          "description": "Explicit policy for unlisted tracks per visit; unspecified cannot claim deterministic replay."
        },
        "visits": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/performanceVisit"
          },
          "minItems": 1
        }
      },
      "required": [
        "id",
        "mode",
        "defaultRealization",
        "visits"
      ],
      "additionalProperties": false,
      "description": "Opt-in finite expanded playthrough. Source Section/Tick remains authoritative. No implicit cues, indefinite loops, or network session state."
    }
  }
}
```

<a id="def-id"></a>
## id

No direct `properties` table (object may be an enum, scalar, array or a composition).

### Exact JSON Schema object

```json
{
  "type": "string",
  "pattern": "^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$",
  "not": {
    "pattern": "[\\r\\n\\u2028\\u2029]"
  }
}
```

<a id="def-nonnegative"></a>
## nonnegative

No direct `properties` table (object may be an enum, scalar, array or a composition).

### Exact JSON Schema object

```json
{
  "type": "integer",
  "minimum": 0,
  "maximum": 9007199254740991
}
```

<a id="def-positive"></a>
## positive

No direct `properties` table (object may be an enum, scalar, array or a composition).

### Exact JSON Schema object

```json
{
  "type": "integer",
  "minimum": 1,
  "maximum": 9007199254740991
}
```

<a id="def-signed"></a>
## signed

No direct `properties` table (object may be an enum, scalar, array or a composition).

### Exact JSON Schema object

```json
{
  "type": "integer",
  "minimum": -9007199254740991,
  "maximum": 9007199254740991
}
```

<a id="def-pitch"></a>
## pitch

No direct `properties` table (object may be an enum, scalar, array or a composition).

### Exact JSON Schema object

```json
{
  "type": "integer",
  "minimum": 0,
  "maximum": 127
}
```

<a id="def-ref"></a>
## ref

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `type` | `enum ["section", "track", "clip", "note", "chord", "scale", "soundSlot", "drumKit", "lyricDocument", "lyricPhrase", "lyricUnit", "lyricAlignment", "resource", "genre", "contributor", "credit", "alternateTitle", "mood", "keyChange", "phraseTemplate", "phraseInstance", "clipChoiceGroup", "clipCandidate", "roleDefinition", "generationProcess", "provenanceRecord", "midiBus", "midiEvent", "lyricVoice", "trackDirection", "ensembleInteraction", "performancePlan", "performanceVisit"]` | Yes |  |
| `id` | `#/$defs/id` | Yes |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "type": {
      "enum": [
        "section",
        "track",
        "clip",
        "note",
        "chord",
        "scale",
        "soundSlot",
        "drumKit",
        "lyricDocument",
        "lyricPhrase",
        "lyricUnit",
        "lyricAlignment",
        "resource",
        "genre",
        "contributor",
        "credit",
        "alternateTitle",
        "mood",
        "keyChange",
        "phraseTemplate",
        "phraseInstance",
        "clipChoiceGroup",
        "clipCandidate",
        "roleDefinition",
        "generationProcess",
        "provenanceRecord",
        "midiBus",
        "midiEvent",
        "lyricVoice",
        "trackDirection",
        "ensembleInteraction",
        "performancePlan",
        "performanceVisit"
      ]
    },
    "id": {
      "$ref": "#/$defs/id"
    }
  },
  "required": [
    "type",
    "id"
  ],
  "additionalProperties": false
}
```

<a id="def-range"></a>
## range

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `start` | `#/$defs/nonnegative` | Yes |  |
| `duration` | `#/$defs/positive` | Yes |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "start": {
      "$ref": "#/$defs/nonnegative"
    },
    "duration": {
      "$ref": "#/$defs/positive"
    }
  },
  "required": [
    "start",
    "duration"
  ],
  "additionalProperties": false
}
```

<a id="def-spelledpitchclass"></a>
## spelledPitchClass

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `step` | `enum ["A", "B", "C", "D", "E", "F", "G"]` | Yes |  |
| `alter` | `integer` | Yes |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "step": {
      "enum": [
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G"
      ]
    },
    "alter": {
      "type": "integer",
      "minimum": -2,
      "maximum": 2
    }
  },
  "required": [
    "step",
    "alter"
  ],
  "additionalProperties": false
}
```

<a id="def-song"></a>
## song

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `title` | `string` | Yes |  |
| `primaryMelodyTrackId` | `#/$defs/id` | No/conditional |  |
| `localizedTitles` | `#/$defs/localizedNames` | No/conditional | Optional localized song-title alternatives. song.title is the stable fallback. |
| `subtitle` | `string` | No/conditional | Optional original-language subtitle. |
| `description` | `string` | No/conditional | Optional original-language description, including Unicode and line breaks. |
| `alternateTitles` | `array<#/$defs/alternateTitle>` | No/conditional | Additional stable-ID source-language titles. |
| `credits` | `array<#/$defs/credit>` | No/conditional | Ordered credit assignments to contributors. Multiple roles and duplicate contributors permitted. |
| `genres` | `array<#/$defs/genre>` | No/conditional | Optional open-ended ordered genre tags; zero or more allowed. Order is authored display preference, first item is primary if a primary label i... |
| `key` | `#/$defs/key` | No/conditional |  |
| `scale` | `#/$defs/scaleDefinition` | No/conditional |  |
| `languages` | `array<string>` | No/conditional |  |
| `primaryLyricDocumentId` | `#/$defs/id` | No/conditional |  |
| `moods` | `array<#/$defs/mood>` | No/conditional |  |
| `rights` | `#/$defs/rightsStatement` | No/conditional |  |
| `melodyTrackIds` | `array<#/$defs/id>` | No/conditional | Optional ordered set of tracks explicitly authored as melody-bearing tracks. If present with primaryMelodyTrackId, the primary track must be a... |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "title": {
      "type": "string"
    },
    "primaryMelodyTrackId": {
      "$ref": "#/$defs/id"
    },
    "localizedTitles": {
      "$ref": "#/$defs/localizedNames",
      "description": "Optional localized song-title alternatives. song.title is the stable fallback."
    },
    "subtitle": {
      "type": "string",
      "description": "Optional original-language subtitle."
    },
    "description": {
      "type": "string",
      "description": "Optional original-language description, including Unicode and line breaks."
    },
    "alternateTitles": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/alternateTitle"
      },
      "description": "Additional stable-ID source-language titles."
    },
    "credits": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/credit"
      },
      "description": "Ordered credit assignments to contributors. Multiple roles and duplicate contributors permitted."
    },
    "genres": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/genre"
      },
      "description": "Optional open-ended ordered genre tags; zero or more allowed. Order is authored display preference, first item is primary if a primary label is desired, not a generator weight. Absent means unspecified."
    },
    "key": {
      "$ref": "#/$defs/key"
    },
    "scale": {
      "$ref": "#/$defs/scaleDefinition"
    },
    "languages": {
      "type": "array",
      "items": {
        "type": "string",
        "minLength": 1,
        "description": "Authored language tag, preferably BCP 47. Unknown spelling is retained; case-insensitive duplicate tags forbidden."
      },
      "uniqueItems": true
    },
    "primaryLyricDocumentId": {
      "$ref": "#/$defs/id"
    },
    "moods": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/mood"
      }
    },
    "rights": {
      "$ref": "#/$defs/rightsStatement"
    },
    "melodyTrackIds": {
      "type": "array",
      "uniqueItems": true,
      "items": {
        "$ref": "#/$defs/id"
      },
      "description": "Optional ordered set of tracks explicitly authored as melody-bearing tracks. If present with primaryMelodyTrackId, the primary track must be a member."
    }
  },
  "required": [
    "title"
  ],
  "additionalProperties": false
}
```

<a id="def-section"></a>
## section

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `id` | `#/$defs/id` | Yes |  |
| `name` | `string` | Yes |  |
| `start` | `#/$defs/nonnegative` | Yes |  |
| `duration` | `#/$defs/positive` | Yes |  |
| `role` | `string` | No/conditional |  |
| `localizedNames` | `#/$defs/localizedNames` | No/conditional | Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity. |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "name": {
      "type": "string",
      "minLength": 1
    },
    "start": {
      "$ref": "#/$defs/nonnegative"
    },
    "duration": {
      "$ref": "#/$defs/positive"
    },
    "role": {
      "type": "string"
    },
    "localizedNames": {
      "$ref": "#/$defs/localizedNames",
      "description": "Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity."
    }
  },
  "required": [
    "id",
    "name",
    "start",
    "duration"
  ],
  "additionalProperties": false
}
```

<a id="def-tempo"></a>
## tempo

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `at` | `#/$defs/nonnegative` | Yes |  |
| `bpm` | `number` | Yes |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "at": {
      "$ref": "#/$defs/nonnegative"
    },
    "bpm": {
      "type": "number",
      "exclusiveMinimum": 0,
      "maximum": 1000
    }
  },
  "required": [
    "at",
    "bpm"
  ],
  "additionalProperties": false
}
```

<a id="def-meter"></a>
## meter

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `at` | `#/$defs/nonnegative` | Yes |  |
| `numerator` | `integer` | Yes |  |
| `denominator` | `enum [1, 2, 4, 8, 16, 32, 64]` | Yes |  |
| `beatGroups` | `array<integer>` | No/conditional | Optional additive grouping in denominator units. Values must sum to numerator. Descriptive only; does not change note timestamps. |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "at": {
      "$ref": "#/$defs/nonnegative"
    },
    "numerator": {
      "type": "integer",
      "minimum": 1,
      "maximum": 64
    },
    "denominator": {
      "enum": [
        1,
        2,
        4,
        8,
        16,
        32,
        64
      ],
      "type": "integer"
    },
    "beatGroups": {
      "type": "array",
      "items": {
        "type": "integer",
        "minimum": 1,
        "maximum": 64
      },
      "minItems": 1,
      "maxItems": 64,
      "description": "Optional additive grouping in denominator units. Values must sum to numerator. Descriptive only; does not change note timestamps."
    }
  },
  "required": [
    "at",
    "numerator",
    "denominator"
  ],
  "additionalProperties": false
}
```

<a id="def-timeline"></a>
## timeline

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `sections` | `array<#/$defs/section>` | Yes |  |
| `tempoChanges` | `array<#/$defs/tempo>` | Yes |  |
| `meterChanges` | `array<#/$defs/meter>` | Yes |  |
| `keyChanges` | `array<#/$defs/keyChange>` | No/conditional |  |
| `duration` | `#/$defs/nonnegative` | No/conditional |  |
| `barOrigin` | `#/$defs/nonnegative` | No/conditional |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "sections": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/section"
      }
    },
    "tempoChanges": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/tempo"
      },
      "minItems": 1
    },
    "meterChanges": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/meter"
      },
      "minItems": 1
    },
    "keyChanges": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/keyChange"
      }
    },
    "duration": {
      "$ref": "#/$defs/nonnegative"
    },
    "barOrigin": {
      "$ref": "#/$defs/nonnegative"
    }
  },
  "required": [
    "sections",
    "tempoChanges",
    "meterChanges"
  ],
  "additionalProperties": false
}
```

<a id="def-chord"></a>
## chord

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `id` | `#/$defs/id` | Yes |  |
| `start` | `#/$defs/nonnegative` | Yes |  |
| `duration` | `#/$defs/positive` | Yes |  |
| `label` | `string` | Yes |  |
| `root` | `#/$defs/spelledPitchClass` | No/conditional |  |
| `intervals` | `array<integer>` | No/conditional |  |
| `bass` | `#/$defs/spelledPitchClass` | No/conditional |  |
| `voicing` | `#/$defs/voicing` | No/conditional | Optional pitch snapshot (not an arrangement note sequence). No automatic playback. |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "start": {
      "$ref": "#/$defs/nonnegative"
    },
    "duration": {
      "$ref": "#/$defs/positive"
    },
    "label": {
      "type": "string",
      "minLength": 1
    },
    "root": {
      "$ref": "#/$defs/spelledPitchClass"
    },
    "intervals": {
      "type": "array",
      "items": {
        "type": "integer",
        "minimum": 0,
        "maximum": 35
      },
      "minItems": 1,
      "maxItems": 36,
      "uniqueItems": true,
      "contains": {
        "const": 0
      }
    },
    "bass": {
      "$ref": "#/$defs/spelledPitchClass"
    },
    "voicing": {
      "$ref": "#/$defs/voicing",
      "description": "Optional pitch snapshot (not an arrangement note sequence). No automatic playback."
    }
  },
  "required": [
    "id",
    "start",
    "duration",
    "label"
  ],
  "additionalProperties": false,
  "dependentRequired": {
    "root": [
      "intervals"
    ],
    "intervals": [
      "root"
    ]
  }
}
```

<a id="def-scale"></a>
## scale

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `id` | `#/$defs/id` | Yes |  |
| `start` | `#/$defs/nonnegative` | Yes |  |
| `duration` | `#/$defs/positive` | Yes |  |
| `label` | `string` | No/conditional |  |
| `tonic` | `#/$defs/spelledPitchClass` | Yes |  |
| `intervals` | `array<integer>` | Yes |  |
| `targets` | `array<#/$defs/scaleTarget>` | No/conditional | Optional explicit scope. Absence means general timed context, not a global key. Overlapping contexts are not resolved by array order. |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "start": {
      "$ref": "#/$defs/nonnegative"
    },
    "duration": {
      "$ref": "#/$defs/positive"
    },
    "label": {
      "type": "string"
    },
    "tonic": {
      "$ref": "#/$defs/spelledPitchClass"
    },
    "intervals": {
      "type": "array",
      "items": {
        "type": "integer",
        "minimum": 0,
        "maximum": 11
      },
      "minItems": 1,
      "maxItems": 12,
      "uniqueItems": true,
      "contains": {
        "const": 0
      }
    },
    "targets": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/scaleTarget"
      },
      "minItems": 1,
      "uniqueItems": true,
      "description": "Optional explicit scope. Absence means general timed context, not a global key. Overlapping contexts are not resolved by array order."
    }
  },
  "required": [
    "id",
    "start",
    "duration",
    "tonic",
    "intervals"
  ],
  "additionalProperties": false
}
```

<a id="def-harmony"></a>
## harmony

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `chords` | `array<#/$defs/chord>` | Yes |  |
| `scales` | `array<#/$defs/scale>` | Yes |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "chords": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/chord"
      }
    },
    "scales": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/scale"
      }
    }
  },
  "required": [
    "chords",
    "scales"
  ],
  "additionalProperties": false
}
```

<a id="def-instrument"></a>
## instrument

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `name` | `string` | Yes |  |
| `family` | `string` | No/conditional |  |
| `localizedNames` | `#/$defs/localizedNames` | No/conditional | Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity. |
| `playablePitchRange` | `#/$defs/playablePitchRange` | No/conditional |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "name": {
      "type": "string"
    },
    "family": {
      "type": "string"
    },
    "localizedNames": {
      "$ref": "#/$defs/localizedNames",
      "description": "Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity."
    },
    "playablePitchRange": {
      "$ref": "#/$defs/playablePitchRange"
    }
  },
  "required": [
    "name"
  ],
  "additionalProperties": false
}
```

<a id="def-note"></a>
## note

Concrete Core DAW-note event. The event target is pitch or soundSlotId. Optional 3.5 note-local properties preserve mute, release velocity, probability and velocity variation. pitchRole=fixedTrigger marks a literal MIDI key trigger that must not be musically transposed or analyzed.

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `id` | `#/$defs/id` | Yes |  |
| `start` | `#/$defs/signed` | Yes |  |
| `duration` | `#/$defs/positive` | Yes | Positive note gate in ticks, not the guaranteed audible duration of a one-shot percussion sample. |
| `pitch` | `#/$defs/pitch` | No/conditional |  |
| `soundSlotId` | `#/$defs/id` | No/conditional | Document-local Sound Slot ID. Distinct events and IDs stay distinct even if several slots share a MIDI key; a renderer decides the acoustic ti... |
| `velocity` | `integer` | No/conditional | Optional authored note-on velocity for performed Core notes, 1–127; omit to mean unspecified. It is not a note-off velocity, controller stream... |
| `enabled` | `boolean` | No/conditional | Optional note-local enable state. Omitted means enabled. False preserves the note but suppresses scheduling/playback; it is distinct from prob... |
| `releaseVelocity` | `integer` | No/conditional | Optional MIDI Note Off/release velocity, 0-127. Omit when unspecified; readers must not invent and write back a default. |
| `probability` | `number` | No/conditional | Optional note-playback probability from 0.0 to 1.0. Omitted means 1.0. Random sequence identity is not standardized; materialize notes for det... |
| `velocityDeviation` | `integer` | No/conditional | Optional note-local velocity variation endpoint relative to velocity. Requires velocity. Semantic rule: velocity + velocityDeviation must rema... |
| `pitchRole` | `enum ["musical", "fixedTrigger"]` | No/conditional | Meaning of a pitch note. musical participates in pitch/harmony/transpose operations; fixedTrigger is an exact MIDI key trigger (for example a ... |
| `channel` | `#/$defs/midiChannel` | No/conditional | Optional concrete MIDI channel for this performed note. In singleChannel mode it may be omitted and inherited from the track; in multiChannel/... |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "start": {
      "$ref": "#/$defs/signed"
    },
    "duration": {
      "$ref": "#/$defs/positive",
      "description": "Positive note gate in ticks, not the guaranteed audible duration of a one-shot percussion sample."
    },
    "pitch": {
      "$ref": "#/$defs/pitch"
    },
    "soundSlotId": {
      "$ref": "#/$defs/id",
      "description": "Document-local Sound Slot ID. Distinct events and IDs stay distinct even if several slots share a MIDI key; a renderer decides the acoustic timbre."
    },
    "velocity": {
      "type": "integer",
      "minimum": 1,
      "maximum": 127,
      "description": "Optional authored note-on velocity for performed Core notes, 1–127; omit to mean unspecified. It is not a note-off velocity, controller stream, chord tone, or a sound-rendering guarantee. Never insert an inferred default when saving."
    },
    "enabled": {
      "type": "boolean",
      "default": true,
      "description": "Optional note-local enable state. Omitted means enabled. False preserves the note but suppresses scheduling/playback; it is distinct from probability=0."
    },
    "releaseVelocity": {
      "type": "integer",
      "minimum": 0,
      "maximum": 127,
      "description": "Optional MIDI Note Off/release velocity, 0-127. Omit when unspecified; readers must not invent and write back a default."
    },
    "probability": {
      "type": "number",
      "minimum": 0,
      "maximum": 1,
      "default": 1,
      "description": "Optional note-playback probability from 0.0 to 1.0. Omitted means 1.0. Random sequence identity is not standardized; materialize notes for deterministic interchange."
    },
    "velocityDeviation": {
      "type": "integer",
      "minimum": -126,
      "maximum": 126,
      "default": 0,
      "description": "Optional note-local velocity variation endpoint relative to velocity. Requires velocity. Semantic rule: velocity + velocityDeviation must remain within 1..127. Omitted means 0."
    },
    "pitchRole": {
      "enum": [
        "musical",
        "fixedTrigger"
      ],
      "default": "musical",
      "description": "Meaning of a pitch note. musical participates in pitch/harmony/transpose operations; fixedTrigger is an exact MIDI key trigger (for example a keyswitch) and is never transposed or used as musical-pitch evidence. Allowed only on pitch notes."
    },
    "channel": {
      "$ref": "#/$defs/midiChannel",
      "description": "Optional concrete MIDI channel for this performed note. In singleChannel mode it may be omitted and inherited from the track; in multiChannel/MPE mode semantic rules require explicit channel where channel identity matters."
    }
  },
  "required": [
    "id",
    "start",
    "duration"
  ],
  "additionalProperties": false,
  "oneOf": [
    {
      "required": [
        "pitch"
      ],
      "not": {
        "required": [
          "soundSlotId"
        ]
      }
    },
    {
      "required": [
        "soundSlotId"
      ],
      "not": {
        "required": [
          "pitch"
        ]
      }
    }
  ],
  "description": "Concrete Core DAW-note event. The event target is pitch or soundSlotId. Optional 3.5 note-local properties preserve mute, release velocity, probability and velocity variation. pitchRole=fixedTrigger marks a literal MIDI key trigger that must not be musically transposed or analyzed.",
  "dependentRequired": {
    "velocityDeviation": [
      "velocity"
    ]
  },
  "allOf": [
    {
      "if": {
        "required": [
          "soundSlotId"
        ]
      },
      "then": {
        "not": {
          "required": [
            "pitchRole"
          ]
        }
      }
    }
  ]
}
```

<a id="def-clip"></a>
## clip

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `id` | `#/$defs/id` | Yes |  |
| `name` | `string` | No/conditional |  |
| `start` | `#/$defs/nonnegative` | Yes |  |
| `duration` | `#/$defs/positive` | Yes |  |
| `enabled` | `boolean` | No/conditional |  |
| `notes` | `array<#/$defs/note>` | Yes |  |
| `localizedNames` | `#/$defs/localizedNames` | No/conditional | Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity. |
| `midiEvents` | `array<#/$defs/midiEvent>` | No/conditional | Optional clip-local MIDI performance/control events. start is local to the clip and may be negative if absolute time remains nonnegative. Note... |
| `vocalPerformances` | `array<#/$defs/vocalPerformance>` | No/conditional | Optional voice-specific phoneme and singing-performance data; references lyrics.voices. Notes/MIDI remain authoritative for MIDI playback. |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "name": {
      "type": "string"
    },
    "start": {
      "$ref": "#/$defs/nonnegative"
    },
    "duration": {
      "$ref": "#/$defs/positive"
    },
    "enabled": {
      "type": "boolean",
      "default": true
    },
    "notes": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/note"
      }
    },
    "localizedNames": {
      "$ref": "#/$defs/localizedNames",
      "description": "Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity."
    },
    "midiEvents": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/midiEvent"
      },
      "description": "Optional clip-local MIDI performance/control events. start is local to the clip and may be negative if absolute time remains nonnegative. Notes remain authoritative in notes[]."
    },
    "vocalPerformances": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/vocalPerformance"
      },
      "minItems": 1,
      "description": "Optional voice-specific phoneme and singing-performance data; references lyrics.voices. Notes/MIDI remain authoritative for MIDI playback."
    }
  },
  "required": [
    "id",
    "start",
    "duration",
    "notes"
  ],
  "additionalProperties": false
}
```

<a id="def-track"></a>
## track

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `id` | `#/$defs/id` | Yes |  |
| `name` | `string` | Yes |  |
| `role` | `string` | No/conditional |  |
| `instrument` | `#/$defs/instrument` | No/conditional |  |
| `enabled` | `boolean` | No/conditional |  |
| `clips` | `array<#/$defs/clip>` | Yes |  |
| `trackType` | `enum ["melodic", "drum", "mixed"]` | No/conditional | Semantic event-target category; optional; missing/empty-note tracks may be unknown. It is not a DAW track class. |
| `preferredView` | `enum ["auto", "pianoRoll", "drumGrid"]` | No/conditional | Non-binding presentation preference. Does not change note meaning. |
| `soundSource` | `#/$defs/soundSource` | No/conditional | Optional sound-source selection hint, not a plug-in state, preset blob, or sound guarantee. |
| `localizedNames` | `#/$defs/localizedNames` | No/conditional | Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity. |
| `drumKitId` | `#/$defs/id` | No/conditional | Optional reference to a declared drumKit; only for a drum/mixed or empty inferred track. All stored slot events in the track must belong to th... |
| `midi` | `#/$defs/trackMidi` | No/conditional |  |
| `directions` | `array<#/$defs/trackDirection>` | No/conditional | Optional typed semantic instructions for performance, interpretation, or generation. Uses the global OSTF timebase; it is not a second timeline. |
| `performanceRequirements` | `#/$defs/performanceRequirements` | No/conditional | Portable requirements for realizing this track, not a robot/device capability report. |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "name": {
      "type": "string"
    },
    "role": {
      "type": "string"
    },
    "instrument": {
      "$ref": "#/$defs/instrument"
    },
    "enabled": {
      "type": "boolean",
      "default": true
    },
    "clips": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/clip"
      }
    },
    "trackType": {
      "enum": [
        "melodic",
        "drum",
        "mixed"
      ],
      "description": "Semantic event-target category; optional; missing/empty-note tracks may be unknown. It is not a DAW track class."
    },
    "preferredView": {
      "enum": [
        "auto",
        "pianoRoll",
        "drumGrid"
      ],
      "default": "auto",
      "description": "Non-binding presentation preference. Does not change note meaning."
    },
    "soundSource": {
      "$ref": "#/$defs/soundSource",
      "description": "Optional sound-source selection hint, not a plug-in state, preset blob, or sound guarantee."
    },
    "localizedNames": {
      "$ref": "#/$defs/localizedNames",
      "description": "Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity."
    },
    "drumKitId": {
      "$ref": "#/$defs/id",
      "description": "Optional reference to a declared drumKit; only for a drum/mixed or empty inferred track. All stored slot events in the track must belong to the referenced kit."
    },
    "midi": {
      "$ref": "#/$defs/trackMidi"
    },
    "directions": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/trackDirection"
      },
      "description": "Optional typed semantic instructions for performance, interpretation, or generation. Uses the global OSTF timebase; it is not a second timeline."
    },
    "performanceRequirements": {
      "$ref": "#/$defs/performanceRequirements",
      "description": "Portable requirements for realizing this track, not a robot/device capability report."
    }
  },
  "required": [
    "id",
    "name",
    "clips"
  ],
  "additionalProperties": false,
  "allOf": [
    {
      "if": {
        "properties": {
          "trackType": {
            "const": "melodic"
          }
        },
        "required": [
          "trackType"
        ]
      },
      "then": {
        "not": {
          "required": [
            "drumKitId"
          ]
        }
      }
    }
  ]
}
```

<a id="def-soundslot"></a>
## soundSlot

Document-local stable logical percussion target. Equal roles, names or MIDI note mappings never merge distinct slot IDs. No sample/audio identity is encoded.

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `id` | `#/$defs/id` | Yes |  |
| `name` | `string` | Yes |  |
| `role` | `string` | No/conditional | Optional free-text musical role; not a standardized GM instrument code or an acoustic sample identifier. |
| `midiNote` | `#/$defs/pitch` | No/conditional | Legacy 3.0 MIDI note hint only; not a GM1 declaration or preview timbre identity. |
| `midiMapping` | `#/$defs/midiMapping` | No/conditional | Explicit external MIDI1 output mapping; standard=gm1 is separate from custom even for an equal note number. Not a unique slot or audio identity. |
| `localizedNames` | `#/$defs/localizedNames` | No/conditional | Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity. |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "name": {
      "type": "string"
    },
    "role": {
      "type": "string",
      "description": "Optional free-text musical role; not a standardized GM instrument code or an acoustic sample identifier."
    },
    "midiNote": {
      "$ref": "#/$defs/pitch",
      "description": "Legacy 3.0 MIDI note hint only; not a GM1 declaration or preview timbre identity."
    },
    "midiMapping": {
      "$ref": "#/$defs/midiMapping",
      "description": "Explicit external MIDI1 output mapping; standard=gm1 is separate from custom even for an equal note number. Not a unique slot or audio identity."
    },
    "localizedNames": {
      "$ref": "#/$defs/localizedNames",
      "description": "Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity."
    }
  },
  "required": [
    "id",
    "name"
  ],
  "additionalProperties": false,
  "description": "Document-local stable logical percussion target. Equal roles, names or MIDI note mappings never merge distinct slot IDs. No sample/audio identity is encoded."
}
```

<a id="def-lyricdocument"></a>
## lyricDocument

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `id` | `#/$defs/id` | Yes |  |
| `title` | `string` | No/conditional |  |
| `language` | `string` | No/conditional |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "title": {
      "type": "string"
    },
    "language": {
      "type": "string"
    }
  },
  "required": [
    "id"
  ],
  "additionalProperties": false
}
```

<a id="def-lyricphrase"></a>
## lyricPhrase

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `id` | `#/$defs/id` | Yes |  |
| `documentId` | `#/$defs/id` | Yes |  |
| `text` | `string` | Yes |  |
| `pronunciation` | `string` | No/conditional |  |
| `start` | `#/$defs/nonnegative` | No/conditional |  |
| `duration` | `#/$defs/positive` | No/conditional |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "documentId": {
      "$ref": "#/$defs/id"
    },
    "text": {
      "type": "string"
    },
    "pronunciation": {
      "type": "string"
    },
    "start": {
      "$ref": "#/$defs/nonnegative"
    },
    "duration": {
      "$ref": "#/$defs/positive"
    }
  },
  "required": [
    "id",
    "documentId",
    "text"
  ],
  "additionalProperties": false,
  "dependentRequired": {
    "start": [
      "duration"
    ],
    "duration": [
      "start"
    ]
  }
}
```

<a id="def-lyricunit"></a>
## lyricUnit

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `id` | `#/$defs/id` | Yes |  |
| `phraseId` | `#/$defs/id` | Yes |  |
| `text` | `string` | Yes |  |
| `pronunciation` | `string` | No/conditional |  |
| `start` | `#/$defs/nonnegative` | No/conditional |  |
| `duration` | `#/$defs/positive` | No/conditional |  |
| `phonetics` | `array<#/$defs/vocalPhonetics>` | No/conditional | Optional alternate phoneme token sequences. Do not alter text/pronunciation. Multiple alphabets are permitted. |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "phraseId": {
      "$ref": "#/$defs/id"
    },
    "text": {
      "type": "string"
    },
    "pronunciation": {
      "type": "string"
    },
    "start": {
      "$ref": "#/$defs/nonnegative"
    },
    "duration": {
      "$ref": "#/$defs/positive"
    },
    "phonetics": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/vocalPhonetics"
      },
      "minItems": 1,
      "description": "Optional alternate phoneme token sequences. Do not alter text/pronunciation. Multiple alphabets are permitted."
    }
  },
  "required": [
    "id",
    "phraseId",
    "text"
  ],
  "additionalProperties": false,
  "dependentRequired": {
    "start": [
      "duration"
    ],
    "duration": [
      "start"
    ]
  }
}
```

<a id="def-lyricalignment"></a>
## lyricAlignment

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `id` | `#/$defs/id` | Yes |  |
| `unitIds` | `array<#/$defs/id>` | Yes |  |
| `noteIds` | `array<#/$defs/id>` | Yes |  |
| `voiceId` | `#/$defs/id` | No/conditional | Optional lyricVoice association. When present, aligned units must belong to that voice document and aligned notes must belong to that voice tr... |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "unitIds": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/id"
      },
      "uniqueItems": true,
      "minItems": 1
    },
    "noteIds": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/id"
      },
      "uniqueItems": true,
      "minItems": 1
    },
    "voiceId": {
      "$ref": "#/$defs/id",
      "description": "Optional lyricVoice association. When present, aligned units must belong to that voice document and aligned notes must belong to that voice track."
    }
  },
  "required": [
    "id",
    "unitIds",
    "noteIds"
  ],
  "additionalProperties": false
}
```

<a id="def-lyrics"></a>
## lyrics

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `documents` | `array<#/$defs/lyricDocument>` | Yes |  |
| `phrases` | `array<#/$defs/lyricPhrase>` | Yes |  |
| `units` | `array<#/$defs/lyricUnit>` | Yes |  |
| `alignments` | `array<#/$defs/lyricAlignment>` | Yes |  |
| `voices` | `array<#/$defs/lyricVoice>` | No/conditional | Optional explicit vocal-part relationships for multi-voice, harmony and chorus lyrics. |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "documents": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/lyricDocument"
      }
    },
    "phrases": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/lyricPhrase"
      }
    },
    "units": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/lyricUnit"
      }
    },
    "alignments": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/lyricAlignment"
      }
    },
    "voices": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/lyricVoice"
      },
      "description": "Optional explicit vocal-part relationships for multi-voice, harmony and chorus lyrics."
    }
  },
  "required": [
    "documents",
    "phrases",
    "units",
    "alignments"
  ],
  "additionalProperties": false
}
```

<a id="def-sha256"></a>
## sha256

No direct `properties` table (object may be an enum, scalar, array or a composition).

### Exact JSON Schema object

```json
{
  "type": "string",
  "pattern": "^[0-9a-f]{64}$",
  "not": {
    "pattern": "[\\r\\n\\u2028\\u2029]"
  }
}
```

<a id="def-resource"></a>
## resource

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `id` | `#/$defs/id` | Yes |  |
| `kind` | `enum ["audio", "midi", "text", "other"]` | Yes |  |
| `uri` | `string` | Yes |  |
| `name` | `string` | No/conditional |  |
| `sha256` | `#/$defs/sha256` | No/conditional |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "kind": {
      "enum": [
        "audio",
        "midi",
        "text",
        "other"
      ]
    },
    "uri": {
      "type": "string",
      "minLength": 1
    },
    "name": {
      "type": "string"
    },
    "sha256": {
      "$ref": "#/$defs/sha256"
    }
  },
  "required": [
    "id",
    "kind",
    "uri"
  ],
  "additionalProperties": false
}
```

<a id="def-dependencies"></a>
## dependencies

No direct `properties` table (object may be an enum, scalar, array or a composition).

### Exact JSON Schema object

```json
{
  "oneOf": [
    {
      "type": "object",
      "properties": {
        "scope": {
          "enum": [
            "document",
            "none"
          ]
        }
      },
      "required": [
        "scope"
      ],
      "additionalProperties": false
    },
    {
      "type": "object",
      "properties": {
        "scope": {
          "const": "objects"
        },
        "refs": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/ref"
          },
          "minItems": 1,
          "uniqueItems": true
        }
      },
      "required": [
        "scope",
        "refs"
      ],
      "additionalProperties": false
    }
  ]
}
```

<a id="def-relativeassignment"></a>
## relativeAssignment

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `noteId` | `#/$defs/id` | Yes |  |
| `basis` | `enum ["chordTone", "scaleDegree"]` | Yes |  |
| `contextId` | `#/$defs/id` | Yes |  |
| `anchorPitch` | `#/$defs/pitch` | Yes |  |
| `index` | `integer` | Yes |  |
| `chromaticOffset` | `integer` | Yes |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "noteId": {
      "$ref": "#/$defs/id"
    },
    "basis": {
      "enum": [
        "chordTone",
        "scaleDegree"
      ]
    },
    "contextId": {
      "$ref": "#/$defs/id"
    },
    "anchorPitch": {
      "$ref": "#/$defs/pitch"
    },
    "index": {
      "type": "integer",
      "minimum": 1,
      "maximum": 36
    },
    "chromaticOffset": {
      "type": "integer",
      "minimum": -24,
      "maximum": 24
    }
  },
  "required": [
    "noteId",
    "basis",
    "contextId",
    "anchorPitch",
    "index",
    "chromaticOffset"
  ],
  "additionalProperties": false,
  "allOf": [
    {
      "if": {
        "properties": {
          "basis": {
            "const": "scaleDegree"
          }
        },
        "required": [
          "basis"
        ]
      },
      "then": {
        "properties": {
          "index": {
            "maximum": 12
          }
        }
      }
    }
  ]
}
```

<a id="def-generator"></a>
## generator

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes |  |
| `version` | `string` | Yes |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "id": {
      "type": "string",
      "minLength": 1
    },
    "version": {
      "type": "string",
      "minLength": 1
    }
  },
  "required": [
    "id",
    "version"
  ],
  "additionalProperties": false
}
```

<a id="def-generationinput"></a>
## generationInput

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `role` | `string` | Yes |  |
| `ref` | `#/$defs/ref` | Yes |  |
| `readRange` | `#/$defs/range` | No/conditional |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "role": {
      "type": "string",
      "minLength": 1
    },
    "ref": {
      "$ref": "#/$defs/ref"
    },
    "readRange": {
      "$ref": "#/$defs/range"
    }
  },
  "required": [
    "role",
    "ref"
  ],
  "additionalProperties": false
}
```

<a id="def-generationprocess"></a>
## generationProcess

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `id` | `#/$defs/id` | Yes |  |
| `generator` | `#/$defs/generator` | Yes |  |
| `inputs` | `array<#/$defs/generationInput>` | Yes |  |
| `outputs` | `array<#/$defs/ref>` | Yes |  |
| `targetRange` | `#/$defs/range` | No/conditional |  |
| `protectedNoteIds` | `array<#/$defs/id>` | Yes |  |
| `intent` | `#/$defs/generationIntent` | No/conditional |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "generator": {
      "$ref": "#/$defs/generator"
    },
    "inputs": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/generationInput"
      }
    },
    "outputs": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/ref"
      },
      "minItems": 1
    },
    "targetRange": {
      "$ref": "#/$defs/range"
    },
    "protectedNoteIds": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/id"
      },
      "uniqueItems": true
    },
    "intent": {
      "$ref": "#/$defs/generationIntent"
    }
  },
  "required": [
    "id",
    "generator",
    "inputs",
    "outputs",
    "protectedNoteIds"
  ],
  "additionalProperties": false
}
```

<a id="def-color"></a>
## color

No direct `properties` table (object may be an enum, scalar, array or a composition).

### Exact JSON Schema object

```json
{
  "type": "string",
  "pattern": "^#[0-9A-Fa-f]{6}$",
  "not": {
    "pattern": "[\\r\\n\\u2028\\u2029]"
  }
}
```

<a id="def-roledefinition"></a>
## roleDefinition

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `id` | `#/$defs/id` | Yes |  |
| `name` | `string` | Yes |  |
| `baseRole` | `string` | No/conditional |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "name": {
      "type": "string",
      "minLength": 1
    },
    "baseRole": {
      "type": "string"
    }
  },
  "required": [
    "id",
    "name"
  ],
  "additionalProperties": false
}
```

<a id="def-rolecolormap"></a>
## roleColorMap

No direct `properties` table (object may be an enum, scalar, array or a composition).

### Exact JSON Schema object

```json
{
  "type": "object",
  "additionalProperties": {
    "$ref": "#/$defs/color"
  }
}
```

<a id="def-customrolecolormap"></a>
## customRoleColorMap

No direct `properties` table (object may be an enum, scalar, array or a composition).

### Exact JSON Schema object

```json
{
  "type": "object",
  "propertyNames": {
    "$ref": "#/$defs/id"
  },
  "additionalProperties": {
    "$ref": "#/$defs/color"
  }
}
```

<a id="def-objectcolor"></a>
## objectColor

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `target` | `#/$defs/ref` | Yes |  |
| `color` | `#/$defs/color` | Yes |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "target": {
      "$ref": "#/$defs/ref"
    },
    "color": {
      "$ref": "#/$defs/color"
    }
  },
  "required": [
    "target",
    "color"
  ],
  "additionalProperties": false
}
```

<a id="def-phrasetemplate"></a>
## phraseTemplate

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `id` | `#/$defs/id` | Yes |  |
| `duration` | `#/$defs/positive` | Yes |  |
| `notes` | `array<#/$defs/corePhraseSourceNote>` | Yes |  |
| `name` | `string` | No/conditional |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "duration": {
      "$ref": "#/$defs/positive"
    },
    "notes": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/corePhraseSourceNote"
      }
    },
    "name": {
      "type": "string"
    }
  },
  "required": [
    "id",
    "duration",
    "notes"
  ],
  "additionalProperties": false
}
```

<a id="def-phrasenotemapping"></a>
## phraseNoteMapping

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `templateNoteId` | `#/$defs/id` | Yes |  |
| `repeatIndex` | `#/$defs/nonnegative` | Yes |  |
| `noteId` | `#/$defs/id` | Yes |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "templateNoteId": {
      "$ref": "#/$defs/id"
    },
    "repeatIndex": {
      "$ref": "#/$defs/nonnegative"
    },
    "noteId": {
      "$ref": "#/$defs/id"
    }
  },
  "required": [
    "templateNoteId",
    "repeatIndex",
    "noteId"
  ],
  "additionalProperties": false
}
```

<a id="def-phraseinstance"></a>
## phraseInstance

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `id` | `#/$defs/id` | Yes |  |
| `templateId` | `#/$defs/id` | Yes |  |
| `clipId` | `#/$defs/id` | Yes |  |
| `repeatCount` | `#/$defs/positive` | Yes |  |
| `transpose` | `integer` | Yes |  |
| `noteMap` | `array<#/$defs/phraseNoteMapping>` | Yes |  |
| `velocityMode` | `enum ["independent", "linked"]` | No/conditional | independent preserves concrete velocities on refresh; linked requires exact presence/value equality with the template. This field does not tri... |
| `noteStateMode` | `enum ["independent", "linked"]` | No/conditional | Controls enabled/releaseVelocity/probability/velocityDeviation after materialization. independent preserves concrete note-state values on refr... |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "templateId": {
      "$ref": "#/$defs/id"
    },
    "clipId": {
      "$ref": "#/$defs/id"
    },
    "repeatCount": {
      "$ref": "#/$defs/positive"
    },
    "transpose": {
      "type": "integer",
      "minimum": -127,
      "maximum": 127
    },
    "noteMap": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/phraseNoteMapping"
      }
    },
    "velocityMode": {
      "enum": [
        "independent",
        "linked"
      ],
      "default": "independent",
      "description": "independent preserves concrete velocities on refresh; linked requires exact presence/value equality with the template. This field does not trigger refresh on load."
    },
    "noteStateMode": {
      "enum": [
        "independent",
        "linked"
      ],
      "default": "independent",
      "description": "Controls enabled/releaseVelocity/probability/velocityDeviation after materialization. independent preserves concrete note-state values on refresh; linked requires exact presence/value equality with the template. pitchRole is structural and must always remain semantically equal between a source pitch note and its mapped concrete note."
    }
  },
  "required": [
    "id",
    "templateId",
    "clipId",
    "repeatCount",
    "transpose",
    "noteMap"
  ],
  "additionalProperties": false
}
```

<a id="def-clipcandidate"></a>
## clipCandidate

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `id` | `#/$defs/id` | Yes |  |
| `clipIds` | `array<#/$defs/id>` | Yes |  |
| `name` | `string` | No/conditional |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "clipIds": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/id"
      },
      "uniqueItems": true
    },
    "name": {
      "type": "string"
    }
  },
  "required": [
    "id",
    "clipIds"
  ],
  "additionalProperties": false
}
```

<a id="def-clipchoicegroup"></a>
## clipChoiceGroup

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `id` | `#/$defs/id` | Yes |  |
| `candidates` | `array<#/$defs/clipCandidate>` | Yes |  |
| `selectedCandidateId` | `anyOf[2]` | Yes |  |
| `name` | `string` | No/conditional |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "candidates": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/clipCandidate"
      },
      "minItems": 1
    },
    "selectedCandidateId": {
      "anyOf": [
        {
          "$ref": "#/$defs/id"
        },
        {
          "type": "null"
        }
      ]
    },
    "name": {
      "type": "string"
    }
  },
  "required": [
    "id",
    "candidates",
    "selectedCandidateId"
  ],
  "additionalProperties": false
}
```

<a id="def-midimapping"></a>
## midiMapping

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `standard` | `enum ["gm1", "custom"]` | Yes | gm1=GM Level 1 percussion key 35..81; custom=explicit arbitrary MIDI1 note number. |
| `note` | `#/$defs/pitch` | Yes | MIDI1 note number in 0..127; for gm1 restrict to 35..81. |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "standard": {
      "enum": [
        "gm1",
        "custom"
      ],
      "description": "gm1=GM Level 1 percussion key 35..81; custom=explicit arbitrary MIDI1 note number."
    },
    "note": {
      "$ref": "#/$defs/pitch",
      "description": "MIDI1 note number in 0..127; for gm1 restrict to 35..81."
    }
  },
  "required": [
    "standard",
    "note"
  ],
  "additionalProperties": false,
  "allOf": [
    {
      "if": {
        "properties": {
          "standard": {
            "const": "gm1"
          }
        },
        "required": [
          "standard"
        ]
      },
      "then": {
        "properties": {
          "note": {
            "type": "integer",
            "minimum": 35,
            "maximum": 81
          }
        }
      }
    }
  ]
}
```

<a id="def-soundsource"></a>
## soundSource

Optional informational rendering class or opaque destination hint. In OSTF 4.0, track.midi.busId is the Core logical MIDI routing reference; soundSource does not bind a physical device, plugin state or preset.

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `kind` | `enum ["unassigned", "gm1", "externalMidi", "plugin", "hostManaged"]` | Yes |  |
| `identifier` | `string` | No/conditional | Opaque informational target identifier (for example a URI or plug-in identifier), not a physical MIDI-port binding or loading command. |

### Exact JSON Schema object

```json
{
  "type": "object",
  "description": "Optional informational rendering class or opaque destination hint. In OSTF 4.0, track.midi.busId is the Core logical MIDI routing reference; soundSource does not bind a physical device, plugin state or preset.",
  "properties": {
    "kind": {
      "enum": [
        "unassigned",
        "gm1",
        "externalMidi",
        "plugin",
        "hostManaged"
      ]
    },
    "identifier": {
      "type": "string",
      "minLength": 1,
      "description": "Opaque informational target identifier (for example a URI or plug-in identifier), not a physical MIDI-port binding or loading command."
    }
  },
  "required": [
    "kind"
  ],
  "additionalProperties": false,
  "allOf": [
    {
      "if": {
        "properties": {
          "kind": {
            "enum": [
              "gm1",
              "unassigned"
            ]
          }
        },
        "required": [
          "kind"
        ]
      },
      "then": {
        "not": {
          "required": [
            "identifier"
          ]
        }
      }
    }
  ]
}
```

<a id="def-localizednames"></a>
## localizedNames

Optional translations indexed by a conservative BCP 47 language-tag subset. The original name/title remains authoritative and is never rewritten by locale changes. Case-insensitive duplicate tags are forbidden semantically.

No direct `properties` table (object may be an enum, scalar, array or a composition).

### Exact JSON Schema object

```json
{
  "type": "object",
  "minProperties": 1,
  "propertyNames": {
    "type": "string",
    "pattern": "^(?:[A-Za-z]{2,3}|[A-Za-z]{5,8})(?:-[A-Za-z0-9]{2,8})*$"
  },
  "additionalProperties": {
    "type": "string",
    "minLength": 1
  },
  "description": "Optional translations indexed by a conservative BCP 47 language-tag subset. The original name/title remains authoritative and is never rewritten by locale changes. Case-insensitive duplicate tags are forbidden semantically."
}
```

<a id="def-drumkit"></a>
## drumKit

Optional named ordered membership of global Sound Slot IDs. Does not define plugin preset, sample loading, choke or a kit-local MIDI remapping.

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `id` | `#/$defs/id` | Yes |  |
| `name` | `string` | Yes |  |
| `localizedNames` | `#/$defs/localizedNames` | No/conditional |  |
| `soundSlotIds` | `array<#/$defs/id>` | Yes | Ordered, unique references to global soundSlots; may be empty. |

### Exact JSON Schema object

```json
{
  "type": "object",
  "description": "Optional named ordered membership of global Sound Slot IDs. Does not define plugin preset, sample loading, choke or a kit-local MIDI remapping.",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "name": {
      "type": "string"
    },
    "localizedNames": {
      "$ref": "#/$defs/localizedNames"
    },
    "soundSlotIds": {
      "type": "array",
      "uniqueItems": true,
      "items": {
        "$ref": "#/$defs/id"
      },
      "description": "Ordered, unique references to global soundSlots; may be empty."
    }
  },
  "required": [
    "id",
    "name",
    "soundSlotIds"
  ],
  "additionalProperties": false
}
```

<a id="def-voicing"></a>
## voicing

Optional informational chord voicing snapshot, not a played Core note collection. Repeated pitches and original array order have meaning for lossless preservation. Per-entry velocity is an optional voicing-preview hint.

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `pitches` | `array<#/$defs/pitch>` | Yes | Ordered multiset of concrete absolute pitches, 0-127. Duplicates allowed. |
| `velocities` | `array<anyOf[2]>` | No/conditional | Optional positional velocities aligned one-to-one to pitches. Null means unspecified at this index, not 0. Exact equal-length rule is semantic. |

### Exact JSON Schema object

```json
{
  "type": "object",
  "additionalProperties": false,
  "description": "Optional informational chord voicing snapshot, not a played Core note collection. Repeated pitches and original array order have meaning for lossless preservation. Per-entry velocity is an optional voicing-preview hint.",
  "properties": {
    "pitches": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/$defs/pitch"
      },
      "description": "Ordered multiset of concrete absolute pitches, 0-127. Duplicates allowed."
    },
    "velocities": {
      "type": "array",
      "minItems": 1,
      "items": {
        "anyOf": [
          {
            "type": "integer",
            "minimum": 1,
            "maximum": 127
          },
          {
            "type": "null"
          }
        ]
      },
      "description": "Optional positional velocities aligned one-to-one to pitches. Null means unspecified at this index, not 0. Exact equal-length rule is semantic."
    }
  },
  "required": [
    "pitches"
  ]
}
```

<a id="def-contributor"></a>
## contributor

One song-local identity; same contributor can receive multiple credit roles. Unicode source name is authoritative.

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `id` | `#/$defs/id` | Yes |  |
| `name` | `string` | Yes |  |
| `kind` | `enum ["person", "organization", "other"]` | No/conditional |  |
| `localizedNames` | `#/$defs/localizedNames` | No/conditional |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "additionalProperties": false,
  "description": "One song-local identity; same contributor can receive multiple credit roles. Unicode source name is authoritative.",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "name": {
      "type": "string",
      "minLength": 1
    },
    "kind": {
      "enum": [
        "person",
        "organization",
        "other"
      ]
    },
    "localizedNames": {
      "$ref": "#/$defs/localizedNames"
    }
  },
  "required": [
    "id",
    "name"
  ]
}
```

<a id="def-credit"></a>
## credit

Ordered credit assignment referencing one contributor; role is an open semantic token, not a translated label.

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `id` | `#/$defs/id` | Yes |  |
| `contributorId` | `#/$defs/id` | Yes |  |
| `role` | `string` | Yes |  |
| `label` | `string` | No/conditional |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "additionalProperties": false,
  "description": "Ordered credit assignment referencing one contributor; role is an open semantic token, not a translated label.",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "contributorId": {
      "$ref": "#/$defs/id"
    },
    "role": {
      "type": "string",
      "pattern": "^[a-z][a-z0-9.-]*$"
    },
    "label": {
      "type": "string"
    }
  },
  "required": [
    "id",
    "contributorId",
    "role"
  ]
}
```

<a id="def-alternatetitle"></a>
## alternateTitle

Stable-ID song title alternative; array position and title text do not identify it.

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `id` | `#/$defs/id` | Yes |  |
| `title` | `string` | Yes |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "additionalProperties": false,
  "description": "Stable-ID song title alternative; array position and title text do not identify it.",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "title": {
      "type": "string",
      "minLength": 1
    }
  },
  "required": [
    "id",
    "title"
  ]
}
```

<a id="def-languagemap32"></a>
## languageMap32

Open BCP 47 language-tag dictionary. Schema checks loose subtag structure; full BCP 47 well-formedness and case-insensitive uniqueness are semantic requirements. String may be empty if intentionally blank.

No direct `properties` table (object may be an enum, scalar, array or a composition).

### Exact JSON Schema object

```json
{
  "type": "object",
  "minProperties": 1,
  "propertyNames": {
    "type": "string",
    "pattern": "^[A-Za-z]{1,8}(?:-[A-Za-z0-9]{1,8})*$"
  },
  "additionalProperties": {
    "type": "string"
  },
  "description": "Open BCP 47 language-tag dictionary. Schema checks loose subtag structure; full BCP 47 well-formedness and case-insensitive uniqueness are semantic requirements. String may be empty if intentionally blank."
}
```

<a id="def-localizationtarget"></a>
## localizationTarget

Core target; song is ID-less, all others use global Core ID. No namespace/profile selector.

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `kind` | `enum ["song", "alternateTitle", "contributor", "credit", "section", "track", "clip", "soundSlot", "drumKit", "lyricDocument", "resource", "phraseTemplate", "clipCandidate", "clipChoiceGroup", "roleDefinition", "genre", "mood", "keyChange", "scale", "midiBus", "lyricVoice"]` | Yes |  |
| `id` | `#/$defs/id` | No/conditional |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "kind": {
      "enum": [
        "song",
        "alternateTitle",
        "contributor",
        "credit",
        "section",
        "track",
        "clip",
        "soundSlot",
        "drumKit",
        "lyricDocument",
        "resource",
        "phraseTemplate",
        "clipCandidate",
        "clipChoiceGroup",
        "roleDefinition",
        "genre",
        "mood",
        "keyChange",
        "scale",
        "midiBus",
        "lyricVoice"
      ]
    },
    "id": {
      "$ref": "#/$defs/id"
    }
  },
  "required": [
    "kind"
  ],
  "allOf": [
    {
      "if": {
        "properties": {
          "kind": {
            "const": "song"
          }
        },
        "required": [
          "kind"
        ]
      },
      "then": {
        "not": {
          "required": [
            "id"
          ]
        }
      },
      "else": {
        "required": [
          "id"
        ]
      }
    }
  ],
  "description": "Core target; song is ID-less, all others use global Core ID. No namespace/profile selector."
}
```

<a id="def-localizationentry"></a>
## localizationEntry

Independent translations for one stable source field. Original source text remains authoritative as fallback.

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `target` | `#/$defs/localizationTarget` | Yes |  |
| `field` | `string` | Yes | Exact allowed source text field for this target kind (see normative matrix). No arbitrary path or musical value fields. |
| `values` | `#/$defs/languageMap32` | Yes |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "target": {
      "$ref": "#/$defs/localizationTarget"
    },
    "field": {
      "type": "string",
      "minLength": 1,
      "description": "Exact allowed source text field for this target kind (see normative matrix). No arbitrary path or musical value fields."
    },
    "values": {
      "$ref": "#/$defs/languageMap32"
    }
  },
  "required": [
    "target",
    "field",
    "values"
  ],
  "description": "Independent translations for one stable source field. Original source text remains authoritative as fallback."
}
```

<a id="def-genre"></a>
## genre

One song-local open genre tag. The label is authored Unicode text and not a predefined controlled taxonomy; ID is stable for metadata merges and localization.

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `id` | `#/$defs/id` | Yes | Stable song-local ID unique among all Core objects. |
| `name` | `string` | Yes | Original Unicode genre label, never normalized or rewritten during import. |
| `externalUri` | `string` | No/conditional | Optional external taxonomy URI hint; never authoritative for a local genre label, and never auto-dereferenced. |

### Exact JSON Schema object

```json
{
  "type": "object",
  "description": "One song-local open genre tag. The label is authored Unicode text and not a predefined controlled taxonomy; ID is stable for metadata merges and localization.",
  "properties": {
    "id": {
      "$ref": "#/$defs/id",
      "description": "Stable song-local ID unique among all Core objects."
    },
    "name": {
      "type": "string",
      "minLength": 1,
      "description": "Original Unicode genre label, never normalized or rewritten during import."
    },
    "externalUri": {
      "type": "string",
      "minLength": 1,
      "format": "uri",
      "description": "Optional external taxonomy URI hint; never authoritative for a local genre label, and never auto-dereferenced."
    }
  },
  "required": [
    "id",
    "name"
  ],
  "additionalProperties": false
}
```

<a id="def-legacy33"></a>
## legacy33

No direct `properties` table (object may be an enum, scalar, array or a composition).

### Exact JSON Schema object

```json
{
  "$defs": {
    "id": {
      "type": "string",
      "pattern": "^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$",
      "not": {
        "pattern": "[\\r\\n\\u2028\\u2029]"
      }
    },
    "nonnegative": {
      "type": "integer",
      "minimum": 0,
      "maximum": 9007199254740991
    },
    "positive": {
      "type": "integer",
      "minimum": 1,
      "maximum": 9007199254740991
    },
    "signed": {
      "type": "integer",
      "minimum": -9007199254740991,
      "maximum": 9007199254740991
    },
    "pitch": {
      "type": "integer",
      "minimum": 0,
      "maximum": 127
    },
    "ref": {
      "type": "object",
      "properties": {
        "type": {
          "enum": [
            "section",
            "track",
            "clip",
            "note",
            "chord",
            "scale",
            "soundSlot",
            "drumKit",
            "lyricDocument",
            "lyricPhrase",
            "lyricUnit",
            "lyricAlignment",
            "resource",
            "genre"
          ]
        },
        "id": {
          "$ref": "#/$defs/legacy33/$defs/id"
        }
      },
      "required": [
        "type",
        "id"
      ],
      "additionalProperties": false
    },
    "range": {
      "type": "object",
      "properties": {
        "start": {
          "$ref": "#/$defs/legacy33/$defs/nonnegative"
        },
        "duration": {
          "$ref": "#/$defs/legacy33/$defs/positive"
        }
      },
      "required": [
        "start",
        "duration"
      ],
      "additionalProperties": false
    },
    "spelledPitchClass": {
      "type": "object",
      "properties": {
        "step": {
          "enum": [
            "A",
            "B",
            "C",
            "D",
            "E",
            "F",
            "G"
          ]
        },
        "alter": {
          "type": "integer",
          "minimum": -2,
          "maximum": 2
        }
      },
      "required": [
        "step",
        "alter"
      ],
      "additionalProperties": false
    },
    "song": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string"
        },
        "primaryMelodyTrackId": {
          "$ref": "#/$defs/legacy33/$defs/id"
        },
        "localizedTitles": {
          "$ref": "#/$defs/legacy33/$defs/localizedNames",
          "description": "Optional localized song-title alternatives. song.title is the stable fallback."
        },
        "subtitle": {
          "type": "string",
          "description": "Optional original-language subtitle."
        },
        "description": {
          "type": "string",
          "description": "Optional original-language description, including Unicode and line breaks."
        },
        "alternateTitles": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/legacy33/$defs/alternateTitle"
          },
          "description": "Additional stable-ID source-language titles."
        },
        "credits": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/legacy33/$defs/credit"
          },
          "description": "Ordered credit assignments to contributors. Multiple roles and duplicate contributors permitted."
        },
        "genres": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/legacy33/$defs/genre"
          },
          "description": "Optional open-ended ordered genre tags; zero or more allowed. Order is authored display preference, first item is primary if a primary label is desired, not a generator weight. Absent means unspecified."
        }
      },
      "required": [
        "title"
      ],
      "additionalProperties": false
    },
    "section": {
      "type": "object",
      "properties": {
        "id": {
          "$ref": "#/$defs/legacy33/$defs/id"
        },
        "name": {
          "type": "string",
          "minLength": 1
        },
        "start": {
          "$ref": "#/$defs/legacy33/$defs/nonnegative"
        },
        "duration": {
          "$ref": "#/$defs/legacy33/$defs/positive"
        },
        "role": {
          "type": "string"
        },
        "localizedNames": {
          "$ref": "#/$defs/legacy33/$defs/localizedNames",
          "description": "Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity."
        }
      },
      "required": [
        "id",
        "name",
        "start",
        "duration"
      ],
      "additionalProperties": false
    },
    "tempo": {
      "type": "object",
      "properties": {
        "at": {
          "$ref": "#/$defs/legacy33/$defs/nonnegative"
        },
        "bpm": {
          "type": "number",
          "exclusiveMinimum": 0,
          "maximum": 1000
        }
      },
      "required": [
        "at",
        "bpm"
      ],
      "additionalProperties": false
    },
    "meter": {
      "type": "object",
      "properties": {
        "at": {
          "$ref": "#/$defs/legacy33/$defs/nonnegative"
        },
        "numerator": {
          "type": "integer",
          "minimum": 1,
          "maximum": 64
        },
        "denominator": {
          "enum": [
            1,
            2,
            4,
            8,
            16,
            32,
            64
          ],
          "type": "integer"
        }
      },
      "required": [
        "at",
        "numerator",
        "denominator"
      ],
      "additionalProperties": false
    },
    "timeline": {
      "type": "object",
      "properties": {
        "sections": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/legacy33/$defs/section"
          }
        },
        "tempoChanges": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/legacy33/$defs/tempo"
          },
          "minItems": 1
        },
        "meterChanges": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/legacy33/$defs/meter"
          },
          "minItems": 1
        }
      },
      "required": [
        "sections",
        "tempoChanges",
        "meterChanges"
      ],
      "additionalProperties": false
    },
    "chord": {
      "type": "object",
      "properties": {
        "id": {
          "$ref": "#/$defs/legacy33/$defs/id"
        },
        "start": {
          "$ref": "#/$defs/legacy33/$defs/nonnegative"
        },
        "duration": {
          "$ref": "#/$defs/legacy33/$defs/positive"
        },
        "label": {
          "type": "string",
          "minLength": 1
        },
        "root": {
          "$ref": "#/$defs/legacy33/$defs/spelledPitchClass"
        },
        "intervals": {
          "type": "array",
          "items": {
            "type": "integer",
            "minimum": 0,
            "maximum": 35
          },
          "minItems": 1,
          "maxItems": 36,
          "uniqueItems": true,
          "contains": {
            "const": 0
          }
        },
        "bass": {
          "$ref": "#/$defs/legacy33/$defs/spelledPitchClass"
        },
        "voicing": {
          "$ref": "#/$defs/legacy33/$defs/voicing",
          "description": "Optional pitch snapshot (not an arrangement note sequence). No automatic playback."
        }
      },
      "required": [
        "id",
        "start",
        "duration",
        "label"
      ],
      "additionalProperties": false,
      "dependentRequired": {
        "root": [
          "intervals"
        ],
        "intervals": [
          "root"
        ]
      }
    },
    "scale": {
      "type": "object",
      "properties": {
        "id": {
          "$ref": "#/$defs/legacy33/$defs/id"
        },
        "start": {
          "$ref": "#/$defs/legacy33/$defs/nonnegative"
        },
        "duration": {
          "$ref": "#/$defs/legacy33/$defs/positive"
        },
        "label": {
          "type": "string"
        },
        "tonic": {
          "$ref": "#/$defs/legacy33/$defs/spelledPitchClass"
        },
        "intervals": {
          "type": "array",
          "items": {
            "type": "integer",
            "minimum": 0,
            "maximum": 11
          },
          "minItems": 1,
          "maxItems": 12,
          "uniqueItems": true,
          "contains": {
            "const": 0
          }
        }
      },
      "required": [
        "id",
        "start",
        "duration",
        "tonic",
        "intervals"
      ],
      "additionalProperties": false
    },
    "harmony": {
      "type": "object",
      "properties": {
        "chords": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/legacy33/$defs/chord"
          }
        },
        "scales": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/legacy33/$defs/scale"
          }
        }
      },
      "required": [
        "chords",
        "scales"
      ],
      "additionalProperties": false
    },
    "instrument": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "family": {
          "type": "string"
        },
        "localizedNames": {
          "$ref": "#/$defs/legacy33/$defs/localizedNames",
          "description": "Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity."
        }
      },
      "required": [
        "name"
      ],
      "additionalProperties": false
    },
    "note": {
      "type": "object",
      "properties": {
        "id": {
          "$ref": "#/$defs/legacy33/$defs/id"
        },
        "start": {
          "$ref": "#/$defs/legacy33/$defs/signed"
        },
        "duration": {
          "$ref": "#/$defs/legacy33/$defs/positive",
          "description": "Positive note gate in ticks, not the guaranteed audible duration of a one-shot percussion sample."
        },
        "pitch": {
          "$ref": "#/$defs/legacy33/$defs/pitch"
        },
        "soundSlotId": {
          "$ref": "#/$defs/legacy33/$defs/id",
          "description": "Document-local Sound Slot ID. Distinct events and IDs stay distinct even if several slots share a MIDI key; a renderer decides the acoustic timbre."
        },
        "velocity": {
          "type": "integer",
          "minimum": 1,
          "maximum": 127,
          "description": "Optional authored note-on velocity for performed Core notes, 1–127; omit to mean unspecified. It is not a note-off velocity, controller stream, chord tone, or a sound-rendering guarantee. Never insert an inferred default when saving."
        }
      },
      "required": [
        "id",
        "start",
        "duration"
      ],
      "additionalProperties": false,
      "oneOf": [
        {
          "required": [
            "pitch"
          ],
          "not": {
            "required": [
              "soundSlotId"
            ]
          }
        },
        {
          "required": [
            "soundSlotId"
          ],
          "not": {
            "required": [
              "pitch"
            ]
          }
        }
      ],
      "description": "Concrete Core note; optional velocity is a note-on attribute. Phrase templates use a separate version-frozen sourceNote shape."
    },
    "clip": {
      "type": "object",
      "properties": {
        "id": {
          "$ref": "#/$defs/legacy33/$defs/id"
        },
        "name": {
          "type": "string"
        },
        "start": {
          "$ref": "#/$defs/legacy33/$defs/nonnegative"
        },
        "duration": {
          "$ref": "#/$defs/legacy33/$defs/positive"
        },
        "enabled": {
          "type": "boolean",
          "default": true
        },
        "notes": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/legacy33/$defs/note"
          }
        },
        "localizedNames": {
          "$ref": "#/$defs/legacy33/$defs/localizedNames",
          "description": "Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity."
        }
      },
      "required": [
        "id",
        "start",
        "duration",
        "notes"
      ],
      "additionalProperties": false
    },
    "track": {
      "type": "object",
      "properties": {
        "id": {
          "$ref": "#/$defs/legacy33/$defs/id"
        },
        "name": {
          "type": "string"
        },
        "role": {
          "type": "string"
        },
        "instrument": {
          "$ref": "#/$defs/legacy33/$defs/instrument"
        },
        "enabled": {
          "type": "boolean",
          "default": true
        },
        "clips": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/legacy33/$defs/clip"
          }
        },
        "trackType": {
          "enum": [
            "melodic",
            "drum",
            "mixed"
          ],
          "description": "Semantic event-target category; optional; missing/empty-note tracks may be unknown. It is not a DAW track class."
        },
        "preferredView": {
          "enum": [
            "auto",
            "pianoRoll",
            "drumGrid"
          ],
          "default": "auto",
          "description": "Non-binding presentation preference. Does not change note meaning."
        },
        "soundSource": {
          "$ref": "#/$defs/legacy33/$defs/soundSource",
          "description": "Optional sound-source selection hint, not a plug-in state, preset blob, or sound guarantee."
        },
        "localizedNames": {
          "$ref": "#/$defs/legacy33/$defs/localizedNames",
          "description": "Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity."
        },
        "drumKitId": {
          "$ref": "#/$defs/legacy33/$defs/id",
          "description": "Optional reference to a declared drumKit; only for a drum/mixed or empty inferred track. All stored slot events in the track must belong to the referenced kit."
        }
      },
      "required": [
        "id",
        "name",
        "clips"
      ],
      "additionalProperties": false,
      "allOf": [
        {
          "if": {
            "properties": {
              "trackType": {
                "const": "melodic"
              }
            },
            "required": [
              "trackType"
            ]
          },
          "then": {
            "not": {
              "required": [
                "drumKitId"
              ]
            }
          }
        }
      ]
    },
    "soundSlot": {
      "type": "object",
      "properties": {
        "id": {
          "$ref": "#/$defs/legacy33/$defs/id"
        },
        "name": {
          "type": "string"
        },
        "role": {
          "type": "string",
          "description": "Optional free-text musical role; not a standardized GM instrument code or an acoustic sample identifier."
        },
        "midiNote": {
          "$ref": "#/$defs/legacy33/$defs/pitch",
          "description": "Legacy 3.0 MIDI note hint only; not a GM1 declaration or preview timbre identity."
        },
        "midiMapping": {
          "$ref": "#/$defs/legacy33/$defs/midiMapping",
          "description": "Explicit external MIDI1 output mapping; standard=gm1 is separate from custom even for an equal note number. Not a unique slot or audio identity."
        },
        "localizedNames": {
          "$ref": "#/$defs/legacy33/$defs/localizedNames",
          "description": "Optional localized display variants; retain the original name and stable ID. Names never determine track type, routing or identity."
        }
      },
      "required": [
        "id",
        "name"
      ],
      "additionalProperties": false,
      "description": "Document-local stable logical percussion target. Equal roles, names or MIDI note mappings never merge distinct slot IDs. No sample/audio identity is encoded."
    },
    "lyricDocument": {
      "type": "object",
      "properties": {
        "id": {
          "$ref": "#/$defs/legacy33/$defs/id"
        },
        "title": {
          "type": "string"
        },
        "language": {
          "type": "string"
        }
      },
      "required": [
        "id"
      ],
      "additionalProperties": false
    },
    "lyricPhrase": {
      "type": "object",
      "properties": {
        "id": {
          "$ref": "#/$defs/legacy33/$defs/id"
        },
        "documentId": {
          "$ref": "#/$defs/legacy33/$defs/id"
        },
        "text": {
          "type": "string"
        },
        "pronunciation": {
          "type": "string"
        },
        "start": {
          "$ref": "#/$defs/legacy33/$defs/nonnegative"
        },
        "duration": {
          "$ref": "#/$defs/legacy33/$defs/positive"
        }
      },
      "required": [
        "id",
        "documentId",
        "text"
      ],
      "additionalProperties": false,
      "dependentRequired": {
        "start": [
          "duration"
        ],
        "duration": [
          "start"
        ]
      }
    },
    "lyricUnit": {
      "type": "object",
      "properties": {
        "id": {
          "$ref": "#/$defs/legacy33/$defs/id"
        },
        "phraseId": {
          "$ref": "#/$defs/legacy33/$defs/id"
        },
        "text": {
          "type": "string"
        },
        "pronunciation": {
          "type": "string"
        },
        "start": {
          "$ref": "#/$defs/legacy33/$defs/nonnegative"
        },
        "duration": {
          "$ref": "#/$defs/legacy33/$defs/positive"
        }
      },
      "required": [
        "id",
        "phraseId",
        "text"
      ],
      "additionalProperties": false,
      "dependentRequired": {
        "start": [
          "duration"
        ],
        "duration": [
          "start"
        ]
      }
    },
    "lyricAlignment": {
      "type": "object",
      "properties": {
        "id": {
          "$ref": "#/$defs/legacy33/$defs/id"
        },
        "unitIds": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/legacy33/$defs/id"
          },
          "uniqueItems": true,
          "minItems": 1
        },
        "noteIds": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/legacy33/$defs/id"
          },
          "uniqueItems": true,
          "minItems": 1
        }
      },
      "required": [
        "id",
        "unitIds",
        "noteIds"
      ],
      "additionalProperties": false
    },
    "lyrics": {
      "type": "object",
      "properties": {
        "documents": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/legacy33/$defs/lyricDocument"
          }
        },
        "phrases": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/legacy33/$defs/lyricPhrase"
          }
        },
        "units": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/legacy33/$defs/lyricUnit"
          }
        },
        "alignments": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/legacy33/$defs/lyricAlignment"
          }
        }
      },
      "required": [
        "documents",
        "phrases",
        "units",
        "alignments"
      ],
      "additionalProperties": false
    },
    "sha256": {
      "type": "string",
      "pattern": "^[0-9a-f]{64}$",
      "not": {
        "pattern": "[\\r\\n\\u2028\\u2029]"
      }
    },
    "resource": {
      "type": "object",
      "properties": {
        "id": {
          "$ref": "#/$defs/legacy33/$defs/id"
        },
        "kind": {
          "enum": [
            "audio",
            "midi",
            "text",
            "other"
          ]
        },
        "uri": {
          "type": "string",
          "minLength": 1
        },
        "name": {
          "type": "string"
        },
        "sha256": {
          "$ref": "#/$defs/legacy33/$defs/sha256"
        }
      },
      "required": [
        "id",
        "kind",
        "uri"
      ],
      "additionalProperties": false
    },
    "dependencies": {
      "oneOf": [
        {
          "type": "object",
          "properties": {
            "scope": {
              "enum": [
                "document",
                "none"
              ]
            }
          },
          "required": [
            "scope"
          ],
          "additionalProperties": false
        },
        {
          "type": "object",
          "properties": {
            "scope": {
              "const": "objects"
            },
            "refs": {
              "type": "array",
              "items": {
                "$ref": "#/$defs/legacy33/$defs/ref"
              },
              "minItems": 1,
              "uniqueItems": true
            }
          },
          "required": [
            "scope",
            "refs"
          ],
          "additionalProperties": false
        }
      ]
    },
    "extension": {
      "type": "object",
      "properties": {
        "version": {
          "type": "string",
          "minLength": 1
        },
        "status": {
          "enum": [
            "current",
            "stale",
            "unverified"
          ]
        },
        "dependencies": {
          "$ref": "#/$defs/legacy33/$defs/dependencies"
        },
        "data": {}
      },
      "required": [
        "version",
        "status",
        "dependencies",
        "data"
      ],
      "additionalProperties": false
    },
    "relativeAssignment": {
      "type": "object",
      "properties": {
        "noteId": {
          "$ref": "#/$defs/legacy33/$defs/id"
        },
        "basis": {
          "enum": [
            "chordTone",
            "scaleDegree"
          ]
        },
        "contextId": {
          "$ref": "#/$defs/legacy33/$defs/id"
        },
        "anchorPitch": {
          "$ref": "#/$defs/legacy33/$defs/pitch"
        },
        "index": {
          "type": "integer",
          "minimum": 1,
          "maximum": 36
        },
        "chromaticOffset": {
          "type": "integer",
          "minimum": -24,
          "maximum": 24
        }
      },
      "required": [
        "noteId",
        "basis",
        "contextId",
        "anchorPitch",
        "index",
        "chromaticOffset"
      ],
      "additionalProperties": false,
      "allOf": [
        {
          "if": {
            "properties": {
              "basis": {
                "const": "scaleDegree"
              }
            },
            "required": [
              "basis"
            ]
          },
          "then": {
            "properties": {
              "index": {
                "maximum": 12
              }
            }
          }
        }
      ]
    },
    "relativeData": {
      "type": "object",
      "properties": {
        "assignments": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/legacy33/$defs/relativeAssignment"
          }
        }
      },
      "required": [
        "assignments"
      ],
      "additionalProperties": false
    },
    "generator": {
      "type": "object",
      "properties": {
        "id": {
          "type": "string",
          "minLength": 1
        },
        "version": {
          "type": "string",
          "minLength": 1
        }
      },
      "required": [
        "id",
        "version"
      ],
      "additionalProperties": false
    },
    "generationInput": {
      "type": "object",
      "properties": {
        "role": {
          "type": "string",
          "minLength": 1
        },
        "ref": {
          "$ref": "#/$defs/legacy33/$defs/ref"
        },
        "readRange": {
          "$ref": "#/$defs/legacy33/$defs/range"
        }
      },
      "required": [
        "role",
        "ref"
      ],
      "additionalProperties": false
    },
    "generationProcess": {
      "type": "object",
      "properties": {
        "id": {
          "$ref": "#/$defs/legacy33/$defs/id"
        },
        "generator": {
          "$ref": "#/$defs/legacy33/$defs/generator"
        },
        "inputs": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/legacy33/$defs/generationInput"
          }
        },
        "outputs": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/legacy33/$defs/ref"
          },
          "minItems": 1
        },
        "targetRange": {
          "$ref": "#/$defs/legacy33/$defs/range"
        },
        "protectedNoteIds": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/legacy33/$defs/id"
          },
          "uniqueItems": true
        },
        "vendorExtension": {
          "type": "string",
          "minLength": 1
        }
      },
      "required": [
        "id",
        "generator",
        "inputs",
        "outputs",
        "protectedNoteIds"
      ],
      "additionalProperties": false
    },
    "generationData": {
      "type": "object",
      "properties": {
        "processes": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/legacy33/$defs/generationProcess"
          }
        }
      },
      "required": [
        "processes"
      ],
      "additionalProperties": false
    },
    "color": {
      "type": "string",
      "pattern": "^#[0-9A-Fa-f]{6}$",
      "not": {
        "pattern": "[\\r\\n\\u2028\\u2029]"
      }
    },
    "roleDefinition": {
      "type": "object",
      "properties": {
        "id": {
          "$ref": "#/$defs/legacy33/$defs/id"
        },
        "name": {
          "type": "string",
          "minLength": 1
        },
        "baseRole": {
          "type": "string"
        }
      },
      "required": [
        "id",
        "name"
      ],
      "additionalProperties": false
    },
    "roleColorMap": {
      "type": "object",
      "additionalProperties": {
        "$ref": "#/$defs/legacy33/$defs/color"
      }
    },
    "customRoleColorMap": {
      "type": "object",
      "propertyNames": {
        "$ref": "#/$defs/legacy33/$defs/id"
      },
      "additionalProperties": {
        "$ref": "#/$defs/legacy33/$defs/color"
      }
    },
    "objectColor": {
      "type": "object",
      "properties": {
        "target": {
          "$ref": "#/$defs/legacy33/$defs/ref"
        },
        "color": {
          "$ref": "#/$defs/legacy33/$defs/color"
        }
      },
      "required": [
        "target",
        "color"
      ],
      "additionalProperties": false
    },
    "appearanceData": {
      "type": "object",
      "properties": {
        "roleDefinitions": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/legacy33/$defs/roleDefinition"
          }
        },
        "sectionRoleAssignments": {
          "type": "object",
          "propertyNames": {
            "$ref": "#/$defs/legacy33/$defs/id"
          },
          "additionalProperties": {
            "$ref": "#/$defs/legacy33/$defs/id"
          }
        },
        "appearance": {
          "type": "object",
          "properties": {
            "roleColors": {
              "$ref": "#/$defs/legacy33/$defs/roleColorMap"
            },
            "customRoleColors": {
              "$ref": "#/$defs/legacy33/$defs/customRoleColorMap"
            },
            "objectColors": {
              "type": "array",
              "items": {
                "$ref": "#/$defs/legacy33/$defs/objectColor"
              }
            }
          },
          "required": [
            "roleColors",
            "customRoleColors",
            "objectColors"
          ],
          "additionalProperties": false
        }
      },
      "required": [
        "roleDefinitions",
        "sectionRoleAssignments",
        "appearance"
      ],
      "additionalProperties": false
    },
    "legacyData": {
      "type": "object",
      "properties": {
        "sourceVersion": {
          "const": "2.3.0"
        },
        "sourceSha256": {
          "$ref": "#/$defs/legacy33/$defs/sha256"
        },
        "sourceText": {
          "type": "string",
          "minLength": 1
        },
        "conversionReport": {
          "type": "object"
        }
      },
      "required": [
        "sourceVersion",
        "sourceSha256",
        "sourceText",
        "conversionReport"
      ],
      "additionalProperties": false
    },
    "extensions": {
      "type": "object",
      "propertyNames": {
        "pattern": "^[a-z][a-z0-9-]*(?:\\.[a-z][a-z0-9-]*){2,}$",
        "not": {
          "pattern": "[\\r\\n\\u2028\\u2029]"
        }
      },
      "properties": {
        "org.ostf.relative-phrase.v1": {
          "allOf": [
            {
              "$ref": "#/$defs/legacy33/$defs/extension"
            },
            {
              "if": {
                "properties": {
                  "version": {
                    "const": "1.0.0-draft.1"
                  }
                },
                "required": [
                  "version"
                ]
              },
              "then": {
                "properties": {
                  "data": {
                    "$ref": "#/$defs/legacy33/$defs/relativeData"
                  }
                }
              }
            }
          ]
        },
        "org.ostf.generation-context.v1": {
          "allOf": [
            {
              "$ref": "#/$defs/legacy33/$defs/extension"
            },
            {
              "if": {
                "properties": {
                  "version": {
                    "const": "1.0.0-draft.1"
                  }
                },
                "required": [
                  "version"
                ]
              },
              "then": {
                "properties": {
                  "data": {
                    "$ref": "#/$defs/legacy33/$defs/generationData"
                  }
                }
              }
            }
          ]
        },
        "org.ostf.appearance.v1": {
          "allOf": [
            {
              "$ref": "#/$defs/legacy33/$defs/extension"
            },
            {
              "if": {
                "properties": {
                  "version": {
                    "const": "1.0.0-draft.1"
                  }
                },
                "required": [
                  "version"
                ]
              },
              "then": {
                "properties": {
                  "data": {
                    "$ref": "#/$defs/legacy33/$defs/appearanceData"
                  }
                }
              }
            }
          ]
        },
        "org.ostf.legacy-import.v1": {
          "allOf": [
            {
              "$ref": "#/$defs/legacy33/$defs/extension"
            },
            {
              "if": {
                "properties": {
                  "version": {
                    "const": "1.0.0-draft.1"
                  }
                },
                "required": [
                  "version"
                ]
              },
              "then": {
                "properties": {
                  "data": {
                    "$ref": "#/$defs/legacy33/$defs/legacyData"
                  }
                }
              }
            }
          ]
        },
        "org.ostf.phrase-library.v1": {
          "allOf": [
            {
              "$ref": "#/$defs/legacy33/$defs/extension"
            },
            {
              "if": {
                "properties": {
                  "version": {
                    "const": "1.0.0-draft.1"
                  }
                },
                "required": [
                  "version"
                ]
              },
              "then": {
                "properties": {
                  "data": {
                    "$ref": "#/$defs/legacy33/$defs/phraseLibraryData"
                  }
                }
              }
            }
          ]
        },
        "org.ostf.clip-choices.v1": {
          "allOf": [
            {
              "$ref": "#/$defs/legacy33/$defs/extension"
            },
            {
              "if": {
                "properties": {
                  "version": {
                    "const": "1.0.0-draft.1"
                  }
                },
                "required": [
                  "version"
                ]
              },
              "then": {
                "properties": {
                  "data": {
                    "$ref": "#/$defs/legacy33/$defs/clipChoicesData"
                  }
                }
              }
            }
          ]
        },
        "org.ostf.localization.v1": {
          "allOf": [
            {
              "$ref": "#/$defs/legacy33/$defs/extension"
            },
            {
              "if": {
                "properties": {
                  "version": {
                    "const": "1.0.0"
                  }
                },
                "required": [
                  "version"
                ]
              },
              "then": {
                "properties": {
                  "data": {
                    "$ref": "#/$defs/legacy33/$defs/localizationData"
                  }
                }
              }
            }
          ]
        }
      },
      "additionalProperties": {
        "$ref": "#/$defs/legacy33/$defs/extension"
      }
    },
    "phraseTemplate": {
      "type": "object",
      "properties": {
        "id": {
          "$ref": "#/$defs/legacy33/$defs/id"
        },
        "duration": {
          "$ref": "#/$defs/legacy33/$defs/positive"
        },
        "notes": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/legacy33/$defs/phraseSourceNote"
          }
        },
        "name": {
          "type": "string"
        }
      },
      "required": [
        "id",
        "duration",
        "notes"
      ],
      "additionalProperties": false
    },
    "phraseNoteMapping": {
      "type": "object",
      "properties": {
        "templateNoteId": {
          "$ref": "#/$defs/legacy33/$defs/id"
        },
        "repeatIndex": {
          "$ref": "#/$defs/legacy33/$defs/nonnegative"
        },
        "noteId": {
          "$ref": "#/$defs/legacy33/$defs/id"
        }
      },
      "required": [
        "templateNoteId",
        "repeatIndex",
        "noteId"
      ],
      "additionalProperties": false
    },
    "phraseInstance": {
      "type": "object",
      "properties": {
        "id": {
          "$ref": "#/$defs/legacy33/$defs/id"
        },
        "templateId": {
          "$ref": "#/$defs/legacy33/$defs/id"
        },
        "clipId": {
          "$ref": "#/$defs/legacy33/$defs/id"
        },
        "repeatCount": {
          "$ref": "#/$defs/legacy33/$defs/positive"
        },
        "transpose": {
          "type": "integer",
          "minimum": -127,
          "maximum": 127
        },
        "noteMap": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/legacy33/$defs/phraseNoteMapping"
          }
        }
      },
      "required": [
        "id",
        "templateId",
        "clipId",
        "repeatCount",
        "transpose",
        "noteMap"
      ],
      "additionalProperties": false
    },
    "phraseLibraryData": {
      "type": "object",
      "properties": {
        "templates": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/legacy33/$defs/phraseTemplate"
          }
        },
        "instances": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/legacy33/$defs/phraseInstance"
          }
        }
      },
      "required": [
        "templates",
        "instances"
      ],
      "additionalProperties": false
    },
    "clipCandidate": {
      "type": "object",
      "properties": {
        "id": {
          "$ref": "#/$defs/legacy33/$defs/id"
        },
        "clipIds": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/legacy33/$defs/id"
          },
          "uniqueItems": true
        },
        "name": {
          "type": "string"
        }
      },
      "required": [
        "id",
        "clipIds"
      ],
      "additionalProperties": false
    },
    "clipChoiceGroup": {
      "type": "object",
      "properties": {
        "id": {
          "$ref": "#/$defs/legacy33/$defs/id"
        },
        "candidates": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/legacy33/$defs/clipCandidate"
          },
          "minItems": 1
        },
        "selectedCandidateId": {
          "anyOf": [
            {
              "$ref": "#/$defs/legacy33/$defs/id"
            },
            {
              "type": "null"
            }
          ]
        },
        "name": {
          "type": "string"
        }
      },
      "required": [
        "id",
        "candidates",
        "selectedCandidateId"
      ],
      "additionalProperties": false
    },
    "clipChoicesData": {
      "type": "object",
      "properties": {
        "groups": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/legacy33/$defs/clipChoiceGroup"
          }
        }
      },
      "required": [
        "groups"
      ],
      "additionalProperties": false
    },
    "midiMapping": {
      "type": "object",
      "properties": {
        "standard": {
          "enum": [
            "gm1",
            "custom"
          ],
          "description": "gm1=GM Level 1 percussion key 35..81; custom=explicit arbitrary MIDI1 note number."
        },
        "note": {
          "$ref": "#/$defs/legacy33/$defs/pitch",
          "description": "MIDI1 note number in 0..127; for gm1 restrict to 35..81."
        }
      },
      "required": [
        "standard",
        "note"
      ],
      "additionalProperties": false,
      "allOf": [
        {
          "if": {
            "properties": {
              "standard": {
                "const": "gm1"
              }
            },
            "required": [
              "standard"
            ]
          },
          "then": {
            "properties": {
              "note": {
                "type": "integer",
                "minimum": 35,
                "maximum": 81
              }
            }
          }
        }
      ]
    },
    "soundSource": {
      "type": "object",
      "description": "Optional informational rendering class or opaque destination hint. Program Change, Bank Select and plugin presets are not standardized by Core.",
      "properties": {
        "kind": {
          "enum": [
            "unassigned",
            "gm1",
            "externalMidi",
            "plugin",
            "hostManaged"
          ]
        },
        "identifier": {
          "type": "string",
          "minLength": 1,
          "description": "Opaque target identifier, e.g. URI, plug-in identifier or port alias, not a loading command."
        }
      },
      "required": [
        "kind"
      ],
      "additionalProperties": false,
      "allOf": [
        {
          "if": {
            "properties": {
              "kind": {
                "enum": [
                  "gm1",
                  "unassigned"
                ]
              }
            },
            "required": [
              "kind"
            ]
          },
          "then": {
            "not": {
              "required": [
                "identifier"
              ]
            }
          }
        }
      ]
    },
    "localizedNames": {
      "type": "object",
      "minProperties": 1,
      "propertyNames": {
        "type": "string",
        "pattern": "^(?:[A-Za-z]{2,3}|[A-Za-z]{5,8})(?:-[A-Za-z0-9]{2,8})*$"
      },
      "additionalProperties": {
        "type": "string",
        "minLength": 1
      },
      "description": "Optional translations indexed by a conservative BCP 47 language-tag subset. The original name/title remains authoritative and is never rewritten by locale changes. Case-insensitive duplicate tags are forbidden semantically."
    },
    "drumKit": {
      "type": "object",
      "description": "Optional named ordered membership of global Sound Slot IDs. Does not define plugin preset, sample loading, choke or a kit-local MIDI remapping.",
      "properties": {
        "id": {
          "$ref": "#/$defs/legacy33/$defs/id"
        },
        "name": {
          "type": "string"
        },
        "localizedNames": {
          "$ref": "#/$defs/legacy33/$defs/localizedNames"
        },
        "soundSlotIds": {
          "type": "array",
          "uniqueItems": true,
          "items": {
            "$ref": "#/$defs/legacy33/$defs/id"
          },
          "description": "Ordered, unique references to global soundSlots; may be empty."
        }
      },
      "required": [
        "id",
        "name",
        "soundSlotIds"
      ],
      "additionalProperties": false
    },
    "phraseSourceNote": {
      "type": "object",
      "properties": {
        "id": {
          "$ref": "#/$defs/legacy33/$defs/id"
        },
        "start": {
          "$ref": "#/$defs/legacy33/$defs/signed"
        },
        "duration": {
          "$ref": "#/$defs/legacy33/$defs/positive"
        },
        "pitch": {
          "$ref": "#/$defs/legacy33/$defs/pitch"
        },
        "soundSlotId": {
          "$ref": "#/$defs/legacy33/$defs/id"
        }
      },
      "required": [
        "id",
        "start",
        "duration"
      ],
      "additionalProperties": false,
      "oneOf": [
        {
          "required": [
            "pitch"
          ],
          "not": {
            "required": [
              "soundSlotId"
            ]
          }
        },
        {
          "required": [
            "soundSlotId"
          ],
          "not": {
            "required": [
              "pitch"
            ]
          }
        }
      ],
      "description": "Version-frozen 1.0.0-draft.1 phrase source note. Does NOT admit velocity; a linked Core instance may independently set velocity."
    },
    "voicing": {
      "type": "object",
      "additionalProperties": false,
      "description": "Optional informational chord voicing snapshot, not a played Core note collection. Repeated pitches and original array order have meaning for lossless preservation. Per-entry velocity is an optional voicing-preview hint.",
      "properties": {
        "pitches": {
          "type": "array",
          "minItems": 1,
          "items": {
            "$ref": "#/$defs/legacy33/$defs/pitch"
          },
          "description": "Ordered multiset of concrete absolute pitches, 0-127. Duplicates allowed."
        },
        "velocities": {
          "type": "array",
          "minItems": 1,
          "items": {
            "anyOf": [
              {
                "type": "integer",
                "minimum": 1,
                "maximum": 127
              },
              {
                "type": "null"
              }
            ]
          },
          "description": "Optional positional velocities aligned one-to-one to pitches. Null means unspecified at this index, not 0. Exact equal-length rule is semantic."
        }
      },
      "required": [
        "pitches"
      ]
    },
    "contributor": {
      "type": "object",
      "additionalProperties": false,
      "description": "One song-local identity; same contributor can receive multiple credit roles. Unicode source name is authoritative.",
      "properties": {
        "id": {
          "$ref": "#/$defs/legacy33/$defs/id"
        },
        "name": {
          "type": "string",
          "minLength": 1
        },
        "kind": {
          "enum": [
            "person",
            "organization",
            "other"
          ]
        },
        "localizedNames": {
          "$ref": "#/$defs/legacy33/$defs/localizedNames"
        }
      },
      "required": [
        "id",
        "name"
      ]
    },
    "credit": {
      "type": "object",
      "additionalProperties": false,
      "description": "Ordered credit assignment referencing one contributor; role is an open semantic token, not a translated label.",
      "properties": {
        "id": {
          "$ref": "#/$defs/legacy33/$defs/id"
        },
        "contributorId": {
          "$ref": "#/$defs/legacy33/$defs/id"
        },
        "role": {
          "type": "string",
          "pattern": "^[a-z][a-z0-9.-]*$"
        },
        "label": {
          "type": "string"
        }
      },
      "required": [
        "id",
        "contributorId",
        "role"
      ]
    },
    "alternateTitle": {
      "type": "object",
      "additionalProperties": false,
      "description": "Stable-ID song title alternative; array position and title text do not identify it.",
      "properties": {
        "id": {
          "$ref": "#/$defs/legacy33/$defs/id"
        },
        "title": {
          "type": "string",
          "minLength": 1
        }
      },
      "required": [
        "id",
        "title"
      ]
    },
    "languageMap32": {
      "type": "object",
      "minProperties": 1,
      "propertyNames": {
        "type": "string",
        "pattern": "^[A-Za-z]{1,8}(?:-[A-Za-z0-9]{1,8})*$"
      },
      "additionalProperties": {
        "type": "string"
      },
      "description": "Open BCP 47 language-tag dictionary. Schema checks loose subtag structure; full BCP 47 well-formedness and case-insensitive uniqueness are semantic requirements. String may be empty if intentionally blank."
    },
    "localizationTarget": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "kind": {
          "enum": [
            "song",
            "alternateTitle",
            "contributor",
            "credit",
            "section",
            "track",
            "clip",
            "soundSlot",
            "drumKit",
            "lyricDocument",
            "resource",
            "phraseTemplate",
            "clipCandidate",
            "clipChoiceGroup",
            "roleDefinition",
            "genre"
          ]
        },
        "id": {
          "$ref": "#/$defs/legacy33/$defs/id"
        },
        "profile": {
          "type": "string",
          "enum": [
            "org.ostf.phrase-library.v1",
            "org.ostf.clip-choices.v1",
            "org.ostf.appearance.v1"
          ]
        }
      },
      "required": [
        "kind"
      ],
      "allOf": [
        {
          "if": {
            "properties": {
              "kind": {
                "const": "song"
              }
            },
            "required": [
              "kind"
            ]
          },
          "then": {
            "not": {
              "anyOf": [
                {
                  "required": [
                    "id"
                  ]
                },
                {
                  "required": [
                    "profile"
                  ]
                }
              ]
            }
          },
          "else": {
            "required": [
              "id"
            ]
          }
        },
        {
          "if": {
            "properties": {
              "kind": {
                "enum": [
                  "phraseTemplate",
                  "clipCandidate",
                  "clipChoiceGroup",
                  "roleDefinition"
                ]
              }
            },
            "required": [
              "kind"
            ]
          },
          "then": {
            "required": [
              "profile"
            ]
          },
          "else": {
            "not": {
              "required": [
                "profile"
              ]
            }
          }
        }
      ],
      "description": "Stable target by Core ID or profile-local scoped ID; song is the only ID-less target. No array indexes or mutable names as locators."
    },
    "localizationEntry": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "target": {
          "$ref": "#/$defs/legacy33/$defs/localizationTarget"
        },
        "field": {
          "type": "string",
          "minLength": 1,
          "description": "Exact allowed source text field for this target kind (see normative matrix). No arbitrary path or musical value fields."
        },
        "values": {
          "$ref": "#/$defs/legacy33/$defs/languageMap32"
        }
      },
      "required": [
        "target",
        "field",
        "values"
      ],
      "description": "Independent translations for one stable source field. Original source text remains authoritative as fallback."
    },
    "localizationData": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "entries": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/legacy33/$defs/localizationEntry"
          }
        }
      },
      "required": [
        "entries"
      ],
      "description": "Language-map translations indexed by stable kind/id/field, never by names or array positions."
    },
    "genre": {
      "type": "object",
      "description": "One song-local open genre tag. The label is authored Unicode text and not a predefined controlled taxonomy; ID is stable for metadata merges and localization.",
      "properties": {
        "id": {
          "$ref": "#/$defs/legacy33/$defs/id",
          "description": "Stable song-local ID unique among all Core objects."
        },
        "name": {
          "type": "string",
          "minLength": 1,
          "description": "Original Unicode genre label, never normalized or rewritten during import."
        },
        "externalUri": {
          "type": "string",
          "minLength": 1,
          "format": "uri",
          "description": "Optional external taxonomy URI hint; never authoritative for a local genre label, and never auto-dereferenced."
        }
      },
      "required": [
        "id",
        "name"
      ],
      "additionalProperties": false
    }
  }
}
```

<a id="def-opaquedocumentid"></a>
## opaqueDocumentId

Stable URI or UUID-style identifier for a document lineage. Compared as exact Unicode text; never fetched.

No direct `properties` table (object may be an enum, scalar, array or a composition).

### Exact JSON Schema object

```json
{
  "type": "string",
  "minLength": 1,
  "description": "Stable URI or UUID-style identifier for a document lineage. Compared as exact Unicode text; never fetched."
}
```

<a id="def-revisionref"></a>
## revisionRef

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `documentId` | `#/$defs/opaqueDocumentId` | Yes |  |
| `revisionId` | `#/$defs/opaqueDocumentId` | Yes |  |
| `sha256` | `#/$defs/sha256` | No/conditional |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "documentId": {
      "$ref": "#/$defs/opaqueDocumentId"
    },
    "revisionId": {
      "$ref": "#/$defs/opaqueDocumentId"
    },
    "sha256": {
      "$ref": "#/$defs/sha256"
    }
  },
  "required": [
    "documentId",
    "revisionId"
  ],
  "additionalProperties": false
}
```

<a id="def-software"></a>
## software

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `name` | `string` | Yes |  |
| `version` | `string` | No/conditional |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "name": {
      "type": "string",
      "minLength": 1
    },
    "version": {
      "type": "string",
      "minLength": 1
    }
  },
  "required": [
    "name"
  ],
  "additionalProperties": false
}
```

<a id="def-documentinfo"></a>
## documentInfo

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `id` | `#/$defs/opaqueDocumentId` | Yes |  |
| `revisionId` | `#/$defs/opaqueDocumentId` | Yes |  |
| `parents` | `array<#/$defs/revisionRef>` | No/conditional |  |
| `createdBy` | `#/$defs/software` | No/conditional |  |
| `modifiedBy` | `#/$defs/software` | No/conditional |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/opaqueDocumentId"
    },
    "revisionId": {
      "$ref": "#/$defs/opaqueDocumentId"
    },
    "parents": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/revisionRef"
      },
      "uniqueItems": true
    },
    "createdBy": {
      "$ref": "#/$defs/software"
    },
    "modifiedBy": {
      "$ref": "#/$defs/software"
    }
  },
  "required": [
    "id",
    "revisionId"
  ],
  "additionalProperties": false
}
```

<a id="def-key"></a>
## key

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `state` | `enum ["tonal", "atonal", "unspecified"]` | Yes |  |
| `tonic` | `#/$defs/spelledPitchClass` | No/conditional |  |
| `mode` | `string` | No/conditional | Authored mode identifier. Canonical recognized values include major, minor, dorian, phrygian, lydian, mixolydian, locrian. Unknown values are ... |
| `label` | `string` | No/conditional |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "state": {
      "enum": [
        "tonal",
        "atonal",
        "unspecified"
      ]
    },
    "tonic": {
      "$ref": "#/$defs/spelledPitchClass"
    },
    "mode": {
      "type": "string",
      "minLength": 1,
      "description": "Authored mode identifier. Canonical recognized values include major, minor, dorian, phrygian, lydian, mixolydian, locrian. Unknown values are preserved, never converted to major/minor."
    },
    "label": {
      "type": "string"
    }
  },
  "required": [
    "state"
  ],
  "additionalProperties": false,
  "allOf": [
    {
      "if": {
        "properties": {
          "state": {
            "const": "tonal"
          }
        },
        "required": [
          "state"
        ]
      },
      "then": {
        "required": [
          "tonic",
          "mode"
        ]
      },
      "else": {
        "not": {
          "anyOf": [
            {
              "required": [
                "tonic"
              ]
            },
            {
              "required": [
                "mode"
              ]
            }
          ]
        }
      }
    }
  ]
}
```

<a id="def-keychange"></a>
## keyChange

A change after tick zero; initial key is stored only at song.key. Change at tick 0 is forbidden to prevent dual authority.

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `id` | `#/$defs/id` | Yes |  |
| `at` | `#/$defs/positive` | Yes |  |
| `key` | `#/$defs/key` | Yes |  |
| `label` | `string` | No/conditional |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "at": {
      "$ref": "#/$defs/positive"
    },
    "key": {
      "$ref": "#/$defs/key"
    },
    "label": {
      "type": "string"
    }
  },
  "required": [
    "id",
    "at",
    "key"
  ],
  "additionalProperties": false,
  "description": "A change after tick zero; initial key is stored only at song.key. Change at tick 0 is forbidden to prevent dual authority."
}
```

<a id="def-scaledefinition"></a>
## scaleDefinition

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `id` | `#/$defs/id` | Yes |  |
| `tonic` | `#/$defs/spelledPitchClass` | Yes |  |
| `intervals` | `array<integer>` | Yes |  |
| `label` | `string` | No/conditional |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "tonic": {
      "$ref": "#/$defs/spelledPitchClass"
    },
    "intervals": {
      "type": "array",
      "items": {
        "type": "integer",
        "minimum": 0,
        "maximum": 11
      },
      "minItems": 1,
      "maxItems": 12,
      "uniqueItems": true,
      "contains": {
        "const": 0
      }
    },
    "label": {
      "type": "string"
    }
  },
  "required": [
    "id",
    "tonic",
    "intervals"
  ],
  "additionalProperties": false
}
```

<a id="def-scaletarget"></a>
## scaleTarget

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `type` | `enum ["section", "track", "clip", "chord", "note"]` | Yes |  |
| `id` | `#/$defs/id` | Yes |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "type": {
      "enum": [
        "section",
        "track",
        "clip",
        "chord",
        "note"
      ]
    },
    "id": {
      "$ref": "#/$defs/id"
    }
  },
  "required": [
    "type",
    "id"
  ],
  "additionalProperties": false
}
```

<a id="def-mood"></a>
## mood

Authored descriptive mood tag; not a generator preset or a probability.

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `id` | `#/$defs/id` | Yes | Stable song-local ID unique among all Core objects. |
| `name` | `string` | Yes | Original Unicode genre label, never normalized or rewritten during import. |
| `externalUri` | `string` | No/conditional | Optional external vocabulary URI hint; never authoritative for the authored mood name and never auto-dereferenced. |

### Exact JSON Schema object

```json
{
  "type": "object",
  "description": "Authored descriptive mood tag; not a generator preset or a probability.",
  "properties": {
    "id": {
      "$ref": "#/$defs/id",
      "description": "Stable song-local ID unique among all Core objects."
    },
    "name": {
      "type": "string",
      "minLength": 1,
      "description": "Original Unicode genre label, never normalized or rewritten during import."
    },
    "externalUri": {
      "type": "string",
      "minLength": 1,
      "format": "uri",
      "description": "Optional external vocabulary URI hint; never authoritative for the authored mood name and never auto-dereferenced."
    }
  },
  "required": [
    "id",
    "name"
  ],
  "additionalProperties": false
}
```

<a id="def-rightsstatement"></a>
## rightsStatement

Authored rights statement only; no rights or permissions are inferred or granted by the format.

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `notice` | `string` | No/conditional |  |
| `licenseUri` | `string` | No/conditional |  |
| `rightsHolderIds` | `array<#/$defs/id>` | No/conditional |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "notice": {
      "type": "string"
    },
    "licenseUri": {
      "type": "string",
      "minLength": 1
    },
    "rightsHolderIds": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/id"
      },
      "uniqueItems": true
    }
  },
  "required": [],
  "additionalProperties": false,
  "description": "Authored rights statement only; no rights or permissions are inferred or granted by the format.",
  "minProperties": 1
}
```

<a id="def-grooveintent"></a>
## grooveIntent

Descriptive generation intent only. Never re-apply to already stored notes. unitTicks is one unswung subdivision; two subdivisions form a pair.

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `name` | `string` | No/conditional |  |
| `unitTicks` | `#/$defs/positive` | No/conditional |  |
| `longWeight` | `integer` | No/conditional |  |
| `shortWeight` | `integer` | No/conditional |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "name": {
      "type": "string"
    },
    "unitTicks": {
      "$ref": "#/$defs/positive"
    },
    "longWeight": {
      "type": "integer",
      "minimum": 1,
      "maximum": 1000000
    },
    "shortWeight": {
      "type": "integer",
      "minimum": 1,
      "maximum": 1000000
    }
  },
  "required": [],
  "additionalProperties": false,
  "description": "Descriptive generation intent only. Never re-apply to already stored notes. unitTicks is one unswung subdivision; two subdivisions form a pair.",
  "minProperties": 1,
  "dependentRequired": {
    "unitTicks": [
      "longWeight",
      "shortWeight"
    ],
    "longWeight": [
      "unitTicks",
      "shortWeight"
    ],
    "shortWeight": [
      "unitTicks",
      "longWeight"
    ]
  }
}
```

<a id="def-generationintent"></a>
## generationIntent

Portable description of intent, not a promise to reproduce an algorithm. Does not change song.genres or song.moods.

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `genreNames` | `array<string>` | No/conditional |  |
| `moodNames` | `array<string>` | No/conditional |  |
| `groove` | `#/$defs/grooveIntent` | No/conditional |  |
| `prompt` | `string` | No/conditional |  |
| `seed` | `string` | No/conditional |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "genreNames": {
      "type": "array",
      "items": {
        "type": "string",
        "minLength": 1
      }
    },
    "moodNames": {
      "type": "array",
      "items": {
        "type": "string",
        "minLength": 1
      }
    },
    "groove": {
      "$ref": "#/$defs/grooveIntent"
    },
    "prompt": {
      "type": "string"
    },
    "seed": {
      "type": "string"
    }
  },
  "required": [],
  "additionalProperties": false,
  "description": "Portable description of intent, not a promise to reproduce an algorithm. Does not change song.genres or song.moods."
}
```

<a id="def-relativephrases"></a>
## relativePhrases

Standard optional Core object under root version 4.0.0, not an extension. Current relationships must be consistent with saved Core; loading never performs editing or generation.

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `status` | `enum ["current", "stale", "unverified"]` | Yes |  |
| `dependencies` | `#/$defs/dependencies` | Yes |  |
| `assignments` | `array<#/$defs/relativeAssignment>` | Yes |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "status": {
      "enum": [
        "current",
        "stale",
        "unverified"
      ]
    },
    "dependencies": {
      "$ref": "#/$defs/dependencies"
    },
    "assignments": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/relativeAssignment"
      }
    }
  },
  "required": [
    "status",
    "dependencies",
    "assignments"
  ],
  "additionalProperties": false,
  "description": "Standard optional Core object under root version 4.0.0, not an extension. Current relationships must be consistent with saved Core; loading never performs editing or generation."
}
```

<a id="def-generation"></a>
## generation

Standard optional Core object under root version 4.0.0, not an extension. Current relationships must be consistent with saved Core; loading never performs editing or generation.

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `status` | `enum ["current", "stale", "unverified"]` | Yes |  |
| `dependencies` | `#/$defs/dependencies` | Yes |  |
| `processes` | `array<#/$defs/generationProcess>` | Yes |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "status": {
      "enum": [
        "current",
        "stale",
        "unverified"
      ]
    },
    "dependencies": {
      "$ref": "#/$defs/dependencies"
    },
    "processes": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/generationProcess"
      }
    }
  },
  "required": [
    "status",
    "dependencies",
    "processes"
  ],
  "additionalProperties": false,
  "description": "Standard optional Core object under root version 4.0.0, not an extension. Current relationships must be consistent with saved Core; loading never performs editing or generation."
}
```

<a id="def-presentation"></a>
## presentation

Standard optional Core object under root version 4.0.0, not an extension. Current relationships must be consistent with saved Core; loading never performs editing or generation.

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `status` | `enum ["current", "stale", "unverified"]` | Yes |  |
| `dependencies` | `#/$defs/dependencies` | Yes |  |
| `roleDefinitions` | `array<#/$defs/roleDefinition>` | Yes |  |
| `sectionRoleAssignments` | `object` | Yes |  |
| `appearance` | `object` | Yes |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "status": {
      "enum": [
        "current",
        "stale",
        "unverified"
      ]
    },
    "dependencies": {
      "$ref": "#/$defs/dependencies"
    },
    "roleDefinitions": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/roleDefinition"
      }
    },
    "sectionRoleAssignments": {
      "type": "object",
      "propertyNames": {
        "$ref": "#/$defs/id"
      },
      "additionalProperties": {
        "$ref": "#/$defs/id"
      }
    },
    "appearance": {
      "type": "object",
      "properties": {
        "roleColors": {
          "$ref": "#/$defs/roleColorMap"
        },
        "customRoleColors": {
          "$ref": "#/$defs/customRoleColorMap"
        },
        "objectColors": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/objectColor"
          }
        }
      },
      "required": [
        "roleColors",
        "customRoleColors",
        "objectColors"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "status",
    "dependencies",
    "roleDefinitions",
    "sectionRoleAssignments",
    "appearance"
  ],
  "additionalProperties": false,
  "description": "Standard optional Core object under root version 4.0.0, not an extension. Current relationships must be consistent with saved Core; loading never performs editing or generation."
}
```

<a id="def-phraselibrary"></a>
## phraseLibrary

Standard optional Core object under root version 4.0.0, not an extension. Current relationships must be consistent with saved Core; loading never performs editing or generation.

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `status` | `enum ["current", "stale", "unverified"]` | Yes |  |
| `dependencies` | `#/$defs/dependencies` | Yes |  |
| `templates` | `array<#/$defs/phraseTemplate>` | Yes |  |
| `instances` | `array<#/$defs/phraseInstance>` | Yes |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "status": {
      "enum": [
        "current",
        "stale",
        "unverified"
      ]
    },
    "dependencies": {
      "$ref": "#/$defs/dependencies"
    },
    "templates": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/phraseTemplate"
      }
    },
    "instances": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/phraseInstance"
      }
    }
  },
  "required": [
    "status",
    "dependencies",
    "templates",
    "instances"
  ],
  "additionalProperties": false,
  "description": "Standard optional Core object under root version 4.0.0, not an extension. Current relationships must be consistent with saved Core; loading never performs editing or generation."
}
```

<a id="def-clipchoices"></a>
## clipChoices

Standard optional Core object under root version 4.0.0, not an extension. Current relationships must be consistent with saved Core; loading never performs editing or generation.

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `status` | `enum ["current", "stale", "unverified"]` | Yes |  |
| `dependencies` | `#/$defs/dependencies` | Yes |  |
| `groups` | `array<#/$defs/clipChoiceGroup>` | Yes |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "status": {
      "enum": [
        "current",
        "stale",
        "unverified"
      ]
    },
    "dependencies": {
      "$ref": "#/$defs/dependencies"
    },
    "groups": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/clipChoiceGroup"
      }
    }
  },
  "required": [
    "status",
    "dependencies",
    "groups"
  ],
  "additionalProperties": false,
  "description": "Standard optional Core object under root version 4.0.0, not an extension. Current relationships must be consistent with saved Core; loading never performs editing or generation."
}
```

<a id="def-localization"></a>
## localization

Standard optional Core object under root version 4.0.0, not an extension. Current relationships must be consistent with saved Core; loading never performs editing or generation.

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `status` | `enum ["current", "stale", "unverified"]` | Yes |  |
| `dependencies` | `#/$defs/dependencies` | Yes |  |
| `entries` | `array<#/$defs/localizationEntry>` | Yes |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "status": {
      "enum": [
        "current",
        "stale",
        "unverified"
      ]
    },
    "dependencies": {
      "$ref": "#/$defs/dependencies"
    },
    "entries": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/localizationEntry"
      }
    }
  },
  "required": [
    "status",
    "dependencies",
    "entries"
  ],
  "description": "Standard optional Core object under root version 4.0.0, not an extension. Current relationships must be consistent with saved Core; loading never performs editing or generation."
}
```

<a id="def-corephrasesourcenote"></a>
## corePhraseSourceNote

Template-local source note for phrase materialization. It carries the same note-local 3.5 properties as concrete notes. It is not performed by itself; concrete track notes remain the saved playback events.

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `id` | `#/$defs/id` | Yes |  |
| `start` | `#/$defs/signed` | Yes |  |
| `duration` | `#/$defs/positive` | Yes | Positive note gate in ticks, not the guaranteed audible duration of a one-shot percussion sample. |
| `pitch` | `#/$defs/pitch` | No/conditional |  |
| `soundSlotId` | `#/$defs/id` | No/conditional | Document-local Sound Slot ID. Distinct events and IDs stay distinct even if several slots share a MIDI key; a renderer decides the acoustic ti... |
| `velocity` | `integer` | No/conditional | Optional template note-on velocity, 1–127. Applied only by an explicit materialization/update according to instance.velocityMode; never a perf... |
| `enabled` | `boolean` | No/conditional | Optional note-local enable state. Omitted means enabled. False preserves the note but suppresses scheduling/playback; it is distinct from prob... |
| `releaseVelocity` | `integer` | No/conditional | Optional MIDI Note Off/release velocity, 0-127. Omit when unspecified; readers must not invent and write back a default. |
| `probability` | `number` | No/conditional | Optional note-playback probability from 0.0 to 1.0. Omitted means 1.0. Random sequence identity is not standardized; materialize notes for det... |
| `velocityDeviation` | `integer` | No/conditional | Optional note-local velocity variation endpoint relative to velocity. Requires velocity. Semantic rule: velocity + velocityDeviation must rema... |
| `pitchRole` | `enum ["musical", "fixedTrigger"]` | No/conditional | Meaning of a pitch note. musical participates in pitch/harmony/transpose operations; fixedTrigger is an exact MIDI key trigger (for example a ... |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "start": {
      "$ref": "#/$defs/signed"
    },
    "duration": {
      "$ref": "#/$defs/positive",
      "description": "Positive note gate in ticks, not the guaranteed audible duration of a one-shot percussion sample."
    },
    "pitch": {
      "$ref": "#/$defs/pitch"
    },
    "soundSlotId": {
      "$ref": "#/$defs/id",
      "description": "Document-local Sound Slot ID. Distinct events and IDs stay distinct even if several slots share a MIDI key; a renderer decides the acoustic timbre."
    },
    "velocity": {
      "type": "integer",
      "minimum": 1,
      "maximum": 127,
      "description": "Optional template note-on velocity, 1–127. Applied only by an explicit materialization/update according to instance.velocityMode; never a performed event by itself."
    },
    "enabled": {
      "type": "boolean",
      "default": true,
      "description": "Optional note-local enable state. Omitted means enabled. False preserves the note but suppresses scheduling/playback; it is distinct from probability=0."
    },
    "releaseVelocity": {
      "type": "integer",
      "minimum": 0,
      "maximum": 127,
      "description": "Optional MIDI Note Off/release velocity, 0-127. Omit when unspecified; readers must not invent and write back a default."
    },
    "probability": {
      "type": "number",
      "minimum": 0,
      "maximum": 1,
      "default": 1,
      "description": "Optional note-playback probability from 0.0 to 1.0. Omitted means 1.0. Random sequence identity is not standardized; materialize notes for deterministic interchange."
    },
    "velocityDeviation": {
      "type": "integer",
      "minimum": -126,
      "maximum": 126,
      "default": 0,
      "description": "Optional note-local velocity variation endpoint relative to velocity. Requires velocity. Semantic rule: velocity + velocityDeviation must remain within 1..127. Omitted means 0."
    },
    "pitchRole": {
      "enum": [
        "musical",
        "fixedTrigger"
      ],
      "default": "musical",
      "description": "Meaning of a pitch note. musical participates in pitch/harmony/transpose operations; fixedTrigger is an exact MIDI key trigger (for example a keyswitch) and is never transposed or used as musical-pitch evidence. Allowed only on pitch notes."
    }
  },
  "required": [
    "id",
    "start",
    "duration"
  ],
  "additionalProperties": false,
  "oneOf": [
    {
      "required": [
        "pitch"
      ],
      "not": {
        "required": [
          "soundSlotId"
        ]
      }
    },
    {
      "required": [
        "soundSlotId"
      ],
      "not": {
        "required": [
          "pitch"
        ]
      }
    }
  ],
  "description": "Template-local source note for phrase materialization. It carries the same note-local 3.5 properties as concrete notes. It is not performed by itself; concrete track notes remain the saved playback events.",
  "dependentRequired": {
    "velocityDeviation": [
      "velocity"
    ]
  },
  "allOf": [
    {
      "if": {
        "required": [
          "soundSlotId"
        ]
      },
      "then": {
        "not": {
          "required": [
            "pitchRole"
          ]
        }
      }
    }
  ]
}
```

<a id="def-provenancesource"></a>
## provenanceSource

Historical source; hashes refer to exact source bytes, not the current document. No automatic retrieval.

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `format` | `string` | No/conditional |  |
| `version` | `string` | No/conditional |  |
| `sha256` | `#/$defs/sha256` | No/conditional |  |
| `uri` | `string` | No/conditional |  |
| `documentId` | `#/$defs/opaqueDocumentId` | No/conditional |  |
| `revisionId` | `#/$defs/opaqueDocumentId` | No/conditional |  |
| `resourceId` | `#/$defs/id` | No/conditional |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "format": {
      "type": "string",
      "minLength": 1
    },
    "version": {
      "type": "string",
      "minLength": 1
    },
    "sha256": {
      "$ref": "#/$defs/sha256"
    },
    "uri": {
      "type": "string",
      "minLength": 1
    },
    "documentId": {
      "$ref": "#/$defs/opaqueDocumentId"
    },
    "revisionId": {
      "$ref": "#/$defs/opaqueDocumentId"
    },
    "resourceId": {
      "$ref": "#/$defs/id"
    }
  },
  "required": [],
  "additionalProperties": false,
  "description": "Historical source; hashes refer to exact source bytes, not the current document. No automatic retrieval.",
  "minProperties": 1,
  "dependentRequired": {
    "revisionId": [
      "documentId"
    ]
  }
}
```

<a id="def-provenancerecord"></a>
## provenanceRecord

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `id` | `#/$defs/id` | Yes |  |
| `action` | `enum ["create", "import", "conversion", "edit", "transpose", "merge", "generation", "other"]` | Yes |  |
| `description` | `string` | No/conditional |  |
| `tool` | `#/$defs/software` | No/conditional |  |
| `sources` | `array<#/$defs/provenanceSource>` | No/conditional |  |
| `semitones` | `integer` | No/conditional |  |
| `beforeKey` | `#/$defs/key` | No/conditional |  |
| `afterKey` | `#/$defs/key` | No/conditional |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "action": {
      "enum": [
        "create",
        "import",
        "conversion",
        "edit",
        "transpose",
        "merge",
        "generation",
        "other"
      ]
    },
    "description": {
      "type": "string"
    },
    "tool": {
      "$ref": "#/$defs/software"
    },
    "sources": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/provenanceSource"
      }
    },
    "semitones": {
      "type": "integer",
      "minimum": -127,
      "maximum": 127
    },
    "beforeKey": {
      "$ref": "#/$defs/key"
    },
    "afterKey": {
      "$ref": "#/$defs/key"
    }
  },
  "required": [
    "id",
    "action"
  ],
  "additionalProperties": false,
  "allOf": [
    {
      "if": {
        "not": {
          "properties": {
            "action": {
              "const": "transpose"
            }
          },
          "required": [
            "action"
          ]
        }
      },
      "then": {
        "not": {
          "required": [
            "semitones"
          ]
        }
      }
    }
  ]
}
```

<a id="def-provenance"></a>
## provenance

Non-executable historical assertions; not composer credits and not a substitute for current metadata. Does not prove authorship or operation correctness.

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `records` | `array<#/$defs/provenanceRecord>` | Yes |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "records": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/provenanceRecord"
      }
    }
  },
  "required": [
    "records"
  ],
  "additionalProperties": false,
  "description": "Non-executable historical assertions; not composer credits and not a substitute for current metadata. Does not prove authorship or operation correctness."
}
```

<a id="def-midichannel"></a>
## midiChannel

Human-readable MIDI 1.0 channel number 1..16. Wire status-nibble channel = value - 1.

No direct `properties` table (object may be an enum, scalar, array or a composition).

### Exact JSON Schema object

```json
{
  "type": "integer",
  "minimum": 1,
  "maximum": 16,
  "description": "Human-readable MIDI 1.0 channel number 1..16. Wire status-nibble channel = value - 1."
}
```

<a id="def-midibus"></a>
## midiBus

Document-local logical MIDI destination. Each bus has its own MIDI channel namespace. It is not a physical OS/USB/DAW port binding.

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `id` | `#/$defs/id` | Yes |  |
| `name` | `string` | Yes |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "description": "Document-local logical MIDI destination. Each bus has its own MIDI channel namespace. It is not a physical OS/USB/DAW port binding.",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "name": {
      "type": "string"
    }
  },
  "required": [
    "id",
    "name"
  ],
  "additionalProperties": false
}
```

<a id="def-midi"></a>
## midi

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `buses` | `array<#/$defs/midiBus>` | Yes |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "buses": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/midiBus"
      }
    }
  },
  "required": [
    "buses"
  ],
  "additionalProperties": false
}
```

<a id="def-mpesettings"></a>
## mpeSettings

Semantic MPE zone declaration. Lower-zone master is channel 1 and upper-zone master is channel 16; member channels are derived contiguously from memberChannelCount.

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `zone` | `enum ["lower", "upper"]` | Yes |  |
| `memberChannelCount` | `integer` | Yes |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "description": "Semantic MPE zone declaration. Lower-zone master is channel 1 and upper-zone master is channel 16; member channels are derived contiguously from memberChannelCount.",
  "properties": {
    "zone": {
      "enum": [
        "lower",
        "upper"
      ]
    },
    "memberChannelCount": {
      "type": "integer",
      "minimum": 1,
      "maximum": 15
    }
  },
  "required": [
    "zone",
    "memberChannelCount"
  ],
  "additionalProperties": false
}
```

<a id="def-trackmidi"></a>
## trackMidi

Optional MIDI channel/routing interpretation for a track. busId is a logical OSTF bus, never a physical MIDI port.

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `busId` | `#/$defs/id` | No/conditional |  |
| `mode` | `enum ["singleChannel", "multiChannel", "mpe"]` | Yes |  |
| `channel` | `#/$defs/midiChannel` | No/conditional |  |
| `mpe` | `#/$defs/mpeSettings` | No/conditional |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "description": "Optional MIDI channel/routing interpretation for a track. busId is a logical OSTF bus, never a physical MIDI port.",
  "properties": {
    "busId": {
      "$ref": "#/$defs/id"
    },
    "mode": {
      "enum": [
        "singleChannel",
        "multiChannel",
        "mpe"
      ]
    },
    "channel": {
      "$ref": "#/$defs/midiChannel"
    },
    "mpe": {
      "$ref": "#/$defs/mpeSettings"
    }
  },
  "required": [
    "mode"
  ],
  "additionalProperties": false,
  "allOf": [
    {
      "if": {
        "properties": {
          "mode": {
            "const": "singleChannel"
          }
        },
        "required": [
          "mode"
        ]
      },
      "then": {
        "required": [
          "channel"
        ],
        "not": {
          "required": [
            "mpe"
          ]
        }
      }
    },
    {
      "if": {
        "properties": {
          "mode": {
            "const": "multiChannel"
          }
        },
        "required": [
          "mode"
        ]
      },
      "then": {
        "not": {
          "anyOf": [
            {
              "required": [
                "channel"
              ]
            },
            {
              "required": [
                "mpe"
              ]
            }
          ]
        }
      }
    },
    {
      "if": {
        "properties": {
          "mode": {
            "const": "mpe"
          }
        },
        "required": [
          "mode"
        ]
      },
      "then": {
        "required": [
          "mpe"
        ],
        "not": {
          "required": [
            "channel"
          ]
        }
      }
    }
  ]
}
```

<a id="def-controlchangeevent"></a>
## controlChangeEvent

MIDI 1.0 Control Change. Controllers 120..127 use channelMode instead.

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `id` | `#/$defs/id` | Yes |  |
| `start` | `#/$defs/signed` | Yes |  |
| `order` | `#/$defs/signed` | No/conditional | Same-tick ordering key. Omitted means 1. Note Off has implicit order 0 and Note On implicit order 2; ties are resolved by the normative orderi... |
| `channel` | `#/$defs/midiChannel` | No/conditional |  |
| `type` | `const "controlChange"` | Yes |  |
| `targetNoteId` | `#/$defs/id` | No/conditional | Optional semantic association with an existing concrete note. It does not replace channel/pitch wire semantics. |
| `controller` | `integer` | Yes |  |
| `value` | `integer` | Yes |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "description": "MIDI 1.0 Control Change. Controllers 120..127 use channelMode instead.",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "start": {
      "$ref": "#/$defs/signed"
    },
    "order": {
      "$ref": "#/$defs/signed",
      "default": 1,
      "description": "Same-tick ordering key. Omitted means 1. Note Off has implicit order 0 and Note On implicit order 2; ties are resolved by the normative ordering rules."
    },
    "channel": {
      "$ref": "#/$defs/midiChannel"
    },
    "type": {
      "const": "controlChange"
    },
    "targetNoteId": {
      "$ref": "#/$defs/id",
      "description": "Optional semantic association with an existing concrete note. It does not replace channel/pitch wire semantics."
    },
    "controller": {
      "type": "integer",
      "minimum": 0,
      "maximum": 119
    },
    "value": {
      "type": "integer",
      "minimum": 0,
      "maximum": 127
    }
  },
  "required": [
    "id",
    "start",
    "type",
    "controller",
    "value"
  ],
  "additionalProperties": false
}
```

<a id="def-channelmodeevent"></a>
## channelModeEvent

MIDI 1.0 Channel Mode message represented separately from ordinary Control Change.

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `id` | `#/$defs/id` | Yes |  |
| `start` | `#/$defs/signed` | Yes |  |
| `order` | `#/$defs/signed` | No/conditional | Same-tick ordering key. Omitted means 1. Note Off has implicit order 0 and Note On implicit order 2; ties are resolved by the normative orderi... |
| `channel` | `#/$defs/midiChannel` | No/conditional |  |
| `type` | `const "channelMode"` | Yes |  |
| `controller` | `integer` | Yes |  |
| `value` | `integer` | Yes |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "description": "MIDI 1.0 Channel Mode message represented separately from ordinary Control Change.",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "start": {
      "$ref": "#/$defs/signed"
    },
    "order": {
      "$ref": "#/$defs/signed",
      "default": 1,
      "description": "Same-tick ordering key. Omitted means 1. Note Off has implicit order 0 and Note On implicit order 2; ties are resolved by the normative ordering rules."
    },
    "channel": {
      "$ref": "#/$defs/midiChannel"
    },
    "type": {
      "const": "channelMode"
    },
    "controller": {
      "type": "integer",
      "minimum": 120,
      "maximum": 127
    },
    "value": {
      "type": "integer",
      "minimum": 0,
      "maximum": 127
    }
  },
  "required": [
    "id",
    "start",
    "type",
    "controller",
    "value"
  ],
  "additionalProperties": false
}
```

<a id="def-programchangeevent"></a>
## programChangeEvent

MIDI 1.0 Program Change using the wire data value 0..127. UI may display 1..128.

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `id` | `#/$defs/id` | Yes |  |
| `start` | `#/$defs/signed` | Yes |  |
| `order` | `#/$defs/signed` | No/conditional | Same-tick ordering key. Omitted means 1. Note Off has implicit order 0 and Note On implicit order 2; ties are resolved by the normative orderi... |
| `channel` | `#/$defs/midiChannel` | No/conditional |  |
| `type` | `const "programChange"` | Yes |  |
| `program` | `integer` | Yes |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "description": "MIDI 1.0 Program Change using the wire data value 0..127. UI may display 1..128.",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "start": {
      "$ref": "#/$defs/signed"
    },
    "order": {
      "$ref": "#/$defs/signed",
      "default": 1,
      "description": "Same-tick ordering key. Omitted means 1. Note Off has implicit order 0 and Note On implicit order 2; ties are resolved by the normative ordering rules."
    },
    "channel": {
      "$ref": "#/$defs/midiChannel"
    },
    "type": {
      "const": "programChange"
    },
    "program": {
      "type": "integer",
      "minimum": 0,
      "maximum": 127
    }
  },
  "required": [
    "id",
    "start",
    "type",
    "program"
  ],
  "additionalProperties": false
}
```

<a id="def-pitchbendevent"></a>
## pitchBendEvent

MIDI 1.0 14-bit Pitch Bend Change. Bend range is receiver state/RPN data, not encoded in value14.

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `id` | `#/$defs/id` | Yes |  |
| `start` | `#/$defs/signed` | Yes |  |
| `order` | `#/$defs/signed` | No/conditional | Same-tick ordering key. Omitted means 1. Note Off has implicit order 0 and Note On implicit order 2; ties are resolved by the normative orderi... |
| `channel` | `#/$defs/midiChannel` | No/conditional |  |
| `type` | `const "pitchBend"` | Yes |  |
| `targetNoteId` | `#/$defs/id` | No/conditional | Optional semantic association with an existing concrete note. It does not replace channel/pitch wire semantics. |
| `value14` | `integer` | Yes | Raw MIDI 1.0 14-bit pitch-bend value; center is 8192. |

### Exact JSON Schema object

```json
{
  "type": "object",
  "description": "MIDI 1.0 14-bit Pitch Bend Change. Bend range is receiver state/RPN data, not encoded in value14.",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "start": {
      "$ref": "#/$defs/signed"
    },
    "order": {
      "$ref": "#/$defs/signed",
      "default": 1,
      "description": "Same-tick ordering key. Omitted means 1. Note Off has implicit order 0 and Note On implicit order 2; ties are resolved by the normative ordering rules."
    },
    "channel": {
      "$ref": "#/$defs/midiChannel"
    },
    "type": {
      "const": "pitchBend"
    },
    "targetNoteId": {
      "$ref": "#/$defs/id",
      "description": "Optional semantic association with an existing concrete note. It does not replace channel/pitch wire semantics."
    },
    "value14": {
      "type": "integer",
      "minimum": 0,
      "maximum": 16383,
      "description": "Raw MIDI 1.0 14-bit pitch-bend value; center is 8192."
    }
  },
  "required": [
    "id",
    "start",
    "type",
    "value14"
  ],
  "additionalProperties": false
}
```

<a id="def-channelpressureevent"></a>
## channelPressureEvent

MIDI 1.0 Channel Pressure (channel aftertouch).

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `id` | `#/$defs/id` | Yes |  |
| `start` | `#/$defs/signed` | Yes |  |
| `order` | `#/$defs/signed` | No/conditional | Same-tick ordering key. Omitted means 1. Note Off has implicit order 0 and Note On implicit order 2; ties are resolved by the normative orderi... |
| `channel` | `#/$defs/midiChannel` | No/conditional |  |
| `type` | `const "channelPressure"` | Yes |  |
| `targetNoteId` | `#/$defs/id` | No/conditional | Optional semantic association with an existing concrete note. It does not replace channel/pitch wire semantics. |
| `value` | `integer` | Yes |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "description": "MIDI 1.0 Channel Pressure (channel aftertouch).",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "start": {
      "$ref": "#/$defs/signed"
    },
    "order": {
      "$ref": "#/$defs/signed",
      "default": 1,
      "description": "Same-tick ordering key. Omitted means 1. Note Off has implicit order 0 and Note On implicit order 2; ties are resolved by the normative ordering rules."
    },
    "channel": {
      "$ref": "#/$defs/midiChannel"
    },
    "type": {
      "const": "channelPressure"
    },
    "targetNoteId": {
      "$ref": "#/$defs/id",
      "description": "Optional semantic association with an existing concrete note. It does not replace channel/pitch wire semantics."
    },
    "value": {
      "type": "integer",
      "minimum": 0,
      "maximum": 127
    }
  },
  "required": [
    "id",
    "start",
    "type",
    "value"
  ],
  "additionalProperties": false
}
```

<a id="def-polypressureevent"></a>
## polyPressureEvent

MIDI 1.0 Polyphonic Key Pressure (poly aftertouch).

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `id` | `#/$defs/id` | Yes |  |
| `start` | `#/$defs/signed` | Yes |  |
| `order` | `#/$defs/signed` | No/conditional | Same-tick ordering key. Omitted means 1. Note Off has implicit order 0 and Note On implicit order 2; ties are resolved by the normative orderi... |
| `channel` | `#/$defs/midiChannel` | No/conditional |  |
| `type` | `const "polyPressure"` | Yes |  |
| `targetNoteId` | `#/$defs/id` | No/conditional | Optional semantic association with an existing concrete note. It does not replace channel/pitch wire semantics. |
| `pitch` | `#/$defs/pitch` | Yes |  |
| `value` | `integer` | Yes |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "description": "MIDI 1.0 Polyphonic Key Pressure (poly aftertouch).",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "start": {
      "$ref": "#/$defs/signed"
    },
    "order": {
      "$ref": "#/$defs/signed",
      "default": 1,
      "description": "Same-tick ordering key. Omitted means 1. Note Off has implicit order 0 and Note On implicit order 2; ties are resolved by the normative ordering rules."
    },
    "channel": {
      "$ref": "#/$defs/midiChannel"
    },
    "type": {
      "const": "polyPressure"
    },
    "targetNoteId": {
      "$ref": "#/$defs/id",
      "description": "Optional semantic association with an existing concrete note. It does not replace channel/pitch wire semantics."
    },
    "pitch": {
      "$ref": "#/$defs/pitch"
    },
    "value": {
      "type": "integer",
      "minimum": 0,
      "maximum": 127
    }
  },
  "required": [
    "id",
    "start",
    "type",
    "pitch",
    "value"
  ],
  "additionalProperties": false
}
```

<a id="def-midievent"></a>
## midiEvent

No direct `properties` table (object may be an enum, scalar, array or a composition).

### Exact JSON Schema object

```json
{
  "oneOf": [
    {
      "$ref": "#/$defs/controlChangeEvent"
    },
    {
      "$ref": "#/$defs/channelModeEvent"
    },
    {
      "$ref": "#/$defs/programChangeEvent"
    },
    {
      "$ref": "#/$defs/pitchBendEvent"
    },
    {
      "$ref": "#/$defs/channelPressureEvent"
    },
    {
      "$ref": "#/$defs/polyPressureEvent"
    }
  ]
}
```

<a id="def-lyricvoice"></a>
## lyricVoice

Explicit relationship between a vocal/melody track and a lyric document. Several voices may reference the same lyric document without duplicating text.

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `id` | `#/$defs/id` | Yes |  |
| `name` | `string` | No/conditional |  |
| `role` | `string` | No/conditional | Open authored role. Recommended values include lead, harmony, backing, unison, double, counter, adlib, response. |
| `trackId` | `#/$defs/id` | Yes |  |
| `documentId` | `#/$defs/id` | Yes |  |
| `vocalProfile` | `#/$defs/vocalProfile` | No/conditional | Optional engine-neutral vocal defaults; absence does not mean an instrument voice. |

### Exact JSON Schema object

```json
{
  "type": "object",
  "description": "Explicit relationship between a vocal/melody track and a lyric document. Several voices may reference the same lyric document without duplicating text.",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "name": {
      "type": "string"
    },
    "role": {
      "type": "string",
      "minLength": 1,
      "description": "Open authored role. Recommended values include lead, harmony, backing, unison, double, counter, adlib, response."
    },
    "trackId": {
      "$ref": "#/$defs/id"
    },
    "documentId": {
      "$ref": "#/$defs/id"
    },
    "vocalProfile": {
      "$ref": "#/$defs/vocalProfile",
      "description": "Optional engine-neutral vocal defaults; absence does not mean an instrument voice."
    }
  },
  "required": [
    "id",
    "trackId",
    "documentId"
  ],
  "additionalProperties": false
}
```

<a id="def-playablepitchrange"></a>
## playablePitchRange

Authored playable pitch capability in the same 0..127 pitch-number domain as melodic notes. Semantic rule: lowPitch <= highPitch.

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `lowPitch` | `#/$defs/pitch` | Yes |  |
| `highPitch` | `#/$defs/pitch` | Yes |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "lowPitch": {
      "$ref": "#/$defs/pitch"
    },
    "highPitch": {
      "$ref": "#/$defs/pitch"
    }
  },
  "required": [
    "lowPitch",
    "highPitch"
  ],
  "additionalProperties": false,
  "description": "Authored playable pitch capability in the same 0..127 pitch-number domain as melodic notes. Semantic rule: lowPitch <= highPitch."
}
```

<a id="def-directionpitchcollection"></a>
## directionPitchCollection

Direction-local pitch-class collection relative to tonic. It is not a harmonic scale-context object and has no independent timeline identity.

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `tonic` | `#/$defs/spelledPitchClass` | Yes |  |
| `intervals` | `array<integer>` | Yes |  |
| `label` | `string` | No/conditional |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "tonic": {
      "$ref": "#/$defs/spelledPitchClass"
    },
    "intervals": {
      "type": "array",
      "items": {
        "type": "integer",
        "minimum": 0,
        "maximum": 11
      },
      "minItems": 1,
      "maxItems": 12,
      "uniqueItems": true,
      "contains": {
        "const": 0
      }
    },
    "label": {
      "type": "string"
    }
  },
  "required": [
    "tonic",
    "intervals"
  ],
  "additionalProperties": false,
  "description": "Direction-local pitch-class collection relative to tonic. It is not a harmonic scale-context object and has no independent timeline identity."
}
```

<a id="def-directionpitchsource"></a>
## directionPitchSource

Source of pitch vocabulary for an improvisation Direction.

No direct `properties` table (object may be an enum, scalar, array or a composition).

### Exact JSON Schema object

```json
{
  "oneOf": [
    {
      "type": "object",
      "properties": {
        "type": {
          "const": "effectiveKeyScale"
        }
      },
      "required": [
        "type"
      ],
      "additionalProperties": false
    },
    {
      "type": "object",
      "properties": {
        "type": {
          "const": "songScale"
        }
      },
      "required": [
        "type"
      ],
      "additionalProperties": false
    },
    {
      "type": "object",
      "properties": {
        "type": {
          "const": "harmonyScales"
        },
        "scaleIds": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/id"
          },
          "minItems": 1,
          "uniqueItems": true
        }
      },
      "required": [
        "type",
        "scaleIds"
      ],
      "additionalProperties": false
    },
    {
      "type": "object",
      "properties": {
        "type": {
          "const": "explicitScale"
        },
        "scale": {
          "$ref": "#/$defs/directionPitchCollection"
        }
      },
      "required": [
        "type",
        "scale"
      ],
      "additionalProperties": false
    }
  ],
  "description": "Source of pitch vocabulary for an improvisation Direction."
}
```

<a id="def-improvisationdirectionparameters"></a>
## improvisationDirectionParameters

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `pitchSource` | `#/$defs/directionPitchSource` | Yes |  |
| `adherence` | `enum ["strict", "preferred"]` | Yes |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "pitchSource": {
      "$ref": "#/$defs/directionPitchSource"
    },
    "adherence": {
      "enum": [
        "strict",
        "preferred"
      ]
    }
  },
  "required": [
    "pitchSource",
    "adherence"
  ],
  "additionalProperties": false
}
```

<a id="def-playingroledirectionparameters"></a>
## playingRoleDirectionParameters

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `role` | `string` | Yes |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "role": {
      "type": "string",
      "minLength": 1
    }
  },
  "required": [
    "role"
  ],
  "additionalProperties": false
}
```

<a id="def-pitchrangedirectionparameters"></a>
## pitchRangeDirectionParameters

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `lowPitch` | `#/$defs/pitch` | Yes |  |
| `highPitch` | `#/$defs/pitch` | Yes |  |
| `constraint` | `enum ["strict", "preferred"]` | Yes |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "lowPitch": {
      "$ref": "#/$defs/pitch"
    },
    "highPitch": {
      "$ref": "#/$defs/pitch"
    },
    "constraint": {
      "enum": [
        "strict",
        "preferred"
      ]
    }
  },
  "required": [
    "lowPitch",
    "highPitch",
    "constraint"
  ],
  "additionalProperties": false
}
```

<a id="def-vendordirectionparameters"></a>
## vendorDirectionParameters

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `namespace` | `string` | Yes |  |
| `name` | `string` | Yes |  |
| `version` | `string` | No/conditional |  |
| `data` | `object` | Yes |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "namespace": {
      "type": "string",
      "minLength": 3,
      "pattern": "^[a-z][a-z0-9-]*(?:\\.[a-z][a-z0-9-]*){2,}$",
      "not": {
        "pattern": "^org\\.ostf(?:\\.|$)"
      }
    },
    "name": {
      "type": "string",
      "minLength": 1
    },
    "version": {
      "type": "string",
      "minLength": 1
    },
    "data": {
      "type": "object"
    }
  },
  "required": [
    "namespace",
    "name",
    "data"
  ],
  "additionalProperties": false
}
```

<a id="def-improvisationdirection"></a>
## improvisationDirection

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `id` | `#/$defs/id` | Yes |  |
| `start` | `#/$defs/nonnegative` | Yes |  |
| `duration` | `#/$defs/positive` | Yes |  |
| `label` | `string` | No/conditional |  |
| `instruction` | `string` | No/conditional | Supplemental human/AI-readable semantic instruction. Structured Core parameters remain authoritative. |
| `type` | `const "improvisation"` | Yes |  |
| `parameters` | `#/$defs/improvisationDirectionParameters` | Yes |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "start": {
      "$ref": "#/$defs/nonnegative"
    },
    "duration": {
      "$ref": "#/$defs/positive"
    },
    "label": {
      "type": "string"
    },
    "instruction": {
      "type": "string",
      "description": "Supplemental human/AI-readable semantic instruction. Structured Core parameters remain authoritative."
    },
    "type": {
      "const": "improvisation"
    },
    "parameters": {
      "$ref": "#/$defs/improvisationDirectionParameters"
    }
  },
  "required": [
    "id",
    "start",
    "duration",
    "type",
    "parameters"
  ],
  "additionalProperties": false
}
```

<a id="def-playingroledirection"></a>
## playingRoleDirection

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `id` | `#/$defs/id` | Yes |  |
| `start` | `#/$defs/nonnegative` | Yes |  |
| `duration` | `#/$defs/positive` | Yes |  |
| `label` | `string` | No/conditional |  |
| `instruction` | `string` | No/conditional | Supplemental human/AI-readable semantic instruction. Structured Core parameters remain authoritative. |
| `type` | `const "playingRole"` | Yes |  |
| `parameters` | `#/$defs/playingRoleDirectionParameters` | Yes |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "start": {
      "$ref": "#/$defs/nonnegative"
    },
    "duration": {
      "$ref": "#/$defs/positive"
    },
    "label": {
      "type": "string"
    },
    "instruction": {
      "type": "string",
      "description": "Supplemental human/AI-readable semantic instruction. Structured Core parameters remain authoritative."
    },
    "type": {
      "const": "playingRole"
    },
    "parameters": {
      "$ref": "#/$defs/playingRoleDirectionParameters"
    }
  },
  "required": [
    "id",
    "start",
    "duration",
    "type",
    "parameters"
  ],
  "additionalProperties": false
}
```

<a id="def-pitchrangedirection"></a>
## pitchRangeDirection

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `id` | `#/$defs/id` | Yes |  |
| `start` | `#/$defs/nonnegative` | Yes |  |
| `duration` | `#/$defs/positive` | Yes |  |
| `label` | `string` | No/conditional |  |
| `instruction` | `string` | No/conditional | Supplemental human/AI-readable semantic instruction. Structured Core parameters remain authoritative. |
| `type` | `const "pitchRange"` | Yes |  |
| `parameters` | `#/$defs/pitchRangeDirectionParameters` | Yes |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "start": {
      "$ref": "#/$defs/nonnegative"
    },
    "duration": {
      "$ref": "#/$defs/positive"
    },
    "label": {
      "type": "string"
    },
    "instruction": {
      "type": "string",
      "description": "Supplemental human/AI-readable semantic instruction. Structured Core parameters remain authoritative."
    },
    "type": {
      "const": "pitchRange"
    },
    "parameters": {
      "$ref": "#/$defs/pitchRangeDirectionParameters"
    }
  },
  "required": [
    "id",
    "start",
    "duration",
    "type",
    "parameters"
  ],
  "additionalProperties": false
}
```

<a id="def-vendorrangedirection"></a>
## vendorRangeDirection

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `id` | `#/$defs/id` | Yes |  |
| `start` | `#/$defs/nonnegative` | Yes |  |
| `duration` | `#/$defs/positive` | Yes |  |
| `label` | `string` | No/conditional |  |
| `instruction` | `string` | No/conditional | Supplemental human/AI-readable semantic instruction. Structured Core parameters remain authoritative. |
| `type` | `const "vendor"` | Yes |  |
| `parameters` | `#/$defs/vendorDirectionParameters` | Yes |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "start": {
      "$ref": "#/$defs/nonnegative"
    },
    "duration": {
      "$ref": "#/$defs/positive"
    },
    "label": {
      "type": "string"
    },
    "instruction": {
      "type": "string",
      "description": "Supplemental human/AI-readable semantic instruction. Structured Core parameters remain authoritative."
    },
    "type": {
      "const": "vendor"
    },
    "parameters": {
      "$ref": "#/$defs/vendorDirectionParameters"
    }
  },
  "required": [
    "id",
    "start",
    "duration",
    "type",
    "parameters"
  ],
  "additionalProperties": false
}
```

<a id="def-vendorpointdirection"></a>
## vendorPointDirection

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `id` | `#/$defs/id` | Yes |  |
| `at` | `#/$defs/nonnegative` | Yes |  |
| `type` | `const "vendor"` | Yes |  |
| `parameters` | `#/$defs/vendorDirectionParameters` | Yes |  |
| `label` | `string` | No/conditional |  |
| `instruction` | `string` | No/conditional | Supplemental human/AI-readable semantic instruction. Structured/vendor parameters remain authoritative. |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "at": {
      "$ref": "#/$defs/nonnegative"
    },
    "type": {
      "const": "vendor"
    },
    "parameters": {
      "$ref": "#/$defs/vendorDirectionParameters"
    },
    "label": {
      "type": "string"
    },
    "instruction": {
      "type": "string",
      "description": "Supplemental human/AI-readable semantic instruction. Structured/vendor parameters remain authoritative."
    }
  },
  "required": [
    "id",
    "at",
    "type",
    "parameters"
  ],
  "additionalProperties": false
}
```

<a id="def-trackdirection"></a>
## trackDirection

Typed semantic instruction owned by a track and positioned on the OSTF global timebase.

No direct `properties` table (object may be an enum, scalar, array or a composition).

### Exact JSON Schema object

```json
{
  "oneOf": [
    {
      "$ref": "#/$defs/improvisationDirection"
    },
    {
      "$ref": "#/$defs/playingRoleDirection"
    },
    {
      "$ref": "#/$defs/pitchRangeDirection"
    },
    {
      "$ref": "#/$defs/vendorRangeDirection"
    },
    {
      "$ref": "#/$defs/vendorPointDirection"
    },
    {
      "$ref": "#/$defs/phrasingDirection"
    },
    {
      "$ref": "#/$defs/vocalFreedomDirection"
    }
  ],
  "description": "Typed semantic instruction owned by a track and positioned on the OSTF global timebase."
}
```

<a id="def-vocalphonetics"></a>
## vocalPhonetics

Ordered phoneme symbols for a lyric unit, not an absolute pronunciation engine command.

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `alphabet` | `enum ["ipa", "xsampa", "arpabet", "other"]` | Yes |  |
| `language` | `string` | No/conditional |  |
| `symbols` | `array<string>` | Yes |  |
| `namespace` | `string` | No/conditional |  |
| `preferred` | `boolean` | No/conditional | Optional preference only within the same (alphabet, language) set for this lyricUnit. At most one preferred variant per key; absent does not i... |

### Exact JSON Schema object

```json
{
  "type": "object",
  "description": "Ordered phoneme symbols for a lyric unit, not an absolute pronunciation engine command.",
  "properties": {
    "alphabet": {
      "enum": [
        "ipa",
        "xsampa",
        "arpabet",
        "other"
      ]
    },
    "language": {
      "type": "string",
      "minLength": 1
    },
    "symbols": {
      "type": "array",
      "minItems": 1,
      "items": {
        "type": "string",
        "minLength": 1
      }
    },
    "namespace": {
      "type": "string",
      "minLength": 1
    },
    "preferred": {
      "type": "boolean",
      "description": "Optional preference only within the same (alphabet, language) set for this lyricUnit. At most one preferred variant per key; absent does not imply false or a guaranteed conversion."
    }
  },
  "required": [
    "alphabet",
    "symbols"
  ],
  "additionalProperties": false,
  "allOf": [
    {
      "if": {
        "properties": {
          "alphabet": {
            "const": "other"
          }
        },
        "required": [
          "alphabet"
        ]
      },
      "then": {
        "required": [
          "namespace"
        ]
      }
    }
  ]
}
```

<a id="def-vocalprofile"></a>
## vocalProfile

Voice default independent of commercial singer preset or license.

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `language` | `string` | No/conditional |  |
| `deliveryMode` | `enum ["sing", "rap", "speak", "hum"]` | No/conditional |  |
| `voiceDescription` | `string` | No/conditional |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "description": "Voice default independent of commercial singer preset or license.",
  "properties": {
    "language": {
      "type": "string",
      "minLength": 1
    },
    "deliveryMode": {
      "enum": [
        "sing",
        "rap",
        "speak",
        "hum"
      ]
    },
    "voiceDescription": {
      "type": "string",
      "minLength": 1
    }
  },
  "additionalProperties": false
}
```

<a id="def-vocalperformance"></a>
## vocalPerformance

Performance belonging to exactly one lyric voice within a containing clip.

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `id` | `#/$defs/id` | Yes |  |
| `voiceId` | `#/$defs/id` | Yes |  |
| `phonemeEvents` | `array<#/$defs/vocalPhonemeEvent>` | No/conditional |  |
| `pitchCurves` | `array<#/$defs/vocalPitchCurve>` | No/conditional |  |
| `expressionCurves` | `array<#/$defs/vocalExpressionCurve>` | No/conditional |  |
| `techniques` | `array<#/$defs/vocalTechnique>` | No/conditional |  |
| `breathEvents` | `array<#/$defs/vocalBreathEvent>` | No/conditional |  |
| `noteIds` | `array<#/$defs/id>` | No/conditional | Optional exact list of existing note IDs performed by this voice in the containing clip. No duplicate note objects. When present it includes a... |

### Exact JSON Schema object

```json
{
  "type": "object",
  "description": "Performance belonging to exactly one lyric voice within a containing clip.",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "voiceId": {
      "$ref": "#/$defs/id"
    },
    "phonemeEvents": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/vocalPhonemeEvent"
      }
    },
    "pitchCurves": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/vocalPitchCurve"
      }
    },
    "expressionCurves": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/vocalExpressionCurve"
      }
    },
    "techniques": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/vocalTechnique"
      }
    },
    "breathEvents": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/vocalBreathEvent"
      }
    },
    "noteIds": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/id"
      },
      "minItems": 1,
      "uniqueItems": true,
      "description": "Optional exact list of existing note IDs performed by this voice in the containing clip. No duplicate note objects. When present it includes all locally aligned note IDs for that voice. When absent, derive ownership only from voice-specific alignments. Never infer from song.melodyTrackIds."
    }
  },
  "required": [
    "id",
    "voiceId"
  ],
  "additionalProperties": false
}
```

<a id="def-vocalphonemeevent"></a>
## vocalPhonemeEvent

Explicit phoneme timing, expressed in clip-relative ppq ticks, negative allowed with nonnegative absolute song time.

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `id` | `#/$defs/id` | Yes |  |
| `unitId` | `#/$defs/id` | Yes |  |
| `noteId` | `#/$defs/id` | No/conditional |  |
| `alphabet` | `enum ["ipa", "xsampa", "arpabet", "other"]` | Yes |  |
| `namespace` | `string` | No/conditional |  |
| `symbol` | `string` | Yes |  |
| `start` | `#/$defs/signed` | Yes |  |
| `duration` | `#/$defs/positive` | Yes |  |
| `order` | `integer` | No/conditional | Optional deterministic ordering when multiple phonemeEvents for one voice share the same start tick; distinct within a (voiceId, start) tie gr... |

### Exact JSON Schema object

```json
{
  "type": "object",
  "description": "Explicit phoneme timing, expressed in clip-relative ppq ticks, negative allowed with nonnegative absolute song time.",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "unitId": {
      "$ref": "#/$defs/id"
    },
    "noteId": {
      "$ref": "#/$defs/id"
    },
    "alphabet": {
      "enum": [
        "ipa",
        "xsampa",
        "arpabet",
        "other"
      ]
    },
    "namespace": {
      "type": "string",
      "minLength": 1
    },
    "symbol": {
      "type": "string",
      "minLength": 1
    },
    "start": {
      "$ref": "#/$defs/signed"
    },
    "duration": {
      "$ref": "#/$defs/positive"
    },
    "order": {
      "type": "integer",
      "description": "Optional deterministic ordering when multiple phonemeEvents for one voice share the same start tick; distinct within a (voiceId, start) tie group. Not an audio rendering priority."
    }
  },
  "required": [
    "id",
    "unitId",
    "alphabet",
    "symbol",
    "start",
    "duration"
  ],
  "additionalProperties": false,
  "allOf": [
    {
      "if": {
        "properties": {
          "alphabet": {
            "const": "other"
          }
        },
        "required": [
          "alphabet"
        ]
      },
      "then": {
        "required": [
          "namespace"
        ]
      }
    }
  ]
}
```

<a id="def-vocalcurvepointpitch"></a>
## vocalCurvePointPitch

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `at` | `#/$defs/signed` | Yes |  |
| `value` | `number` | Yes | Semitone offset from the targeted MIDI note, in cents (signed). |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "at": {
      "$ref": "#/$defs/signed"
    },
    "value": {
      "type": "number",
      "description": "Semitone offset from the targeted MIDI note, in cents (signed)."
    }
  },
  "required": [
    "at",
    "value"
  ],
  "additionalProperties": false
}
```

<a id="def-vocalcurvepointnormalized"></a>
## vocalCurvePointNormalized

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `at` | `#/$defs/signed` | Yes |  |
| `value` | `number` | Yes |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "at": {
      "$ref": "#/$defs/signed"
    },
    "value": {
      "type": "number",
      "minimum": 0,
      "maximum": 1
    }
  },
  "required": [
    "at",
    "value"
  ],
  "additionalProperties": false
}
```

<a id="def-vocalpitchcurve"></a>
## vocalPitchCurve

Specific vocal pitch offset for a single concrete Note, in cents; sample points use clip-relative ppq ticks.

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `id` | `#/$defs/id` | Yes |  |
| `targetNoteId` | `#/$defs/id` | Yes |  |
| `unit` | `const "cents"` | Yes |  |
| `interpolation` | `enum ["step", "linear"]` | Yes |  |
| `points` | `array<#/$defs/vocalCurvePointPitch>` | Yes |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "description": "Specific vocal pitch offset for a single concrete Note, in cents; sample points use clip-relative ppq ticks.",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "targetNoteId": {
      "$ref": "#/$defs/id"
    },
    "unit": {
      "const": "cents"
    },
    "interpolation": {
      "enum": [
        "step",
        "linear"
      ]
    },
    "points": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/$defs/vocalCurvePointPitch"
      }
    }
  },
  "required": [
    "id",
    "targetNoteId",
    "unit",
    "interpolation",
    "points"
  ],
  "additionalProperties": false
}
```

<a id="def-vocalexpressioncurve"></a>
## vocalExpressionCurve

Portable vocal parameters, each normalized 0..1, with no promise of perceptually identical output across engines.

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `id` | `#/$defs/id` | Yes |  |
| `parameter` | `enum ["dynamics", "breathiness", "tension", "brightness", "voicing"]` | Yes |  |
| `interpolation` | `enum ["step", "linear"]` | Yes |  |
| `points` | `array<#/$defs/vocalCurvePointNormalized>` | Yes |  |
| `targetNoteId` | `#/$defs/id` | No/conditional | Optional note-specific replacement of a clip-scoped curve of the same parameter while the note is active. Points still use clip-relative ticks... |

### Exact JSON Schema object

```json
{
  "type": "object",
  "description": "Portable vocal parameters, each normalized 0..1, with no promise of perceptually identical output across engines.",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "parameter": {
      "enum": [
        "dynamics",
        "breathiness",
        "tension",
        "brightness",
        "voicing"
      ]
    },
    "interpolation": {
      "enum": [
        "step",
        "linear"
      ]
    },
    "points": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/$defs/vocalCurvePointNormalized"
      }
    },
    "targetNoteId": {
      "$ref": "#/$defs/id",
      "description": "Optional note-specific replacement of a clip-scoped curve of the same parameter while the note is active. Points still use clip-relative ticks. Do not sum both curves."
    }
  },
  "required": [
    "id",
    "parameter",
    "interpolation",
    "points"
  ],
  "additionalProperties": false
}
```

<a id="def-vocaltechnique"></a>
## vocalTechnique

Semantic artistic intention, not deterministic rendering or an extra pitch source.

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `id` | `#/$defs/id` | Yes |  |
| `start` | `#/$defs/signed` | Yes |  |
| `duration` | `#/$defs/positive` | Yes |  |
| `kind` | `enum ["scoop", "fall", "vibrato", "portamento", "legato", "staccato", "accent", "whisper", "growl", "falsetto", "humming", "rap", "melisma"]` | Yes |  |
| `intensity` | `number` | No/conditional |  |
| `targetNoteId` | `#/$defs/id` | No/conditional |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "description": "Semantic artistic intention, not deterministic rendering or an extra pitch source.",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "start": {
      "$ref": "#/$defs/signed"
    },
    "duration": {
      "$ref": "#/$defs/positive"
    },
    "kind": {
      "enum": [
        "scoop",
        "fall",
        "vibrato",
        "portamento",
        "legato",
        "staccato",
        "accent",
        "whisper",
        "growl",
        "falsetto",
        "humming",
        "rap",
        "melisma"
      ]
    },
    "intensity": {
      "type": "number",
      "minimum": 0,
      "maximum": 1
    },
    "targetNoteId": {
      "$ref": "#/$defs/id"
    }
  },
  "required": [
    "id",
    "start",
    "duration",
    "kind"
  ],
  "additionalProperties": false
}
```

<a id="def-vocalbreathevent"></a>
## vocalBreathEvent

Optional breath marker. The renderer decides whether to synthesize audible breath.

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `id` | `#/$defs/id` | Yes |  |
| `start` | `#/$defs/signed` | Yes |  |
| `duration` | `#/$defs/positive` | Yes |  |
| `kind` | `enum ["inhale", "exhale"]` | Yes |  |
| `intensity` | `number` | No/conditional |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "description": "Optional breath marker. The renderer decides whether to synthesize audible breath.",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "start": {
      "$ref": "#/$defs/signed"
    },
    "duration": {
      "$ref": "#/$defs/positive"
    },
    "kind": {
      "enum": [
        "inhale",
        "exhale"
      ]
    },
    "intensity": {
      "type": "number",
      "minimum": 0,
      "maximum": 1
    }
  },
  "required": [
    "id",
    "start",
    "duration",
    "kind"
  ],
  "additionalProperties": false
}
```

<a id="def-positiveintrange"></a>
## positiveIntRange

Inclusive tick bounds; semantic check min <= max.

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `min` | `#/$defs/positive` | Yes |  |
| `max` | `#/$defs/positive` | Yes |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "min": {
      "$ref": "#/$defs/positive"
    },
    "max": {
      "$ref": "#/$defs/positive"
    }
  },
  "required": [
    "min",
    "max"
  ],
  "additionalProperties": false,
  "description": "Inclusive tick bounds; semantic check min <= max."
}
```

<a id="def-nonnegativenumberrange"></a>
## nonnegativeNumberRange

Inclusive range; semantic check min <= max. Count distinct note-on groups at equal onset ticks as one onset.

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `min` | `number` | Yes |  |
| `max` | `number` | Yes |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "min": {
      "type": "number",
      "minimum": 0,
      "maximum": 128
    },
    "max": {
      "type": "number",
      "minimum": 0,
      "maximum": 128
    }
  },
  "required": [
    "min",
    "max"
  ],
  "additionalProperties": false,
  "description": "Inclusive range; semantic check min <= max. Count distinct note-on groups at equal onset ticks as one onset."
}
```

<a id="def-phrasingdirectionparameters"></a>
## phrasingDirectionParameters

At least one musical property beyond adherence must be authored; motifRef resolves to phraseLibrary.templates[].id.

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `phraseLengthTicks` | `#/$defs/positiveIntRange` | No/conditional |  |
| `onsetGroupsPerQuarter` | `#/$defs/nonnegativeNumberRange` | No/conditional |  |
| `development` | `enum ["repetition", "motivicVariation", "sequence", "contrast", "free"]` | No/conditional |  |
| `contour` | `enum ["ascending", "descending", "arch", "valley", "stable", "free"]` | No/conditional |  |
| `energyShape` | `enum ["rising", "falling", "arch", "valley", "stable", "free"]` | No/conditional | Abstract musical-energy direction; not equivalent to output velocity or volume. |
| `motifRef` | `#/$defs/id` | No/conditional |  |
| `adherence` | `enum ["strict", "preferred"]` | Yes |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "phraseLengthTicks": {
      "$ref": "#/$defs/positiveIntRange"
    },
    "onsetGroupsPerQuarter": {
      "$ref": "#/$defs/nonnegativeNumberRange"
    },
    "development": {
      "enum": [
        "repetition",
        "motivicVariation",
        "sequence",
        "contrast",
        "free"
      ]
    },
    "contour": {
      "enum": [
        "ascending",
        "descending",
        "arch",
        "valley",
        "stable",
        "free"
      ]
    },
    "energyShape": {
      "enum": [
        "rising",
        "falling",
        "arch",
        "valley",
        "stable",
        "free"
      ],
      "description": "Abstract musical-energy direction; not equivalent to output velocity or volume."
    },
    "motifRef": {
      "$ref": "#/$defs/id"
    },
    "adherence": {
      "enum": [
        "strict",
        "preferred"
      ]
    }
  },
  "required": [
    "adherence"
  ],
  "additionalProperties": false,
  "description": "At least one musical property beyond adherence must be authored; motifRef resolves to phraseLibrary.templates[].id.",
  "minProperties": 2
}
```

<a id="def-phrasingdirection"></a>
## phrasingDirection

4.3 optional phrasing Track Direction, using global source-timeline ticks.

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `id` | `#/$defs/id` | Yes |  |
| `type` | `const "phrasing"` | Yes |  |
| `start` | `#/$defs/nonnegative` | Yes |  |
| `duration` | `#/$defs/positive` | Yes |  |
| `label` | `string` | No/conditional |  |
| `instruction` | `string` | No/conditional | Non-executable music-text context, subordinate to structured fields. |
| `parameters` | `#/$defs/phrasingDirectionParameters` | Yes |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "type": {
      "const": "phrasing"
    },
    "start": {
      "$ref": "#/$defs/nonnegative"
    },
    "duration": {
      "$ref": "#/$defs/positive"
    },
    "label": {
      "type": "string"
    },
    "instruction": {
      "type": "string",
      "description": "Non-executable music-text context, subordinate to structured fields."
    },
    "parameters": {
      "$ref": "#/$defs/phrasingDirectionParameters"
    }
  },
  "required": [
    "id",
    "type",
    "start",
    "duration",
    "parameters"
  ],
  "additionalProperties": false,
  "description": "4.3 optional phrasing Track Direction, using global source-timeline ticks."
}
```

<a id="def-lyriccandidateset"></a>
## lyricCandidateSet

One ordered candidate sequence of authored Lyric Phrase IDs. No implicit note alignment.

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `phraseIds` | `array<#/$defs/id>` | Yes |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "phraseIds": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/id"
      },
      "minItems": 1,
      "uniqueItems": true
    }
  },
  "required": [
    "phraseIds"
  ],
  "additionalProperties": false,
  "description": "One ordered candidate sequence of authored Lyric Phrase IDs. No implicit note alignment."
}
```

<a id="def-vocalfreedomdirectionparameters"></a>
## vocalFreedomDirectionParameters

Voice-specific freedom policy. Fixed text does not automatically imply fixed melody or vice versa.

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `voiceId` | `#/$defs/id` | Yes |  |
| `textPolicy` | `enum ["fixed", "alternatives", "open"]` | Yes |  |
| `melodyPolicy` | `enum ["fixed", "ornamentable", "open"]` | Yes |  |
| `vocalizationKind` | `enum ["lexical", "scat", "humming", "nonLexical"]` | No/conditional |  |
| `candidatePhraseSets` | `array<#/$defs/lyricCandidateSet>` | No/conditional |  |
| `adherence` | `enum ["strict", "preferred"]` | Yes |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "voiceId": {
      "$ref": "#/$defs/id"
    },
    "textPolicy": {
      "enum": [
        "fixed",
        "alternatives",
        "open"
      ]
    },
    "melodyPolicy": {
      "enum": [
        "fixed",
        "ornamentable",
        "open"
      ]
    },
    "vocalizationKind": {
      "enum": [
        "lexical",
        "scat",
        "humming",
        "nonLexical"
      ]
    },
    "candidatePhraseSets": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/lyricCandidateSet"
      },
      "minItems": 2
    },
    "adherence": {
      "enum": [
        "strict",
        "preferred"
      ]
    }
  },
  "required": [
    "voiceId",
    "textPolicy",
    "melodyPolicy",
    "adherence"
  ],
  "additionalProperties": false,
  "description": "Voice-specific freedom policy. Fixed text does not automatically imply fixed melody or vice versa.",
  "if": {
    "properties": {
      "textPolicy": {
        "const": "alternatives"
      }
    },
    "required": [
      "textPolicy"
    ]
  },
  "then": {
    "required": [
      "candidatePhraseSets"
    ]
  },
  "else": {
    "not": {
      "required": [
        "candidatePhraseSets"
      ]
    }
  }
}
```

<a id="def-vocalfreedomdirection"></a>
## vocalFreedomDirection

4.3 optional vocalFreedom Track Direction, using global source-timeline ticks.

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `id` | `#/$defs/id` | Yes |  |
| `type` | `const "vocalFreedom"` | Yes |  |
| `start` | `#/$defs/nonnegative` | Yes |  |
| `duration` | `#/$defs/positive` | Yes |  |
| `label` | `string` | No/conditional |  |
| `instruction` | `string` | No/conditional | Non-executable music-text context, subordinate to structured fields. |
| `parameters` | `#/$defs/vocalFreedomDirectionParameters` | Yes |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "type": {
      "const": "vocalFreedom"
    },
    "start": {
      "$ref": "#/$defs/nonnegative"
    },
    "duration": {
      "$ref": "#/$defs/positive"
    },
    "label": {
      "type": "string"
    },
    "instruction": {
      "type": "string",
      "description": "Non-executable music-text context, subordinate to structured fields."
    },
    "parameters": {
      "$ref": "#/$defs/vocalFreedomDirectionParameters"
    }
  },
  "required": [
    "id",
    "type",
    "start",
    "duration",
    "parameters"
  ],
  "additionalProperties": false,
  "description": "4.3 optional vocalFreedom Track Direction, using global source-timeline ticks."
}
```

<a id="def-performancerequirements"></a>
## performanceRequirements

Minimum/peak musical capabilities required to realize this authored part, not an assertion about the performer. No robot mechanics or safety commands.

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `requiredPolyphony` | `integer` | No/conditional |  |
| `requiredPitchRange` | `#/$defs/playablePitchRange` | No/conditional |  |
| `requiredArticulations` | `array<string>` | No/conditional |  |
| `peakOnsetGroupsPerQuarter` | `number` | No/conditional |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "requiredPolyphony": {
      "type": "integer",
      "minimum": 1,
      "maximum": 128
    },
    "requiredPitchRange": {
      "$ref": "#/$defs/playablePitchRange"
    },
    "requiredArticulations": {
      "type": "array",
      "items": {
        "type": "string",
        "minLength": 1
      },
      "minItems": 1,
      "uniqueItems": true
    },
    "peakOnsetGroupsPerQuarter": {
      "type": "number",
      "exclusiveMinimum": 0,
      "maximum": 128
    }
  },
  "required": [],
  "additionalProperties": false,
  "description": "Minimum/peak musical capabilities required to realize this authored part, not an assertion about the performer. No robot mechanics or safety commands.",
  "minProperties": 1
}
```

<a id="def-performancescope"></a>
## performanceScope

Bind to exactly one finite visit within a specific plan.

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `performancePlanId` | `#/$defs/id` | Yes |  |
| `visitId` | `#/$defs/id` | Yes |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "performancePlanId": {
      "$ref": "#/$defs/id"
    },
    "visitId": {
      "$ref": "#/$defs/id"
    }
  },
  "required": [
    "performancePlanId",
    "visitId"
  ],
  "additionalProperties": false,
  "description": "Bind to exactly one finite visit within a specific plan."
}
```

<a id="def-ensembleinteraction"></a>
## ensembleInteraction

Directed actor/partner relationship: different Tracks, or the same Track only with both explicit and different Lyric Voice IDs whose trackId equals the shared Track. Use source tick range, visit scope, or both. No audio, real-time event, or motor control is implied. Same Track without two distinct owned Voices is a semantic error (JSON Schema cannot compare sibling ID values).

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `id` | `#/$defs/id` | Yes |  |
| `actorTrackId` | `#/$defs/id` | Yes |  |
| `partnerTrackId` | `#/$defs/id` | Yes |  |
| `actorVoiceId` | `#/$defs/id` | No/conditional |  |
| `partnerVoiceId` | `#/$defs/id` | No/conditional |  |
| `relation` | `enum ["respondTo", "followRhythm", "alternateWith", "leaveSpaceFor", "reinforce"]` | Yes |  |
| `start` | `#/$defs/nonnegative` | No/conditional |  |
| `duration` | `#/$defs/positive` | No/conditional |  |
| `scope` | `#/$defs/performanceScope` | No/conditional |  |
| `responseWindowTicks` | `#/$defs/positive` | No/conditional |  |
| `adherence` | `enum ["strict", "preferred"]` | Yes |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "actorTrackId": {
      "$ref": "#/$defs/id"
    },
    "partnerTrackId": {
      "$ref": "#/$defs/id"
    },
    "actorVoiceId": {
      "$ref": "#/$defs/id"
    },
    "partnerVoiceId": {
      "$ref": "#/$defs/id"
    },
    "relation": {
      "enum": [
        "respondTo",
        "followRhythm",
        "alternateWith",
        "leaveSpaceFor",
        "reinforce"
      ]
    },
    "start": {
      "$ref": "#/$defs/nonnegative"
    },
    "duration": {
      "$ref": "#/$defs/positive"
    },
    "scope": {
      "$ref": "#/$defs/performanceScope"
    },
    "responseWindowTicks": {
      "$ref": "#/$defs/positive"
    },
    "adherence": {
      "enum": [
        "strict",
        "preferred"
      ]
    }
  },
  "required": [
    "id",
    "actorTrackId",
    "partnerTrackId",
    "relation",
    "adherence"
  ],
  "additionalProperties": false,
  "description": "Directed actor/partner relationship: different Tracks, or the same Track only with both explicit and different Lyric Voice IDs whose trackId equals the shared Track. Use source tick range, visit scope, or both. No audio, real-time event, or motor control is implied. Same Track without two distinct owned Voices is a semantic error (JSON Schema cannot compare sibling ID values).",
  "anyOf": [
    {
      "required": [
        "start",
        "duration"
      ]
    },
    {
      "required": [
        "scope"
      ]
    }
  ],
  "dependentRequired": {
    "start": [
      "duration"
    ],
    "duration": [
      "start"
    ]
  }
}
```

<a id="def-visitpart"></a>
## visitPart

A part rule within one performance visit, not a mutation of the source Track.

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `trackId` | `#/$defs/id` | Yes |  |
| `role` | `string` | No/conditional | Visit-scoped role override of Track default; timed playingRole conflict requires explicitly listed replacement. |
| `realization` | `enum ["fixed", "open", "silent"]` | Yes |  |
| `replacesDirectionIds` | `array<#/$defs/id>` | No/conditional | Only explicit source-track playingRole Direction IDs may be replaced by the visit role. |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "trackId": {
      "$ref": "#/$defs/id"
    },
    "role": {
      "type": "string",
      "minLength": 1,
      "description": "Visit-scoped role override of Track default; timed playingRole conflict requires explicitly listed replacement."
    },
    "realization": {
      "enum": [
        "fixed",
        "open",
        "silent"
      ]
    },
    "replacesDirectionIds": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/id"
      },
      "uniqueItems": true,
      "description": "Only explicit source-track playingRole Direction IDs may be replaced by the visit role."
    }
  },
  "required": [
    "trackId",
    "realization"
  ],
  "additionalProperties": false,
  "description": "A part rule within one performance visit, not a mutation of the source Track."
}
```

<a id="def-performancevisit"></a>
## performanceVisit

Finite visit; exactly one source selector. Ordinals must be 0..N-1 in unique sequence within one plan.

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `id` | `#/$defs/id` | Yes |  |
| `ordinal` | `#/$defs/nonnegative` | Yes |  |
| `label` | `string` | No/conditional |  |
| `sourceSectionIds` | `array<#/$defs/id>` | No/conditional |  |
| `sourceRange` | `#/$defs/range` | No/conditional |  |
| `parts` | `array<#/$defs/visitPart>` | Yes |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "ordinal": {
      "$ref": "#/$defs/nonnegative"
    },
    "label": {
      "type": "string"
    },
    "sourceSectionIds": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/id"
      },
      "minItems": 1
    },
    "sourceRange": {
      "$ref": "#/$defs/range"
    },
    "parts": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/visitPart"
      }
    }
  },
  "required": [
    "id",
    "ordinal",
    "parts"
  ],
  "additionalProperties": false,
  "description": "Finite visit; exactly one source selector. Ordinals must be 0..N-1 in unique sequence within one plan.",
  "oneOf": [
    {
      "required": [
        "sourceSectionIds"
      ]
    },
    {
      "required": [
        "sourceRange"
      ]
    }
  ],
  "not": {
    "required": [
      "sourceSectionIds",
      "sourceRange"
    ]
  }
}
```

<a id="def-performanceplan"></a>
## performancePlan

Opt-in finite expanded playthrough. Source Section/Tick remains authoritative. No implicit cues, indefinite loops, or network session state.

| Property | Type/constraint | Direct required | Description |
| --- | --- | --- | --- |
| `id` | `#/$defs/id` | Yes |  |
| `name` | `string` | No/conditional |  |
| `mode` | `const "orderedFinite"` | Yes |  |
| `defaultRealization` | `enum ["fixed", "silent", "unspecified"]` | Yes | Explicit policy for unlisted tracks per visit; unspecified cannot claim deterministic replay. |
| `visits` | `array<#/$defs/performanceVisit>` | Yes |  |

### Exact JSON Schema object

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "name": {
      "type": "string"
    },
    "mode": {
      "const": "orderedFinite"
    },
    "defaultRealization": {
      "enum": [
        "fixed",
        "silent",
        "unspecified"
      ],
      "description": "Explicit policy for unlisted tracks per visit; unspecified cannot claim deterministic replay."
    },
    "visits": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/performanceVisit"
      },
      "minItems": 1
    }
  },
  "required": [
    "id",
    "mode",
    "defaultRealization",
    "visits"
  ],
  "additionalProperties": false,
  "description": "Opt-in finite expanded playthrough. Source Section/Tick remains authoritative. No implicit cues, indefinite loops, or network session state."
}
```

## Draft 0.13 — Companion production profile parameter scope

This file remains the **full, unchanged OSTF 4.3 musical Core parameter reference** (127 `$defs`). The newly proposed **independently versioned** Production Session Profile 0.1.0 has its own 12 `$defs` and complete 61-property inventory in `PRODUCTION_PARAMETER_REFERENCE.md`. Mixer, device, asset, automation and host-extension fields MUST NOT be presented as additional root OSTF Core properties. The earlier Distributed Session Profile 0.2 continues to have its separate `SESSION_PARAMETER_REFERENCE.md`.
