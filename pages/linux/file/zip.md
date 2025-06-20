# zip Command

Create compressed ZIP archives

[Back to File Commands](./index.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Description |
|--------|-------------|
| `-r` | Recursively include directories |
| `-v` | Verbose output |
| `-q` | Quiet mode |

## Examples
1. **Run command**:
```bash
zip archive.zip file.txt
```
Output: Creates archive.zip containing file.txt

2. **Run command**:
```bash
zip -r docs.zip /docs
```
Output: Recursively archives /docs into docs.zip


## Notes
- Requires `zip` package (`sudo apt install zip`)
- Use `unzip` to extract

## References
- [man zip](https://man7.org/linux/man-pages/man1/zip.1.html)

[Back to File Commands](../index.md) | [Back to Main Index](../../README.md)