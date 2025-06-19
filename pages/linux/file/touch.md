# Linux `touch` Command

The `touch` command creates empty files or updates the timestamps (access or modification) of existing files or directories. It is commonly used to create placeholder files or trigger build systems.

[Back to File Commands](../file.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Purpose | Example |
|--------|---------|---------|
| `-a` | Update only access time | `touch -a file.txt` (Update access time of `file.txt`) |
| `-m` | Update only modification time | `touch -m file.txt` (Update modification time) |
| `-c` | Do not create file if it doesn’t exist | `touch -c nonexistent.txt` (No file created) |
| `-t <timestamp>` | Set specific timestamp (format `[[CC]YY]MMDDhhmm[.ss]`) | `touch -t 202501011200 file.txt` (Set timestamp to Jan 1, 2025) |
| `-r <file>` | Use timestamp of another file | `touch -r ref.txt file.txt` (Match `ref.txt`’s timestamp) |
| `-d <date>` | Set timestamp using date string | `touch -d "2025-01-01" file.txt` (Set to Jan 1, 2025) |

## Examples
1. **Create an empty file**:  
   `touch newfile.txt`  
   Creates `newfile.txt` if it doesn’t exist.
2. **Update timestamp of multiple files**:  
   `touch *.txt`  
   Updates timestamps of all `.txt` files.
3. **Set a specific timestamp**:  
   `touch -t 202501011200 document.txt`  
   Sets `document.txt`’s timestamp to Jan 1, 2025, 12:00 PM.
4. **Match timestamp of another file**:  
   `touch -r source.txt target.txt`  
   Sets `target.txt`’s timestamp to match `source.txt`.

## Notes
- If no options are specified, `touch` updates both access and modification times.
- Use `stat file.txt` to verify timestamps after using `touch`.
- Useful in build systems (e.g., `make`) to mark files as updated.

## References
- [GNU Coreutils: touch](https://www.gnu.org/software/coreutils/manual/html_node/touch-invocation.html)
- [man touch](https://man7.org/linux/man-pages/man1/touch.1.html)

[Back to File Commands](../file.md) | [Back to Main Index](../../README.md)
