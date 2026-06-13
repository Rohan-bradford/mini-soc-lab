# Safe Simulation Catalog

Run simulations only on the isolated lab network after taking snapshots. Every procedure has
a rollback step and a synthetic-only alternative.

| ID | Scenario | Preferred method | Rollback |
| --- | --- | --- | --- |
| SIM-001 | Windows failed logons | Intentionally mistype lab account password | Unlock/reset lab account |
| SIM-002 | Suspicious PowerShell | Write a harmless encoded string to stdout | Delete transcript/test file |
| SIM-003 | Admin group addition | Add temporary lab user, then remove it | Remove membership and account |
| SIM-004 | Test-file hash | Create known harmless text file | Delete file |
| SIM-005 | Port scan | Scan one owned VM at low rate | None |
| SIM-006 | SSH failures | Mistype password against owned SSH VM | Unlock/reset lab account |
| SIM-007 | Web indicators | Request harmless malformed URLs from Juice Shop | Restart disposable container |
| SIM-008 | DNS pattern | Query `.invalid` test domain six times | None |

## Safety Rules

- Target only `10.10.10.0/24` lab assets.
- Keep scan rates low.
- Never download or execute malware.
- Use `.invalid`, `.test`, or `.example` domains.
- Do not disable endpoint protection.
- Stop immediately if traffic leaves the isolated network.
- Prefer `scripts/generate_sample_logs.py` when no live lab is available.

Detailed commands and evidence expectations are in each scenario file.

