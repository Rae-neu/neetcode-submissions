class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        area = 0
        n = len(heights)

        for i in range(0, n):
            while stack and heights[i] < heights[stack[-1]]:
                index = stack.pop()
                height = heights[index]

                if stack:
                    width = i - stack[-1] -1
                else:
                    width = i

                area = max(area, height * width)
            stack.append(i)


        while stack:
                index = stack.pop()
                height = heights[index]

                if stack:
                    width = n - stack[-1] -1
                else:
                    width = n
                
                area = max(area, height * width)


        return area        
                

        
        