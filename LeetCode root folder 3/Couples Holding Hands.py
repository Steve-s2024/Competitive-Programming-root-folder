# does not feel that hard...: 100%
# pretty greedy solution
class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        rec = {}
        n = len(row)
        iMp = {}
        for i in range(n):
            iMp[row[i]] = i

        cnt = 0
        for i in range(0, n, 2):
            if row[i] % 2 == 1:
                ptn = row[i]-1
            else:
                ptn = row[i]+1
            if row[i+1] != ptn:
                # make the swap
                a, b = i+1, iMp[ptn]
                row[a], row[b] = row[b], row[a]
                iMp[row[a]], iMp[row[b]] = a, b
                cnt += 1
        return cnt
