from __future__ import annotations

import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_DIRS = (
    "architecture",
    "dashboards",
    "detection-rules",
    "incident-reports",
    "playbooks",
    "sample-logs",
)
REQUIRED_SIGMA_KEYS = {
    "title",
    "id",
    "status",
    "description",
    "logsource",
    "detection",
    "level",
}


def main() -> None:
    errors: list[str] = []
    for directory in REQUIRED_DIRS:
        if not (ROOT / directory).is_dir():
            errors.append(f"missing directory: {directory}")

    sigma_files = [
        path
        for path in (ROOT / "detection-rules").rglob("*.yml")
        if "wazuh" not in path.parts
    ]
    if len(sigma_files) != 8:
        errors.append(f"expected 8 Sigma rules, found {len(sigma_files)}")
    for path in sigma_files:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
        missing = REQUIRED_SIGMA_KEYS - set(data or {})
        if missing:
            errors.append(f"{path.relative_to(ROOT)} missing keys: {sorted(missing)}")

    for path in (
        ROOT / ".github/workflows/ci.yml",
        ROOT / "deploy/juice-shop/compose.yml",
    ):
        try:
            yaml.safe_load(path.read_text(encoding="utf-8"))
        except yaml.YAMLError as exc:
            errors.append(f"invalid YAML {path.relative_to(ROOT)}: {exc}")

    for path in (ROOT / "dashboards").rglob("*.json"):
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            errors.append(f"invalid JSON {path.relative_to(ROOT)}: {exc}")

    for path in (
        ROOT / "config/sysmon/sysmon-lab.xml",
        ROOT / "config/wazuh/agent-collection.xml",
        ROOT / "detection-rules/wazuh/local_rules.xml",
    ):
        try:
            ET.parse(path)
        except ET.ParseError as exc:
            errors.append(f"invalid XML {path.relative_to(ROOT)}: {exc}")

    summary_path = ROOT / "sample-logs/alerts-summary.json"
    if not summary_path.exists():
        errors.append("missing generated alerts summary")
    else:
        summary = json.loads(summary_path.read_text(encoding="utf-8"))
        if summary.get("matched_count") != 8:
            errors.append("alerts summary does not contain 8 matches")

    link_pattern = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
    for path in ROOT.rglob("*.md"):
        for target in link_pattern.findall(path.read_text(encoding="utf-8")):
            if target.startswith(("http://", "https://", "#", "mailto:")):
                continue
            relative_target = target.split("#", 1)[0]
            if relative_target and not (path.parent / relative_target).resolve().exists():
                errors.append(
                    f"broken link in {path.relative_to(ROOT)}: {relative_target}"
                )

    if errors:
        raise SystemExit("\n".join(errors))
    print("project validation passed")


if __name__ == "__main__":
    main()
