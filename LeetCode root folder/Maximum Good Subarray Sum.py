# a tiny change of the prev, after realizing some detail: 30%
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        prefix = []
        total = 0
        n = len(nums)
        for num in nums:
            total += num
            prefix.append(total)
        
        hashMap = defaultdict(int)
        res = -float('inf')
        for i in range(n):
            cur = nums[i]
            a, b = cur - k, cur + k
            maxSum = -float('inf')
            if a in hashMap:
                maxSum = prefix[i] - hashMap[a] + a
            if b in hashMap:
                maxSum = max(maxSum, prefix[i] - hashMap[b] + b)

            res = max(res, maxSum)
            if cur not in hashMap:
                hashMap[cur] = prefix[i]
            else:
                hashMap[cur] = min(hashMap[cur], prefix[i])
        if res == -float('inf'):
            return 0
        return res



# another failed attempt
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        prefix = []
        total = 0
        for num in nums:
            total += num
            prefix.append(total)
    
        hashMap = defaultdict(list)
        res = -float('inf')
        map2 = {}
        for i in range(len(nums)):
            cur = nums[i]
            a, b = cur - k, cur + k
            maxSum = -float('inf')
            for prevI in hashMap[a]:
                maxSum = max(maxSum, prefix[i]-prefix[prevI]+a)
            for prevI in hashMap[b]:
                maxSum = max(maxSum, prefix[i]-prefix[prevI]+b)
            if cur in map2:
                [prevSum, prevI] = map2[cur]
                maxSum = max(maxSum, prevSum+(prefix[i]-prefix[prevI]))
            map2[cur] = (maxSum, i)
            hashMap[a].clear()
            hashMap[b].clear()
            hashMap[cur].append(i)
        if res == -float('inf'):
            return 0
        return res

# prefix & hashing: tle
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        prefix = []
        total = 0
        for num in nums:
            total += num
            prefix.append(total)
    
        hashMap = defaultdict(list)
        res = -float('inf')
        for i in range(nums):
            cur = nums[i]
            a, b = cur - k, cur + k

            maxSum = -float('inf')
            for prevI in hashMap[a]:
                maxSum = max(maxSum, prefix[i]-prefix[prevI]+a)
            for prevI in hashMap[b]:
                maxSum = max(maxSum, prefix[i]-prefix[prevI]+b)
            res = max(res, maxSum)
            hashMap[nums].append(i)
        return res