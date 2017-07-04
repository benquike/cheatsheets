# functools module

The functools module provides tools for adapting or
extending functions and other callable objects, without
completely rewriting them.

## partial object

functools module provides a partial class, which can be used to wrap
a callable object with default arguments. The resulting object is itself
callable and can be treated as though it is the original function.
It takes all of the same arguments as the original, and can be invoked with
extra positional or named arguments as well.

Example:

```
import functools

def myfunc(a, b=2):
    print('  called myfunc with:', (a, b))

p = functools.partial(myfunc, b=4)

myfunc("passing a")
>>> ('  called myfunc with:', ('passing a', 2))

p("passing a")
>>> ('  called myfunc with:', ('passing a', 4))
```

## total_ordering

This decorator works on classes.
Given a class having:
- `__lt__`
- `__le__`
- `__gt__`
- `__gt__`
- `__eq__`

This decorator will supply other methods
to make it a total-ordering class.


## wrappers

```
from functools import wraps

def my_decorator(f):
    @wraps(f)
    def wrapper(*args, **kwds):
        print 'Calling decorated function'
        return f(*args, **kwds)
    return wrapper

@my_decorator
def example():
    """Docstring"""
    print 'Called example function'

example()

>> Calling decorated function
>> Called example function

example.__name__
>> 'example'

example.__doc__
'Docstring'
```
