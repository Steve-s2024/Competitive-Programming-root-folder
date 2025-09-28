# jesus what is this? fking lucky enough to solve it. completely surprised by that though
class Solution:
    def minDifference(self, n: int, k: int) -> List[int]:
        fs = []
        for f in range(2, int(sqrt(n))+1):
            while n%f == 0:
                fs.append(f)
                n//=f

        if n > 1: fs.append(n)
        # print(fs)
        arr = [1]*k
        res = []
        mi = inf
        vis = set()
        def recursive(i):
            state = (i, tuple(arr))
            if state in vis: return
            vis.add(state)
            nonlocal res, mi
            if i >= len(fs):
                if mi > max(arr)-min(arr):
                    mi = max(arr)-min(arr)
                    res = arr[:]
                return

            for j in range(k):
                arr[j] *= fs[i]
                recursive(i+1)
                arr[j] //= fs[i]
        recursive(0)
        return res