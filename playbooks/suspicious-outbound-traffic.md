# Playbook: Suspicious Outbound DNS or HTTP

1. Identify endpoint, process, user, destination, protocol, and timing pattern.
2. Validate whether the domain is reserved lab infrastructure or expected software.
3. Correlate Sysmon process/network data with Suricata DNS/HTTP/TLS records.
4. Look for periodicity, rare destinations, unusual user agents, and high-entropy subdomains.
5. Isolate the endpoint if malicious command-and-control is plausible.
6. Block confirmed malicious indicators at DNS, proxy, and firewall layers.
7. Preserve volatile evidence and determine the initial execution vector.
8. Tune allowlists narrowly, using process and destination context.

