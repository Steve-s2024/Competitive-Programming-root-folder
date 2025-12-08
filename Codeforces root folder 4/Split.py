# this is hell of a stupid and difficult Q2 in div2

def solve():
    n = int(input())
    nums = [int(e) for e in input().split()]
    evev, evod = 0, 0
    odd = 0
    f = 0
    ct = 0
    # print(Counter(nums))
    for v in Counter(nums).values():
        if v%2 == 1:
            if v > 1: f = 1
            else: ct += 1
        if v%2 == 0:
            if v//2%2 == 0: evev += 1
            else: evod += 1
        else: odd += 1


    # print(evev, evod, odd)
    res = 2*evod + 2*(evev - (evev%2)) + odd + (2 if evev%2 == 1 and (f or ct >= 2) else 0)
    print(res)

t = int(input())
for i in range(t): solve()