# solution no.1: tle
'''class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        hashMap = defaultdict(list)
        idx = 0
        for l, r, val in queries:
            for i in range(l, r + 1):
                hashMap[i].append([idx, val])
            idx += 1

        # print(hashMap)
        def minQuery(val, i, arr):
            if val == 0:
                return i - 1
            if val < 0 or i >= len(arr):
                return float('inf')

            return min(
                minQuery(val, i + 1, arr),
                minQuery(val - arr[i][1], i + 1, arr)
            )

        res = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                continue
            a = minQuery(nums[i], 0, hashMap[i])
            if a == float('inf'):
                # print(i, nums[i])
                return -1
            res = max(res, hashMap[i][a][0])
        return res + 1'''

# solution no.2, i can't believe i actually figure out the issue why my code didn't pass the 711/713th testcase just by
# throwing completely random testcases desperately. I luckily created this (nums = [0] queries = [[0,0,1]]) testcase, and
# it is all i need to realize the issue. after that it took me about 3 minutes to fix the issue and finally passed the Q3
# while only 11 minutes left for the contest. this is some crazy odd.
class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        hashMap = defaultdict(list)
        count = 1
        for l, r, val in queries:
            for i in range(l, r + 1):
                hashMap[i].append([count, val])
            count += 1
        # print(hashMap)
        dp = {}

        def minQuery(val, i, arr):
            if (val, i) in dp:
                return dp[(val, i)]
            if val == 0:
                return i - 1
            if val < 0 or i >= len(arr):
                return float('inf')

            tmp = min(
                minQuery(val, i + 1, arr),
                minQuery(val - arr[i][1], i + 1, arr)
            )
            dp[(val, i)] = tmp
            return tmp

        res = -float('inf')
        for i in range(len(nums)):
            if nums[i] == 0:
                continue
            dp = {}
            a = minQuery(nums[i], 0, hashMap[i])
            if a == float('inf'):
                # print(i, nums[i])
                return -1
            res = max(res, hashMap[i][a][0])
        if res == -float('inf'):
            return 0
        return res

