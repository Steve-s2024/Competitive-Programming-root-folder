# dp solution, apparently there is a greedy solution that runs in 0ms: 2300ms beats 18%
class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        @cache
        def recursive(i, k, f):
            if i >= n: return 1 if k == 0 else 0

            res = recursive(i+1, k, f)
            if k and not f: res += recursive(i+1, k, not f)
            if f: res += recursive(i, k-1, not f)

            return res % MOD
        return recursive(0, k, 0)


# here is the 0ms version, hehe...
class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        return comb(n + k - 1, 2 * k) % 1_000_000_007