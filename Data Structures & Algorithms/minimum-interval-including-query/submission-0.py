class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        sorted_queries = sorted(queries)
        intervals.sort()

        min_heap = []
        res = dict()

        i = 0
        for query in sorted_queries:
            while i < len(intervals) and intervals[i][0] <= query:
                left, right = intervals[i]
                length = right - left + 1
                heapq.heappush(min_heap, (length, right))

                i += 1
            
            while min_heap and min_heap[0][1] < query:
                heapq.heappop(min_heap)
            
            if min_heap:
                res[query] = min_heap[0][0]
            else:
                res[query] = -1
            
        
        result = []

        for query in queries:
            result.append(res[query])
        
        return result
