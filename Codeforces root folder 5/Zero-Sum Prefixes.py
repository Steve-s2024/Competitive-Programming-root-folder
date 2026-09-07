# have to give up on the defaultdict and use the sorting and counting strategy for finding maximum frequency just to avoid
# the anti-hash testcase


def solve():
    n = int(input())
    nums = [int(e) for e in input().split()]

    nums.append(0)
    res = 0
    sm = 0
    ar = []
    def helper(ar):
        x = 1
        res = 1
        for i in range(1, len(ar)):
            if ar[i] == ar[i-1]: x+= 1
            else: x = 1
            res = max(res, x)
        return res

    for v in nums[nums.index(0):]:
        ar.append(sm)
        sm += v
        if v == 0:
            ar.sort()
            res += helper(ar)
            ar.clear()
    # print(res)
    i = 0
    sm = 0
    while nums[i]:
        sm += nums[i]
        if sm == 0: res += 1
        i += 1

    print(res-1)





for _ in range(int(input())): solve()






