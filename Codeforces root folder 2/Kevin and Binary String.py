# this is unbelievably stupid, how the fk this brute force
# solution passed the testcase with s.length == 5000?
# I would not have waste time on this if I tried the brute
# force at first.
from collections import defaultdict, deque, Counter

def solve():
    s = input()
    n = len(s)
    first = n
    for i, c in enumerate(s):
        if c == '0':
            first = i
            break
    if first == n:
        print(1, n, 1, 1)
    else:
        # the second string must have size len(s)-first
        size = len(s) - first
        res = deque(list(s[:size]))
        num = int(s, 2)
        max_ = num ^ int(''.join(res), 2)
        l, r = 0, size-1
        for i in range(size, n):
            res.popleft()
            res.append(s[i])
            cur = int(''.join(res), 2)
            tmp = num ^ cur
            if tmp > max_:
                max_ = tmp
                l, r = i-size+1, i
        print(1, n, l+1, r+1)
        #



t = int(input())

for tt in range(t):
    solve()