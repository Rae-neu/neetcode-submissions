class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n = len(s)
        m = len(t)

        if n != m:
            return False
        
        dict_s = dict()
        for i in range(n):
            dict_s[s[i]] = dict_s.get(s[i], 0) + 1
        
        for j in range(m):
            if t[j] in dict_s:
                dict_s[t[j]] = dict_s.get(t[j]) - 1

                if dict_s[t[j]] < 0:
                    return False
            else:
                return False
        
        return True
