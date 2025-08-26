
# I have to do it two different way, use existing element and not use existing element when finding max frequency
#: 24%
class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        nums.sort()
        n = len(nums)
        mp = Counter(nums)
        res = 0
        for key, val in mp.items():
            l, r = 0, n - 1
            left = -1
            while l <= r:
                m = (l + r) // 2
                if nums[m] >= key - k:
                    left = m
                    r = m - 1
                else:
                    l = m + 1
            l, r = 0, n - 1
            right = -1
            while l <= r:
                m = (l + r) // 2
                if nums[m] <= key + k:
                    right = m
                    l = m + 1
                else:
                    r = m - 1
            res = max(res, val + min(right - left + 1 - val, numOperations))

        res2 = 0
        l, r = 1, numOperations
        while l <= r:
            m = (l + r) // 2
            flag = False
            for i in range(n - m + 1):
                a, b = nums[i], nums[i + m - 1]
                if b - a <= 2 * k:
                    flag = True
                    break

            if flag:
                res2 = m
                l = m + 1
            else:
                r = m - 1
        return max(res, res2)