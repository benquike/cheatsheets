# static methods

If we mark a method of a class as `@staticmethod`, that
function will be called when the module is loaded.


```python

class MyClass(object):
    @staticmethod
    def the_static_method(x):
        print(x)
```


# ref
1. https://stackoverflow.com/questions/735975/static-methods-in-python
