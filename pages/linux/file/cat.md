# Linux `cat` Command

The `cat` command concatenates and displays file contents. It is commonly used to view file contents, combine files, or redirect output to another file.

[Back to File Commands](../file.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Purpose | Example |
|--------|---------|---------|
| `-n` | Number all output lines | `cat -n file.txt` (Show line numbers) |
| `-b` | Number non-blank lines | `cat -b file.txt` (Number non-empty lines) |
| `-s` | Squeeze multiple blank lines into one | `cat -s file.txt` (Reduce blank lines) |
| `-E` | Show `$` at end of each line | `cat -E file.txt` (Mark line endings) |
| `-T` | Show tabs as `^I` | `cat -T file.txt` (Show tab characters) |
| `-v` | Show non-printing characters | `cat -v file.txt` (Display control characters) |

## Examples
1. **Display file contents**:  
   `cat readme.txt`  
   Prints the contents of `readme.txt` to the terminal.
2. **Concatenate multiple files**:  
   `cat file1.txt file2.txt > combined.txt`  
   Combines `file1.txt` and `file2.txt` into `combined.txt`.
3. **Add line numbers**:  
   `cat -n script.sh`  
   Displays `script.sh` with line numbers.
4. **Create a file from input**:  
   `cat > newfile.txt`  
   Reads input from the terminal until `Ctrl+D`, saving to `newfile.txt`.

## Notes
- Use `less` or `more` for large files to avoid overwhelming the terminal.
- Combine with pipes, e.g., `cat file.txt | grep "pattern"` for searching.
- Be cautious with binary files, as `cat` may produce unreadable output.

## References
- [GNU Coreutils: cat](https://www.gnu.org/software/coreutils/manual/html_node/cat-invocation.html)
- [man cat](https://man7.org/linux/man-pages/man1/cat.1.html)

[Back to File Commands](../file.md) | [Back to Main Index](../../README.md)
