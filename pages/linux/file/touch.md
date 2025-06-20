# touch Command

Create empty files or update timestamps

[Back to File Commands](./index.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Description |
|--------|-------------|
| `-m` | Update modification time only |
| `-a` | Update access time only |
| `-t <time>` | Set specific timestamp (e.g., -t 202301011200) |

## Examples
1. **Run command**:
```bash
touch file.txt
```
Output: Creates file.txt or updates its timestamp

2. **Run command**:
```bash
touch -m file.txt
```
Output: Updates modification time of file.txt


## Notes
- Useful for creating placeholder files
- Timestamps affect `find -mtime`

## References
- [man touch](https://man7.org/linux/man-pages/man1/touch.1.html)

[Back to File Commands](../index.md) | [Back to Main Index](../../README.md)