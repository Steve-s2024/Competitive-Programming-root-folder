# another effortless conquer of 1600
from sys import stdout

def query(l, r):
    print(f'? {l} {r}')
    stdout.flush()
    return int(input())

def solve():
    n = int(input())
    res = query(1, n)
    if res == 0:
        print('! IMPOSSIBLE')
        return
    prev = res
    arr = []
    for i in range(2, n):
        res = query(i, n)
        if res == 0:
            arr.append(0)
            for i in range(prev): arr.append(1)
            while len(arr) < n: arr.append(0)
            prev = 0
            break

        if prev == res: arr.append(1)
        else: arr.append(0)
        prev = res
    if prev == 1:
        arr.append(0)
        arr.append(1)
    print('! ' + ''.join(str(e) for e in arr))


t = int(input())
for i in range(t): solve()

