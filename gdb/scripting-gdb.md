# Scripting GDB

## command

Starting GDB, run `python-interactive` pr `python` command

## scripting

Important APIs[^1]

- ` gdb.execute`
  This API can be used to execute a gdb command.
  Using this API, we can get the result of a command by setting `to_string` as `True`.
  After this, the result of the command will be returned as a string
  ```
      num = gdb.execute("x/s " + addr_str, to_string=True)
  ```


[^1]: https://sourceware.org/gdb/onlinedocs/gdb/Python-API.html#Python-API
