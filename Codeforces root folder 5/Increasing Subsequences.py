# ehhh... okay!


def solve():
    X = int(input())

    ar = []
    s = 1000
    i = 0
    while 1<<(i+1) <= X:
        if 1<<i & X and 1<<(i+1) <= X:
            ar.append(s)
            s -= 1

        ar.append(i)
        i += 1


    print(len(ar))
    print(*ar)

for _ in range(int(input())): solve()
