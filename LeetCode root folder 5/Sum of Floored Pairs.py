# very hard to analyze the time complexity, O(nlogn) cause 1+1/2+1/3...+1/n is about logn: 7%
class Solution:
    def sumOfFlooredPairs(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        mp = Counter(nums)
        sl = SortedList(mp.keys())
        res = 0
        mx = max(nums)
        pre = [0]
        for val in sl: pre.append(mp[val]+pre[-1])
        pre.append(pre[-1]+mp[sl[-1]])
        for key, val in mp.items():
            prev = 0
            cnt = 0
            for m in range(key, mx+key+1, key):
                pos = sl.bisect_left(m)
                res += (pre[pos]-pre[prev])*cnt*val
                res %= MOD
                prev = pos
                cnt += 1
        return res


# TLE
class Solution:
    def sumOfFlooredPairs(self, nums: List[int]) -> int:
        sl = SortedList(nums)
        res = 0
        mx = max(nums)
        MOD = 10**9 + 7
        for num in nums:
            prev = 0
            cnt = 0
            for m in range(num, mx+num+1, num):
                pos = sl.bisect_left(m)
                res += (pos-prev)*cnt
                res %= MOD
                prev = pos
                cnt += 1
        return res
