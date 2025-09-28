# bottom up upgrade, it's pretty hard to get everything in bottom up DP right: 56% 92ms
class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)

        dp = [0, 1]
        for i in range(n-2, -1, -1):
            tmp = [inf, inf]
            if nums1[i] < nums1[i+1] and nums2[i] < nums2[i+1]:
                tmp[0] = dp[0]
                tmp[1] = dp[1]+1
            if nums1[i] < nums2[i+1] and nums2[i] < nums1[i+1]:
                tmp[0] = min(tmp[0], dp[1])
                tmp[1] = min(tmp[1], dp[0]+1)
            dp = tmp
        return min(dp)



# not very hard for me now, the state machine solution: 17% 451ms
class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        dp = {}
        def recursive(i):
            nonlocal n
            if i >= n: return 0
            state = (i, nums1[i-1], nums2[i-1])
            if state in dp: return dp[state]
            res = inf
            if nums2[i-1] < nums2[i] and nums1[i-1] < nums1[i]:
                a = recursive(i+1)
                res = min(a, res)
            if nums2[i-1] < nums1[i] and nums1[i-1] < nums2[i]:
                nums1[i], nums2[i] = nums2[i], nums1[i]
                a = recursive(i+1) + 1
                nums1[i], nums2[i] = nums2[i], nums1[i]
                res = min(a, res)
            dp[state] = res
            return res
        a = recursive(1)
        nums1[0], nums2[0] = nums2[0], nums1[0]
        b = recursive(1)+1
        return min(a, b)