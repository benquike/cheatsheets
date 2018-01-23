/*******************************************************
 * Copyright (C) 2016 Hui Peng <peng124@purdue.edu>
 *
 * This file is part of project.
 *
 * The source files from project can not be copied and/or
 * distributed without the express permission of Hui Peng
 *******************************************************/

#include <stdio.h>
#include <stack>
#include "tree.h"

void inorder_non_rec(btnode *root) {
  std::stack<btnode*> s;
  btnode *t1 = root, *t2;

  while (t1 != NULL || !s.empty()) {
    t2 = t1;

    while (t2 != NULL) {
      s.push(t2);
      t2 = t2->left;
    }

    t1 = s.top();
    s.pop();
    printf("%d ", t1->val);
    t1 = t1->right;
  }

  printf("\n");
}

void inorder_rec(btnode *root) {
  if (root == NULL)
    return;

  inorder_rec(root->left);
  printf("%d ", root->val);
  inorder_rec(root->right);
}
