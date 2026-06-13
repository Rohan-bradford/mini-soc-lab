# SOC Playbooks

| Playbook | Primary trigger |
| --- | --- |
| Brute-force response | Repeated authentication failures |
| Suspicious PowerShell response | Encoded/hidden/noninteractive PowerShell |
| Privileged account change | Administrator membership change |
| Web attack response | Injection or traversal indicators |
| File hash response | Known or suspicious hash |
| Suspicious outbound traffic | DNS/HTTP beacon or rare destination |

Each playbook should be exercised, timed, and revised during the live lab. Production
playbooks also require ownership, escalation contacts, legal requirements, and service-level
targets.

