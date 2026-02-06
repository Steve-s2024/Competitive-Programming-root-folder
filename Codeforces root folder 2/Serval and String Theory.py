# case judging heavy question

def solve():
    n, k = [int(e) for e in input().split()]
    s = input()
    mp = Counter(s)
    flag = False
    for i in range(n//2):
        if s[i] < s[n-1-i]:
            flag = True
            break
        elif s[i] > s[n-1-i]:
            break

    if flag or (len(mp) != 1 and k != 0):
        print('Yes')
    else:
        print('No')


t = int(input())
for tt in range(t):
    solve()

