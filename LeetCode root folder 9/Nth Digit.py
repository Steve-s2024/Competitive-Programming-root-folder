# the 400th problem, binary search with a twist.
# not too interesting nor boring


class Solution:
    def findNthDigit(self, n: int) -> int:
        l, r = 1, 1 << 32
        while l <= r:
            m = (l + r) // 2
            t = 0
            x = 10
            d = 1
            while x < m:
                t += (x - x // 10) * d
                x *= 10
                d += 1
            t += d * (m - x // 10)
            if n in range(t + 1, t + len(str(m)) + 1):  # the current number
                # print(m, t)
                return int(str(m)[n - t - 1])
            elif n < t + 1:
                r = m - 1
            else:
                l = m + 1
