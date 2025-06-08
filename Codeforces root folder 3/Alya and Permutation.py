# funny question, the greedy solution requires some observation
# but overall the solution is neet
def test(arr):
    k = 0
    for i in range(len(arr)):
        if i%2 == 0:
            k &= arr[i]
        else:
            k |= arr[i]
    print(k)

def solve():
    n = int(input())

    res = [0] * n
    bi = str(bin(n))[2:]
    size = len(bi)
    st = set()
    if n == 5:
        res = [2, 1, 3, 4, 5]
    else:
        i = n-2 if n%2 == 1 else n-1
        tmp = 1 << (size-1)
        while tmp > 0:
            res[i] = tmp
            res[i-1] = tmp - 1
            st.add(tmp)
            st.add(tmp-1)
            tmp >>= 1
            i -= 2
        res[i+2] = 5
        st.add(5)
        i = 0
        cnt = 1
        while res[i] == 0:
            while cnt in st:
                cnt += 1
            res[i] = cnt
            st.add(cnt)
            i += 1
        res[-1] = n if n%2 == 1 else res[-1]

    test(res)
    print(' '.join([str(e) for e in res]))

t = int(input())
for i in range(t):
    solve()
