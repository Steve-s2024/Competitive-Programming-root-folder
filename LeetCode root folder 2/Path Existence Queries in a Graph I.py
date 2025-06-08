# a refreshing Q2
class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        hashMap = [0] * n
        hashMap[0] = 0
        i = 1
        curId = 0
        while i < n:
            while i < n and nums[i]-nums[i-1] <= maxDiff:
                hashMap[i] = curId
                i += 1
            curId += 1
            if i >= n:
                break
            hashMap[i] = curId
            i += 1
        # print(hashMap)
        m = len(queries)
        ans = [False] * m
        for i in range(m):
            [a, b] = queries[i]
            ans[i] = hashMap[a] == hashMap[b]
        return ans