# Sysmon Lab Configuration

The compact configuration collects the event types used in this project without pretending
to be a production baseline.

Install or enable Sysmon according to current Microsoft documentation, then apply:

```powershell
Sysmon64.exe -accepteula -i .\sysmon-lab.xml
```

Update an existing installation:

```powershell
Sysmon64.exe -c .\sysmon-lab.xml
```

Confirm events under:

```text
Applications and Services Logs
Microsoft
Windows
Sysmon
Operational
```

Microsoft documentation:
https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon

