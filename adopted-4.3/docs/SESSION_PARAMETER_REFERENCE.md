> **Current document edition: Draft 0.69 (unratified).** Older Draft headings and snapshot notes are retained as history. D01–D05 remain pending.

> **Historical editorial snapshot: Draft 0.59 (unratified).** Existing headings referring to earlier Drafts describe cumulative editorial proposals, not competing active document versions. The exact versioned Schemas remain unchanged; the single current release gate is [RELEASE_READINESS.md](RELEASE_READINESS.md). Publisher acceptance D01–D05 is still pending; runtime/independent tests are excluded, not passed.

# OSTF Distributed Session Profile 0.2 — Full Parameter Reference (Draft 0.53 editorial edition; Schema unchanged)

**Unratified development specification.** These fields belong to a separate JSON profile, never in `.ostf` Core.

Structural authority: `schema/ostf-distributed-session-0.2.schema.json`.
Semantic authority: `docs/SESSION_STATE_MACHINE.md` and `docs/SESSION_PROFILE.md`.

The root is `oneOf` Snapshot or Event. Both **require** `performancePlanId` and `scoreSha256`; an optional nested Position must reference the same Plan. `scoreSha256` is a lowercase 64-digit digest of the **exact original UTF-8 OSTF source bytes**, not a semantic hash.

## All definitions (including nested payloads)

## `id`

No object properties (primitive or union).

**Complete JSON Schema definition:**

```json
{
  "type": "string",
  "minLength": 1
}
```

## `participant`

| Field | Type/schema summary | Direct required |
| --- | --- | --- |
| `participantId` | `{"$ref":"#/$defs/id"}` | Yes |
| `kind` | `{"enum":["human","softwareAgent","physicalRobot"]}` | Yes |
| `assignedTrackIds` | `{"type":"array","items":{"$ref":"#/$defs/id"},"uniqueItems":true}` | Yes |
| `supportedFeatures` | `{"type":"array","items":{"type":"string","minLength":1},"uniqueItems":true}` | No/Conditional |
| `capabilities` | `{"type":"object","description":"Untrusted advisory data, not robot actuator authorization","additionalProperties":true}` | No/Conditional |

**Complete JSON Schema definition:**

```json
{
  "type": "object",
  "properties": {
    "participantId": {
      "$ref": "#/$defs/id"
    },
    "kind": {
      "enum": [
        "human",
        "softwareAgent",
        "physicalRobot"
      ]
    },
    "assignedTrackIds": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/id"
      },
      "uniqueItems": true
    },
    "supportedFeatures": {
      "type": "array",
      "items": {
        "type": "string",
        "minLength": 1
      },
      "uniqueItems": true
    },
    "capabilities": {
      "type": "object",
      "description": "Untrusted advisory data, not robot actuator authorization",
      "additionalProperties": true
    }
  },
  "required": [
    "participantId",
    "kind",
    "assignedTrackIds"
  ],
  "additionalProperties": false
}
```

## `position`

| Field | Type/schema summary | Direct required |
| --- | --- | --- |
| `performancePlanId` | `{"$ref":"#/$defs/id"}` | Yes |
| `visitId` | `{"$ref":"#/$defs/id"}` | Yes |
| `sourceTick` | `{"type":"integer","minimum":0}` | Yes |
| `performanceTick` | `{"type":"integer","minimum":0}` | Yes |
| `clockDomainId` | `{"$ref":"#/$defs/id"}` | Yes |
| `epochUtc` | `{"type":"string","format":"date-time"}` | Yes |
| `uncertaintyMs` | `{"type":"number","minimum":0}` | Yes |
| `tempoBpm` | `{"type":"number","exclusiveMinimum":0}` | No/Conditional |

**Complete JSON Schema definition:**

```json
{
  "type": "object",
  "properties": {
    "performancePlanId": {
      "$ref": "#/$defs/id"
    },
    "visitId": {
      "$ref": "#/$defs/id"
    },
    "sourceTick": {
      "type": "integer",
      "minimum": 0
    },
    "performanceTick": {
      "type": "integer",
      "minimum": 0
    },
    "clockDomainId": {
      "$ref": "#/$defs/id"
    },
    "epochUtc": {
      "type": "string",
      "format": "date-time"
    },
    "uncertaintyMs": {
      "type": "number",
      "minimum": 0
    },
    "tempoBpm": {
      "type": "number",
      "exclusiveMinimum": 0
    }
  },
  "required": [
    "performancePlanId",
    "visitId",
    "sourceTick",
    "performanceTick",
    "clockDomainId",
    "epochUtc",
    "uncertaintyMs"
  ],
  "additionalProperties": false,
  "description": "epochUtc denotes the clock-domain estimate for the explicitly stated performanceTick (at the sourceTick). Clock synchronization algorithm is out of scope."
}
```

## `note`

| Field | Type/schema summary | Direct required |
| --- | --- | --- |
| `startTick` | `{"type":"integer","minimum":0}` | Yes |
| `durationTicks` | `{"type":"integer","minimum":1}` | Yes |
| `pitch` | `{"type":"integer","minimum":0,"maximum":127}` | Yes |
| `velocity` | `{"type":"integer","minimum":1,"maximum":127}` | Yes |

**Complete JSON Schema definition:**

```json
{
  "type": "object",
  "properties": {
    "startTick": {
      "type": "integer",
      "minimum": 0
    },
    "durationTicks": {
      "type": "integer",
      "minimum": 1
    },
    "pitch": {
      "type": "integer",
      "minimum": 0,
      "maximum": 127
    },
    "velocity": {
      "type": "integer",
      "minimum": 1,
      "maximum": 127
    }
  },
  "required": [
    "startTick",
    "durationTicks",
    "pitch",
    "velocity"
  ],
  "additionalProperties": false,
  "description": "MIDI-like note within a proposed session phrase, not a new authoritative OSTF Core Note."
}
```

## `phrase`

| Field | Type/schema summary | Direct required |
| --- | --- | --- |
| `representation` | `{"const":"midi1Notes"}` | Yes |
| `durationTicks` | `{"type":"integer","minimum":1}` | Yes |
| `notes` | `{"type":"array","items":{"$ref":"#/$defs/note"},"minItems":1}` | Yes |

**Complete JSON Schema definition:**

```json
{
  "type": "object",
  "properties": {
    "representation": {
      "const": "midi1Notes"
    },
    "durationTicks": {
      "type": "integer",
      "minimum": 1
    },
    "notes": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/note"
      },
      "minItems": 1
    }
  },
  "required": [
    "representation",
    "durationTicks",
    "notes"
  ],
  "additionalProperties": false,
  "description": "A portable minimal pitched-note session phrase. No lyrics, MPE, instrument actuation or audio realization is implied. Notes are relative to phrase start/effectivePerformanceTick."
}
```

## `committedPhrase`

| Field | Type/schema summary | Direct required |
| --- | --- | --- |
| `commitEventId` | `{"$ref":"#/$defs/id"}` | Yes |
| `proposalId` | `{"$ref":"#/$defs/id"}` | Yes |
| `targetTrackId` | `{"$ref":"#/$defs/id"}` | Yes |
| `effectivePerformanceTick` | `{"type":"integer","minimum":0}` | Yes |
| `phrase` | `{"$ref":"#/$defs/phrase"}` | Yes |

**Complete JSON Schema definition:**

```json
{
  "type": "object",
  "properties": {
    "commitEventId": {
      "$ref": "#/$defs/id"
    },
    "proposalId": {
      "$ref": "#/$defs/id"
    },
    "targetTrackId": {
      "$ref": "#/$defs/id"
    },
    "effectivePerformanceTick": {
      "type": "integer",
      "minimum": 0
    },
    "phrase": {
      "$ref": "#/$defs/phrase"
    }
  },
  "required": [
    "commitEventId",
    "proposalId",
    "targetTrackId",
    "effectivePerformanceTick",
    "phrase"
  ],
  "additionalProperties": false
}
```

## `snapshot`

| Field | Type/schema summary | Direct required |
| --- | --- | --- |
| `profile` | `{"const":"OSTF-Distributed-Session-0.2"}` | Yes |
| `recordType` | `{"const":"snapshot"}` | Yes |
| `sessionId` | `{"$ref":"#/$defs/id"}` | Yes |
| `documentId` | `{"$ref":"#/$defs/id"}` | Yes |
| `revisionId` | `{"$ref":"#/$defs/id"}` | Yes |
| `performancePlanId` | `{"$ref":"#/$defs/id","description":"Required pinned finite 4.3 Core performancePlans[].id, also in prepared or stopped Snapshots; positions must match this ID."}` | Yes |
| `scoreSha256` | `{"type":"string","pattern":"^[0-9a-f]{64}$","description":"SHA-256 lowercase hex over the exact UTF-8 OSTF source document bytes after HTTP Content-Encoding removal and before parsing; byte identity pin only, not authentication or semantic normalization."}` | Yes |
| `sessionStatus` | `{"enum":["prepared","playing","stopped"],"description":"Authoritative session lifecycle state; not participant availability or network connection status."}` | Yes |
| `stateRevision` | `{"type":"integer","minimum":0}` | Yes |
| `authorityParticipantId` | `{"$ref":"#/$defs/id"}` | Yes |
| `participants` | `{"type":"array","items":{"$ref":"#/$defs/participant"},"minItems":1}` | Yes |
| `position` | `{"$ref":"#/$defs/position"}` | No/Conditional |
| `committedPhrases` | `{"type":"array","items":{"$ref":"#/$defs/committedPhrase"},"description":"Self-contained accepted phrases for late joiners; only active/future material is required for live join, full archive required for full replay claims."}` | No/Conditional |
| `commitmentWindow` | `{"$ref":"#/$defs/commitmentWindow","description":"Optional truthful late-join phrase completeness assertion. Only allowed in playing Snapshots with position; absent means no completeness claim, not an empty session."}` | No/Conditional |

**Complete JSON Schema definition:**

```json
{
  "type": "object",
  "properties": {
    "profile": {
      "const": "OSTF-Distributed-Session-0.2"
    },
    "recordType": {
      "const": "snapshot"
    },
    "sessionId": {
      "$ref": "#/$defs/id"
    },
    "documentId": {
      "$ref": "#/$defs/id"
    },
    "revisionId": {
      "$ref": "#/$defs/id"
    },
    "performancePlanId": {
      "$ref": "#/$defs/id",
      "description": "Required pinned finite 4.3 Core performancePlans[].id, also in prepared or stopped Snapshots; positions must match this ID."
    },
    "scoreSha256": {
      "type": "string",
      "pattern": "^[0-9a-f]{64}$",
      "description": "SHA-256 lowercase hex over the exact UTF-8 OSTF source document bytes after HTTP Content-Encoding removal and before parsing; byte identity pin only, not authentication or semantic normalization."
    },
    "sessionStatus": {
      "enum": [
        "prepared",
        "playing",
        "stopped"
      ],
      "description": "Authoritative session lifecycle state; not participant availability or network connection status."
    },
    "stateRevision": {
      "type": "integer",
      "minimum": 0
    },
    "authorityParticipantId": {
      "$ref": "#/$defs/id"
    },
    "participants": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/participant"
      },
      "minItems": 1
    },
    "position": {
      "$ref": "#/$defs/position"
    },
    "committedPhrases": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/committedPhrase"
      },
      "description": "Self-contained accepted phrases for late joiners; only active/future material is required for live join, full archive required for full replay claims."
    },
    "commitmentWindow": {
      "$ref": "#/$defs/commitmentWindow",
      "description": "Optional truthful late-join phrase completeness assertion. Only allowed in playing Snapshots with position; absent means no completeness claim, not an empty session."
    }
  },
  "required": [
    "profile",
    "recordType",
    "sessionId",
    "documentId",
    "revisionId",
    "performancePlanId",
    "scoreSha256",
    "sessionStatus",
    "stateRevision",
    "authorityParticipantId",
    "participants"
  ],
  "additionalProperties": false,
  "allOf": [
    {
      "if": {
        "properties": {
          "sessionStatus": {
            "const": "playing"
          }
        },
        "required": [
          "sessionStatus"
        ]
      },
      "then": {
        "required": [
          "position"
        ]
      }
    },
    {
      "if": {
        "required": [
          "commitmentWindow"
        ]
      },
      "then": {
        "required": [
          "position",
          "committedPhrases"
        ],
        "properties": {
          "sessionStatus": {
            "const": "playing"
          }
        }
      }
    }
  ],
  "description": "A playing Session Snapshot must have a pinned Plan/Visit clock position. Prepared/stopped may omit position. Only the current authority can certify an authoritative Snapshot. Draft 0.5: commitmentWindow asserts complete accepted phrase coverage as of stateRevision; absence makes no completeness guarantee. Draft 0.9 requires a pinned Plan and exact score-byte digest on every 0.2 Snapshot/Event, including positionless prepared snapshots. Draft 0.12: a Snapshot has at least one Participant so the required authority identity can resolve."
}
```

## `phraseProposedPayload`

| Field | Type/schema summary | Direct required |
| --- | --- | --- |
| `proposalId` | `{"$ref":"#/$defs/id"}` | Yes |
| `targetTrackId` | `{"$ref":"#/$defs/id"}` | Yes |
| `phrase` | `{"$ref":"#/$defs/phrase"}` | Yes |

**Complete JSON Schema definition:**

```json
{
  "type": "object",
  "properties": {
    "proposalId": {
      "$ref": "#/$defs/id"
    },
    "targetTrackId": {
      "$ref": "#/$defs/id"
    },
    "phrase": {
      "$ref": "#/$defs/phrase"
    }
  },
  "required": [
    "proposalId",
    "targetTrackId",
    "phrase"
  ],
  "additionalProperties": false
}
```

## `phraseCommittedPayload`

| Field | Type/schema summary | Direct required |
| --- | --- | --- |
| `proposalId` | `{"$ref":"#/$defs/id"}` | Yes |
| `targetTrackId` | `{"$ref":"#/$defs/id"}` | Yes |
| `phrase` | `{"$ref":"#/$defs/phrase"}` | Yes |

**Complete JSON Schema definition:**

```json
{
  "type": "object",
  "properties": {
    "proposalId": {
      "$ref": "#/$defs/id"
    },
    "targetTrackId": {
      "$ref": "#/$defs/id"
    },
    "phrase": {
      "$ref": "#/$defs/phrase"
    }
  },
  "required": [
    "proposalId",
    "targetTrackId",
    "phrase"
  ],
  "additionalProperties": false
}
```

## `turnRequestedPayload`

| Field | Type/schema summary | Direct required |
| --- | --- | --- |
| `targetTrackId` | `{"$ref":"#/$defs/id"}` | Yes |
| `requestedRole` | `{"type":"string","minLength":1}` | Yes |
| `requestedVisitId` | `{"$ref":"#/$defs/id"}` | No/Conditional |

**Complete JSON Schema definition:**

```json
{
  "type": "object",
  "properties": {
    "targetTrackId": {
      "$ref": "#/$defs/id"
    },
    "requestedRole": {
      "type": "string",
      "minLength": 1
    },
    "requestedVisitId": {
      "$ref": "#/$defs/id"
    }
  },
  "required": [
    "targetTrackId",
    "requestedRole"
  ],
  "additionalProperties": false
}
```

## `cueIssuedPayload`

| Field | Type/schema summary | Direct required |
| --- | --- | --- |
| `cueId` | `{"$ref":"#/$defs/id"}` | Yes |
| `targetVisitId` | `{"$ref":"#/$defs/id"}` | No/Conditional |

**Complete JSON Schema definition:**

```json
{
  "type": "object",
  "properties": {
    "cueId": {
      "$ref": "#/$defs/id"
    },
    "targetVisitId": {
      "$ref": "#/$defs/id"
    }
  },
  "required": [
    "cueId"
  ],
  "additionalProperties": false
}
```

## `performanceObservedPayload`

| Field | Type/schema summary | Direct required |
| --- | --- | --- |
| `observedParticipantId` | `{"$ref":"#/$defs/id"}` | Yes |
| `sourceTrackId` | `{"$ref":"#/$defs/id"}` | Yes |
| `confidence` | `{"type":"number","minimum":0,"maximum":1}` | Yes |
| `features` | `{"type":"object","additionalProperties":true}` | No/Conditional |

**Complete JSON Schema definition:**

```json
{
  "type": "object",
  "properties": {
    "observedParticipantId": {
      "$ref": "#/$defs/id"
    },
    "sourceTrackId": {
      "$ref": "#/$defs/id"
    },
    "confidence": {
      "type": "number",
      "minimum": 0,
      "maximum": 1
    },
    "features": {
      "type": "object",
      "additionalProperties": true
    }
  },
  "required": [
    "observedParticipantId",
    "sourceTrackId",
    "confidence"
  ],
  "additionalProperties": false
}
```

## `participantStatusPayload`

| Field | Type/schema summary | Direct required |
| --- | --- | --- |
| `participantId` | `{"$ref":"#/$defs/id"}` | Yes |
| `availability` | `{"enum":["ready","busy","disconnected"]}` | Yes |
| `message` | `{"type":"string"}` | No/Conditional |

**Complete JSON Schema definition:**

```json
{
  "type": "object",
  "properties": {
    "participantId": {
      "$ref": "#/$defs/id"
    },
    "availability": {
      "enum": [
        "ready",
        "busy",
        "disconnected"
      ]
    },
    "message": {
      "type": "string"
    }
  },
  "required": [
    "participantId",
    "availability"
  ],
  "additionalProperties": false
}
```

## `sessionStateChangedPayload`

| Field | Type/schema summary | Direct required |
| --- | --- | --- |
| `changeKind` | `{"enum":["sessionStarted","visitChanged","assignmentChanged","sessionStopped"]}` | Yes |
| `targetVisitId` | `{"$ref":"#/$defs/id"}` | No/Conditional |
| `participantId` | `{"$ref":"#/$defs/id"}` | No/Conditional |
| `assignedTrackIds` | `{"type":"array","items":{"$ref":"#/$defs/id"},"uniqueItems":true}` | No/Conditional |
| `position` | `{"$ref":"#/$defs/position","description":"Authoritative anchored musical/clock position for prepared-to-playing transition; position.performanceTick MUST equal enclosing effectivePerformanceTick (semantic rule)."}` | No/Conditional |

**Complete JSON Schema definition:**

```json
{
  "type": "object",
  "properties": {
    "changeKind": {
      "enum": [
        "sessionStarted",
        "visitChanged",
        "assignmentChanged",
        "sessionStopped"
      ]
    },
    "targetVisitId": {
      "$ref": "#/$defs/id"
    },
    "participantId": {
      "$ref": "#/$defs/id"
    },
    "assignedTrackIds": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/id"
      },
      "uniqueItems": true
    },
    "position": {
      "$ref": "#/$defs/position",
      "description": "Authoritative Plan/Visit/source/performance Tick and clock-domain/UTC anchor. Required for sessionStarted and visitChanged; position.performanceTick MUST equal event effectivePerformanceTick. For visitChanged, position.visitId MUST equal targetVisitId at that Visit start."
    }
  },
  "required": [
    "changeKind"
  ],
  "additionalProperties": false,
  "allOf": [
    {
      "if": {
        "properties": {
          "changeKind": {
            "const": "sessionStarted"
          }
        },
        "required": [
          "changeKind"
        ]
      },
      "then": {
        "required": [
          "position"
        ],
        "not": {
          "anyOf": [
            {
              "required": [
                "targetVisitId"
              ]
            },
            {
              "required": [
                "participantId"
              ]
            },
            {
              "required": [
                "assignedTrackIds"
              ]
            }
          ]
        }
      }
    },
    {
      "if": {
        "properties": {
          "changeKind": {
            "const": "visitChanged"
          }
        },
        "required": [
          "changeKind"
        ]
      },
      "then": {
        "required": [
          "targetVisitId",
          "position"
        ],
        "not": {
          "anyOf": [
            {
              "required": [
                "participantId"
              ]
            },
            {
              "required": [
                "assignedTrackIds"
              ]
            }
          ]
        }
      }
    },
    {
      "if": {
        "properties": {
          "changeKind": {
            "const": "assignmentChanged"
          }
        },
        "required": [
          "changeKind"
        ]
      },
      "then": {
        "required": [
          "participantId",
          "assignedTrackIds"
        ],
        "not": {
          "anyOf": [
            {
              "required": [
                "targetVisitId"
              ]
            },
            {
              "required": [
                "position"
              ]
            }
          ]
        }
      }
    },
    {
      "if": {
        "properties": {
          "changeKind": {
            "const": "sessionStopped"
          }
        },
        "required": [
          "changeKind"
        ]
      },
      "then": {
        "not": {
          "anyOf": [
            {
              "required": [
                "targetVisitId"
              ]
            },
            {
              "required": [
                "participantId"
              ]
            },
            {
              "required": [
                "assignedTrackIds"
              ]
            },
            {
              "required": [
                "position"
              ]
            }
          ]
        }
      }
    }
  ],
  "description": "Authoritative sessionStarted and visitChanged both supply an explicit musical/UTC Position anchor. assignmentChanged changes assignments only and MUST NOT carry position or targetVisitId; sessionStopped is immediate."
}
```

## `event`

| Field | Type/schema summary | Direct required |
| --- | --- | --- |
| `profile` | `{"const":"OSTF-Distributed-Session-0.2"}` | Yes |
| `recordType` | `{"const":"event"}` | Yes |
| `eventId` | `{"$ref":"#/$defs/id"}` | Yes |
| `sessionId` | `{"$ref":"#/$defs/id"}` | Yes |
| `documentId` | `{"$ref":"#/$defs/id"}` | Yes |
| `revisionId` | `{"$ref":"#/$defs/id"}` | Yes |
| `performancePlanId` | `{"$ref":"#/$defs/id","description":"Required pinned finite 4.3 Core performancePlans[].id, also in prepared or stopped Snapshots; positions must match this ID."}` | Yes |
| `scoreSha256` | `{"type":"string","pattern":"^[0-9a-f]{64}$","description":"SHA-256 lowercase hex over the exact UTF-8 OSTF source document bytes after HTTP Content-Encoding removal and before parsing; byte identity pin only, not authentication or semantic normalization."}` | Yes |
| `baseStateRevision` | `{"type":"integer","minimum":0}` | Yes |
| `resultStateRevision` | `{"type":"integer","minimum":0}` | No/Conditional |
| `issuerParticipantId` | `{"$ref":"#/$defs/id"}` | Yes |
| `kind` | `{"enum":["phraseProposed","phraseCommitted","turnRequested","cueIssued","performanceObserved","participantStatus","sessionStateChanged"]}` | Yes |
| `effectivePerformanceTick` | `{"type":"integer","minimum":0}` | Yes |
| `payload` | `{"type":"object"}` | Yes |

**Complete JSON Schema definition:**

```json
{
  "type": "object",
  "properties": {
    "profile": {
      "const": "OSTF-Distributed-Session-0.2"
    },
    "recordType": {
      "const": "event"
    },
    "eventId": {
      "$ref": "#/$defs/id"
    },
    "sessionId": {
      "$ref": "#/$defs/id"
    },
    "documentId": {
      "$ref": "#/$defs/id"
    },
    "revisionId": {
      "$ref": "#/$defs/id"
    },
    "performancePlanId": {
      "$ref": "#/$defs/id",
      "description": "Required pinned finite 4.3 Core performancePlans[].id, also in prepared or stopped Snapshots; positions must match this ID."
    },
    "scoreSha256": {
      "type": "string",
      "pattern": "^[0-9a-f]{64}$",
      "description": "SHA-256 lowercase hex over the exact UTF-8 OSTF source document bytes after HTTP Content-Encoding removal and before parsing; byte identity pin only, not authentication or semantic normalization."
    },
    "baseStateRevision": {
      "type": "integer",
      "minimum": 0
    },
    "resultStateRevision": {
      "type": "integer",
      "minimum": 0
    },
    "issuerParticipantId": {
      "$ref": "#/$defs/id"
    },
    "kind": {
      "enum": [
        "phraseProposed",
        "phraseCommitted",
        "turnRequested",
        "cueIssued",
        "performanceObserved",
        "participantStatus",
        "sessionStateChanged"
      ]
    },
    "effectivePerformanceTick": {
      "type": "integer",
      "minimum": 0
    },
    "payload": {
      "type": "object"
    }
  },
  "required": [
    "profile",
    "recordType",
    "eventId",
    "sessionId",
    "documentId",
    "revisionId",
    "performancePlanId",
    "scoreSha256",
    "baseStateRevision",
    "issuerParticipantId",
    "kind",
    "effectivePerformanceTick",
    "payload"
  ],
  "additionalProperties": false,
  "oneOf": [
    {
      "properties": {
        "kind": {
          "const": "phraseProposed"
        },
        "payload": {
          "$ref": "#/$defs/phraseProposedPayload"
        }
      },
      "required": [
        "kind",
        "payload"
      ],
      "not": {
        "required": [
          "resultStateRevision"
        ]
      }
    },
    {
      "properties": {
        "kind": {
          "const": "phraseCommitted"
        },
        "payload": {
          "$ref": "#/$defs/phraseCommittedPayload"
        }
      },
      "required": [
        "kind",
        "payload",
        "resultStateRevision"
      ]
    },
    {
      "properties": {
        "kind": {
          "const": "turnRequested"
        },
        "payload": {
          "$ref": "#/$defs/turnRequestedPayload"
        }
      },
      "required": [
        "kind",
        "payload"
      ],
      "not": {
        "required": [
          "resultStateRevision"
        ]
      }
    },
    {
      "properties": {
        "kind": {
          "const": "cueIssued"
        },
        "payload": {
          "$ref": "#/$defs/cueIssuedPayload"
        }
      },
      "required": [
        "kind",
        "payload"
      ],
      "not": {
        "required": [
          "resultStateRevision"
        ]
      }
    },
    {
      "properties": {
        "kind": {
          "const": "performanceObserved"
        },
        "payload": {
          "$ref": "#/$defs/performanceObservedPayload"
        }
      },
      "required": [
        "kind",
        "payload"
      ],
      "not": {
        "required": [
          "resultStateRevision"
        ]
      }
    },
    {
      "properties": {
        "kind": {
          "const": "participantStatus"
        },
        "payload": {
          "$ref": "#/$defs/participantStatusPayload"
        }
      },
      "required": [
        "kind",
        "payload"
      ],
      "not": {
        "required": [
          "resultStateRevision"
        ]
      }
    },
    {
      "properties": {
        "kind": {
          "const": "sessionStateChanged"
        },
        "payload": {
          "$ref": "#/$defs/sessionStateChangedPayload"
        }
      },
      "required": [
        "kind",
        "payload",
        "resultStateRevision"
      ]
    }
  ],
  "description": "Authorized state changes must increment base revision by exactly 1. Proposals and observations never increment revision. See SESSION_STATE_MACHINE.md. Draft 0.9 requires a pinned Plan and exact score-byte digest on every 0.2 Snapshot/Event, including positionless prepared snapshots."
}
```

## `commitmentWindow`

| Field | Type/schema summary | Direct required |
| --- | --- | --- |
| `startPerformanceTick` | `{"type":"integer","minimum":0}` | Yes |
| `endPerformanceTick` | `{"type":"integer","minimum":1}` | Yes |

**Complete JSON Schema definition:**

```json
{
  "type": "object",
  "properties": {
    "startPerformanceTick": {
      "type": "integer",
      "minimum": 0
    },
    "endPerformanceTick": {
      "type": "integer",
      "minimum": 1
    }
  },
  "required": [
    "startPerformanceTick",
    "endPerformanceTick"
  ],
  "additionalProperties": false,
  "description": "Optional assertion that all accepted committed phrases intersecting half-open [startPerformanceTick, endPerformanceTick) are listed in committedPhrases for the Snapshot stateRevision. Semantic validator MUST check start < end and intersection/completeness against authority log."
}
```

## Draft 0.9 cross-document invariants (not representable by this Schema)

1. The root `performancePlanId` MUST resolve to an exact, finite OSTF 4.3 `performancePlans[].id` on the pinned document; it is mandatory even for `prepared` Snapshots without `position`.
2. When `position` exists (including inside `sessionStarted`), its `performancePlanId` MUST equal the record root `performancePlanId`. Source/performance Tick mapping and Visit references MUST resolve under that Plan.
3. Root `scoreSha256` MUST equal the SHA-256 of the *actual pinned OSTF source bytes*; changed byte content is a conflict even when `documentId`/`revisionId` are unchanged. The field does not confer trust/authorization or canonicalize JSON.
4. A `phraseCommitted` or retained `committedPhrase` MUST fit one explicitly `open` Part of the same pinned finite Plan and must not overlap accepted Track phrases; other Session 0.2 constraints remain in `SESSION_STATE_MACHINE.md`.
5. Earlier unpublished 0.2 Draft examples without both root fields must be explicitly re-authored. The already distinct Profile 0.1 is not silently upgraded.

No independently implemented parser, WAN, robot or DAW claims follow from this editorial reference.

## Draft 0.10 Visit re-anchoring requirement (not expressible by JSON Schema alone)

- On `changeKind:"visitChanged"`, both `targetVisitId` and `position` are mandatory; `assignmentChanged` must still not include either. No new `$defs` or Core 4.3 property is introduced.
- `position.visitId == targetVisitId`, `position.performanceTick == event.effectivePerformanceTick == pinned target Visit.startPerformanceTick`; `position.sourceTick` maps to the first source Tick of that Visit, and the inner Plan ID equals the pinned envelope Plan.
- `position.epochUtc` estimates the UTC clock-domain time associated with the asserted Performance Tick, not time of receipt. The new anchor must be usable to interpret the authorized jump without extrapolating a prior Visit's tempo/clock mapping across a skipped interval.
- Check Session authority, frozen Score tuple and forward-only transition before adopting the anchor. Clock-domain synchronization, command dispatch, safe robot timing and actually sounded notes remain external.
- Unpublished Draft 0.9 Profile 0.2 `visitChanged` Events with no `position` must be explicitly updated; Profile 0.1 is not silently migrated.

## Draft 0.11 — Cross-document semantic constraints on existing fields

- `position.clockDomainId`: on an accepted `sessionStarted`, establishes the authoritative musical clock domain for that playing Session; every later playing Snapshot and `visitChanged` Position MUST match. Cannot authenticate the real clock or certify accuracy.
- `position.tempoBpm`: optional, **descriptive**; if supplied, MUST numerically equal the effective `timeline.tempoChanges[].bpm` at its mapped source Tick. A missing source tempo cannot be filled by a Session hint.
- `event.effectivePerformanceTick`: a phrase start or a musical context depending on Event kind. For `sessionStopped`, audit/context only—NOT a future stop and NOT a claim that a physical robot stopped.

All requiredness and numeric bounds in the published Draft 0.10 Profile 0.2 Schema are unchanged in Draft 0.11. The detailed proposed rules are in `SESSION_STATE_MACHINE.md`. This appendix does not impose a new parameter name.
