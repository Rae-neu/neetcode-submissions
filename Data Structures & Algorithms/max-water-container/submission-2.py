class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)

        left = 0
        right = n - 1
        area = 0

        while left < right:
            area = max(area, min(heights[left], heights[right]) * (right - left))
            
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return area