class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int

        >>> s = Solution()
        >>> s.findComplement(1)
        0
        >>> s.findComplement(2)
        1
        >>> s.findComplement(3)
        0
        >>> s.findComplement(4)
        3
        """

        i = 0
        m = 0x1
        x = 0
        for i in range(32):
            if ((0x1 << i) & num) != 0:
                x = i
        # print 'x = ' + '{%x}'.format(x)
        while x > 0:
            m = m << 1
            m = m + 1
            x = x - 1

        # print 'm = ' + '{%x}'.format(m)
        return (~num ) & m


if __name__ == "__main__":
    import doctest
    doctest.testmod()
