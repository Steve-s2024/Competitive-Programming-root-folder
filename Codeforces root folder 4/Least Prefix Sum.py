#

def solve():
    n, m = [int(e) for e in input().split()]
    nums = [int(e) for e in input().split()]
    m -= 1

    hp = []
    res = 0
    sm = 0
    for i in range(m, 0, -1):
        sm += nums[i]
        heappush(hp, -nums[i])
        while sm > 0:
            x = -heappop(hp)
            sm -= 2*x
            res += 1

    hp = []
    sm = 0
    for i in range(m+1, n):
        sm += nums[i]
        heappush(hp, nums[i])
        while sm < 0:
            x = heappop(hp)
            sm -= 2*x
            res += 1
    print(res)



for _ in range(int(input())): solve()