class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        minDist = [float('inf')] * n
        minDist[src] = 0

        for _ in range(k + 1):
            minDist_copy = minDist.copy()

            for start, end, price in flights:
                if minDist_copy[start] == float('inf'):
                    continue
                
                if minDist_copy[start] + price < minDist[end]:
                    minDist[end] = minDist_copy[start] + price
        
        if minDist[dst] == float('inf'):
            return -1
        
        return minDist[dst]