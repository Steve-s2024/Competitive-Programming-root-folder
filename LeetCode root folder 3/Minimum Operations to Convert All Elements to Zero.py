# recursive solution: TLE
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        def recursive(l, r):
            # print(l, r)
            min_ = nums[l]
            max_ = nums[l]
            for i in range(l, r + 1):
                min_ = min(nums[i], min_)
                max_ = max(max_, nums[i])

            if min_ == max_:
                return 1

            res = 1
            L, R = l, l
            while R <= r:
                while R <= r and nums[R] != min_:
                    R += 1
                if L != R:
                    res += recursive(L, R - 1)
                L = R + 1
                R += 1
            return res

        res = recursive(0, len(nums) - 1)
        if min(nums) == 0:
            return res - 1
        else:
            return res


# its a monotonic stack question, I did a hell lot of complicated thought
# to convert the problem from brute force to recursion, and from recursion
# to monotonic stack. its a pain that I am not familiar with monotonic
# stack, but I manage to solve it relatively fast and solution worked with
# first try😁.

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # monotonic stack
        if min(nums) == 0:
            offset = 1
        else:
            offset = 0

        nums.append(-1)
        n = len(nums)
        stack = []
        res = 0
        for i in range(n):
            while stack and nums[i] < stack[-1]:
                cur = stack.pop()
                res += 1
                while stack and stack[-1] == cur:
                    stack.pop()
            stack.append(nums[i])

        return res - offset
