# WA solution; not even able to get TLE

class Solution:
    def minMoves(self, nums: List[int], k: int) -> int:
        n = len(nums)

        Dsts = [0] * n
        Sms = [0] * n
        for i in range(n):
            Dsts[i] = Dsts[i - 1] + (i if nums[i] else 0)
            Sms[i] = Sms[i - 1] + nums[i]

        Dsts2 = [0] * n
        Sms2 = [0] * n
        for i in range(n - 1, -1, -1):
            Dsts2[i] = Dsts2[(i + 1) % n] + (n - 1 - i if nums[i] else 0)
            Sms2[i] = Sms2[(i + 1) % n] + nums[i]

        res = 1 << 31
        for i in range(n):
            l, r = i, n - 1
            while l <= r:
                m = (l + r) // 2
                sm = Sms[m] - Sms[i]
                dst = Dsts[m] - Dsts[i] - i * sm - sm * (sm + 1) // 2

                L, R = 0, i
                tp = -1
                while L <= R:
                    M = (L + R) // 2
                    SM = Sms2[M] - Sms2[i]
                    DST = Dsts2[M] - Dsts2[i] - (n - 1 - i) * SM - SM * (SM + 1) // 2
                    if sm + SM + nums[i] >= k:
                        cst = dst + DST + (min(sm, SM) if nums[i] == 0 else 0)
                        res = min(res, cst)
                        tp = DST
                        L = M + 1
                    else:
                        R = M - 1
                # if i in range(5, 8): print(i, M, m, tp, dst)
                if tp == -1 or tp > dst: l = m + 1
                else: r = m - 1
        return res