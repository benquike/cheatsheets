class Solution(object):

    def numberOfArithmeticSlices(self, A):

        """
        :type A: List[int]
        :rtype: int

        >>> s = Solution()
        >>> s.numberOfArithmeticSlices([1, 2, 3])
        1

        >>> s.numberOfArithmeticSlices([1, 2, 3, 4])
        3

        >>> s.numberOfArithmeticSlices([1, 2, 3, 5])
        1

        >>> s.numberOfArithmeticSlices([1, 2, 3, 5, 6])
        1

        >>> s.numberOfArithmeticSlices([1, 2, 3, 5, 6, 7])
        2
        """

        if len(A) < 3:
            return 0
        l = len(A)
        dp = [0 for i in range(l)]

        diff = A[1] - A[0]
        for i in range(2, l):
            if A[i] - A[i-1] == diff:
                dp[i] = dp[i-1] + 1
            else:
                dp[i] = 0
                diff = A[i] - A[i-1]

        return sum(dp)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
