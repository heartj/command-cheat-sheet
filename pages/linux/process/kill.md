# kill Command

Send signals to processes to terminate or control them

[Back to Process Commands](./index.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Description |
|--------|-------------|
| `-s <signal>` | Specify the signal to send (e.g., -s SIGTERM) |
| `-l` | List all signal names |
| `-9` | Send SIGKILL to forcefully terminate a process |
| `-15` | Send SIGTERM to gracefully terminate a process |

## Examples
1. **Run command**:
```bash
kill -9 1234
```
Output: Forcefully terminates process with PID 1234

2. **Run command**:
```bash
kill -15 5678
```
Output: Requests process with PID 5678 to terminate gracefully

3. **Run command**:
```bash
kill -l
```
Output: Lists available signals (e.g., SIGHUP, SIGTERM, SIGKILL)


## Notes
- Requires `sudo` for processes owned by other users.
- Use SIGTERM (-15) before SIGKILL (-9) to allow cleanup.

## References
- [man kill](https://man7.org/linux/man-pages/man1/kill.1.html)

[Back to Process Commands](../index.md) | [Back to Main Index](../../README.md)