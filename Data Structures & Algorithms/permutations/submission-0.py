class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        path = []
        result = []

        used = [False] * len(nums
        )
        self.backtracking(nums, used, path, result)
        return result

    def backtracking(self, nums, used, path, result):
        if len(path) == len(nums):
            result.append(path.copy())
            return
        
        for i in range(0, len(nums)):
            if used[i] == True:
                continue

            path.append(nums[i])
            used[i] = True

            self.backtracking(nums, used, path, result)

            path.pop()
            used[i] = False


