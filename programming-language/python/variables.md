# variable usage

## referencing a global variable in function

You need to declare it as global

```python
var = 1
def func():
    global var
    var = 2
```
