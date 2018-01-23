class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """

        if len(obstacleGrid) == 0:
            return 0
        if len(obstacleGrid[0]) == 0:
            return 0

        def __uniq_paths(x, y, d, obsGrid):
            if d[x][y] == -1:
                if obsGrid[x][y] == 1:
                    d[x][y] = 0
                elif x == len(obsGrid) - 1 and y == len(obsGrid[0]) - 1:
                    d[x][y] = 1
                else:
                    c = 0
                    if x + 1 < len(obsGrid):
                        c = c + __uniq_paths(x+1, y, d,obsGrid)
                    if y + 1 < len(obsGrid[0]):
                        c = c + __uniq_paths(x, y+1, d, obsGrid)
                    d[x][y] = c
            return d[x][y]


        d = []
        for i in range(len(obstacleGrid)):
            d.append([])
            for j in range(len(obstacleGrid[i])):
                d[i].append(-1)

        __uniq_paths(0, 0, d, obstacleGrid)

        return d[0][0]

if __name__ == '__main__':
    s = Solution()
    print s.uniquePathsWithObstacles([[0,1], [0, 0]])
