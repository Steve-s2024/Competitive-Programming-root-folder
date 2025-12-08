# holy funny problem. absolutely no clue about the property of this kind of operation on a number. however, the problem
# is never meant to be solved by the normal approach, i realize I could just simulate the process by enumerate over all
# a and selecting all b's that satisfy the condition given. the trick here is that when a is fixed, I can force b
# to be in a small range (noted as bmi and bmx in the code) so that finding the b for each a is just constant time

# this question is the true paradigm of solving it by evading the intuitive approach and instead develop a magically
# functioning solution by manipulating the constraint and condition

def check(s1, s2):
    m = len(s2)
    n = len(s1)
    for i in range(n):
        if s1[i] != s2[i%m]: return False
    return True


def solve():
    n = int(input())
    s = str(n)
    l = len(s)
    ans = []
    for a in range(1, 10**4+1):
        size = len(str(n*a))
        bmi = max(1, l*a - size)
        bmx = min(l*a-1, n*a-1)
        for b in range(bmi, bmx+1):
            x = n*a-b
            ss = str(x)
            if l*a-b != len(ss): continue
            if check(ss, s): ans.append((a, b))
    print(len(ans))
    print('\n'.join(str(e[0]) + ' ' + str(e[1]) for e in ans))


t = int(input())
for i in range(t): solve()

