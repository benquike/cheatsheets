import collections

class Solution(object):
    def findMinStep(self, board, hand):
        """
        :type board: str
        :type hand: str
        :rtype: int
        """

        if len(board) == 0:
            return 0

        print "board:" + board + ", hand:" + hand

        # handle board first
        handled_board = ''
        i = 0
        while i < len(board):
            j = i + 1
            while j < len(board) and board[j] == board[i]:
                j = j + 1
            if j-i < 3:
                handled_board = handled_board + board[i:j]
            i = j

        if len(handled_board) > 0 and len(hand) == 0:
            return -1

        print "handled_board:" + board

        ## else
        ## do something interesting

        # we are going to put a ball to the board
        i = 0
        for i in range(len(hand)):
            f = board.find(hand[i] * 2)
            if f != -1:
                print "There are 2 " + hand[i] + " in board, index is " + str(f)
                ret = self.findMinStep(board[0:f] + board[f+2:], hand[0:i]+hand[i+1:])
                if ret == -1:
                    return -1
                return ret + 1

        # all balls have only one
        for i in range(len(board)):
            cnt = collections.Counter(hand)
            if cnt[board[i]] >= 2:
                #
                i1 = hand.find(board[i])
                h1 = hand[0:i1] + hand[i1+1:]
                i2 = h1.find(board[i])
                h2 = h1[0:i2] + h1[i2+1:]
                ret = self.findMinStep(board[0:i] + board[i+1:], h2)
                if ret == -1:
                    return -1
                return ret + 2
        return -1

if __name__ == "__main__":
    s = Solution()
    print s.findMinStep("WRRBBW", "RB")
    print s.findMinStep("WWRRBBWW", "WRBRW")
    print s.findMinStep("G", "GGGGG")
    print s.findMinStep("RBYYBBRRB", "YRBGB")
