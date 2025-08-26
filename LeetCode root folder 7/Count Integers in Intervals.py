# not hard interval merging question, sometime the rating is overrated: 64%
class CountIntervals:

    def __init__(self):
        sl = SortedList()
        self.sl = sl
        self.cnt = 0

    def add(self, left: int, right: int) -> None:
        sl = self.sl
        cnt = self.cnt
        pos = sl.bisect_left((left, 0))
        l, r = left, right
        if pos and sl[pos - 1][1] >= left:
            pos -= 1
            L, R = sl.pop(pos)
            cnt -= (R - L + 1)
            l = L
            r = max(r, R)

        while pos < len(sl) and sl[pos][0] <= r:
            L, R = sl.pop(pos)
            cnt -= (R - L + 1)
            r = max(right, R)
        sl.add((l, r))
        cnt += (r - l + 1)
        self.cnt = cnt

    def count(self) -> int:
        return self.cnt
