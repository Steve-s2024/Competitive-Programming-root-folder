# piece of CAKE! this is not 1800.: 15%
class Solution:
    @staticmethod
    def checkMinSwap(arr1, arr2):
        a1, a2 = arr1[-1], arr2[-1]
        n = len(arr1)
        cnt = 0
        for i in range(n-2, -1, -1):
            if arr1[i] > arr1[-1]:
                arr1[i], arr2[i] = arr2[i], arr1[i]
                cnt += 1
            elif arr2[i] > arr2[-1]:
                arr1[i], arr2[i] = arr2[i], arr1[i]
                cnt += 1

            if arr1[i] > arr1[-1] or arr2[i] > arr2[-1]:
                return -1
        return cnt

    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        a = Solution.checkMinSwap(nums1[:], nums2[:])
        nums1[-1], nums2[-1] = nums2[-1], nums1[-1]
        b = Solution.checkMinSwap(nums1[:], nums2[:]) + 1
        return min(a, b)