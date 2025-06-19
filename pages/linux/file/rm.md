# Linux `rm` Command

The `rm` command removes files or directories. It is used to delete unwanted files or directories, but requires caution as deletions are typically irreversible.

[Back to File Commands](../file.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Purpose | Example |
|--------|---------|---------|
| `-r` | Remove directories recursively | `rm -r old_folder/` (Delete `old_folder` and contents) |
| `-f` | Force deletion without prompting | `rm -f file.txt` (Delete without confirmation) |
| `-i` | Prompt before each removal | `rm -i *.txt` (Prompt for each `.txt` file) |
| `-v` | Verbose output (show deleted files) | `rm -v *.log` (Show each deleted file) |
| `-d` | Remove empty directories | `rm -d empty_dir/` (Delete empty directory) |
| `--no-preserve-root` | Allow deletion of `/` (dangerous) | `rm -r --no-preserve-root /` (Use with extreme caution) |

## Examples
1. **Delete a single file**:  
   `rm file.txt`  
   Removes `file.txt` from the current directory.
2. **Delete a directory recursively**:  
   `rm -rf old_project/`  
   Deletes `old_project` and all its contents without prompting.
3. **Prompt before deletion**:  
   `rm -i *.bak`  
   Asks for confirmation before deleting each `.bak` file.
4. **Delete empty directories**:  
   `rm -d temp_dir/`  
   Removes `temp_dir` if it is empty.

## Notes
- Use `-i` in scripts to avoid accidental deletions.
- Be extremely cautious with `rm -rf`, especially with wildcards or near `/`.
- Deleted files are not sent to a recycle bin; consider using `trash-cli` for recoverable deletion.

## References
- [GNU Coreutils: rm](https://www.gnu.org/software/coreutils/manual/html_node/rm-invocation.html)
- [man rm](https://man7.org/linux/man-pages/man1/rm.1.html)

[Back to File Commands](../file.md) | [Back to Main Index](../../README.md)
