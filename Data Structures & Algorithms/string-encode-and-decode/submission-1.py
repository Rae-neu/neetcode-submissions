class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ''
        for i in range(len(strs)):
            num = len(strs[i])
            result += str(num) + '#' + strs[i]
        return result

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

