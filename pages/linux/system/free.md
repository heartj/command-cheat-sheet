# free Command

The `free` command displays the amount of free and used memory in the system, including physical and swap memory.

[Back to System Commands](../system.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Description |
|--------|-------------|
| `-h` | Display sizes in human-readable format (e.g., GB, MB) |
| `-s <seconds>` | Continuously update every specified seconds (e.g., `-s 5`) |
| `-t` | Show a total line for physical and swap memory |
| `-m` | Display sizes in megabytes |

## Examples

1. **Show memory usage in human-readable format**:
   ```bash
   free -h
   ```
   Output: Shows total, used, free, shared, and available memory in GB/MB.

2. **Continuously monitor memory every 3 seconds**:
   ```bash
   free -h -s 3
   ```
   Output: Updates memory stats every 3 seconds.

## Notes
- The `available` column estimates memory available for new processes.
- Use `sudo` for detailed memory stats on some systems.
- Combine with `vmstat` for deeper memory analysis.

## References
- [man free](https://man7.org/linux/man-pages/man1/free.1.html)
- [GNU Coreutils Documentation](https://www.gnu.org/software/coreutils/)

[Back to System Commands](../system.md) | [Back to Main Index](../../README.md)