class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left <= right:
            mid = (right + left) // 2
            total = 0
            
            for pile in piles:
                total += (pile + mid - 1) // mid

            if total > h:
                left = mid + 1
            else:
                ans = mid
                right = mid - 1
        
        return ans