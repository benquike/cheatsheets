# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
            
class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        def cvt(root, addend):
            if root == None:
                return addend, None
    
            rt = TreeNode(root.val)

            rt.val = rt.val + addend

            lr, right = cvt(root.right, addend)

            if right != None:
                rt.val = rt.val + lr
            
            ll, left = cvt(root.left, rt.val)
        
            rt.left = left
            rt.right = right
            # print 'rt: ' + str(rt.val)
            return ll, rt
                
        return cvt(root, 0)

if __name__ == "__main__":
    t = TreeNode(0)
    t.left = TreeNode(-4)
    t.right = TreeNode(2)
    t.right.left = TreeNode(1)
    t.right.right = TreeNode(3)

    s = Solution()
    s.convertBST(t)
