class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = [[] for _ in range(n + 1)]

        for u, v, t in times:
            graph[u].append([v, t])
        
        minHeap = [(0, k)]
        visited = set()
        maxTime = 0

        while minHeap:
            time, node  = heapq.heappop(minHeap)

            if node in visited:
                continue
            
            visited.add(node)
            maxTime = time

            for neighbor, edgeTime in graph[node]:
                heapq.heappush(minHeap, (time + edgeTime, neighbor))

        if len(visited) == n:
            return maxTime
        
        return -1