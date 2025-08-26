

# optimized 1D dp with un-bounded knap-sack: 48%
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        @cache
        def recursive(i):
            nonlocal n
            if i >= n: return 0
            res = inf
            for d, c in zip([1, 7, 30], costs):
                j = i+1
                while j < n and days[j] <= days[i]+d-1: j += 1
                res = min(res, recursive(j) + c)
            return res
        return recursive(0)

# 2D dp with kanp-sack: 7.8%
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)

        @cache
        def recursive(i, cur):
            nonlocal n
            if i >= n: return 0
            if days[i] <= cur: return recursive(i + 1, cur)

            return min(
                recursive(i, days[i]) + costs[0],
                recursive(i, days[i] + 6) + costs[1],
                recursive(i, days[i] + 29) + costs[2]
            )

        return recursive(0, 0)
