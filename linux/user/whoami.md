# Linux `whoami` Command

The `whoami` command displays the username of the current effective user.

[Back to User Commands](../user.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Purpose | Example |
|--------|---------|---------|
| (none) | Show current username | `whoami` (Display current user) |

## Examples
1. **Show current user**:  
   `whoami`  
   Outputs the current user’s username (e.g., `john`).
2. **Use in scripts**:  
   `echo "Current user is $(whoami)"`  
   Prints the current username in a script.
3. **Check after `su`**:  
   `su john; whoami`  
   Confirms the user is now `john`.

## Notes
- No root privileges required.
- Useful for verifying the effective user in scripts or after `su`/`sudo`.
- Similar to `id -un` but simpler.

## References
- [man whoami](https://man7.org/linux/man-pages/man1/whoami.1.html)

[Back to User Commands](../user.md) | [Back to Main Index](../../README.md)
