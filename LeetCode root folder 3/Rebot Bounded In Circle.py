# true simulation solution, it is definitely 100% not easy to
# realize the heuristic for this problem, I think it deserve to
# be rated above 1800 but not 1500:100%
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        r, c = 0, 0
        coors = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        d = 0
        for char in instructions:
            if char == 'R':
                d = (d + 1) % 4
            elif char == 'L':
                d = ((d + 4) - 1) % 4
            else:
                rr, cc = coors[d]
                r += rr
                c += cc

        return (r, c) == (0, 0) or (r, c) != (0, 0) and d != 0




# simulation, don't plausible ig
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        r, c = 0, 0
        coors = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        d = 0
        for char in instructions:
            if char == 'R':
                d = (d + 1) % 4
            if char == 'L':
                d = ((d + 4) - 1) % 4
            else:
                rr, cc = coors[d]
                r += rr
                c += cc

        return (r, c) == (0, 0)

