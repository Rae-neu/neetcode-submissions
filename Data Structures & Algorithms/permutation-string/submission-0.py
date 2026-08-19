class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        count1 = [0] * 26
        count2 = [0] * 26

        for i in range(len(s1)):
            index1 = ord(s1[i]) - ord('a')
            index2 = ord(s2[i]) - ord('a')

            count1[index1] += 1
            count2[index2] += 1

        if count1 == count2:
            return True
        
        left = 0
        for right in range(len(s1), len(s2)):
            index = ord(s2[right]) - ord('a')
            count2[index] += 1

            index = ord(s2[left]) - ord('a')
            count2[index] -= 1
            left += 1

            if count1 == count2:
                return True
        
        return False