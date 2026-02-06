# a very though mental game, and it is from a div2 B...
def solve():
    n, k = [int(e) for e in input().split()]
    nums = [int(e) for e in input().split()]
    nums = list(set(nums))
    nums.sort()
    # print(nums[:k-1])
    st = set(nums[:k-1])
    for i in range(k+1):
        if i not in st:
            print(i)
            return



for _ in range(int(input())): solve()