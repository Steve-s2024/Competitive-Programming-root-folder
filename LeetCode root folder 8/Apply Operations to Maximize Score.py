# hahaahhahhahahahhahahhaa lalalalalaallaa~~~~~
#
#@
# independently solved 2400 rated problem, within 30min. 2025/11/17
#
# for the first time, 2400.
# the testcases have shown mercy on my n*sqrt(n) solution. though I can easily make it n*logn after learned linear sieve

class Solution:
    def getCnt(self, n):
        f = 2
        cnt = 0
        while n and f < sqrt(n) + 1:
            res = 0
            while n % f == 0:
                n //= f
                res = 1
            cnt += res
            f += 1
        if n > 1: cnt += 1
        return cnt

    def maximumScore(self, nums: List[int], k: int) -> int:
        mod = 10 ** 9 + 7
        n = len(nums)
        arr = [self.getCnt(e) for e in nums]

        # print(arr)
        ri, le = [0] * n, [0] * n
        stk = []
        for i in range(n):
            while stk and stk[-1][0] < arr[i]: ri[stk.pop()[1]] = i
            stk.append((arr[i], i))
        while stk: ri[stk.pop()[1]] = n
        stk = []
        for i in range(n - 1, -1, -1):
            while stk and stk[-1][0] <= arr[i]: le[stk.pop()[1]] = i
            stk.append((arr[i], i))
        while stk: le[stk.pop()[1]] = -1

        # print(ri, le)
        tar = sorted([(nums[i], i) for i in range(n)], reverse=True)
        x = 1
        for e, i in tar:
            l, r = le[i], ri[i]
            mi = min((i-l)*(r-i), k)
            k -= mi
            # print(e, mi)
            x *= pow(e, mi, mod)
            x %= mod
            if k == 0: return x

        return 0

