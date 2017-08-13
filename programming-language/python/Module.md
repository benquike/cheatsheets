# Modules

## Add a directory to the source search list
1. Add it to environmental variable `PYTHONPATH`
2. Add the path to the `sys.path` using the `append` method in the code

## reload a module when it is modified

   reload(<package_name>)

You can also use `is_changed` to detect whether a package was modified
or not[^1].


## debugging module loading

Start the python interpreter with `-v`:

```
$ python -v -m /usr/lib/python2.6/timeit.py
# installing zipimport hook
import zipimport # builtin
# installed zipimport hook
# /usr/lib/python2.6/site.pyc matches /usr/lib/python2.6/site.py
import site # precompiled from /usr/lib/python2.6/site.pyc
# /usr/lib/python2.6/os.pyc matches /usr/lib/python2.6/os.py
import os # precompiled from /usr/lib/python2.6/os.pyc
import errno # builtin
import posix # builtin
# /usr/lib/python2.6/posixpath.pyc matches /usr/lib/python2.6/posixpath.py
import posixpath # precompiled from /usr/lib/python2.6/posixpath.pyc
# /usr/lib/python2.6/stat.pyc matches /usr/lib/python2.6/stat.py
import stat # precompiled from /usr/lib/python2.6/stat.pyc
# /usr/lib/python2.6/genericpath.pyc matches /usr/lib/python2.6/genericpath.py
import genericpath # precompiled from /usr/lib/python2.6/genericpath.pyc
# /usr/lib/python2.6/warnings.pyc matches /usr/lib/python2.6/warnings.py
import warnings # precompiled from /usr/lib/python2.6/warnings.pyc
# /usr/lib/python2.6/linecache.pyc matches /usr/lib/python2.6/linecache.py
import linecache # precompiled from /usr/lib/python2.6/linecache.pyc
# /usr/lib/python2.6/types.pyc matches /usr/lib/python2.6/types.py
import types # precompiled from /usr/lib/python2.6/types.pyc
# /usr/lib/python2.6/UserDict.pyc matches /usr/lib/python2.6/UserDict.py
...
```

[^1]: http://stackoverflow.com/questions/437589/how-do-i-unload-reload-a-python-module
