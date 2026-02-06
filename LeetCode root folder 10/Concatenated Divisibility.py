# hah? i didn't even handle lexicographically smallest. how it worked?
# oh I see by lexicographically smallest it means separately not as a whole... sorting is suffice.
class Solution:
    def concatenatedDivisibility(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        n = len(nums)

        @cache
        def fn(msk, re):
            nonlocal k, n
            if msk == (1 << n) - 1: return re == 0
            for i in range(n):
                if msk & 1 << i: continue
                pw = pow(10, len(str(nums[i])))
                if fn(msk | 1 << i, (re * pw + nums[i]) % k): return True
            return False

        res = fn(0, 0)
        # print(res)
        ar = []
        msk, re = 0, 0
        while msk != (1 << n) - 1:
            for i in range(n):
                if msk & 1 << i: continue
                pw = pow(10, len(str(nums[i])))
                if fn(msk | 1 << i, (re * pw + nums[i]) % k):
                    msk, re = msk | 1 << i, (re * pw + nums[i]) % k
                    ar.append(nums[i])
                    break
            else:
                return []
        return ar

