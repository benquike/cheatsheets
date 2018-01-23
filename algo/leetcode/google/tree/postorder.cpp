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


void postorder_non_rec(btnode *root) {
  std::stack<btnode*> s;
  btnode *t1 = root;

  do {

    while (t1 != NULL) {
      if (t1->right != NULL)
        s.push(t1->right);
      s.push(t1);

      t1 = t1 -> left;
    }

    t1 = s.top();
    s.pop();

    if (!s.empty() && (t1->right == s.top())) {
      // right child not visited yet
      s.pop();
      s.push(t1);
      t1 = t1 -> right;
    } else {
      // right child visited
      printf("%d ", t1->val);
      t1 = NULL;
    }
  } while (!s.empty());

  printf("\n");
}

void postorder_rec(btnode *root) {
  if (root == NULL) {
    // printf("\n");
    return;
  }

  postorder_rec(root->left);
  postorder_rec(root->right);
  printf("%d ", root->val);
}
