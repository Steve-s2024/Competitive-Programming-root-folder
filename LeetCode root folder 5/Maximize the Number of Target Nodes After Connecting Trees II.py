# easy hard: 15%
class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:

        tree1, tree2 = defaultdict(list), defaultdict(list)
        for u, v in edges1:
            tree1[u].append(v)
            tree1[v].append(u)
        for u, v in edges2:
            tree2[u].append(v)
            tree2[v].append(u)

        vis = set()
        g1, g2 = [0], [0]
        mp = {}

        def dfs(node, dep):
            if dep % 2 == 0:
                mp[node] = g1
                g1[0] += 1
            else:
                mp[node] = g2
                g2[0] += 1

            for nxt in tree1[node]:
                if nxt in vis: continue
                vis.add(nxt)
                dfs(nxt, dep + 1)

        vis.add(0)
        dfs(0, 0)

        cnt1, cnt2 = 0, 0
        vis.clear()

        def dfs2(node, dep):
            nonlocal cnt1, cnt2
            if dep % 2 == 0:
                cnt1 += 1
            else:
                cnt2 += 1
            for nxt in tree2[node]:
                if nxt in vis: continue
                vis.add(nxt)
                dfs2(nxt, dep + 1)

        vis.add(0)
        dfs2(0, 0)
        mx = max(cnt1, cnt2)
        n = len(edges1) + 1
        ans = [0] * n
        for i in range(n):
            ans[i] = mp[i][0] + mx
        return ans