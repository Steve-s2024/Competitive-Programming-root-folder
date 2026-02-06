# holy smoke in another 10 times I would not though this could work!
# my survival instinct come save the day with this brilliant yet very not perfect gamble of optimization by luck
# this new technique/discovery could really mean something

# imagine doing one DFS on tree, and for each node visit in DFS we call one dfs on the subtree rooted on that node
# this algo is easily proven O(n^2)
#
# in contrast, is this idea (in abstract term):  "for each node we visit in a tree, we visit all of its subtree nodes
# except for the largest subtree nodes."
# we can assume approximate nlogn (definitely less than n^2 if not nlogn) time performance for this algo

class Solution:
    def smallestMissingValueSubtree(self, ps: List[int], nums: List[int]) -> List[int]:
        n = len(nums)
        g = [[] for _ in range(n)]
        for u, v in enumerate(ps):
            if u: g[v].append(u)
        ans = [0]*n
        def dfs(u):
            if not g[u]:
                sl = SortedList()
                sl.add(nums[u])
                ans[u] = 1 if nums[u] != 1 else 2
                return sl
            mp = defaultdict(list)
            mx = 0
            for v in g[u]:
                sl = dfs(v)
                mp[len(sl)].append(sl)
                mx = max(mx, len(sl))
            sl = mp[mx].pop()
            for a in mp.values():
                for SL in a:
                    for v in SL: sl.add(v)
            sl.add(nums[u])
            # print(sl)

            res = -1
            if sl[0] != 1: ans[u] = 1
            else:
                l, r = 2, len(sl)
                while l <= r:
                    m = (l+r)//2
                    j = sl.bisect_left(m)
                    if j != m-1 or sl[j] != m:
                        res = m
                        r = m-1
                    else: l = m+1
                if res == -1: res = len(sl)+1
                ans[u] = res
            return sl

        dfs(0)
        return ans