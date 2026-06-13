# Linux Hardening Checklist

- [ ] Apply security updates and document patch date.
- [ ] Disable direct root SSH login.
- [ ] Prefer SSH keys; disable password authentication after the brute-force exercise.
- [ ] Restrict SSH to the isolated management subnet.
- [ ] Enable host firewall default-deny inbound policy.
- [ ] Remove unused services and packages.
- [ ] Configure time synchronization.
- [ ] Set account lockout and password policy appropriate to the lab.
- [ ] Protect Wazuh agent keys and configuration.
- [ ] Enable audit logging for privileged actions.
- [ ] Restrict Docker socket access.
- [ ] Pin container versions and scan images.
- [ ] Back up configuration and test restoration.

