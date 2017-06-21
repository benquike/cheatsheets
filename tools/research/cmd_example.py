import os
import gdb
import sys

if not ('GDB_AUTO_EXEC' in os.environ and 'GDB_BIN_FILE' in os.environ and 'GDB_INPUT_FILE' in os.environ):
    sys.exit(0)

def write_memory(addr, val):
    '''
    Write val to addr using only one byte
    '''

    # print "writing " + str(val) +  " to " +hex(addr)
    cmd = "set {unsigned char} " + hex(addr) + " = " + str(val)

def read_memory(addr):
    '''
    Read one byte from addr
    '''
    cmd = 'x /1ub ' + hex(addr)
    ret = gdb.execute(cmd, to_string=True)
    # print "ret|" + ret 
    byte = int(ret.strip().split()[1])
    return byte

class LLVMGCDAFileStartBp(gdb.Breakpoint):
    def __init__(self):
        super(LLVMGCDAFileStartBp, self).__init__("GCDAProfiling.c:204")

    def stop(self):
        write_buffer = gdb.parse_and_eval("write_buffer")
        filename = gdb.parse_and_eval("filename")
        gcda_filename = filename.string()

        if not os.path.exists(gcda_filename):
            return False

        f = open(gcda_filename, "rb")
        c = f.read()
        base_addr = long(write_buffer)
        for i in range(len(c)):
            write_memory(base_addr + i, ord(c[i]))

        return False

class LLVMGCDAFileEndBp(gdb.Breakpoint):
    def __init__(self):
        super(LLVMGCDAFileEndBp, self).__init__("llvm_gcda_end_file")
        # super(LLVMGCDAFileEndBp, self).__init__("lib/GCDAProfiling.c:331")

    def stop(self):
        filename = gdb.parse_and_eval("filename")
        write_buffer = gdb.parse_and_eval("write_buffer")
        cur_pos = gdb.parse_and_eval("cur_pos")

        # print "value of filename:" + filename.string()
        # print "value of write_buffer=====:" + write_buffer.address
        # print "value of cur_pos:" + str(cur_pos)
        gcda_filename = filename.string()
        try:
            os.makedirs(os.path.dirname(gcda_filename))
        except OSError:
            pass

        size = long(cur_pos)
        base_addr = long(write_buffer)
        # print "size:" + hex(size)
        # print "base_addr:" + str(base_addr)

        with open(gcda_filename, 'wb') as f:
            for i in range(size):
                b = read_memory(base_addr + i)
                f.write(chr(b))

        return False

if 'GDB_BIN_FILE' in os.environ:
    gdb.execute('file ' + os.environ['GDB_BIN_FILE'])

LLVMGCDAFileStartBp()
LLVMGCDAFileEndBp()

if 'GDB_AUTO_EXEC' in os.environ and 'GDB_INPUT_FILE' in os.environ:
    gdb.execute("run < " + os.environ['GDB_INPUT_FILE'])
    gdb.execute("quit")
