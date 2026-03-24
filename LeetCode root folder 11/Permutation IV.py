# not easy for sure, but hardly 2470
class Solution:
    def permute(self, n: int, k: int) -> List[int]:
        fac = [1]*(n+1)
        for i in range(2, n+1): fac[i] = min(10**15, fac[i-1]*i)

        def helper(re):
            a, b = re//2, (re+1)//2
            return fac[b]*fac[a]

        p = [-1]*n
        vs = [0]*n
        t = 0
        f = 0
        for i in range(n):
            ct = helper(n-i-1)
            for j in range(n):
                if (n%2==1 or i!=0) and (vs[j] or j%2 != f): continue
                if n%2 == 0 and i == 0: f = j%2
                if t+ct >= k:
                    p[i] = j
                    vs[j] = 1
                    break
                t += ct
            f = f^1
        if -1 in p: return []
        return [e+1 for e in p]