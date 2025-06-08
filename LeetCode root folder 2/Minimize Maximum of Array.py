

# optimized binary search, but slower?: 10%

class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, max(nums)
        res = r
        while l <= r:
            m = (r+l)//2
            # pretend m is the minimum max(nums) after operations
            owe = 0
            for i in range(n-1, -1, -1):
                if nums[i] > m:
                    owe += nums[i] - m
                else:
                    owe -= m - nums[i]
                    owe = max(owe, 0)
            if owe > 0:
                l = m+1
            else:
                res = m
                r = m-1
        return res
                



# binary search and greedy solution: 18%

class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, max(nums)
        res = r
        while l <= r:
            m = (r+l)//2
            # pretend m is the minimum max(nums) after operations
            tmp = nums[:]
            for i in range(n-1, 0, -1):
                if tmp[i] > m:
                    diff = tmp[i]-m
                    tmp[i] = m
                    tmp[i-1] += diff
            # print(m, tmp)
            if tmp[0] > m:
                l = m+1
            else:
                res = m
                r = m-1
        return res
                

