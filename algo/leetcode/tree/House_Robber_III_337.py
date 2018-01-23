#!/usr/bin/env python

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        # def __rob_n(root, r):
        #     if root == None:
        #         return 0

        #     if r 
