# pretty good dfs question, key point is to find the target to iterate through (which is each node), and notice that
# maintaining the correct guess when shifting candidate root node from one to another adjacent node only take O(1) time
#: 33%
class Solution:
    def rootCount(self, edges: List[List[int]], guesses: List[List[int]], k: int) -> int:
        st = set((u, v) for u, v in guesses)

        tree = defaultdict(list)
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)

        vis = set()
        cnt = 0

        def dfs(u):
            nonlocal cnt
            for v in tree[u]:
                if v in vis: continue
                if (u, v) in st: cnt += 1
                vis.add(v)
                dfs(v)

        vis.add(0)
        dfs(0)

        vis2 = set()
        ans = 0

        def dfs2(u):
            nonlocal ans, cnt
            if cnt >= k: ans += 1
            for v in tree[u]:
                if v in vis2: continue

                if (u, v) in st: cnt -= 1
                if (v, u) in st: cnt += 1
                vis2.add(v)
                dfs2(v)
                if (u, v) in st: cnt += 1
                if (v, u) in st: cnt -= 1

        vis2.add(0)
        dfs2(0)

        return ans