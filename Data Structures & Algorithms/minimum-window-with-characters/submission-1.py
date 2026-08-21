class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count = dict()

        for char in t:
            count[char] = count.get(char, 0) + 1

        n = len(s)
        missing = len(t)

        ans = float('inf')
        ans_left = 0
        ans_right = n + 1

        left = 0
        for right in range(left, n):
            if s[right] in count:

                if count[s[right]] > 0:
                    missing -= 1

                count[s[right]] -= 1

            if missing == 0:

                while left <= right:
                    if s[left] not in count:
                        left += 1
                    elif count[s[left]] < 0:
                        count[s[left]] += 1
                        left += 1
                    else:
                        break
            
                if right - left + 1 < ans:
                    ans = right - left + 1
                    ans_left = left
                    ans_right = right

        if ans == float('inf'):
            return ''

        return s[ans_left: ans_right + 1]

                
                
            