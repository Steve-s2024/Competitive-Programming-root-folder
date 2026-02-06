# can't believe is this easy, the problem can be translated to find two nodes other than root, detach the subtrees
# rooted by those two node -> will get three smaller trees. compute the xor of three trees and define score as max(xor)-min(xor)
# simply brute force over all such pair of nodes and precompute their subtree xor value.

class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        n = len(nums)
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        mp = [0]*n
        cd = defaultdict(set)
        stk = []
        def dfs(u, p):
            res = nums[u]
            for w in stk: cd[w].add(u)
            for v in g[u]:
                if v == p: continue
                stk.append(u)
                res ^= dfs(v, u)
                stk.pop()
            mp[u] = res
            return res
        dfs(0, -1)
        print(mp)
        # print(cd)


        res = inf
        for u1 in range(1, n):
            for u2 in range(u1+1, n):
                if u1 in cd[u2]:
                    a, b, c = mp[0]^mp[u2], mp[u2]^mp[u1], mp[u1]
                elif u2 in cd[u1]:
                    a, b, c = mp[0]^mp[u1], mp[u1]^mp[u2], mp[u2]
                else:
                    a, b, c = mp[0]^mp[u2]^mp[u1], mp[u2], mp[u1]
                res = min(res, max(a, b, c)-min(a, b, c))
        return res



