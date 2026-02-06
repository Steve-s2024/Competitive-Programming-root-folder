# the observation is not intuitive "window to collect bags will/(can be made) to rest on the head or tail of some block/interval"

class Solution:
    def maximumCoins(self, coins: List[List[int]], k: int) -> int:
        n = len(coins)
        coins.sort()
        pre = []
        t = 0
        for i in range(n):
            l, r, w = coins[i]
            t += (r - l + 1) * w
            pre.append(t)

        res = 0
        j = 0
        for i in range(n):
            _, r, _ = coins[i]
            l = r - k + 1
            while j < n and coins[j][1] < l: j += 1
            L, R, W = coins[j]
            x = min(R - l + 1, R - L + 1) * W
            sm = pre[i] - pre[j] + x
            # print(r, sm)
            res = max(res, sm)

        j = 0
        for i in range(n):
            l, _, _ = coins[i]
            r = l + k - 1
            while j < n - 1 and coins[j + 1][0] <= r: j += 1
            L, R, W = coins[j]
            x = min(r - L + 1, R - L + 1) * W
            sm = (pre[j - 1] if j else 0) - (pre[i - 1] if i else 0) + x
            res = max(res, sm)

        return res