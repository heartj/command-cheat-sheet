# rmdir Command

Remove empty directories

[Back to File Commands](./index.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Description |
|--------|-------------|
| `-p` | Remove parent directories if empty |
| `-v` | Verbose output, show removed directories |

## Examples
1. **Run command**:
```bash
rmdir empty_dir
```
Output: Removes empty_dir if it is empty

2. **Run command**:
```bash
rmdir -p /path/to/empty_dir
```
Output: Removes empty_dir and empty parent directories


## Notes
- Fails for non-empty directories; use `rm -r` instead
- Safer than `rm -r` for directories

## References
- [man rmdir](https://man7.org/linux/man-pages/man1/rmdir.1.html)

[Back to File Commands](../index.md) | [Back to Main Index](../../README.md)