class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        if m == 0:
            return 0
        if n == 0:
            return 0
        if m == 1:
            return 1
        if n == 1:
            return 1


        def __uniq_paths(m, n, d):
            print 'm=' + str(m) + ', n=' + str(n)
            if d[m][n] == -1:
                if m == 0 or n == 0:
                    d[m][n] = 1
                else:
                    d[m][n] = __uniq_paths(m - 1, n, d) + __uniq_paths(m, n - 1, d)
            return d[m][n]

        d = []
        for i in range(m):
            d.append([])
            for j in range(n):
                d[i].append(-1)

        __uniq_paths(m-1, n-1, d)

        return d[m-1][n-1]

if __name__ == '__main__':
    s = Solution()
    #print s.uniquePaths(1, 2)

    print s.uniquePaths(2, 3)
