# almost TLE, but the time comp is the same as the problem intended: 5%
class Solution:
    def minimumTime(self, s: str) -> int:
        n = len(s)

        suf = [[-1] * 2 for _ in range(n)]
        def forward(i, status):
            nonlocal n
            if i >= n: return 0
            if suf[i][status] != -1: return suf[i][status]
            if status:
                res = min(forward(i+1, status) + (2 if s[i] == '1' else 0), forward(i+1, 0)+1)
            else:
                res = forward(i+1, status) + 1
            suf[i][status] = res
            return res
        forward(0, 1)
        forward(0, 0)

        pre = [[-1] * 2 for _ in range(n)]
        def backward(i, status):
            if i < 0: return 0
            if pre[i][status] != -1: return pre[i][status]
            if status:
                res = min(backward(i-1, status) + (2 if s[i] == '1' else 0), backward(i-1, 0) + 1)
            else:
                res = backward(i-1, status) + 1
            pre[i][status] = res
            return res
        backward(n - 1, 1)
        backward(n - 1, 0)

        # print(pre)
        # print(suf)

        res = min(suf[0]+pre[-1])
        for i in range(n-1):
            a, b = pre[i]
            c, d = suf[i+1]
            res = min(res, a+c, a+d, b+c, b+d)
        return res