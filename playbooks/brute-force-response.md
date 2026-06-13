# Playbook: Brute-Force Authentication

## Trigger

Five or more failures from one source in five minutes, or a successful authentication after
repeated failures.

## Triage

1. Validate source, destination, account, protocol, and time window.
2. Determine whether the source is an approved scanner or administrator.
3. Search for successful logons from the same source/account.
4. Review other targeted accounts and hosts.
5. Assign severity: Medium for failures only; High if followed by success.

## Containment

- Disable or reset the affected lab account if compromise is plausible.
- Block the source at the lab firewall after confirming it is not required infrastructure.
- Preserve relevant authentication and network logs.

## Recovery

Restore access with a strong credential, enable MFA where supported, and confirm no
unauthorized sessions remain.

## Closure Evidence

Timeline, affected accounts, source reputation/ownership, containment action, and tuned rule.

