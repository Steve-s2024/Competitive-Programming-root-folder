# actually pretty simple, I'm overcomplicating it with binary search, dp
# and all that. sliding window solution: 62%
class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)

        idxMp = defaultdict(list)
        for i in range(n):
            val = nums[i]
            idxMp[val].append(i)

        def getMaxLen(arr, total):
            n = len(arr)
            cost = 0
            l, r = 0, 1
            res = 1
            while r < n:
                cost += arr[r] - arr[r - 1] - 1
                while cost > total:
                    cost -= arr[l + 1] - arr[l] - 1
                    l += 1
                res = max(res, r - l + 1)
                r += 1
            # print(arr, res)
            return res

        res = 0
        for val in idxMp.values():
            tmp = getMaxLen(val, k)
            res = max(res, tmp)
        return res




# brute force: TLE
class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        stack = []
        n = len(nums)

        def getMaxEqualSubarray(nums):
            n = len(nums)
            res = 0
            l, r = 0, 1
            while r < n:
                while r < n and nums[r] == nums[r-1]:
                    r+=1
                res = max(r-l, res)
                l = r
                r += 1
            res = max(r-l, res)
            return res

        res = 0
        def recursive(i, remain):
            nonlocal res
            if i >= n:
                res = max(res, getMaxEqualSubarray(stack))
                return
            if remain > 0:
                recursive(i+1, remain-1)
            stack.append(nums[i])
            recursive(i+1, remain)
            stack.pop()
        recursive(0, k)
        return res