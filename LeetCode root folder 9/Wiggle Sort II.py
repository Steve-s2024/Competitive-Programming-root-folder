# truly don't enjoy this problem

class Solution:
    def wiggleSort(self, ar: List[int]) -> None:
        if len(ar) == 1: return
        ar.sort()
        n = len(ar)
        fst, scd = ar[:(n + 1) // 2], ar[(n + 1) // 2:]
        if fst[-1] == scd[0]:
            a = fst.index(fst[-1])
            i = 0
            while i < len(scd) and scd[i] == scd[0]: i += 1
            b = i
            fst = fst[a:] + fst[:a]
            scd = scd[b:] + scd[:b]

        for i in range(0, n, 2):
            ar[i] = fst[i // 2]

        for i in range(1, n, 2):
            ar[i] = scd[i // 2]



