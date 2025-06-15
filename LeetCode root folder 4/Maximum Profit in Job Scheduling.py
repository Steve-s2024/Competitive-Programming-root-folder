# an optimized dp solution, it combined binary search to find the maximum dp state in logn time
# so the total time complexity is changed from n^2 to nlogn: 29%
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        dp = [(-1, 0)]
        mx = [0]
        max_ = 0
        n = len(startTime)
        arr = [(startTime[i], endTime[i], profit[i]) for i in range(n)]
        arr.sort(key=lambda i: i[1])
        for i in range(n):
            sta, end, pro = arr[i]
            l, r = 0, len(dp) - 1
            res = -1
            while l <= r:
                m = (l + r) // 2
                en, pr = dp[m]
                if en <= sta:
                    res = m
                    l = m + 1
                else:
                    r = m - 1
            # dp.append((end, pro+dp[res][1]))
            dp.append((end, pro + mx[res]))
            max_ = max(max_, dp[-1][1])
            mx.append(max_)

        # print(dp)
        return max(e[1] for e in dp)


#TLE
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        inter = [(startTime[i], endTime[i], profit[i]) for i in range(n)]
        inter.sort(key = lambda i:(i[0], i[1]))
        @cache
        def recursive(i):
            nonlocal n
            if i >= n-1:
                return 0
            res = 0
            for j in range(i+1, n):
                if inter[j][0] >= inter[i][1]:
                    a = recursive(j)+inter[j][2]
                    res = max(a, res)
            return res

        return max(recursive(i)+inter[i][2] for i in range(n))


