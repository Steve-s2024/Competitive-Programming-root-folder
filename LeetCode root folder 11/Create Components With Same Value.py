# sometimes I just shocked how fast I can come up with correct idea and implement it. 2460 is nothing difficult
class Solution:
    def componentValue(self, nums: List[int], edges: List[List[int]]) -> int:
        sm = sum(nums)
        n = len(nums)
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        def dfs(u, p, x):
            sm = nums[u]
            for v in g[u]:
                if v == p: continue
                tsm = dfs(v, u, x)
                if tsm == inf: return inf
                sm += tsm
            if sm > x: return inf
            if sm == x: return 0
            return sm

        f = []
        for i in range(sm, 0, -1):
            if sm % i == 0 and dfs(0, -1, sm // i) == 0: return i - 1


