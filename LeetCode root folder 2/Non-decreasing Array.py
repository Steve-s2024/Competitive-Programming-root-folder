# easiest and most brainless solution, also the most efficient: 100%
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(1, n):
            if nums[i] - nums[i - 1] < 0:
                a, b = nums[i], nums[i - 1]
                nums[i] = b
                nums[i - 1] = b
                for j in range(1, n):
                    if nums[j] - nums[j - 1] < 0:
                        break
                else:
                    return True
                nums[i] = a
                nums[i - 1] = a
                for j in range(1, n):
                    if nums[j] - nums[j - 1] < 0:
                        break
                else:
                    return True
                return False
        return True


# translate the problem into judging if alter the current indexed element
# can make the array non-decreasing, with the help of suffix array
# it's quite hard to get everything right: 30%
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        inf = float('inf')
        n = len(nums)
        suffix = [-inf] * n
        suffix[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            if nums[i + 1] - nums[i] < 0:
                break
            suffix[i] = nums[i]

        for i in range(n):
            a = nums[i - 1] if i > 0 else -inf
            b = suffix[i + 1] if i < n - 1 else inf
            if a <= b and b != -inf:
                return True
            if i > 0 and nums[i] - nums[i - 1] < 0:
                return False

