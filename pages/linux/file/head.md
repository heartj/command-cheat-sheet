# head Command

Display the beginning of files

[Back to File Commands](./index.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Description |
|--------|-------------|
| `-n <lines>` | Show specified number of lines |
| `-c <bytes>` | Show specified number of bytes |
| `-q` | Quiet mode, suppress file names |

## Examples
1. **Run command**:
```bash
head -n 5 file.txt
```
Output: Shows first 5 lines of file.txt

2. **Run command**:
```bash
head file1.txt file2.txt
```
Output: Shows first 10 lines of each file


## Notes
- Default is 10 lines
- Use with `tail` for specific ranges

## References
- [man head](https://man7.org/linux/man-pages/man1/head.1.html)

[Back to File Commands](../index.md) | [Back to Main Index](../../README.md)