# find Command

Search for files in a directory hierarchy

[Back to File Commands](./index.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Description |
|--------|-------------|
| `-name <pattern>` | Search by file name (e.g., -name "*.txt") |
| `-type <type>` | Specify file type (e.g., -type f for files) |
| `-mtime <days>` | Search by modification time (e.g., -mtime -7) |
| `-exec <command>` | Execute command on found files |

## Examples
1. **Run command**:
```bash
find /home -name "*.txt"
```
Output: Finds all .txt files in /home

2. **Run command**:
```bash
find . -type d
```
Output: Lists all directories in current directory

3. **Run command**:
```bash
find /var -mtime -7
```
Output: Finds files modified in the last 7 days in /var

4. **Run command**:
```bash
find . -name "*.log" -exec rm {} \;
```
Output: Deletes all .log files in current directory


## Notes
- Use quotes for patterns with wildcards
- Requires `sudo` for restricted directories

## References
- [man find](https://man7.org/linux/man-pages/man1/find.1.html)

[Back to File Commands](../index.md) | [Back to Main Index](../../README.md)