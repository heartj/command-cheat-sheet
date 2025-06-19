# free Command

Display free and used memory, including physical and swap

[Back to System Commands](./index.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Description |
|--------|-------------|
| `-h` | Display sizes in human-readable format (e.g., GB, MB) |
| `-s <seconds>` | Continuously update every specified seconds |
| `-m` | Display sizes in megabytes |
| `-g` | Display sizes in gigabytes |
| `-t` | Show total for RAM and swap |

## Examples
1. **Run command**:
```bash
free -h
```
Output: Shows total, used, free, and available memory in GB/MB

2. **Run command**:
```bash
free -h -s 3
```
Output: Updates memory stats every 3 seconds


## Notes
- The `available` column estimates memory for new processes.
- Combine with `vmstat` for deeper analysis.

## References
- [man free](https://man7.org/linux/man-pages/man1/free.1.html)

[Back to System Commands](../index.md) | [Back to Main Index](../../README.md)