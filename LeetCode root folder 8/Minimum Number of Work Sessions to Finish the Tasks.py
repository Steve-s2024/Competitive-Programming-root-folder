# bitmask DP, faster than the old solution by one third: 56%
class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        n = len(tasks)
        @cache
        def recursive(mask):
            nonlocal n
            if mask == (1 << n) - 1: return 0, 0
            micnt, mitot = inf, inf
            for i in range(n):
                if mask & (1 << i): continue
                cnt, tot = recursive(mask | (1 << i))
                if tot + tasks[i] > sessionTime: cnt, tot = cnt + 1, tasks[i]
                else: tot = tot+tasks[i]
                if cnt == micnt: mitot = min(mitot, tot)
                if cnt < micnt: micnt, mitot = cnt, tot
            return micnt, mitot

        return recursive(0)[0] + 1