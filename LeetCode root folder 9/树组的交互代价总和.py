# 我靠这帮人搞得我很慌， 两道困难题被他们打成手速场
# 解出来两道hard才排~200， baozi 11 分钟all kill...
class Solution:
    def interactionCosts(self, n: int, edges: List[List[int]], group: List[int]) -> int:
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        def dfs(u, f):
            nonlocal ans
            CT, SM = 0, 0
            for v in g[u]:
                if vs[v]: continue
                vs[v] = 1
                ct, sm = dfs(v, f)
                ans += CT * sm + SM * ct
                CT += ct
                SM += sm
            if group[u] == f:
                CT += 1
                ans += SM
            return CT, SM + CT

        ans = 0
        st = set()
        for u, grp in enumerate(group):
            if grp in st: continue
            st.add(grp)
            vs = [0] * n
            vs[u] = 1
            dfs(u, grp)

        return ans