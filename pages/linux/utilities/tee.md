# tee Command

Read from standard input and write to standard output and files

[Back to Utilities Commands](./index.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Description |
|--------|-------------|
| `-a` | Append to files instead of overwriting |
| `-i` | Ignore interrupt signals |

## Examples
1. **Run command**:
```bash
ls | tee output.txt
```
Output: Writes ls output to output.txt and displays it

2. **Run command**:
```bash
echo "log" | tee -a log.txt
```
Output: Appends "log" to log.txt and displays it


## Notes
- Useful for logging pipeline output.
- Requires `sudo` for protected files.

## References
- [man tee](https://man7.org/linux/man-pages/man1/tee.1.html)

[Back to Utilities Commands](../index.md) | [Back to Main Index](../../README.md)