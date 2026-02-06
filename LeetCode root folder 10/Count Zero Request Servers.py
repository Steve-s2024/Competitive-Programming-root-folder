# pretty straightforward sliding window & frequency map approach, the hard part is to handle every aspect and code up the algorithm
# yeah also offline query is required here.
class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        size = len(queries)
        ans = [0]*size
        ar = [(q, i) for i, q in enumerate(queries)]
        ar.sort()
        logs.sort(key = lambda i:i[1])
        logs.append([0, inf])
        frq = [0]*(n+1)
        y = 0
        i, j = 0, 0

        for v, t in logs:
            # print(y)
            while i < size and ar[i][0] < t:
                T, idx = ar[i]
                while logs[j][1]+x < T:
                    frq[logs[j][0]] -= 1
                    if frq[logs[j][0]] == 0: y -= 1
                    j += 1
                # print(T, y)
                ans[idx] = n-y
                i += 1
            frq[v] += 1
            if frq[v] == 1: y += 1
        return ans
