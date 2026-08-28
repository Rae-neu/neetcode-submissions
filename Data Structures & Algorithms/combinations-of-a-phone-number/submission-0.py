class Solution:
    def __init__(self):
        self.letterMap = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
    
    def backtracking(self, digits, index, s, result):
        if index == len(digits):
            result.append(s)
            return 

        digit = int(digits[index])
        letter = self.letterMap[digit]

        for i in range(0, len(letter)):
            s += letter[i]

            self.backtracking(digits, index + 1, s, result)

            s = s[:-1]


    def letterCombinations(self, digits: str) -> List[str]:
        if not len(digits):
            return []

        s = ''
        result = []
        
        self.backtracking(digits, 0, s, result)
        return result
        