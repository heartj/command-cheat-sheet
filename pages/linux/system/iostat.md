# iostat Command

Display CPU and I/O statistics for disk performance

[Back to System Commands](./index.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Description |
|--------|-------------|
| `-x` | Show extended statistics |
| `-d` | Display only device statistics |
| `-c` | Display only CPU statistics |
| `-k` | Display statistics in kilobytes |
| `-m` | Display statistics in megabytes |

## Examples
1. **Run command**:
```bash
iostat
```
Output: Displays CPU usage and device I/O metrics

2. **Run command**:
```bash
iostat -x 3 4
```
Output: Updates extended disk stats 4 times, every 3 seconds


## Notes
- Requires `sysstat` package (`sudo apt install sysstat`).
- High `%iowait` indicates I/O bottlenecks.

## References
- [man iostat](https://man7.org/linux/man-pages/man1/iostat.1.html)

[Back to System Commands](../index.md) | [Back to Main Index](../../README.md)