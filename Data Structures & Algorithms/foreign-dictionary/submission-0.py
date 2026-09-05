class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = {}
        indegree = {}

        for word in words:
            for c in word:
                if c not in graph:
                    graph[c] = set()
                    indegree[c] = 0
                
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]

            if len(word1) > len(word2) and word1.startswith(word2):
                return ''
            
            for j in range(min(len(word1), len(word2))):
                if word1[j] != word2[j]:
                    if word2[j] not in graph[word1[j]]:
                        graph[word1[j]].add(word2[j])
                        indegree[word2[j]] += 1
                    break
        
        queue = deque()
        for c in indegree:
            if indegree[c] == 0:
                queue.append(c)
        
        result = []
        while queue:
            c = queue.popleft()
            result.append(c)

            for next_c in graph[c]:
                indegree[next_c] -= 1

                if indegree[next_c] == 0:
                    queue.append(next_c)
        
        if len(result) != len(graph):
            return ''
        
        return ''.join(result)
