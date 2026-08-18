class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        ans = 0

        i = 0
        j = i + 1

        while j < n:
            if prices[j] > prices[i]:
                ans = max(ans, prices[j] - prices[i])
                j += 1
            else:
                i = j
                j += 1
        return ans
