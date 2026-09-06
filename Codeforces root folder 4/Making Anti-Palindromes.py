# no idea how to explain this, but it worked. the strategy can be found from several previous problem
# pairwise elimination and the remaining ones only take one operation per each
# greed greedy here we meet


def solve():
    n = int(input())
    s = input()
    if n%2:
        print(-1)
        return
    mx = max(Counter(s).values())
    if mx > n//2:
        print(-1)
        return

    s1, s2 = s[:n//2], s[n//2:][::-1]
    mp = defaultdict(int)
    for i in range(n//2):
        if s1[i] == s2[i]: mp[s1[i]] += 1
    tp = mp.values()
    if not tp:
        print(0)
        return
    mx = max(tp)
    sm = sum(tp)
    if mx <= sm//2:
        res = (sm+1)//2
    else:
        res = sm-mx + (mx-(sm-mx))
    print(res)



for _ in range(int(input())): solve()
