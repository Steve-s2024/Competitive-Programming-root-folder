# ridiculous level of reasoning on bitwise operation

def query(a, b, c, d):
    print(f'? {a} {b} {c} {d}')
    stdout.flush()
    res = input()
    return res


def solve():
    n = int(input())
    j = 0
    for i in range(1, n):
        res = query(j, j, i, i)
        if res == '<': j = i


    x = j
    j = 0
    ar = [0]
    for i in range(1, n):
        res = query(j, x, i, x)
        if res == '<':
            j = i
            ar = [i]
        elif res == '=': ar.append(i)

    # print(x, ar)

    j = ar[0]
    for i in range(1, len(ar)):
        res = query(j, j, ar[i], ar[i])
        if res == '>': j = ar[i]
    print(f'! {j} {x}')

for _ in range(int(input())): solve()
