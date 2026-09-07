class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        result = []

        if nums[n - 1] + nums[n - 2] + nums[n - 3] < 0:
            return []
        
        if nums[0] + nums[1] + nums[2] > 0:
            return []

        for i in range(0, n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            if nums[i] + nums[n - 1] + nums[n - 2] < 0:
                continue
            
            if nums[i] + nums[i + 1] + nums[i + 2] > 0:
                break
            
            j = i + 1
            k = n - 1

            while j < k:
                if nums[i] + nums[j] + nums[k] < 0:
                    j += 1 

                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                    
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    
                    j += 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1

                    k -= 1
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1
        
        return result