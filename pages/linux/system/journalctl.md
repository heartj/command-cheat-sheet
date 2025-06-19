# journalctl Command

Query and display systemd journal logs

[Back to System Commands](./index.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Description |
|--------|-------------|
| `-u <unit>` | Show logs for a specific systemd unit (e.g., -u sshd) |
| `-b` | Show logs since last boot |
| `-f` | Follow new log entries in real-time |
| `--since <time>` | Show logs since specified time (e.g., --since "2023-06-01") |
| `--until <time>` | Show logs until specified time |

## Examples
1. **Run command**:
```bash
journalctl -u nginx
```
Output: Displays all logs related to the `nginx` service

2. **Run command**:
```bash
journalctl -f
```
Output: Shows new log entries in real-time


## Notes
- Requires `sudo` for system-wide logs.
- Use `--since` and `--until` for time-based filtering.

## References
- [man journalctl](https://man7.org/linux/man-pages/man1/journalctl.1.html)

[Back to System Commands](../index.md) | [Back to Main Index](../../README.md)