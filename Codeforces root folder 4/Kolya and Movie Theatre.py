# greedy greedy lalala

def solve():
    n, m, d = [int(e) for e in input().split()]
    nums = [int(e) for e in input().split()]
    hp = []
    sm = 0
    res = 0
    for i, v in enumerate(nums):
        if v <= 0: continue
        sm += v
        heappush(hp, v)
        if len(hp) > m: sm -= heappop(hp)
        res = max(res, sm-(i+1)*d)
        # print(i, sm, hp)
    print(res)

for _ in range(int(input())): solve()
