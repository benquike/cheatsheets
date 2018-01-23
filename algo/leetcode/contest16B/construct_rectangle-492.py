import math

class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """

        if area < 1:
            return [0, 0]

        def abs(x):
            if x[0] > x[1]:
                return x[0] - x[1]
            return x[1] - x[0]

        res = [area, 1]
        for i in range(int(math.sqrt(area)), 0, -1):
            if area % i == 0:
                if abs(res) > abs([i, area/i]):
                    res = [i, area/i]
                    break

        if res[0] > res[1]:
            return res
        return [res[1], res[0]]

if __name__ == '__main__':
    s = Solution()
    s.constructRectangle()
