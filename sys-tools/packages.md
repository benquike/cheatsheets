# packages to install


```
sudo apt-get install -y git curl build-essential libpython-dev python-pip python-virtualenv
sudo apt-get install -y zsh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
sudo pip install virtualenvwrapper
echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.zshrc

sudo apt-get install nfs-common
sudo apt-get install -y emacs vim
sudo apt-get install libffi-dev
sudo apt-get install libtool-bin
sudo apt-get install build-essential gcc-multilib libtool automake autoconf bison debootstrap debian-archive-keyring
sudo apt-get build-dep qemu
pip install driller
pip install git+https://github.com/angr/tracer.git

```


## PAC


Install

Add

```
deb http://archive.getdeb.net/ubuntu <disto-name>-getdeb apps
```

To sources.list

```
sudo apt-get update
```
If it complains key issue, fix it using the following section.

Then


```
sudo apt-get install pac
```

## solving key issues

Fix apt-get update “the following signatures couldn’t be verified because the public key is not available”

```
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys <KEY>
```

https://chrisjean.com/fix-apt-get-update-the-following-signatures-couldnt-be-verified-because-the-public-key-is-not-available/
