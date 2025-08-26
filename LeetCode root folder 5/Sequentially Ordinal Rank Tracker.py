# SortedList function better than sorted set and crushed this question: 34%
class SORTracker:

    def __init__(self):
        self.sl = SortedList()
        self.cnt = 0

    def add(self, name: str, score: int) -> None:
        sl = self.sl
        sl.add(A(score, name))

    def get(self) -> str:
        sl = self.sl
        self.cnt += 1
        return sl[self.cnt - 1].name


class A:
    def __init__(self, score, name):
        self.name = name
        self.score = score

    def __lt__(self, p):
        if self.score == p.score: return self.name < p.name
        return self.score > p.score