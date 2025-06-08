# nice binary array manipulation question: 38%

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        bi = []
        n = len(nums)
        for num in nums:
            bi.append(1 if num > k else -1)
        mp = defaultdict(int)
        mp[0] = 1
        tot = 0
        idx = 0
        for i, b in enumerate(bi):
            if nums[i] == k:
                idx = i
                break
            tot += b
            mp[tot] += 1

        res = 0
        for i in range(idx, n):
            tot += bi[i]
            res += mp[tot] + mp[tot + 1]

        return res


