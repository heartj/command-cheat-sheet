# mv Command

Move or rename files and directories

[Back to File Commands](./index.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Description |
|--------|-------------|
| `-v` | Verbose output, show moved files |
| `-u` | Move only when source is newer |
| `-i` | Prompt before overwriting |

## Examples
1. **Run command**:
```bash
mv file.txt /backup
```
Output: Moves file.txt to /backup

2. **Run command**:
```bash
mv oldname.txt newname.txt
```
Output: Renames oldname.txt to newname.txt

3. **Run command**:
```bash
mv -vi *.jpg /photos
```
Output: Moves .jpg files to /photos with confirmation


## Notes
- Overwrites destination by default unless `-i` is used
- No recursive flag needed for directories

## References
- [man mv](https://man7.org/linux/man-pages/man1/mv.1.html)

[Back to File Commands](../index.md) | [Back to Main Index](../../README.md)