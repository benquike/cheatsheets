# libvirt



# virsh


## creating vm

```
virt-install \
   --connect qemu:///system \
   --virt-type kvm \
   --name rhel5 \
   --ram 512 \
   --disk path=/var/lib/libvirt/images/rhel5.img,size=8 \
   --extra-args "ks=http://172.16.0.1/class.cfg  console=ttyS0  serial" \
   --graphics vnc \
   --cdrom /tmp/boot.iso \
   --os-variant rhel5
```

## Ref
https://unix.stackexchange.com/questions/309788/how-to-create-a-vm-from-scratch-with-virsh
http://rabexc.org/posts/how-to-get-started-with-libvirt-on
https://help.ubuntu.com/community/KVM/Virsh
http://blog.vmsplice.net/2011/03/how-to-access-qemu-monitor-through.html
