# mkdir Command

Create directories

[Back to File Commands](./index.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Description |
|--------|-------------|
| `-p` | Create parent directories as needed |
| `-v` | Verbose output, show created directories |
| `-m <mode>` | Set permissions (e.g., -m 755) |

## Examples
1. **Run command**:
```bash
mkdir newdir
```
Output: Creates a directory named newdir

2. **Run command**:
```bash
mkdir -p /path/to/newdir
```
Output: Creates newdir and parent directories if needed


## Notes
- Fails if directory exists unless `-p` is used
- Default permissions depend on umask

## References
- [man mkdir](https://man7.org/linux/man-pages/man1/mkdir.1.html)

[Back to File Commands](../index.md) | [Back to Main Index](../../README.md)