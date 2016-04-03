# dict

## initialization

### static initialization
```
d1 = {}
d2 = {'a':1, 'b':3}
```

### dynamic initialization
```
d3 = dict()
```

## accessing elements
### Using array-like accessors
```
print d2['a']
print d2['b']
```
### get
passing it a key object, the associated value object will be returned

## updating elements
### change the value of an element
```
d2['b'] = 9
```
### remove an element
```
del d2['b']
```

## iteration
### keys
    Get the list of keys
### values
    Get the list of values
### items
    Get the list of (key, val) pairs


## Merge
### update
    udpate can be used to merge 2 dicts together
