# class Solution(object):
#     def calculate(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """

#         if s.find('+') == -1 and s.find('-') == -1 and s.find('(') == -1:
#             return int(s)

#         def isNum(c):
#             if ord(c) >= ord('0') and ord(c) <= ord('9'):
#                 return True
#             return False


#         def findClosingPos(s, i):
#             assert s[i] == '('
#             stk = ['(']

#             for j in range(i+1, len(s)):
#                 if s[j] == '(':
#                     stk.append('(')
#                 elif s[j] == ')':
#                     if len(stk) == 1:
#                         return j
#                     else:
#                         if len(stk) == 0:
#                             return -1
#                         stk.pop()

#             return -1

#         def comp(op, n1, n2):
#             if op == '+':
#                 return n1 + n2
#             if op == '-':
#                 return n1 - n2

#         i = 0
#         ret = None
#         c_op = None
#         while i < len(s):
#             if s[i] == '(':
#                 closing = findClosingPos(s, i)
#                 if c_op == None:
#                     ret = self.calculate(s[i+1:closing])
#                 else:
#                     ret = comp(c_op, ret, self.calculate(s[i+1:closing]))
#                 i = closing + 1
#                 continue

#             if isNum(s[i]):
#                 j = i + 1
#                 while j < len(s) and isNum(s[j]):
#                     j = j + 1
#                 t = int(s[i:j])
#                 if c_op == None:
#                     ret = t
#                 else:
#                     ret = comp(c_op, ret, t)
#                 i = j
#                 continue
#             if s[i] == '+' or s[i] == '-':
#                 c_op = s[i]
#                 i = i + 1
#                 continue
#             i = i + 1
#         return ret


class Node(object):
    def __init__(self, node_t = 0):
        self.node_t = node_t
        self.node_val = 0
        self.left = None
        self.right = None

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """

        if s.find('+') == -1 and s.find('-') == -1 and s.find('(') == -1:
            return int(s)

        def isNum(c):
            if ord(c) >= ord('0') and ord(c) <= ord('9'):
                return True
            return False


        def comp(op, n1, n2):
            if op == '+':
                return n1 + n2
            if op == '-':
                return n1 - n2


if __name__ == '__main__':
    s = Solution()
    print s.calculate('((1 + 2) - 3) - 4')
