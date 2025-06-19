# lscpu Command

The `lscpu` command displays detailed information about the CPU architecture, including cores, threads, and model name.

[Back to System Commands](../system.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Description |
|--------|-------------|
| `-e` | Display extended CPU information in a table |
| `--parse` | Output parseable format for scripting |
| `-p` | Output parseable format with specific fields |
| `-a` | Include all CPUs, including offline |

## Examples

1. **Show CPU details**:
   ```bash
   lscpu
   ```
   Output: Lists CPU model, cores, threads, and frequency.

2. **Parse CPU info for scripting**:
   ```bash
   lscpu --parse
   ```
   Output: Comma-separated CPU data for easy parsing.

## Notes
- No root privileges required.
- Useful for system profiling and performance tuning.
- Combine with `uname` for complete system info.

## References
- [man lscpu](https://man7.org/linux/man-pages/man1/lscpu.1.html)
- [util-linux Documentation](https://www.kernel.org/doc/html/latest/)

[Back to System Commands](../system.md) | [Back to Main Index](../../README.md)