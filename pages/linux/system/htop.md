# htop Command

Interactive process viewer with enhanced interface

[Back to System Commands](./index.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Description |
|--------|-------------|
| `-d <delay>` | Set update delay in tenths of a second (e.g., -d 20 for 2 seconds) |
| `-u <user>` | Show processes for a specific user (e.g., -u john) |
| `-s <column>` | Sort by specified column (e.g., -s CPU) |
| `-C` | Disable color output |
| `-t` | Display processes in tree view |

## Examples
1. **Run command**:
```bash
htop -d 10
```
Output: Displays processes with a 1-second update interval

2. **Run command**:
```bash
htop -u alice
```
Output: Filters processes owned by user `alice`


## Notes
- Press `q` or `F10` to exit.
- Requires installation (`sudo apt install htop` on Debian/Ubuntu).

## References
- [man htop](https://man7.org/linux/man-pages/man1/htop.1.html)

[Back to System Commands](../index.md) | [Back to Main Index](../../README.md)