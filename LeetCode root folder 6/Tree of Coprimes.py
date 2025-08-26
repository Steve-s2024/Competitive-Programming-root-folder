# pretty tough implementation: 32%
class Solution:
    def __init__(self):
        mp = defaultdict(set)
        for i in range(50):
            for j in range(50):
                if gcd(i + 1, j + 1) == 1:
                    mp[i + 1].add(j + 1)
        self.mp = mp

    def getCoprimes(self, nums: List[int], edges: List[List[int]]) -> List[int]:
        mp = self.mp

        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        n = len(nums)
        ans = [-1] * n
        cand = defaultdict(list)

        def dfs(parent, node, dep):
            val = nums[node]
            mx = -1
            for i in range(1, 51):
                if i in mp[val] and cand[i]:
                    if cand[i][-1][1] > mx:
                        mx = cand[i][-1][1]
                        ans[node] = cand[i][-1][0]

            cand[val].append((node, dep))
            for nxt in graph[node]:
                if nxt == parent: continue
                dfs(node, nxt, dep + 1)
            cand[val].pop()

        dfs(-1, 0, 0)
        return ans

