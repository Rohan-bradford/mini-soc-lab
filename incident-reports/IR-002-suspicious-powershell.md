# IR-002: Suspicious PowerShell Command Line

**Severity:** High  
**Status:** Closed  
**Evidence:** Synthetic lab telemetry  
**ATT&CK:** T1059.001 PowerShell

## Executive Summary

Sysmon recorded PowerShell running with `-NonInteractive` and `-EncodedCommand` on
`win-endpoint-01`. Encoded commands can obscure behavior, so the event was treated as
high-priority until decoded. The content resolved to a harmless string-output command used
by the approved simulation.

## Evidence

- Event: Sysmon process creation, Event ID 1
- Image: `powershell.exe`
- User: lab analyst
- Flags: `-NoProfile -NonInteractive -EncodedCommand`
- Parent and network activity: no suspicious follow-on behavior in the synthetic case

## Investigation

1. Preserved the original command line.
2. Decoded the Base64 as UTF-16LE in an offline text-only workflow.
3. Confirmed the decoded command only printed `SOC-LAB-SAFE-TEST`.
4. Reviewed the process tree, file creation, registry, DNS, and network events.
5. Confirmed the timing matched the approved simulation window.

## Root Cause

Authorized detection testing intentionally used suspicious flags with harmless command
content.

## Response

No isolation was required after validation. The event remained in the case record to prove
the rule and triage process.

## Recommendations

- Correlate command-line flags with parent process, signer, user, and outbound traffic.
- Enable PowerShell Script Block and Module logging.
- Alert more strongly when encoded PowerShell writes executables, changes persistence, or
  connects to rare external destinations.

## Lessons Learned

Encoded content is a lead, not a verdict. Analysts must safely decode and correlate context
before declaring malicious activity.

