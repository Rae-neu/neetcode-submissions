class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ''
        
        t_dict = dict()

        for char in t:
            t_dict[char] = t_dict.get(char, 0) + 1
        
        missing = len(t)
        left = 0
        min_length = float('inf')
        start = 0

        for right in range(len(s)):
            char = s[right]

            if char in t_dict:
                if t_dict[char] > 0:
                    missing -= 1
                
                t_dict[char] -= 1
            
            while missing == 0:
                if right - left + 1 < min_length:
                    min_length = right - left + 1
                    start = left

                if s[left] in t_dict:
                    t_dict[s[left]] += 1

                    if t_dict[s[left]] > 0:
                        missing += 1
                
                left += 1
        
        if min_length == float('inf'):
            return ''

        return s[start : start + min_length]
