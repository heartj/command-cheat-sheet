# wc Command

Count lines, words, or characters in files

[Back to Utilities Commands](./index.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Description |
|--------|-------------|
| `-l` | Count lines |
| `-w` | Count words |
| `-c` | Count bytes |
| `-m` | Count characters |

## Examples
1. **Run command**:
```bash
wc -l file.txt
```
Output: Shows number of lines in file.txt

2. **Run command**:
```bash
ls | wc -l
```
Output: Counts number of files in current directory

3. **Run command**:
```bash
wc file.txt
```
Output: Shows lines, words, and bytes in file.txt


## Notes
- Use with pipes for dynamic input.
- Handles multiple files.

## References
- [man wc](https://man7.org/linux/man-pages/man1/wc.1.html)

[Back to Utilities Commands](../index.md) | [Back to Main Index](../../README.md)