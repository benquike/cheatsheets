class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int

        >>> s = Solution()
        
        >>> s.integerBreak(2)
        2
        >>> s.integerBreak(3)
        3
        >>> s.integerBreak(4)
        4
        >>> s.integerBreak(5)
        6
        >>> s.integerBreak(6)
        9
        >>> s.integerBreak(7)
        12
        >>> s.integerBreak(8)
        18

        """
        
        # f(n) = max(f(i) * f(n - i)), i = 1, 2, ..., n - 1
        # d[i] = f(i + 1)
        
        def m_mul(d, u):
            
            for i in range(0, u - 1):
                if d[u] < d[i] * d[u-i-1]:
                    d[u] = d[i] * d[u-i-1]
        
        if n < 2:
            return 1

        d = [0 for i in range(n)]
        d[0] = 1  # f(1)
        d[1] = 2  # f(2)
        for i in range(2, n):
            m_mul(d, i)
        
        return d[n-1]

if __name__ == '__main__':
    # s = Solution()
    # print s.integerBreak(3)
    import doctest
    doctest.testmod()