# pkill Command

Terminate processes by name or other attributes

[Back to Process Commands](./index.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Description |
|--------|-------------|
| `-s <signal>` | Specify the signal to send (e.g., -s SIGTERM) |
| `-u <user>` | Match processes owned by a specific user |
| `-f` | Match against full command line |
| `-n` | Match the newest process |

## Examples
1. **Run command**:
```bash
pkill nginx
```
Output: Terminates all `nginx` processes

2. **Run command**:
```bash
pkill -u alice
```
Output: Terminates all processes owned by user `alice`

3. **Run command**:
```bash
pkill -f "python script.py"
```
Output: Terminates processes matching the full command line


## Notes
- More flexible than `killall` due to pattern matching.
- Requires `sudo` for other users' processes.

## References
- [man pkill](https://man7.org/linux/man-pages/man1/pkill.1.html)

[Back to Process Commands](../index.md) | [Back to Main Index](../../README.md)