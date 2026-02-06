

# incorrect
def solve():
    n, k = [int(e) for e in input().split()]

    if k%2 == 1: res = [n]*k
    else:
        res = [n]*(k-2)
        s = str(bin(n))[2:]
        a, b = s, '0'
        for i in range(1, len(s)):
            if s[i] == '1':
                a = '0'
                b = s[:i] + '0'
                while len(a) < len(s):
                    if len(a) < i: a += '0'
                    else: a += '1'
                for j in range(i+1, len(s)):
                    if s[j] == '0': b += '1'
                    else: b += '0'
                break
        res.append(int(a, 2))
        res.append(int(b, 2))
    print(' '.join(str(e) for e in res))
    print(sum(res))
for _ in range(int(input())): solve()