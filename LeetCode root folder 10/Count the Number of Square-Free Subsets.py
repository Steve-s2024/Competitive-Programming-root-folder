# barely pass the memory limit, kinda intuitive bitmask dp. the idea mostly comes from the fact nums[i] <= 30
# and there is only 10 prime numbers <= 30
class Solution:
    def squareFreeSubsets(self, nums: List[int]) -> int:
        ref = {2:0, 3:1, 5:2, 7:3, 11:4, 13:5, 17:6, 19:7, 23:8, 29:9}
        mod = 10**9 + 7

        n = len(nums)
        mp = [1<<31]*n
        for i in range(n):
            x = nums[i]
            j = 2
            msk = 0
            while j < int(sqrt(x))+1 and x > 1:
                if x%j == 0:
                    msk |= 1<<ref[j]
                    x //= j
                if x%j == 0: break
                j += 1
            else:
                if x <= 1: mp[i] = msk
                elif msk&1<<ref[x] == 0: mp[i] = msk|1<<ref[x]
        # print(mp)
        @cache
        def fn(i, msk):
            if i >= n: return 1
            res = fn(i+1, msk)
            if mp[i] != 1<<31 and mp[i]&msk == 0: res += fn(i+1, msk|mp[i])
            return res % mod
        res = (fn(0, 0)-1)%mod
        fn.cache_clear()
        return res