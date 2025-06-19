# Linux `file` Command

The `file` command determines the type of a file by examining its contents. It is useful for identifying file formats, such as text, binary, or image files, without relying on extensions.

[Back to File Commands](../file.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Purpose | Example |
|--------|---------|---------|
| `-b` | Brief output (omit filenames) | `file -b image.jpg` (Show only file type) |
| `-i` | Output MIME type | `file -i file.txt` (Show `text/plain; charset=utf-8`) |
| `-f <file>` | Read filenames from a file | `file -f list.txt` (Process files listed in `list.txt`) |
| `-L` | Follow symbolic links | `file -L link.txt` (Analyze target file) |
| `-z` | Look inside compressed files | `file -z archive.gz` (Show type of compressed content) |
| `-s` | Read special files (e.g., block devices) | `file -s /dev/sda` (Analyze device file) |

## Examples
1. **Identify a single file**:  
   `file document.txt`  
   Outputs `document.txt: ASCII text`.
2. **Check multiple files**:  
   `file *.jpg`  
   Identifies types of all `.jpg` files in the current directory.
3. **Show MIME type**:  
   `file -i script.sh`  
   Outputs `script.sh: text/x-shellscript; charset=us-ascii`.
4. **Analyze compressed file contents**:  
   `file -z backup.tar.gz`  
   Shows the type of files inside the compressed archive.

## Notes
- `file` relies on magic numbers and heuristics, not just extensions, for accurate identification.
- Use `-b` with pipes, e.g., `find . -type f | xargs file -b`.
- The `-s` option is useful for inspecting device files or raw data.

## References
- [file Command Manual](https://man7.org/linux/man-pages/man1/file.1.html)
- [GNU file](https://www.darwinsys.com/file/)

[Back to File Commands](../file.md) | [Back to Main Index](../../README.md)
