class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []

        self.backtracking(nums, 0, path, result)
        return result

    def backtracking(self, nums, startIndex, path, result):
        result.append(path[:])

        for i in range(startIndex, len(nums)):
            path.append(nums[i])
            self.backtracking(nums,i + 1, path, result)
            path.pop()