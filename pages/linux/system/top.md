# top Command

Display system processes and resource usage in real-time

[Back to System Commands](./index.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Description |
|--------|-------------|
| `-d <seconds>` | Set the delay between updates (e.g., -d 1 for 1-second intervals) |
| `-p <pid>` | Monitor specific process IDs (e.g., -p 1234) |
| `-u <user>` | Show processes for a specific user (e.g., -u alice) |
| `-b` | Run in batch mode, suitable for output redirection |
| `-n <number>` | Limit the number of iterations (e.g., -n 5 for 5 updates) |

## Examples
1. **Run command**:
```bash
top -d 2
```
Output: Updates the display every 2 seconds, showing CPU, memory, and process details

2. **Run command**:
```bash
top -u alice
```
Output: Shows only processes owned by user `alice`


## Notes
- Press `q` to quit `top`.
- High CPU or memory usage may indicate a bottleneck.

## References
- [man top](https://man7.org/linux/man-pages/man1/top.1.html)

[Back to System Commands](../index.md) | [Back to Main Index](../../README.md)