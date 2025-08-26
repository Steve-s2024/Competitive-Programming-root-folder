# solution credit to NeetCode, sliding window with three pointers: 43%
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        n = len(nums)
        mp = defaultdict(int)
        mp2 = defaultdict(int)
        l, r = 0, 0
        res = 0

        for i in range(n):
            mp[nums[i]] += 1
            mp2[nums[i]] += 1

            while len(mp) > k:
                mp[nums[l]] -= 1
                if mp[nums[l]] == 0: mp.pop(nums[l])
                l += 1

            while len(mp2) >= k:
                mp2[nums[r]] -= 1
                if mp2[nums[r]] == 0: mp2.pop(nums[r])
                r += 1
            # print(i)
            # print(l, r)
            res += r - l

        return res
