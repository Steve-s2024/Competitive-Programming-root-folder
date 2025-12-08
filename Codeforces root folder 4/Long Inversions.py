# a worst case 25/2 million iteration solution just get accepted...
from collections import defaultdict, deque, Counter

def solve():
    n = int(input())
    s = input()

    res = 1
    for x in range(2, n+1):
        q = deque()
        t = 0
        for i in range(n):
            if q and q[0] < i:
                t -= 1
                q.popleft()

            if (t+int(s[i]))%2 == 0:
                t += 1
                if i+x-1 < n: q.append(i+x-1)
                else: break
        else: res = x

    print(res)



for _ in range(int(input())): solve()