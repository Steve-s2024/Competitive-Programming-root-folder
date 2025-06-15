# binary search and greedy solution: 55%
class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        n = len(price)
        price.sort()
        l, r = 0, price[-1] - price[0]
        maxTaste = 0
        while l <= r:
            m = (l + r) // 2
            prev = price[0]
            cnt = 1
            for i in range(1, n):
                if price[i] - prev >= m:
                    cnt += 1
                    prev = price[i]

            if cnt >= k:
                maxTaste = m
                l = m + 1
            else:
                r = m - 1
        return maxTaste


