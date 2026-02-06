# meet in half way

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        mp = defaultdict(int)
        res = 0
        for v1 in nums1:
            for v2 in nums2:
                mp[v1+v2] += 1
        for v3 in nums3:
            for v4 in nums4:
                res += mp[-(v3+v4)]
        return res