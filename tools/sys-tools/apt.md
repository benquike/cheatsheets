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

2. install the dependencies

    apt-get build-dep <pkg_name>

3. goto the source directory, `dpkg-buildpackage`command will build the deb file for us and put it
in the parent directory.


## get the available packages

`apt-cache` can be use to do the query[^4].

1. Get all the available packages

    apt-cache dumpavail

2. get the dependency of a package[^5]

    apt-cache showsrc <pkg_name>

## show detailed info about a package

`dpkg -s <pkg_name>`

## meta package

a meta package is a package that does not contain important stuff itself, but
it depends on some other packages so that when you install that package, the dependent
packages are all installed[^7].

## apt-cache

apt-cache creates a repository of information about the
packages that are avaiable from your sources list, so this
way you can search packages and information about it.
commands are as follows

| command               | desc                                                   |
|-----------------------|--------------------------------------------------------|
| apt-cache add         | Adds a package file to the source cache.               |
| apt-cache gencaches   | Builds both the package and source cache               |
| apt-cache showpkg     | Show some general information for a single package     |
| apt-cache stats       | Show some basic statistics                             |
| apt-cache dump        | Show the entire file in a terse form                   |
| apt-cache dumpavail   | Print an available file to stdout                      |
| apt-cache unmet       | Show unmet dependencies                                |
| apt-cache check       | Check the cache a bit                                  |
| apt-cache search      | Search the package list for a regex pattern            |
| apt-cache show        | Show a readable record for the package                 |
| apt-cache depends     | Show raw dependency information for a package          |
| apt-cache pkgnames    | List the names of all packages                         |
| apt-cache dotty       | Generate package graphs for GraphVis                   |


## customization

1. When installing a package, always answer yes[^6]

    apt-get --yes (-y) install <pkg_name>

[^1]:

http://www.claudiokuenzler.com/blog/611/installing-cmake-3.4.1-ubuntu-14.04-trusty-using-alternatives#.V7-nDN9vGV4

[^2]: http://askubuntu.com/questions/28372/how-do-i-get-and-modify-the-source-code-of-packages-installed-through-apt-get

[^3]: http://www.cyberciti.biz/ref/apt-dpkg-ref.html

[^4]: http://askubuntu.com/questions/531403/how-to-download-all-repository-using-apt-get

[^5]: http://askubuntu.com/questions/180504/how-can-i-remove-all-build-dependencies-for-a-particular-package

[^6]: http://superuser.com/questions/164553/automatically-answer-yes-when-using-apt-get-install

[^7]: https://help.ubuntu.com/community/MetaPackages
