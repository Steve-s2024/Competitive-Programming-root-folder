# pretty straightforward bottom up tree summing solution, same as the old one,
# but it only takes me 5 minutes to realize the approach: 42%
class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:

        tree = defaultdict(list)
        for a, b in edges:
            tree[a].append(b)
            tree[b].append(a)

        vis = set()
        vis.add(0)

        def dfs(node):
            nonlocal k, cnt
            tot = values[node]
            for nxt in tree[node]:
                if nxt in vis: continue
                vis.add(nxt)
                tot += dfs(nxt)

            if tot % k == 0:
                # print(node)
                cnt += 1
            return tot

        cnt = 0
        dfs(0)
        return cnt
