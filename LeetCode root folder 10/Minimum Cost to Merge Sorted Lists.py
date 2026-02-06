# merge sort replace sortedlist doing precomputation, pushed forward another 30 some testcases
class Solution:
    def minMergeCost(self, lists: List[List[int]]) -> int:
        n = len(lists)
        mp = [[0, 0] for _ in range(1 << n)]

        def helper(i, msk, ar):
            if ar: mp[msk] = [len(ar), ar[(len(ar)-1)//2]]
            if i >= n: return
            br = lists[i]
            cr = []
            i1, i2 = 0, 0
            while i1 < len(ar) and i2 < len(br):
                if ar[i1] <= br[i2]:
                    cr.append(ar[i1])
                    i1 += 1
                else:
                    cr.append(br[i2])
                    i2 += 1
            while i1 < len(ar):
                cr.append(ar[i1])
                i1 += 1
            while i2 < len(br):
                cr.append(br[i2])
                i2 += 1

            helper(i + 1, msk, ar)
            helper(i + 1, msk | 1 << i, cr)

        helper(0, 0, [])
        # print(mp)

        dp = [inf] * (1 << n)
        for msk in range(1 << n):
            if msk.bit_count() == 1:
                dp[msk] = 0
                continue
            m1 = msk
            while (m1 - 1) & msk:
                m1 = (m1 - 1) & msk
                m2 = msk ^ m1
                a = dp[m1] + dp[m2]
                s1, med1 = mp[m1]
                s2, med2 = mp[m2]
                # print(m1, m2, a)
                dp[msk] = min(dp[msk], a + s1 + s2 + abs(med1 - med2))
        return dp[(1 << n) - 1]




# TLE. a good introduction problem to DP over subset, still optimizing (if I know SOS I can optimize right away)
# now the bottleneck is the precomputation, not the dp part
class Solution:
    def minMergeCost(self, lists: List[List[int]]) -> int:
        n = len(lists)
        sl = SortedList()
        mp = [[0, 0] for _ in range(1<<n)]
        def helper(i, msk):
            if sl: mp[msk] = [len(sl), sl[(len(sl)-1)//2]]
            if i >= n: return
            helper(i+1, msk)
            for v in lists[i]: sl.add(v)
            helper(i+1, msk|1<<i)
            for v in lists[i]: sl.remove(v)
        helper(0, 0)
        # print(mp)

        dp = [inf]*(1<<n)
        for msk in range(1<<n):
            if msk.bit_count() == 1:
                dp[msk] = 0
                continue
            m1 = msk
            while (m1-1)&msk:
                m1 = (m1-1)&msk
                m2 = msk^m1
                s1, med1 = mp[m1]
                s2, med2 = mp[m2]
                # print(m1, m2, a)
                dp[msk] = min(dp[msk], dp[m1] + dp[m2]+s1+s2+abs(med1-med2))
        return dp[(1<<n)-1]