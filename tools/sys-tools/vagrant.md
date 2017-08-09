# vagrant usage

## initialization

    vagrant init

This command will create a file named `Vagrantfile` in which all the
available configuration are commented out.

## download os image

    vagrant box add ubuntu/xenial64

After this, modfify `Vagrantfile` replacing `config.vm.box = "hashicorp/precise64"`

## delete os image

    vagrant box remove

## run guest

    vagrant up

## stop the guest

    vagrant destroy


## login the guest

    vagrant ssh


## logout the guest

    Ctrl-D


## build a vagrant box


## share a host directory with the guest system

```
Vagrant.configure("2") do |config|
  # other config here

  config.vm.synced_folder "src/", "/srv/website"
  end
  ```

The first parameter is a path to a directory on the host machine.
If the path is relative, it is relative to the project root. The
second parameter must be an absolute path of where to share the
folder within the guest machine. This folder will be created
(recursively, if it must) if it does not exist.


https://www.vagrantup.com/docs/synced-folders/basic_usage.html
