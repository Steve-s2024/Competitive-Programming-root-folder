# brute force: TLE
class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        stack = []
        trio = set()

        def dfs(node, i):
            if i >= 3:
                if stack[0] == node:
                    # trio-cycle
                    trio.add(tuple(sorted(stack)))
                return
            for nxt in graph[node]:
                stack.append(node)
                dfs(nxt, i + 1)
                stack.pop()

        for i in range(n):
            dfs(i, 0)

        # print(trio)

        res = float('inf')
        for a, b, c in trio:
            l1, l2, l3 = len(graph[a]), len(graph[b]), len(graph[c])
            res = min(res, l1 + l2 + l3 - 6)
        return res if res != float('inf') else -1