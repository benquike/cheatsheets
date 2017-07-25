# re module

## name a match

`(?P<name>xxxx)`

## backreferencing a group

`(?P=name)`

## others

`(?#...)`: a comment
`(?=...)`: Matches if `...` matches next, but doesn’t consume any of the string.
    This is called a lookahead assertion. For example, Isaac (?=Asimov) will
    match 'Isaac ' only if it’s followed by 'Asimov'.

`(?!...)`: Matches if `...` does not match next. This is a negative lookahead assertion. For example,
    `Isaac (?!Asimov)` will match 'Isaac ' only if it’s not followed by 'Asimov'.


## Get a dict of mapping

```
m.groupdict()
```

## non-greedy match

The `*`, `+`, and `?` qualifiers are all greedy; they match as much text as possible. 
Sometimes this behaviour isn’t desired; to make them non-greedy, append a `?` mark to
them.
