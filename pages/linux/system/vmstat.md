# vmstat Command

The `vmstat` command reports virtual memory, CPU, and I/O statistics, useful for system performance monitoring.

[Back to System Commands](../system.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Description |
|--------|-------------|
| `-s` | Display detailed memory statistics |
| `-d` | Show disk statistics |
| `-w` | Use wide output format |
| `<delay> <count>` | Update every <delay> seconds for <count> times (e.g., `vmstat 2 5`) |

## Examples

1. **Show memory and CPU stats**:
   ```bash
   vmstat
   ```
   Output: Displays memory, swap, CPU, and I/O metrics.

2. **Monitor stats every 2 seconds**:
   ```bash
   vmstat 2 5
   ```
   Output: Updates stats 5 times, every 2 seconds.

## Notes
- Use `sudo` for detailed disk stats (`-d`).
- High `si`/`so` (swap in/out) indicates memory pressure.
- Combine with `iostat` for deeper I/O analysis.

## References
- [man vmstat](https://man7.org/linux/man-pages/man8/vmstat.8.html)
- [procps Documentation](https://gitlab.com/procps-ng/procps)

[Back to System Commands](../system.md) | [Back to Main Index](../../README.md)