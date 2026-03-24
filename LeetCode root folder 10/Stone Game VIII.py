#

class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        n = len(stones)
        pre = [0]*n
        for i in range(n): pre[i] = pre[i-1] + stones[i]
        @cache
        def fn(i, f):
            if i == n-1: return 0 if not f else pre[i], 0 if f else pre[i]
            A, B = 0, 0
            if f:  # alice
                a, b = fn(i + 1, f)
                c, d = fn(i + 1, not f)
                if a - b >= c + pre[i] - d:
                    A, B = a, b
                else:
                    A, B = c+pre[i], d
            else:
                a, b = fn(i + 1, f)
                c, d = fn(i + 1, not f)
                if a - b <= c - d - pre[i]:
                    A, B = a, b
                else:
                    A, B = c, d+pre[i]
            return A, B

        a, b = fn(1, 1)
        return a-b