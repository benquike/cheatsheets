# gdb usage

## debugging forked programms


```
set follow-fork-mode child
```

Will make gdb trace the parent process.

```
set follow-fork-mode child
```

Will make gdb trace the child process.


## debugging with multiple inferiors


```
set detach-on-fork mode
```

Tells gdb whether to detach one of the processes after a fork, or retain debugger control over them both.

* on

The child process (or parent process, depending on the value of follow-fork-mode) will be detached and allowed to run independently. This is the default.

* off
Both processes will be held under the control of GDB. One process (child or parent, depending on the value of follow-fork-mode) is debugged as usual, while the other is held suspended.


https://sourceware.org/gdb/onlinedocs/gdb/Inferiors-and-Programs.html#Inferiors-and-Programs
