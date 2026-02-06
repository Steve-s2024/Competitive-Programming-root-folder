# although I did realize quickly that the result must be
# between the maximum out of mixing w and b or one below
# the maximum out of mixing w and b, but it is still quite
# surprising it is always possible to build a valid triangle
# same as the maximum by building a in-valid triangle
import heapq, math

def solve():
    w, b = [int(e) for e in input().split()]
    sm = w+b
    x = int(math.sqrt(sm))
    while x*(x+1)//2 <= sm:
        x+=1
    while x*(x+1)//2 > sm:
        x-=1
    print(x)
t = int(input())
for tt in range(t):
    solve()