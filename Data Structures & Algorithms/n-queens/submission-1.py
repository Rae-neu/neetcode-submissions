class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        chessboard = [ ['.'] * n for _ in range(n)]
        result = []

        self.backtracking(n, 0, chessboard, result)
        return result
    
    def backtracking(self, n, row, chessboard, result):
        if row == n:
            result.append([''.join(r) for r in chessboard])
            return 
        
        for col in range(0, n):
            if self.isValid(row, col, chessboard):
                chessboard[row][col] = 'Q'

                self.backtracking(n, row + 1, chessboard, result)

                chessboard[row][col] = '.'
    
    def isValid(self, row, col, chessboard):
        for i in range(0, row):
            if chessboard[i][col] == 'Q':
                return False
        
        i = row - 1
        j = col - 1
        while i >= 0 and j >= 0:
            if chessboard[i][j] == 'Q':
                return False
            else:
                i -= 1
                j -= 1
        
        i = row - 1
        j = col + 1
        while i >= 0 and j < len(chessboard):
            if chessboard[i][j] == 'Q':
                return False
            else:
                i -= 1
                j += 1
        
        return True



