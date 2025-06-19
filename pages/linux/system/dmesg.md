# dmesg Command

The `dmesg` command displays the kernel ring buffer, showing system logs related to hardware and kernel events.

[Back to System Commands](../system.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Description |
|--------|-------------|
| `-T` | Show human-readable timestamps |
| `--level=<level>` | Filter by log level (e.g., `--level=err`) |
| `-w` | Follow new messages in real-time |
| `-C` | Clear the ring buffer |

## Examples

1. **Show kernel logs with timestamps**:
   ```bash
   dmesg -T
   ```
   Output: Displays logs with readable dates and times.

2. **Follow kernel messages**:
   ```bash
   dmesg -w
   ```
   Output: Shows new kernel messages as they occur.

## Notes
- Requires `sudo` to clear buffer (`-C`) or access restricted logs.
- Use `grep` to filter specific events (e.g., `dmesg | grep usb`).
- Large buffers may need `--buffer-size` adjustment.

## References
- [man dmesg](https://man7.org/linux/man-pages/man8/dmesg.8.html)
- [util-linux Documentation](https://www.kernel.org/doc/html/latest/)

[Back to System Commands](../system.md) | [Back to Main Index](../../README.md)