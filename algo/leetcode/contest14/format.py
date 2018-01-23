class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str

        >>> s = Solution()
        >>> s.licenseKeyFormatting("2-4A0r7-4k", 3)
        '24-A0R-74K'

        >>> s.licenseKeyFormatting("2-4A0r7-4k", 4)
        '24A0-R74K'

        >>> s.licenseKeyFormatting("---", 4)
        ''
        """

        if K == 0 or len(S) == 0:
            return S
        ret = ''
        added = 0
        for i in range(len(S) - 1, -1, -1):
            if S[i] == '-':
                continue
            p = S[i].upper()
            ret = p + ret
            added = added + 1
            if added == K:
                ret = '-' + ret
                added = 0

        if len(ret) > 0 and ret[0] == '-':
            return ret[1:]
        return ret



if __name__ == "__main__":
    import doctest
    doctest.testmod()
