# why the fk my bitmask solution is much slower compared with
# the below brute force solution??: 17%
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        if k > len(s):
            return False
        hashSet = set()
        n = len(s)
        mask = int(s[:k], 2)
        hashSet.add(mask)
        for i in range(k, n):
            if 1 << (k-1) <= mask:
                mask -= 1 << (k-1)
            mask <<= 1
            mask += int(s[i])
            hashSet.add(mask)
        return len(hashSet) == 1 << k


# this is the actual solution, which is easy as hell
# the problem is easy as hell if I know the constraint
# and description well enough: 40%
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        hashSet = set()
        n = len(s)
        l, r = 0, k-1
        while r < n:
            hashSet.add(s[l:r+1])
            r += 1
            l += 1
        return len(hashSet) == 1 << k


# my stupid brain took the question the wrong way and end up
# making this solution
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        hashSet = set()
        n = len(s)
        for i in range(min(n, k)):
            for j in range(i, min(n, k)):
                hashSet.add(s[i:j+1])
        for i in range(k ,n):
            for j in range(i, i-k, -1):
                hashSet.add(s[j:i+1])
        print(hashSet)
        return len(hashSet) == 1 << k