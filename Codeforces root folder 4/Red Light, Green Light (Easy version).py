# hah, one attempt AC, my ability is unrivaled



def solve():
    n, k = [int(e) for e in input().split()]
    nums = [int(e) for e in input().split()]
    dely = [int(e) for e in input().split()]
    q = int(input())
    qs = [int(e) for e in input().split()]

    zp = list(zip(nums, dely))
    zp.sort()
    mp = {}
    lit = {}
    for i in range(n): lit[nums[i]] = dely[i]
    for i in range(1, n):
        dif = zp[i][0] - zp[i-1][0]
        a = zp[i][0]
        b = zp[i-1][0]
        if a not in mp: mp[a] = [0, 0]
        if b not in mp: mp[b] = [0, 0]
        mp[a][0] = dif
        mp[b][1] = dif
    # print(mp)
    # print(lit)
    ans = []
    for srt in qs:
        t = 0
        loc = srt
        dir = 'r'
        dp = set()
        for i in range(n):
            if zp[i][0] >= srt:
                dif = zp[i][0]-srt
                loc += dif
                t = (t+dif)%k
                break
        else:
            ans.append('yes')
            continue
        # print(srt, ans)
        # print(loc, t)
        while 1:
            # print(loc, t)
            state = (t, loc, dir)
            if state not in dp: dp.add(state)
            else :
                ans.append('no')
                break
            if lit[loc] == t: # red light
                dir = 'r' if dir != 'r' else 'l'

            if dir == 'l' and loc == zp[0][0] or dir == 'r' and loc == zp[-1][0]:
                ans.append('yes')
                break

            if dir == 'r':
                t = (t+mp[loc][1])%k
                loc += mp[loc][1]
            else:
                t = (t+mp[loc][0])%k
                loc -= mp[loc][0]

    for a in ans: print(a)

t = int(input())
for i in range(t): solve()


