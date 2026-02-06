# I fucked up the sortedlist, it is logn in query so the overhead just tle the solution, here is the exact same approach
# using sorted array and bisect method, passed under 1 sec...
class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        def helper(arr):
            st = {0}
            for v in arr:
                t = list(st)
                for e in t: st.add(e+v)
            return st
        ar = sorted(helper(nums[:n//2]))
        res = inf
        for x in helper(nums[n//2:]):
            i = bisect_left(ar, goal-x)
            if i < len(ar): res = min(res, abs(goal-x-ar[i]))
            if i: res = min(res, abs(goal-x-ar[i-1]))

        return res


# TLE
class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        sl = SortedList()

        def recursive(arr, i, sm):
            if i >= len(arr):
                sl.add(sm)
                return
            recursive(arr, i + 1, sm)
            recursive(arr, i + 1, sm + arr[i])

        recursive(nums[:n // 2], 0, 0)
        # print(sl)
        res = inf
        def dfs(arr, i, sm):
            nonlocal res
            if i >= len(arr):
                # sm+x is close to goal
                # goal-sm is close to x
                i1 = sl.bisect_left(goal - sm)
                i2 = sl.bisect_right(goal - sm)
                if i1 >= len(sl): i1 -= 1
                if i2 >= len(sl): i2 -= 1
                a = abs(goal - sm - sl[i1])
                b = abs(goal - sm - sl[i2])
                # print(sm, i1, i2)
                res = min(res, a, b)
                if i1: res = min(res, abs(goal - sm - sl[i1-1]))
                if i2 < len(sl)-1: res = min(res, abs(goal - sm - sl[i2+1]))
                return
            dfs(arr, i + 1, sm)
            dfs(arr, i + 1, sm + arr[i])

        dfs(nums[n // 2:], 0, 0)
        return res
