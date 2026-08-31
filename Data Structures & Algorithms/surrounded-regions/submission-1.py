class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])

        directions = [[0,1], [1,0], [-1,0], [0,-1]]

        def dfs(row, col):
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return
            
            if board[row][col] != 'O':
                return
            
            board[row][col] = '#'

            for dx, dy in directions:
                next_x = dx + row
                next_y = dy + col
                
                dfs(next_x, next_y)
        
        for i in range(rows):
            if board[i][0] == 'O':
                dfs(i, 0)
            if board[i][cols-1] == 'O':
                dfs(i, cols-1)

        for j in range(cols):
            if board[0][j] == 'O':
                dfs(0, j)
            if board[rows-1][j] == 'O':
                dfs(rows-1, j)
            
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == '#':
                    board[i][j] = 'O'
        

