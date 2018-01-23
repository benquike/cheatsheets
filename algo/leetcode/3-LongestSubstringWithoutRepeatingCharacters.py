#!/usr/bin env python

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        if s == None:
            return None
        if s == '':
            return ''
        if len(s) == 1:
            return s

        maxlens = []
        maxlens.append(1)
    
        for i in range(1, len(s)):
            print '=============================='
            print 'i = ' + str(i)
            print 'longest substring without repetition:' + s[i- maxlens[i-1] :i]
            p = s[i- maxlens[i-1] :i].find(s[i])
            print 'p=' + str(p)
            if p == -1:
                maxlens.append(maxlens[i-1] + 1)
                continue
            else:
                maxlens.append(i - p)

            print 'maxlens = ' + str(maxlens)

        max = maxlens[0]
        for i in range(len(maxlens)):
            if max < maxlens[i]:
                max = maxlens[i]

        return max


if __name__ == '__main__':
    s = Solution()
    print s.lengthOfLongestSubstring("abcabcbb")
