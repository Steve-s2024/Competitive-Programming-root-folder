# the solution is targeted to the constraint palindrome size = 5: 74%
class Solution:
    def countPalindromes(self, s: str) -> int:
        n = len(s)
        mp = [[0] * 10 for _ in range(10)]
        frq = [0] * 10
        pre = []
        for i in range(n):
            for j in range(10):
                mp[j][int(s[i])] += frq[j]
            pre.append([mp[k][:] for k in range(10)])
            frq[int(s[i])] += 1

        mp = [[0] * 10 for _ in range(10)]
        frq = [0] * 10
        suf = []
        for i in range(n - 1, -1, -1):
            for j in range(10):
                mp[int(s[i])][j] += frq[j]
            suf.append([mp[k][:] for k in range(10)])
            frq[int(s[i])] += 1
        suf = suf[::-1]

        ans = 0
        MOD = 10 ** 9 + 7
        for i in range(2, n - 2):
            l, r = pre[i - 1], suf[i + 1]
            for j in range(10):
                for k in range(10):
                    ans += l[j][k] * r[k][j]
                    ans %= MOD
        return ans
