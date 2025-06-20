# ln Command

Create hard or symbolic links

[Back to File Commands](./index.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Description |
|--------|-------------|
| `-s` | Create a symbolic link |
| `-f` | Force creation, overwrite existing links |
| `-v` | Verbose output, show created links |

## Examples
1. **Run command**:
```bash
ln -s /data/file.txt link.txt
```
Output: Creates a symbolic link link.txt to file.txt

2. **Run command**:
```bash
ln file.txt hardlink.txt
```
Output: Creates a hard link hardlink.txt to file.txt


## Notes
- Symbolic links can point to non-existent files
- Hard links require same filesystem

## References
- [man ln](https://man7.org/linux/man-pages/man1/ln.1.html)

[Back to File Commands](../index.md) | [Back to Main Index](../../README.md)