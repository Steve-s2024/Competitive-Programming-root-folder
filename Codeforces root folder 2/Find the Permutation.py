# O(n^2) solution, I wasted so many times thinking it is
# topological sort, but the greedy solution is right there...
from collections import defaultdict, deque, Counter

def solve():
    n = int(input())
    graph = defaultdict(list)
    for i in range(n):
        s = input()
        for j in range(i):
            if s[j] == '1':
                graph[i].append(j)
    # print(graph)

    res = [-1] * n
    res[len(graph[n-1])] = n
    for i in range(n-2, -1, -1):
        size = len(graph[i])+1
        j = 0
        while size:
            if res[j] == -1:
                size -= 1
            j+=1
        j-=1
        res[j] = i+1


    print(' '.join([str(num) for num in res]))





t = int(input())
for tt in range(t):
    solve()

