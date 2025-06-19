# lsblk Command

List block devices (disks, partitions, mount points)

[Back to System Commands](./index.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Description |
|--------|-------------|
| `-f` | Show filesystem information (type, mount point) |
| `-o <columns>` | Specify output columns (e.g., -o NAME,SIZE) |
| `-a` | Include empty devices |
| `-l` | Use list format instead of tree |
| `-d` | Show only disks, exclude partitions |

## Examples
1. **Run command**:
```bash
lsblk -f
```
Output: Shows device names, filesystem types, and mount points

2. **Run command**:
```bash
lsblk -o NAME,SIZE,TYPE
```
Output: Displays only name, size, and type of devices


## Notes
- Use `sudo` for full device information.
- Useful for identifying unmounted partitions.

## References
- [man lsblk](https://man7.org/linux/man-pages/man8/lsblk.8.html)

[Back to System Commands](../index.md) | [Back to Main Index](../../README.md)