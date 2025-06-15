# DP with game theory: 11%
class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        # (i, cnt)
        n = len(stoneValue)
        dp = [[None] * 2 for _ in range(n)]

        def recursive(i, cnt):
            nonlocal n
            if i >= n: return 0, 0
            # if (i, cnt%2) in dp: return dp[(i, cnt%2)]
            if dp[i][cnt % 2] is not None: return dp[i][cnt % 2]

            a, b = -float('inf'), -float('inf')
            if cnt % 2 == 0:
                # alice
                tot = 0
                for j in range(i, min(i + 3, n)):
                    tot += stoneValue[j]
                    A, B = recursive(j + 1, cnt + 1)
                    if A + tot > a:
                        a = A + tot
                        b = B
            else:
                # bob
                tot = 0
                for j in range(i, min(i + 3, n)):
                    tot += stoneValue[j]
                    A, B = recursive(j + 1, cnt + 1)
                    if B + tot > b:
                        b = B + tot
                        a = A

            # dp[(i, cnt%2)] = (a, b)
            dp[i][cnt % 2] = (a, b)
            return a, b

        a, b = recursive(0, 0)
        if a > b: return 'Alice'
        if b > a: return 'Bob'
        return 'Tie'