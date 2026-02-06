# insanely powerful probability knowledge helped me come up with a solution to this...
class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0: return 1
        dp = [0]*(k+maxPts)
        dp[0] = 1
        pre = [1]
        for i in range(1, k+maxPts):
            if i < k: a, b = pre[i-maxPts-1] if i > maxPts else 0, pre[i-1]
            else: a, b = pre[i-maxPts-1] if i > maxPts else 0, pre[k-1]
            dp[i] += (b-a)/maxPts
            pre.append(pre[-1] + dp[i])

            # if i < k:
            #     for j in range(max(0, i-maxPts), i): dp[i] += dp[j]/maxPts
            # else:
            #     for j in range(max(0, i-maxPts), k): dp[i] += dp[j]/maxPts

        # print(dp)
        nu, de = 0, 0
        for i in range(k, min(n+1, k+maxPts)): nu += dp[i]
        for i in range(k, k+maxPts): de += dp[i]
        return nu/de
