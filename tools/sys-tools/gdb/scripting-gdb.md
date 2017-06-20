# Scripting GDB

## command

Starting GDB, run `python-interactive` or `python` command

## scripting

Important APIs[^1]

- ` gdb.execute`
  This API can be used to execute a gdb command.
  Using this API, we can get the result of a command by setting `to_string` as `True`.
  After this, the result of the command will be returned as a string
  ```
      num = gdb.execute("x/s " + addr_str, to_string=True)
  ```

More reference is [here](./gdb_python.pdf) and here[^2] and here[^3]

[^1]: https://sourceware.org/gdb/onlinedocs/gdb/Python-API.html#Python-API
[^2]: [Using Python to debug C and C++ programs](https://dmalcolm.fedorapeople.org/presentations/PyCon-US-2011/GdbPythonPresentation/GdbPython.html)
[^3]: [PythonGdbTutorial](https://sourceware.org/gdb/wiki/PythonGdbTutorial)
