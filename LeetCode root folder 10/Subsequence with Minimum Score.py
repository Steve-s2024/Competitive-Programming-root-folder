# BS + pre/suf recording

class Solution:
    def minimumScore(self, s: str, t: str) -> int:
        N, M = len(s), len(t)
        res = M
        l, r = 0, M - 1
        while l <= r:
            m = (l + r) // 2
            j = 0
            pre = [-1] * M
            for i in range(M - m):
                while j < N and s[j] != t[i]: j += 1
                if j >= N: break
                pre[i] = j
                j += 1

            suf = [-1] * M
            j = N - 1
            for i in range(M - 1, m - 1, -1):
                while j >= 0 and s[j] != t[i]: j -= 1
                if j < 0: break
                suf[i] = j
                j -= 1

            # print(m, pre, suf)
            f = pre[M - 1 - m] != -1 or suf[m] != -1
            for i in range(M - m - 1):
                if pre[i] != -1 and suf[i + m + 1] != -1 and pre[i] < suf[i + m + 1]:
                    f = 1
                    break

            if f:
                res = m
                r = m - 1
            else:
                l = m + 1
        return res

