# itertools module


## count

This functions returns a iterator object.

## cycle

This will generate a iterator object that will cycle again
and and again.

```
import itertools

x = itertools.cycle("01")

for i in x:
    print i
>>> 01010101010101........

```

## chain

Chain two or more iterables together.

## compress

Drop data based in selectors

```
from itertools import *
x = compress([1,4,6,2,34,9],[True,False,True,True,True,False])
for i in x:
    print i
>>> 1 6 2 34
```

## dropwhile

Drop data based on condition

## takewhile

Save data based on condition

## groupby

## filter


## islice

## izip



## reference
1. [Python itertools Module](http://www.endmemo.com/python/itertools.php)
