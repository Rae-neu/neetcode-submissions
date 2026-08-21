class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n =  len(nums)
        res = []

        left = 0
        right = left + k - 1

        while left < right < n:
            num = float('-inf')
            
            for i in range(left, right + 1):
                num = max(num, nums[i])
            res.append(num)

            left += 1
            right += 1
        
        return res
