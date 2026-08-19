class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)

        i = 0
        char_set = set()
        res = 0

        for j in range(i, n):
            while s[j] in char_set:
                char_set.remove(s[i])
                i += 1

            char_set.add(s[j])
            res = max(res, j - i + 1)

        return res
