class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-freq for freq in count.values()]

        heapq.heapify(maxHeap)

        cycles = 0
        queue = deque()

        while maxHeap or queue:
            cycles += 1

            if maxHeap:
                freq = heapq.heappop(maxHeap)
                freq += 1

                if freq != 0:
                    queue.append([freq, cycles + n])
            
            if queue and queue[0][1] == cycles:
                freq, readyTime = queue.popleft()

                heapq.heappush(maxHeap, freq)
        

        return cycles