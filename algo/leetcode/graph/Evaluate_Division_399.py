class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        assert len(equations) == len(values)

        if len(equations) == 0:
            return -1.0

        for i in range(len(equations)):
            pass



if __name__ == '__main__':
    s = Solution()
    s.calcEquation()
