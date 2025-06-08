# min heap solution:3
# ms
# Beats
# 16.18%
class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        minHeap = []
        heapq.heapify(minHeap)
        for i in range(len(arr)-1, -1, -1):
            if minHeap and arr[i] > minHeap[0][0]:
                cur = None
                while minHeap and arr[i] > minHeap[0][0]:
                    if cur is None or cur[0] != minHeap[0][0]:
                        cur = heapq.heappop(minHeap)
                    else:
                        heapq.heappop(minHeap)
                a, b = i, cur[1]
                tmp = arr[a]
                arr[a] = arr[b]
                arr[b] = tmp
                break
            heapq.heappush(minHeap, (arr[i], i))
        return arr