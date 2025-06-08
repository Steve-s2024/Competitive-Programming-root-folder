# brute-force: TLE

'''class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        # brute-force
        stack = []
        count = 0
        def dfs(idx):
            nonlocal count
            if len(stack) == 4:
                if stack[0] * stack[3] == stack[1] * stack[2]:
                    count += 1
                return
            if idx >= len(nums):
                return #🤣
            stack.append(nums[idx])
            dfs(idx + 1)
            stack.pop()
            dfs(idx + 1)
        dfs(0)
        return count * 8'''


# hash table solution:419
# ms
# Beats
# 39.05%
# not very fast, but is the best you can get
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        # slightly better than brute-force
        hashMap = defaultdict(int)
        res = 0
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                prod = nums[i] * nums[j]
                res += hashMap[prod] * 8
                hashMap[prod] += 1

        return res
