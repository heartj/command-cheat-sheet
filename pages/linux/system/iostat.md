# iostat Command

The `iostat` command displays CPU and I/O statistics, focusing on disk performance and system load.

[Back to System Commands](../system.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Description |
|--------|-------------|
| `-x` | Show extended statistics |
| `-d` | Display only device statistics |
| `-c` | Display only CPU statistics |
| `<interval> <count>` | Update every <interval> seconds for <count> times (e.g., `iostat 2 5`) |

## Examples

1. **Show CPU and disk stats**:
   ```bash
   iostat
   ```
   Output: Displays CPU usage and device I/O metrics.

2. **Show extended disk stats every 3 seconds**:
   ```bash
   iostat -x 3 4
   ```
   Output: Updates extended disk stats 4 times, every 3 seconds.

## Notes
- Requires `sysstat` package (`sudo apt install sysstat`).
- Use `sudo` for detailed stats.
- High `%iowait` indicates I/O bottlenecks.

## References
- [man iostat](https://man7.org/linux/man-pages/man1/iostat.1.html)
- [sysstat Documentation](http://sebastien.godard.pagesperso-orange.fr/)

[Back to System Commands](../system.md) | [Back to Main Index](../../README.md)