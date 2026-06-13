# Windows Event Simulations

## SIM-001: Failed Logons

1. Create a nonprivileged account named `lab-user`.
2. From the Windows lock screen or another owned lab endpoint, submit an incorrect password
   six times over two minutes.
3. Confirm Security Event ID 4625 is collected.
4. Record source address, target account, logon type, and failure status.

Do not test domain or production accounts.

## SIM-002: Suspicious PowerShell Flags

Use a harmless payload that only writes text:

```powershell
$command = 'Write-Output "SOC-LAB-SAFE-TEST"'
$encoded = [Convert]::ToBase64String([Text.Encoding]::Unicode.GetBytes($command))
powershell.exe -NoProfile -NonInteractive -EncodedCommand $encoded
```

Expected telemetry: Sysmon Event ID 1 with PowerShell image and encoded-command flag.

## SIM-003: Temporary Administrator

Run on a disposable Windows VM:

```powershell
New-LocalUser -Name "temporary-admin" -NoPassword
Add-LocalGroupMember -Group "Administrators" -Member "temporary-admin"
Remove-LocalGroupMember -Group "Administrators" -Member "temporary-admin"
Remove-LocalUser -Name "temporary-admin"
```

Capture the addition event before rollback. Never use `-NoPassword` outside an isolated,
disposable VM.

## SIM-004: Harmless Test File

```powershell
New-Item -ItemType Directory -Force C:\SOC-Lab
Set-Content C:\SOC-Lab\harmless-test.txt "MINI-SOC-LAB-HARMLESS-TEST-FILE"
Get-FileHash C:\SOC-Lab\harmless-test.txt -Algorithm SHA256
Remove-Item C:\SOC-Lab\harmless-test.txt
```

The repository evaluator uses a canonical byte sequence with a newline, so a PowerShell-created
file may have a different hash due to encoding. Update the local hash rule with the observed
value and document why.

