class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        left = 0
        right = n - 1
        left_max = 0
        right_max = 0
        water = 0

        while left < right:
            if height[left] < height[right]:
                if left_max > height[left]:
                    water += left_max - height[left]
                    left += 1
                else:
                    left_max = height[left]
                    left += 1
            else:
                if height[right] < right_max:
                    water += right_max - height[right]
                    right -= 1
                else:
                    right_max = height[right]
                    right -= 1

        return water


