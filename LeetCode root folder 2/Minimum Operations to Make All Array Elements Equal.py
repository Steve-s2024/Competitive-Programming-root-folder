# sorting and binary search, prefix sum solution: 45%
class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        m = len(queries)
        ans = [0] * m
        nums.sort()
        prefix = []
        total = 0
        for num in nums:
            total += num
            prefix.append(total)

        for i in range(m):
            target = queries[i]
            if target <= nums[0]:
                res = prefix[-1] - n*target
            elif target >= nums[-1]:
                res = n* target - prefix[-1]
            else:
                l, r = 0, n-1
                while l < r:
                    mid = (r+l)//2
                    if nums[mid] >= target:
                        r = mid
                    else:
                        l = mid+1
                s1, s2 = l, n-l
                diff1, diff2 = s1*target - prefix[s1-1], (prefix[-1] - prefix[s1-1]) - s2*target
                res = diff1 + diff2
            ans[i] = res
        return ans

# brute force: tle
class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        m = len(queries)
        ans = [0] * m
        for i in range(m):
            target = queries[i]
            res = 0
            for j in range(n):
                res += abs(nums[j] - target)
            ans[i] = res
        return ans