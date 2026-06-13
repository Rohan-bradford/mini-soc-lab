# Suricata Sensor

Enable EVE JSON for at least:

- alerts
- flows
- DNS
- HTTP
- TLS
- file information

Copy `local.rules` into the sensor's local rule path and test before restarting:

```bash
sudo suricata -T -c /etc/suricata/suricata.yaml
```

Forward `/var/log/suricata/eve.json` through the Wazuh agent using the collection snippet in
`config/wazuh/agent-collection.xml`.

Thresholds are intentionally small for an isolated lab. They are not production defaults.

