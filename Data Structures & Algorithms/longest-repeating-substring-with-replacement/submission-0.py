class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_freq = 0
        n = len(s)
        count = dict()
        res = 0

        i = 0
        for j in range(n):
            count[s[j]] = count.get(s[j], 0) + 1
            max_freq = max(count.values())

            if (j - i + 1) - max_freq <= k:
                res = j - i + 1
            else:
                i += 1
                count[s[i]] -= 1

        return res
            