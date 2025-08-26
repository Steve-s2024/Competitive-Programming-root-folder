# interactive question is always annoying, cause the testing is so time-wasting and prone to error
from collections import defaultdict, deque, Counter
import sys

def query(x, arr):
    s = '? ' + str(x) + ' ' + str(len(arr)) + ' ' + ' '.join(str(e) for e in arr)
    print(s)
    sys.stdout.flush()
    res = int(input())
    if res == -1: exit()
    return res


def solve():
    n = int(input())
    nums = [i for i in range(1, n+1)]
    mp = defaultdict(list)
    for i in range(1, n+1):
        res = query(i, nums)
        mp[res].append(i)

    lvl = max(mp.keys())
    strarr = [mp[lvl][0]]
    while lvl > 1:
        cur = strarr[-1]
        lvl -= 1
        for cand in mp[lvl]:
            if cur == cand: continue
            if query(cur, [cur, cand]) == 2:
                strarr.append(cand)
                break
    print('! ' + str(len(strarr)) + ' ' + ' '.join(str(e) for e in strarr))


t = int(input())
for i in range(t):
    solve()


