# this is the most brute force solution i can come up with, how it did not hit TLE. it is not even close to TLE!
#: 400ms beats 64%

class Solution:
    @staticmethod
    def getFac(num):
        res = []
        for i in range(2, int(sqrt(num)) + 1):
            while num % i == 0:
                num //= i
                res.append(i)
        if num > 1: res.append(num)
        return res

    mp = {}

    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        if len(nums) == 1: return True
        cands = set()
        tmp = []
        for num in nums:
            if num == 1: return False
            if num not in cands:
                cands.add(num)
                tmp.append(num)
        nums = tmp

        graph = defaultdict(set)
        n = len(nums)
        mp = {}
        for i in range(n):
            fs = Solution.getFac(nums[i])
            mp[nums[i]] = fs
            for f in fs: graph[f].add(nums[i])

        vis = set()
        visF = set()

        def dfs(f):
            for nxt in graph[f]:
                vis.add(nxt)
                for nxtF in mp[nxt]:
                    if nxtF not in visF:
                        visF.add(nxtF)
                        dfs(nxtF)

        dfs(Solution.getFac(nums[0])[0])
        return len(vis) == len(nums)

