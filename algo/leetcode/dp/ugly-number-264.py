class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int

        >>> s = Solution()
        >>> s.nthUglyNumber(1)
        1
        >>> s.nthUglyNumber(2)
        2
        >>> s.nthUglyNumber(3)
        3
        >>> s.nthUglyNumber(4)
        4
        >>> s.nthUglyNumber(5)
        5
        >>> s.nthUglyNumber(6)
        6
        >>> s.nthUglyNumber(7)
        8
        >>> s.nthUglyNumber(8)
        9
        >>> s.nthUglyNumber(9)
        10
        >>> s.nthUglyNumber(10)
        12
        """
        
        if n == 1:
            return 1
        
        def __extract_min(q1, q2, q3):
            ret = None
            x = [q1, q2, q3]
            i = None
            if len(q1) > 0:
                ret = q1[0]
                i = 0
            
            if len(q2) > 0:
                if ret == None or ret > q2[0]:
                    ret = q2[0]
                    i = 1
                    
                elif ret == q2[0]:
                    del q2[0]
            if len(q3) > 0:
                if ret == None or ret > q3[0]:
                    ret = q3[0]
                    i = 2
                elif ret == q3[0]:
                    del q3[0]
            
            if i != None:
                del x[i][0]
                
            return ret
            
        cnt = 1
        cur = 1
        q1 = [2]
        q2 = [3]
        q3 = [5]
        
        while cnt < n:
            cur = __extract_min(q1, q2, q3)
            cnt = cnt + 1
            q1.append(cur * 2)
            q2.append(cur * 3)
            q3.append(cur * 5)
        
        return cur

if __name__ == '__main__':
    # s = Solution()
    # print s.integerBreak(3)
    import doctest
    doctest.testmod()