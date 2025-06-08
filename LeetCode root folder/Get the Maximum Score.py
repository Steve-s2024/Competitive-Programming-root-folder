# greedy solution, only work for the given condition
# nums must have distinct element and are in increasing 
# order: 28%
class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        res = 0
        hashSet = set(nums2)
        n, m = len(nums1), len(nums2)
        i1, i2 = n-1, m-1
        total1, total2 = 0, 0
        while i1 >= 0:
            total1 += nums1[i1]
            if nums1[i1] in hashSet:
                while i2 >= 0:
                    total2 += nums2[i2]
                    if nums2[i2] == nums1[i1]:
                        break
                    i2-=1
                print(i1, i2, total1, total2)
                res += max(total1, total2)
                total1, total2 = 0, 0
                i2-=1
            i1-=1
        total1, total2 = 0, 0
        i1, i2 = 0, 0
        while i1 < n and nums1[i1] not in hashSet:
            total1 += nums1[i1]
            i1+=1
        hashSet = set(nums1)
        while i2 < m and nums2[i2] not in hashSet:
            total2 += nums2[i2]
            i2+=1

        return (res + max(total1, total2)) % 1000000007

                