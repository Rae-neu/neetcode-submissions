class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        path = []
        candidates.sort()
        self.backtracking(candidates, target, 0, path, result)
        return result

    def backtracking(self, candidates, target, startIndex, path, result):
        if target == 0:
            result.append(path.copy())
            return result
        
        if target < 0:
            return 
        
        for i in range(startIndex, len(candidates)):
            if i >startIndex and candidates[i] == candidates[i-1]:
                continue

            target -= candidates[i]
            path.append(candidates[i])

            self.backtracking(candidates, target, i + 1, path, result)

            path.pop()
            target += candidates[i]


