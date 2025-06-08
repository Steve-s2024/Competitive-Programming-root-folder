# interval checking and binary search solution: 25%
# brain melting down...
class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        n = len(nums)
        mp = defaultdict(int)

        arr = []
        for i in range(n // 2):
            a, b = nums[i], nums[n - i - 1]
            # 0 <= a + key <= k OR 0 <= a - key <= k
            # -a <= key <= k-a OR a >= key >= a-k
            # so, if key not in [-a, k-a] or [a-k, a], and key not in [-b, k-b] or [b-k, b], and key is not
            # abs(a-b), we will have to change both a and b.
            # otherwise, we only need to change one of a and b
            # otherwise, a and b don't need to be changed
            # so, if key in (0, max(k-b, b, k-a, a)), only one need to be changed
            arr.append(max(k - b, b, k - a, a))
            mp[abs(a - b)] += 1
        arr.append(float('inf'))
        arr.sort()
        print(arr)
        res = n

        def binarySearch(tar):
            l, r = 0, n // 2 - 1
            res = 0
            while l <= r:
                m = (r + l) // 2
                mid = arr[m]
                if mid < tar:
                    l = m + 1
                else:
                    res = m
                    r = m - 1
            # print('binary search', tar, n//2 - res)
            return n // 2 - res

        for key in mp:
            ones = binarySearch(key) - mp[key]
            # print(key, ones)
            twos = n // 2 - mp[key] - ones
            cost = 2 * twos + ones
            res = min(res, cost)
        return res


# brute force: TLE
class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        mp = defaultdict(int)
        n = len(nums)
        for i in range(n // 2):
            diff = abs(nums[i] - nums[n - i - 1])
            mp[diff] += 1
        # print(mp)
        res = n
        for key in mp:
            cnt = 0
            for i in range(n // 2):
                a, b = nums[i], nums[n - i - 1]
                diff = abs(a - b)
                if diff != key:
                    if (
                            a + key in range(k+1) or a - key in range(k+1) or
                            b + key in range(k+1) or b - key in range(k+1)
                    ):
                        cnt += 1
                    else:
                        cnt += 2
            # print(key, cnt)
            res = min(res, cnt)
        return res