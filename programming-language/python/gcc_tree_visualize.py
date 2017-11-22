import os
import argparse
from graphviz import Digraph

def parse_tree_dump_file(tree_dump_file):
    pass

def main():
	parser = argparse.ArgumentParser(description="A tool for visualizing the TREE structure of GCC")
	parser.add_argument("--tree_dump", required=True, help="the tree dump file from GCC by 'gcc -fdump-tree-all xxx.c'")

	args = parser.parse_args()

	tree_dump_file = os.path.abspath(args.tree_dump)
	

if __name__ == '__main__':
    main()
