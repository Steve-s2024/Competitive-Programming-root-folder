# the functionalities are trivial and not sophisticated, but the annoying thing is it mix up a bunch of small and distinct
# logic for you to implement, which is manifested by the annoying edge cases. fortunately I know sorted list, which
# really helped me release some of the burden: 17%
class Item:
    def __init__(self, s, m, p):
        self.s = s
        self.m = m
        self.p = p

    def __lt__(self, other):
        if self.p == other.p: return self.s < other.s
        return self.p < other.p

    def __eq__(self, other):
        return self.s == other.s and self.m == other.m and self.p == other.p

class Item2:
    def __init__(self, s, m, p):
        self.s = s
        self.m = m
        self.p = p

    def __lt__(self, other):
        if self.p == other.p:
            if self.s == other.s: return self.m < other.m
            return self.s < other.s
        return self.p < other.p

    def __eq__(self, other):
        return self.s == other.s and self.m == other.m and self.p == other.p



class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]]):
        mMp = defaultdict(SortedList)
        pMp = {}
        for s, m, p in entries:
            mMp[m].add(Item(s, m, p))
            pMp[(s, m)] = p
        self.mMp = mMp
        self.pMp = pMp
        rented = SortedList()
        self.rented = rented

    def search(self, movie: int) -> List[int]:
        mMp = self.mMp
        res = []
        for i in range(min(len(mMp[movie]), 5)):
            res.append(mMp[movie][i].s)
        return res

    def rent(self, shop: int, movie: int) -> None:
        p = self.pMp[(shop, movie)]
        mMp = self.mMp
        mMp[movie].remove(Item(shop, movie, p))
        self.rented.add(Item2(shop, movie, p))

    def drop(self, shop: int, movie: int) -> None:
        mMp = self.mMp
        p = self.pMp[(shop, movie)]
        mMp[movie].add(Item(shop, movie, p))
        self.rented.remove(Item2(shop, movie, p))

    def report(self) -> List[List[int]]:
        rented = self.rented
        res = []
        for i in range(min(len(rented), 5)):
            res.append((rented[i].s, rented[i].m))
        return res