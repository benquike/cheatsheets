# bisect

## bisect_left(l, x)

Locate the place(index) to place `x` in a sorted array `l`. if there is an element
which is equal to `x`, the index **before** `x` is returned.

```python
a = [1, 2, 3, 4]
assert bisect.bisect_left(a, 3) == 2
```

## bisect_right

Locate the place(index) to place `x` in a sorted array `l`. if there is an element
which is equal to `x`, the index **after** `x` is returned.

```python
a = [1, 2, 3, 4]
assert bisect.bisect_left(a, 3) == 3
```

## bisect

Same as `bisect_right`

## insort_left(l, x)

Insert `x` in a sorted array `l` to make it sorted. if there is an element
which is equal to `x`, it is inserted **before** it.

```python
a = [1, 2, 3, 4]
assert bisect.inorder_left(a, 3) == [1, 2, 3, 3, 4]
```

## insort_right

Insert `x` in a sorted array `l` to make it sorted. if there is an element
which is equal to `x`, it is inserted **after** it.

```python
a = [1, 2, 3, 4]
assert bisect.inorder_left(a, 3) == [1, 2, 3, 3, 4]
```

## insort

Same as insort_right.
