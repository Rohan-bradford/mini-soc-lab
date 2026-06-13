# Evidence Handling

## Collection

Capture the smallest useful time window and record:

- Source system and clock/timezone
- Collection command or dashboard query
- File hash
- Collector and date
- Case identifier

## Sanitization

Remove:

- Passwords, tokens, cookies, API keys, and certificates
- Public or employer/customer addresses
- Personal names and email addresses
- Full packet captures
- Unrelated events

Use private lab addresses and fictional account names in published excerpts.

## Integrity

Hash source evidence before analysis:

```bash
sha256sum evidence-file
```

Work from a copy, keep notes chronological, and separate facts from analyst interpretation.

## Git Policy

Do not commit `.pcap`, `.evtx`, private keys, VM images, database files, or bulk raw logs.
Commit only minimal sanitized excerpts needed to support a detection or report.

