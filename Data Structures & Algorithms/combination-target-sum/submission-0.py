class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        path = []
        result = []

        self.backtracking(nums, target, 0, path, result)
        return result
        
    def backtracking(self, nums, target, startIndex, path, result):
        if target == 0:
            result.append(path.copy())
            return
        
        if target < 0:
            return
        
        for i in range(startIndex, len(nums)):
            target -= nums[i]
            path.append(nums[i])

            self.backtracking(nums, target, i, path, result)

            path.pop()
            target += nums[i]
        

        