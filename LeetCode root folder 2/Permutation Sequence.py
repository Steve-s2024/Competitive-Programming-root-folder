# greedy solution, number system: 27%
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        hashSet = set()
        factorial = 1
        for i in range(1, n+1):
            factorial *= i

        res = []
        k -= 1
        def recursive(i, cur, fac):
            nonlocal n, k
            if i >= n:
                return
            fac //= (n-i)
            increment = fac
            # print(res)
            cnt = 1
            for cand in range(1, n+1):
                l, r = cur + (cnt-1)*increment, cur + cnt*increment
                # print(cand, l, r)
                if cand not in hashSet:
                    if k in range(l, r):
                        hashSet.add(cand)
                        res.append(str(cand))
                        recursive(i+1, l, fac)
                    cnt += 1
        recursive(0, 0, factorial)
        return ''.join(res)