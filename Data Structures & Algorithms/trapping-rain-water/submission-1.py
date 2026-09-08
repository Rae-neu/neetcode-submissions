class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        left = 0
        right = n - 1
        max_left = float('-inf')
        max_right = float("-inf")
        ans = 0

        while left < right:
            if height[left] < height[right]:
                if height[left] > max_left:
                    max_left = height[left]
                    left += 1
                else:
                    ans += max_left - height[left]
                    left += 1
            
            else:
                if height[right] > max_right:
                    max_right = height[right]
                    right -= 1
                else:
                    ans += max_right - height[right]
                    right -= 1
        
        return ans