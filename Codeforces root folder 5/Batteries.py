# haha lol wtf


def query(i, j):
    print(f'{i+1} {j+1}')
    stdout.flush()
    res = int(input())
    if res == -1: exit(4399)
    return res

def solve():
    n = int(input())
    for i in range(n):
        for j in range(0, n-(i+1)):
            if query(j, j+(i+1)):
                return


for _ in range(int(input())): solve()
