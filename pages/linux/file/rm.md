# rm Command

Remove files or directories

[Back to File Commands](./index.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Description |
|--------|-------------|
| `-r` | Remove directories recursively |
| `-f` | Force removal without prompt |
| `-v` | Verbose output, show removed files |
| `-i` | Prompt before removal |

## Examples
1. **Run command**:
```bash
rm file.txt
```
Output: Deletes file.txt

2. **Run command**:
```bash
rm -rf /tmp/file
```
Output: Forcefully deletes /tmp/file and its contents

3. **Run command**:
```bash
rm -vi *.bak
```
Output: Deletes .bak files with confirmation


## Notes
- Use with caution; no undo for deleted files
- Requires `sudo` for protected files

## References
- [man rm](https://man7.org/linux/man-pages/man1/rm.1.html)

[Back to File Commands](../index.md) | [Back to Main Index](../../README.md)