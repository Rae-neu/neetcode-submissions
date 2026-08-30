class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])

        dir = [[0,1], [0,-1], [1,0], [-1,0]]

        visited = [[False] * m for _ in range(n)]

        def dfs(x, y):
            if x < 0 or x >= n or y < 0 or y >= m:
                return
            
            if visited[x][y] or grid[x][y] == '0':
                return
            
            visited[x][y] = True

            for dx, dy in dir:
                next_x = x + dx
                next_y = y + dy

                dfs(next_x, next_y)

        result = 0
        for i in range(n):
            for j in range(m):
                if not visited[i][j] and grid[i][j] == '1':
                    result += 1

                    dfs(i,j)
        return result
