# the solution is kinda tricky to implement, I didn't use seg tree but instead used ordered list:68%
class MyCalendar:

    def __init__(self):
        sl = SortedList()
        sl.add(inf)
        sl.add(-inf)
        self.sl = sl

        mp = {}
        mp[inf] = inf
        mp[-inf] = -inf
        self.mp = mp

    def book(self, startTime: int, endTime: int) -> bool:
        sl = self.sl
        mp = self.mp
        idx = sl.bisect_left(startTime)
        a, b = sl[idx-1], sl[idx]
        c, d = mp[a], mp[b]
        if startTime >= c and endTime <= b:
            mp[startTime] = endTime
            sl.add(startTime)
            return True
        return False

