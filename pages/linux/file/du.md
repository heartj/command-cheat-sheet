# du Command

Estimate file and directory space usage

[Back to File Commands](./index.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Description |
|--------|-------------|
| `-h` | Human-readable sizes |
| `-s` | Summarize total size |
| `-c` | Show grand total |
| `--max-depth=<n>` | Limit directory depth |

## Examples
1. **Run command**:
```bash
du -sh /home
```
Output: Shows total size of /home in human-readable format

2. **Run command**:
```bash
du -ch --max-depth=1 /var
```
Output: Shows sizes of /var subdirectories with total


## Notes
- Use with `sort -h` for sorted output
- Requires `sudo` for restricted directories

## References
- [man du](https://man7.org/linux/man-pages/man1/du.1.html)

[Back to File Commands](../index.md) | [Back to Main Index](../../README.md)