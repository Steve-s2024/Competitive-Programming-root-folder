# goddamnit hard

# a new template build. nlogn to find the result of such O(n^2logn) algorithm
# [sum((median-e) for e in range(i, x)) for i in range(n-x)]


class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)
        sl = SortedList(nums[-x:])
        mp = [0]*n
        mp[n-x] = sl[x//2]
        for i in range(n-x-1, -1, -1):
            a, b = nums[i], nums[i+x]
            sl.add(a)
            sl.remove(b)
            mp[i] = sl[x//2]

        sl = SortedList(nums[-x:])
        m = sl[x//2]
        dp = [0]*n
        t = sum(abs(e - m) for e in sl)
        dp[n - x] = t
        # print(mp)
        for i in range(n - x - 1, -1, -1):
            a, b = nums[i], nums[i + x]
            m, prv = mp[i], mp[i+1]
            if m == prv: t += -abs(m-b) + abs(m-a)
            else:
                if m < prv:
                    l = sl.bisect_left(prv)
                    r = x-l
                    d = prv-m
                    t += -d*l + d*r
                else:
                    l = sl.bisect_right(prv)
                    r = x-l
                    d = m-prv
                    # print('?', l, r, d)
                    t += d*l - d*r
                t += -abs(m - b) + abs(m - a)
            # print(a, b, t)
            dp[i] = t
            sl.add(a)
            sl.remove(b)
        # print(dp)

        DP = [[1<<40] * (k + 1) for _ in range(n + 1)]
        for i in range(n+1): DP[i][k] = 0
        for i in range(n - x, -1, -1):
            for t in range(k):
                DP[i][t] = min(DP[i + 1][t], DP[i + x][t + 1] + dp[i])
        return DP[0][0]
        # @cache
        # def fn(i, t):
        #     if i >= n-x+1: return 0 if t == k else 1<<31
        #
        #     a = fn(i+1, t)
        #     b = fn(i+x, t+1) + dp[i]
        #     return min(b, a)
        # return fn(0, 0)






