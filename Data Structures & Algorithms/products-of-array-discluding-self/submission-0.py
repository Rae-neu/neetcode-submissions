class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)
        i = 0

        while i < len(nums):
            for j in range(len(nums)):
                if j != i:
                    ans[i] *= nums[j]
            i += 1

        return ans