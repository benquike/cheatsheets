#!/usr/bin/env python

import sys
import os
import subprocess

import argparse

def main():

    parser = argparse.ArgumentParser(usage="A tool for running gcov in batch")
    parser.add_argument("--bin_path", required=True, help="The path to the binary to run")
    parser.add_argument("--input_dir", required=True, help="The directory containing all the inputs")
    parser.add_argument("--timeout",  type=int, default=5, help="The directory containing all the inputs")
    parser.add_argument("--cov_dir", help="The directory to put the coverage info files")

    args = parser.parse_args()

    bin_path  = os.path.abspath(args.bin_path)
    # here we assume that the executable binary resides
    # in the bin directory of the challenge
    bin_root_dir = os.path.join(os.path.dirname(bin_path), '..')
    bin_filename = os.path.basename(bin_path)
    input_dir = os.path.abspath(args.input_dir)
    cov_dir   = os.path.abspath(args.cov_dir) if args.cov_dir is not None else "lcov-" + bin_filename

    if not os.path.exists(cov_dir):
        os.makedirs(cov_dir)

    for i in os.listdir(input_dir):
        if not i.startswith("id:"):
            continue

        print "running " + bin_path + " < " + os.path.join(input_dir, i)
        env = os.environ.copy()
        env["GDB_AUTO_EXEC"] = "1"
        env["GDB_BIN_FILE"]  = bin_path
        env["GDB_INPUT_FILE"] = os.path.join(input_dir, i)
        null_fd = open("/dev/null", "wb")
        # collect the coverage info
        subprocess.call(["gdb"], env=env, stdout=null_fd, stderr=null_fd, timeout=args.timeout)
        # generate lcov info
        subprocess.call(['lcov', '-c', '--directory', bin_root_dir,
                         '--output-file', os.path.join(cov_dir, i + '.info')],
                        stdout=null_fd, stderr=null_fd)

if __name__ == '__main__':
    main()
