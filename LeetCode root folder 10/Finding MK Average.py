# finding the things that matter, the things that will be affected when adding a new element,
# the things that will affect MK average when new element is added,
# turns out only 1 or 2 number will be affecting the average, so focus on them

class MKAverage:

    def __init__(self, m: int, k: int):
        self.m, self.k = m, k
        self.q = deque()
        self.sl = SortedList()
        self.sm = 0

    def addElement(self, num: int) -> None:
        m, q, k, sl, sm = self.m, self.q, self.k, self.sl, self.sm
        q.append(num)
        sl.add(num)
        size = len(sl)
        if size > 2*k:
            i = sl.bisect_left(num)
            if i<=k-1: sm += sl[k]
            elif i>=size-k: sm += sl[size-k-1]
            else: sm += num

        if len(q) > m:
            x = q.popleft()
            i = sl.bisect_left(x)
            size = len(sl)
            if size > 2*k:
                l, r = sl[k], sl[size-k-1]
                if i<=k-1: sm -= l
                elif i>=size-k: sm -= r
                else: sm -= x
            sl.remove(x)
        # print(sm)
        self.sm = sm

    def calculateMKAverage(self) -> int:
        q, m, k, sm = self.q, self.m, self.k, self.sm
        if len(q) < m: return -1
        return sm//(m-2*k)
