# very boring question, the entire solution is built on the
# small observation that the room for the first subarray of
# even index, if room is 1, you have no choice but simulate
# else return either 1 or 2.
def solve():
    n, k = [int(e) for e in input().split()]
    nums = [int(e) for e in input().split()]
    size = n-(k-2)-1
    if size == 1:
        res = k // 2 + 1  # the default value if all element of b equals to their index
        for i in range(1, n, 2):
            if nums[i] != (i+1)//2:
                res = (i+1)//2
                break
        print(res)

    else:
        cnt = 0
        for i in range(1, 1+size):
            if nums[i] == 1:
                cnt += 1
        if cnt == size:
            print(2)
        else:
            print(1)




t = int(input())
for tt in range(t):
    solve()