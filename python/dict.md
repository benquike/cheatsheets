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

## query

### checking the existence of elements
#### hasattr
passing it an object `o`, it will return a boolean indicating whether there is some value
associated with key `o`.

```
m = {'a': 1, 'b': 2}

if hasattr(m, 'a')
```

It is also used in implementing the keyword `in` to check whether a global or local variable
is defined or not.

```
# to check whether 'a' is defined as a local variable

if 'myVar' in locals():
    print "myVar is defined locally"
if 'myVar' in globals():
    print "myVar is defined globally"
```

### Using array-like accessors
    ```
    print d2['a']
    print d2['b']
    ```

### get
Passing it a key object, the associated value object will be returned

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
