# so headache yet brainless

from sys import stdout

def query(x, y):
    print(f'? {x} {y}')
    stdout.flush()
    res = int(input())
    if res == -1: exit(4399)
    return res


def solve():
    n, m = [int(e) for e in input().split()]
    a = query(1, 1)+1
    b = query(n, m)+1
    if a+b == n+m: # same diagonal
        c = query(n, 1)+1
        xpy = a+1
        xsy = n-c
        x = (xpy+xsy)//2
        y = xpy-x
        print(f'! {x} {y}')

    else:
        c = query(n, 1)+1
        xpy = a+1
        xsy = n-c
        x = (xpy + xsy) // 2
        y = xpy-x
        if x in range(1, n+1) and y in range(1, m+1):
            if query(x, y) == 0:
                print(f'! {x} {y}')
                return

        xpy = (n+m-1 - b)+2
        xsy = n-c
        x = (xpy+xsy) // 2
        y = xpy-x
        print(f'! {x} {y}')

for _ in range(int(input())): solve()
