class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}

        for word in strs:

            key = ''.join(sorted(word))

            if key in group:
                group[key].append(word)
            else:
                group[key] = [word]
            
        return list(group.values())
        
