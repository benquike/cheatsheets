# regular expression

There are 3 flavors of regular expression:
* POSIX BRE
* POSIX ERE
* PCRE

Others
* Emacs regular expression

## BRE

Meta characters:

| meta char  |                            Description                                                               |
|------------|------------------------------------------------------------------------------------------------------|
|    `.`     | Match any char excluding new line                                                                    |
|  `[  ]`    | matches a single char in the bracket                                                                 |
|  `[^ ]`    | Match any char that is not included in the bracket                                                   |
|   `^`      | matches beginning position of line                                                                   |
|   `$`      | matches ending position of line                                                                      |
|  `( )`     | defines a group which can be referred using `\n`                                                     |
|  `\n`      | Back reference a group defined using `()`, `n` can be 1-9                                            |
|   `*`      | Matches the preceding element (char, group or anything enclosed in `[ ]`) or group 0 or more times   |
|  `{m,n}`   | Matches the preceding element m-n times inclusive                                                    |

`(`, `)`, `{`, and `}` need to be escaped by preceding them with `\`, or they will
be treated as literals, others do not need to.

E.g.:

| regexp     |     Description                                               |
|------------|---------------------------------------------------------------|
| `(a)*`     | `(a`, `(a)` `(a))` `(a)))`                                    |
| `\(a\)*`   | ``, `a`, `aa`, `aaa`, `aaaa`                                  |
| `a{3,5}`   | `a{3,5}`                                                      |
|`a\{3,5\}`  | `aaa`, `aaaa`, `aaaaa`                                        |

## ERE

ERE adds 3 more meta chars `?`, `+`, and `|`.

And `(`, `)`, `{`, and `}` should not be escaped when they are used as meta char.

In addition, a lot of useful character classes are added. but POSIX character classes
can only be used within bracket expressions.

## PCRE

Features added:
* lazy regexps
* backtracking
* capture group
* recrusive patterns


## Application

### grep

Grep supports all of the 3 flavors of regexps. they can be switched by `-E`, `-P`
and `-P` options, by default, `-P` is used.
