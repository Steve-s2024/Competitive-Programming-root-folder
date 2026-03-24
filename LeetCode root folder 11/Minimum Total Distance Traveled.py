# so easy? 20 minutes solved this 2455 question...

class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:

        n, m = len(robot), len(factory)
        robot.sort()
        factory.sort()
        @cache
        def fn(i, j):
            if i >= n: return 0
            if j >= m: return inf

            pos, lim = factory[j]
            sm = 0
            res = fn(i, j+1)
            for k in range(i, min(n, i+lim)):
                sm += abs(pos-robot[k])
                res = min(res, fn(k+1, j+1)+sm)

            return res
        return fn(0, 0)


