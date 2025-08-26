# stupid constraint, if this complexity is intended then make n <= 10000 at least, got me worried for the whole
# time of TLE: 51%
class Solution:
    @staticmethod
    def getFacs(x):
        res = []
        for i in range(2, int(math.sqrt(x)) + 1):
            while x % i == 0:
                x //= i
                res.append(i)
        if x > 1: res.append(x)
        return res

    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        if len(nums) == 1: return True
        if 1 in nums: return False
        n = len(nums)
        graph = defaultdict(set)
        for i in range(n):
            fs = Solution.getFacs(nums[i])
            for f in fs: graph[f].update(set(fs))

        begin = list(graph.keys())[0]
        vis = set()

        def dfs(node):
            for nxt in graph[node]:
                if nxt not in vis:
                    vis.add(nxt)
                    dfs(nxt)

        vis.add(begin)
        dfs(begin)
        return len(vis) == len(graph)


# failed attempt
class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        if len(nums) == 1: return True

        st = set(nums)
        if 1 in st: return False
        mx = max(st)
        graph = defaultdict(list)
        for key in st:
            for j in range(key * 2, mx + key + 1, key):
                if j in st:
                    u, v = key, j
                    graph[u].append(v)
                    graph[v].append(u)

        vis = set()

        def dfs(node):
            for nxt in graph[node]:
                if nxt in vis: continue
                vis.add(nxt)
                dfs(nxt)

        vis.add(nums[0])
        dfs(nums[0])
        return len(vis) == len(st)