# feels very similar to a div2 C
# 11ms beats 98% 😱
class Solution:
    def earliestSecondToMarkIndices(self, nums: List[int], ci: List[int]) -> int:
        n, m = len(nums), len(ci)
        l, r = 0, m-1
        res = -1
        while l <= r:
            M = (l+r)//2
            vs = set()
            f = 1
            x = 0
            for i in range(M, -1, -1):
                if ci[i] in vs:
                    x = max(x-1, 0)
                    continue
                if i+1-x - (n-len(vs)) < nums[ci[i]-1]:
                    # if M == 7
                    f = 0
                    break
                x += nums[ci[i]-1]
                vs.add(ci[i])
            if f and len(vs) == n:
                res = M
                r = M-1
            else: l = M+1
        if res == -1: return -1
        return res+1