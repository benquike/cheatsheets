class ASTNode(object):
    def __init__(self, times):
        self.times = times
        self.subNodes = []

    def decode(self):
        s = ''
        for n in self.subNodes:
            s = s + n.decode()
        return s * self.times

class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stk
