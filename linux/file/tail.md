# Linux `tail` Command

The `tail` command displays the last part of files, typically the last 10 lines by default. It is commonly used to monitor log files or view the end of text files.

[Back to File Commands](../file.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Purpose | Example |
|--------|---------|---------|
| `-n <num>` | Show last `<num>` lines | `tail -n 5 file.txt` (Show last 5 lines) |
| `-c <num>` | Show last `<num>` bytes | `tail -c 100 file.txt` (Show last 100 bytes) |
| `-f` | Follow file for new data (monitor) | `tail -f log.txt` (Monitor `log.txt` for updates) |
| `-q` | Quiet mode (suppress headers for multiple files) | `tail -q file1.txt file2.txt` (No headers) |
| `-v` | Verbose mode (show file headers) | `tail -v file.txt` (Show filename header) |
| `-z` | Use NUL as line separator | `tail -z -n 1 file.txt` (Handle NUL-separated input) |

## Examples
1. **Show last 10 lines**:  
   `tail file.txt`  
   Displays the last 10 lines of `file.txt`.
2. **Show specific number of lines**:  
   `tail -n 20 log.txt`  
   Shows the last 20 lines of `log.txt`.
3. **Monitor a log file**:  
   `tail -f /var/log/syslog`  
   Continuously displays new lines appended to `syslog`.
4. **Show last 100 bytes**:  
   `tail -c 100 data.bin`  
   Outputs the last 100 bytes of `data.bin`.

## Notes
- Use `-f` for real-time log monitoring, common in debugging or system administration.
- Combine with `grep`, e.g., `tail -n 100 log.txt | grep "error"` to filter recent entries.
- Use `Ctrl+C` to exit `-f` mode.

## References
- [GNU Coreutils: tail](https://www.gnu.org/software/coreutils/manual/html_node/tail-invocation.html)
- [man tail](https://man7.org/linux/man-pages/man1/tail.1.html)

[Back to File Commands](../file.md) | [Back to Main Index](../../README.md)
