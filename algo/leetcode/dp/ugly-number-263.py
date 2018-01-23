class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool

        >>> s = Solution()
        >>> s.isUgly(1)
        True
        >>> s.isUgly(2)
        True
        >>> s.isUgly(3)
        True
        >>> s.isUgly(4)
        True
        >>> s.isUgly(5)
        True
        >>> s.isUgly(6)
        True
        >>> s.isUgly(7)
        False
        >>> s.isUgly(8)
        True
        >>> s.isUgly(9)
        True
        >>> s.isUgly(10)
        True
        >>> s.isUgly(11)
        False

        """
        if num == 1:
            return True
        
        while num % 5 == 0:
            num = num/5
        while num % 3 == 0:
            num = num / 3
        while num % 2 == 0:
            num = num /2
        return num == 1



if __name__ == '__main__':
    # s = Solution()
    # print s.integerBreak(3)
    import doctest
    doctest.testmod()