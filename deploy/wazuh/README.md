# Wazuh Deployment

Use the official Wazuh Docker repository rather than copying a large vendor Compose stack
into this portfolio repository.

## Prerequisites

- Linux host or VM
- Docker Engine and Docker Compose plugin
- At least 8 GB RAM for a comfortable small lab
- `vm.max_map_count=262144`
- An isolated lab network

## Bootstrap

Review `bootstrap.sh`, then run:

```bash
cd deploy/wazuh
chmod +x bootstrap.sh
./bootstrap.sh
```

The script checks out the pinned stable Wazuh Docker tag and prints the official certificate
and startup commands. It does not silently start services or alter firewall rules.

At the time this repository was prepared, stable `4.14.5` was selected instead of Wazuh 5
beta or a release candidate. Review the official releases and update `WAZUH_VERSION` before
deployment when appropriate.

## Post-deployment

1. Change every default credential.
2. Limit dashboard access to the management interface.
3. Enroll one endpoint at a time.
4. Confirm time synchronization.
5. Apply `config/wazuh/agent-collection.xml` snippets.
6. Add `config/wazuh/local_rules.xml` after validating IDs do not conflict.
7. Capture versions and sanitized screenshots in `live-evidence/` locally.

Official documentation:

- https://documentation.wazuh.com/current/deployment-options/docker/
- https://github.com/wazuh/wazuh-docker

