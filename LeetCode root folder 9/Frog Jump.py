# quite a brain twister, could not think straight in this problem, but did come up with a solution that is not bad
# turn out it is knap sack (with binary search / precomputation), but I could not realize and somehow invented this approach

class Solution:
    def canCross(self, ar: List[int]) -> bool:
        if len(ar) <= 2: return ar[1] == ar[0]+1
        n = len(ar)
        mp = [set() for _ in range(n)]

        for i in range(n-2, -1, -1):
            x = ar[-1]-ar[i]
            mp[i].add(x)
            mp[i].add(x-1)
            mp[i].add(x+1)
            for j in range(i+1, n):
                x = ar[j]-ar[i]
                if x in mp[j]:
                    mp[i].add(x-1)
                    mp[i].add(x)
                    mp[i].add(x+1)
        # print(mp)
        # return 1 in mp[0]
        idx = 1
        while idx < n and ar[idx] < ar[0]+1: idx+=1
        if idx >= n: return False

        return 1 in mp[idx] and ar[idx]-ar[0] == 1