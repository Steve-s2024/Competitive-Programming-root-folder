# ingenious way of viewing the problem (credit to neetcode), prefix solution: 85%
class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        prefix = [0] * n
        for l, r, d in shifts:
            w = 1 if d == 1 else -1
            prefix[r] += w
            if l:
                prefix[l - 1] -= w

        arr = list(s)
        total = 0
        # print(prefix, arr)
        for i in range(n - 1, -1, -1):
            total += prefix[i]
            tar = ord(arr[i]) - ord('a')
            tar += total % 26
            if tar > 25:
                tar -= 26
            elif tar < 0:
                tar += 26
            arr[i] = chr(tar + ord('a'))
        return ''.join(arr)



# all the hard work comes down to the invention of weighted overlap
# interval merging algorithm, but clearly it's not the best way to tackle
# this problem: 5%
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
                tar = idx + (w%26)
                if tar < 0:
                    tar += 26
                elif tar > 25:
                    tar -= 26
                res[i] = chr(tar+ord('a'))
        return ''.join(res)


