# Learning Roadmap

## 1. Networking Fundamentals

Learn:

- IPv4 addressing and subnetting
- TCP/UDP, ports, handshakes, and connection states
- DNS, HTTP, TLS, SSH, and NAT
- Firewalls, routing, VLANs, and packet capture

Practice:

- Read packets in Wireshark.
- Explain a DNS lookup and HTTPS connection packet by packet.
- Build an isolated virtual network and prove its boundaries.

## 2. Windows Security Telemetry

Learn:

- Windows Event Log structure
- Security Event IDs 4624, 4625, 4688, 4720, 4728/4732
- Sysmon process, network, DNS, file, and registry events
- PowerShell Script Block logging
- Users, groups, services, scheduled tasks, and Defender

Practice:

- Reconstruct a process tree.
- Trace an account from failed login to privileged group membership.

## 3. Linux Administration and Logging

Learn:

- Users, groups, permissions, `sudo`, SSH, systemd, and package management
- `auth.log`, journald, auditd, cron, and firewall logging
- Docker basics, volumes, networks, and least privilege

Practice:

- Harden SSH without locking yourself out.
- Correlate an SSH session with process and network activity.

## 4. SIEM and Log Engineering

Learn:

- Collection, parsing, normalization, indexing, retention, and time synchronization
- Wazuh manager, agents, indexer, dashboard, rules, decoders, and FIM
- Search syntax, aggregation, timelines, dashboards, and alert severity

Practice:

- Onboard one source at a time.
- Diagnose missing events from source to dashboard.

## 5. Detection Engineering

Learn:

- Detection hypotheses and data requirements
- Sigma structure and Wazuh rule concepts
- Threshold, sequence, anomaly, and indicator detections
- Baselines, false positives, precision/recall, testing, and tuning
- MITRE ATT&CK mapping

Practice:

- Write positive and negative test cases.
- Explain what each rule misses and how it can be bypassed.

## 6. Network Security Monitoring

Learn:

- Suricata signatures, flow records, and EVE JSON
- Zeek connection, DNS, HTTP, TLS, and file logs
- IDS versus IPS and sensor placement

Practice:

- Reconstruct a web request using endpoint and network logs.
- Detect a port sweep without relying only on a signature alert.

## 7. Incident Response and Forensics

Learn:

- Preparation, identification, containment, eradication, recovery, lessons learned
- Evidence preservation, timelines, scoping, root-cause analysis, and case notes
- Process trees, persistence, account activity, and network correlation

Practice:

- Write reports that separate facts, assumptions, and conclusions.
- Defend your severity and containment decisions.

## 8. Vulnerability Management

Learn:

- CVE, CWE, CVSS, exploitability versus exposure
- Authenticated scanning, validation, prioritization, remediation, and rescanning
- Secure configuration benchmarks

Practice:

- Remediate one real lab finding and prove the risk changed.

## 9. Automation and Git

Learn:

- Python, PowerShell, Bash, JSON, YAML, XML, and regular expressions
- Git branches, pull requests, code review, CI, and secret hygiene
- Detection-as-code validation

Practice:

- Add a ninth scenario with a rule, samples, tests, dashboard query, report, and playbook.

## Suggested 10-Week Order

| Week | Focus | Deliverable |
| --- | --- | --- |
| 1 | Networking and virtualization | Isolated network diagram |
| 2 | Linux and Docker | Hardened Ubuntu endpoint |
| 3 | Windows logging and Sysmon | Verified endpoint telemetry |
| 4 | Wazuh operation | Searchable Windows/Linux logs |
| 5 | Suricata and web logs | Network dashboard |
| 6 | Detection engineering | Four tested rules |
| 7 | Remaining detections | Eight tested rules |
| 8 | Incident response | Four case reports |
| 9 | Vulnerability management | Remediation and rescan |
| 10 | Portfolio polish | Live screenshots and final README |

## Interview Preparation

Be ready to explain:

- Why the network is isolated
- How a log reaches Wazuh
- Why each threshold was chosen
- How you tested false positives
- Difference between an alert and an incident
- How you established root cause
- What you would change in production
- Which evidence is live and which is synthetic

