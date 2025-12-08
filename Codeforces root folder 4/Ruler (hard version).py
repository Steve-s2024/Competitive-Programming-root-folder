# first time practicing ternary search (upgrade of binary search), lucky enough to pass the testcase even though I am not sure about the
# implementation.

import sys
def query(a, b):
    print(f'? {a} {b}')
    sys.stdout.flush()
    return int(input())



def solve():
    l, r = 2, 999
    res = 999
    while l <= r:
        x = (r-l+1)//3
        m1, m2 = l+x, l+2*x
        a = query(m1, m2)
        if a == m1*m2: # search the third section
            l = m2+1
        elif a == m1*(m2+1): # search the middle section
            l = m1+1
            r = m2
            res = m2
        elif a == (m1+1)*(m2+1): # search the first section
            r = m1-1
            res = m1

    print(f'! {res}')

t = int(input())
for i in range(t): solve()

