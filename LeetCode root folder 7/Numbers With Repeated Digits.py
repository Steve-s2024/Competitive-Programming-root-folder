# very drill that i forget to cache the recursive, and it runs in 2 seconds even in the worst case haha: 18%
class Solution:
    @cache
    def genericRecursive(self, n, mask, f):
        if n == 0: return 1
        res = 0
        for i in range(10):
            if f and i == 0: continue
            if mask&(1<<i) == 0:
                res += self.genericRecursive(n-1, mask|(1<<i), 0)
        return res


    def numDupDigitsAtMostN(self, n: int) -> int:
        s = str(n)
        size = len(s)
        @cache
        def recursive(i, mask, f):
            nonlocal s, size
            if i >= size: return 1
            res = 0
            for j in range(10):
                if mask & (1<<j) == 0:
                    if i == 0 and j == 0: continue
                    if f and int(s[i]) < j: break
                    res += recursive(i+1, mask|(1<<j), f and int(s[i]) == j)
            return res
        tot = recursive(0, 0, 1)

        size -= 1
        while size:
            tot += self.genericRecursive(size, 0, 1)
            size -= 1

        return n-tot



