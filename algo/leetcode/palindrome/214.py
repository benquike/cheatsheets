class Solution(object):
    def shortestPalindrome(self, t):
        """
        :type s: str
        :rtype: str
        """

        lt = len(t)
        next = []
        for i in range(lt):
            next.append(0)

        for i in range(1, lt):
            j = next[i - 1]
            while j > 0 and t[i] != t[j]:
                j = next[j - 1]

            if j == 0:
                if t[0] == t[i]:
                    next[i] = 1
                else:
                    next[i] = 0
            else:
                next[i] = j + 1

        print next

if __name__ == '__main__':
    s = Solution()
    print 'abcda'
    s.shortestPalindrome('abcda')
    print 'aaaaa'
    s.shortestPalindrome('aaaaa')
