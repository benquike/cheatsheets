class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        lp = len(p)
        ls = len(s)

        if 0 == lp and 0 == ls:
            return True
        if lp == 0 and ls != 0:
            return False

        # if (0 == lp and 0 != ls) or (0 != lp and 0 == ls):
        #     return False

        ## lp > 0 and ls > 0

        ## lp == 1
        if 1 == lp:
            if 1 != ls:
                return False
            if p[0] == s[0] or p[0] == '.':
                return True
            return False

        # lp > 1
        if p[0] != '.' and p[1] != '*':
            if p[0] != s[0]:
                return False
            else:
                return self.isMatch(s[1:], p[1:])

        if p[0] == '.' and p[1] != '*':
            if ls == 0:
                return False
            return self.isMatch(s[1:], p[1:])

        for k in range(0, ls + 1):
            print 'try ' + k*p[0] + p[2:]
            if self.isMatch(s, k*p[0] + p[2:]):
                return True

        return False

if __name__ == '__main__':
    s = Solution()
    if s.isMatch('', '.a*'):
        print 'Match'
    else:
        print 'UnMatch'
