# log trick, O(nlog^2n)
class Solution:
    def closestToTarget(self, arr: List[int], target: int) -> int:
        n = len(arr)
        B = max(arr).bit_length() + 1

        suf = [[] for _ in range(n)]
        ar = [n] * B

        for i in range(n - 1, -1, -1):
            suf[i] = ar[:]
            for j in range(B):
                if 1 << j & arr[i] == 0: ar[j] = i
        # print(suf)

        res = inf
        for i in range(n):
            t = arr[i]
            idx = i
            while idx < n:
                t &= arr[idx]
                res = min(res, abs(target - t))
                mi = n
                for j in range(B):
                    if 1 << j & t: mi = min(mi, suf[i][j])
                idx = mi

        return res



