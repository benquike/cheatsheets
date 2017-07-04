# python __XX__ functions

## attribute access

###  __getattr__(self, attr)
    x.__getattr__(self, attr) <==> x.attr
    Only called when attr isn't found in any of the usual places (it is not an instance attribute or a class attribute, and class is old-style or __getattribute__ is not defined).
    Should return the value of the key attr in the relevant mapping object.
    If not implemented, the attribute cannot be found and an AttributeError is raised.

### __getattribute__(self, attr)
    x.__getattribute__(self, attr) <==> x.attr
    New-style classes only.
    Called whenever attribute assignment is attempted (unlike __getattr__).
    Should return the value of the key attr in the relevant mapping object.
    If not implemented, Python will find the attribute as normal (including calling __getattr__).
    If raises AttributeError, Python will call __getattr__, but will not look anywhere else for the attribute.

### __setattr__(self, attr, value)
    x.__setattr__(self, attr, value) <==> x.attr = value
    Called whenever attribute assignment is attempted.
    Should give attr a value of value in the relevant mapping object.
    If not implemented, Python will assign the attribute to the instance as normal: self.__dict__[attr] = value for old-style classes and object.__setattr__(self, attr, value) for new-style classes.

### __delattr__(self, attr)
    x.__delattr__(self, attr) <==> del x.attr
    Called whenever attribute deletion is attempted.
    Should delete the key attr in the relevant mapping object.
    If not implemented, Python deletes the attribute as normal: del x.__dict__[attr] for old-style classes and object.__delattr__(self, attr) for new-style classes. (I think, can anyone verify?)

## __new__ and __init__

```
Use __new__ when you need to control the creation of a new instance. Use __init__ when you need to control initialization of a new instance.

__new__ is the first step of instance creation. It's called first, and is responsible for returning a new instance of your class. In contrast, __init__ doesn't return anything; it's only responsible for initializing the instance after it's been created.

In general, you shouldn't need to override __new__ unless you're subclassing an immutable type like str, int, unicode or tuple.
```

## operator overloading

To overload add, subtraction and multiplication,
we can overload `__add__`, `__sub__`, `__mul__`
functions

To overide `[]` operator, we need to overload the
following functions: `__getitem__` and `__setitem__`:


https://stackoverflow.com/questions/20507745/overloading-addition-subtraction-and-multiplication-operators


## pickling

`__getstate__` and `__setstate__` decide how the objects are serialized and deserialized.

## Full reference
1. [Python __Underscore__ Methods](http://www.siafoo.net/article/57)
2. [Magic Methods and Operator Overloading](http://www.python-course.eu/python3_magic_methods.php)
