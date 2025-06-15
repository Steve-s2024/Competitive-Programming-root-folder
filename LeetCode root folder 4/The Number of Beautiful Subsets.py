# interesting fact, this worked while the @cache attempt (meant to be faster)
# didn't work due to MLE: 17%
class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        n = len(nums)
        bitmask = 0
        dp = {}
        def recursive(i):
            nonlocal n, bitmask
            if (i, bitmask) in dp:
                return dp[(i, bitmask)]
            if i >= n:
                return 1

            res = recursive(i+1)
            flag = True
            cur = nums[i]
            for idx, num in enumerate(nums):
                if abs(cur-num) == k and (bitmask&(1<<idx)==1<<idx):
                    flag = False
                    break
            if flag:
                bitmask ^= 1<<i
                res += recursive(i+1)
                bitmask ^= 1<<i
            dp[(i, bitmask)] = res
            return res
        return recursive(0)-1