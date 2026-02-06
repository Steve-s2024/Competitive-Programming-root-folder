# convert to using two bit masks to replace the tuple, halved the run time
class Solution:
    def maximumANDSum(self, nums: List[int], numSlots: int) -> int:
        n = len(nums)
        m = numSlots

        @cache
        def recursive(i, msk1, msk2):
            nonlocal n
            if i >= n: return 0
            res = 0
            for j in range(m):
                if 1<<j & msk2: continue
                if 1<<j & msk1: a = recursive(i + 1, msk1, 1<<j|msk2) + ((j + 1) & nums[i])
                else: a = recursive(i + 1, 1<<j|msk1, msk2) + ((j + 1) & nums[i])
                res = max(res, a)
            # print(i, msk, res)
            return res

        return recursive(0, 0, 0)


# maybe able to do it with bit-mask, two bitmask to replace the tuple in the dp state
# O(numSlots*3^n)
class Solution:
    def maximumANDSum(self, nums: List[int], numSlots: int) -> int:
        n = len(nums)
        m = numSlots

        @cache
        def recursive(i, msk):
            nonlocal n
            if i >= n: return 0
            nw = list(msk)
            res = 0
            for j in range(m):
                if msk[j] == 2: continue
                nw[j] += 1
                a = recursive(i + 1, tuple(nw)) + ((j + 1) & nums[i])
                res = max(res, a)
                nw[j] -= 1
            # print(i, msk, res)
            return res

        return recursive(0, tuple([0] * m))
