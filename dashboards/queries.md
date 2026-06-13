# Investigation Queries

Field names vary by Wazuh decoder and version. Confirm mappings in Discover before saving.

## Windows Failed Logons

```text
win.system.eventID:4625
```

Group by source address and target username over five-minute windows.

## Suspicious PowerShell

```text
win.system.eventID:1 AND
win.eventdata.image:*powershell.exe AND
win.eventdata.commandLine:(*EncodedCommand* OR *NonInteractive* OR *WindowStyle\ Hidden*)
```

## Administrator Group Changes

```text
win.system.eventID:4732 AND win.eventdata.targetUserName:Administrators
```

## SSH Failures

```text
full_log:"Failed password" AND agent.name:linux-endpoint-01
```

## Suricata Port Activity

```text
data.event_type:flow AND data.proto:TCP
```

Group by `data.src_ip`, then count unique `data.dest_port`.

## Web Attack Indicators

```text
data.url.original:(*../* OR *script* OR *union* OR *1=1*)
```

