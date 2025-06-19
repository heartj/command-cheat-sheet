# Linux `find` Command

The `find` command searches for files and directories in a specified path based on criteria like name, type, size, or modification time. It is a powerful tool for locating files across complex directory structures and can execute actions on matching files.

[Back to File Commands](../file.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Purpose | Example |
|--------|---------|---------|
| `-name <pattern>` | Match files by name (case-sensitive) | `find . -name "*.txt"` (Find all `.txt` files) |
| `-iname <pattern>` | Match files by name (case-insensitive) | `find /home -iname "readme*"` (Find files starting with "readme") |
| `-type <type>` | Match file type (e.g., `f` for file, `d` for directory) | `find . -type d` (Find all directories) |
| `-mtime <n>` | Match files modified `n` days ago | `find /tmp -mtime -1` (Find files modified in last day) |
| `-size <n>` | Match files by size (e.g., `+1M` for >1MB) | `find . -size +1M` (Find files larger than 1MB) |
| `-exec <command>` | Execute a command on found files | `find . -name "*.bak" -exec rm {} \;` (Delete all `.bak` files) |
| `-maxdepth <n>` | Limit search depth to `n` levels | `find . -maxdepth 2 -name "*.log"` (Search 2 levels deep) |

## Examples
1. **Find empty files**:  
   `find /tmp -type f -empty`  
   Locates all empty regular files in `/tmp`.
2. **Find and copy files**:  
   `find . -name "*.jpg" -exec cp {} /backup/ \;`  
   Copies all `.jpg` files to `/backup`.
3. **Find files modified within a specific time range**:  
   `find . -mtime -7 -mtime +2`  
   Finds files modified between 2 and 7 days ago.
4. **Find directories with specific permissions**:  
   `find /var -type d -perm 755`  
   Finds directories with exactly 755 permissions.

## Notes
- Use quotes around patterns (e.g., `"*.txt"`) to prevent shell expansion.
- Be cautious with `-exec`, as it can modify or delete files; test with `echo` first (e.g., `-exec echo rm {} \;`).
- Use `-maxdepth 1` to search only the current directory.
- Combine with `xargs` for complex operations, e.g., `find . -name "*.txt" | xargs grep "error"`.

## References
- [GNU findutils: find](https://www.gnu.org/software/findutils/manual/find.html)
- [man find](https://man7.org/linux/man-pages/man1/find.1.html)

[Back to File Commands](../file.md) | [Back to Main Index](../../README.md)