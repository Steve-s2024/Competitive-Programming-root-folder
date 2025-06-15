# didn't expect to pass first try
class FreqStack:

    def __init__(self):
        self.frq = defaultdict(int)
        self.mp = defaultdict(list)
        self.maxHeap = []

    def push(self, val: int) -> None:
        self.frq[val] += 1
        cnt = self.frq[val]
        heapq.heappush(self.maxHeap, (-cnt, val))
        self.mp[cnt].append(val)

    def pop(self) -> int:
        frq = self.frq
        mp = self.mp
        maxHeap = self.maxHeap

        while frq[maxHeap[0][1]] != -maxHeap[0][0]: heapq.heappop(maxHeap)

        cnt, _ = maxHeap[0]
        cnt = -cnt
        while frq[mp[cnt][-1]] != cnt: mp[cnt].pop()
        tar = mp[cnt].pop()
        frq[tar] -= 1
        return tar
