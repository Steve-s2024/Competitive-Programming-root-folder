# exclude the time to read the question, it only took me 10 minutes to solve. the intuition is pretty clear right
# away. doesn't feel like a 2300 rated question:  43%
class Solution:
    def minEdgeReversals(self, n: int, edges: List[List[int]]) -> List[int]:
        tree = defaultdict(list)
        for u, v in edges:
            tree[u].append((v, 0))
            tree[v].append((u, 1))

        def dfs(node, par):
            res = 0
            for nxt, drct in tree[node]:
                if nxt != par: res += dfs(nxt, node) + drct
            return res

        tot = dfs(0, -1)
        ans = [0]*n

        def dfs2(node, par, cnt, dep):
            ans[node] = tot-cnt + dep-cnt
            for nxt, drct in tree[node]:
                if nxt != par:
                    dfs2(nxt, node, cnt+drct, dep+1)
        dfs2(0, -1, 0, 0)
        return ans