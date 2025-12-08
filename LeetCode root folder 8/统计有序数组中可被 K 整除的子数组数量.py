# 卧槽Q4搞我心态， 直接坠机。 本来前三题排在了前三十， 第四题直接wa 4次排名估计得250开外。


class Solution:
    def numGoodSubarrays(self, nums: List[int], k: int) -> int:
        cp = nums[:]
        n = len(nums)
        nums = [e % k for e in nums]
        mp = defaultdict(int)
        mp[0] = 1
        tot = 0
        res = 0
        for i in range(n):
            tot += nums[i]
            res += mp[tot % k]
            mp[tot % k] += 1

        arr = []
        all = []
        for i in range(n):
            if i and cp[i] != cp[i - 1]:
                all.append(arr)
                arr = []
            arr.append(cp[i])

        all.append(arr)
        for val in all:
            m = len(val)
            size = 0
            tot = 0
            for v in val:
                tot += v
                size += 1
                if tot % k == 0: break
            ct = 1
            while ct * size <= m:
                res -= m - ct * size + 1
                res += 1
                ct += 1

        return res