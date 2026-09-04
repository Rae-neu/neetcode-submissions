class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = {}

        for start, end in tickets:

            if start not in graph:
                graph[start] = []

            graph[start].append(end)
        
        for start in graph:
            graph[start].sort(reverse = True)
        
        result = []

        def dfs(airport):
            while airport in graph and graph[airport]:
                next_airport = graph[airport].pop()
                dfs(next_airport)

            result.append(airport)
        
        dfs('JFK')

        return result[::-1]
        