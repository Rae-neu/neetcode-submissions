class Solution:
    def partition(self, s: str) -> List[List[str]]:
        path = []
        result = []

        self.backtracking(s, 0, path, result)
        return result

    def backtracking(self, s, startIndex, path, result):
        if startIndex == len(s):
            result.append(path.copy())
            return
        
        for i in range(startIndex, len(s)):
            if self.isPalindrome(s, startIndex, i):
                path.append(s[startIndex : i + 1])

                self.backtracking(s, i + 1, path, result)

                path.pop()
    
    def isPalindrome(self, s, start, end):
        while start < end:
            if s[start] == s[end]:
                start += 1
                end -= 1
            else:
                return False
        
        return True
        
