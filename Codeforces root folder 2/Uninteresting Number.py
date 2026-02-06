# very very uninteresting question. but I did learn the fun fact about the result of 9 modulo any number.
from collections import defaultdict, deque, Counter
import heapq, math

def solve():
    s = input()
    remain = 0
    for c in s:
        remain += int(c)
    remain %= 9
    if remain != 0:
        cnt = {'3':0, '2':0}
        for c in s:
            if c in ['3', '2']:
                cnt[c] += 1
        two, six = cnt['2'], cnt['3']
        if remain == 3 and six > 0 or remain == 6 and six > 1:
            print('Yes')
        else:
            flag = False

            while two:
                remain += 2
                remain %= 9
                if remain == 0 or remain == 3 and six > 0 or remain == 6 and six > 1:
                    flag = True
                    break
                two -= 1
            
            print('Yes') if flag else print('No')

    else:
        print('Yes')


t = int(input())

for tt in range(t):
    solve()