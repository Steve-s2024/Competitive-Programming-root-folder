# knapsack 89%
class Solution:
    def minArraySum(self, nums: List[int], k: int, op1: int, op2: int) -> int:
        n = len(nums)

        @cache
        def recursive(i, op1, op2):
            if i >= n: return 0
            res = recursive(i + 1, op1, op2) + nums[i]
            if op1:
                a = recursive(i + 1, op1 - 1, op2) + ceil(nums[i] / 2)
                res = min(a, res)
            if op2 and nums[i] >= k:
                a = recursive(i + 1, op1, op2 - 1) + nums[i] - k
                res = min(a, res)
            if op1 and op2:
                if ceil(nums[i] / 2) >= k:
                    a = recursive(i + 1, op1 - 1, op2 - 1) + ceil(nums[i] / 2) - k
                    res = min(a, res)
                elif nums[i] >= k:
                    a = recursive(i + 1, op1 - 1, op2 - 1) + ceil((nums[i] - k) / 2)
                    res = min(a, res)
            return res

        return recursive(0, op1, op2)


