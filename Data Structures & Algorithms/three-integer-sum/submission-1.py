class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = []

        for i in range(0, n - 2):
            j = i + 1
            k = n - 1

            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            if nums[n-1] + nums[n-2] + nums[n-3] < 0:
                break
            
            if nums[i] + nums[i+1] + nums[i+2] > 0:
                break

            while j < k:
                total = nums[i] + nums[j] + nums[k]

                if total == 0:
                    ans.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while i < j < k and nums[j] == nums[j-1]:
                        j += 1
                    while j < k < n-1 and nums[k] == nums[k+1]:
                        k -= 1

                elif total < 0:
                    j += 1

                else:
                    k -= 1

        return ans