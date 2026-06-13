from __future__ import annotations

import hashlib
import json
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
BASE = datetime(2026, 6, 13, 9, 0, tzinfo=timezone.utc)
TEST_CONTENT = b"MINI-SOC-LAB-HARMLESS-TEST-FILE\n"


def timestamp(offset: int) -> str:
    return (BASE + timedelta(seconds=offset)).isoformat().replace("+00:00", "Z")


def write_ndjson(relative: str, events: list[dict[str, Any]]) -> None:
    path = ROOT / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        "".join(json.dumps(event, sort_keys=True) + "\n" for event in events),
        encoding="utf-8",
    )


def main() -> None:
    windows: list[dict[str, Any]] = []
    for index in range(6):
        windows.append(
            {
                "@timestamp": timestamp(index * 20),
                "scenario": "windows_failed_logons",
                "event_id": 4625,
                "host": "win-endpoint-01",
                "source_ip": "10.10.10.50",
                "target_user": "lab-user",
                "status": "failure",
            }
        )
    windows.extend(
        [
            {
                "@timestamp": timestamp(200),
                "scenario": "windows_suspicious_powershell",
                "event_id": 1,
                "host": "win-endpoint-01",
                "image": "C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe",
                "command_line": "powershell.exe -NoProfile -NonInteractive -EncodedCommand TEST",
                "note": "Synthetic command line; TEST is not executable payload data.",
            },
            {
                "@timestamp": timestamp(300),
                "scenario": "windows_admin_group_add",
                "event_id": 4732,
                "host": "win-endpoint-01",
                "actor": "SOC-LAB\\analyst",
                "member": "SOC-LAB\\temporary-admin",
                "target_group": "Administrators",
            },
            {
                "@timestamp": timestamp(400),
                "scenario": "windows_test_hash",
                "event_id": 11,
                "host": "win-endpoint-01",
                "target_filename": "C:\\SOC-Lab\\harmless-test.txt",
                "sha256": hashlib.sha256(TEST_CONTENT).hexdigest().upper(),
            },
        ]
    )
    write_ndjson("sample-logs/windows/events.ndjson", windows)

    linux = [
        {
            "@timestamp": timestamp(500 + index * 20),
            "scenario": "linux_ssh_bruteforce",
            "service": "sshd",
            "host": "linux-endpoint-01",
            "source_ip": "10.10.10.50",
            "user": "demo",
            "message": "Failed password for demo from 10.10.10.50 port 54321 ssh2",
        }
        for index in range(6)
    ]
    write_ndjson("sample-logs/linux/auth.ndjson", linux)

    network: list[dict[str, Any]] = []
    for index, port in enumerate(range(20, 40)):
        network.append(
            {
                "timestamp": timestamp(700 + index),
                "scenario": "network_port_scan",
                "event_type": "flow",
                "src_ip": "10.10.10.50",
                "dest_ip": "10.10.10.30",
                "dest_port": port,
                "proto": "TCP",
            }
        )
    for index in range(6):
        network.append(
            {
                "timestamp": timestamp(900 + index * 60),
                "scenario": "network_dns_beacon",
                "event_type": "dns",
                "src_ip": "10.10.10.20",
                "dns": {"type": "query", "rrname": "heartbeat.soc-lab.invalid"},
            }
        )
    write_ndjson("sample-logs/suricata/eve.ndjson", network)

    web = [
        {
            "@timestamp": timestamp(1300),
            "scenario": "web_attack_patterns",
            "source_ip": "10.10.10.50",
            "http.request.method": "GET",
            "url.original": "/rest/products/search?q=' or 1=1--",
            "http.response.status_code": 400,
            "user_agent": "SOC-Lab-Safe-Simulator/1.0",
        },
        {
            "@timestamp": timestamp(1310),
            "scenario": "web_attack_patterns",
            "source_ip": "10.10.10.50",
            "http.request.method": "GET",
            "url.original": "/assets/../../etc/passwd",
            "http.response.status_code": 404,
            "user_agent": "SOC-Lab-Safe-Simulator/1.0",
        },
    ]
    write_ndjson("sample-logs/web/juice-shop.ndjson", web)
    print("8 scenarios generated")


if __name__ == "__main__":
    main()

