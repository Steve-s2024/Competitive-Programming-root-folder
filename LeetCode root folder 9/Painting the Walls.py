# freaking genius trick, I can't think like this at the moment. (credit neetcode)
class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n = len(cost)

        @cache
        def recursive(i, tx):
            nonlocal n
            if tx >= n: return 0
            if i >= n: return inf
            a = recursive(i + 1, tx)
            b = recursive(i + 1, tx+time[i]+1) + cost[i]
            return min(a, b)

        res = recursive(0, 0)
        recursive.cache_clear()
        return res

# MLE
class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n = len(cost)

        @cache
        def recursive(i, t, x):
            nonlocal n
            if t + x >= n: return 0
            if i >= n: return inf
            a = recursive(i + 1, t, x)
            b = recursive(i + 1, t + time[i], x + 1) + cost[i]
            return min(a, b)

        res = recursive(0, 0, 0)
        recursive.cache_clear()
        return res


