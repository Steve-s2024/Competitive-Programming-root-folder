# I had a misconception and bias against bitmask, with this question it correct me: 27%
class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        graph = defaultdict(list)
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                a, b = nums[i], nums[j]
                if a%b == 0 or b%a == 0:
                    graph[i].append(j)
                    graph[j].append(i)

        mask = 0
        dp = {}
        MOD = 10**9+7
        def dfs(i):
            nonlocal n, mask, MOD
            if (i, mask) in dp:
                return dp[(i, mask)]
            if mask == (1<<n)-1:
                return 1
            res = 0
            for j in graph[i]:
                if mask&(1<<j) == (1<<j):
                    continue
                mask ^= 1<<j
                res += dfs(j)
                mask ^= 1<<j
            res %= MOD
            dp[(i, mask)] = res
            return res

        res = 0
        for i in range(n):
            mask ^= 1<<i
            res += dfs(i)
            mask ^= 1<<i
        return res % MOD





# TLE, dfs solution
class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        graph = defaultdict(list)
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                a, b = nums[i], nums[j]
                if a%b == 0 or b%a == 0:
                    graph[a].append(b)
                    graph[b].append(a)


        # print(graph)
        vis = set()
        def dfs(node, cnt):
            nonlocal n
            if cnt >= n:
                return 1
            res = 0
            for nxt in graph[node]:
                if nxt in vis:
                    continue
                vis.add(nxt)
                res += dfs(nxt, cnt+1)
                vis.remove(nxt)
            return res

        res = 0
        for num in nums:
            vis.add(num)
            res += dfs(num, 1)
            vis.remove(num)
        return res