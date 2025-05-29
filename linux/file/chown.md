# Linux `chown` Command

The `chown` command changes the owner and/or group of files or directories. It is used to manage access control by assigning ownership to specific users or groups.

[Back to File Commands](../file.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Purpose | Example |
|--------|---------|---------|
| `-R` | Apply changes recursively | `chown -R user:group dir/` (Change owner for `dir` and contents) |
| `-v` | Verbose output (show changed files) | `chown -v user file.txt` (Show ownership change) |
| `-c` | Report only when changes are made | `chown -c user:group file.txt` (Show changes only) |
| `--reference=<file>` | Copy ownership from another file | `chown --reference=ref.txt file.txt` (Match `ref.txt` ownership) |
| `-f` | Suppress error messages | `chown -f user file.txt` (Ignore errors) |
| `-h` | Change symbolic link ownership (not target) | `chown -h user link.txt` (Change link ownership) |

## Examples
1. **Change file owner**:  
   `chown user1 file.txt`  
   Sets `user1` as the owner of `file.txt`.
2. **Change owner and group**:  
   `chown user1:group1 file.txt`  
   Sets `user1` as owner and `group1` as group.
3. **Change ownership recursively**:  
   `chown -R webuser:webgroup /var/www/`  
   Sets ownership for `/var/www` and its contents.
4. **Copy ownership from another file**:  
   `chown --reference=template.txt file.txt`  
   Applies `template.txt`’s ownership to `file.txt`.

## Notes
- Use `ls -l` to verify ownership after changes.
- Requires root privileges to change ownership to another user.
- Use `-h` for symbolic links to avoid modifying the target file.

## References
- [GNU Coreutils: chown](https://www.gnu.org/software/coreutils/manual/html_node/chown-invocation.html)
- [man chown](https://man7.org/linux/man-pages/man1/chown.1.html)

[Back to File Commands](../file.md) | [Back to Main Index](../../README.md)
