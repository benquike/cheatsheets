# curl usage

## Providing credentials

Sometimes the server requires you to provide some credentials
to access some web site. To provide credentials, we have 2 options:

    curl http://some.site --user username:password

or you can save the username password in the ~/.netrc like this:

    machine some.machine
    login username
    password password
    protocol https

