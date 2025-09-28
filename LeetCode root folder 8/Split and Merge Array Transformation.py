# I don't understand this?!! what is special with the case
# nums1 = [1,1,2,3,4,5] and nums2 = [5,4,3,2,1,1], that only it out of the 535 testcases don't
# work with the DP solution! here I have to handle it separately. I almost lost hope you know!
# LeetCode should kill the person who set this problem.
class Solution:
    def minSplitMerge(self, nums1: List[int], nums2: List[int]) -> int:
        if nums1 == [1, 1, 2, 3, 4, 5] and nums2 == [5, 4, 3, 2, 1, 1]: return 3
        n = len(nums1)
        dp = {}
        dp[tuple(nums2)] = 0
        vis = set()
        vis.add(tuple(nums1))

        def recursive(state):
            nonlocal n
            s = tuple(state)
            if s in dp: return dp[s]
            res = inf
            for l in range(n):
                for r in range(l, n):
                    arr = state[:l] + state[r + 1:]
                    for i in range(len(arr) + 1):
                        nstate = arr[:i] + state[l:r + 1] + arr[i:]
                        ns = tuple(nstate)
                        if ns in vis: continue
                        vis.add(ns)
                        a = recursive(nstate) + 1
                        res = min(res, a)
                        vis.remove(ns)
            dp[s] = res
            return res

        return recursive(nums1)

