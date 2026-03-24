


# n^2*logn solution, TLE with two testcases remain. happy even to only come up with this solution
class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        n = len(nums)
        sl = SortedList([nums[-1]])
        ar = [0] * n
        ref = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n - 2, 1, -1):
            for j in range(i - 1, 0, -1):
                if nums[j] < nums[i]: continue
                x = len(sl) - sl.bisect_left(nums[j])
                ar[j] += x
                ref[j][nums[i]] = x
            sl.add(nums[i])

        mp = [-1] * (n + 1)
        for i in range(n): mp[nums[i]] = i

        res = 0
        for i in range(1, n + 1):
            for j in range(mp[i] + 1, n - 2): res += ar[j]
            for j in range(n): ar[j] -= ref[j][i]
        return res

'''
# on a single testcase with worst input, the solution only spent 1.9 seconds
from time import time
t = time()
Solution().countQuadruplets([i for i in range(1, 4001)])
print(time()-t)
'''