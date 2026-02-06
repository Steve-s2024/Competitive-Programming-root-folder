# insane solution, my brain is cooked after this😥😭
# ridiculous I become so fking good that I can write even a solution as ugly and complicated as this
class Solution:
    def minMoves(self, nums: List[int], lim: int) -> int:
        n = len(nums)
        a = nums[:n // 2]
        b = nums[n // 2:][::-1]

        miar = []
        mxar = []
        mp = defaultdict(list)
        for i in range(n // 2):
            mi = min(a[i], b[i])
            mx = max(a[i], b[i])
            miar.append((mi, i))
            mxar.append((mx, i))
            mp[a[i] + b[i]].append(i)

        miar.sort()
        mxar.sort()

        vs = [0] * n
        x = 0
        i1, i2 = 0, 0
        j1, j2 = 0, 0
        # print([a[i]+b[i] for i in range(n//2)])
        # print(miar, mxar)
        res = inf
        for k in range(2, 2 * lim + 1):
            while i1 < n // 2 and k > miar[i1][0]:
                j = miar[i1][1]
                vs[j] += 1
                if vs[j] == 1: x += 1
                i1 += 1

            while j1 < n // 2 and k > miar[j1][0] + lim:
                j = miar[j1][1]
                vs[j] -= 1
                if vs[j] == 0: x -= 1
                j1 += 1

            while i2 < n // 2 and k > mxar[i2][0]:
                j = mxar[i2][1]
                vs[j] += 1
                if vs[j] == 1: x += 1
                i2 += 1

            while j2 < n // 2 and k > mxar[j2][0] + lim:
                j = mxar[j2][1]
                vs[j] -= 1
                if vs[j] == 0: x -= 1
                j2 += 1

            t = sum(1 if vs[i] else 0 for i in mp[k]) if k in mp else 0
            # print(k, x, t)
            # x is the cnt of pos with one/zero operation
            # t is the cnt of pos with zero operation
            # so, x-t is the cnt of pos with two operation
            tmp = x - t + 2 * (n // 2 - x)
            res = min(res, tmp)
        return res
