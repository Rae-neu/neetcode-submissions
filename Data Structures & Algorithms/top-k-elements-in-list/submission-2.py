class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_nums = dict()
        result = []

        for num in nums:
            dict_nums[num] = dict_nums.get(num, 0) + 1

        freq = [[] for _ in range(len(nums) + 1)]

        for num, count in dict_nums.items():
            freq[count].append(num)
        
        for i in range(len(freq) - 1, -1, -1):
                for num in freq[i]:
                    result.append(num)
                    k -= 1
        
                    if k == 0:
                        return result