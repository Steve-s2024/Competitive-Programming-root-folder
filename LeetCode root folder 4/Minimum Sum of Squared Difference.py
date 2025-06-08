# the greedy solution is pretty intuitive...: 24%
class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        dif = []
        n = len(nums1)
        for i in range(n):
            dif.append(abs(nums1[i] - nums2[i]))

        dif.sort()
        l, r = 0, dif[-1]
        res = float('inf')
        tok = k1 + k2
        while l <= r:
            m = (l + r) // 2
            tot = 0
            for i in range(n):
                if dif[i] > m:
                    tot += dif[i] - m
            if tot <= tok:
                res = m
                rem = tok - tot
                r = m - 1
            else:
                l = m + 1

        dif = [min(res, e) for e in dif]
        for i in range(n - 1, -1, -1):
            if rem == 0:
                break
            if dif[i] > 0:
                dif[i] -= 1
                rem -= 1

        # print(dif)
        ans = 0
        for num in dif:
            ans += num ** 2
        return ans