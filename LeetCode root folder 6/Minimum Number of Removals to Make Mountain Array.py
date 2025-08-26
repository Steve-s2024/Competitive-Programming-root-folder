# got it, it is the same LIS approach, but with prefix and suffix arr to precompute result: 73%


class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        pre = [0] * n
        arr = []
        for i in range(n):
            res = 0
            l, r = 0, len(arr) - 1
            while l <= r:
                m = (l + r) // 2
                if arr[m] < nums[i]:
                    res = m + 1
                    l = m + 1
                else:
                    r = m - 1

            if res == len(arr): arr.append(nums[i])
            else:
                arr[res] = nums[i]
            pre[i] = res + 1

        suf = [0] * n
        arr = []
        for i in range(n-1, -1, -1):
            res = 0
            l, r = 0, len(arr) - 1
            while l <= r:
                m = (l + r) // 2
                if arr[m] < nums[i]:
                    res = m + 1
                    l = m + 1
                else:
                    r = m - 1
            if res == len(arr): arr.append(nums[i])
            else:
                arr[res] = nums[i]
            suf[i] = res + 1
        # print(pre)
        # print(suf)
        ans = inf
        for i in range(1, n - 1):
            if pre[i] > 1 and suf[i] > 1: ans = min(ans, n - pre[i] - suf[i] + 1)
        return ans

# trying DP, not 1D dp though
class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)

        def recursive(i, flag, prev):
            nonlocal n

            if i >= n: return 0 if not flag else inf
            res = recursive(i + 1, flag, prev) + 1
            if flag and nums[i] > prev:
                a = recursive(i + 1, flag, nums[i])
                b = recursive(i + 1, not flag, nums[i])
                res = min(a, b, res)
            elif not flag and nums[i] < prev:
                a = recursive(i + 1, flag, nums[i])
                res = min(a, res)

            return res

        return recursive(0, True, -inf)

# tried LIS but tle, but clearly everyone in the discussion is suggesting this solution. I don't know what happened
# now it is not accepted
class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)

        def lis(strt, end, inc):
            arr = []
            for i in range(strt, end, inc):
                res = 0
                l, r = 0, len(arr)-1
                while l <= r:
                    m = (l+r)//2
                    if arr[m] < nums[i]:
                        res = m+1
                        l = m+1
                    else: r = m-1
                if res == len(arr): arr.append(nums[i])
                else: arr[res] = nums[i]
                if i+inc == end: return res+1

        ans = inf
        for i in range(1, n - 1):
            a = lis(0, i+1, 1)
            b = lis(n-1, i-1, -1)
            if a > 1 and b > 1: ans = min(ans, n-a-b+1)
        return ans