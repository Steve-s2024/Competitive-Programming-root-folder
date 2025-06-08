# nested knap-sack, STILL TLE! @cache or customized DP array
class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        n = len(prices)
        dp = [[[-1] * (k + 1) for _ in range(n)] for _ in range(n)]

        def recursive(i, buy, k):
            nonlocal n

            if i >= n or k <= 0:
                return 0
            if dp[i][buy][k] != -1:
                return dp[i][buy][k]
            res = -float('inf')
            if buy != -1:
                a = recursive(i + 1, -1, k - 1) + abs(prices[i] - prices[buy])
                b = recursive(i + 1, buy, k)
            else:
                a = recursive(i + 1, i, k)
                b = recursive(i + 1, -1, k)
            res = max(a, b)
            dp[i][buy][k] = res
            return res

        return recursive(0, -1, k)

# there is no way to make this recursion better: TLE
class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        n = len(prices)

        @cache
        def recursive(i, k):
            nonlocal n
            if i >= n or k <= 0:
                return 0
            res = -float('inf')
            prefix = {}
            mx, mi = prices[i], prices[i]
            for j in range(i + 1, n):
                prefix[j] = (mx, mi)
                mx, mi = max(mx, prices[j]), min(mi, prices[j])
            # print(prefix)
            for j in range(i + 1, n):
                mx, mi = prefix[j]
                b = max(mx - prices[j], prices[j] - mi)
                a = recursive(j + 1, k - 1) + b
                res = max(res, a, b)
            return res

        return recursive(0, k)




# TLE
class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        n = len(prices)

        @cache
        def recursive(i, k):
            nonlocal n
            if i >= n or k <= 0:
                return 0

            res = -float('inf')
            MX = MI = prices[i]
            for i1 in range(i, n):
                if prices[i1] in range(MI + 1, MX):
                    continue
                MX = max(prices[i], MX)
                MI = min(prices[i], MI)

                mx = mi = prices[i1]
                for i2 in range(i1 + 1, n):
                    if mx < prices[i2]:
                        mx = prices[i2]
                        a, b = prices[i1], prices[i2]
                        t = recursive(i2 + 1, k - 1) + b - a
                        res = max(t, b - a, res)

                    if mi > prices[i2]:
                        mi = prices[i2]
                        a, b = prices[i1], prices[i2]
                        t = recursive(i2 + 1, k - 1) + a - b
                        res = max(t, a - b, res)

            return res

        return recursive(0, k)





# TLE
class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        n = len(prices)

        @cache
        def recursive(i, k):
            nonlocal n
            if i >= n or k <= 0:
                return 0

            res = -float('inf')
            for i1 in range(i, n):
                for i2 in range(i1 + 1, n):
                    a, b = prices[i1], prices[i2]
                    t = recursive(i2 + 1, k - 1) + abs(a - b)
                    t2 = recursive(n, k) + abs(a - b)
                    res = max(t, t2, res)
            return res

        return recursive(0, k)


