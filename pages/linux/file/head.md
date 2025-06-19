# Linux `head` Command

The `head` command displays the first part of files, typically the first 10 lines by default. It is useful for quickly inspecting the beginning of text files or logs.

[Back to File Commands](../file.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Purpose | Example |
|--------|---------|---------|
| `-n <num>` | Show first `<num>` lines | `head -n 5 file.txt` (Show first 5 lines) |
| `-c <num>` | Show first `<num>` bytes | `head -c 100 file.txt` (Show first 100 bytes) |
| `-q` | Quiet mode (suppress headers for multiple files) | `head -q file1.txt file2.txt` (No headers) |
| `-v` | Verbose mode (show file headers) | `head -v file.txt` (Show filename header) |
| `-z` | Use NUL as line separator | `head -z -n 1 file.txt` (Handle NUL-separated input) |

## Examples
1. **Show first 10 lines**:  
   `head file.txt`  
   Displays the first 10 lines of `file.txt`.
2. **Show specific number of lines**:  
   `head -n 20 log.txt`  
   Shows the first 20 lines of `log.txt`.
3. **Show first 100 bytes**:  
   `head -c 100 data.bin`  
   Outputs the first 100 bytes of `data.bin`.
4. **Process multiple files**:  
   `head -n 5 *.txt`  
   Shows the first 5 lines of each `.txt` file.

## Notes
- Use with pipes, e.g., `cat file.txt | head -n 5` for filtering.
- Combine with `grep` to find specific lines, e.g., `head -n 100 log.txt | grep "error"`.
- For large files, `head` is more efficient than viewing the entire file.

## References
- [GNU Coreutils: head](https://www.gnu.org/software/coreutils/manual/html_node/head-invocation.html)
- [man head](https://man7.org/linux/man-pages/man1/head.1.html)

[Back to File Commands](../file.md) | [Back to Main Index](../../README.md)
