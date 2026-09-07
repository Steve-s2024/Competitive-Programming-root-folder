# require a parameter k for do the k-smallest elements sum
# provide logn insertion deletion of single element. DualHeap.sm will store the current k-smallest elements sum
# 2026-07-01


from collections import defaultdict, deque, Counter
from heapq import heapify, heappush, heappop

class DualHeap:
    def __init__(self, k):
        self.k, self.mihp, self.mxhp = k, [], []
        self.frq, self.frq2, self.sm, self.ct = defaultdict(int), defaultdict(int), 0, 0

    def push(self, e):
        k, mihp, mxhp, frq, sm, ct, frq2 = self.k, self.mihp, self.mxhp, self.frq, self.sm, self.ct, self.frq2
        frq[e] += 1
        ct += 1
        sm += e
        heappush(mxhp, -e)
        if ct > k:
            while frq[-mxhp[0]] == 0: heappop(mxhp)
            e = -heappop(mxhp)
            heappush(mihp, e)
            frq2[e] += 1
            frq[e] -= 1
            ct -= 1
            sm -= e
        self.sm, self.ct = sm, ct

    def pop(self, e):
        k, mihp, mxhp, frq, sm, ct, frq2 = self.k, self.mihp, self.mxhp, self.frq, self.sm, self.ct, self.frq2
        if frq2[e]: frq2[e] -= 1
        elif frq[e]:
            frq[e] -= 1
            sm -= e
            while frq2[mihp[0]] == 0: heappop(mihp)
            e = heappop(mihp)
            heappush(mxhp, -e)
            frq2[e] -= 1
            frq[e] += 1
            sm += e
        self.sm, self.ct = sm, ct





dh = DoubleHeap(3)
for i in range(10, -1, -1):
    dh.push(i)
    if dh.ct == dh.k: print(dh.sm)