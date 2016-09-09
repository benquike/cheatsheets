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


## build the package from source by yourself

1. get the source package

    apt-get source <package_name>

This command will download the source of the package[^2][^3] and put the tarball in the current
directory, extract the source files in the source directory.

2. goto the source directory, `dpkg-buildpackage`command will build the deb file for us and put it
in the parent directory.


## get the available packages

`apt-cache` can be use to do the query[^4].

[^1]:

http://www.claudiokuenzler.com/blog/611/installing-cmake-3.4.1-ubuntu-14.04-trusty-using-alternatives#.V7-nDN9vGV4

[^2]: http://askubuntu.com/questions/28372/how-do-i-get-and-modify-the-source-code-of-packages-installed-through-apt-get

[^3]: http://www.cyberciti.biz/ref/apt-dpkg-ref.html

[^4]: http://askubuntu.com/questions/531403/how-to-download-all-repository-using-apt-get
