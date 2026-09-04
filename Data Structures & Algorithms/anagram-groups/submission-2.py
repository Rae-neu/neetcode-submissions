class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = dict()
        
        for word in strs:
            word_str = ''.join(sorted(word))

            if word_str in group:
                group[word_str].append(word)
            
            else:
                group[word_str] = [word]
        
        return list(group.values())
        

            

        
