# brute-force: tle
'''class Solution:
    def minCost(self, nums: List[int]) -> int:
        # brute-force
        minCost = float('inf')

        def recursive(i1, i2, i3, cost):
            # print(i1, i2, i3)
            nonlocal minCost
            maxIdx = max(i1, i2, i3)
            if maxIdx >= len(nums):
                overHead = 0
                for i in sorted([i1, i2, i3]):
                    if i >= len(nums):
                        break
                    overHead = max(overHead, nums[i])
                minCost = min(minCost, cost + overHead)
                return
            arr = [[nums[i1], i1], [nums[i2], i2], [nums[i3], i3]]
            arr.sort(key = lambda i: i[0])
            recursive(arr[0][1], maxIdx + 1, maxIdx + 2, cost + arr[2][0])
            # recursive(arr[2][1]+1, arr[1][1], arr[2][1]+2, cost+arr[2][0])
            recursive(arr[2][1], maxIdx + 1, maxIdx + 2, cost + arr[1][0])

        recursive(0, 1, 2, 0)
        return minCost'''

# dp solution O(n^3): it shouldn't work but with this complexity but i guess i'm lucky and the complexity
# somehow is actually O(n^2)

class Solution:
    def minCost(self, nums: List[int]) -> int:
        # dp solution
        dp = {}

        def recursive(i1, i2, i3):
            # print(i1, i2, i3)
            maxIdx = max(i1, i2, i3)
            if (i1, i2, i3) in dp:
                return dp[(i1, i2, i3)]
            if maxIdx >= len(nums):
                overHead = 0
                for i in [i1, i2, i3]:
                    if i >= len(nums):
                        break
                    overHead = max(overHead, nums[i])
                return overHead

            arr = [[nums[i1], i1], [nums[i2], i2], [nums[i3], i3]]
            arr.sort(key=lambda i: i[0])
            res = min(
                recursive(arr[0][1], maxIdx + 1, maxIdx + 2) + arr[2][0],
                # recursive(arr[2][1]+1, arr[1][1], arr[2][1]+2, cost+arr[2][0]),
                recursive(arr[2][1], maxIdx + 1, maxIdx + 2) + arr[1][0]
            )
            dp[(i1, i2, i3)] = res
            return res

        return recursive(0, 1, 2)