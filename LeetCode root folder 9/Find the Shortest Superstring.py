# solved independently, a problem which combine multiple area of algorithm
# very challenging
class Solution:
    def shortestSuperstring(self, words: List[str]) -> str:
        mp = {}
        n = len(words)
        for i in range(n):
            for j in range(n):
                if i == j: continue
                w1, w2 = words[i], words[j]
                w = 0
                for k in range(1, min(len(w2), len(w1))):
                    if w1[-k:] == w2[:k]: w = k
                mp[(i, j)] = w
        ref = {}

        @cache
        def recursive(pv, msk):
            nonlocal n
            if msk == (1 << n) - 1: return 0
            x = -inf
            t = -1
            for j in range(n):
                if 1 << j & msk: continue
                a = recursive(j, msk | 1 << j) + (mp[(pv, j)] if pv != -1 else 0)
                if a > x:
                    x = a
                    t = j
            ref[(pv, msk)] = t
            return x

        res = recursive(-1, 0)

        # print(sum(len(e) for e in words), res)
        ar = []
        pv, msk = -1, 0
        while msk != (1 << n) - 1:
            nxt = ref[(pv, msk)]
            ar.append(nxt)
            msk |= 1 << nxt
            pv = nxt
        # print(ar)

        ans = [words[ar[0]]]
        sm = 0
        for i in range(1, len(ar)):
            x = mp[(ar[i - 1], ar[i])]
            sm += x
            ans.append(words[ar[i]][x:])
        # print(sm)
        return ''.join(ans)
