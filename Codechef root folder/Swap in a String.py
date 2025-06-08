# this is embarrassing, I could've solved this so long ago, early in the
# contest. but I fking missed it and jumped from Q3 straight to Q5
# wasted 40 minutes on Q5 before realizing I skipped Q4
# then took me less than 30 minutes to actually solve Q4
# I could've got to around top 200...
def solve():
    n = int(input())
    s = input()


    res = 0
    aMp = {}
    cMp = {}
    a = 0
    for i in range(n):
        if s[i] == 'B':
            aMp[i] = a
        elif s[i] == 'A':
            a+=1
        else:
            a=0

    c = 0
    for i in range(n-1, -1, -1):
        if s[i] == 'B':
            cMp[i] = c
        elif s[i] == 'C':
            c+=1
        else:
            c=0

    for i in range(n):
        if s[i] != 'B':
            continue
        res += max(aMp[i], cMp[i])

    print(res)


t = int(input())
for i in range(t):
    solve()




# haha, the brute force solution is easy to come up for a fourth question
def solve():
    n = int(input())
    s = input()


    res = 0
    for i in range(n):
        if s[i] != 'B':
            continue
        a, c = 0, 0
        j = i-1
        while j >= 0 and s[j] != 'C':
            if s[j] == 'A':
                a += 1
            j-=1

        j = i+1
        while j < n and s[j] != 'A':
            if s[j] == 'C':
                c+=1
            j+=1
        res += max(a, c)



    print(res)





t = int(input())
for i in range(t):
    solve()