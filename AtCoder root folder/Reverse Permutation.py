# just an ABC C, but the idea is interesting so i keep it
def solve():
    n = int(input())
    s = input()
    q = deque()
    f = 0
    for i, c in enumerate(s):
        if not f: q.append(i+1)
        else: q.appendleft(i+1)

        if c == 'o': f ^= 1

    res = list(q)
    if f == 0: print(' '.join(str(e) for e in res))
    else: print(' '.join(str(e) for e in res[::-1]))



solve()