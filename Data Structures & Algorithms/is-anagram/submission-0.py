class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count = {}
        
        for i in s:
            count[i] = count.get(i, 0) + 1
        
        for j in t:
            count[j] = count.get(j, 0) - 1
        
        for val in count.values():
            if val != 0:
                return False

        return True
        