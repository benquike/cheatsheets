# apt usage

## install

    apt-get install package name

## query all files related to a package

    dpkg -L <package_name>

## search packages

    apt-cache search name

## uninstall
`apt-get remove package` will remove the binary, but the config files are still there.
`apt-get purge package` will remove all files related to the package, including config files.
