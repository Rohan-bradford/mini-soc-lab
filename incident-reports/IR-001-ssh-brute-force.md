# IR-001: SSH Password Guessing

**Severity:** Medium  
**Status:** Closed  
**Evidence:** Synthetic lab telemetry  
**ATT&CK:** T1110.001 Password Guessing

## Executive Summary

Six failed SSH authentication attempts targeted the `demo` account on
`linux-endpoint-01` from `10.10.10.50` within two minutes. The source was confirmed as the
authorized analyst VM. No successful authentication followed the failures and no impact was
observed.

## Timeline

| Time UTC | Event |
| --- | --- |
| 09:08:20 | First failed password for `demo` |
| 09:08:40 | Second failure from the same source |
| 09:09:00-09:10:00 | Four additional failures |
| 09:10:05 | Correlation threshold met |
| 09:12:00 | Source confirmed as authorized simulation |

## Investigation

- Reviewed `/var/log/auth.log` events by source, account, and destination.
- Searched for `Accepted password`, `Accepted publickey`, and session-open events.
- Confirmed `10.10.10.50` belonged to `analyst-01`.
- Checked for failures against other accounts and found none.
- Checked Suricata flows for other activity from the source during the window.

## Root Cause

An approved password-guessing simulation intentionally submitted incorrect credentials.
Password authentication remained enabled to support the exercise.

## Response

No emergency containment was required. The account was checked for lockout and the source
was not blocked because it was an approved tester.

## Remediation

- Transition SSH administration to key-based authentication.
- Disable password authentication after completing the exercise.
- Restrict SSH to the management subnet.
- Elevate severity when failures are followed by a successful login.

## Lessons Learned

Threshold detections need success-after-failure correlation and a documented scanner/tester
allowlist. Source allowlisting should suppress notifications, not discard underlying events.

