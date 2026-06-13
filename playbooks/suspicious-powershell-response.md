# Playbook: Suspicious PowerShell

1. Capture host, user, parent process, command line, hashes, and network connections.
2. Decode command content in an offline text-only workflow; do not execute it.
3. Determine whether the activity belongs to approved administration.
4. Search for sibling processes, file writes, registry changes, DNS, and outbound traffic.
5. Isolate the endpoint if malicious behavior is supported by evidence.
6. Remove persistence, reset exposed credentials, and scan the host.
7. Restore from a trusted snapshot/image when integrity cannot be established.
8. Document the process tree, scope, root cause, and detection improvements.

