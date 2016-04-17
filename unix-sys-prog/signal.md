# IPC with signal

## signal handlers
We need to define a signal handling function which has
the following signature.

```
void <signal handler func name> (int sig)
```

## register signal handlers

```
typedef void (*sighandler_t)(int);
sighandler_t signal(int signum, sighandler_t handler);
```


## signal numbers

all the signal numbers are listed here[^1]

[^1]: http://www.ucs.cam.ac.uk/docs/course-notes/unix-courses/Building/files/signals.pdf
