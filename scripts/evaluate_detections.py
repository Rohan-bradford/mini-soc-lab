from __future__ import annotations

import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Callable

ROOT = Path(__file__).resolve().parents[1]


def read_events(relative: str) -> list[dict[str, Any]]:
    with (ROOT / relative).open(encoding="utf-8") as handle:
        return [json.loads(line) for line in handle if line.strip()]


def count_by(events: list[dict[str, Any]], field: str) -> Counter[str]:
    return Counter(str(event.get(field, "")) for event in events)


def largest_count(events: list[dict[str, Any]], field: str) -> int:
    counts = count_by(events, field)
    return max(counts.values(), default=0)


def detect(events: list[dict[str, Any]]) -> dict[str, list[dict[str, Any]]]:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for event in events:
        grouped[event["scenario"]].append(event)

    checks: dict[str, Callable[[list[dict[str, Any]]], bool]] = {
        "windows_failed_logons": lambda items: largest_count(items, "source_ip") >= 5,
        "windows_suspicious_powershell": lambda items: any(
            "powershell" in item.get("image", "").lower()
            and any(
                flag in item.get("command_line", "").lower()
                for flag in ("-encodedcommand", "-enc ", "-noninteractive", "-windowstyle hidden")
            )
            for item in items
        ),
        "windows_admin_group_add": lambda items: any(
            item.get("event_id") == 4732 and item.get("target_group") == "Administrators"
            for item in items
        ),
        "windows_test_hash": lambda items: any(
            item.get("sha256")
            == "C252BE63E223AB40C3AEA0777F23B4D867B0FF0DD2AD591875AB2ED829E15AD9"
            for item in items
        ),
        "linux_ssh_bruteforce": lambda items: largest_count(items, "source_ip") >= 5,
        "network_port_scan": lambda items: len(
            {item.get("dest_port") for item in items if item.get("proto") == "TCP"}
        )
        >= 15,
        "network_dns_beacon": lambda items: sum(
            1 for item in items if item.get("dns", {}).get("rrname", "").endswith(".invalid")
        )
        >= 6,
        "web_attack_patterns": lambda items: any(
            marker in item.get("url.original", "").lower()
            for item in items
            for marker in ("../", "<script", "union select", "or 1=1")
        ),
    }

    return {name: grouped[name] for name, check in checks.items() if check(grouped[name])}


def main() -> None:
    events = (
        read_events("sample-logs/windows/events.ndjson")
        + read_events("sample-logs/linux/auth.ndjson")
        + read_events("sample-logs/suricata/eve.ndjson")
        + read_events("sample-logs/web/juice-shop.ndjson")
    )
    matches = detect(events)
    output = ROOT / "sample-logs" / "alerts-summary.json"
    output.write_text(
        json.dumps(
            {
                "generated": "2026-06-13T10:00:00Z",
                "evidence_type": "synthetic",
                "matched_count": len(matches),
                "alerts": [
                    {
                        "scenario": name,
                        "event_count": len(items),
                        "first_seen": items[0].get("@timestamp", items[0].get("timestamp")),
                        "host": items[0].get("host", items[0].get("dest_ip", "n/a")),
                    }
                    for name, items in sorted(matches.items())
                ],
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    print(f"{len(matches)} detections matched")
    if len(matches) != 8:
        raise SystemExit("expected all 8 synthetic scenarios to match")


if __name__ == "__main__":
    main()
