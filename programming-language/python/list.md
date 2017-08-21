# list, set and tuples

## initialization

### static initialization
```
listA = [] # init as empty
listB = [i for i in range(10)]
```

### dynamic initialization
```
listC = list()
```

## mutate

### insert(index, value)
    Insert value at index

### remove(value)
    remove the first occurence of value in the list

### extend
    It accepts variadic arguents and extend the current list by appending all the elements in the argument list to it.
### append
add an element in the end of the list

### pop
    It accepts an `index` as argument and removes an element from the list at `index`. if no arguments are passed, the last element will be removed and returned

## query

### index(value, [start, [stop]])
    return the index of the first occurence of of value

### count(value)
    return the number of occurrences of value in the list

## reorder
### reverse
    reverse the list in place.
### sort
    In place sort. we can specify the key

    natural sort

```
import re

def atoi(text):
    return int(text) if text.isdigit() else text

    def natural_keys(text):
    '''
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    (See Toothy's implementation in the comments)
    '''
    return [ atoi(c) for c in re.split('(\d+)', text) ]

    alist=[
            "something1",
            "something12",
            "something17",
            "something2",
            "something25",
            "something29"]

    alist.sort(key=natural_keys)
    print(alist)
```

https://stackoverflow.com/questions/5967500/how-to-correctly-sort-a-string-with-a-number-inside
    

## Accessing elements like an array
### Accessing one element

```
a = [1,2,3,4,5]
a[0]
a[-1] # the last one
a[-2] # the second last one
```

### Accessing range

```
a = [1,2,3,4,5]
a[0:3] # starting from 0 to 3 -1 
a[4:] # 4 to end
a[:4] # 0 ~ 4(exclusive)
```

### getting all elements

```
a = [1,2,3,4,5]
```

## iteration

```
for elem in listA:
    do something with elem
    ...
```

## Other Misc
### clear
    removes all the elements in the list


## set

### union

`union` takes another set as argument and returns a set containing
the union of 2 sets, the original sets are intact(not updated)

### update

`a.update(b)`: `a` will be updated with elements in `b` added to it.
