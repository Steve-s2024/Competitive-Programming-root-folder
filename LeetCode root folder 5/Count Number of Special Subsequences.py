# took me 5~10 minutes to solve it... its hard and reated 2100. unbelievable: 59%
class Solution:
    def countSpecialSubsequences(self, nums: List[int]) -> int:
        two, one, zero = 0, 0, 0
        MOD = 10**9 + 7
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == 2:
                two += two+1
                two %= MOD
            elif nums[i] == 1:
                one += one+two
                one %= MOD
            elif nums[i] == 0:
                zero += zero+one
                zero %= MOD
        return zero

