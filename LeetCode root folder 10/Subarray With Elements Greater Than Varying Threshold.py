# after modifying the equation, the problem becomes "84. Largest Rectangle in Histogram"
class Solution:
    def validSubarraySize(self, nums: List[int], threshold: int) -> int:
        n = len(nums)
        stk = []
        rar = [n] * n
        for i in range(n):
            while stk and stk[-1][0] > nums[i]: rar[stk.pop()[1]] = i
            stk.append((nums[i], i))
        lar = [-1] * n
        for i in range(n - 1, -1, -1):
            while stk and stk[-1][0] > nums[i]: lar[stk.pop()[1]] = i
            stk.append((nums[i], i))

        res = 0
        mx = 0
        for i in range(n):
            l, r = lar[i], rar[i]
            size = r - l - 1
            area = size * nums[i]
            if area > mx:
                mx = area
                res = size
        if mx <= threshold: return -1
        return res