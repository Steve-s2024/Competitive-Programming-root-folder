# translatable into finding number of triplet of increasing order (a < b < c)
# pretty neat heuristics

class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        mp = {nums1[i]:i for i in range(n)}
        ar = [mp[nums2[i]] for i in range(n)]
        # print(ar)

        le = SortedList()
        ri = SortedList(ar)
        res = 0
        for i in range(n):
            ri.remove(ar[i])
            a, b = le.bisect_left(ar[i]), len(ri)-ri.bisect_left(ar[i])
            res += a*b
            le.add(ar[i])
        return res