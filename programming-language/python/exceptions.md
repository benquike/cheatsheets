# exceptions in python

## built-in exceptions

https://docs.python.org/2/library/exceptions.html


## catch and pring backtrace

```
import traceback

try:
    raise TypeError("Oups!")
except Exception, err:
    try:
        raise TypeError("Again !?!")
    except:
        pass

    traceback.print_exc()
```

https://stackoverflow.com/questions/3702675/how-to-print-the-full-traceback-without-halting-the-program
