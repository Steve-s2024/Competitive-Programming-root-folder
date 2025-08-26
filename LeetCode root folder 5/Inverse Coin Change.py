# feels impossible but not that impossible...
class Solution:
    def findCoins(self, numWays: List[int]) -> List[int]:
        dp = {}

        def recursive(x, i):
            if (x, i) in dp: return dp[(x, i)]
            if x == 0: return 1
            if x < 0: return 0
            if i >= len(cands): return 0
            res = 0
            j = 0
            while j * cands[i] <= x:
                res += recursive(x - cands[i] * j, i + 1)
                j += 1
            dp[(x, i)] = res
            return res

        cands = []
        for i in range(len(numWays)):
            tot = recursive(i + 1, 0)
            dp.clear()
            re = numWays[i] - tot
            if re == 1:
                cands.append(i + 1)
            elif re != 0:
                return []
        return sorted(cands)