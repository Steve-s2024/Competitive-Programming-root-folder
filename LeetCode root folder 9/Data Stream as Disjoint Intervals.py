# pretty boring binary search solution


class SummaryRanges:

    def __init__(self):
        ar = []
        self.ar = ar

    def addNum(self, v: int) -> None:
        ar = self.ar
        l, r = 0, len(ar) - 1
        le, ri = -1, len(ar)
        while l <= r:
            m = (l + r) // 2
            if ar[m][1] < v:
                le = m
                l = m + 1
            else:
                r = m - 1

        l, r = 0, len(ar) - 1
        while l <= r:
            m = (l + r) // 2
            if ar[m][0] > v:
                ri = m
                r = m - 1
            else:
                l = m + 1
        if ri - le > 1: return  # already in interval
        f = 1
        if le != -1 and ar[le][1] + 1 == v:  # join left
            f = 0
            ar[le][1] = v
        if ri != len(ar) and ar[ri][0] - 1 == v:  # join right
            f = 0
            ar[ri][0] = v
        if le != -1 and ri != len(ar) and ar[le][1] == ar[ri][0]:  # combine to one
            ar[le][1] = ar[ri][1]
            ar.pop(ri)

        if f: ar.insert(le + 1, [v, v])
        # print(ar)

    def getIntervals(self) -> List[List[int]]:
        return self.ar
