# reduced it to 2 seconds: 62%
class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        MOD = 10**9+7
        frq = [0]*26
        for c in s: frq[ord(c)-ord('a')]+=1
        for i in range(t):
            # print(frq)
            tmp = frq[25]
            for j in range(25, 0, -1):
                frq[j] = frq[j-1]
            frq[0] = tmp
            frq[1] += tmp
            frq[1] %= MOD
        return sum(frq) % MOD


# my god whopping 10 seconds: 5%
class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        MOD = 10 ** 9 + 7
        frq = defaultdict(int)
        for c in s: frq[c] += 1
        for i in range(t):
            tmp = defaultdict(int)
            for j in range(25):
                a, b = chr(ord('a') + j), chr(ord('a') + j + 1)
                if a in frq: tmp[b] = frq[a]
            if 'z' in frq:
                tmp['a'] += frq['z']
                tmp['b'] += frq['z']
                tmp['a'] %= MOD
                tmp['b'] %= MOD
            frq = tmp

        return sum(frq.values()) % MOD


# tried with DP and failed with MLE, it is actually a o(1) space and O(26*n) time question
# if I simply maintain the frequency of each digit and do simulation
class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        MOD = 10 ** 9 + 7
        dp = {}

        def recursive(i, tot):
            if (i, tot) in dp:
                return dp[(i, tot)]
            if tot >= t:
                return 1

            if i % 26 == 25:
                res = recursive(0, tot + 1) + recursive(1, tot + 1)
            else:
                res = recursive(i + 1, tot + 1)
            res %= MOD
            dp[(i, tot)] = res
            return res

        mp = [0] * 26
        for i in range(26):
            mp[i] = recursive(i, 0)

        res = 0
        for c in s:
            res += mp[ord(c) - ord('a')]
            res %= MOD
        return res
