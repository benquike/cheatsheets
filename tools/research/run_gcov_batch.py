#!/usr/bin/env python

import sys
import os
import subprocess

def main():
    if len(sys.argv) != 3:
        print "Usage: run_gcov_batch.py <bin_path> <dir_to_input>"
        sys.exit(-1)

    bin_path = os.path.abspath(sys.argv[1])
    input_dir = os.path.abspath(sys.argv[2])

    for i in os.listdir(input_dir):
        if i == '.' or i == '..':
            continue

        print "running " + bin_path + " < " + os.path.join(input_dir, i)
        env = os.environ.copy()
        env["GDB_AUTO_EXEC"] = "1"
        env["GDB_BIN_FILE"]  = bin_path
        env["GDB_INPUT_FILE"] = os.path.join(input_dir, i)
        subprocess.call(["gdb"], env=env)

if __name__ == '__main__':
    main()
