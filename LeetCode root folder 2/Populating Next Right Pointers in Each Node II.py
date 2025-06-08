
# bfs solution, simple implementation: 89%
class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        m = len(queries)
        ans = [0] * m
        nums.sort()
        for i in range(m):
            l, r = 0, n-1
            target = queries[i]
            while l < r:
                m = (r+l)//2
                if nums[m] >= target:
                    r = m
                else:
                    l = m+1

            s1, s2 = l, n-l
            diff1, diff2 = s1 * target - sum(nums[:s1+1]), sum(nums[s2:]) - s2 * target
            ans[i] = diff1+diff2
        return ans
