# dp solution:803
# ms
# Beats
# 5.24%
# this is linear, but there should be a constant solution, probably greedy.
class Solution:
    def countHousePlacements(self, n: int) -> int:
        dp = {}
        def recursive(p, prev):
            if p > n:
                return 1
            if (p, prev) in dp:
                return dp[(p, prev)]
            total = 0
            if prev == 0:
                total += recursive(p+1, 1)
            total += recursive(p+1, 0)
            dp[(p, prev)] = total
            return total
        return recursive(1, 0) ** 2 % (pow(10, 9) + 7)

# no, there are only linear solutions. but the best way is to use fibonacci sequence. this question is just a variation
# of the different ways to walk a staircase, and they kind of share the same solution
