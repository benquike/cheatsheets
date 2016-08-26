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

## replace the apt-managed version with source compiled version

    update-alvernatives

for example, you have compiled a version of cmake and want to replace apt-managed version
of cmake with the one you compiled, you can use the following command[^1].


    update-alternatives --install /usr/bin/cmake cmake /usr/local/bin/cmake 1 --force

[^1]: http://www.claudiokuenzler.com/blog/611/installing-cmake-3.4.1-ubuntu-14.04-trusty-using-alternatives#.V7-nDN9vGV4
