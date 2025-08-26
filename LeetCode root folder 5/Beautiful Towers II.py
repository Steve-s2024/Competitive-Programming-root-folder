# sometimes it is easy to get the intuition but some other time it is so hard I even doubt how they are rated in the
# same range: 40%
class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        n = len(maxHeights)
        pre = [0] * n
        stk = []
        tot = 0
        for i in range(n):
            cnt = 0
            while stk and stk[-1][0] >= maxHeights[i]:
                h, c = stk.pop()
                tot -= h * c
                cnt += c

            cnt += 1
            tot += maxHeights[i] * cnt
            stk.append((maxHeights[i], cnt))
            pre[i] = tot

        suf = [0] * n
        stk = []
        tot = 0
        for i in range(n - 1, -1, -1):
            cnt = 0
            while stk and stk[-1][0] >= maxHeights[i]:
                h, c = stk.pop()
                tot -= h * c
                cnt += c

            cnt += 1
            tot += maxHeights[i] * cnt
            stk.append((maxHeights[i], cnt))
            suf[i] = tot

        return max(pre[i] + suf[i] - maxHeights[i] for i in range(n))
