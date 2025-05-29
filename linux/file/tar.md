# Linux `tar` Command

The `tar` command creates or extracts archive files, often used for bundling files or directories into a single file, typically with compression (e.g., `.tar.gz`).

[Back to File Commands](../file.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Purpose | Example |
|--------|---------|---------|
| `-c` | Create a new archive | `tar -cvf archive.tar files/` (Create `archive.tar`) |
| `-x` | Extract files from an archive | `tar -xvf archive.tar` (Extract `archive.tar`) |
| `-z` | Use gzip compression | `tar -czvf archive.tar.gz files/` (Create compressed archive) |
| `-j` | Use bzip2 compression | `tar -cjvf archive.tar.bz2 files/` (Create bzip2 archive) |
| `-t` | List archive contents | `tar -tvf archive.tar` (List contents of `archive.tar`) |
| `-f <file>` | Specify archive file name | `tar -cf archive.tar file.txt` (Use `archive.tar`) |
| `-v` | Verbose output (show processed files) | `tar -xvf archive.tar` (Show extracted files) |

## Examples
1. **Create a compressed archive**:  
   `tar -czvf backup.tar.gz /home/user/`  
   Creates a gzip-compressed archive of `/home/user`.
2. **Extract an archive**:  
   `tar -xzvf backup.tar.gz -C /tmp/`  
   Extracts `backup.tar.gz` to `/tmp`.
3. **List archive contents**:  
   `tar -tvf archive.tar`  
   Shows files in `archive.tar` without extracting.
4. **Append files to an existing archive**:  
   `tar -rvf archive.tar newfile.txt`  
   Adds `newfile.txt` to `archive.tar`.

## Notes
- Use `-C <directory>` to change the extraction directory.
- Combine compression options (e.g., `-z` for gzip, `-j` for bzip2) for smaller archives.
- Ensure sufficient disk space when extracting large archives.

## References
- [GNU tar Manual](https://www.gnu.org/software/tar/manual/tar.html)
- [man tar](https://man7.org/linux/man-pages/man1/tar.1.html)

[Back to File Commands](../file.md) | [Back to Main Index](../../README.md)
