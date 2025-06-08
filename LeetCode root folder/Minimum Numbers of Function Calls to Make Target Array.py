# greedy solution, counting number of 1 bit in binary representation:314
# ms
# Beats
# 59.41%
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res = 0
        maxLen = 0
        for num in nums:
            cur = bin(num)[2:]
            maxLen = max(maxLen, len(cur))
            res += Counter(cur)['1']
        return res + maxLen - 1