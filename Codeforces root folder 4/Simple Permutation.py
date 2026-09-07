# this easy? okay I guessed anyway

def solve():
    n = int(input())

    vs = [0]*(n//2+1)
    if n >= 5:
        for i in range(2, n//2+1):
            for j in range(i*i, n//2+1, i): vs[j] = 1

        for i in range(n//2, 1, -1):
            if vs[i] == 0:
                # print(i)
                ar = []
                x = i*2 - 1
                for j in range(1, i):
                    ar.append(j)
                    ar.append(x)
                    x -= 1
                ar.append(i)
                for j in range(i*2, n+1): ar.append(j)
                # print(ar)
                print(' '.join(map(str, ar)))
                return
    else:
        ar = [2, 1, 3, 4]
        print(' '.join(str(e) for e in ar[:n]))
        # print(ar[:n])
for _ in range(int(input())): solve()