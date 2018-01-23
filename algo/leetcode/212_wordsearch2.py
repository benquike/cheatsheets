#!/bin/env python

class Solution(object):

    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """

        def tryPos(i, j, board, flag, word, pos):
            r = len(board)
            c = len(board[0])

            print "i = " + str(i) + ", j = " + str(j) + ', pos = ' + str(pos)
            if i >= 0 and i < r and j >= 0 and j < c and not flag[i][j] and word[pos] == board[i][j]:
                print "Match"
                flag[i][j] = True
                ret = findWordOnBoard(i, j, board, flag, word, pos+1)
                flag[i][j] = False

                return ret
            return False

        def findWordOnBoard(i, j, board, flag, word, start):
            """
            Find word `word` in board fron pos (i, j) starting from index `start`(of `word`)

            we assume that board[i][j] matches word[start - 1]
            """

            if start >= len(word):
                return True

            assert board[i][j] == word[start - 1], "board(i, j) does not match word[start - 1]"
            assert flag[i][j] != False, "flag(i, j) is not set"

            ret = tryPos(i + 1, j, board, flag, word, start) or \
                  tryPos(i - 1, j, board, flag, word, start) or \
                  tryPos(i, j + 1, board, flag, word, start) or \
                  tryPos(i, j - 1, board, flag, word, start)

            return ret

        ret = []
        r = len(board)
        c = len(board[0])

        for word in words:
            print 'trying word:' + word
            flag = [[False for _ in range(c)] for _ in range(r)]

            for i in range(c):
                for j in range(r):
                    if tryPos(i, j, board, flag, word, 0):
                        ret.append(word)

        return ret


if __name__ == '__main__':
    s = Solution()

    board = [
        ['o','a','a','n'],
        ['e','t','a','e'],
        ['i','h','k','r'],
        ['i','f','l','v']
    ]

    words = ["oath","pea","eat","rain"]

    print s.findWords(board, words)
