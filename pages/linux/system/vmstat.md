# vmstat Command

Report virtual memory, CPU, and I/O statistics

[Back to System Commands](./index.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Description |
|--------|-------------|
| `-s` | Display detailed memory statistics |
| `-d` | Show disk statistics |
| `-w` | Use wide output format |
| `-t` | Include timestamp in output |
| `-a` | Show active and inactive memory |

## Examples
1. **Run command**:
```bash
vmstat
```
Output: Displays memory, swap, CPU, and I/O metrics

2. **Run command**:
```bash
vmstat 2 5
```
Output: Updates stats 5 times, every 2 seconds


## Notes
- Use `sudo` for detailed disk stats.
- High swap usage indicates memory pressure.

## References
- [man vmstat](https://man7.org/linux/man-pages/man8/vmstat.8.html)

[Back to System Commands](../index.md) | [Back to Main Index](../../README.md)