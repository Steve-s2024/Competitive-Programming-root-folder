# simulation
class Solution:
    def magicalString(self, n: int) -> int:
        res = 0
        x = 2
        ar = [1]
        i = 1
        while len(ar) < n:
            ar.append(x)
            frq = ar[i]
            for _ in range(frq-1): ar.append(x)
            x = 2 if x == 1 else 1
            i += 1

        # print(ar)
        res = 0
        for i in range(n):
            if ar[i] == 1: res += 1
        return res
