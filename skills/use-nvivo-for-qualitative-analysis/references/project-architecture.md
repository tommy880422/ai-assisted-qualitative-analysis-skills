# NVivo Project Architecture

## Start With a Data Dictionary

| Object | Naming rule | Required metadata | Purpose |
|---|---|---|---|
| Source file | Stable ID + source type + date | origin, consent, language, status | Primary data |
| Case | Stable case ID | case type and permitted attributes | Unit of analysis |
| Code | Analytic label | definition, version, origin | Meaning or analytic category |
| Memo | Object ID + memo type | author, date, version | Analytic and method record |
| Set | Purpose + date | static or rule-based logic | Temporary or persistent grouping |
| Relationship | Relation type + direction | evidence and memo | Explicit analytic relation |

Avoid personal names in object labels when disclosure is a risk.

## Suggested Top-Level Organization

- primary data by source type or study phase;
- contextual and secondary materials;
- cases and classifications;
- codes organized by analytic role only when hierarchy is meaningful;
- memos separated into source, code, category, method, reflexive, and theory types;
- queries saved by research question and version;
- outputs and exports;
- archive or superseded items clearly marked.

## Import Checklist

- preserve an untouched original outside NVivo;
- anonymize or document controlled identifiers;
- check text encoding, language, page or paragraph boundaries, timestamps, speaker names, and transcript-media synchronization;
- assign source type and collection metadata;
- verify all expected files and row counts;
- record exclusions, failed imports, and transformations;
- link transcripts, field notes, debriefs, and related media without collapsing their distinct evidentiary roles.

## Backup and Repair

- use dated, versioned backups in more than one approved location;
- close or coordinate project access before copying;
- test opening a backup periodically;
- maintain a change log for structural revisions;
- use project repair only on a copy;
- preserve exchange exports when long-term portability matters.

Never experiment on the sole live project.
