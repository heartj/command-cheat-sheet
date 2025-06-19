# df Command

The `df` command reports disk space usage for mounted filesystems, showing total, used, and available space. It is essential for monitoring storage capacity.

[Back to System Commands](../system.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Description |
|--------|-------------|
| `-h` | Display sizes in human-readable format (e.g., GB, MB) |
| `-T` | Show filesystem type (e.g., ext4, tmpfs) |
| `-t <type>` | Limit to specific filesystem types (e.g., `-t ext4`) |
| `--exclude-type=<type>` | Exclude specific filesystem types (e.g., `--exclude-type=tmpfs`) |

## Examples

1. **Show disk usage in human-readable format**:
   ```bash
   df -h
   ```
   Output: Lists filesystems with sizes like `10G`, `500M`, showing total and available space.

2. **Display specific filesystem type**:
   ```bash
   df -t ext4
   ```
   Output: Shows only `ext4` filesystems' disk usage.

## Notes
- Use `sudo` to access restricted filesystems.
- Exclude pseudo-filesystems (e.g., `tmpfs`) with `--exclude-type` for cleaner output.
- Combine with `du` to investigate high disk usage.

## References
- [man df](https://man7.org/linux/man-pages/man1/df.1.html)
- [GNU Coreutils Documentation](https://www.gnu.org/software/coreutils/)

[Back to System Commands](../system.md) | [Back to Main Index](../../README.md)