# interesting and kindda challenging Q3, I like this contest for the Q2 and Q3, very simple ideas but elegant
class Solution:
    def minIncrease(self, n: int, edges: List[List[int]], cost: List[int]) -> int:
        tree = defaultdict(list)
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)

        cnt = 0
        vis = set()

        def dfs(node):
            nonlocal cnt
            if len(tree[node]) == 1 and tree[node][0] in vis: return cost[node]
            arr = []
            for nxt in tree[node]:
                if nxt not in vis:
                    vis.add(nxt)
                    a = dfs(nxt)
                    arr.append(a)
            mx = max(arr)
            for num in arr:
                if num < mx: cnt += 1

            return mx + cost[node]

        vis.add(0)
        dfs(0)
        return cnt

