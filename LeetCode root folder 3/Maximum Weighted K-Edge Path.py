# dfs brute force: TLE
class Solution:
    def maxWeight(self, n: int, edges: List[List[int]], k: int, t: int) -> int:
        graph = defaultdict(list)
        for a, b, w in edges:
            graph[a].append((b, w))

        def dfs(node, pathLen, total):
            nonlocal t, k, res
            if pathLen == k:
                if total < t:
                    res = max(total, res)
                return
            for nxt, weight in graph[node]:
                dfs(nxt, pathLen + 1, total + weight)

        res = -float('inf')
        for i in range(n):
            dfs(i, 0, 0)

        if res == -float('inf'):
            return -1
        else:
            return res

# dfs hashing, take difference, don't know why its wrong: WA
class Solution:
    def maxWeight(self, n: int, edges: List[List[int]], k: int, t: int) -> int:
        if k == 0:
            return 0

        graph = defaultdict(list)
        for a, b, w in edges:
            graph[a].append((b, w))

        mp = defaultdict(int)
        stack = []

        def dfs(node, pathLen, total):
            nonlocal t, k
            if pathLen >= k:
                prevNode, prevTotal = stack[pathLen - k]
                if prevNode in mp:
                    return
                if total - prevTotal < t:
                    mp[prevNode] = max(total - prevTotal, mp[prevNode])
            for nxt, weight in graph[node]:
                stack.append((nxt, total + weight))
                dfs(nxt, pathLen + 1, total + weight)
                stack.pop()

        for i in range(n):
            if i not in mp:
                stack.append((i, 0))
                dfs(i, 0, 0)
                stack.pop()

        vals = mp.values()
        if len(vals) == 0:
            return -1
        else:
            return max(vals)

