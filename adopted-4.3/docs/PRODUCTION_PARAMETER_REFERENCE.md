> **Current document edition: Draft 0.69 (unratified).** Older Draft headings and snapshot notes are retained as history. D01–D05 remain pending.

> **Historical editorial snapshot: Draft 0.59 (unratified).** Existing headings referring to earlier Drafts describe cumulative editorial proposals, not competing active document versions. The exact versioned Schemas remain unchanged; the single current release gate is [RELEASE_READINESS.md](RELEASE_READINESS.md). Publisher acceptance D01–D05 is still pending; runtime/independent tests are excluded, not passed.

# OSTF Production Session Profile 0.2.0 — Complete parameter reference (Draft 0.53 editorial edition; Schema unchanged)

Full schema-derived reference for Production Profile 0.2.0 including inherited 0.1 parameters and new Automation target branches. Schema authority: `schema/ostf-production-session-0.2.schema.json`; semantic authority: `docs/PRODUCTION_SESSION_PROFILE.md` §§1–30 (including later source/Visit, asset, version and cross-profile rules). This is a proposed non-ratified specification.

The Schema examples below are **exact source JSON definitions**. Structural validation alone cannot resolve Core Track/Score IDs, plugin ports or cross-object audio/automation references.

## Root

Optional studio companion profile; audio regions, sidechains and targeted Send/Region/Device-control automation. Descriptive data, not plug-in execution or DAW interoperability certification.

| Field | Required | Type | Constraints |
|---|---|---|---|
| `profile` | Yes | const OSTF-Production-Session |  |
| `profileVersion` | Yes | const 0.2.0 |  |
| `score` | Yes | ref score |  |
| `channels` | Yes | array | minItems=1; items:ref channel |
| `devices` | Optional / conditional | array | minItems=0; items:ref device |
| `assets` | Optional / conditional | array | minItems=0; items:ref asset |
| `automation` | Optional / conditional | array | minItems=0; items:ref automation |
| `notes` | Optional / conditional | string |  |
| `hostExtensions` | Optional / conditional | array | items:ref hostExtension |
| `audioRegions` | Optional / conditional | array | minItems=0; items:ref audioRegion; Optional authored audio-region arrangement in source-score global Tick time. Does not modify OSTF Core Clips/Notes. |
| `sidechainConnections` | Optional / conditional | array | minItems=0; items:ref sidechainConnection; Optional typed, acyclic audio detector/key inputs to effect plugin ports; not part of normal audible output routing. |

**Exact schema:**

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://yoh-nak.github.io/ostf/schema/ostf-production-session-0.2.schema.json",
  "title": "OSTF Production Session Profile 0.2.0 (Draft 0.15; not ratified)",
  "description": "Optional studio companion profile; audio regions, sidechains and targeted Send/Region/Device-control automation. Descriptive data, not plug-in execution or DAW interoperability certification.",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "profile": {
      "const": "OSTF-Production-Session"
    },
    "profileVersion": {
      "const": "0.2.0"
    },
    "score": {
      "$ref": "#/$defs/score"
    },
    "channels": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/channel"
      },
      "minItems": 1
    },
    "devices": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/device"
      },
      "minItems": 0
    },
    "assets": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/asset"
      },
      "minItems": 0
    },
    "automation": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/automation"
      },
      "minItems": 0
    },
    "notes": {
      "type": "string"
    },
    "hostExtensions": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/hostExtension"
      }
    },
    "audioRegions": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/audioRegion"
      },
      "minItems": 0,
      "description": "Optional authored audio-region arrangement in source-score global Tick time. Does not modify OSTF Core Clips/Notes."
    },
    "sidechainConnections": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/sidechainConnection"
      },
      "minItems": 0,
      "description": "Optional typed, acyclic audio detector/key inputs to effect plugin ports; not part of normal audible output routing."
    }
  },
  "required": [
    "profile",
    "profileVersion",
    "score",
    "channels"
  ],
  "$defs": {
    "id": {
      "type": "string",
      "minLength": 1,
      "pattern": "^\\S+$"
    },
    "sha256": {
      "type": "string",
      "pattern": "^[0-9a-f]{64}$"
    },
    "score": {
      "type": "object",
      "properties": {
        "formatVersion": {
          "const": "4.3.0"
        },
        "sha256": {
          "$ref": "#/$defs/sha256"
        },
        "documentId": {
          "$ref": "#/$defs/id"
        },
        "revisionId": {
          "$ref": "#/$defs/id"
        },
        "sourceUri": {
          "type": "string",
          "minLength": 1
        }
      },
      "required": [
        "formatVersion",
        "sha256"
      ],
      "additionalProperties": false
    },
    "channel": {
      "type": "object",
      "properties": {
        "id": {
          "$ref": "#/$defs/id"
        },
        "kind": {
          "enum": [
            "track",
            "audioTrack",
            "bus",
            "master"
          ],
          "description": "audioTrack is a production-only recorded-audio channel, and MUST NOT claim a Core trackId. kind track still maps an OSTF Track exactly as in 0.1."
        },
        "name": {
          "type": "string",
          "minLength": 1
        },
        "trackId": {
          "$ref": "#/$defs/id"
        },
        "audioChannels": {
          "enum": [
            1,
            2
          ]
        },
        "gainDb": {
          "type": "number",
          "minimum": -120,
          "maximum": 24
        },
        "pan": {
          "type": "number",
          "minimum": -1,
          "maximum": 1
        },
        "mute": {
          "type": "boolean"
        },
        "solo": {
          "type": "boolean"
        },
        "soloSafe": {
          "type": "boolean"
        },
        "outputChannelId": {
          "$ref": "#/$defs/id"
        },
        "deviceIds": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/id"
          },
          "minItems": 0,
          "uniqueItems": true
        },
        "sends": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/send"
          },
          "minItems": 0
        }
      },
      "required": [
        "id",
        "kind",
        "audioChannels",
        "gainDb",
        "pan",
        "mute",
        "solo",
        "soloSafe",
        "deviceIds"
      ],
      "additionalProperties": false
    },
    "send": {
      "type": "object",
      "properties": {
        "id": {
          "$ref": "#/$defs/id"
        },
        "targetChannelId": {
          "$ref": "#/$defs/id"
        },
        "gainDb": {
          "type": "number",
          "minimum": -120,
          "maximum": 24
        },
        "preFader": {
          "type": "boolean"
        },
        "enabled": {
          "type": "boolean"
        }
      },
      "required": [
        "id",
        "targetChannelId",
        "gainDb",
        "preFader",
        "enabled"
      ],
      "additionalProperties": false
    },
    "device": {
      "type": "object",
      "properties": {
        "id": {
          "$ref": "#/$defs/id"
        },
        "role": {
          "enum": [
            "instrument",
            "effect",
            "utility"
          ]
        },
        "plugin": {
          "$ref": "#/$defs/plugin"
        },
        "enabled": {
          "type": "boolean"
        },
        "bypass": {
          "type": "boolean"
        },
        "stateAssetId": {
          "$ref": "#/$defs/id"
        },
        "onUnavailable": {
          "enum": [
            "reportAndPreserve",
            "preserveAndBypass",
            "preserveAndSilence"
          ]
        }
      },
      "required": [
        "id",
        "role",
        "plugin",
        "enabled",
        "bypass"
      ],
      "additionalProperties": false
    },
    "plugin": {
      "type": "object",
      "properties": {
        "format": {
          "enum": [
            "vst2",
            "vst3",
            "clap",
            "au",
            "aax",
            "builtin",
            "hostNative",
            "other"
          ]
        },
        "pluginId": {
          "type": "string",
          "minLength": 1
        },
        "vendor": {
          "type": "string",
          "minLength": 1
        },
        "name": {
          "type": "string",
          "minLength": 1
        },
        "version": {
          "type": "string",
          "minLength": 1
        },
        "namespace": {
          "type": "string",
          "minLength": 1
        }
      },
      "required": [
        "format",
        "pluginId",
        "name"
      ],
      "additionalProperties": false
    },
    "asset": {
      "type": "object",
      "properties": {
        "id": {
          "$ref": "#/$defs/id"
        },
        "purpose": {
          "enum": [
            "pluginState",
            "renderedAudio",
            "other",
            "audioSource"
          ]
        },
        "uri": {
          "type": "string",
          "minLength": 1
        },
        "sha256": {
          "$ref": "#/$defs/sha256"
        },
        "mediaType": {
          "type": "string",
          "minLength": 1
        },
        "byteLength": {
          "type": "integer",
          "minimum": 0
        },
        "sampleRateHz": {
          "type": "integer",
          "minimum": 1,
          "maximum": 768000,
          "description": "Audio-source decoded sample frames per second; required only for purpose audioSource."
        },
        "frameCount": {
          "type": "integer",
          "minimum": 1,
          "description": "Number of decoded sample frames in the complete audio source asset; required for audioSource."
        },
        "audioChannels": {
          "type": "integer",
          "enum": [
            1,
            2
          ],
          "description": "Mono/stereo decoded source-channel count; required only for audioSource in 0.2."
        }
      },
      "required": [
        "id",
        "purpose",
        "uri",
        "sha256"
      ],
      "additionalProperties": false,
      "allOf": [
        {
          "if": {
            "properties": {
              "purpose": {
                "const": "audioSource"
              }
            },
            "required": [
              "purpose"
            ]
          },
          "then": {
            "required": [
              "sampleRateHz",
              "frameCount",
              "audioChannels",
              "mediaType"
            ]
          },
          "else": {
            "not": {
              "anyOf": [
                {
                  "required": [
                    "sampleRateHz"
                  ]
                },
                {
                  "required": [
                    "frameCount"
                  ]
                },
                {
                  "required": [
                    "audioChannels"
                  ]
                }
              ]
            }
          }
        }
      ],
      "description": "Opaque asset descriptors. audioSource requires sampling metadata for frame-accurate regions; plug-in state remains uninterpreted and never executable merely by presence in JSON."
    },
    "automation": {
      "type": "object",
      "properties": {
        "id": {
          "$ref": "#/$defs/id"
        },
        "target": {
          "$ref": "#/$defs/automationTarget"
        },
        "valueType": {
          "enum": [
            "number",
            "boolean"
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
          "items": {
            "$ref": "#/$defs/point"
          },
          "minItems": 1
        }
      },
      "required": [
        "id",
        "target",
        "valueType",
        "interpolation",
        "points"
      ],
      "additionalProperties": false,
      "description": "Unique source-global-Tick automation lane. Boolean controls use step interpolation. A single lane per exact target; static value acts as baseline before first point where available. Device plugin parameters are normalized 0..1, while deviceControl.enabled/bypass are explicit booleans.",
      "allOf": [
        {
          "if": {
            "properties": {
              "valueType": {
                "const": "boolean"
              }
            },
            "required": [
              "valueType"
            ]
          },
          "then": {
            "properties": {
              "interpolation": {
                "const": "step"
              }
            }
          }
        }
      ]
    },
    "automationTarget": {
      "oneOf": [
        {
          "type": "object",
          "properties": {
            "kind": {
              "const": "channel"
            },
            "channelId": {
              "$ref": "#/$defs/id"
            },
            "parameter": {
              "enum": [
                "gainDb",
                "pan",
                "mute"
              ]
            }
          },
          "required": [
            "kind",
            "channelId",
            "parameter"
          ],
          "additionalProperties": false
        },
        {
          "type": "object",
          "properties": {
            "kind": {
              "const": "device"
            },
            "deviceId": {
              "$ref": "#/$defs/id"
            },
            "parameterId": {
              "type": "string",
              "minLength": 1
            }
          },
          "required": [
            "kind",
            "deviceId",
            "parameterId"
          ],
          "additionalProperties": false
        },
        {
          "type": "object",
          "additionalProperties": false,
          "properties": {
            "kind": {
              "const": "send"
            },
            "sendId": {
              "$ref": "#/$defs/id"
            },
            "parameter": {
              "enum": [
                "gainDb",
                "enabled"
              ]
            }
          },
          "required": [
            "kind",
            "sendId",
            "parameter"
          ]
        },
        {
          "type": "object",
          "additionalProperties": false,
          "properties": {
            "kind": {
              "const": "audioRegion"
            },
            "audioRegionId": {
              "$ref": "#/$defs/id"
            },
            "parameter": {
              "enum": [
                "gainDb",
                "mute"
              ]
            }
          },
          "required": [
            "kind",
            "audioRegionId",
            "parameter"
          ]
        },
        {
          "type": "object",
          "additionalProperties": false,
          "properties": {
            "kind": {
              "const": "deviceControl"
            },
            "deviceId": {
              "$ref": "#/$defs/id"
            },
            "parameter": {
              "enum": [
                "enabled",
                "bypass"
              ]
            }
          },
          "required": [
            "kind",
            "deviceId",
            "parameter"
          ]
        }
      ],
      "description": "Channel, plugin parameter, Send, audio Region, or Device slot control automation target. Non-channel options added to the unpublished 0.2 development draft. References resolve within this Production Profile, not into MIDI CC or Core Note IDs."
    },
    "point": {
      "type": "object",
      "properties": {
        "atTick": {
          "type": "integer",
          "minimum": 0
        },
        "value": {
          "oneOf": [
            {
              "type": "number"
            },
            {
              "type": "boolean"
            }
          ]
        }
      },
      "required": [
        "atTick",
        "value"
      ],
      "additionalProperties": false
    },
    "hostExtension": {
      "type": "object",
      "properties": {
        "namespace": {
          "type": "string",
          "pattern": "^[A-Za-z0-9]+(?:\\.[A-Za-z0-9-]+)+$"
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
        "data"
      ],
      "additionalProperties": false
    },
    "audioRegion": {
      "type": "object",
      "additionalProperties": false,
      "description": "Source-score-tick audio segment on a production track or score-bound track channel, referencing a bounded range of exact audioSource PCM-decoded frames.",
      "properties": {
        "id": {
          "$ref": "#/$defs/id"
        },
        "channelId": {
          "$ref": "#/$defs/id"
        },
        "sourceAssetId": {
          "$ref": "#/$defs/id"
        },
        "startTick": {
          "type": "integer",
          "minimum": 0
        },
        "durationTicks": {
          "type": "integer",
          "minimum": 1
        },
        "sourceStartFrame": {
          "type": "integer",
          "minimum": 0
        },
        "sourceFrameCount": {
          "type": "integer",
          "minimum": 1
        },
        "playbackMode": {
          "enum": [
            "native",
            "fit"
          ],
          "description": "native maps ideal source-time seconds to sample frames at sampleRateHz; fit uniformly maps authored global Tick progress to the selected frame interval."
        },
        "pitchPolicy": {
          "enum": [
            "preserve",
            "followRate"
          ],
          "description": "Required for fit; preserve means retain source pitch as a musical goal, followRate means speed/rate-based pitch change. Both are DSP/host dependent."
        },
        "gainDb": {
          "type": "number",
          "minimum": -120,
          "maximum": 24
        },
        "mute": {
          "type": "boolean"
        },
        "fadeInTicks": {
          "type": "integer",
          "minimum": 0
        },
        "fadeOutTicks": {
          "type": "integer",
          "minimum": 0
        }
      },
      "required": [
        "id",
        "channelId",
        "sourceAssetId",
        "startTick",
        "durationTicks",
        "sourceStartFrame",
        "sourceFrameCount",
        "playbackMode",
        "gainDb",
        "mute"
      ],
      "allOf": [
        {
          "if": {
            "properties": {
              "playbackMode": {
                "const": "fit"
              }
            },
            "required": [
              "playbackMode"
            ]
          },
          "then": {
            "required": [
              "pitchPolicy"
            ]
          },
          "else": {
            "not": {
              "required": [
                "pitchPolicy"
              ]
            }
          }
        }
      ]
    },
    "sidechainConnection": {
      "type": "object",
      "additionalProperties": false,
      "description": "Directed detector/key signal from sourceChannelId to named key input port of an effect Device belonging to a different audio channel. Does not mix into its audible output path.",
      "properties": {
        "id": {
          "$ref": "#/$defs/id"
        },
        "sourceChannelId": {
          "$ref": "#/$defs/id"
        },
        "targetDeviceId": {
          "$ref": "#/$defs/id"
        },
        "targetPortId": {
          "$ref": "#/$defs/id",
          "description": "Opaque plugin-format-scoped sidechain input identifier. A host must verify the port actually exists; no port auto-matching by label."
        },
        "tapPoint": {
          "enum": [
            "preFader",
            "postFader"
          ]
        },
        "followMute": {
          "type": "boolean",
          "description": "If true, source channel mute suppresses this sidechain; if false, the detector feed can remain present even when that source channel is muted audibly."
        },
        "gainDb": {
          "type": "number",
          "minimum": -120,
          "maximum": 24
        },
        "enabled": {
          "type": "boolean"
        }
      },
      "required": [
        "id",
        "sourceChannelId",
        "targetDeviceId",
        "targetPortId",
        "tapPoint",
        "followMute",
        "gainDb",
        "enabled"
      ]
    }
  }
}
```

## $defs / id



| Field | Required | Type | Constraints |
|---|---|---|---|

**Exact schema:**

```json
{
  "type": "string",
  "minLength": 1,
  "pattern": "^\\S+$"
}
```

## $defs / sha256



| Field | Required | Type | Constraints |
|---|---|---|---|

**Exact schema:**

```json
{
  "type": "string",
  "pattern": "^[0-9a-f]{64}$"
}
```

## $defs / score



| Field | Required | Type | Constraints |
|---|---|---|---|
| `formatVersion` | Yes | const 4.3.0 |  |
| `sha256` | Yes | ref sha256 |  |
| `documentId` | Optional / conditional | ref id |  |
| `revisionId` | Optional / conditional | ref id |  |
| `sourceUri` | Optional / conditional | string | minLength=1 |

**Exact schema:**

```json
{
  "type": "object",
  "properties": {
    "formatVersion": {
      "const": "4.3.0"
    },
    "sha256": {
      "$ref": "#/$defs/sha256"
    },
    "documentId": {
      "$ref": "#/$defs/id"
    },
    "revisionId": {
      "$ref": "#/$defs/id"
    },
    "sourceUri": {
      "type": "string",
      "minLength": 1
    }
  },
  "required": [
    "formatVersion",
    "sha256"
  ],
  "additionalProperties": false
}
```

## $defs / channel



| Field | Required | Type | Constraints |
|---|---|---|---|
| `id` | Yes | ref id |  |
| `kind` | Yes | enum track, audioTrack, bus, master | audioTrack is a production-only recorded-audio channel, and MUST NOT claim a Core trackId. kind track still maps an OSTF |
| `name` | Optional / conditional | string | minLength=1 |
| `trackId` | Optional / conditional | ref id |  |
| `audioChannels` | Yes | enum 1, 2 |  |
| `gainDb` | Yes | number | minimum=-120; maximum=24 |
| `pan` | Yes | number | minimum=-1; maximum=1 |
| `mute` | Yes | boolean |  |
| `solo` | Yes | boolean |  |
| `soloSafe` | Yes | boolean |  |
| `outputChannelId` | Optional / conditional | ref id |  |
| `deviceIds` | Yes | array | minItems=0; uniqueItems=True; items:ref id |
| `sends` | Optional / conditional | array | minItems=0; items:ref send |

**Exact schema:**

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "kind": {
      "enum": [
        "track",
        "audioTrack",
        "bus",
        "master"
      ],
      "description": "audioTrack is a production-only recorded-audio channel, and MUST NOT claim a Core trackId. kind track still maps an OSTF Track exactly as in 0.1."
    },
    "name": {
      "type": "string",
      "minLength": 1
    },
    "trackId": {
      "$ref": "#/$defs/id"
    },
    "audioChannels": {
      "enum": [
        1,
        2
      ]
    },
    "gainDb": {
      "type": "number",
      "minimum": -120,
      "maximum": 24
    },
    "pan": {
      "type": "number",
      "minimum": -1,
      "maximum": 1
    },
    "mute": {
      "type": "boolean"
    },
    "solo": {
      "type": "boolean"
    },
    "soloSafe": {
      "type": "boolean"
    },
    "outputChannelId": {
      "$ref": "#/$defs/id"
    },
    "deviceIds": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/id"
      },
      "minItems": 0,
      "uniqueItems": true
    },
    "sends": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/send"
      },
      "minItems": 0
    }
  },
  "required": [
    "id",
    "kind",
    "audioChannels",
    "gainDb",
    "pan",
    "mute",
    "solo",
    "soloSafe",
    "deviceIds"
  ],
  "additionalProperties": false
}
```

## $defs / send



| Field | Required | Type | Constraints |
|---|---|---|---|
| `id` | Yes | ref id |  |
| `targetChannelId` | Yes | ref id |  |
| `gainDb` | Yes | number | minimum=-120; maximum=24 |
| `preFader` | Yes | boolean |  |
| `enabled` | Yes | boolean |  |

**Exact schema:**

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "targetChannelId": {
      "$ref": "#/$defs/id"
    },
    "gainDb": {
      "type": "number",
      "minimum": -120,
      "maximum": 24
    },
    "preFader": {
      "type": "boolean"
    },
    "enabled": {
      "type": "boolean"
    }
  },
  "required": [
    "id",
    "targetChannelId",
    "gainDb",
    "preFader",
    "enabled"
  ],
  "additionalProperties": false
}
```

## $defs / device



| Field | Required | Type | Constraints |
|---|---|---|---|
| `id` | Yes | ref id |  |
| `role` | Yes | enum instrument, effect, utility |  |
| `plugin` | Yes | ref plugin |  |
| `enabled` | Yes | boolean |  |
| `bypass` | Yes | boolean |  |
| `stateAssetId` | Optional / conditional | ref id |  |
| `onUnavailable` | Optional / conditional | enum reportAndPreserve, preserveAndBypass, preserveAndSilence |  |

**Exact schema:**

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "role": {
      "enum": [
        "instrument",
        "effect",
        "utility"
      ]
    },
    "plugin": {
      "$ref": "#/$defs/plugin"
    },
    "enabled": {
      "type": "boolean"
    },
    "bypass": {
      "type": "boolean"
    },
    "stateAssetId": {
      "$ref": "#/$defs/id"
    },
    "onUnavailable": {
      "enum": [
        "reportAndPreserve",
        "preserveAndBypass",
        "preserveAndSilence"
      ]
    }
  },
  "required": [
    "id",
    "role",
    "plugin",
    "enabled",
    "bypass"
  ],
  "additionalProperties": false
}
```

## $defs / plugin



| Field | Required | Type | Constraints |
|---|---|---|---|
| `format` | Yes | enum vst2, vst3, clap, au, aax, builtin, hostNative, other |  |
| `pluginId` | Yes | string | minLength=1 |
| `vendor` | Optional / conditional | string | minLength=1 |
| `name` | Yes | string | minLength=1 |
| `version` | Optional / conditional | string | minLength=1 |
| `namespace` | Optional / conditional | string | minLength=1 |

**Exact schema:**

```json
{
  "type": "object",
  "properties": {
    "format": {
      "enum": [
        "vst2",
        "vst3",
        "clap",
        "au",
        "aax",
        "builtin",
        "hostNative",
        "other"
      ]
    },
    "pluginId": {
      "type": "string",
      "minLength": 1
    },
    "vendor": {
      "type": "string",
      "minLength": 1
    },
    "name": {
      "type": "string",
      "minLength": 1
    },
    "version": {
      "type": "string",
      "minLength": 1
    },
    "namespace": {
      "type": "string",
      "minLength": 1
    }
  },
  "required": [
    "format",
    "pluginId",
    "name"
  ],
  "additionalProperties": false
}
```

## $defs / asset

Opaque asset descriptors. audioSource requires sampling metadata for frame-accurate regions; plug-in state remains uninterpreted and never executable merely by presence in JSON.

| Field | Required | Type | Constraints |
|---|---|---|---|
| `id` | Yes | ref id |  |
| `purpose` | Yes | enum pluginState, renderedAudio, other, audioSource |  |
| `uri` | Yes | string | minLength=1 |
| `sha256` | Yes | ref sha256 |  |
| `mediaType` | Optional / conditional | string | minLength=1 |
| `byteLength` | Optional / conditional | integer | minimum=0 |
| `sampleRateHz` | Optional / conditional | integer | minimum=1; maximum=768000; Audio-source decoded sample frames per second; required only for purpose audioSource. |
| `frameCount` | Optional / conditional | integer | minimum=1; Number of decoded sample frames in the complete audio source asset; required for audioSource. |
| `audioChannels` | Optional / conditional | enum 1, 2 | Mono/stereo decoded source-channel count; required only for audioSource in 0.2. |

**Exact schema:**

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "purpose": {
      "enum": [
        "pluginState",
        "renderedAudio",
        "other",
        "audioSource"
      ]
    },
    "uri": {
      "type": "string",
      "minLength": 1
    },
    "sha256": {
      "$ref": "#/$defs/sha256"
    },
    "mediaType": {
      "type": "string",
      "minLength": 1
    },
    "byteLength": {
      "type": "integer",
      "minimum": 0
    },
    "sampleRateHz": {
      "type": "integer",
      "minimum": 1,
      "maximum": 768000,
      "description": "Audio-source decoded sample frames per second; required only for purpose audioSource."
    },
    "frameCount": {
      "type": "integer",
      "minimum": 1,
      "description": "Number of decoded sample frames in the complete audio source asset; required for audioSource."
    },
    "audioChannels": {
      "type": "integer",
      "enum": [
        1,
        2
      ],
      "description": "Mono/stereo decoded source-channel count; required only for audioSource in 0.2."
    }
  },
  "required": [
    "id",
    "purpose",
    "uri",
    "sha256"
  ],
  "additionalProperties": false,
  "allOf": [
    {
      "if": {
        "properties": {
          "purpose": {
            "const": "audioSource"
          }
        },
        "required": [
          "purpose"
        ]
      },
      "then": {
        "required": [
          "sampleRateHz",
          "frameCount",
          "audioChannels",
          "mediaType"
        ]
      },
      "else": {
        "not": {
          "anyOf": [
            {
              "required": [
                "sampleRateHz"
              ]
            },
            {
              "required": [
                "frameCount"
              ]
            },
            {
              "required": [
                "audioChannels"
              ]
            }
          ]
        }
      }
    }
  ],
  "description": "Opaque asset descriptors. audioSource requires sampling metadata for frame-accurate regions; plug-in state remains uninterpreted and never executable merely by presence in JSON."
}
```

## $defs / automation

Unique source-global-Tick automation lane. Boolean controls use step interpolation. A single lane per exact target; static value acts as baseline before first point where available. Device plugin parameters are normalized 0..1, while deviceControl.enabled/bypass are explicit booleans.

| Field | Required | Type | Constraints |
|---|---|---|---|
| `id` | Yes | ref id |  |
| `target` | Yes | ref automationTarget |  |
| `valueType` | Yes | enum number, boolean |  |
| `interpolation` | Yes | enum step, linear |  |
| `points` | Yes | array | minItems=1; items:ref point |

**Exact schema:**

```json
{
  "type": "object",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "target": {
      "$ref": "#/$defs/automationTarget"
    },
    "valueType": {
      "enum": [
        "number",
        "boolean"
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
      "items": {
        "$ref": "#/$defs/point"
      },
      "minItems": 1
    }
  },
  "required": [
    "id",
    "target",
    "valueType",
    "interpolation",
    "points"
  ],
  "additionalProperties": false,
  "description": "Unique source-global-Tick automation lane. Boolean controls use step interpolation. A single lane per exact target; static value acts as baseline before first point where available. Device plugin parameters are normalized 0..1, while deviceControl.enabled/bypass are explicit booleans.",
  "allOf": [
    {
      "if": {
        "properties": {
          "valueType": {
            "const": "boolean"
          }
        },
        "required": [
          "valueType"
        ]
      },
      "then": {
        "properties": {
          "interpolation": {
            "const": "step"
          }
        }
      }
    }
  ]
}
```

## $defs / automationTarget

Channel, plugin parameter, Send, audio Region, or Device slot control automation target. Non-channel options added to the unpublished 0.2 development draft. References resolve within this Production Profile, not into MIDI CC or Core Note IDs.

| Field | Required | Type | Constraints |
|---|---|---|---|

**Exact schema:**

```json
{
  "oneOf": [
    {
      "type": "object",
      "properties": {
        "kind": {
          "const": "channel"
        },
        "channelId": {
          "$ref": "#/$defs/id"
        },
        "parameter": {
          "enum": [
            "gainDb",
            "pan",
            "mute"
          ]
        }
      },
      "required": [
        "kind",
        "channelId",
        "parameter"
      ],
      "additionalProperties": false
    },
    {
      "type": "object",
      "properties": {
        "kind": {
          "const": "device"
        },
        "deviceId": {
          "$ref": "#/$defs/id"
        },
        "parameterId": {
          "type": "string",
          "minLength": 1
        }
      },
      "required": [
        "kind",
        "deviceId",
        "parameterId"
      ],
      "additionalProperties": false
    },
    {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "kind": {
          "const": "send"
        },
        "sendId": {
          "$ref": "#/$defs/id"
        },
        "parameter": {
          "enum": [
            "gainDb",
            "enabled"
          ]
        }
      },
      "required": [
        "kind",
        "sendId",
        "parameter"
      ]
    },
    {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "kind": {
          "const": "audioRegion"
        },
        "audioRegionId": {
          "$ref": "#/$defs/id"
        },
        "parameter": {
          "enum": [
            "gainDb",
            "mute"
          ]
        }
      },
      "required": [
        "kind",
        "audioRegionId",
        "parameter"
      ]
    },
    {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "kind": {
          "const": "deviceControl"
        },
        "deviceId": {
          "$ref": "#/$defs/id"
        },
        "parameter": {
          "enum": [
            "enabled",
            "bypass"
          ]
        }
      },
      "required": [
        "kind",
        "deviceId",
        "parameter"
      ]
    }
  ],
  "description": "Channel, plugin parameter, Send, audio Region, or Device slot control automation target. Non-channel options added to the unpublished 0.2 development draft. References resolve within this Production Profile, not into MIDI CC or Core Note IDs."
}
```

## $defs / point



| Field | Required | Type | Constraints |
|---|---|---|---|
| `atTick` | Yes | integer | minimum=0 |
| `value` | Yes | oneOf (2 alternatives) |  |

**Exact schema:**

```json
{
  "type": "object",
  "properties": {
    "atTick": {
      "type": "integer",
      "minimum": 0
    },
    "value": {
      "oneOf": [
        {
          "type": "number"
        },
        {
          "type": "boolean"
        }
      ]
    }
  },
  "required": [
    "atTick",
    "value"
  ],
  "additionalProperties": false
}
```

## $defs / hostExtension



| Field | Required | Type | Constraints |
|---|---|---|---|
| `namespace` | Yes | string | pattern=^[A-Za-z0-9]+(?:\.[A-Za-z0-9-]+)+$ |
| `version` | Optional / conditional | string | minLength=1 |
| `data` | Yes | object |  |

**Exact schema:**

```json
{
  "type": "object",
  "properties": {
    "namespace": {
      "type": "string",
      "pattern": "^[A-Za-z0-9]+(?:\\.[A-Za-z0-9-]+)+$"
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
    "data"
  ],
  "additionalProperties": false
}
```

## $defs / audioRegion

Source-score-tick audio segment on a production track or score-bound track channel, referencing a bounded range of exact audioSource PCM-decoded frames.

| Field | Required | Type | Constraints |
|---|---|---|---|
| `id` | Yes | ref id |  |
| `channelId` | Yes | ref id |  |
| `sourceAssetId` | Yes | ref id |  |
| `startTick` | Yes | integer | minimum=0 |
| `durationTicks` | Yes | integer | minimum=1 |
| `sourceStartFrame` | Yes | integer | minimum=0 |
| `sourceFrameCount` | Yes | integer | minimum=1 |
| `playbackMode` | Yes | enum native, fit | native maps ideal source-time seconds to sample frames at sampleRateHz; fit uniformly maps authored global Tick progress |
| `pitchPolicy` | Optional / conditional | enum preserve, followRate | Required for fit; preserve means retain source pitch as a musical goal, followRate means speed/rate-based pitch change.  |
| `gainDb` | Yes | number | minimum=-120; maximum=24 |
| `mute` | Yes | boolean |  |
| `fadeInTicks` | Optional / conditional | integer | minimum=0 |
| `fadeOutTicks` | Optional / conditional | integer | minimum=0 |

**Exact schema:**

```json
{
  "type": "object",
  "additionalProperties": false,
  "description": "Source-score-tick audio segment on a production track or score-bound track channel, referencing a bounded range of exact audioSource PCM-decoded frames.",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "channelId": {
      "$ref": "#/$defs/id"
    },
    "sourceAssetId": {
      "$ref": "#/$defs/id"
    },
    "startTick": {
      "type": "integer",
      "minimum": 0
    },
    "durationTicks": {
      "type": "integer",
      "minimum": 1
    },
    "sourceStartFrame": {
      "type": "integer",
      "minimum": 0
    },
    "sourceFrameCount": {
      "type": "integer",
      "minimum": 1
    },
    "playbackMode": {
      "enum": [
        "native",
        "fit"
      ],
      "description": "native maps ideal source-time seconds to sample frames at sampleRateHz; fit uniformly maps authored global Tick progress to the selected frame interval."
    },
    "pitchPolicy": {
      "enum": [
        "preserve",
        "followRate"
      ],
      "description": "Required for fit; preserve means retain source pitch as a musical goal, followRate means speed/rate-based pitch change. Both are DSP/host dependent."
    },
    "gainDb": {
      "type": "number",
      "minimum": -120,
      "maximum": 24
    },
    "mute": {
      "type": "boolean"
    },
    "fadeInTicks": {
      "type": "integer",
      "minimum": 0
    },
    "fadeOutTicks": {
      "type": "integer",
      "minimum": 0
    }
  },
  "required": [
    "id",
    "channelId",
    "sourceAssetId",
    "startTick",
    "durationTicks",
    "sourceStartFrame",
    "sourceFrameCount",
    "playbackMode",
    "gainDb",
    "mute"
  ],
  "allOf": [
    {
      "if": {
        "properties": {
          "playbackMode": {
            "const": "fit"
          }
        },
        "required": [
          "playbackMode"
        ]
      },
      "then": {
        "required": [
          "pitchPolicy"
        ]
      },
      "else": {
        "not": {
          "required": [
            "pitchPolicy"
          ]
        }
      }
    }
  ]
}
```

## $defs / sidechainConnection

Directed detector/key signal from sourceChannelId to named key input port of an effect Device belonging to a different audio channel. Does not mix into its audible output path.

| Field | Required | Type | Constraints |
|---|---|---|---|
| `id` | Yes | ref id |  |
| `sourceChannelId` | Yes | ref id |  |
| `targetDeviceId` | Yes | ref id |  |
| `targetPortId` | Yes | ref id | Opaque plugin-format-scoped sidechain input identifier. A host must verify the port actually exists; no port auto-matchi |
| `tapPoint` | Yes | enum preFader, postFader |  |
| `followMute` | Yes | boolean | If true, source channel mute suppresses this sidechain; if false, the detector feed can remain present even when that so |
| `gainDb` | Yes | number | minimum=-120; maximum=24 |
| `enabled` | Yes | boolean |  |

**Exact schema:**

```json
{
  "type": "object",
  "additionalProperties": false,
  "description": "Directed detector/key signal from sourceChannelId to named key input port of an effect Device belonging to a different audio channel. Does not mix into its audible output path.",
  "properties": {
    "id": {
      "$ref": "#/$defs/id"
    },
    "sourceChannelId": {
      "$ref": "#/$defs/id"
    },
    "targetDeviceId": {
      "$ref": "#/$defs/id"
    },
    "targetPortId": {
      "$ref": "#/$defs/id",
      "description": "Opaque plugin-format-scoped sidechain input identifier. A host must verify the port actually exists; no port auto-matching by label."
    },
    "tapPoint": {
      "enum": [
        "preFader",
        "postFader"
      ]
    },
    "followMute": {
      "type": "boolean",
      "description": "If true, source channel mute suppresses this sidechain; if false, the detector feed can remain present even when that source channel is muted audibly."
    },
    "gainDb": {
      "type": "number",
      "minimum": -120,
      "maximum": 24
    },
    "enabled": {
      "type": "boolean"
    }
  },
  "required": [
    "id",
    "sourceChannelId",
    "targetDeviceId",
    "targetPortId",
    "tapPoint",
    "followMute",
    "gainDb",
    "enabled"
  ]
}
```

## Automation target compatibility — Draft 0.15

| Kind | Identifier | Parameter / value type | Introduced |
|---|---|---|---|
| `channel` | `channelId` | gainDb number, pan number, mute boolean | 0.1 |
| `device` | `deviceId` | plugin parameterId normalized number | 0.1 |
| `send` | `sendId` | gainDb number, enabled boolean | 0.2 pre-release |
| `audioRegion` | `audioRegionId` | gainDb number, mute boolean | 0.2 pre-release |
| `deviceControl` | `deviceId` | enabled boolean, bypass boolean | 0.2 pre-release |

Boolean lanes MUST use step; each full typed target MUST have at most one lane; points are source-score global ticks and recur under source Visit repeats. References, scalar parameter ranges, and source lifetime behavior require semantic validation. A 0.2 → 0.1 downgrade loses all lanes with new target kinds; disclose each lane ID.

## Cross-object semantic checks

- Exactly one Master, unique Channel/Device/Asset/Send/Region/Automation IDs, and one ownership per Device chain.
- Score-bound `trackId` resolves to Core Track; `audioTrack` has none; score SHA-256 pins exact original bytes.
- Audio Region references valid audioSource and channel; frame range, channel count, and fades are bounded.
- Output/Send/Sidechain dependency graph is acyclic, and a sidechain target is an owned effect device port.
- All Automation Target references resolve; type/interpolation/value range and unique target/point-order constraints apply.
- URI strings are data; external resources or plug-ins are never automatically fetched/executed.
- Runtime DSP/audio restoration and independent DAW/plugin compatibility are NOT certified.


## Draft 0.16 — interpretation of existing Mixer flags (no new parameters)

`channels[].solo` and `channels[].soloSafe` remain required booleans in the 0.2 Schema; neither becomes a new Automation target. `solo` on source Channels selects those sources; `solo` on a Bus selects source Channels reaching the Bus through current enabled sends/outputs; source `soloSafe` keeps that source selected during Solo; Bus `soloSafe` only keeps an already-selected routed signal eligible and is not an unconditional upstream source selector. Master Solo/SoloSafe do not select sources. Channel `mute` is stronger than Solo for audible output. `track.enabled` of Core is limited to Score-derived content, independent Production audio Regions remain subject to Region and Channel mute. See `PRODUCTION_SESSION_PROFILE.md` §22 for the complete candidate algorithm and host deviation reporting. A local asset URI must resolve inside the Profile's directory after symbolic-link resolution. No Schema field, enum, requiredness or other `$defs` entry changed in Draft 0.16.

## Draft 0.17 — Interpretation of `assets[].uri` (no new properties)

The original `uri` string is the authoritative serialized value. Production Profile 0.2's additional portable rule is strictly once-decoded UTF-8 POSIX URI path segments for *relative* Asset references, bundle-root/symlink containment and rejection of decoded dot segments, encoded separators, residual percent escapes, invalid UTF-8 and platform-reserved filenames. `safe_asset_uri` in the bundled helper is an authoring aid, not an operating-system security guarantee. For examples and the precise rule see `PRODUCTION_SESSION_PROFILE.md` §23.1. No numeric field, enum, `$defs` count or Schema property is changed by Draft 0.17.

`performancePlans[].visits[].parts[].realization` is owned by Music Core, not by any production audio Region; see Production Specification §23.2. An explicitly authored Region remains independent of a Score `silent` Part.

## Draft 0.18 — Interpretation note (no changes to field declarations)

All Profile 0.2 parameter names, requiredness, value ranges and `$defs` are unchanged. `audioRegions[].startTick`, `durationTicks`, `sourceStartFrame`, `sourceFrameCount`, `playbackMode`, `fadeInTicks` and `fadeOutTicks` are interpreted against original source Score Tick even when finite Performance Plans skip or repeat ranges. `automation[].points[].atTick` is likewise source-global. Values are re-evaluated from the whole lane on each selected source Tick; before the first point an opaque `kind:"device"` numeric parameter cannot be determined from the typed Profile alone. Detailed proposed normative semantics: `PRODUCTION_SESSION_PROFILE.md` §24 / `PRODUCTION_SESSION_PROFILE.ja.md` §24. No schema changes or app runtime guarantees are implied.
