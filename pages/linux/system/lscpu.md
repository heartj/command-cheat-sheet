# lscpu Command

Display CPU architecture details (cores, threads, model)

[Back to System Commands](./index.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Description |
|--------|-------------|
| `-e` | Display extended CPU information in a table |
| `--parse` | Output parseable format for scripting |
| `-a` | Include all CPUs, including offline ones |
| `-b` | Show only online CPUs |

## Examples
1. **Run command**:
```bash
lscpu
```
Output: Lists CPU model, cores, threads, and frequency

2. **Run command**:
```bash
lscpu --parse
```
Output: Comma-separated CPU data for scripting


## Notes
- No root privileges required.
- Combine with `uname` for complete system info.

## References
- [man lscpu](https://man7.org/linux/man-pages/man1/lscpu.1.html)

[Back to System Commands](../index.md) | [Back to Main Index](../../README.md)