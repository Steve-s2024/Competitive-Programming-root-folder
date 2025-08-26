# a hard one, but not a bad one. though the description is shit af
def solve():
    n, k = [int(e) for e in input().split()]

    x = 0
    digits = []
    while n:
        re = n%3
        digits.append(re)
        n //= 3
        x += 1
    digits = digits[::-1]
    # print(digits)
    size = len(digits)
    sm = sum(digits)
    if sm > k:
        print(-1)
        return
    for i in range(size-1):
        cancellable = min(digits[i], (k - sm)//2)
        sm -= digits[i] + digits[i+1]
        digits[i] -= cancellable
        digits[i+1] += 3*cancellable
        sm += digits[i] + digits[i+1]

    # print(digits)

    res = 0
    x = 0
    for d in digits[::-1]:
        res += d*(pow(3, x+1) + x*pow(3, x-1))
        x += 1
    print(int(res))


t = int(input())
for i in range(t):
    solve()



