#

def solve():
    n = int(input())
    nums = [int(e) for e in input().split()]

    sm = sum(nums)
    if sm%n != 0:
        print('No')
        return

    MX = 50
    mp = [0]*MX
    avg = sm//n
    for i, e in enumerate(nums):
        if e == avg: continue

        for i in range(MX):
            a = 1<<i
            if e-a >= avg: continue
            b = avg-(e-a)

            if b.bit_count() == 1:
                mp[a.bit_length()] += 1
                mp[b.bit_length()] -= 1
                break
        else:
            print('No')
            return

    for e in mp:
        if e:
            print('No')
            return
    print('Yes')

for _ in range(int(input())): solve()

