# a brilliant way to avoid the duplicating of string/array when copying and pasting server string and PC string
# without this the code will TLE
def solve():
    n, q = [int(e) for e in input().split()]
    arrs = {}
    server = []
    for i in range(q):
        line = input().split()
        t, p = int(line[0]), int(line[1])
        if t == 1:
            arrs[p] = server
        elif t == 2:
            if p not in arrs: arrs[p] = []
            txt = line[2]
            arrs[p] = [arrs[p], txt]
        elif t == 3:
            if p not in arrs: arrs[p] = []
            server = arrs[p]
    res = []
    cur = server
    while cur:
        res.append(cur[1])
        cur = cur[0]
    # print(res)
    print(''.join(reversed(res)))
solve()




