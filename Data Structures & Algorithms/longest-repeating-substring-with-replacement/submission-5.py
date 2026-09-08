class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        s_dict = dict()
        length = 0

        i = 0
        for j in range(i, n):
            s_dict[s[j]] = s_dict.get(s[j], 0) + 1

            while (j - i + 1) - max(s_dict.values()) > k:
                s_dict.get(s[i]) - 1
                i += 1
            
            length = max(length, j - i +1)
        
        return length