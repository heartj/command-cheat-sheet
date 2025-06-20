# grep Command

Search text using patterns

[Back to Utilities Commands](./index.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Description |
|--------|-------------|
| `-i` | Ignore case distinctions |
| `-r` | Search recursively in directories |
| `-n` | Show line numbers |
| `-v` | Invert match, show non-matching lines |
| `-E` | Use extended regular expressions |

## Examples
1. **Run command**:
```bash
grep "error" /var/log/syslog
```
Output: Shows lines containing "error" in syslog

2. **Run command**:
```bash
grep -rin "TODO" /src
```
Output: Recursively searches for "TODO" in /src with line numbers

3. **Run command**:
```bash
grep -v "^#" config.txt
```
Output: Shows non-comment lines in config.txt

4. **Run command**:
```bash
grep -E "[0-9]{3}-[0-9]{4}" file.txt
```
Output: Matches phone numbers like 123-4567


## Notes
- Use `zgrep` for compressed files.
- Combine with pipes (e.g., `ps aux | grep python`).

## References
- [man grep](https://man7.org/linux/man-pages/man1/grep.1.html)

[Back to Utilities Commands](../index.md) | [Back to Main Index](../../README.md)