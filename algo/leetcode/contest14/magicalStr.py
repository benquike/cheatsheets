class Solution(object):
    def magicalString(self, n):
        """
        :type n: int
        :rtype: int

        >>> s = Solution()
        >>> s.magicalString(1)
        1
        >>> s.magicalString(2)
        1
        >>> s.magicalString(3)
        1
        >>> s.magicalString(4)
        2
        >>> s.magicalString(5)
        3
        >>> s.magicalString(6)
        3

        >>> s.magicalString(7)
        4
        >>> s.magicalString(8)
        4
        """
        if n <= 3:
            return 1
        # go from 4
        s = '122'
        ci = 2
        c1 = 1
        one = True
        while len(s) <= n:
            if one:
                if s[ci] == '2':
                    s = s + '11'
                    c1 = c1 + 2
                else:
                    s = s + '1'
                    c1 = c1 + 1
            else:
                if s[ci] == '2':
                    s = s + '22'
                else:
                    s = s + '2'
            print s
            one = not one
            ci = ci + 1

        if len(s) > n and s[len(s) - 1] == '1':
            return c1 - 1
        return c1

if __name__ == "__main__":
    import doctest
    doctest.testmod()
