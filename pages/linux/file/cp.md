# Linux `cp` Command

The `cp` command copies files or directories from one location to another. It is widely used for duplicating files, backing up data, or transferring content between directories.

[Back to File Commands](../file.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Purpose | Example |
|--------|---------|---------|
| `-r` | Copy directories recursively | `cp -r src/ dest/` (Copy `src` directory to `dest`) |
| `-p` | Preserve file attributes (e.g., permissions, timestamps) | `cp -p file.txt file.bak` (Copy with attributes) |
| `-i` | Prompt before overwriting files | `cp -i file.txt /tmp/` (Prompt if file exists) |
| `-u` | Copy only if source is newer | `cp -u file.txt /backup/` (Update `/backup/file.txt`) |
| `-v` | Verbose output (show copied files) | `cp -v *.txt /tmp/` (Show each copied file) |
| `-a` | Archive mode (preserve structure and attributes) | `cp -a dir/ /backup/` (Copy `dir` with all attributes) |
| `-f` | Force overwrite without prompting | `cp -f file.txt /tmp/` (Overwrite without asking) |

## Examples
1. **Copy a single file**:  
   `cp document.txt /tmp/document.txt`  
   Copies `document.txt` to `/tmp`.
2. **Copy a directory recursively**:  
   `cp -r project/ /backup/project/`  
   Copies the entire `project` directory to `/backup`.
3. **Copy only newer files**:  
   `cp -uv *.jpg /backup/`  
   Copies `.jpg` files to `/backup` only if they are newer.
4. **Preserve attributes during copy**:  
   `cp -p config.conf /etc/config.conf`  
   Copies `config.conf` with its original permissions and timestamps.

## Notes
- Use `-i` to avoid accidental overwrites in scripts or batch operations.
- Combine `-r` and `-p` for copying directories with attributes, e.g., `cp -rp`.
- Be cautious with `-f`, as it overwrites files without confirmation.

## References
- [GNU Coreutils: cp](https://www.gnu.org/software/coreutils/manual/html_node/cp-invocation.html)
- [man cp](https://man7.org/linux/man-pages/man1/cp.1.html)

[Back to File Commands](../file.md) | [Back to Main Index](../../README.md)