# Linux `ls` Command

The `ls` command lists directory contents, displaying files and directories in the current or specified directory. It is one of the most frequently used Linux commands for navigating and inspecting file systems, offering various options to customize output format and content.

[Back to File Commands](../file.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Purpose | Example |
|--------|---------|---------|
| `-l` | Use long listing format (shows permissions, owner, size, etc.) | `ls -l` (List files with detailed information) |
| `-a` | Include hidden files (starting with `.`) | `ls -a` (Show all files, including `.hidden`) |
| `-h` | Show human-readable file sizes (e.g., KB, MB) | `ls -lh` (Long format with readable sizes) |
| `-t` | Sort by modification time (newest first) | `ls -lt` (List files sorted by time) |
| `-r` | Reverse sort order | `ls -lr` (Reverse the default sort order) |
| `-R` | List directories recursively | `ls -R` (Show contents of subdirectories) |
| `--color` | Colorize output (e.g., directories in blue) | `ls --color=auto` (Enable color output) |

## Examples
1. **List all files with details**:  
   `ls -la`  
   Shows all files (including hidden) in long format, including permissions and timestamps.
2. **Sort by size**:  
   `ls -lhS`  
   Lists files in long format, sorted by size (largest first), with human-readable sizes.
3. **List only directories**:  
   `ls -d */`  
   Displays only directories in the current path.
4. **List files modified in the last 2 days**:  
   `ls -lt --time-style=long-iso | grep "$(date -d '2 days ago' +%Y-%m-%d)"`  
   Filters files modified on a specific date.

## Notes
- Use `ls -F` to append indicators (e.g., `/` for directories, `*` for executables).
- Combine options for flexibility, e.g., `ls -lart` for all files, long format, sorted by time in reverse order.
- On some systems, `--color=auto` is enabled by default in interactive terminals.

## References
- [GNU Coreutils: ls](https://www.gnu.org/software/coreutils/manual/html_node/ls-invocation.html)
- [man ls](https://man7.org/linux/man-pages/man1/ls.1.html)

[Back to File Commands](../file.md) | [Back to Main Index](../../README.md)