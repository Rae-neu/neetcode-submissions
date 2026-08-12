class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}

        for i in range(len(strs)):
            word = strs[i]

            key = ''.join(sorted(word))
            if key in group:
                group[key].append(word)
            else:
                group[key] = []
                group[key].append(word)
            
        return list(group.values())
        
