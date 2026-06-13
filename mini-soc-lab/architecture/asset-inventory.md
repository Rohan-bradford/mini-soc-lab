# Asset Inventory

| Asset ID | Role | Owner | Criticality | Logging | Exposure |
| --- | --- | --- | --- | --- | --- |
| SOC-001 | Wazuh SIEM | Lab owner | High | Local + Wazuh | Management network |
| WIN-001 | Windows endpoint | Lab owner | Medium | Sysmon/Security/Defender | Lab only |
| LNX-001 | Linux endpoint | Lab owner | Medium | auth/audit/container | Lab only |
| NET-001 | Suricata sensor | Lab owner | Medium | EVE JSON | Passive/lab only |
| APP-001 | OWASP Juice Shop | Lab owner | Low | HTTP/application | Lab only |
| ANA-001 | Analyst/test system | Lab owner | Medium | Shell history/audit | Lab only |

## Data Classification

All assets and identities are fictional. No customer, employer, or production information
belongs in this lab or repository.

