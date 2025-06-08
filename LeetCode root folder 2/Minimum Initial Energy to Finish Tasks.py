# binary search solution, once you observe the monotonic nature
# of testing each of the remaining energies after all tasks and find
# the minimum, binary search is the solution: 37%
class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        n = len(tasks)
        tasks.sort(key = lambda i : i[1] - i[0])
        l, r = 0, max([e[1] - e[0] for e in tasks])
        res = r

        while l <= r:
            m = (l+r)//2
            # pretend m is the remaining energies after all tasks
            i = 0
            energies = m
            # print(m)
            while i < n:
                [a, b] = tasks[i]
                if b-a <= energies:
                    energies += a
                    i += 1
                else:
                    break
            # print(i)
            # print()
            if i == n:
                res = m
                r = m-1
            else:
                l = m+1

        return sum([e[0] for e in tasks]) + res

