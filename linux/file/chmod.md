# Linux `chmod` Command

The `chmod` command changes the permissions of files or directories. Permissions control who can read, write, or execute a file, specified in numeric (octal) or symbolic notation.

[Back to File Commands](../file.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Purpose | Example |
|--------|---------|---------|
| `-R` | Apply permissions recursively | `chmod -R 755 dir/` (Set permissions for `dir` and contents) |
| `-v` | Verbose output (show changed files) | `chmod -v 644 file.txt` (Show permission change) |
| `-c` | Report only when changes are made | `chmod -c 755 script.sh` (Show changes only) |
| `--reference=<file>` | Copy permissions from another file | `chmod --reference=ref.txt file.txt` (Match `ref.txt` permissions) |
| `-f` | Suppress error messages | `chmod -f 600 file.txt` (Ignore errors) |

## Examples
1. **Set permissions using octal notation**:  
   `chmod 644 file.txt`  
   Sets `file.txt` to read/write for owner, read-only for group and others.
2. **Set permissions using symbolic notation**:  
   `chmod u+x script.sh`  
   Adds execute permission for the owner of `script.sh`.
3. **Change permissions recursively**:  
   `chmod -R 755 public/`  
   Sets `public` directory and its contents to 755.
4. **Copy permissions from another file**:  
   `chmod --reference=template.txt file.txt`  
   Applies `template.txt`’s permissions to `file.txt`.

## Notes
- Common octal modes: `644` (files: owner read/write, others read), `755` (executables/directories: owner full, others read/execute).
- Symbolic notation uses `u` (user), `g` (group), `o` (others), and `+`/`-`/`=` for adding/removing/setting permissions.
- Use `ls -l` to verify permissions after changes.

## References
- [GNU Coreutils: chmod](https://www.gnu.org/software/coreutils/manual/html_node/chmod-invocation.html)
- [man chmod](https://man7.org/linux/man-pages/man1/chmod.1.html)

[Back to File Commands](../file.md) | [Back to Main Index](../../README.md)
