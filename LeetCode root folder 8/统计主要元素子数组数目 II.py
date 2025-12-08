# 赛中排51 （全球284）， 半个小时all kill。 应该是这个账户打的最好的一场了 杀完AI也可能是有史以来排名最靠前的一场。

class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        sl = SortedList()
        sl.add(1)
        ct = 0
        n = len(nums)
        ans = 0
        for i in range(n):
            if nums[i] == target: ct += 1
            x = 2*ct-i
            a = sl.bisect_left(x)
            ans += a
            sl.add(x)
        return ans