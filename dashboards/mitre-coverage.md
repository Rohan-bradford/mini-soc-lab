# MITRE ATT&CK Coverage

| Technique | Name | Detection | Data source |
| --- | --- | --- | --- |
| T1046 | Network Service Discovery | Internal TCP port sweep | Suricata flow |
| T1059.001 | PowerShell | Suspicious PowerShell flags | Sysmon process creation |
| T1071.004 | DNS | Beacon-like reserved-domain queries | Suricata DNS |
| T1098 | Account Manipulation | Administrators group addition | Windows Security |
| T1110 | Brute Force | Windows failures | Windows Security |
| T1110.001 | Password Guessing | SSH failures | Linux auth |
| T1190 | Exploit Public-Facing Application | Web attack indicators | Web/Suricata |
| T1204 | User Execution | Harmless hash test | Sysmon/FIM |

Coverage means the lab has a documented telemetry source and test rule. It does not imply
complete detection of every implementation of the technique.

