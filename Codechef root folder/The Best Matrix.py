# 置之死地而后生！！！！, can't solve stupid questions
# but this hard one is crashed by me!! 
from collections import defaultdict
# cook your dish here
t = int(input())
for tt in range(t):
    [n, m] = [int(e) for e in input().split(' ')]
    mat = []
    for r in range(n):
        mat.append([int(e) for e in input().split(' ')])
    # print(mat)
    mp1 = defaultdict(int)
    mp2 = defaultdict(int)
    mp3 = defaultdict(int)
    mp4 = defaultdict(int)
    for r in range(n):
        for c in range(m):
            cur = mat[r][c]
            d1, d2, d3, d4 = r+c, (n-1-r)+c, (n-1-r)+(m-1-c), r+(m-1-c)
            df1, df2, df3, df4 = cur-d1, cur-d2, cur-d3, cur-d4
            mp1[df1]+=1
            mp2[df2]+=1
            mp3[df3]+=1
            mp4[df4]+=1
    
    maxFit = max(max(mp1.values()), max(mp2.values()), max(mp3.values()), max(mp4.values()))
    print(m*n - maxFit)