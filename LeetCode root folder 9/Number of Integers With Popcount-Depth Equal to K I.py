# I remember this problem from the contest, the first hard problem solved during contest is the second part of
# this problem. and that is easier one. now I solved this without much sweat... lol improving

class Solution:
    def popcountDepth(self, n: int, k: int) -> int:
        if k == 0: return 1
        # bit length of 10**15 is 50
        # popcount depth of number less than 10**15 is < 5 (5 is not possible)
        x = n.bit_length()

        ar = [0] * 50
        for i in range(1, 51):
            x = i
            ct = 0
            while x > 1:
                x = x.bit_count()
                ct += 1
            ar[i - 1] = ct
        # print(ar)

        s = str(bin(n))[2:]
        l = len(s)

        @cache
        def recursive(i, x, hf):
            if i >= n.bit_length(): return 1 if x == 0 else 0
            res = recursive(i + 1, x, hf and s[i] == '0')
            if x and (not hf or s[i] == '1'): res += recursive(i + 1, x - 1, hf)
            return res

        res = 0
        for i, v in enumerate(ar):
            if v + 1 == k: res += recursive(0, i + 1, 1)
        if k == 1: res -= 1
        return res


