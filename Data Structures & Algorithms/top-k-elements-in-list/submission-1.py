class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
        n = len(nums)
        
        l = [[] for _ in range(n + 1)]

        for num, count in freq.items():
            l[count].append(num)
        
        result = []

        for i in range(len(l)-1, -1, -1):
            for num in l[i]:
                result.append(num)

                if len(result) == k:
                    return result

        



        
