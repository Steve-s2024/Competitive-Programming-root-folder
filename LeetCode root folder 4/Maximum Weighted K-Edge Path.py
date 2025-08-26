# who would think this can pass... 300*300*600 in worse case: 29%
# it turns out that due to the problem condition, the actual number of unique path possible is much less
# than 300*300*600 even in worst case. that's why this solution passed
class Solution:
    def maxWeight(self, n: int, edges: List[List[int]], k: int, t: int) -> int:
        graph = defaultdict(list)
        for u, v, w in edges: graph[u].append((v, w))

        @cache
        def recursive(node, k, tot):
            nonlocal n, t
            if k == 0: return 0
            res = -float('inf')
            for nxt, wei in graph[node]:
                a = recursive(nxt, k - 1, tot + wei) + wei
                if a + tot < t: res = max(a, res)
            return res

        res = max(recursive(i, k, 0) for i in range(n))
        return -1 if res == -float('inf') else res