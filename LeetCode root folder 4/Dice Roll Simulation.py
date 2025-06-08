# easy as hell DP problem, don't know why its rated 2008: 45%

class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        @cache
        def recursive(i, cur, cnt):
            nonlocal n
            if i >= n:
                return 1
            res = 0
            for nxt in range(1, 7):
                if nxt == cur and cnt >= rollMax[cur-1]:
                    continue
                if nxt == cur:
                    res += recursive(i + 1, nxt, cnt + 1)
                else:
                    res += recursive(i + 1, nxt, 1)
            res %= 10**9 + 7
            return res
        return sum(recursive(1, die, 1) for die in range(1, 7)) % (10**9 + 7)

# using dp, but 
class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        dp = [[[0]*16 for _ in range(7)] for _ in range(n)]
        def recursive(i, cur, cnt):
            nonlocal n
            if i >= n:
                return 1
            if dp[i][cur][cnt] != 0:
                return dp[i][cur][cnt]
            res = 0
            for nxt in range(1, 7):
                if nxt == cur and cnt >= rollMax[cur-1]:
                    continue
                if nxt == cur:
                    res += recursive(i + 1, nxt, cnt + 1)
                else:
                    res += recursive(i + 1, nxt, 1)
            res %= 10**9 + 7
            dp[i][cur][cnt] = res
            return res
        return sum(recursive(1, die, 1) for die in range(1, 7)) % (10**9 + 7)
