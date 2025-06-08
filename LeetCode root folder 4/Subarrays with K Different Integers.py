# : 5%
class Solution:
    @staticmethod
    def getSubarrayCnt(nums, k):
        if k == 0:
            return 0
        mp = defaultdict(int)
        res = 0
        n = len(nums)
        j = 0
        for i in range(n):
            while j < n and len(mp) <= k:
                mp[nums[j]] += 1
                j += 1
            if len(mp) > k:
                j -= 1
                mp[nums[j]] -= 1
                if mp[nums[j]] == 0:
                    mp.pop(nums[j])

            res += j - i
            mp[nums[i]] -= 1
            if mp[nums[i]] == 0:
                mp.pop(nums[i])
        return res

    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        a, b = Solution.getSubarrayCnt(nums, k), Solution.getSubarrayCnt(nums, k - 1)
        print(a, b)
        return a - b


