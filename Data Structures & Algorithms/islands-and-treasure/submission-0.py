class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        INF = 2 ** 31 - 1

        queue = deque()
        dir = [[0,1], [1,0], [0,-1], [-1,0]]

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    queue.append([row, col])

        
        while queue:
            row, col = queue.popleft()

            for dx, dy in dir:
                next_x = row + dx
                next_y = col + dy

                if next_x < 0 or next_x >= rows or next_y < 0 or next_y >= cols:
                    continue
                
                if grid[next_x][next_y] != INF:
                    continue
                
                grid[next_x][next_y] = grid[row][col] + 1
                queue.append([next_x, next_y])

