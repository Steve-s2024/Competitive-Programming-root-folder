# didn't even realize i solved it until i run it: 85%
# this begin as a little ideal in my head and its complicated so i did not have much hope, but guess the brain proved
# itself.
class DinnerPlates:

    def __init__(self, capacity: int):
        self.stk = []
        self.n = capacity
        self.minheap = []

    def push(self, val: int) -> None:
        stk = self.stk
        n = self.n
        minheap = self.minheap

        while minheap and (minheap[0] >= len(stk) or len(stk[minheap[0]]) == n): heapq.heappop(minheap)
        if minheap:
            pos = minheap[0]
            stk[pos].append(val)
            if len(stk[pos]) >= n: heapq.heappop(minheap)

        elif not stk or len(stk[-1]) >= n:
            stk.append([])
            stk[-1].append(val)
        else:
            stk[-1].append(val)

    def pop(self) -> int:
        stk = self.stk
        minheap = self.minheap
        while stk and len(stk[-1]) == 0: stk.pop()
        if not stk: return -1
        res = stk[-1].pop()
        if not stk[-1]:
            stk.pop()
        else:
            heapq.heappush(minheap, len(stk) - 1)
        return res

    def popAtStack(self, index: int) -> int:
        stk = self.stk
        minheap = self.minheap
        if index >= len(stk) or len(stk[index]) == 0: return -1
        res = stk[index].pop()
        if index == len(stk) - 1 and len(stk[index]) == 0:
            stk.pop()
        else:
            heapq.heappush(minheap, index)
        return res