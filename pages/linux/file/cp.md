# cp Command

Copy files and directories

[Back to File Commands](./index.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Description |
|--------|-------------|
| `-r` | Copy directories recursively |
| `-v` | Verbose output, show copied files |
| `-u` | Copy only when source is newer |
| `-p` | Preserve file attributes |

## Examples
1. **Run command**:
```bash
cp file.txt /backup
```
Output: Copies file.txt to /backup

2. **Run command**:
```bash
cp -r /docs /backup
```
Output: Recursively copies /docs to /backup

3. **Run command**:
```bash
cp -uv *.jpg /photos
```
Output: Copies newer .jpg files to /photos with verbose output


## Notes
- Overwrites destination files by default
- Use `-i` for interactive confirmation

## References
- [man cp](https://man7.org/linux/man-pages/man1/cp.1.html)

[Back to File Commands](../index.md) | [Back to Main Index](../../README.md)