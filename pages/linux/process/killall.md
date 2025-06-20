# killall Command

Terminate processes by name

[Back to Process Commands](./index.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Description |
|--------|-------------|
| `-s <signal>` | Specify the signal to send (e.g., -s SIGTERM) |
| `-u <user>` | Terminate processes owned by a specific user |
| `-i` | Interactively confirm each process before killing |
| `-q` | Quiet mode, suppress output |

## Examples
1. **Run command**:
```bash
killall nginx
```
Output: Terminates all `nginx` processes

2. **Run command**:
```bash
killall -s SIGKILL firefox
```
Output: Forcefully terminates all `firefox` processes

3. **Run command**:
```bash
killall -u alice
```
Output: Terminates all processes owned by user `alice`


## Notes
- Be cautious as it affects all matching processes.
- Requires `sudo` for other users' processes.

## References
- [man killall](https://man7.org/linux/man-pages/man1/killall.1.html)

[Back to Process Commands](../index.md) | [Back to Main Index](../../README.md)