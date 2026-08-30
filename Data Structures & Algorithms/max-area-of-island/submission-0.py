class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        visited = [[False] * m for _ in range(n)]
        dir = [[0,1], [1,0], [-1,0], [0,-1]]

        def dfs(x, y):
            if x < 0 or x >= n or y < 0 or y >= m:
                return 0
            
            if visited[x][y] == True or grid[x][y] == 0:
                return 0
            
            visited[x][y] = True
            area = 1

            for dx, dy in dir:
                next_x = x + dx
                next_y = y + dy

                area += dfs(next_x, next_y)
            
            return area
            
        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if visited[i][j] == False and grid[i][j] == 1:
                    area = dfs(i,j)

                    result = max(result, area)
        return result
