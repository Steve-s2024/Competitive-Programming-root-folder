#
def solve():
    n, q = [int(e) for e in input().split()]
    arr = [(i+1) for i in range(n)]
    offset = 0
    for i in range(q):
        query = [int(e) for e in input().split()]
        if query[0] == 3: offset += query[1]
        elif query[0] == 2: print(arr[(query[1]-1+offset)%n])
        elif query[0] == 1: arr[(query[1]-1+offset)%n] = query[2]

solve()

