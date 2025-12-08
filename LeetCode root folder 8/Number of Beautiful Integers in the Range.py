# TLE
class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        a = str(high)
        b = str(low).zfill(len(a))
        n = len(a)
        # if n%2: return 0
        stk = []
        arr = []
        def recursive(i, f1, f2, pf1, pf2, f):
            nonlocal n
            if pf1 > n//2 or pf2 > n//2: return
            if i >= n:
                if pf1 == pf2: arr.append(''.join(str(e) for e in stk))
                return

            lw, hi = 0 if not f1 else int(b[i]), 9 if not f2 else int(a[i])
            for j in range(lw, hi+1):
                stk.append(j)
                f = f and j == 0
                recursive(i+1, f1 and j==int(b[i]), f2 and j==int(a[i]), pf1+j%2 if not f else 0, (pf2+(j+1)%2) if not f else 0, f)
                stk.pop()
        recursive(0, 1, 1, 0, 0, 1)
        # print(arr)
        res = 0
        for val in arr:
            if int(val) % k == 0: res += 1
        return res