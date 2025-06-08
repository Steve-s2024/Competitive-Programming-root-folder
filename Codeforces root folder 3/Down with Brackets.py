#

def solve():
    s = input()
    n = len(s)
    stack = 0
    flag = False
    for i in range(n):
        if s[i] == '(':
            stack+=1
        else:
            stack-=1
            if stack == 0 and i != n-1:
                flag = True
                break

    if flag:
        print('Yes')
    else:
        print('No')
