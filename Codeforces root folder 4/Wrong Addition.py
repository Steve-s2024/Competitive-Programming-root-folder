# this is a lot harder than the 1200 rated... this is at least 1400
# time: 15min 23sec



def solve():
    a, s = [e for e in input().split()]
    strarr = []
    n = len(a)
    j = len(s)-1
    for i in range(n-1, -1, -1):
        x, y = int(a[i]), int(s[j])
        if x <= y: # no carry happened
            if j < 0 or y-x < 0:
                print(-1)
                return
            strarr.append(y-x)
            j -= 1
        else: # a carry happened
            if j < 1:
                print(-1)
                return
            t = int(s[j-1:j+1])
            if t-x >= 10 or t-x < 0:
                print(-1)
                return
            strarr.append(t-x)
            j -= 2

    while j >= 0:
        strarr.append(s[j])
        j -= 1
    while len(strarr) > 1 and strarr[-1] == 0: strarr.pop()
    print(''.join(str(e) for e in strarr[::-1]))

t = int(input())
for i in range(t): solve()

