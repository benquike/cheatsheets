class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        
        if root == None:
            return None
        if p == q:
            return p;
        
        def __lca(r, p, q, res):
            # neither p nor q is in root
            if r == None:
                return 0
                
            left = __lca(r.left, p, q, res)
            right = __lca(r.right, p, q, res)
            
            if left == 0 and right == 0 and r != p and r != q:
                return 0
            
            # either p or q is in root
            # one of p,q is in the left
            # one of p,q is in the right
            # one of p,q is root
            if left == 0 and right == 0 and (p == r or q == r):
                return 1
            if left + right == 1 and p != r and q != r:
                return 1
            
            # both p and q are in root
            # p and q both in left
            # p and q both in right
            # one is r, the other is in left
            # one is r, the other is in right
            
            if left == 2 or right == 2:
                return 2
            if left == 1 and right == 1:
                res[0] = r
                return 2
            if (p == r or q == r) and (left == 1 or right == 1):
                res[0] = r
                return 2
        ret = [None]
        __lca(root, p, q, ret)
        
        return ret[0]

if __name__ == '__main__':
    s = Solution()
    n1 = TreeNode(2)
    n2 = TreeNode(1)
    n1.right = n2

    x = s.lowestCommonAncestor(n1, n1, n2)
    print x.val
