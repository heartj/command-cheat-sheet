# htop Command

The `htop` command is an enhanced, interactive version of `top`, providing a user-friendly interface to monitor system processes, CPU, memory, and tasks. It supports mouse interaction and customizable displays.

[Back to System Commands](../system.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Description |
|--------|-------------|
| `-d <delay>` | Set the delay between updates in tenths of a second (e.g., `-d 20` for 2 seconds) |
| `-u <user>` | Show only processes for a specific user (e.g., `-u john`) |
| `-p <pid>` | Monitor specific process IDs (e.g., `-p 1234`) |
| `-C` | Disable color output |

## Examples

1. **Launch htop with a 1-second refresh**:
   ```bash
   htop -d 10
   ```
   Output: Displays processes with a 1-second update interval, showing CPU and memory usage.

2. **Show processes for a specific user**:
   ```bash
   htop -u alice
   ```
   Output: Filters processes owned by user `alice`.

## Notes
- Press `q` or `F10` to exit `htop`.
- Use `F` keys for actions like `F3` (search), `F5` (tree view), or `F9` (kill process).
- `htop` may need to be installed (`sudo apt install htop` on Debian/Ubuntu).

## References
- [man htop](https://man7.org/linux/man-pages/man1/htop.1.html)
- [htop Official Website](https://htop.dev/)

[Back to System Commands](../system.md) | [Back to Main Index](../../README.md)