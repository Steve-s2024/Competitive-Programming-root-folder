# a solution without proof. though im trying to prove the algorithm does produce the maximum subarray min sums.
# the algo goes like this: with a zero initialized n sized array, iterate from 1 to n, each time pick the left or
# right end of the segment of zeros, called zeros segment. my hypothesis is that the permutation produced by this way
# will always yield the maximum subarray min sums. yet not able to prove it

def solve():
    n, k = [int(e) for e in input().split()]
    pw = pow(2, n-1)
    if k > pw:
        print(-1)
        return
    pw //= 2
    arr = [0]*n
    l, r = 0, n-1
    tot = 0
    for i in range(1, n+1):
        if k > tot+pw:
            arr[r] = i
            r -= 1
            tot += pw
        else:
            arr[l] = i
            l += 1

        pw //= 2

    # print(arr)
    print(' '.join(str(e) for e in arr))



t = int(input())
for i in range(t): solve()





