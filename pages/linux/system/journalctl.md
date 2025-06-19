# journalctl Command

The `journalctl` command queries and displays logs from the systemd journal, useful for debugging system issues.

[Back to System Commands](../system.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Description |
|--------|-------------|
| `-u <unit>` | Show logs for a specific systemd unit (e.g., `-u sshd`) |
| `-b` | Show logs since last boot |
| `-f` | Follow new log entries in real-time |
| `--since <time>` | Show logs since a specific time (e.g., `--since "2023-06-01"`) |

## Examples

1. **Show logs for a service**:
   ```bash
   journalctl -u nginx
   ```
   Output: Displays all logs related to the `nginx` service.

2. **Follow logs in real-time**:
   ```bash
   journalctl -f
   ```
   Output: Shows new log entries as they are added.

## Notes
- Requires `sudo` for system-wide logs.
- Use `--since` and `--until` for time-based filtering.
- Large logs may require `--no-pager` or `grep` for efficiency.

## References
- [man journalctl](https://man7.org/linux/man-pages/man1/journalctl.1.html)
- [systemd Documentation](https://www.freedesktop.org/wiki/Software/systemd/)

[Back to System Commands](../system.md) | [Back to Main Index](../../README.md)