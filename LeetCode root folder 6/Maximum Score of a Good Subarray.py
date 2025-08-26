# so not fast, not cool! : 7%
class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pre = [0] * n
        stk = []
        for i in range(n):
            while stk and stk[-1][0] > nums[i]:
                _, j = stk.pop()
                pre[j] = i - 1
            stk.append((nums[i], i))
        while stk:
            _, j = stk.pop()
            pre[j] = n - 1

        suf = [0] * n
        for i in range(n - 1, -1, -1):
            while stk and stk[-1][0] > nums[i]:
                _, j = stk.pop()
                suf[j] = i + 1
            stk.append((nums[i], i))
        while stk:
            _, j = stk.pop()
            suf[j] = 0
        res = 0
        for i in range(n):
            if pre[i] < k or suf[i] > k: continue
            res = max(res, nums[i] * (pre[i] - suf[i] + 1))
        return res