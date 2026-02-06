# never trust leetcode again, freaking the thing make me TLE by using 10**18 + 3 is not the big number itself
# it is because every testcases re-instantiate the freaking Solution class. so every time new array of size 10**4 is created
# I simply changed the size of that precomputed array to match the current input, and it passed all testcases
# this solution is not perfect though, for bigger input we likely need bigger mod (> 10**18 + 3) to keep it on track
class Solution:
    def helper(self, n):
        mod = 10 ** 18 + 3
        # mod = 10**9 + 7
        fac = [1] * n
        inv = [0] * n
        f = 1
        for i in range(1, n):
            f = (f * i) % mod
            fac[i] = f
            inv[i] = pow(f, mod - 2, mod)

        self.fac = fac
        self.inv = inv

    def smallestPalindrome(self, s: str, k: int) -> str:
        n = len(s)
        hf = s[:n // 2]
        self.helper(n // 2 + 1)
        inv = self.inv
        fac = self.fac
        # mod = 10**9 + 7
        mod = 10 ** 18 + 3

        mp = Counter(hf)
        ar = []
        x = 1
        for i in range(n // 2):
            for ke in sorted(mp.keys()):
                if mp[ke] == 0: continue
                mp[ke] -= 1
                f = fac[n // 2 - i - 1]
                # print(n//2-i-1)
                for v in mp.values():
                    if v == 0: continue
                    f *= inv[v]
                    f %= mod
                # print(ke, x, x+f)
                if k in range(x, x + f):
                    ar.append(ke)
                    break
                x += f
                mp[ke] += 1
            else:
                return ''
        # print(ar)
        res = ''.join(ar)
        return res + (s[n // 2] if n % 2 else '') + res[::-1]



# reason found, the mod 10**9 + 7 is too small, but anyway when I tried 10**18 + 3 as mod (which is also prime)
# it hit TLE😥
class Solution:
    def __init__(self):
        # mod = 10**9 + 7
        mod = 10 ** 18 + 3
        n = 10 ** 4
        fac = [1] * n
        inv = [0] * n
        f = 1
        for i in range(1, n):
            f = (f * i) % mod
            fac[i] = f
            inv[i] = pow(f, mod - 2, mod)

        self.fac = fac
        self.inv = inv

    def smallestPalindrome(self, s: str, k: int) -> str:
        inv = self.inv
        fac = self.fac
        # mod = 10**9 + 7
        mod = 10 ** 18 + 3
        n = len(s)
        hf = s[:n // 2]

        mp = Counter(hf)
        ar = []
        x = 1
        for i in range(n // 2):
            for ke in sorted(mp.keys()):
                if mp[ke] == 0: continue
                mp[ke] -= 1
                f = fac[n // 2 - i - 1]
                # print(n//2-i-1)
                for v in mp.values():
                    if v == 0: continue
                    f *= inv[v]
                    f %= mod
                # print(ke, x, x+f)
                if k in range(x, x + f):
                    ar.append(ke)
                    break
                x += f
                mp[ke] += 1
            else:
                return ''
        # print(ar)
        res = ''.join(ar)
        return res + (s[n // 2] if n % 2 else '') + res[::-1]



# incorrect
# can't find the issue. and the thing is that it worked for a lot of extreme cases I can think of
class Solution:
    def __init__(self):
        mod = 10 ** 9 + 7
        n = 10 ** 4
        fac = [1] * n
        inv = [0] * n
        f = 1
        for i in range(1, n):
            f = (f * i) % mod
            fac[i] = f
            inv[i] = pow(f, mod - 2, mod)

        self.fac = fac
        self.inv = inv

    def smallestPalindrome(self, s: str, k: int) -> str:
        inv = self.inv
        fac = self.fac
        mod = 10 ** 9 + 7
        n = len(s)
        hf = s[:n // 2]

        mp = Counter(hf)
        ar = []
        x = 1
        for i in range(n // 2):
            for ke in sorted(mp.keys()):
                if mp[ke] == 0: continue
                mp[ke] -= 1
                f = fac[n // 2 - i - 1]
                # print(n//2-i-1)
                for v in mp.values():
                    if v == 0: continue
                    f *= inv[v]
                    f %= mod
                # print(ke, x, x+f)
                if k in range(x, x + f):
                    ar.append(ke)
                    break
                x += f
                mp[ke] += 1
            else:
                return ''
        # print(ar)
        res = ''.join(ar)
        return res + (s[n // 2] if n % 2 else '') + res[::-1]