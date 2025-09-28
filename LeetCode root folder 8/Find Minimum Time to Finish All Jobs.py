# improved bitmask DP solution, instead of producing all the permutation of 12 sized array, I do the bitmask and
# get from 12! to 2**12 complex, multiply by the binary search, which is log(10**8) in worst case. it's a passing
# solution, but not the intended one since many people finished 28ms: 14% 3398ms
class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        n = len(jobs)

        @cache
        def recursive(mask, m):
            nonlocal n
            if mask == (1 << n) - 1: return 0, 0

            micnt, mitot = inf, inf
            for i in range(n):
                if mask & (1 << i): continue
                cnt, tot = recursive(mask | (1 << i), m)
                if tot + jobs[i] > m:
                    cnt, tot = cnt + 1, jobs[i]
                else:
                    tot += jobs[i]
                if micnt == cnt: mitot = min(mitot, tot)
                if micnt > cnt: micnt, mitot = cnt, tot
            return micnt, mitot

        res = -1
        l, r = max(jobs), sum(jobs)
        while l <= r:
            m = (l + r) // 2
            cnt, tot = recursive(0, m)
            if cnt + 1 <= k:
                res = m
                r = m-1
            else: l = m+1
        return res




# bit brute forcing binary search solution: MLE TLE
class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        n = len(jobs)
        ref = []
        stk = []

        def recursive(mask):
            nonlocal n
            if mask == (1 << n) - 1:
                ref.append(stk[:])
                return

            for i in range(n):
                if mask & (1 << i): continue
                stk.append(i)
                recursive(mask | (1 << i))
                stk.pop()

        recursive(0)
        # print(ref)

        res = -1
        l, r = max(jobs), sum(jobs)
        while l <= r:
            m = (l + r) // 2
            for arr in ref:
                tot = 0
                cnt = 1
                for i in arr:
                    num = jobs[i]
                    if tot + num > m:
                        tot = num
                        cnt += 1
                    else:
                        tot += num
                if cnt <= k:
                    # print(m, cnt)
                    # print(arr)
                    break
            else:
                l = m + 1
                continue
            res = m
            r = m - 1
        return res



