# interval tree

A mutable, self-balancing interval tree for Python 2 and 3.
Queries may be by point, by range overlap, or by range envelopment.


Build AVL tree
```
from intervaltree import Interval, IntervalTree
t = IntervalTree()
```

Setup values of intervals
```
t[1:2] = "1-2"
```

Query
```
x = t[0:1]
```

This returns a set of `Interval`s.

https://pypi.python.org/pypi/intervaltree/2.0.4
