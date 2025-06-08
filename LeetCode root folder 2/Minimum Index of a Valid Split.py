# simple prefix sum implementation: 86%
class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        frq = Counter(nums)
        cnt = 0
        dmnt = None
        n = len(nums)
        for key, val in frq.items():
            if 2*val > n:
                dmnt = key
                cnt = val
                break
        total = 0
        for i in range(n):
            if nums[i] == dmnt:
                total += 1
                l, r = total, cnt - total
                s1, s2 = i+1, n-1-i
                if 2*l > s1 and 2*r > s2:
                    return i
        return -1