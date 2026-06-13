# Linux, Network, and Web Simulations

## SIM-005: Low-Rate Port Scan

From `analyst-01`, scan only the owned Ubuntu endpoint:

```bash
nmap -sT -T2 -p 20-40 10.10.10.30
```

Expected evidence: multiple TCP destination ports from one source in Suricata flows. Do not
scan public address space or networks you do not own.

## SIM-006: SSH Authentication Failures

Attempt to sign in to a disposable `demo` account and intentionally enter the wrong password
six times:

```bash
ssh demo@10.10.10.30
```

Expected evidence: repeated `Failed password` entries in `/var/log/auth.log`.

## SIM-007: Web Attack Indicators

Send harmless requests to your isolated Juice Shop instance:

```bash
curl --path-as-is -A "SOC-Lab-Safe-Simulator/1.0" \
  "http://10.10.10.30:3000/assets/../../not-a-real-file"

curl -G -A "SOC-Lab-Safe-Simulator/1.0" \
  --data-urlencode "q=' or 1=1--" \
  "http://10.10.10.30:3000/rest/products/search"
```

These requests provide log indicators; they are not instructions to extract data.

## SIM-008: Reserved-Domain DNS Pattern

```bash
for i in 1 2 3 4 5 6; do
  nslookup heartbeat.soc-lab.invalid
  sleep 60
done
```

The `.invalid` top-level domain is reserved and should not resolve publicly.

