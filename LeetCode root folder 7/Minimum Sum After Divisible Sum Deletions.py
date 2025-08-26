# took half of my life away, sometimes i wonder why keep doing contest. hey...
class Solution:
    def minArraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pre = []
        tot = 0
        mp = defaultdict(list)
        for i, num in enumerate(nums):
            tot += num
            pre.append(tot % k)
            mp[tot % k].append(i)

        @cache
        def recursive(i):
            nonlocal n
            if i >= n: return 0
            res = recursive(i + 1) + nums[i]
            if i:
                arr = mp[pre[i-1]]
                idx = -1
                l, r = 0, len(arr) - 1
                while l <= r:
                    m = (l + r) // 2
                    if arr[m] > i-1:
                        idx = m
                        r = m - 1
                    else:
                        l = m + 1
                if idx != -1:
                    a = recursive(arr[idx]+1)
                    res = min(res, a)
            return res

        res = recursive(0)
        for i in mp[0]:
            a = recursive(i + 1)
            res = min(a, res)
        return res
