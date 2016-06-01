# Iterable, iterator, Generator

## Definition

### Iterable
A container is called `iterable` if it has the `__iter__` method defined

### Iterator
Iterator is an object that has the following 2 methods defined which is specified by the iterator protocol:

- __iter__: a method that returns itself.
- next:a method that returns the next value every time it is invoked

### Generator
A generator is a function that returns a series of values(one at a time it is called)instead of
a list at a time.

## Reference
1. Understanding Python Iterables and Iterators[^1]
2. Python practice book[^2]

[^1]: http://www.shutupandship.com/2012/01/understanding-python-iterables-and.html
[^2]: http://anandology.com/python-practice-book/iterators.html
