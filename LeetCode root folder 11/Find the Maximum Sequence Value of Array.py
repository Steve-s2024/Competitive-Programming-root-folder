# not easy


def helper(nums, k):
    MX = 1<<7
    n = len(nums)
    mp = [1 << 31] * MX
    if k < 7:
        @cache
        def fn(i, x, num):
            if x == k:
                mp[num] = min(mp[num], i-1)
                return
            if i >= n: return
            fn(i + 1, x, num)
            if x < k: fn(i + 1, x + 1, num | nums[i])

        fn(0, 0, 0)
    else:
        tp = [1<<31] * 7
        for i in range(n):
            j = 0
            t = nums[i]
            while t:
                if t & 1: tp[j] = min(tp[j], i)
                t >>= 1
                j += 1
        # print(tp)
        for t in range(1, MX):
            j, mx = 0, -1
            s = t
            while s:
                if s & 1: mx = max(mx, tp[j])
                s >>= 1
                j += 1
            ct = 0
            for i in range(n):
                if nums[i] | t == t: ct += 1
                if ct == k:
                    mp[t] = max(i, mx)
                    break
    return mp

class Solution:
    def maxValue(self, nums: List[int], k: int) -> int:
        n = len(nums)
        MX = 1<<7
        ref = []
        for i in range(MX):
            ar = []
            for j in range(MX): ar.append((i^j, j))
            ref.append([e[1] for e in sorted(ar, reverse = True)])

        pre = helper(nums, k)
        # print(pre)
        suf = helper(nums[::-1], k)
        suf = [n-e-1 for e in suf]
        # print(suf)


        res = -1
        for i in range(n):
            for x in range(1, MX):
                if pre[x] > i: continue
                for y in ref[x]:
                    if suf[y] > i:
                        res = max(res, x^y)
                        break
        return res