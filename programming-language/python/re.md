# re module

## name a match

`(?P<name>xxxx)`

## Get a dict of mapping

```
m.groupdict()
```

## non-greedy match

The `*`, `+`, and `?` qualifiers are all greedy; they match as much text as possible. 
Sometimes this behaviour isn’t desired; to make them non-greedy, append a `?` mark to
them.
