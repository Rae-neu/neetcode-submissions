class Solution:

    def encode(self, strs: List[str]) -> str:
        part = []
        
        for word in strs:
            part.append(str(len(word)) + '#' + word)

        return ''.join(part)

    def decode(self, s: str) -> List[str]:
        answer = []
        i = 0

        while i < len(s):
            for j in range(i, len(s)):
                if s[j] == '#':
                    num = int(s[i : j])
                    answer.append(s[j + 1 : j + num + 1])

                    i = j + num + 1
                    break

        return answer

