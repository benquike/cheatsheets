
import math

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int

        >>> s = Solution()
        >>> s.numSquares(1)
        1
        >>> s.numSquares(2)
        2
        >>> s.numSquares(3)
        3
        >>> s.numSquares(4)
        1
        >>> s.numSquares(5)
        2
        >>> s.numSquares(6)
        3
        >>> s.numSquares(7)
        4
        >>> s.numSquares(8)
        2
        >>> s.numSquares(9)
        1
        >>> s.numSquares(10)
        2
        """
        
        if math.floor(math.sqrt(n)) ** 2 == n:
            return 1

        d = [0 for i in range(n)]

        for i in range(n):
        	if math.floor(math.sqrt(n)) ** 2 == i + 1:
        		d[i] = 1
        	else:
        		d[i] = 1 + d[0] + d[i-1]
        		for j in range(i-1):
        			if d[i] > 1 + d[j] + d[i- 1 - j]:
                        d[i] = 1 + d[j] + d[i - 1 - j]
        	
        return d[n-1]

if __name__ == '__main__':
    import doctest
    doctest.testmod()