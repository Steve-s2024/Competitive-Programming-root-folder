# literally the LIS algorithm implementation, not the optimal, but the idea strike me right a way: 10%

class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        n = len(obstacles)
        arr = []
        ans = [0]*n
        for i in range(n):
            val = obstacles[i]
            l, r = 0, len(arr)-1
            res = 0
            while l <= r:
                m = (l+r)//2
                if arr[m] <= val:
                    res = m+1
                    l = m+1
                else: r = m-1

            ans[i] = res+1
            if res == len(arr): arr.append(val)
            else: arr[res] = val
        return ans