# optimized: 100%
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for u, v in tickets: graph[u].append(v)
        for val in graph.values(): val.sort(reverse=True)

        arr = []
        def dfs(node):
            while graph[node]: dfs(graph[node].pop())
            arr.append(node)
        dfs('JFK')
        return arr[::-1]


# Eulerian path solution: 41%
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for u, v in tickets: graph[u].append(v)
        for val in graph.values(): val.sort(reverse=True)

        arr = []
        def dfs(node):
            while graph[node]:
                nxt = graph[node].pop()
                dfs(nxt)
                arr.append(nxt)
                # print(node, '->', nxt)
        dfs('JFK')
        return ['JFK'] + arr[::-1]