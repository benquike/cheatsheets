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


