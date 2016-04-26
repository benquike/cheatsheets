# Linux System administration

## zombie process
A zombie process is a dead process, but because
its parent is still live and not call wait on it.

It is actually a bug in the program. If a daemon
program pawns a lot processes and does not wait
on the child processes, those PCBs can not be reused.

To release the PCBs of zombie processes, we need to
kill their parent process and make init process their
parent, and init process will wait on them and release
the PCBs used by them.

This is the command to do this:

```
$ kill $(ps -A -ostat,ppid | awk '/[zZ]/{print $2}')
```
