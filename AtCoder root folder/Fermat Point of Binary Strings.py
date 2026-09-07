# damn! lets do it



def solve():
    n = int(input())
    A = input()
    B = input()
    C = input()

    ar, br, cr = [], [], []
    for i in range(2*n):
        if A[i] == '1': ar.append(i)
        if B[i] == '1': br.append(i)
        if C[i] == '1': cr.append(i)

    tp = []
    x = 0
    for i in range(n):
        a, b, c = sorted([ar[i], br[i], cr[i]])
        tp.append(b)
        x += b-a + c-b


    # print(tp)
    s = ['0']*(2*n)
    for i in tp: s[i] = '1'
    s = ''.join(s)
    print(x)
    print(s)



solve()