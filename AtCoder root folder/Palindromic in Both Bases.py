
def checkPalin(s):
    l, r = 0, len(s)-1
    while l < r:
        if s[l] != s[r]: return False
        l += 1
        r -= 1
    return True

def getNumber(num, a):
    strarr = []
    while num:
        re = num%a
        strarr.append(str(re))
        num //= a
    return ''.join(strarr[::-1])

def solve():
    a = int(input())
    n = int(input())
    res = 0
    s = str(n)


    # print(int(s[:len(s)//2]))
    for i in range(1, int(s[:len(s)//2+(len(s)+1)%2])+1):
        cand1 = int(str(i) + str(i)[::-1])
        if cand1 < n and checkPalin(getNumber(int(cand1), a)):
            # print(cand1)
            res += cand1

        cand2 = int(str(i) + str(i)[::-1][1:])
        # print(cand1, cand2)
        if cand2 > n: break
        if checkPalin(getNumber(int(cand2), a)):
            # print(cand2)
            res += cand2

    print(res)

solve()