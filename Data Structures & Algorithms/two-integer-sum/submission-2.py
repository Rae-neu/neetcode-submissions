class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        n = len(nums)

        i = 0
        j = n - 1

        while i < j:
            if nums[i] + nums[j] < target:
                i += 1
            elif nums[i] + nums[j] > target:
                j -= 1
            else:
                return [i, j]