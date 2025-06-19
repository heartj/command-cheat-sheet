# lsblk Command

The `lsblk` command lists information about block devices, such as disks, partitions, and their mount points.

[Back to System Commands](../system.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Description |
|--------|-------------|
| `-f` | Show filesystem information (e.g., type, mount point) |
| `-o <columns>` | Specify output columns (e.g., `-o NAME,SIZE`) |
| `-a` | Include empty devices |
| `-l` | Use list format instead of tree |

## Examples

1. **List block devices with filesystems**:
   ```bash
   lsblk -f
   ```
   Output: Shows device names, filesystem types, and mount points.

2. **Show specific columns**:
   ```bash
   lsblk -o NAME,SIZE,TYPE
   ```
   Output: Displays only name, size, and type of devices.

## Notes
- Use `sudo` for full device information.
- Useful for identifying unmounted partitions.
- Combine with `df` for storage analysis.

## References
- [man lsblk](https://man7.org/linux/man-pages/man8/lsblk.8.html)
- [util-linux Documentation](https://www.kernel.org/doc/html/latest/)

[Back to System Commands](../system.md) | [Back to Main Index](../../README.md)