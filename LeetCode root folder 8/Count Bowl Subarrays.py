# nice, back to the winner's column. an interesting monotonic stack question as a Q3 that requires a lot good
# observations
class Solution:
    def bowlSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        stk = []
        res = 0
        for i in range(n):
            while stk and stk[-1][0] < nums[i]:
                if stk.pop()[1] == i-1: continue
                print(1, i)
                res += 1
            stk.append((nums[i], i))

        stk = []
        for i in range(n-1, -1, -1):
            while stk and stk[-1][0] < nums[i]:
                if stk.pop()[1] == i+1: continue
                res += 1
            stk.append((nums[i], i))
        return res