# Linux `nc` (netcat) Command

The `nc` (netcat) command is a versatile networking tool for reading and writing data across network connections using TCP or UDP. It is used for tasks like port scanning, creating simple servers, or transferring data.

[Back to Network Commands](../network.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Purpose | Example |
|--------|---------|---------|
| `-l` | Listen mode (act as a server) | `nc -l 12345` (Listen on port 12345) |
| `-p <port>` | Specify source port (client mode) | `nc -p 54321 localhost 12345` (Connect from port 54321) |
| `-u` | Use UDP instead of TCP | `nc -u localhost 12345` (Connect via UDP) |
| `-v` | Verbose output | `nc -v localhost 80` (Show connection details) |
| `-z` | Scan ports without sending data | `nc -z localhost 20-80` (Scan ports 20 to 80) |
| `-w <sec>` | Set timeout for connections | `nc -w 5 localhost 80` (Timeout after 5 seconds) |
| `-e <prog>` | Execute program on connection | `nc -l -e /bin/bash 12345` (Run `bash` on connection) |

## Examples
1. **Create a simple TCP server**:  
   `nc -l 12345`  
   Listens for incoming connections on port 12345.
2. **Connect to a server**:  
   `nc localhost 12345`  
   Connects to a server running on `localhost:12345`.
3. **Port scanning**:  
   `nc -zv localhost 20-80`  
   Scans ports 20 to 80 on `localhost` and reports open ports.
4. **Transfer a file**:  
   `nc -l 12345 > file.txt` (server) and `nc localhost 12345 < file.txt` (client)  
   Transfers `file.txt` from client to server.

## Notes
- Requires root privileges for binding to privileged ports (<1024).
- Different `nc` implementations (e.g., traditional vs. OpenBSD) may have varying options.
- Use `Ctrl+C` to stop a listening server.
- Be cautious with `-e`, as it can execute arbitrary programs (security risk).

## References
- [man nc](https://man7.org/linux/man-pages/man1/nc.1.html)
- [Netcat Documentation](http://nc110.sourceforge.net/)

[Back to Network Commands](../network.md) | [Back to Main Index](../../README.md)
