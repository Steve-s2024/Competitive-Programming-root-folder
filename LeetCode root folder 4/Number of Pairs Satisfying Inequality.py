# just love sorted list, powerful: 60%
from sortedcontainers import SortedList
class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        # (nums1[i] - nums2[i]) - (nums1[j] - nums2[j]) <= diff
        n = len(nums1)
        diffs = []
        for i in range(n):
            diffs.append(nums1[i] - nums2[i])
        # print(diffs)

        # find all i, j such that:
        #   diffs[i] - diffs[j] <= diff

        res = 0
        sl = SortedList()
        for i in range(n - 1, -1, -1):
            a = len(sl) - sl.bisect_left(diffs[i])
            # print(a, sl, diffs[i])
            res += a
            sl.add(diffs[i] + diff)

        return res


# TLE
class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        # (nums1[i] - nums2[i]) - (nums1[j] - nums2[j]) <= diff
        n = len(nums1)
        diffs = []
        for i in range(n):
            diffs.append(nums1[i] - nums2[i])
        print(diffs)

        # find all i, j such that:
        #   diffs[i] - diffs[j] <= diff

        res = 0
        for i in range(n):
            for j in range(i+1, n):
                if diffs[i] - diffs[j] <= diff: res += 1
        return res
