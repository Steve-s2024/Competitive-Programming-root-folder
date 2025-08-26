# it is supposed to be DP, but I am stubbornly fixated on the pure math approach, luckily ended up finishing it
# with O(logn) complexity and it is much faster than the DP solution: 100%
class Solution:
    @staticmethod
    def getFac(x, u):
        res = 1
        for i in range(x):
            res *= u
            u -= 1
        return res


    def countSpecialNumbers(self, n: int) -> int:
        s = str(n)
        size = len(s)
        res = 0
        for i in range(1, size):
            cnt = 9
            tot = 9
            for j in range(1, i):
                tot *= cnt
                cnt -= 1
            res += tot


        vis = set()
        def recursive(i):
            nonlocal s, res
            if i >= len(s): return
            for x in range(int(s[i])):
                if str(x) not in vis and (i != 0 or x != 0):
                    a = Solution.getFac(size-i-1, 10-len(vis)-1)
                    res += a
            if s[i] in vis: return
            vis.add(s[i])
            recursive(i+1)
        recursive(0)
        if len(set(s)) == len(s): res += 1
        return res

