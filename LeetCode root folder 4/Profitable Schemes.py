# a heuristic to make the minProfit always positive, and therefore reduce the
# number of states by a factor of at most 100.
# basically the minProfit nolonger need to be part of the state once it becomes zero (or belong)
# so for the sake of simplicity just make it always 0, and consequently make the state become 2D (i, n)
# : 50% (the version with hash set DP beets 25%)
class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:

        dp = [[[-1] * (minProfit + 1) for _ in range(n + 1)] for _ in range(len(profit))]
        # dp = {}
        MOD = 10 ** 9 + 7

        def recursive(i, n, minProfit):
            nonlocal MOD
            if i >= len(profit):
                return 1 if minProfit <= 0 else 0

            if dp[i][n][minProfit] != -1:
                return dp[i][n][minProfit]
            # if (i, n, minProfit) in dp:
            #     return dp[(i, n, minProfit)]

            res = recursive(i + 1, n, minProfit)
            if n >= group[i]:
                res += recursive(i + 1, n - group[i], max(0, minProfit - profit[i]))
            res %= MOD
            dp[i][n][minProfit] = res
            # dp[(i, n, minProfit)] = res
            return res

        return recursive(0, n, minProfit)


# Knap-sack brute force with dp: MLE
class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:

        # dp = [[0]*len(profit) for _ in range(n+1) for _ in range(minProfit+1)]
        dp = {}
        MOD = 10 ** 9 + 7

        def recursive(i, n, minProfit):
            nonlocal MOD
            if i >= len(profit):
                return 1 if minProfit <= 0 else 0

            # if dp[i][n][minProfit]:
            #     return dp[i][n][minprofit]
            if (i, n, minProfit) in dp:
                return dp[(i, n, minProfit)]

            res = recursive(i + 1, n, minProfit)
            if n >= group[i]:
                res += recursive(i + 1, n - group[i], minProfit - profit[i])
            # dp[i][n][minProfit] = res
            res %= MOD
            dp[(i, n, minProfit)] = res
            return res

        return recursive(0, n, minProfit)



