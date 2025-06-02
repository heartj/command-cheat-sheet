# Linux `du` Command

The `du` command estimates disk usage for files and directories. It is used to analyze how much space files or directories occupy, helping with storage management.

[Back to File Commands](../file.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Purpose | Example |
|--------|---------|---------|
| `-h` | Show human-readable sizes (e.g., KB, MB) | `du -h /home` (Display sizes in readable format) |
| `-s` | Summarize total size of a directory | `du -sh /var/log` (Show total size of `/var/log`) |
| `-a` | Include files (not just directories) | `du -ah /tmp` (Show sizes for files and directories) |
| `-c` | Display grand total | `du -ch *.txt` (Show total size for `.txt` files) |
| `--max-depth=<n>` | Limit depth of directory traversal | `du -h --max-depth=1 /home` (Show sizes one level deep) |
| `-b` | Show sizes in bytes | `du -b file.txt` (Display exact byte count) |
| `--exclude=<pattern>` | Exclude files matching pattern | `du -h --exclude="*.log" /var` (Skip `.log` files) |

## Examples
1. **Summarize directory size**:  
   `du -sh /home/user`  
   Shows the total size of `/home/user` in human-readable format.
2. **List sizes of all files and directories**:  
   `du -ah /tmp | sort -h`  
   Displays sizes for all items in `/tmp`, sorted by size.
3. **Show sizes one level deep**:  
   `du -h --max-depth=1 /var`  
   Lists sizes of top-level directories in `/var`.
4. **Calculate total size of specific files**:  
   `du -ch *.jpg`  
   Shows total size of all `.jpg` files with a grand total.

## Notes
- Use `sort -h` with `du` to sort human-readable sizes correctly.
- Combine with `grep` to filter specific paths, e.g., `du -ah | grep "\.txt$"`.
- Be cautious with large directories, as `du` can be slow; use `--max-depth` to limit scope.

## References
- [GNU Coreutils: du](https://www.gnu.org/software/coreutils/manual/html_node/du-invocation.html)
- [man du](https://man7.org/linux/man-pages/man1/du.1.html)

[Back to File Commands](../file.md) | [Back to Main Index](../../README.md)
