# google's question is always so simple but un-intuitive. I have to check the hint to solve it: 11%
class Solution:
    def maximumScore(self, scores: List[int], edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        for val in graph.values():
            val.sort(key=lambda i: scores[i], reverse=True)

        res = -1
        for u, v in edges:
            for i in range(min(len(graph[u]), 4)):
                for j in range(min(len(graph[v]), 4)):
                    if (
                        graph[u][i] not in [v, graph[v][j]] and
                        graph[v][j] not in [u, graph[u][i]]
                    ):
                        tot = scores[u] + scores[v] + scores[graph[u][i]] + scores[graph[v][j]]
                        res = max(res, tot)
        return res

