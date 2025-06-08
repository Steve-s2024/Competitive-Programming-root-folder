# cook your dish here
t = int(input())
for x in range(t):
    size = int(input())
    s = input()
    cnt = 0
    flag = False
    for c in s:
        if c not in 'aeiou':
            cnt += 1
            if cnt == 4:
                flag = True
                break
        else:
            cnt = 0
        
    if not flag:
        print("YES")
    else:
        print("NO")