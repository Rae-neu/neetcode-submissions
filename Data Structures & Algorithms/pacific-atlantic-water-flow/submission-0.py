class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])

        pacific = set()
        atlantic = set()

        directions = [[0,1], [1,0], [0,-1], [-1,0]]

        def dfs(row, col, visited):
            visited.add((row, col))

            for dx, dy in directions:
                next_x = dx + row
                next_y = dy + col

                if next_x < 0 or next_x >= rows or next_y < 0 or next_y >= cols:
                    continue
                
                if (next_x, next_y) in visited:
                    continue
                
                if heights[next_x][next_y] >= heights[row][col]:
                    dfs(next_x, next_y, visited)

        for row in range(rows):
            dfs(row, 0, pacific)
        for col in range(cols):
            dfs(0, col, pacific)
        
        for row in range(rows):
            dfs(row, cols - 1, atlantic)
        for col in range(cols):
            dfs(rows - 1, col, atlantic)

        result = []
        for i in range(rows):
            for j in range(cols):
                if (i,j) in pacific and (i,j) in atlantic:
                    result.append([i, j])
        return result
        
