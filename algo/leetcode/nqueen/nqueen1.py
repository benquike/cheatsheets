#!/usr/bin/env python

class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """

        sol = []
        for i in range(n):
            sol.append([])
            for j in range(j):
                sol[i].append(False)

        def checkIJ(flags, i, j, n, val):
            for k in range(n):
                if flags[i][k] != val:
                    return False
                if flags[k][j] != val:
                    return False
            x, y =  i - 1, j -1

            # x - y = i - j
            while x >= 0 and y >= 0:
                if flags[x][y] != val:
                    return False
                x = x - 1
                y = y - 1

            x, y = i + 1, j + 1
            while x < n and y < n:
                if flags[x][y] != val:
                    return False
                x = x + 1
                y = y + 1

            # x + y = i + j
            x, y = i - 1, j + 1
            while x >= 0 and y < n:
                if flags[x][y] != val:
                    return False

                x = x - 1
                y = y + 1

            x, y = i + 1, j - 1
            while i < n and y >= 0:
                if flags[x][y] != val:
                    return False
                x = x + 1
                y = y -1

            return True

        def setIJ(flags, i, j, n, val):
            for k in range(n):
                flags[i][k] = val
                flags[k][j] = val

            # x - y = i - j
            while x >= 0 and y >= 0:
                flags[x][y] = val
                x = x - 1
                y = y - 1

            x, y = i + 1, j + 1
            while x < n and y < n:
                flags[x][y] = val
                x = x + 1
                y = y + 1

            # x + y = i + j
            x, y = i - 1, j + 1
            while x >= 0 and y < n:
                flags[x][y] = val
                x = x - 1
                y = y + 1

            x, y = i + 1, j - 1
            while i < n and y >= 0:
                flags[x][y] = val
                x = x + 1
                y = y - 1

        for i in range(n): # the i the chess, to be put in the ith row
            for j in range(n):   # search all the positions in the ith row
                if not checkIJ(sol, i, j, n, True):
                    # position taken
                    continue
                # not taken, try taking it
                

if __name__ == '__main__':
    pass
