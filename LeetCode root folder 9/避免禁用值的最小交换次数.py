# 真的完全是被直觉带着走， 一条路贪到底。 最后居然真给贪出来了...
class Solution:
    def minSwaps(self, nums: List[int], forb: List[int]) -> int:
        n = len(nums)
        ar = []
        for i in range(n):
            if nums[i] == forb[i]: ar.append(nums[i])

        mp = Counter(ar)
        tr = -1
        mx = -1
        for key, val in mp.items():
            if val > mx:
                mx = val
                tr = key
        ct1 = Counter(nums)[tr]
        ct2 = Counter(forb)[tr]
        # print(tr, ct, mp[tr])
        x = n-ct1 - (ct2-mp[tr])
        if x < mp[tr]: return -1
        x = mp[tr]
        if x <= len(ar)//2: return (len(ar)+1)//2
        res = len(ar)-x
        x -= len(ar)-x
        res += x
        return res