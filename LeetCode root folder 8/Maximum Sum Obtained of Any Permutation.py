# difference array: 15%

class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        arr = [0] * n
        for l, r in requests:
            arr[l] += 1
            if r < n - 1: arr[r + 1] -= 1

        mp = defaultdict(int)
        tot = 0
        for v in arr:
            tot += v
            mp[tot] += 1

        pair = list(mp.items())
        pair.sort(reverse=True)
        nums.sort(reverse=True)
        res = 0
        j = 0
        MOD = 10 ** 9 + 7
        for i in range(len(pair)):
            cnt, cap = pair[i]
            sm = 0
            lim = j + cap
            while j < min(lim, n):
                sm += nums[j]
                j += 1
            res += sm * cnt
            res %= MOD
            if j >= n: break
        return res

