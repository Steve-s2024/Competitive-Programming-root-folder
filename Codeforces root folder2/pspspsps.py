# I just gambled... it worked
from collections import defaultdict, deque, Counter

def solve():
    n = int(input())
    s = input()
    mp = Counter(s)
    if len(mp) == 1:
        print('Yes')
    elif '.' in mp and len(mp) == 2:
        print('Yes')
    else:
        sIdx, pIdx = n-1, 0
        while s[sIdx] != 's':
            sIdx -= 1
        while s[pIdx] != 'p':
            pIdx += 1
        if sIdx > pIdx or (sIdx != 0 and pIdx != n-1):
            print('No')
        else:
            print('Yes')


t = int(input())
for tt in range(t):
    solve()

