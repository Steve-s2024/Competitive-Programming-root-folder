# greedy solution:43
# ms
# Beats
# 90.67%
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l, r = 0, len(people) - 1
        boat = 0
        while l < r:
            if people[l] + people[r] <= limit:
                boat += 1
                l += 1
                r -= 1
            else:
                boat += 1
                r -= 1

        if l == r:
            boat += 1
        return boat