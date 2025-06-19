# df Command

Report disk space usage for mounted filesystems

[Back to System Commands](./index.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Description |
|--------|-------------|
| `-h` | Display sizes in human-readable format (e.g., GB, MB) |
| `-T` | Show filesystem type (e.g., ext4) |
| `-t <type>` | Limit to specific filesystem types (e.g., -t ext4) |
| `-x <type>` | Exclude specific filesystem types (e.g., -x tmpfs) |
| `-a` | Include all filesystems, including those with zero blocks |

## Examples
1. **Run command**:
```bash
df -h
```
Output: Lists filesystems with sizes like `10G`, showing total and available space

2. **Run command**:
```bash
df -t ext4
```
Output: Shows only `ext4` filesystems' disk usage


## Notes
- Use `sudo` for restricted filesystems.
- Combine with `du` for detailed usage analysis.

## References
- [man df](https://man7.org/linux/man-pages/man1/df.1.html)

[Back to System Commands](../index.md) | [Back to Main Index](../../README.md)