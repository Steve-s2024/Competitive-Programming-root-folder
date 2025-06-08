import sys
import heapq, math
from collections import defaultdict, deque, Counter

def solve():
    n = int(input())
    s = input()


    res = 0
    aMp = {}
    cMp = {}
    a = 0
    for i in range(n):
        if s[i] == 'B':
            aMp[i] = a
        elif s[i] == 'A':
            a+=1
        else:
            a=0

    c = 0
    for i in range(n-1, -1, -1):
        if s[i] == 'B':
            cMp[i] = c
        elif s[i] == 'C':
            c+=1
        else:
            c=0

    for i in range(n):
        if s[i] != 'B':
            continue
        res += max(aMp[i], cMp[i])



    print(res)





t = int(input())
for i in range(t):
    solve()