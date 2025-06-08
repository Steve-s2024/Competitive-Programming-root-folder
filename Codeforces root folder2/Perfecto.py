# working algo, need to write in c++ to pass testcases
import math
t = int(input())

for tt in range(t):
    n = int(input())
    total = n*(n+1)//2
    root = math.sqrt(total)
    if root == int(root):
        print(-1)    
    else:
        s = ''
        total = 0
        i = 1
        while i <= n:
            nextTotal = total + i
            root = math.sqrt(nextTotal)
            if root == int(root):
                s += str(i+1) + ' ' + str(i) + ' '
                total += i + i + 1
                i+=2
            else:
                s += str(i) + ' '
                total += i
                i+=1
        print(s)


# depricated
from collections import deque
import math
t = int(input())

for tt in range(t):
    n = int(input())
    q = deque([i for i in range(1, n+1)])
    used = set()
    total = 0
    res = []
    while q:
        
        nextTotal = total + q[0]
        root = math.sqrt(nextTotal)
        i = 0
        while root == int(root):
            i+=1
            if q[i] in used:
                continue
            nextTotal = total + q[0]
            root = math.sqrt(nextTotal)      
        used.add(q[i])
        res.append(q[i])
        while q[0] in used:
            q.popleft()
    s = ''
    for n in res:
        s += n + ' '
    print(s)
