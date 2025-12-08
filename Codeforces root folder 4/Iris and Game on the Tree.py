# nice! though didn't fully prove the approach, it is very much a victory to solve it independently
# this is rated 1763 on clist by the way


# g: graph, s: node mark
def helper(g, s):
    n = len(g)
    lf = []
    md = 0
    for i in range(1, n):
        if len(g[i]) == 1: lf.append(i)
        if s[i] == '?' and len(g[i]) > 1: md += 1


    ct, one, zero = 0, 0, 0
    for l in lf:
        if s[l] == '?': ct += 1
        elif s[l] == '1': one += 1
        else: zero += 1
    if s[0] != '?':
        res = (one if s[0] == '0' else zero) + (ct+1)//2
        return res

    # now, root node is ?
    if one != zero:
        res = max(one, zero) + ct//2
        return res

    # now, one equals zero, we discuss the md.
    res = one
    if md%2 == 1: res += (ct+1)//2
    else: res += ct//2
    return res

def solve():
    n = int(input())
    g = [[] for _ in range(n)]
    for i in range(n-1):
        u, v = [int(e) for e in input().split()]
        u, v = u-1, v-1
        g[u].append(v)
        g[v].append(u)
    s = list(input())
    print(helper(g, s))


t = int(input())
for i in range(t): solve()

