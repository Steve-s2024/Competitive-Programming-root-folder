# very interesting problem, doing a sliding window on tree
# while doing the DFS, the cap and dep argument behaves as the "left and right pointer", while the mp2 and stk also
# dynamically changes with the DFS movement.
class Solution:
    def longestSpecialPath(self, edges: List[List[int]], nums: List[int]) -> List[int]:
        n = len(nums)
        g = [[] for _ in range(n)]
        for u, v, w in edges:
            g[u].append((v, w))
            g[v].append((u, w))

        mx, ct = 0, inf
        mp = [0] * n
        mp2 = defaultdict(list)
        stk = []

        def dfs(u, p, cap, dep, sm):
            nonlocal mx, ct
            stk.append(u)
            mp[u] = sm
            ar = mp2[nums[u]]
            cap = max(cap, ar[-1] if ar else 0)
            ar.append(dep)
            l = dep - cap
            wsm = sm - mp[stk[-l]]
            # print(wsm, mx, l, ct)
            if wsm > mx: mx, ct = wsm, l
            if wsm == mx: ct = min(ct, l)

            for v, w in g[u]:
                if v == p: continue
                dfs(v, u, cap, dep + 1, sm + w)

            stk.pop()
            ar.pop()

        dfs(0, -1, 0, 1, 1)
        return [mx, ct]



