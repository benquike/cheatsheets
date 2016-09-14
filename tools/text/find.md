# find usage

find is a tool which can be used to find files/directories recursively.

## execute command on files found

    find . -executable -exec command {} \;

or

    find . -executable -exec command {} +

find will replace `{}` with the file name that matches the querying
criterion and execute the command for you.

If `\;` is appended to the command, the command will be executed
on eachn file once. if `+` is used, all matched files will be passed
to the command and the command will be executed only once.
