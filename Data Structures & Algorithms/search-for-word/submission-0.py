class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if self.backtracking(board, word, 0, i, j):
                        return True
        return False

    def backtracking(self, board, word, index, row, col):
        if index == len(word):
            return True
        
        if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
            return False

        if board[row][col] != word[index]:
            return False
        
        temp = board[row][col]
        board[row][col] = '#'

        up = self.backtracking(board, word, index + 1, row - 1, col)
        down = self.backtracking(board, word, index + 1, row + 1, col)
        left = self.backtracking(board, word, index + 1, row, col - 1)
        right = self.backtracking(board, word, index + 1, row, col + 1)

        board[row][col] = temp

        return up or down or left or right


