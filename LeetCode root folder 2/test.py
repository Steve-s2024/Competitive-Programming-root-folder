
from collections import defaultdict, deque, Counter
import heapq, math
from typing import List


class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        shifts.sort(key = lambda i : i[0])
        shifts = [(a, b, 1 if c == 1 else -1) for a, b, c in shifts]
        inf = float('inf')
        shifts.append((inf, inf, 0)) # add the terminator
        minHeap = []
        heapq.heapify(minHeap)
        intervals = []
        L, R, tmp = shifts[0]
        weight = 0
        for l, r, w in shifts:
            while minHeap and minHeap[0][0] < l:
                R, W = heapq.heappop(minHeap)
                if L <= R:
                    intervals.append((L, R, weight))
                L = R+1
                weight -= W
            if l > L:
                intervals.append((L, l-1, weight))
            L = l
            weight += w
            heapq.heappush(minHeap, (r, w))

        intervals.pop()
        # print(intervals)
        res = list(s)
        for l, r, w in intervals:
            for i in range(l, r+1):
                val = res[i]
                idx = ord(val) - ord('a')
                tar = idx + w
                if tar < 0:
                    tar += 26
                elif tar > 25:
                    tar -= 26
                res[i] = chr(tar+ord('a'))
        return ''.join(res)


