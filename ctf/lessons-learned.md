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

## injecting special chars to victim program

the shell separate input using `;`, but it can be escaped.
So we can inject strings containing any chars to program argument.

`scanf` seperate input using `\x0a`, so we can not input strings
containing `\0x0a` to scanf(is there any workaround?TBC).

If you want to inject some address containing `0x0a` to scanf to
and the address is located in the stack, we can change that addresses
by injecting some arguments or environmental variables to the program
and thus avoiding injecting addresses containing `0x0a`(learned from Greg).

[^1]: http://askubuntu.com/questions/41629/after-upgrade-gdb-wont-attach-to-process
