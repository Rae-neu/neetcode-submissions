class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProduct = nums[0]
        minProduct = nums[0]
        result = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]

            previousMax = maxProduct
            previousMin = minProduct

            maxProduct = max(num, previousMax * num, previousMin * num)
            minProduct = min(num, previousMax * num, previousMin * num)

            result = max(result, maxProduct)
        
        return result