# superb boring question, please ban all these problem writer: 6%
class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        n = len(nums)
        mi, mx = nums[0], nums[0]
        i1, i2 = 0, 0
        pre = []
        prei = []
        for i in range(n):
            if mi > nums[i]:
                mi = nums[i]
                i1 = i
            if mx < nums[i]:
                mx = nums[i]
                i2 = i
            pre.append((mi, mx))
            prei.append((i1, i2))

        mi, mx = nums[-1], nums[-1]
        i1, i2 = n-1, n-1
        suf = []
        sufi = []
        for i in range(n - 1, -1, -1):
            if mi > nums[i]:
                mi = nums[i]
                i1 = i
            if mx < nums[i]:
                mx = nums[i]
                i2 = i
            suf.append((mi, mx))
            sufi.append((i1, i2))

        suf = suf[::-1]
        sufi = sufi[::-1]
        # print(suf, sufi)
        for i in range(indexDifference, n):
            if abs(pre[i - indexDifference][0] - suf[i][1]) >= valueDifference:
                return [prei[i - indexDifference][0], sufi[i][1]]
            if abs(pre[i - indexDifference][1] - suf[i][0]) >= valueDifference:
                return [prei[i - indexDifference][1], sufi[i][0]]
        return [-1, -1]


