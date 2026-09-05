class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        minHeap = [(grid[0][0], 0, 0)]

        visited = [[False] * n for _ in range(n)]

        directions = [[0,1], [1,0], [-1,0], [0,-1]]

        while minHeap:
            time, row, col = heapq.heappop(minHeap)

            if visited[row][col]:
                continue
            
            visited[row][col] = True

            if row == n - 1 and col == n - 1:
                return time
            
            for dx, dy in directions:
                next_x = dx + row
                next_y = dy + col

                if next_x < 0 or next_x >= n or next_y < 0 or next_y >= n:
                    continue
                
                if visited[next_x][next_y]:
                    continue
                
                new_time = max(time, grid[next_x][next_y])

                heapq.heappush(minHeap, (new_time, next_x, next_y))
        
            
