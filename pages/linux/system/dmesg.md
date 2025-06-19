# dmesg Command

Display kernel ring buffer logs (hardware, kernel events)

[Back to System Commands](./index.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Description |
|--------|-------------|
| `-T` | Show human-readable timestamps |
| `--level=<level>` | Filter by log level (e.g., --level=err) |
| `-w` | Follow new messages in real-time |
| `-C` | Clear the kernel ring buffer |
| `-k` | Show only kernel messages |

## Examples
1. **Run command**:
```bash
dmesg -T
```
Output: Displays logs with readable dates and times

2. **Run command**:
```bash
dmesg -w
```
Output: Shows new kernel messages in real-time


## Notes
- Requires `sudo` to clear buffer or access restricted logs.
- Use `grep` to filter events (e.g., `dmesg | grep usb`).

## References
- [man dmesg](https://man7.org/linux/man-pages/man8/dmesg.8.html)

[Back to System Commands](../index.md) | [Back to Main Index](../../README.md)