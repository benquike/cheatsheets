# Lessons

## Get information about a process

### ptrace
`ptrace` or `gdb` can be used to get information about a running process.
But this can be restricted by the administrator[^1].

This is configured in `/etc/sysctl.d/10-ptrace.conf `
by the following option(introduced in Ubuntu 10.10).

```
kernel.yama.ptrace_scope = 0
```


[^1]: http://askubuntu.com/questions/41629/after-upgrade-gdb-wont-attach-to-process
