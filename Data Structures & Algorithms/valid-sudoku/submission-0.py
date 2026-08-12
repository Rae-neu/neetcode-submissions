class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(0, 9):
            row_set = set()
            for j in range(0, 9):
                if board[i][j] == '.':
                    continue
                elif board[i][j] in row_set:
                    return False
                else:
                    row_set.add(board[i][j])
        

        for j in range(0, 9):
            col_set = set()
            for i in range(0, 9):
                if board[i][j] == '.':
                    continue
                elif board[i][j] in col_set:
                    return False
                else:
                    col_set.add(board[i][j])
        

        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                box_set = set()

                for i in range(box_row, box_row + 3):
                    for j in range(box_col, box_col + 3):
                        if board[i][j] == '.':
                            continue
                        
                        elif board[i][j] in box_set:
                            return False
                        
                        else:
                            box_set.add(board[i][j])
        return True