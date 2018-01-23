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


void preorder_non_rec(btnode *root) {
  std::stack<btnode*> s;
  btnode *t1 = root, *t2;

  while (t1 != NULL || !s.empty()) {

    t2 = t1;

    while (t2 != NULL) {
      printf("%d ", t2->val);
      s.push(t2);
      t2 = t2 -> left;
    }

    t1 = s.top();
    t1 = t1->right;
    s.pop();
  }

  printf("\n");
}

void preorder_rec(btnode *root) {
  if (root == NULL) {
    // printf("\n");
    return;
  }

  printf("%d ", root->val);

  preorder_rec(root->left);
  preorder_rec(root->right);
}
