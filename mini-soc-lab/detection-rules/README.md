# Detection Rules

## Formats

- `windows/`, `linux/`, `network/`, and `web/`: portable Sigma-style portfolio rules
- `wazuh/local_rules.xml`: Wazuh implementation examples
- `config/suricata/local.rules`: network IDS signatures

## Rule Lifecycle

1. Define the hypothesis.
2. Identify required telemetry and fields.
3. Write the rule and ATT&CK mapping.
4. Generate or collect a positive test event.
5. Verify a benign event does not match.
6. Document false positives and tuning.
7. Peer review.
8. Deploy to the lab.
9. Record alert evidence and update the rule.

These rules use small thresholds for demonstration. Validate decoder names, field mappings,
rule IDs, and baseline volume in your installed Wazuh version.

