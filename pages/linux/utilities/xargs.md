# xargs Command

Build and execute commands from standard input

[Back to Utilities Commands](./index.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Description |
|--------|-------------|
| `-n <number>` | Use at most <number> arguments per command |
| `-I <placeholder>` | Replace placeholder with input |
| `-t` | Print command before execution |

## Examples
1. **Run command**:
```bash
find . -name "*.txt" | xargs rm
```
Output: Deletes all .txt files in current directory

2. **Run command**:
```bash
echo "file1 file2" | xargs -n 1 ls
```
Output: Lists file1 and file2 separately

3. **Run command**:
```bash
find . -type f | xargs -I {} mv {} /backup
```
Output: Moves all files to /backup


## Notes
- Use with `find` for batch operations.
- Handle spaces in filenames with `-0`.

## References
- [man xargs](https://man7.org/linux/man-pages/man1/xargs.1.html)

[Back to Utilities Commands](../index.md) | [Back to Main Index](../../README.md)