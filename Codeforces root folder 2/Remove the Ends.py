# good medium question, not too hard to discover the greedy
# solution (prefix and suffix sum)
def solve():
    n = int(input())
    coins = [int(e) for e in input().split()]
    prefix, suffix = 0, 0

    for num in coins:
        if num < 0:
            suffix += num

    res = abs(suffix)
    for num in coins:
        if num > 0:
            prefix += num
        if num < 0:
            suffix -= num
        res = max(res, prefix + abs(suffix))
    print(res)


t = int(input())
for tt in range(t):
    solve()