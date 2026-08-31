class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        fresh = 0
        queue = deque()
        directions = [[0,1], [1,0], [0,-1], [-1,0]]
        minutes = 0

        for row in range(n):
            for col in range(m):
                if grid[row][col] == 2:
                    queue.append([row, col])
                elif grid[row][col] == 1:
                    fresh += 1
        
        while queue and fresh > 0:
            for _ in range(len(queue)):
                row, col = queue.popleft()

                for dx, dy in directions:
                    next_x = dx + row
                    next_y = dy + col

                    if next_x < 0 or next_x >= n or next_y < 0 or next_y >= m:
                        continue
                    
                    if grid[next_x][next_y] != 1:
                        continue
                    
                    grid[next_x][next_y] = 2
                    fresh -= 1
                    queue.append([next_x, next_y])

            minutes += 1
        
        if fresh == 0:
            return minutes
        
        return -1