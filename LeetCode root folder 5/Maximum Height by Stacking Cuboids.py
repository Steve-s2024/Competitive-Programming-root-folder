# the intuition for this approach is very hard to spot, credit for chat, greedy solution with sorting and DP: 95%
class Solution:
    def maxHeight(self, cuboids: List[List[int]]) -> int:
        for c in cuboids: c.sort()
        cuboids.sort()

        n = len(cuboids)
        dp = [0]*n
        for i in range(n):
            A, B, C = cuboids[i]
            dp[i] = C
            for j in range(i):
                a, b, c = cuboids[j]
                if a <= A and b <= B and c <= C:
                    dp[i] = max(dp[i], dp[j]+C)
        return max(dp)

