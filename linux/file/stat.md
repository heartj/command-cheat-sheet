# Linux `stat` Command

The `stat` command displays detailed information about files or filesystems, including metadata like permissions, timestamps, and inode details. It is useful for inspecting file attributes.

[Back to File Commands](../file.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Purpose | Example |
|--------|---------|---------|
| `-f` | Display filesystem status instead of file | `stat -f /home` (Show filesystem info for `/home`) |
| `-c <format>` | Use custom output format | `stat -c "%n %s" file.txt` (Show name and size) |
| `-t` | Use terse output (machine-readable) | `stat -t file.txt` (Compact output) |
| `-L` | Follow symbolic links | `stat -L link.txt` (Show target file info) |
| `--format=<format>` | Specify detailed output format | `stat --format="%U %G" file.txt` (Show owner and group) |
| `-Z` | Show SELinux security context | `stat -Z file.txt` (Display SELinux context) |

## Examples
1. **Display file metadata**:  
   `stat file.txt`  
   Shows detailed info like size, permissions, and timestamps for `file.txt`.
2. **Custom output format**:  
   `stat -c "%n %A %s bytes" *.txt`  
   Lists name, permissions, and size for all `.txt` files.
3. **Show filesystem details**:  
   `stat -f /`  
   Displays filesystem info for the root filesystem.
4. **Check SELinux context**:  
   `stat -Z config.conf`  
   Shows security context (on SELinux-enabled systems).

## Notes
- Use `--format` with specifiers like `%s` (size), `%U` (user), `%A` (permissions) for custom output.
- Combine with `find` for batch processing, e.g., `find . -type f -exec stat -c "%n %s" {} \;`.
- SELinux options (`-Z`) are relevant only on systems with SELinux enabled.

## References
- [GNU Coreutils: stat](https://www.gnu.org/software/coreutils/manual/html_node/stat-invocation.html)
- [man stat](https://man7.org/linux/man-pages/man1/stat.1.html)

[Back to File Commands](../file.md) | [Back to Main Index](../../README.md)
