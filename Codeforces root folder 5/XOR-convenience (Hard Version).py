# blablabla

def solve():
    n = int(input())
    if n.bit_count() == 1:
        print(-1)
        return

    ar = []
    for i in range(1, n, 2):
        ar.append(i+1)
        ar.append(i)

    ar = [ar.pop()] + ar
    if n%2 == 0: ar.pop()
    ar.append(0)

    if n%2 == 0:
        i, j = 0, n-(1<<(n.bit_length()-1))-1
        # print(i, j)
        ar[i], ar[j] = ar[j], ar[i]


    print(' '.join(str(e+1) for e in ar))




for _ in range(int(input())): solve()

