# debian build system

## build a debian package from source

```
apt-get source <pkg-name>
debuild
```

## extract a deb file

```
mkdir ~/temp
pkg -x somepackage.deb ~/temp/
```

[Reference](./packaging-tutorial.en.pdf)
