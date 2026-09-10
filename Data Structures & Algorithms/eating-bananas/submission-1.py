class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left <= right:
            time = 0
            mid = (left + right) // 2

            for pile in piles:
                time += (pile + mid - 1) // mid

            if time > h:
                left  =  mid + 1
            else:
                right = mid - 1
            
        return left
            