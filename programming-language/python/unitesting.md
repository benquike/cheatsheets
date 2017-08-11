# unit testing in python


## doctest

## unittest and unittest2


## nose

### nosetests

http://nose.readthedocs.io/en/latest/usage.html

By deafult it scans all the python files, directories, modules matching `testMatch`
and recursively seaches python modules, functions and so on and so on in the current
working directory. by specifying `-w` we can tell `nosetests` where to find tests from.

passing in python files or directory are also accepted.

to disable logging capturation:

```
$ nosetests --nologcapture
```

Configuration for `nosetests`: in `~/.noserc`

```
[nosetests]
verbosity=3
with-doctest=1
```

#### generate coverage

first install `coverage` module

```
$ nosetests --nologcapture --with-coverage
```

Generating html coverate report file

```
$ nosetests --nologcapture --with-coverage --cover-html
```
http://nose.readthedocs.io/en/latest/plugins/cover.html

## py.test

## mock


## Ref

* [Testing Your Code](http://docs.python-guide.org/en/latest/writing/tests/)
* [testing with nose](http://nose.readthedocs.io/en/latest/testing.html)
* [nose introduction](http://pythontesting.net/framework/nose/nose-introduction/#no_boilerplate)
* [Improve Your Python: Understanding Unit Testing](https://jeffknupp.com/blog/2013/12/09/improve-your-python-understanding-unit-testing/)
