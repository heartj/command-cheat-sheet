# Linux System Commands

This page provides a quick reference for Linux commands related to system monitoring, resource management, service management, and system control. These commands are essential for administering and troubleshooting Linux systems. Click on a command for detailed guides.

[Back to Main Index](../../README.md)

## Commands

| Command | Purpose | Link |
|---------|---------|------|
| `top` | Display system processes and resource usage in real-time | [Details](./system/top.md) |
| `htop` | Enhanced version of `top` with an interactive interface | [Details](./system/htop.md) |
| `uptime` | Show system runtime, load average, and user count | [Details](./system/uptime.md) |
| `df` | Report disk space usage | [Details](./system/df.md) |
| `du` | Estimate file and directory disk usage | [Details](./system/du.md) |
| `free` | Display memory usage (total, used, free) | [Details](./system/free.md) |
| `uname` | Display system information (kernel version, architecture) | [Details](./system/uname.md) |
| `lscpu` | Display CPU architecture and details | [Details](./system/lscpu.md) |
| `lsblk` | List block device information (e.g., disks, partitions) | [Details](./system/lsblk.md) |
| `dmesg` | Display system logs (kernel message buffer) | [Details](./system/dmesg.md) |
| `who` | Show currently logged-in users | [Details](./system/who.md) |
| `crontab` | Manage user crontab files (edit, view, delete) | [Details](./system/crontab.md) |
| `systemctl` | Manage systemd services and units (start, stop, enable) | [Details](./system/systemctl.md) |
| `vmstat` | Report virtual memory, CPU, and I/O statistics | [Details](./system/vmstat.md) |
| `iostat` | Display CPU and I/O statistics (disk performance) | [Details](./system/iostat.md) |
| `journalctl` | Query and display systemd logs | [Details](./system/journalctl.md) |
| `hostnamectl` | Manage system hostname | [Details](./system/hostnamectl.md) |
| `reboot` | Restart the system | [Details](./system/reboot.md) |
| `shutdown` | Shut down or restart the system | [Details](./system/shutdown.md) |

## References
- [GNU Coreutils Documentation](https://www.gnu.org/software/coreutils/manual/coreutils.html)
- [man systemctl](https://man7.org/linux/man-pages/man1/systemctl.1.html)
- [man crontab](https://man7.org/linux/man-pages/man1/crontab.1.html)

## Notes
- Use `man <command>` (e.g., `man top`) to view detailed documentation.
- Many commands require root privileges (e.g., `sudo systemctl`).
- Be cautious with commands like `reboot` or `shutdown`, as they affect system availability.

[Back to Main Index](../../README.md)