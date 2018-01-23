/*******************************************************
 * Copyright (C) 2016 Hui Peng <peng124@purdue.edu>
 *
 * This file is part of project.
 *
 * The source files from project can not be copied and/or
 * distributed without the express permission of Hui Peng
 *******************************************************/

#ifndef TREE_H
#define TREE_H

typedef struct btnode {
  int val;
  struct btnode *left;
  struct btnode *right;
} btnode;

#endif /* TREE_H */
