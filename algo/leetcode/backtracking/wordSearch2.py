class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """

        def findWordFromPos(board, m, w, i, j):
            print board
            print m
            print w
            print i
            print j
            if i >= len(board) or j > len(board[0]):
                return False
            if len(w) == 0:
                return True
            if board[i][j] != w[0]:
                return False
            m[i][j] = True
            # board[i][j] == w[0]
            if i >  0 and m[i-1][j] != True and findWordFromPos(board, m, w[1:], i-1, j):
                return True
            if j > 0 and m[i][j-1] != True and findWordFromPos(board, m, w[1:], i, j-1):
                return True
            if i < len(board) - 1 and m[i+1][j] != True and findWordFromPos(board, m, w[1:], i+1, j):
                return True
            if j < len(board[0]) - 1 and m[i][j+1] != True and findWordFromPos(board, m, w[1:], i, j+1):
                return True
            m[i][j] = False
            return False

        def findWord(board, word):
            m = []
            for i in range(len(board)):
                m.append([])
                for j in range(len(board[i])):
                    m[i].append(False)

            return findWordFromPos(board, m, word, 0, 0)

        ret = []
        for w in words:
            if findWord(board, w):
                ret.append(w)
        return ret


if __name__ == '__main__':
    s = Solution()
    ws = s.findWords(["oaan","etae","ihkr","iflv"], ["oath","pea","eat","rain"])
    print ws
