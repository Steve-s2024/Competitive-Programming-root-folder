# a great great solution, stroke of genius. almost deemed impossible
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        sl = SortedList(nums)
        n = len(nums)
        l, r = min(nums[i]-nums[i-1] for i in range(1, n)), nums[-1] - nums[0]
        res = -1
        while l <= r:
            m = (l + r) // 2
            # print(m)
            x = 0
            mx = 0
            for i in range(1, n):
                # assume nums[i] to be right end, check how many left end can make distance <= m
                j = sl.bisect_left(nums[i]-m)
                # print(j, i)
                if j >= i: continue
                mx = max(mx, nums[i]-nums[j])
                x += i-j


            if x >= k:
                res = mx
                r = m - 1
            else: l = m + 1

        return res