# new algo! LIS algorithm obtained!: 5.66%
# it is indeed impossible to solve this questino if
# you don't know the LIS algorithm, brilliant algorithm!
class Solution:
    def kIncreasing(self, arr: List[int], k: int) -> int:
        def getLongestNondecreSubseq(nums):
            res = []
            # print(nums)
            def binarySearch(tar):
                # u want to fit tar inside the res array such that tar replace an existing element 
                # that is greater then it without break the increasing order of the array.
                l, r = 0, len(res)
                while l < r:
                    m = (l+r)//2
                    if tar >= res[m]:
                        l = m+1
                    else:
                        r = m
                return l
            n = len(nums)
            for i in range(n):
                idx = binarySearch(nums[i])
                if idx >= len(res):
                    res.append(nums[i])
                else:
                    res[idx] = nums[i]
            # print(res)
            return len(res)
            

        nums = []
        n = len(arr)
        for i in range(0, k):
            nums.append([])
            for j in range(i, n, k):
                nums[i].append(arr[j])
        
        res = 0
        for subNums in nums:
            size = len(subNums)
            res += size - getLongestNondecreSubseq(subNums)
        return res

# solution no.3 dp solution with bottom up to curb the memory consumption
# to make it possible to use bottom up, i fiddled the state of dp from (i, prev)
# to (i, j), where j is the index of the prev element: TLE
# I have to add in a binary search to optimize it.
class Solution:
    def kIncreasing(self, arr: List[int], k: int) -> int:
        def getLongestNondecreSubseq(nums):
            # print(nums)
            n = len(nums)
            dp = [0]*n
            res = 0 
            for i in range(n-1, -1, -1):
                max_ = 0
                for j in range(i+1, n):
                    if nums[j] >= nums[i]:
                        max_ = max(max_, dp[j])
                dp[i] = max_+1
                res = max(res, dp[i])
            return res
            

        nums = []
        n = len(arr)
        for i in range(0, k):
            nums.append([])
            for j in range(i, n, k):
                nums[i].append(arr[j])
        # print(nums)
        
        res = 0
        for subNums in nums:
            size = len(subNums)
            res += size - getLongestNondecreSubseq(subNums)
        return res
    


# solution no.2 dp solution to find the longest non-decre subsequence
# this matches exactly what the tip LeetCode provided says, but why
# it hit MLE
#: MLE
class Solution:
    def kIncreasing(self, arr: List[int], k: int) -> int:
        def getLongestNondecreSubseq(nums):
            # print(nums)
            dp = {}
            n = len(nums)
            def recursive(i, prev):
                nonlocal n
                if (i, prev) in dp:
                    return dp[(i, prev)]
                if i >= n:
                    return 0
                res = 0
                if nums[i] >= prev:
                    res = recursive(i+1, nums[i]) + 1
                res = max(res, recursive(i+1, prev))
                dp[(i, prev)] = res
                return res
            res = recursive(0, -float('inf'))
            # print(res)
            return res


        nums = []
        n = len(arr)
        for i in range(0, k):
            nums.append([])
            for j in range(i, n, k):
                nums[i].append(arr[j])
        # print(nums)
        
        res = 0
        for subNums in nums:
            size = len(subNums)
            res += size - getLongestNondecreSubseq(subNums)
        return res

# solution no.1 greedy, failed.
class Solution:
    def kIncreasing(self, arr: List[int], k: int) -> int:
        nums = []
        n = len(arr)
        for i in range(0, k):
            nums.append([])
            for j in range(i, n, k):
                nums[i].append(arr[j])
        # print(nums)
        
        res = 0
        for subNums in nums:
            l, r = 0, 1
            size = len(subNums)
            while r < size:
                # print(l, r)
                if subNums[r] >= subNums[r-1]:
                    length = r-l
                    res += length-1
                    l = r
                r += 1
            # print(l, r)
            res += r-l-1
        return res 