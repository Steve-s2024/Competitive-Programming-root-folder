# neetcode taught me another good way to manipulate binary search


class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n = len(nums1)
        flp = [-e for e in nums2][::-1]
        l, r = inf, -inf
        for v in nums1:
            a, b = nums2[0]*v, nums2[-1]*v
            l = min(l, a, b)
            r = max(r, a, b)
        # print(l, r)

        res = -1
        while l <= r:
            m = (l+r)//2
            x = 0
            mx = -inf
            for i in range(n):
                v = nums1[i]
                if v == 0:
                    if m >= 0:
                        x += len(nums2)
                        mx = max(0, mx)
                    continue
                if v > 0: a = bisect_right(nums2, m/v)
                else: a = bisect_right(flp, m/-v)
                x += a
                if a: mx = max(mx, v * (nums2[a-1] if v > 0 else -flp[a-1]))
            # print(m, x)
            if x >= k:
                res = mx
                r = m-1
            else: l = m+1

        return res