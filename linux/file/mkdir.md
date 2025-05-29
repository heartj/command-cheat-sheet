# Linux `mkdir` Command

The `mkdir` command creates directories. It is used to organize files by creating new folders in the file system.

[Back to File Commands](../file.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Purpose | Example |
|--------|---------|---------|
| `-p` | Create parent directories as needed | `mkdir -p dir/subdir` (Create `dir` and `subdir`) |
| `-m <mode>` | Set permissions for new directories | `mkdir -m 755 new_dir` (Create `new_dir` with 755 permissions) |
| `-v` | Verbose output (show created directories) | `mkdir -v new_dir` (Show confirmation of creation) |
| `-Z` | Set SELinux security context | `mkdir -Z secure_dir` (Set SELinux context) |

## Examples
1. **Create a single directory**:  
   `mkdir project`  
   Creates a directory named `project`.
2. **Create nested directories**:  
   `mkdir -p src/main/java`  
   Creates the full path `src/main/java` if parent directories don’t exist.
3. **Create directory with specific permissions**:  
   `mkdir -m 700 private_dir`  
   Creates `private_dir` with owner-only permissions.
4. **Create multiple directories**:  
   `mkdir dir1 dir2 dir3`  
   Creates `dir1`, `dir2`, and `dir3` in the current directory.

## Notes
- Use `-p` to avoid errors when parent directories are missing.
- Check permissions with `ls -ld` after using `-m`.
- SELinux contexts (`-Z`) are relevant only on systems with SELinux enabled.

## References
- [GNU Coreutils: mkdir](https://www.gnu.org/software/coreutils/manual/html_node/mkdir-invocation.html)
- [man mkdir](https://man7.org/linux/man-pages/man1/mkdir.1.html)

[Back to File Commands](../file.md) | [Back to Main Index](../../README.md)
