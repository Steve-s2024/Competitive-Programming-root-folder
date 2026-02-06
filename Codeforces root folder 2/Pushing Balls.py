# depricated
def solve():
    [n, m] = [int(e) for e in input().split(' ')]
    valid = set()
    flag = True
    for r in range(n):
        row = input()
        for c in range(m):
            if row[c] == '1':
                valid.add((r, c+1))
                valid.add((r+1, c))
            if row[c] == '1' and r != 0 and c != 0 and (r, c) not in valid:
                flag = False
          
    if flag:
        print('YES')
    else:
        print('NO')



t = int(input())
for tt in range(t):
  solve()
  
 

  