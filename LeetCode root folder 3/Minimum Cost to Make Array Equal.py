# somewhat intuitive prefix sum solution: 58%
class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        pairs = []
        n = len(nums)
        for i in range(n):
            pairs.append((nums[i], cost[i]))

        pairs.sort(key=lambda i: i[0])

        sm = pairs[-1][1]
        prev = pairs[-1][0]
        tot = 0
        suf = [0] * n
        for i in range(n - 2, -1, -1):
            num, cos = pairs[i]
            tot += sm * (prev - num)
            suf[i] = tot
            sm += cos
            prev = num

        sm = pairs[0][1]
        prev = pairs[0][0]
        tot = 0
        pre = [0] * n
        for i in range(1, n):
            num, cos = pairs[i]
            tot += sm * (num - prev)
            pre[i] = tot
            sm += cos
            prev = num
        # print(suf, pre)

        mi = pre[0] + suf[0]
        for i in range(n):
            mi = min(mi, pre[i] + suf[i])
        return mi