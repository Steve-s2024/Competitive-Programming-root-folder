# brute force, deprecated
primes = []
cands = [i for i in range(2, 10000)]
while cands:
    # print(cands)
    primes.append(cands[0])
    n = len(cands)
    tmp = []

    for j in range(1, n):
        if cands[j] % cands[0] != 0:
            tmp.append(cands[j])
    cands = tmp
# print(sum(primes))


def solve():
    n = int(input())
    nums = [int(e) for e in input().split(' ')]
    nums.sort()
    sm1, sm2 = sum(nums), sum(primes[:n])
    res = 0
    for i in range(n):
        # print(sm1, sm2)
        if sm1 >= sm2:
            res = i
            break
        sm1 -= nums[i]
        sm2 -= primes[n-1-i]
    print(res)


t = int(input())
for tt in range(t):
    solve()