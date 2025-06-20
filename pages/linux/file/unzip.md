# unzip Command

Extract files from ZIP archives

[Back to File Commands](./index.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Description |
|--------|-------------|
| `-l` | List archive contents |
| `-d <dir>` | Extract to specified directory |
| `-q` | Quiet mode |

## Examples
1. **Run command**:
```bash
unzip archive.zip
```
Output: Extracts archive.zip to current directory

2. **Run command**:
```bash
unzip -d /extract archive.zip
```
Output: Extracts archive.zip to /extract


## Notes
- Requires `unzip` package (`sudo apt install unzip`)
- Overwrites files unless `-n` is used

## References
- [man unzip](https://man7.org/linux/man-pages/man1/unzip.1.html)

[Back to File Commands](../index.md) | [Back to Main Index](../../README.md)