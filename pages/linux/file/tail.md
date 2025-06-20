# tail Command

Display the end of files

[Back to File Commands](./index.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Description |
|--------|-------------|
| `-n <lines>` | Show specified number of lines |
| `-f` | Follow file changes in real-time |
| `-c <bytes>` | Show specified number of bytes |

## Examples
1. **Run command**:
```bash
tail -n 5 file.txt
```
Output: Shows last 5 lines of file.txt

2. **Run command**:
```bash
tail -f /var/log/syslog
```
Output: Monitors syslog in real-time


## Notes
- Useful for log monitoring
- Use `Ctrl+C` to exit `-f` mode

## References
- [man tail](https://man7.org/linux/man-pages/man1/tail.1.html)

[Back to File Commands](../index.md) | [Back to Main Index](../../README.md)