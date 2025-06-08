# prefix sum solution: 86%
class Solution:
    def sumDistance(self, nums: List[int], s: str, d: int) -> int:
        n = len(nums)
        for i in range(n):
            if s[i] == 'L':
                nums[i] -= d
            else:
                nums[i] += d
        nums.sort()
        res = 0
        total = 0
        for i in range(1, n):
            diff = abs(nums[i]-nums[i-1])
            total += i * diff
            res += total
        
        return res % 1000000007


# brute force
class Solution:
    def sumDistance(self, nums: List[int], s: str, d: int) -> int:
        n = len(nums)
        for i in range(n):
            if s[i] == 'L':
                nums[i] -= d
            else:
                nums[i] += d
        # try brute-force
        res = 0
        for i in range(n):
            for j in range(i+1, n):
                res += abs(nums[i] - nums[j])
        return res