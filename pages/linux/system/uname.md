# uname Command

The `uname` command displays system information, such as the operating system name, kernel version, and hardware architecture.

[Back to System Commands](../system.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Description |
|--------|-------------|
| `-a` | Display all system information |
| `-r` | Show kernel release version |
| `-m` | Show machine hardware name (e.g., x86_64) |
| `-s` | Show operating system name (e.g., Linux) |

## Examples

1. **Display all system information**:
   ```bash
   uname -a
   ```
   Output: `Linux hostname 5.15.0-73-generic x86_64 GNU/Linux`

2. **Show kernel version**:
   ```bash
   uname -r
   ```
   Output: `5.15.0-73-generic`

## Notes
- No root privileges required.
- Useful for scripting to detect system properties.
- Combine with `lscpu` for detailed hardware info.

## References
- [man uname](https://man7.org/linux/man-pages/man1/uname.1.html)
- [GNU Coreutils Documentation](https://www.gnu.org/software/coreutils/)

[Back to System Commands](../system.md) | [Back to Main Index](../../README.md)