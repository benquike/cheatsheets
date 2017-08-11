# Linux Usage

## how to get the path of the executable of a process

```
$ sudo ls -l /proc/<pid>/exe
```

## kill all zombie processes

A zombie is already dead, so you cannot kill it. To clean up a zombie, it must be waited on by its parent, so killing the parent should work to eliminate the zombie. (After the parent dies, the zombie will be inherited by init, which will wait on it and clear its entry in the process table.) If your daemon is spawning children that become zombies, you have a bug. Your daemon should notice when its children die and wait on them to determine their exit status.

```
kill $(ps -A -ostat,ppid | awk '/[zZ]/{print $2}')
```
