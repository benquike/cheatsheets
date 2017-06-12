# threading module

## create threads


## use timers

`threading.Timer` can be used to create timers

```python
t = Timer(30.0, f, args=[], kwargs={})
t.start()
```
That way, function f will be called 30 seconds later.
