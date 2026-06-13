# IR-003: Local Administrator Group Membership Change

**Severity:** High  
**Status:** Closed  
**Evidence:** Synthetic lab telemetry  
**ATT&CK:** T1098 Account Manipulation

## Executive Summary

Windows Security Event ID 4732 showed `temporary-admin` added to the local Administrators
group on `win-endpoint-01`. Privileged group changes require authorization validation. The
change belonged to an approved lab exercise and was rolled back immediately.

## Timeline

| Time UTC | Event |
| --- | --- |
| 09:05:00 | Temporary local account created |
| 09:05:10 | Account added to Administrators |
| 09:05:15 | Detection generated |
| 09:06:00 | Analyst confirmed approved exercise |
| 09:07:00 | Membership and temporary account removed |

## Investigation

- Identified actor, target member, group, endpoint, and logon session.
- Verified the actor was the lab analyst.
- Searched for other account/group changes in the surrounding hour.
- Reviewed process creation for the PowerShell cmdlets involved.
- Verified the account did not create persistence or remote sessions.

## Root Cause

Controlled simulation of unauthorized privilege assignment.

## Containment and Recovery

The member was removed from Administrators and the temporary account was deleted. A
follow-up membership inventory confirmed only expected administrators remained.

## Recommendations

- Require change records for privileged membership changes.
- Alert on additions and removals, retaining actor/session context.
- Maintain separate standard and administrative identities.
- Perform periodic local administrator inventory.

