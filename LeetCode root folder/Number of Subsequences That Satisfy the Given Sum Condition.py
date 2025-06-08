# nested loop solution: TLE

'''class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = 0
        for i in range(len(nums)):
            cur = 0
            for j in range(i, len(nums)):
                if nums[i] + nums[j] > target:
                    break
                cur = pow(2, j-i)
            res += cur

        return res % (pow(10, 9) + 7)'''


# theoretically valid, but some time the result of the pow() is too large that python can't handle
'''class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = 0
        l, r = 0, 0
        while r < len(nums) and nums[l] + nums[r] <= target:
            r += 1
        r = min(r, len(nums) - 1)

        while True:
            while r >= 0 and nums[l] + nums[r] > target:
                r -= 1
            if l > r:
                break
            res += pow(2, r - l)
            l += 1

        return res % (pow(10, 9) + 7)'''


# now with a tiny adjust, it worked like charm:
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = 0
        l, r = 0, 0
        while r < len(nums) and nums[l] + nums[r] <= target:
            r += 1
        r = min(r, len(nums) - 1)

        while l <= r:
            while r >= 0 and nums[l] + nums[r] > target:
                r -= 1
            if l > r:
                break
            res %= (pow(10, 9) + 7)
            res += pow(2, r - l)
            l += 1

        return res % (pow(10, 9) + 7)

