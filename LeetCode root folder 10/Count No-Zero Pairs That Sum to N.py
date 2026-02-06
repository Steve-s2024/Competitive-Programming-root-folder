# kept thinking about greedy strategy and figuring out the induction transition
# but solved via digit dp
class Solution:
    def countNoZeroPairs(self, n: int) -> int:
        s = str(n)
        m = len(s)
        @cache
        def fn(i, cf, bf1, bf2):
            nonlocal m
            if i >= m: return 1 if not cf and not bf1 and not bf2 else 0
            res = 0
            x = int(s[i])
            if cf: x += 10
            for j in range(10):
                for k in range(10):
                    if j == 0 and not bf1: continue
                    if k == 0 and not bf2: continue
                    if j+k == x: res += fn(i+1, 0, bf1 and j==0, bf2 and k==0)
                    if j+k == x-1: res += fn(i+1, 1, bf1 and j==0, bf2 and k==0)
            return res
        return fn(0, 0, 1, 1)
