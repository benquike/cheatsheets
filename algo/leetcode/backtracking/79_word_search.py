class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        
        if len(board) == 0 or len(board[0]) == 0:
            return False
        
        if len(word) == 0:
            return True
        
        def helper(board, flag, word, i, x, y):
            

            if board[x][y] != word[i]:
                return False
            else:
                if i == len(word) - 1:
                    return True
            
            flag[x][y] = True
            
            if x - 1 >= 0 and not flag[x-1][y] and helper(board, flag, word, i+1, x - 1, y):
                flag[x][y] = False
                return  True
            
            if x + 1 < row and not flag[x+1][y] and helper(board, flag, word, i+1, x + 1, y):
                flag[x][y] = False
                return  True
            
            if y - 1 >= 0 and not flag[x][y - 1] and helper(board, flag, word, i+1, x, y - 1):
                flag[x][y] = False
                return  True
            
            if y + 1 < column and not flag[x][y + 1] and helper(board, flag, word, i+1, x, y + 1):
                flag[x][y] = False
                return  True
            
            flag[x][y] = False
            return False
             
            
            
        
        row = len(board)
        column = len(board[0])
        
        flag = [[False for i in range(column)] for j in range(row)]
        
        for i in range(row):
            for j in range(column):
                if helper(board, flag, word, 0, i, j):
                    return True
        
        return False


def main():
    board = [["a","b"]]
    _str = "ba"
    s = Solution()
    print s.exist(board, _str)

if __name__ == '__main__':
    main()
