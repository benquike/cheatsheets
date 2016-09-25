# Modules

## Add a directory to the source search list
1. Add it to environmental variable `PYTHONPATH`
2. Add the path to the `sys.path` using the `append` method in the code

## reload a module when it is modified

   reload(<package_name>)

You can also use `is_changed` to detect whether a package was modified
or not[^1].



[^1]: http://stackoverflow.com/questions/437589/how-do-i-unload-reload-a-python-module