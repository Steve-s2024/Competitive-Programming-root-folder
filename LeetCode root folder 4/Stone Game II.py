# stone game usual DP solution, done something similar with other four stone game variation: 44%
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        @cache
        def recursive(i, m, turn):
            nonlocal n
            if i >= n: return 0, 0
            res = [-1, -1]
            tot = 0
            if turn == 0:
                # alice
                for j in range(i, min(n, i+2*m)):
                    tot += piles[j]
                    a, b = recursive(j+1, max(m, j-i+1), 1)
                    if a + tot > res[0]: res = (a+tot, b)
            else:
                # bob
                for j in range(i, min(n, i+2*m)):
                    tot += piles[j]
                    a, b = recursive(j+1, max(m, j-i+1), 0)
                    if b+tot > res[1]: res = (a, b+tot)
            return res
        a, b = recursive(0, 1, 0)
        return a



# greedy attempt a year ago: WA
class Solution():
    def stoneGameII(self, piles):
        if len(piles) < 3:
            return sum(piles)
        l = len(piles)
        summation = 0
        rank = dict()
        maxlist = [0]
        for i in range(l, 0, -1):
            i -= 1
            summation += piles[i]
            j = i
            m = -float('inf')
            while j < l-1:
                # j-i+1 many steps
                # j-i+1*2 and j-i+1 rectangle
                if (j-i+1)*2 not in rank:
                    a = min(maxlist[:j-i+1])
                else:
                    a = min(rank[(j-i+1)*2][:j-i+1])
                m = max(m, summation-a)
                rank[j-i+1] = [m] + rank[j-i+1]
                j += 1

            maxlist = [summation] + maxlist
            rank[l-i] = maxlist[:]
        return max(rank[1][0], rank[2][0])
