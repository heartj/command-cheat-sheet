# traceroute Command

Trace the route packets take to a network host

[Back to Network Commands](./index.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Description |
|--------|-------------|
| `-n` | Show numerical addresses instead of hostnames |
| `-m <max_hops>` | Set maximum number of hops |
| `-w <timeout>` | Set wait timeout for each hop |
| `-I` | Use ICMP ECHO instead of UDP |

## Examples
1. **Run command**:
```bash
traceroute google.com
```
Output: Shows the route to `google.com` with hop details

2. **Run command**:
```bash
traceroute -n -m 10 example.com
```
Output: Traces up to 10 hops to `example.com` with numerical addresses


## Notes
- Requires `sudo` for some options (e.g., `-I`).
- Use `mtr` for real-time tracing.

## References
- [man traceroute](https://man7.org/linux/man-pages/man8/traceroute.8.html)

[Back to Network Commands](../index.md) | [Back to Main Index](../../README.md)