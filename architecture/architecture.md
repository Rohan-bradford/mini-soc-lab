# Architecture

## Objective

Create a small, isolated SOC environment that produces endpoint, identity, network, and web
telemetry and supports repeatable detection and incident-response exercises.

## Components

| Asset | Suggested specification | Purpose |
| --- | --- | --- |
| `soc-wazuh-01` | Ubuntu, 4 vCPU, 8 GB RAM, 80 GB disk | Wazuh manager, indexer, dashboard |
| `win-endpoint-01` | Windows 11, 2 vCPU, 4 GB RAM | Sysmon, Windows logs, Wazuh agent |
| `linux-endpoint-01` | Ubuntu, 2 vCPU, 2 GB RAM | SSH, audit/auth logs, Juice Shop |
| `sensor-01` | Ubuntu, 2 vCPU, 2 GB RAM | Suricata EVE JSON network sensor |
| `analyst-01` | Ubuntu/Kali, 2 vCPU, 2 GB RAM | Authorized simulation and investigation |

For a memory-constrained host, combine `sensor-01`, `linux-endpoint-01`, and `analyst-01`,
but document the reduced isolation.

## Network Plan

Use a hypervisor **internal** or **host-only** network:

```text
SOC-LAB: 10.10.10.0/24

10.10.10.10  soc-wazuh-01
10.10.10.20  win-endpoint-01
10.10.10.30  linux-endpoint-01
10.10.10.40  sensor-01
10.10.10.50  analyst-01
```

Use NAT only for controlled package updates. Do not bridge Juice Shop, DVWA, SSH test
services, or Wazuh administrative interfaces onto an untrusted network.

## Trust Boundaries

1. **Management boundary:** Wazuh dashboard and API are accessible only from the host and
   analyst VM.
2. **Endpoint boundary:** Windows and Linux agents initiate telemetry connections to Wazuh.
3. **Sensor boundary:** Suricata observes mirrored/test traffic and forwards only logs.
4. **Vulnerable-app boundary:** Juice Shop binds to the lab address, never `0.0.0.0` on a
   publicly reachable interface.
5. **Evidence boundary:** Git contains only sanitized excerpts, hashes, reports, and images.

## Data Flows

| Source | Transport/path | Destination | Data |
| --- | --- | --- | --- |
| Windows | Wazuh agent | Wazuh manager | Security, PowerShell, Defender, Sysmon |
| Linux | Wazuh agent | Wazuh manager | auth.log, audit, system logs |
| Suricata | Agent file collection | Wazuh manager | `/var/log/suricata/eve.json` |
| Juice Shop | Container/file collection | Wazuh manager | HTTP access/application logs |
| Wazuh manager | Internal pipeline | Indexer | Alerts and normalized events |
| Indexer | HTTPS | Dashboard | Searches, visualizations, investigations |

## Retention

- Raw lab telemetry: 7 days
- Alerts: 30 days
- Git samples: fewer than 20 sanitized events per scenario
- Incident reports: retained without credentials or private identifiers

## Recovery

Take snapshots after:

1. Operating-system installation
2. Agent enrollment
3. Telemetry configuration
4. Detection deployment

Revert after simulations that modify users, groups, services, or vulnerable applications.

