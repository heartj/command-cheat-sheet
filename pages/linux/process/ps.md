# ps Command

Display information about active processes

[Back to Process Commands](./index.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Description |
|--------|-------------|
| `-aux` | Show all processes for all users in BSD format |
| `-ef` | Show all processes in full-format listing |
| `-u <user>` | Show processes for a specific user (e.g., -u alice) |
| `-p <pid>` | Show information for specific process IDs |
| `-o <format>` | Customize output format (e.g., -o pid,comm) |

## Examples
1. **Run command**:
```bash
ps -aux
```
Output: Lists all processes with details like PID, user, and CPU usage

2. **Run command**:
```bash
ps -ef | grep nginx
```
Output: Shows processes related to `nginx`

3. **Run command**:
```bash
ps -u alice
```
Output: Displays processes owned by user `alice`

4. **Run command**:
```bash
ps -o pid,comm -p 1234
```
Output: Shows PID and command name for process ID 1234


## Notes
- Use `kill` to terminate processes by PID.
- Combine with `grep` for filtering.
- BSD (`aux`) and System V (`-ef`) formats differ in output.

## References
- [man ps](https://man7.org/linux/man-pages/man1/ps.1.html)

[Back to Process Commands](../index.md) | [Back to Main Index](../../README.md)