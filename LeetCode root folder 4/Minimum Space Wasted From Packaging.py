# for some weird reason modulo the cost will not work, but mod at the end will...
# really peculiar (tin_le give the tip to mod at the end): 5%
# fk it is stupid to mod in progress, just realize the stupidity in it...
from sortedcontainers import SortedList

class Solution:
    def minWastedSpace(self, packages: List[int], boxes: List[List[int]]) -> int:
        n = len(packages)
        packages.sort()
        sl = SortedList()
        pre = [0] * n
        tot = 0
        MOD = 10 ** 9 + 7
        mx = max(packages)
        for i, x in enumerate(packages):
            tot += x
            pre[i] = tot
            sl.add(x)
        # print(pre)
        minCost = float('inf')
        for box in boxes:
            if max(box) < mx:
                continue
            l, r = 0, 0
            cost = 0
            for size in sorted(box):
                r = sl.bisect_right(size)
                if r <= l: continue

                a = (r - l) * size
                b = pre[r - 1] - pre[l] + packages[l]
                cost += a - b
                l = r
            minCost = min(minCost, cost)
        return minCost % MOD if minCost != float('inf') else -1


# WA on second last tc?


class Solution:
    def minWastedSpace(self, packages: List[int], boxes: List[List[int]]) -> int:
        n = len(packages)
        packages.sort()
        sl = SortedList()
        pre = [0] * n
        tot = 0
        MOD = 10 ** 9 + 7
        mx = max(packages)
        for i, x in enumerate(packages):
            tot += x
            pre[i] = tot
            sl.add(x)
        # print(pre)
        minCost = float('inf')
        for box in boxes:
            if max(box) < mx:
                continue
            l, r = 0, 0
            cost = 0
            for size in sorted(box):
                r = sl.bisect_right(size)
                if r <= l: continue

                a = (r - l) * size
                b = pre[r - 1] - pre[l] + packages[l]
                cost += a - b
                cost %= MOD
                l = r
            minCost = min(minCost, cost)
        return minCost if minCost != float('inf') else -1


