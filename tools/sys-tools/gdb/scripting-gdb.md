# Scripting GDB

## command

Starting GDB, run `python-interactive` or `python` command

## scripting

### Important APIs[^1]

- `gdb.execute`
  This API can be used to execute a gdb command.
  Using this API, we can get the result of a command by setting `to_string` as `True`.
  After this, the result of the command will be returned as a string
  ```
      num = gdb.execute("x/s " + addr_str, to_string=True)
  ```

- `gdb.breakpoints`

    Get all the `Breakpoint` object.
    Using a `Breakpoint` object, we can manipulate it.

- `gdb.parse_and_eval`

    Given an expression, it returns the `Value` object. Using this object,
    we can extract its values in various form.

### Subclassing Breakpoint class

A subclass of `Breakpoint` can customize the behavior of it.
We can do something when a breakpoint is intercept and decide
whether continuing exeuction or stopping.

The customization is done in the `stop` method. We can return `True`
to let the execution continue.

More reference is [here](./gdb_python.pdf) and here[^2] and here[^3].



[^1]: https://sourceware.org/gdb/onlinedocs/gdb/Python-API.html#Python-API
[^2]: [Using Python to debug C and C++ programs](https://dmalcolm.fedorapeople.org/presentations/PyCon-US-2011/GdbPythonPresentation/GdbPython.html)
[^3]: [PythonGdbTutorial](https://sourceware.org/gdb/wiki/PythonGdbTutorial)



## cool tools

GEF: https://github.com/hugsy/gef
PwnGDB:https://github.com/pwndbg/pwndbg && https://blahcat.github.io/tutorials/
PEDA: https://github.com/longld/peda