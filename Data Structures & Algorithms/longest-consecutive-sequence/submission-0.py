class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set()
        ans = 0

        for num in nums:
            nums_set.add(num)
        
        for num in nums_set:
            if num-1 not in nums_set:
                start = num
                result = 1

                while start+1 in nums_set:
                    result += 1
                    start += 1

                ans = max(ans, result)

        return ans