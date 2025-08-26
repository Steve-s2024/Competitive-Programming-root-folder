# very crazy inefficient sorted list implementation, but luckily passed O(n^2logn): 6%

class Solution:
    def sumImbalanceNumbers(self, nums: List[int]) -> int:
        n = len(nums)
        inf = math.inf
        res = 0
        for i in range(n):
            sl = SortedList(nums[:i])
            cnt = 0
            for j in range(len(sl)-1):
                if sl[j+1]-sl[j] > 1: cnt += 1

            for j in range(i, n):
                pos = sl.bisect_left(nums[j])
                sl.add(nums[j])
                a, b = sl[pos-1] if pos > 0 else inf, sl[pos+1] if pos < len(sl)-1 else inf
                if a != inf and nums[j]-a > 1: cnt += 1
                if b != inf and b-nums[j] > 1: cnt += 1
                if inf not in [a, b] and b-a > 1: cnt -= 1
                res += cnt

                pos = sl.bisect_left(nums[j-i])
                a, b = sl[pos-1] if pos > 0 else inf, sl[pos+1] if pos < len(sl)-1 else inf
                if a != inf and nums[j-i]-a > 1: cnt -= 1
                if b != inf and b-nums[j-i] > 1: cnt -= 1
                if inf not in [a, b] and b-a > 1: cnt += 1
                sl.remove(nums[j-i])

        return res