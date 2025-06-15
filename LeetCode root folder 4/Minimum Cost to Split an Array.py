# not that hard DP solution:22%

class Solution:
    def minCost(self, nums: List[int], k: int) -> int:
        n = len(nums)

        @cache
        def recursive(i):
            nonlocal n, k
            if i >= n:
                return 0
            res = float('inf')
            cost = k
            mp = defaultdict(int)
            for j in range(i, n):
                mp[nums[j]] += 1
                if mp[nums[j]] == 2:
                    cost += 2
                elif mp[nums[j]] > 2:
                    cost += 1
                res = min(res, recursive(j + 1) + cost)

            return res

        return recursive(0)