https://github.com/dariubs/GoBooks
http://www.golang-book.com/


# tagging

we can add some extra info to fields of structs in golang using ```.
And these tags can be retrieved using  reflection.

Example:

```
type User struct {
    Name string `json:"name" xml:"name"`
}
```

https://stackoverflow.com/questions/30681054/what-is-the-usage-of-backtick-in-golang-structs-definition


# ... operator in go lang

1. Variadic arguments
2. passing variadic arguments
3. array literals
4. wildcard in `go get command`

https://programming.guide/go/three-dots-ellipsis.html