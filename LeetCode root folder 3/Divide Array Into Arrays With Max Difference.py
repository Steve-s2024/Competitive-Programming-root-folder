# easy 100%, greedy solution, I am not able to prove the entire greedy approach
class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []
        for i in range(0, n, 3):
            a, b, c = nums[i], nums[i+1], nums[i+2]
            if c - a > k:
                return []
            res.append([a, b, c])
        return res