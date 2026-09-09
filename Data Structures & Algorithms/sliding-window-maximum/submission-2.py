class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        queue = deque()

        for right in range(len(nums)):

            while queue and nums[queue[-1]] < nums[right]:
                queue.pop()
            
            queue.append(right)

            if queue[0] < right - k + 1:
                queue.popleft()
            
            if right >= k - 1:
                result.append(nums[queue[0]])
        
        return result