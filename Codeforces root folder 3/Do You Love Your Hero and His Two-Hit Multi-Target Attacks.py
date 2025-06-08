# Do You Love Your Hero and His Two-Hit Multi-Target Attacks?
# name has nothing to do with the problem, the binary search tag
# is also irrelevant, overall the problem is easy. bit too easy for its rating

def solve():
    k = int(input())
    i = 0
    tot = 0
    offset = 0
    res = []
    while tot < k:
        cur = 0
        res.append((i, offset))
        j = 1
        while tot+cur+j <= k:
            res.append((i, offset+j))
            cur += j
            j+=1
        tot+=cur
        i+=1
        offset+=j

    # print(res)
    print(len(res))
    for a, b in res:
        print(str(a) + ' ' + str(b))


t = int(input())
for i in range(t):
    solve()
