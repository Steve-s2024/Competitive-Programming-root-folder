# TLE
class Solution:
    def __init__(self):
        q = deque()
        res = set()
        vis = set()

        def recursive(q):
            if len(q) > 9:
                return
            if q:
                x = int(''.join(q))
                if x in vis:
                    return
                vis.add(x)
                if q[0] != '0':
                    res.add(x)
            for i in range(10):
                q.appendleft(str(i))
                q.append((str(i)))
                recursive(q)
                q.popleft()
                q.pop()

        recursive(q)
        for i in range(10):
            q.append(str(i))
            recursive(q)
            q.pop()

        if 0 in res: res.remove(0)
        res = sorted(list(res))
        self.res = res

    @staticmethod
    def getNum(num, k):
        res = []
        while num:
            re = num % k
            res.append(re)
            num //= k
        return ''.join(reversed([str(e) for e in res]))

    def kMirror(self, k: int, n: int) -> int:

        ans = 0
        cnt = 0
        for num in self.res:
            a = Solution.getNum(num, k)
            if a == a[::-1]:
                ans += num
                cnt += 1
                if cnt >= n:
                    break
        return ans
