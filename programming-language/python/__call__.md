# __call__

if `__call__` is defined, when we use `()` operator
on an object, that method will be called.

```python
class A:

    def __init__(self, a):
        self.a = a
        print("A init")

    def __call__(self, b):
        print("A call")
        print(b + self.a)

```

```
a = A(1)
a(2)
    A call
    3
```
