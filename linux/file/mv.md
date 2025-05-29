# Linux `mv` Command

The `mv` command moves or renames files and directories. It is used to relocate files to a new directory or change their names without creating copies.

[Back to File Commands](../file.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Purpose | Example |
|--------|---------|---------|
| `-i` | Prompt before overwriting files | `mv -i file.txt /tmp/` (Prompt if file exists) |
| `-u` | Move only if source is newer | `mv -u file.txt /backup/` (Move if newer) |
| `-v` | Verbose output (show moved files) | `mv -v *.txt /tmp/` (Show each moved file) |
| `-f` | Force overwrite without prompting | `mv -f file.txt /tmp/` (Overwrite without asking) |
| `-n` | Do not overwrite existing files | `mv -n file.txt /tmp/` (Skip if file exists) |
| `-b` | Create backup of overwritten files | `mv -b file.txt /tmp/` (Create backup with `~` suffix) |

## Examples
1. **Rename a file**:  
   `mv oldname.txt newname.txt`  
   Renames `oldname.txt` to `newname.txt`.
2. **Move files to a directory**:  
   `mv *.jpg /photos/`  
   Moves all `.jpg` files to `/photos`.
3. **Move with backup**:  
   `mv -b config.conf /etc/`  
   Moves `config.conf` to `/etc`, backing up existing file.
4. **Move only newer files**:  
   `mv -uv *.log /backup/`  
   Moves `.log` files to `/backup` if they are newer.

## Notes
- Unlike `cp`, `mv` does not create copies; it relocates files.
- Use `-i` or `-n` in scripts to avoid accidental overwrites.
- Moving files across filesystems (e.g., different drives) may involve copying and deleting.

## References
- [GNU Coreutils: mv](https://www.gnu.org/software/coreutils/manual/html_node/mv-invocation.html)
- [man mv](https://man7.org/linux/man-pages/man1/mv.1.html)

[Back to File Commands](../file.md) | [Back to Main Index](../../README.md)
