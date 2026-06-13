# OWASP Juice Shop

This Compose file binds Juice Shop to loopback by default.

```bash
docker compose up -d
```

For a VM-only lab, replace `127.0.0.1` with the Ubuntu endpoint's isolated lab address. Do
not bind the application to an internet-facing interface.

The image version is pinned for reproducibility. Review and update it deliberately.

