# IR-004: Web Attack Indicators Against Juice Shop

**Severity:** High  
**Status:** Closed  
**Evidence:** Synthetic lab telemetry  
**ATT&CK:** T1190 Exploit Public-Facing Application

## Executive Summary

Two requests containing SQL-injection and path-traversal indicators targeted the isolated
Juice Shop service from `analyst-01`. Responses were errors and no evidence showed code
execution, file disclosure, authentication bypass, or persistence. The traffic was an
approved simulation.

## Evidence

| Source | Request | Response |
| --- | --- | --- |
| `10.10.10.50` | Product search containing `' or 1=1--` | 400 |
| `10.10.10.50` | `/assets/../../etc/passwd` style path | 404 |

User agent: `SOC-Lab-Safe-Simulator/1.0`

## Investigation

1. Correlated application, reverse-proxy, Suricata HTTP, and endpoint logs.
2. Confirmed the source was the authorized test VM.
3. Reviewed response status and byte counts.
4. Searched the container/host for process, file, and authentication changes.
5. Confirmed no suspicious outbound traffic followed the requests.

## Root Cause

An approved test submitted recognizable attack strings to verify web telemetry and detection.

## Response

No blocking was required after source validation. The disposable application was restarted
to demonstrate a clean recovery action.

## Recommendations

- Preserve decoded and raw URI fields.
- Correlate web indicators with response size/status and host activity.
- Place vulnerable applications on isolated networks.
- Rebuild disposable containers after meaningful security tests.
- Avoid marking every attack string as a confirmed exploit.

