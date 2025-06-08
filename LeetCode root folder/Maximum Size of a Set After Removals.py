# fking retard question destroyed me, so tedious OMG!!!
# : 60%
class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        set1, set2 = set(nums1), set(nums2)
        l1, l2 = len(set1), len(set2)
        repCnt = len(set1 & set2)

        n1, n2 = n//2 - (n-l1), n//2 - (n-l2)
        n1, n2 = max(0, n1), max(0, n2)
        # print(l1, l2, n1, n2, repCnt)
        
        if n1+n2 <= repCnt:
            return l1+l2 - repCnt
        return l1+l2 - repCnt - (n1+n2-repCnt)