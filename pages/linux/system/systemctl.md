# systemctl Command

Manage systemd services and units (start, stop, enable)

[Back to System Commands](./index.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Description |
|--------|-------------|
| `start <unit>` | Start a service or unit (e.g., start sshd) |
| `stop <unit>` | Stop a service or unit |
| `restart <unit>` | Restart a service or unit |
| `status <unit>` | Show the status of a service or unit |
| `enable <unit>` | Enable a unit to start at boot |
| `disable <unit>` | Disable a unit from starting at boot |

## Examples
1. **Run command**:
```bash
sudo systemctl start sshd
```
Output: Starts the SSH daemon, enabling remote access

2. **Run command**:
```bash
systemctl status nginx
```
Output: Displays whether `nginx` is running, with recent logs


## Notes
- Requires root privileges for most operations (use `sudo`).
- Be cautious with `stop` on critical services like `sshd`.

## References
- [man systemctl](https://man7.org/linux/man-pages/man1/systemctl.1.html)

[Back to System Commands](../index.md) | [Back to Main Index](../../README.md)