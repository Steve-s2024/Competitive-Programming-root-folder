# although i checked the problem tag before diving into it, but end up not using any of it and instead used sliding
# window, maybe because they have changed the question from AND to OR: 18%

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        inf = math.inf
        n = len(nums)
        j = 0
        tot = 0
        mp = [0]*30
        res = inf
        for i in range(n):
            while j < n and tot < k:
                x = nums[j]
                if tot | x >= k and j != i: res = min(res, abs(k-tot))
                tot |= x
                idx = 0
                while x:
                    if x&1: mp[idx] += 1
                    x >>= 1
                    idx += 1
                j += 1
            res = min(res, abs(k-tot))
            x = nums[i]
            idx = 0
            while x:
                if x&1:
                    mp[idx] -= 1
                    if mp[idx] == 0: tot ^= 1<<idx
                x >>= 1
                idx += 1

        return res