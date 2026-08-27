class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        path = []

        open_count = 0
        close_count = 0

        self.backtracking(n, open_count, close_count, path, result)
        return result
    
    def backtracking(self, n, open_count, close_count, path, result):
        if len(path) == 2 * n:
            result.append("".join(path))
            return
        
        if open_count < n:
            path.append("(")
            self.backtracking(n, open_count + 1, close_count, path, result)
            path.pop()
        
        if close_count < n and open_count > close_count:
            path.append(")")
            self.backtracking(n, open_count, close_count + 1, path, result)
            path.pop()

        
