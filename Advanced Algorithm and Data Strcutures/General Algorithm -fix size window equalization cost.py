# nlogn to find the cost to equalize all windows of size x by *atomic operation
# *atomic operation: increase/decrease element by 1


def findCost(nums, x):
    n = len(nums)
    sl = SortedList(nums[-x:])
    mp = [0] * n
    mp[n - x] = sl[x // 2]
    for i in range(n - x - 1, -1, -1):
        a, b = nums[i], nums[i + x]
        sl.add(a)
        sl.remove(b)
        mp[i] = sl[x // 2]

    sl = SortedList(nums[-x:])
    m = sl[x // 2]
    dp = [1<<63] * n
    t = sum(abs(e - m) for e in sl)
    dp[n - x] = t
    for i in range(n - x - 1, -1, -1):
        a, b = nums[i], nums[i + x]
        m, prv = mp[i], mp[i + 1]
        if m == prv:
            t += -abs(m - b) + abs(m - a)
        else:
            if m < prv:
                l = sl.bisect_left(prv)
                r = x - l
                d = prv - m
                t += -d * l + d * r
            else:
                l = sl.bisect_right(prv)
                r = x - l
                d = m - prv
                t += d * l - d * r
            t += -abs(m - b) + abs(m - a)
        dp[i] = t
        sl.add(a)
        sl.remove(b)
        return dp