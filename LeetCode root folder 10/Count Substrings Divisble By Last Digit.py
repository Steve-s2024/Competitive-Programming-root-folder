# unbelievable, end up with discussing cases... the one thing I don't believe LeetCode will do

class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)

        def helper(k):
            nonlocal n
            suf = [0] * n
            x = 1
            re = 0
            for i in range(n - 1, -1, -1):
                re += int(s[i]) * x
                re %= k
                suf[i] = re
                x *= 10
                x %= k
            frq = defaultdict(int)
            res = 0
            if k == 7: print(suf)
            for i in range(n):
                frq[suf[i]] += 1
                if s[i] == str(k) or (k == 3 and s[i] == '6'):
                    for x in range(k):
                        t = k + x - (suf[i + 1] if i < n - 1 else 0)
                        if t % k == 0: res += frq[x]
            return res

        res = 0
        for k in [1, 3, 7, 9]:
            a = helper(k)
            # print(k, a)
            res += a

        for i in range(n):
            if s[i] in '25': res += i + 1
            if s[i] == '4':
                res += 1
                if i and s[i - 1] in '02468': res += i
            if s[i] == '8':
                res += 1
                if i and s[i - 1] in '048': res += 1
                if i > 1 and int(s[i - 2] + s[i - 1]) % 4 == 0: res += i - 1
        return res