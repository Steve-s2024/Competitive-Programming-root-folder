# very interesting bitmask dp approach. proven that for bitmask dp, the transition does not involve the index information
# so the index in the usual dp state design can be ignored


class Solution:
    def numberOfGoodSubsets(self, nums: List[int]) -> int:
        ref = {v: i for i, v in enumerate([2, 3, 5, 7, 9, 11, 13, 17, 19, 23, 29])}
        ar = [2, 3, 5, 6, 7, 10, 11, 13, 14, 15, 17, 19, 21, 22, 23, 26, 29, 30]
        M = 10**9 + 7

        def fac(v):
            res = []
            for f in range(2, int(sqrt(v)) + 1):
                while v%f == 0:
                    v //= f
                    res.append(f)
            if v > 1: res.append(v)
            return res
        fs = {i:fac(i) for i in range(2, 31)}



        mp = defaultdict(int)
        for v in nums: mp[v] += 1
        @cache
        def fn(msk, prv):
            res = 1
            for c in ar:
                nmsk = 0
                if c <= prv: continue
                for f in fs[c]: nmsk |= 1 << ref[f]
                if nmsk & msk: continue
                res = (res + fn(msk | nmsk, c) * mp[c]) % M
            return res
        res = fn(0, -1)-1
        # print(res)
        return (pow(2, mp[1], M)*res) % M