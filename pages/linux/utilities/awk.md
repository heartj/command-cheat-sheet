# awk Command

Process and analyze text using patterns and actions

[Back to Utilities Commands](./index.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Description |
|--------|-------------|
| `-F <delimiter>` | Specify field separator (e.g., -F ",") |
| `-v <var=value>` | Assign a variable |
| `{print $n}` | Print the nth field (e.g., {print $1}) |

## Examples
1. **Run command**:
```bash
awk -F ":" '{print $1}' /etc/passwd
```
Output: Prints usernames from /etc/passwd

2. **Run command**:
```bash
awk '{sum += $1} END {print sum}' numbers.txt
```
Output: Sums the first column in numbers.txt

3. **Run command**:
```bash
awk -v name="alice" '$1 == name {print $0}' users.txt
```
Output: Prints lines where first field is "alice"


## Notes
- Powerful for column-based data processing.
- Use single quotes to avoid shell interpretation.

## References
- [man awk](https://man7.org/linux/man-pages/man1/awk.1.html)

[Back to Utilities Commands](../index.md) | [Back to Main Index](../../README.md)