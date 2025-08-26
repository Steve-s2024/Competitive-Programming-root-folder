# use of two magic numbers, but the solution is good: 81%
class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        mp = [0]*1025
        mp[0] = 1
        n = len(word)
        res = 0
        mask = 0
        for i in range(n):
            mask ^= 1<<(ord(word[i])-ord('a'))
            res += mp[mask]
            for i in range(10):
                res += mp[mask^(1<<i)]
            mp[mask] += 1

        return res



# without the optimization, with an extra frequency array and re-compute the mask everytime: 19%
class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        mp = [0]*1025
        mp[0] = 1
        n = len(word)
        frq = [0]*10
        res = 0
        for i in range(n):
            frq[ord(word[i])-ord('a')] += 1
            mask = 0
            for i in range(10):
                if frq[i] % 2 == 1: mask |= (1<<i)
            res += mp[mask]
            for i in range(10):
                res += mp[mask^(1<<i)]
            mp[mask] += 1

        return res