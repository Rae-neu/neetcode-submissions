class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        path =[]
        result = []

        nums.sort()
        self.backtracking(nums, 0, path, result)
        return result

    def backtracking(self, nums, startIndex, path, result):
        result.append(path.copy())

        for i in range(startIndex, len(nums)):
            if i > startIndex and nums[i] == nums[i-1]:
                continue

            path.append(nums[i])

            self.backtracking(nums, i + 1, path, result)

            path.pop()
