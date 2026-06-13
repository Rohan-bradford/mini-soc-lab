#!/usr/bin/env bash
set -euo pipefail

WAZUH_VERSION="${WAZUH_VERSION:-v4.14.5}"
TARGET_DIR="${TARGET_DIR:-wazuh-docker}"

if ! command -v git >/dev/null 2>&1; then
  echo "git is required" >&2
  exit 1
fi

if ! command -v docker >/dev/null 2>&1; then
  echo "Docker is not installed. Install Docker Engine and the Compose plugin first." >&2
  exit 1
fi

if [[ -e "$TARGET_DIR" ]]; then
  echo "Refusing to overwrite existing path: $TARGET_DIR" >&2
  exit 1
fi

git clone --depth 1 --branch "$WAZUH_VERSION" \
  https://github.com/wazuh/wazuh-docker.git "$TARGET_DIR"

cat <<EOF
Official Wazuh Docker files checked out at: $TARGET_DIR

Review the vendor README and configuration before continuing.
Typical single-node commands are:

  cd $TARGET_DIR/single-node
  docker compose -f generate-indexer-certs.yml run --rm generator
  docker compose up -d

Do not expose the dashboard publicly. Change default credentials immediately.
EOF

