# BS & PIE, I can't believe I just wrote a PIE so easily, the whole function is 4 lines of code...
class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        @cache
        def recursive(i, LCM, x):
            nonlocal n, m
            if i >= n: return (m//LCM) if x%2 == 1 else -(m//LCM)
            return recursive(i+1, LCM, x) + recursive(i+1, lcm(LCM, coins[i]), x+1)

        res = -1
        n = len(coins)
        l, r = 0, min(coins)*k
        while l <= r:
            m = (l+r)//2
            x = 0
            for i in range(n): x += recursive(i+1, coins[i], 1)
            recursive.cache_clear()
            # print(m, x)
            if x >= k:
                res = m
                r = m-1
            else: l = m+1
        return res