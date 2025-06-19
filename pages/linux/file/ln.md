# Linux `ln` Command

The `ln` command creates hard or symbolic links between files or directories. Symbolic links act as shortcuts, while hard links share the same inode as the original file.

[Back to File Commands](../file.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Purpose | Example |
|--------|---------|---------|
| `-s` | Create a symbolic link | `ln -s file.txt link.txt` (Create symbolic link `link.txt`) |
| `-f` | Force overwrite of existing links | `ln -sf new.txt link.txt` (Replace existing link) |
| `-v` | Verbose output (show created links) | `ln -sv file.txt link.txt` (Show link creation) |
| `-n` | Treat existing destination as a file, not a directory | `ln -snf file.txt dir/link` (Force link in directory) |
| `-i` | Prompt before overwriting | `ln -si file.txt link.txt` (Prompt if link exists) |
| `--backup` | Create backup of overwritten links | `ln -s --backup file.txt link.txt` (Backup existing link) |

## Examples
1. **Create a symbolic link**:  
   `ln -s /etc/config.conf config_link`  
   Creates a symbolic link `config_link` pointing to `config.conf`.
2. **Create a hard link**:  
   `ln file.txt hard_link.txt`  
   Creates a hard link `hard_link.txt` to `file.txt`.
3. **Replace an existing link**:  
   `ln -sf newfile.txt link.txt`  
   Overwrites `link.txt` to point to `newfile.txt`.
4. **Link a directory**:  
   `ln -s /var/log logs`  
   Creates a symbolic link `logs` to `/var/log`.

## Notes
- Symbolic links (`-s`) can point to files or directories and work across filesystems.
- Hard links (no `-s`) cannot cross filesystems and only work for regular files.
- Use `ls -l` to verify links (symbolic links show `l` and the target path).

## References
- [GNU Coreutils: ln](https://www.gnu.org/software/coreutils/manual/html_node/ln-invocation.html)
- [man ln](https://man7.org/linux/man-pages/man1/ln.1.html)

[Back to File Commands](../file.md) | [Back to Main Index](../../README.md)
