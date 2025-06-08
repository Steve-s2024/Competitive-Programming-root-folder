# difficult and advanced interval manipulation problem
# also a good exemplary of solving by breaking down problem to
# easier sub problems.: 42%
class Solution:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        segments.sort(key=lambda i: i[0])
        segments.append([float('inf'), float('inf'), 0]) # add the terminator
        n = len(segments)

        painting = []
        minHeap = []
        heapq.heapify(minHeap)
        L = segments[0][0]
        mixedColor = 0
        i = 0
        while i < n:
            # print(L, i, minHeap)
            [l, r, c] = segments[i]
            if l == L:
                heapq.heappush(minHeap, (r, c))
                mixedColor += c
                i+=1
            else:
                while minHeap and minHeap[0][0] <= l:
                    [R, C] = heapq.heappop(minHeap)
                    if L < R:
                        painting.append([L, R, mixedColor])
                        L = R
                    mixedColor -= C
                if minHeap and L < l:
                    painting.append([L, l, mixedColor])
                L = l

        return painting