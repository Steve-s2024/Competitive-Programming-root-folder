# backward simulation, with technique that save time by a factor of n: 10%
class Solution:
    def bestRotation(self, nums: List[int]) -> int:
        mp = defaultdict(int)
        for i, val in enumerate(nums):
            mp[max(0, val-i)] += 1
        tot = 0
        mxScore = -1
        res = -1

        n = len(nums)
        for i in range(n):
            # imagine i is the k
            tot += mp[i]
            if tot >= mxScore:
                mxScore = tot
                res = n-i
            tot -= 1
            mp[i+nums[-i-1]+1] += 1
        if mp[0] == mxScore: return 0
        return res


