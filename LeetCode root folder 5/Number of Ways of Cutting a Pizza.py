# O(rows*cols*k*rows*cols), worst 625000: 84%
class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        row, col = len(pizza), len(pizza[0])
        MOD = 10**9 + 7

        @cache
        def recursive(t, b, l, r, k):
            if k == 0:
                for i in range(t, b+1):
                    for j in range(l, r+1):
                        if pizza[i][j] == 'A': return 1
                return 0
            res = 0
            i = t
            while i < b:
                cnt = 0
                for j in range(l, r+1):
                    if pizza[i][j] == 'A':
                        cnt+=1
                        break
                if cnt: break
                i+=1
            while i < b:
                res += recursive(i+1, b, l, r, k-1)
                i += 1
            i = l
            while i < r:
                cnt = 0
                for j in range(t, b+1):
                    if pizza[j][i] == 'A':
                        cnt+=1
                        break
                if cnt: break
                i += 1
            while i < r:
                res += recursive(t, b, i+1, r, k-1)
                i += 1
            res %= MOD
            return res

        return recursive(0, row-1, 0, col-1, k-1)