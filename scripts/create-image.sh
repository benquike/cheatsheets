#!/bin/bash
# Copyright 2016 syzkaller project authors. All rights reserved.
# Use of this source code is governed by Apache 2 LICENSE that can be found in the LICENSE file.

# create-image.sh creates a minimal Debian Linux image suitable for qemu testing, default, wheezy is used.

set -eux

distname=stretch
host_name=qemu_test_vm

sudo rm -rf ${distname}
mkdir -p ${distname}
sudo debootstrap --include=openssh-server,curl,tar,gcc,libc6-dev,time,strace,sudo,less,psmisc,selinux-utils,policycoreutils,checkpolicy,selinux-policy-default ${distname} ${distname}

# Set some defaults and enable promtless ssh to the machine for root.
sudo sed -i '/^root/ { s/:x:/::/ }' ${distname}/etc/passwd
echo 'T0:23:respawn:/sbin/getty -L ttyS0 115200 vt100' | sudo tee -a ${distname}/etc/inittab
printf '\nauto eth0\niface eth0 inet dhcp\n' | sudo tee -a ${distname}/etc/network/interfaces
echo 'debugfs /sys/kernel/debug debugfs defaults 0 0' | sudo tee -a ${distname}/etc/fstab
echo "kernel.printk = 7 4 1 3" | sudo tee -a ${distname}/etc/sysctl.conf
echo 'debug.exception-trace = 0' | sudo tee -a ${distname}/etc/sysctl.conf
echo "net.core.bpf_jit_enable = 1" | sudo tee -a ${distname}/etc/sysctl.conf
echo "net.core.bpf_jit_harden = 2" | sudo tee -a ${distname}/etc/sysctl.conf
echo "net.ipv4.ping_group_range = 0 65535" | sudo tee -a ${distname}/etc/sysctl.conf
echo -en "127.0.0.1\tlocalhost\n" | sudo tee ${distname}/etc/hosts
echo "nameserver 8.8.8.8" | sudo tee -a ${distname}/etc/resolve.conf
echo "${host_name}" | sudo tee ${distname}/etc/hostname
sudo mkdir -p ${distname}/root/.ssh/
rm -rf ssh
mkdir -p ssh
ssh-keygen -f ssh/id_rsa -t rsa -N ''
cat ssh/id_rsa.pub | sudo tee ${distname}/root/.ssh/authorized_keys

# Build a disk image
dd if=/dev/zero of=${distname}.img bs=1M seek=2047 count=1
sudo mkfs.ext4 -F ${distname}.img
sudo mkdir -p /mnt/${distname}
sudo mount -o loop ${distname}.img /mnt/${distname}
sudo cp -a ${distname}/. /mnt/${distname}/.
sudo umount /mnt/${distname}
