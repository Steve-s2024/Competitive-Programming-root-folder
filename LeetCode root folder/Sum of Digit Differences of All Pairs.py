# brute force:928
# ms
# Beats
# 8.01%
'''class Solution:
    def sumDigitDifferences(self, nums: List[int]) -> int:
        hashMap = defaultdict(int)
        l = len(nums)
        for num in nums:
            for i, d in enumerate(str(num)):
                hashMap[(i, d)] += 1
        # print(hashMap)
        res = 0
        for num in nums:
            for i, d in enumerate(str(num)):
                res += l - hashMap[(i, d)]
        return res // 2'''

# adjusted a bit:493
# ms
# Beats
# 29.78%
class Solution:
    def sumDigitDifferences(self, nums: List[int]) -> int:
        hashMap = defaultdict(int)
        l = len(nums)
        for num in nums:
            for i, d in enumerate(str(num)):
                hashMap[(i, d)] += 1
        # print(hashMap)
        res = 0
        for val in hashMap.values():
            res += val * (l - val)
        return res // 2