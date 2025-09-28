# an immature attempt of simplified SOS DP solution, but the time complexity is very close: TLE
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        size = 1
        mx = max(nums)
        while 1 << size <= mx: size += 1
        arr = [0] * (1 << size)
        for num in nums: arr[num] = num
        for num in range(1 << size):
            for i in range(size):
                if num & (1 << i): continue
                arr[num | (1 << i)] = max(arr[num | (1 << i)], arr[num])

        # print(arr)
        res = 0
        for num in nums:
            a, b = num, arr[num ^ ((1 << size) - 1)]
            res = max(res, a * b)

        return res
