# * and ** operator

Star(*) operator unpack a sequence or collection to a positional arguments

```
def sum(a, b):
    return a + b

values = (1, 2)

s = sum(*values) # same as s = sum(1,2)
```


Double star(**) unpack a dict into a list of named args:

```python
values = { 'a': 1, 'b': 2 }
s = sum(**values) # same as s = sum(a = 1, b = 2)
```

# Reference

1. https://stackoverflow.com/questions/2921847/what-does-the-star-operator-mean
