# not a bad question, not like the impossible D question in some ABC

def solve():
    n, m = [int(e) for e in input().split()]
    arr = [int(e)%m for e in input().split()]
    brr = [int(e)%m for e in input().split()]
    arr.sort()
    brr.sort()
    j = 0
    tot = 0
    for i in range(n-1, -1, -1):
        while j < n and brr[j] + arr[i] < m:
            # print(brr[j], arr[i])
            tot += brr[j]
            j += 1
        if j < n:
            sm = arr[i] + brr[j]
            tot += sm%m
        else: tot += arr[i]
        j += 1
    print(tot)




