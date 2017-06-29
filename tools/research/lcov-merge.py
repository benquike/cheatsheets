#!/usr/bin/env python

import sys
import os
import subprocess

import argparse

def main():
    parser = argparse.ArgumentParser(usage="A tool for merging all lcov info files in a directory in batch")
    parser.add_argument("--data_dir", required=True, help="The directory containing .info files")
    parser.add_argument("--out", required=True, help="The output file name")

    args = parser.parse_args()

    first = True
    for i in os.listdir(args.data_dir):
        if not i.endswith('.info'):
            continue
        if first:
            subprocess.call(['cp', os.path.join(args.data_dir, i), args.out])
            first = False
        else:
            subprocess.call(['lcov', '-a',
                             os.path.join(args.data_dir, i),
                             '-a', args.out, '-o', args.out])

if __name__ == '__main__':
    main()
