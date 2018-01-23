class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        ret = ''
        if self.left == None:
            ret = ret + 'null,'
        else:
            ret = ret + str(self.left)
        ret = ret + str(self.val) + ','
        if self.right == None:
            ret = ret + 'null,'
        else:
            ret = ret + str(self.right)

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """

        def gen(start, end):
            if start > end:
                return [None]
            if start == end:
                return [TreeNode(start)]

            ret = []
            for i in range(start, end+1):
                ls = gen(start, i - 1)
                rs = gen(i+1, end)

                for l in ls:
                    for r in rs:
                        root = TreeNode(i)
                        root.left = l
                        root.right = r
                        ret.append(root)
            return ret

        return gen(1, n)

if __name__ == '__main__':
    s = Solution()
    print str(s.generateTrees(3))
