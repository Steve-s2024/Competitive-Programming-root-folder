# wasting so much time to implement the checking: spend more time on it than learning and implementing Manacher's algorithm

def manacher(s):
    s = '#' + '#'.join(list(s)) + '#'
    n = len(s)

    ar = [0] * n
    c, r = 0, 0
    for i in range(n):
        m = 2 * c - i
        if i <= r and m >= 0: ar[i] = min(r - i, ar[m])
        while i - ar[i] >= 0 and i + ar[i] < n and s[i - ar[i]] == s[i + ar[i]]: ar[i] += 1
        if i + ar[i] >= r: c, r = i, i + ar[i]

    return ar


class Solution:
    def findAnswer(self, parent: List[int], s: str) -> List[bool]:
        n = len(parent)

        g = [[] for _ in range(n)]
        for u, p in enumerate(parent):
            if p != -1: g[p].append(u)
        # print(g)
        t = []

        def fn(u):
            for v in g[u]: fn(v)
            t.append(s[u])
        fn(0)
        # print(t)
        ar = manacher(''.join(t))
        ans = [False] * n
        x = 1
        # print(ar)
        def dfs(u):
            nonlocal x
            l = 1
            for v in g[u]: l += dfs(v)
            x += 2
            c = x-2 -(l-1)
            if l % 2 == 1: ans[u] = (ar[c]-1)//2 >= l//2
            else: ans[u] = ar[c]//2 >= l//2
            return l

        dfs(0)
        return ans
