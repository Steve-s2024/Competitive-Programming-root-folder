#
def solve():
    n = int(input())
    nums = [int(e) for e in input().split()]
    thr, sev = defaultdict(int), defaultdict(int)
    mp3 = defaultdict(int)
    mp7 = defaultdict(int)
    res = 0
    for i in range(n):
        x = nums[i]
        if x%5 == 0:
            res += mp7[x//5] + mp3[x//5]
        if x%7 == 0:
            mp7[x//7] += thr[x//7]
            sev[x//7] += 1
        if x%3 == 0:
            mp3[x//3] += sev[x//3]
            thr[x//3] += 1

    # print(res)
    thr, sev = defaultdict(int), defaultdict(int)
    mp3 = defaultdict(int)
    mp7 = defaultdict(int)
    for i in range(n-1, -1, -1):
        x = nums[i]
        if x % 5 == 0: res += mp7[x // 5] + mp3[x // 5]
        if x % 7 == 0:
            mp7[x // 7] += thr[x // 7]
            sev[x // 7] += 1
        if x % 3 == 0:
            mp3[x // 3] += sev[x // 3]
            thr[x // 3] += 1
    print(res)

solve()