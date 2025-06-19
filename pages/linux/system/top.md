# top Command

The `top` command displays real-time information about system processes, including CPU and memory usage, running tasks, and load averages. It is widely used for system monitoring and identifying resource-intensive processes.

[Back to System Commands](../system.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Description |
|--------|-------------|
| `-d <seconds>` | Set the delay between updates (e.g., `-d 1` for 1-second intervals) |
| `-p <pid>` | Monitor specific process IDs (e.g., `-p 1234`) |
| `-u <user>` | Display processes for a specific user (e.g., `-u john`) |
| `-i` | Toggle display of idle processes |

## Examples

1. **Monitor system processes with a 2-second refresh**:
   ```bash
   top -d 2
   ```
   Output: Updates the display every 2 seconds, showing CPU, memory, and process details.

2. **View processes for a specific user**:
   ```bash
   top -u alice
   ```
   Output: Shows only processes owned by user `alice`.

## Notes
- Press `q` to quit `top`.
- Use interactive keys like `k` to kill a process or `r` to renice (requires root for some actions).
- High CPU or memory usage in `top` may indicate a bottleneck; check `%CPU` and `%MEM` columns.

## References
- [man top](https://man7.org/linux/man-pages/man1/top.1.html)
- [GNU Coreutils Documentation](https://www.gnu.org/software/coreutils/)

[Back to System Commands](../system.md) | [Back to Main Index](../../README.md)