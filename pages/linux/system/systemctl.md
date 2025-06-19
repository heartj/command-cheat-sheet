# systemctl Command

The `systemctl` command manages systemd services, units, and system state. It is used to start, stop, enable, disable, and inspect services, as well as manage system targets and resources.

[Back to System Commands](../system.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Description |
|--------|-------------|
| `start <unit>` | Start a service or unit (e.g., `start sshd`) |
| `stop <unit>` | Stop a service or unit |
| `enable <unit>` | Enable a service to start at boot |
| `disable <unit>` | Disable a service from starting at boot |
| `status <unit>` | Show the status of a service or unit |
| `--type=<type>` | Filter units by type (e.g., `--type=service`) |

## Examples

1. **Start the SSH service**:
   ```bash
   sudo systemctl start sshd
   ```
   Output: Starts the SSH daemon, enabling remote access.

2. **Check the status of a service**:
   ```bash
   systemctl status nginx
   ```
   Output: Displays whether `nginx` is running, along with recent logs.

## Notes
- Requires root privileges for most operations (use `sudo`).
- Use `systemctl list-units --type=service` to list all services.
- Be cautious with `stop` or `disable` on critical services like `sshd`, as it may lock you out.

## References
- [man systemctl](https://man7.org/linux/man-pages/man1/systemctl.1.html)
- [systemd Documentation](https://www.freedesktop.org/wiki/Software/systemd/)

[Back to System Commands](../system.md) | [Back to Main Index](../../README.md)