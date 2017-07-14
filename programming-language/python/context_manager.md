# context manager

`__enter__` and `__exit__` functions are called upon the creation of
a context and exit of a context.

## contextlib

`contextlib.contextmanager` decorator can be used
to create context managers.

```
from contextlib import contextmanager

@contextmanager
def open_file(path, mode):
    the_file = open(path, mode)
    yield the_file
    the_file.close()

files = []

for x in range(100000):
    with open_file('foo.txt', 'w') as infile:
        files.append(infile)

for f in files:
    if not f.closed:
        print('not closed')
```

## Reference

1. [Python with Context Managers](https://jeffknupp.com/blog/2016/03/07/python-with-context-managers/)
