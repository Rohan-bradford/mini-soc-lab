from scripts.evaluate_detections import detect


def test_port_scan_requires_multiple_unique_ports() -> None:
    events = [
        {
            "scenario": "network_port_scan",
            "src_ip": "10.10.10.50",
            "dest_port": 22,
            "proto": "TCP",
        }
        for _ in range(20)
    ]
    assert "network_port_scan" not in detect(events)


def test_admin_group_detection_matches_expected_event() -> None:
    events = [
        {
            "scenario": "windows_admin_group_add",
            "event_id": 4732,
            "target_group": "Administrators",
        }
    ]
    assert "windows_admin_group_add" in detect(events)

