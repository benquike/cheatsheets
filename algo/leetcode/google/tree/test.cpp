/*******************************************************
 * Copyright (C) 2016 Hui Peng <peng124@purdue.edu>
 *
 * This file is part of project.
 *
 * The source files from project can not be copied and/or
 * distributed without the express permission of Hui Peng
 *******************************************************/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "tree.h"

btnode *build_node(int val, btnode *left, btnode *right) {
  btnode *node = (btnode*) malloc(sizeof(btnode));
    if (node == NULL)
    return node;

  memset(node, 0, sizeof(btnode));
  node->val = val;
  node->left = left;
  node->right = right;

  return node;
}


btnode *build_tree() {
  btnode* n8 = build_node(8, NULL, NULL);
  btnode* n9 = build_node(9, NULL, NULL);
  btnode* n10 = build_node(10, NULL, NULL);
  btnode* n11 = build_node(11, NULL, NULL);
  btnode* n12 = build_node(12, NULL, NULL);
  btnode* n13 = build_node(13, NULL, NULL);


  btnode* n4 = build_node(4, n8, n9);
  btnode* n5 = build_node(5, n10, n11);
  btnode* n6 = build_node(6, NULL, n12);
  btnode* n7 = build_node(7, NULL, n13);

  btnode* n2 = build_node(2, n4, n5);
  btnode* n3 = build_node(3, n6, n7);

  btnode* n1 = build_node(1, n2, n3);


  return n1;
}


void free_tree(btnode *root) {
  if (root == NULL) return;

  free_tree(root->left);
  free_tree(root->right);

  free(root);
}


extern void preorder_non_rec(btnode *root);
extern void preorder_rec(btnode *root);
extern void inorder_non_rec(btnode *root);
extern void inorder_rec(btnode *root);
extern void postorder_non_rec(btnode *root);
extern void postorder_rec(btnode *root);

int main() {

  btnode *root = build_tree();
  printf("preorder nonrecursive\n");
  preorder_non_rec(root);
  printf("========================\n");
  printf("preorder recursive\n");
  preorder_rec(root);
  printf("\n");
  printf("========================\n");

  printf("inorder nonrecursive\n");
  inorder_non_rec(root);
  printf("========================\n");
  printf("inorder recursive\n");
  inorder_rec(root);
  printf("\n");
  printf("========================\n");

  printf("postorder nonrecursive\n");
  postorder_non_rec(root);
  printf("========================\n");
  printf("postorder recursive\n");
  postorder_rec(root);
  printf("\n");
  printf("========================\n");


  free_tree(root);
  return 0;
}
