class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        visited = [False] * n
        minDist = [float('inf')] * n

        minDist[0] = 0
        result = 0

        for _ in range(n):
            current = -1

            for i in range(n):
                if not visited[i] and (current == -1 or minDist[i] < minDist[current]):
                    current = i
                
            visited[current] = True
            result += minDist[current]

            x1, y1 = points[current]

            for nextNode in range(n):
                if not visited[nextNode]:
                    x2, y2 = points[nextNode]

                    distance = abs(x2 - x1) + abs(y2 - y1)

                    if distance < minDist[nextNode]:
                        minDist[nextNode] = distance
                        
        return result