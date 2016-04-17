# filesystem APIs

## readlink
read the content of a symbolic link

```
ssize_t readlink(const char *pathname, char *buf, size_t bufsiz);
```

The command line utility `readlink` is implementetd using this API.

## realpath
Given an path that contains relative names in it, resolve it to absolute
path.

```
char *realpath(const char *path, char *resolved_path);
```

Unix utility `realpath` is implemented using this API, similar tools include
`dirname`, `basename`.
