# List

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


## iteration

```
for elem in listA:
    do something with elem
    ...
```

## Other Misc
### clear
    removes all the elements in the list
