# tree problem
class Solution:
    def baseUnitConversions(self, conversions: List[List[int]]) -> List[int]:
        n = len(conversions)+1
        graph = defaultdict(list)
        for a, b, factor in conversions:
            graph[a].append((b, factor))
        visited = set()
        res = 0
        ans = [0] * n
        MOD = 1000000007
        def dfs(node, totalFac):
            nonlocal res, MOD
            totalFac %= MOD
            ans[node] = totalFac
            for nextNode, factor in graph[node]:
                if nextNode not in visited:
                    visited.add(nextNode)
                    dfs(nextNode, totalFac * factor)

        dfs(0, 1)
        return ans