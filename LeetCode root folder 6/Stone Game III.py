# so many pitfalls in this question... I actually can't beat the old submission: 10%
class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        @cache
        def recursive(i, turn):
            nonlocal n
            if i>=n: return [0, 0]
            tot = 0
            res = [-inf, -inf]
            for j in range(3):
                if i+j >= n: break
                tot += stoneValue[i+j]
                if turn:
                    #alice
                    a = recursive(i+j+1, not turn)
                    if res[0] < a[0]+tot:
                        res = a[:]
                        res[0] += tot
                else:
                    #bob
                    b = recursive(i+j+1, not turn)
                    if res[1] < b[1]+tot:
                        res = b[:]
                        res[1] += tot
            return res

        res = recursive(0, True)
        if res[0] == res[1]: return 'Tie'
        if res[0] > res[1]: return 'Alice'
        return 'Bob'