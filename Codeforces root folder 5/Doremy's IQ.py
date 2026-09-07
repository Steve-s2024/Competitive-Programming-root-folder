# snappy

def solve():
    n, q = [int(e) for e in input().split()]
    nums = [int(e) for e in input().split()]
    x = 0
    res = 0
    ar = [0]*n
    for i in range(n-1, -1, -1):
        if nums[i] > x:
            if x < q:
                ar[i] = 1
                x += 1
        else: ar[i] = 1
    print(''.join(str(e) for e in ar))



for _ in range(int(input())): solve()
