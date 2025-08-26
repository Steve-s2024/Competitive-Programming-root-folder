# pure survival time (didn't know i could pull it off)! without solve this I rank ~300, now I am 65!
# personally think this is a hard and very bad question, where your only strategy is to make wild guesses and
# try them out one by one. at least this is how I coped it

from collections import Counter

def solve():
    n = int(input())
    arr = [int(e) for e in input().split()]
    brr = [int(e) for e in input().split()]

    skip = set()
    for i in range(n):
        if arr[i] == brr[i]: skip.add(arr[i])

    i = 0
    res = []
    while i < n and len(res) < 2:
        if i in skip:
            i += 1
            continue
        res.append(i)
        i += 1

    while len(res) < 2:
        res.append(n)

    ans = max(res)
    mp = Counter(arr+brr)
    for i in range(n):
        if i not in mp:
            ans = min(ans, i)

    print(ans)




t = int(input())
for i in range(t):
    solve()