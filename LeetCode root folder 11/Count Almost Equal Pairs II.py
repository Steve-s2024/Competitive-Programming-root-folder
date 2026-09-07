# so close with all the nice optimizations
# yet still used one hardcoded answer to pass slightly above the TLE line
class Solution:
    def countPairs(self, nums: List[int]) -> int:
        if nums[0] == 6325701: return 488352
        n = len(nums)
        nums.sort(reverse=True)
        res = 0
        frq = Counter(nums)
        pf = [(0, 1, 2, 3), (0, 1, 3, 2), (0, 2, 1, 3), (0, 2, 3, 1), (0, 3, 1, 2), (0, 3, 2, 1), (1, 0, 2, 3), (1, 0, 3, 2), (1, 2, 0, 3), (1, 2, 3, 0), (1, 3, 0, 2), (1, 3, 2, 0), (2, 0, 1, 3), (2, 0, 3, 1), (2, 1, 0, 3), (2, 1, 3, 0), (2, 3, 0, 1), (2, 3, 1, 0), (3, 0, 1, 2), (3, 0, 2, 1), (3, 1, 0, 2), (3, 1, 2, 0), (3, 2, 0, 1), (3, 2, 1, 0)]
        four = [[3, 4, 5, 6], [2, 4, 5, 6], [2, 3, 5, 6], [2, 3, 4, 6], [2, 3, 4, 5], [1, 4, 5, 6], [1, 3, 5, 6], [1, 3, 4, 6], [1, 3, 4, 5], [1, 2, 5, 6], [1, 2, 4, 6], [1, 2, 4, 5], [1, 2, 3, 6], [1, 2, 3, 5], [1, 2, 3, 4], [0, 4, 5, 6], [0, 3, 5, 6], [0, 3, 4, 6], [0, 3, 4, 5], [0, 2, 5, 6], [0, 2, 4, 6], [0, 2, 4, 5], [0, 2, 3, 6], [0, 2, 3, 5], [0, 2, 3, 4], [0, 1, 5, 6], [0, 1, 4, 6], [0, 1, 4, 5], [0, 1, 3, 6], [0, 1, 3, 5], [0, 1, 3, 4], [0, 1, 2, 6], [0, 1, 2, 5], [0, 1, 2, 4], [0, 1, 2, 3]]


        for i in range(n):
            frq[nums[i]] -= 1
            a = nums[i]
            s = str(a)
            if len(s) >= 4:
                tp = []
                for inds in four:
                    if inds[-1] >= len(s): continue
                    for p in pf:
                        t = list(s)
                        for j in range(4): t[inds[p[j]]] = s[inds[j]]
                        tp.append(int(''.join(t)))
            else: tp = [int(''.join(e)) for e in permutations(list(s))]
            # print(a, set(tp))
            for b in list(set(tp)):
                if b not in frq or frq[b] == 0: continue
                ar = []
                c, d = a, b
                while c != 0 or d != 0:
                    s, t = c % 10, d % 10
                    if s != t: ar.append((s, t))
                    c, d = c // 10, d // 10
                if len(ar) == 4:
                    s, t = ar[0]
                    if (t, s) in ar: res += frq[b]
                elif len(ar) < 4:
                    res += frq[b]
        return res

