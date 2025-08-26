# dont know why the recursion didn't work, I have confirmed it over and over again...
def solve():
    n, m = [int(e) for e in input().split()]

    st = set()
    for i in range(m):
        a, b = [int(e) for e in input().split()]
        st.add((a, b))
        st.add((b, a))

    inf = math.inf
    def dfs(node, begin, size, mask):
        nonlocal inf
        if mask == (1<<(n+1))-2:
            return 0 if size == 0 else inf
        res = inf
        if node is None:
            for i in range(1, n + 1):
                if mask & (1 << i): continue
                a = dfs(i, i, 1, mask^(1 << i))
                res = min(a, res)
        else:
            for i in range(1, n+1):
                if mask&(1<<i): continue
                if (node, i) in st:
                    st.remove((node, i))
                    st.remove((i, node))
                    a = dfs(i, begin, size+1, mask^(1<<i))
                    res = min(a, res)
                    st.add((node, i))
                    st.add((i, node))
                else:
                    a = dfs(i, begin, size+1, mask^(1<<i)) + 1
                    res = min(a, res)
            if size > 2:
                if (node, begin) in st:
                    st.remove((node, begin))
                    st.remove((begin, node))
                    a = dfs(None, None, 0, mask)
                    res = min(a, res)
                    st.add((node, begin))
                    st.add((begin, node))
                else:
                    a = dfs(None, None, 0, mask) + 1
                    res = min(a, res)
        return res

    res = dfs(1, 1, 1, 2)
    print(res)

solve()


# deprecated
import sys
from collections import defaultdict, deque, Counter
import cmath, heapq
sys.setrecursionlimit(1 << 20)  # Increase recursion limit for deep trees



def solve():
    n, m = [int(e) for e in input().split()]

    deg = [0]*(n+1)
    graph = defaultdict(list)
    for i in range(m):
        a, b = [int(e) for e in input().split()]
        deg[a] += 1
        deg[b] += 1
        graph[a].append(b)
        graph[b].append(a)
    print(deg)


    vis = defaultdict(int)
    cnt = 0
    mx = 0
    def dfs(node):
        nonlocal mx, cnt
        for nxt in graph[node]:
            if vis[node] >= 2: break
            if vis[nxt] >= 2: continue
            vis[node] += 1
            vis[nxt] += 1
            cnt += 1
            mx = max(mx, cnt)
            dfs(nxt)
            cnt -= 1
            vis[node] -= 1
            vis[nxt] -= 1
    dfs(1)
    print(mx)

    print(n - mx)



solve()




