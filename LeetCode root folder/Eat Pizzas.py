# incomplete
'''class Solution:
    def maxWeight(self, pizzas: List[int]) -> int:
        pizzas.sort()
        l = len(pizzas)
        count = 0
        res = 0
        total = 0
        print(pizzas)
        while True:
            if total == l // 4:
                break
            count += 1
            if count % 2 == 1:
                res += pizzas.pop()
            else:
                if total == l // 4 - 1:
                    return res + pizzas[-2]
                pizzas.pop(-2)
                res += pizzas.pop(-2)
            total += 1
        return res
# -----------------------------------------------
class Solution:
    def maxWeight(self, pizzas: List[int]) -> int:
        l = len(pizzas)
        def backtrack(idx, s1, s2):
            nonlocal l
            if s1 + s2 == l // 4 and abs(s1-s2) <= 1:
                return 0
            if s1 > ceil(l / 8) or s2 > ceil(l / 8):
                return -float('inf')
            if idx < 0:
                return -float('inf')

            return max(
                backtrack(idx-1, s1+1, s2) + pizzas[idx],
                backtrack(idx-2, s1, s2+1) + pizzas[idx-1]
            )
        return backtrack(l-1, 0, 0)'''


# finally, have mercy on my brain cell!!!
class Solution:
    def maxWeight(self, pizzas: List[int]) -> int:
        pizzas.sort()
        limit = len(pizzas) // 4 + len(pizzas) // 8
        # print(limit)
        # i only need to focus on the top(max) limit-th element
        count = len(pizzas) // 8
        idx = len(pizzas) - limit + 1
        sum_ = sum(pizzas[-limit:])
        while count:
            count -= 1
            sum_ -= pizzas[idx]
            idx += 2
        return sum_